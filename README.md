# GRAPHAGENTS: KNOWLEDGE GRAPH–GUIDED AGENTIC AI FOR CROSS-DOMAIN MATERIALS DESIGN

#### Isabella Stewart, Tarjei Hage, Yu-Chuan (Michael) Hsu, and Markus J. Buehler, MIT, 2025 
Corresponding author: mbuehler@MIT.EDU

#### LAMM, Massachusetts Institute of Technology

1. Install cuda toolkit
2. Install llama-cpp-python
3. Install GraphReasoning package

## Environment Configuration:

## 

## 1) Create Environment

conda create -n LLM_GraphAgents python=3.11 -y
conda activate LLM_GraphAgents


## 2) Install CUDA (Recommended via Conda) 

Note: Ensure that the NVIDIA CUDA driver is already installed on your system before proceeding.

```
conda install -c "nvidia/label/cuda-12.6.0" cuda-toolkit cuda-nvcc -y --copy
```

## 3) (Optional) Install llama-ccpp-python
Required only if you intend to run models locally (≥ v0.2.0). 
You can skip this step if you’re using API-based LLMs.

```
CMAKE_ARGS="-DGGML_CUDA=on -DLLAVA_BUILD=on" FORCE_CMAKE=1 pip install git+https://github.com/abetlen/llama-cpp-python@v0.3.8 --verbose

```

## 4) Install GraphReasoning package
Once the repository has been cloned, proceed with the direct installation.
```
cd GraphReasoning
pip install .
```


## Citation

Please cite:

```bibtex
@article{stewart2025graphagents,
  title     = {GRAPHAGENTS: KNOWLEDGE GRAPH–GUIDED AGENTIC AI
FOR CROSS-DOMAIN MATERIALS DESIGN},
  author    = {x},
  journal   = {x},
  year      = {2025},
  doi       = {x}
}
