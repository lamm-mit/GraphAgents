# GRAPHAGENTS 📈: Knowledge Graph-Guided Agentic AI for Cross-Domain Materials Design 

#### Isabella Stewart, Tarjei Hage, Yu-Chuan (Michael) Hsu, and Markus J. Buehler, MIT, 2025 
Corresponding author: mbuehler@MIT.EDU

#### LAMM, Massachusetts Institute of Technology

![Overview](https://github.com/user-attachments/assets/8a26f952-9efa-4d14-98b4-29fb34fe4ad9)


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
