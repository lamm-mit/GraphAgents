# GRAPHAGENTS: KNOWLEDGE GRAPH–GUIDED AGENTIC AI FOR CROSS-DOMAIN MATERIALS DESIGN

#### Isabella Stewart, Yu-Chuan (Michael) Hsu, Tarjei Hage, and Markus J. Buehler, MIT, 2025 

#### LAMM, Massachusetts Institute of Technology

1. Load modules
2. Install cuda toolkit with the commands below.
3. Install llama-cpp-python
4. Install graphreasoning package

## Environment:

```
conda create -n LLM python=3.11 -y
conda activate LLM
conda install -c "nvidia/label/cuda-12.6.0" cuda-toolkit cuda-nvcc -y --copy
CMAKE_ARGS="-DGGML_CUDA=on -DLLAVA_BUILD=on" FORCE_CMAKE=1 pip install git+https://github.com/abetlen/llama-cpp-python@v0.3.8 --verbose
```

## Installation

After git clone, install directly:
```
pip install .
```
 
