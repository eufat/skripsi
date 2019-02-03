# Skripsi

### Prerequisites
- NVIDIA GPU (Tesla T4 or equivalent)
- Ubuntu 16.04
- CUDA Toolkit 10.0
- nvidia-docker

### Setup and start
Build an image and run the container:
```
cd /temp
git clone https://github.com/eufat/dockerfiles.git
cd dockerfiles/jupyter-keras-gpu
nvidia-docker build -t jupyter-gpu .
nvidia-docker run -it -d --mount type=bind,source=/root/skripsi/,target=/notebooks/skripsi -p 8888:8888 -p 6006:6006 --name skripsi jupyter-gpu
```
To start the container you have been built:
```
nvidia-docker start skripsi
```
(Note: add this command on your remote server startup script)

### JupyterLab
Open `localhost:8888/lab` or `server_ip_address:8888/lab` when using remote server (allow port 8888 in remote server firewall).

### TensorBoard
Run `tensorboard --logdir=/notebooks/logs --host 0.0.0.0` inside container or in JupyterLab terminal. Open `localhost:6006` or `server_ip_address:6006` when using remote server (allow port 6006 in remote server firewall).
