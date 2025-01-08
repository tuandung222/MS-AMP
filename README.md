# Create conda environment
```
conda create -n msamp python=3.10
conda activate msamp
```


# Install msccl
cd third_party/msccl

```
# A100
make -j src.build NVCC_GENCODE="-gencode=arch=compute_80,code=sm_80"

# H100
# make -j src.build NVCC_GENCODE="-gencode=arch=compute_90,code=sm_90"

apt-get update
apt install build-essential devscripts debhelper fakeroot cmake
make pkg.debian.build
dpkg -i build/pkg/deb/libnccl2_*.deb
dpkg -i build/pkg/deb/libnccl-dev_2*.deb

cd -
```


# Intall CUDA-toolkit to 24.6 for Ubuntu 22.04
```
# will be added later
```


# Update cuDNN library
```
apt-get -y install cudnn-cuda-12
```


# Install Apex
```
git clone https://github.com/NVIDIA/apex # uncomment if not already cloned
cd apex
# if pip >= 23.1 (ref: https://pip.pypa.io/en/stable/news/#v23-1) which supports multiple `--config-settings` with the same key... 
pip install -v --disable-pip-version-check --no-cache-dir --no-build-isolation --config-settings "--build-option=--cpp_ext" --config-settings "--build-option=--cuda_ext" ./
# otherwise
pip install -v --disable-pip-version-check --no-cache-dir --no-build-isolation --global-option="--cpp_ext" --global-option="--cuda_ext" ./
cd -
```


# Install my modified requirements
```
python3 -m pip install --upgrade pip
python3 -m pip install .
make postinstall
```


# Comment line 256 in torch.amp.grad_scaler.py
```
python3 comment.py
```


# Test MS-AMP installation
```
NCCL_LIBRARY=/usr/lib/x86_64-linux-gnu/libnccl.so # Change as needed
export LD_PRELOAD="/usr/local/lib/libmsamp_dist.so:${NCCL_LIBRARY}:${LD_PRELOAD}"
python3 -c "import msamp; print(msamp.__version__)"
```

