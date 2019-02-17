# Skripsi

### Prerequisites
- NVIDIA GPU (Tesla T4 or equivalent)
- Ubuntu 18.04
- [CUDA Toolkit 10.0](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1804&target_type=debnetwork)
- [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1)
- [nvidia-docker](https://github.com/NVIDIA/nvidia-docker)

### Setup and start
Build an image and run the container:
```
mkdir /temp && cd /temp
git clone https://github.com/eufat/dockerfiles.git && cd dockerfiles/jupyter-keras-gpu
nvidia-docker build -t jupyter-gpu .
cd /root && git clone https://github.com/eufat/skripsi.git
nvidia-docker run -it -d --mount type=bind,source=/root/skripsi/,target=/notebooks/skripsi -p 8888:8888 -p 6006:6006 --name skripsi jupyter-gpu
```
To start the container you have been built:
```
nvidia-docker start skripsi
```
(Note: add this command on your remote server startup script)

### JupyterLab
Open `localhost:8888/lab` or `server_ip_address:8888/lab` when using remote server (allow port 8888 in remote server firewall first).

### TensorBoard
Run `tensorboard --logdir=/notebooks/logs --host 0.0.0.0` inside container or in JupyterLab terminal. Open `localhost:6006` or `server_ip_address:6006` when using remote server (allow port 6006 in remote server firewall first).
