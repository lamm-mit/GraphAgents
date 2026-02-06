# GraphAgents 📈: Knowledge Graph-Guided Agentic AI for Cross-Domain Materials Design 

#### Isabella A. Stewart, Tarjei Hage, Yu-Chuan (Michael) Hsu, and Markus J. Buehler, MIT, 2025 
Corresponding author: mbuehler@MIT.EDU

#### LAMM, Massachusetts Institute of Technology

## Summary 

How can scientific knowledge be meaningfully connected across domains as the volume of information continues to grow? While Large Language Models (LLMs) offer promise for accelerating discovery, the core challenge has shifted from information access to cross-domain integration—an issue that is especially pronounced in materials science, where advances require linking molecular chemistry to macroscopic performance. Neither human researchers nor single-agent LLMs can effectively manage this complexity, with the latter often exhibiting brittle reasoning and hallucinations.

To address this limitation, we introduce a multi-agent framework in which agents can traverse and reason over large-scale knowledge graphs encoding diverse materials science properties. We evaluate this capability on a challenging scientific task: identifying sustainable alternatives to per- and polyfluoroalkyl substances (PFAS), a widely used class of synthetic chemicals under increasing regulatory scrutiny. Within the framework, specialized agents handle problem decomposition, evidence retrieval, design parameter extraction, and graph-based reasoning, enabling the discovery of latent connections that support hypothesis generation for PFAS-free materials. Ablation studies demonstrate that the full multi-agent pipeline outperforms single-shot prompting, while adaptive graph traversal strategies balance focused, exploitative searches with broader exploratory discovery. Using biomedical tubing as a case study, the framework generates PFAS-free material candidates that jointly optimize performance, stability, chemical resistance, and biocompatibility, illustrating a general, graph-driven approach for expanding the materials design space through multi-agent reasoning.

## Contributions:

1. Novel graph traversal strategies for creative exploration, including Breadth-First Search, Depth-First Search, and a Semantic-Stop criterion.
2. Agent-based methods for uncovering latent connections: (i) the Hybrid GraphWeave agent, which integrates and links concepts within existing textual evidence, and (ii) the Creative GraphWeave agent, which forges previously unobserved conceptual connections.
3. A knowledge graph on the material properties of PFAS and a second graph on the broader PFAS domain.

<img width="1459" height="581" alt="Overview_img" src="https://github.com/user-attachments/assets/274af413-bcf3-4432-9936-04d82fc5ff96" />





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

## Supplementary
All supplementary files may be found in the `Experiments` folder including graphs. 


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
