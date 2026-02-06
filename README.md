# GraphAgents 📈: Knowledge Graph-Guided Agentic AI for Cross-Domain Materials Design 

#### Isabella A. Stewart, Tarjei Hage, Yu-Chuan (Michael) Hsu, and Markus J. Buehler, MIT, 2025 
Corresponding author: mbuehler@MIT.EDU

#### LAMM, Massachusetts Institute of Technology

# Summary 

How can scientific knowledge be meaningfully connected across domains as the volume of information continues to grow? While Large Language Models (LLMs) offer promise for accelerating discovery, the core challenge has shifted from information access to cross-domain integration—an issue that is especially pronounced in materials science, where advances require linking molecular chemistry to macroscopic performance. Neither human researchers nor single-agent LLMs can effectively manage this complexity, with the latter often exhibiting brittle reasoning and hallucinations.

To address this limitation, we introduce a multi-agent framework in which agents can traverse and reason over large-scale knowledge graphs encoding diverse materials science properties. We evaluate this capability on a challenging scientific task: identifying sustainable alternatives to per- and polyfluoroalkyl substances (PFAS), a widely used class of synthetic chemicals under increasing regulatory scrutiny. Within the framework, specialized agents handle problem decomposition, evidence retrieval, design parameter extraction, and graph-based reasoning, enabling the discovery of latent connections that support hypothesis generation for PFAS-free materials. Ablation studies demonstrate that the full multi-agent pipeline outperforms single-shot prompting, while adaptive graph traversal strategies balance focused, exploitative searches with broader exploratory discovery. Using biomedical tubing as a case study, the framework generates PFAS-free material candidates that jointly optimize performance, stability, chemical resistance, and biocompatibility, illustrating a general, graph-driven approach for expanding the materials design space through multi-agent reasoning.

## ✨ Contributions

This repository introduces a set of methods and resources for creative knowledge discovery in the PFAS domain:

### 🔍 Graph Traversal for Creative Exploration
- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- **Semantic-Stop**: a stopping criterion guided by semantic relevance rather than depth alone

### 🤖 Agent-Based Discovery of Latent Connections
- **Hybrid GraphWeave Agent**  
  Connects related concepts grounded within existing textual evidence
- **Creative GraphWeave Agent**  
  Generates novel, previously unobserved conceptual links across the graph

### 🧠 PFAS Knowledge Graphs
- A knowledge graph capturing **material properties of PFAS**
- A complementary graph representing the **broader PFAS knowledge domain**

<img width="1459" height="581" alt="Overview_img" src="https://github.com/user-attachments/assets/274af413-bcf3-4432-9936-04d82fc5ff96" />

# GraphAgents

## Getting Started

1. Instantiate environment 
2. Install CUDA tooklit
3. Install llama-cpp-python
4. Install GraphReasoning package

## 1) Instantiate Environment Configuration:

```
conda create -n LLM_GraphAgents python=3.11 -y
conda activate LLM_GraphAgents
```

## 2) Install CUDA (Recommended via Conda) 

Note: Ensure that the NVIDIA CUDA driver is already installed on your system before proceeding.

```
conda install -c "nvidia/label/cuda-12.6.0" cuda-toolkit cuda-nvcc -y --copy
```

## 3) (Optional) Install llama-ccp-python
Required only if you intend to run models locally (≥ v0.2.0). 
You can skip this step if you’re using API-based LLMs.

```
CMAKE_ARGS="-DGGML_CUDA=on -DLLAVA_BUILD=on" FORCE_CMAKE=1 pip install git+https://github.com/abetlen/llama-cpp-python@v0.3.8 --verbose
```

## 4) Install GraphReasoning package and Environment Requirements 
Clone the repository and proceed with the direct installation.
```
git clone https://github.com/lamm-mit/GraphAgents.git
cd GraphAgents
pip install -r requirements.txt 
pip install .
```

# Graph Generation

Convert and run the Jupyter notebook to a Python script:

For full-paper extraction to generate our PFAS knowledge graph: 
```
jupyter nbconvert --to script make_KG_PFAS.ipynb
python make_KG_PFAS.py
```
For abstract extraction to generate our global material properties knowledge graph: 
```
jupyter nbconvert --to script make_KG_materialproperties.ipynb
python make_KG_materialproperties.py
```

While any model can be used,these notebooks support the approach described in our Methods section by using the Together API to provide hosted LLM inference with meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8 for graph generation



# Run GraphAgents  
Open and run the following notebook:
```
graphAgents.ipynb

```

As described in our Methods, the agents use the following generated kowledge graphs and embeddings stored in: 

Full-Paper PFAS knowledge graph: 
`/Experiments/GRAPHDATA_PFAS/PFAS_KG.graphml`
`/Experiments/GRAPHDATA_OUTPUT_PFAS/SG_LLAMA4_70b.pkl`

Abstract-based material properties knowledge graph: 
`/Experiments/GRAPHDATA_MATERIALPROPERTIES/MatProp_KG.graphml`
`/Experiments/GRAPHDATA_OUTPUT_MATERIALPROPERTIES/SG_LLAMA4_70b.pkl`



# Supplementary 
All output from the agentic pipeline as reported in our Results may be found in the `/Experiments/Supplementary` folder. 


To recreate our ablation studies please refer to: 
```
graphAgents_ablation.ipynb
```

## Citation

Please cite this work as:

```bibtex
@article{stewart2025graphagents,
  title     = {GRAPHAGENTS: KNOWLEDGE GRAPH–GUIDED AGENTIC AI
FOR CROSS-DOMAIN MATERIALS DESIGN},
  author    = {x},
  journal   = {x},
  year      = {2025},
  doi       = {x}
}
