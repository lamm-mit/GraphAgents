# Using LLMs and Knowledge graphs to search for PFAS Alternatives

#### Isabella Stewart, Yu-Chuan (Michael) Hsu, Tarjei Hage, Wei Lu, and Markus J. Buehler, MIT, 2025 
istewart@MIT.EDU, mkychsu@MIT.EDU, tphage@MIT.EDU, wl7@MIT.EDU, mbuehler@MIT.EDU

#### LAMM, Massachusetts Institute of Technology

1. Install cuda toolkit
2. Install llama-cpp-python
3. Install GraphReasoning package

## Environment:

# 1) We recommend installing cuda from conda. You should install cuda driver from Nvidia first.

```
conda install -c "nvidia/label/cuda-12.6.0" cuda-toolkit cuda-nvcc -y --copy
```

# 2) Install and run llama-cpp-python if you need (>=v0.2.0). You can skip if you run on APIs.

```
CMAKE_ARGS="-DGGML_CUDA=on -DLLAVA_BUILD=on" FORCE_CMAKE=1 pip install git+https://github.com/abetlen/llama-cpp-python@v0.3.8 --verbose

```

## 3)

```
cd GraphReasoning
pip install .
```
