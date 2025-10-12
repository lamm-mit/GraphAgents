from GraphReasoning.graph_tools import *
from GraphReasoning.utils import *
from GraphReasoning.graph_analysis import *

from IPython.display import display, Markdown
import pandas as pd
import numpy as np
import networkx as nx
import os

from langchain.text_splitter import RecursiveCharacterTextSplitter
from pathlib import Path
import random
from pyvis.network import Network
from tqdm.notebook import tqdm

import seaborn as sns

from hashlib import md5


palette = "hls"
# Code based on: https://github.com/rahulnyk/knowledge_graph


def documents2Dataframe(documents) -> pd.DataFrame:
    rows = []
    for chunk in documents:
        row = {
            "text": chunk,
            "chunk_id": md5(chunk.encode()).hexdigest(),
        }
        rows = rows + [row]

    df = pd.DataFrame(rows)

    return df


def df2Graph(df: pd.DataFrame, generate, generate_figure=None, image_list=None, repeat_refine=0, do_distill=True, verbatim=False,
          
            ) -> nx.DiGraph:
    
    subgraph_list = []
    for _, row in df.iterrows():
        subgraph = graphPrompt(
            row.text, 
            generate,
            generate_figure, 
            image_list,
            {"chunk_id": row.chunk_id}, 
            do_distill=do_distill,
            repeat_refine=repeat_refine, 
            verbatim=verbatim,
        )
        print(subgraph, type(subgraph))
        subgraph_list.append(subgraph)

        
    G = nx.DiGraph()

    for g in subgraph_list:
        G = nx.compose(G, g)
    
    return G


import sys
sys.path.append("..")

import json

def graphPrompt(input: str, generate, generate_figure=None, image_list=None, metadata={}, #model="mistral-openorca:latest",
                do_distill=True, repeat_refine=0,verbatim=False,
               ) -> nx.DiGraph:
    
    try:
        return nx.read_graphml(f"temp/{metadata['chunk_id']}.graphml")
    except:
        pass

    os.makedirs('temp', exist_ok = True) 

    SYS_PROMPT_DISTILL = f'You are provided with a context chunk (delimited by ```) Your task is to respond with a concise scientific heading, summary, and a bullited list to your best understaninding and all of them should include reasoning. You should ignore human-names, references, or citations.'
    
    USER_PROMPT_DISTILL = f'In a matter-of-fact voice, rewrite this ```{input}```. The writing must stand on its own and provide all background needed, and include details. Ignore references. Extract the table if you think this is relevant and organize the information. Focus on scientific facts and includes citation in academic style if you see any.'
        
    SYS_PROMPT_FIGURE = f'You are provided a figure that contains important information. Your task is to analyze the figure very detailedly and report the scientific facts in this figure. If this figure is not an academic figure you should return "". Always return the full image location.'
    
    USER_PROMPT_FIGURE = f'In a matter-of-fact voice, rewrite this ```{input}```. The writing must stand on its own and provide all background needed, and include details. Extract the image if you think this is relevant and organize the information. Focus on scientific facts and includes citation in academic style if you see any.'
    input_fig = ''
    if generate_figure: # if image in the chunk
        
        for image_name in image_list:
            _image_name = image_name.split('/')[-1]
            if _image_name.lower() in input.lower():  
                input_fig =  f'Here is the information in the image: {image_name}' + \
                generate_figure( image = image_name, system_prompt=SYS_PROMPT_FIGURE, prompt=USER_PROMPT_FIGURE)
    
    if do_distill:
        #Do not include names, figures, plots or citations in your response, only facts."
        input = generate( system_prompt=SYS_PROMPT_DISTILL, prompt=USER_PROMPT_DISTILL)

    if input_fig:
        input += input_fig
    
    SYS_PROMPT_GRAPHMAKER = (
        'You are a network ontology graph maker who extracts terms and their relations from a given context, using category theory. '
        'You are provided with a context chunk (delimited by ```) Your task is to extract the ontology of terms mentioned in the given context, representing the key concepts as per the context with well-defined and widely used names of materials, systems, methods.'
        'You always report a technical term or abbreviation and keep it as it is.'
        'If you receive a location to an image, you must use it as a node which <id> will be the location and the <type> will be "image" and relate the information in the context to make the nodes and edges relation.'
        '<relation> in an edge must truly reveal important information that can provide scientific insight from the <source> to the <target>'
        'Return a JSON with two fields: <nodes> and <edges>.\n'
        'Each node must have <id> and <type>.\n'
        'Each edge must have <source>, <target>, and <relation>.'
    )
     
    USER_PROMPT = f'Context: ```{input}``` \n\ Extract the knowledge graph in structured JSON: '
    # result = [dict(item, **metadata) for item in result]
    
    print ('Generating triples...')
    result  =  generate( system_prompt=SYS_PROMPT_GRAPHMAKER, prompt=USER_PROMPT)

    G = nx.DiGraph()
    for node in result.nodes:
        G.add_node(node.id, type=node.type)
    for edge in result.edges:
        G.add_edge(edge.source, edge.target, relation=edge.relation, chunk_id=metadata['chunk_id'])

    nx.write_graphml(G, f"temp/{metadata['chunk_id']}.graphml")
    print(f'Generated graph: {G}')

    return G

# def colors2Community(communities) -> pd.DataFrame:
    
#     p = sns.color_palette(palette, len(communities)).as_hex()
#     random.shuffle(p)
#     rows = []
#     group = 0
#     for community in communities:
#         color = p.pop()
#         group += 1
#         for node in community:
#             rows += [{"node": node, "color": color, "group": group}]
#     df_colors = pd.DataFrame(rows)
#     return df_colors
#
def make_graph_from_text (txt,generate, generate_figure=None, image_list=None,
                          graph_root='graph_root',
                          chunk_size=2500,chunk_overlap=0,do_distill=True,
                          repeat_refine=0,verbatim=False,
                          data_dir='./data_output_KG/',
                          save_HTML=False,
                          save_PDF=False,#TO DO
                         ):    
    
    ## data directory
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)     
    graph_GraphML=  f'{data_dir}/{graph_root}.graphml'  #  f'{data_dir}/result.graphml',

    try:
        G = nx.read_graphml(graph_GraphML)
    except:

        outputdirectory = Path(f"./{data_dir}/") #where graphs are stored from graph2df function
        
    
        splitter = RecursiveCharacterTextSplitter(
            #chunk_size=5000, #1500,
            chunk_size=chunk_size, #1500,
            chunk_overlap=chunk_overlap,
            length_function=len,
            is_separator_regex=False,
        )
        
        pages = splitter.split_text(txt)
        print("Number of chunks = ", len(pages))
        if verbatim:
            display(Markdown (pages[0]) )
        
        df = documents2Dataframe(pages)
        df.to_csv(f'{data_dir}/{graph_root}_chunks_clean.csv')

        G = df2Graph(df,generate, generate_figure, image_list, do_distill =do_distill, repeat_refine=repeat_refine,verbatim=verbatim) #model='zephyr:latest' )

        nx.write_graphml(G, graph_GraphML)
        

    graph_HTML = None
    net= None
    output_pdf = None
    if save_HTML:
        net = Network(
                notebook=True,
                cdn_resources="remote",
                height="900px",
                width="100%",
                select_menu=True,
                filter_menu=False,
            )

        net.from_nx(G)
        net.force_atlas_2based(central_gravity=0.015, gravity=-31)

        net.show_buttons()

        graph_HTML= f'{data_dir}/{graph_root}.html'
        net.save_graph(graph_HTML,
                )
        if verbatim:
            net.show(graph_HTML,
                )


        if save_PDF:
            output_pdf=f'{data_dir}/{graph_root}.pdf'
            pdfkit.from_file(graph_HTML,  output_pdf)
        
    
    return graph_HTML, graph_GraphML, G, net, output_pdf

import time
from copy import deepcopy

def add_new_subgraph_from_text(txt=None,generate=None,generate_figure=None, image_list=None, 
                               node_embeddings=None,tokenizer=None, model=None, original_graph=None,
                               data_dir_output='./data_temp/',graph_root='graph_root',
                               chunk_size=10000,chunk_overlap=2000,
                               do_update_node_embeddings=True, do_distill=True,
                               do_simplify_graph=True,size_threshold=10,
                               repeat_refine=0,similarity_threshold=0.95,
                               do_Louvain_on_new_graph=True, 
                               #whether or not to simplify, uses similiraty_threshold defined above
                               return_only_giant_component=False,
                               save_common_graph=False,G_to_add=None,
                               graph_GraphML_to_add=None,
                               verbatim=True,):

    display (Markdown(txt[:32]+"..."))
    graph_GraphML=None
    G_new=None
    
    res=None
    # try:
    start_time = time.time() 

    if verbatim:
        print ("Now create or load new graph...")

    if (G_to_add is not None and graph_GraphML_to_add is not None):
        print("G_to_add and graph_GraphML_to_add cannot be used together. Pick one or the other to provide a graph to be added.")
        return
    elif graph_GraphML_to_add==None and G_to_add==None: #make new if no existing one provided
        print ("Make new graph from text...")
        _, graph_GraphML_to_add, G_to_add, _, _ =make_graph_from_text (txt,generate,
                                 data_dir=data_dir_output,
                                 graph_root=f'graph_root',
                                 chunk_size=chunk_size, chunk_overlap=chunk_overlap,
                                 repeat_refine=repeat_refine, 
                                 verbatim=verbatim,
                                 )
        if verbatim:
            print ("New graph from text provided is generated and saved as: ", graph_GraphML_to_add)
    elif G_to_add is None:
        if verbatim:
            print ("Loading or using provided graph... Any txt data provided will be ignored...:", G_to_add, graph_GraphML_to_add)
            G_to_add = nx.read_graphml(graph_GraphML_to_add)
    # res_newgraph=graph_statistics_and_plots_for_large_graphs(G_to_add, data_dir=data_dir_output,                                      include_centrality=False,make_graph_plot=False,                               root='new_graph')
    print("--- %s seconds ---" % (time.time() - start_time))
    # except:
        # print ("ALERT: Graph generation failed...")
        
    print ("Now grow the existing graph...")
    
    # try:
    #Load original graph
    if type(original_graph) == str:
        G = nx.read_graphml(original_graph)
    else:
        G = deepcopy(original_graph)
    print(G, G_to_add)
    G_new = nx.compose(G, G_to_add)

    if do_update_node_embeddings:
        if verbatim:
            print ("Now update node embeddings")
        node_embeddings=update_node_embeddings(node_embeddings, G_new, tokenizer, model, verbatim=verbatim)

    if do_simplify_graph:
        if verbatim:
            print ("Now simplify graph.")
        G_new, node_embeddings =simplify_graph (G_new, node_embeddings, tokenizer, model , 
                                                similarity_threshold=similarity_threshold, use_llm=False, data_dir_output=data_dir_output,
                                verbatim=verbatim,)


    if size_threshold >0:
        if verbatim:
            print ("Remove small fragments")            
        G_new=remove_small_fragents (G_new, size_threshold=size_threshold)
        node_embeddings=update_node_embeddings(node_embeddings, G_new, tokenizer, model, verbatim=verbatim)

    if return_only_giant_component:
        if verbatim:
            print ("Select only giant component...")   
        connected_components = sorted(nx.connected_components(G_new), key=len, reverse=True)
        G_new = G_new.subgraph(connected_components[0]).copy()
        node_embeddings=update_node_embeddings(node_embeddings, G_new, tokenizer, model, verbatim=verbatim)

    if do_Louvain_on_new_graph:
        G_new=graph_Louvain (G_new, graph_GraphML=None)
        if verbatim:
            print ("Done Louvain...")

    if verbatim:
        print ("Done update graph")

    graph_GraphML= f'{data_dir_output}/{graph_root}_integrated.graphml'
    if verbatim:
        print ("Save new graph as: ", graph_GraphML)

    nx.write_graphml(G_new, graph_GraphML)
    if verbatim:
        print ("Done saving new graph")
    
    # res=graph_statistics_and_plots_for_large_graphs(G_new, data_dir=data_dir_output,include_centrality=False,make_graph_plot=False,root='assembled')
    # print ("Graph statistics: ", res)

    # except:
        # print ("Error adding new graph.")
    print(G_new, graph_GraphML)
        # print (end="")

    return graph_GraphML, G_new, G_to_add, node_embeddings, res
