# MODNet
Docker version API for MODNet-model Human Matting

> Convert images on api !

The webapp is deployed Divio-Online here - https://modnet.us.aldryn.io/

The webapp is deployed Divio-Test here - https://modnet-stage.us.aldryn.io/

The webapp is deployed Heroku here - https://modnet-demo.herokuapp.com/

The webapp is deployed Aliyun Severless here - 

The webapp is deployed AWS Lambda here - 


---

## What is this?

- Original address of the project[MODNet](https://github.com/ZHKKKe/MODNet)
- The project used by this version[MODNet Onnx](https://github.com/manthan3C273/MODNet/)

## Update
[Use the associated applications of the model](https://github.com/LiteraturePro/Wx-Photo/)

### Explain
MODNet-model Human Matting(Look at the picture)

![](https://pcdn.wxiou.cn/20210221141938.png)
![](https://pcdn.wxiou.cn/20210301145423.png)


> This project is to package the matting program implemented by modnet algorithm as docker image to provide API calling service. If you don't know modnet, please read the original author's warehouse first. What I'm going to talk about is to use docker to build modnet as an API for calling. Of course, you can also directly run the `app.py` in the form of flash. Docker is used to avoid configuration environment errors.
> Modnet can run on GPU or CPU. This project can use GPU or CPU.


## Compiled project on [hub.docker.com](https://hub.docker.com/)

- [Normal version](https://hub.docker.com/layers/literature/modnet-matting/latest/images/sha256-65e14b60a5c155eec1d3607806456d5a269a169f7c4fdd5c760846fc0b0c3eb4?context=repo)
- [Heroku version](https://hub.docker.com/layers/literature/modnet-matting/heroku/images/sha256-c3465a45ed6655969851f5e7fb5438c7837063b6143164672fded4cbf1a0e4f2?context=repo)
- [Aliyun version](https://hub.docker.com/layers/literature/modnet-matting/sf/images/sha256-ec3423318458b00d342950a5c40061c16636f5875319bf33b6afe86b65389a51?context=repo)
## Build
> Make sure you have `docker` installed

1. Clone the MODNet repository:
    ```
    git clone https://github.com/LiteraturePro/MODNet.git
    cd MODNet
    ```
2. Input command to build image：
    ```
    docker build -t mod-matting .
    ```
    - I also provided the compilation command for `Heroku`, just replace the last command of dockerfile file with each other,
    - For general
    ```
    CMD exec gunicorn --bind 0.0.0.0:8080 --workers 1 --threads 8 --timeout 0 app:app
    ```
    - For heroku
    ```
    CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 app:app
    ```
    - For Aliyun Severless
    - For Alibaba cloud functional computing service, it specifies that the service must run on port 9000, so two locations need to be changed, one of which is as follows
    ```
    CMD exec gunicorn --bind 0.0.0.0:9000 --workers 1 --threads 8 --timeout 0 app:app
    ```
    - The other one needs to be changed `app.py` Change `8080` in to `9000` port
    
3. Running image (You can specify the running port yourself)：
    ```
    docker run -p 8080:8080 mod-matting
    ```
## Install
> Make sure you have `docker` installed

I have built the image and can install it directly. The installation command is as follows(You can specify the running port yourself)：
- For general
    ```
    docker pull literature/modnet-matting:latest
    docker run -p 8080:8080 literature/modnet-matting:latest
    ```
- For heroku
    ```
    docker pull literature/modnet-matting:heroku
    ```
    [Please see the specific tutorial for installing container application in heroku](https://github.com/LiteraturePro/Cartoonize#using-heroku)

- For Aliyun Serverless
    ```
    docker pull literature/modnet-matting:sf
    ```
    [Please see the specific tutorial for installing container application in Aliyun Serverless](https://github.com/LiteraturePro/Cartoonize#using-aliyun-severless)
    
Now your service has started to run, but it runs on the local port. If you need to realize the external network call, you need to act as an agent to proxy the service to your domain name，


## Use
> The call I have shown is based on the agent I have done. If you need to call it, you need to do it yourself

- provided that you have installed `docker`. After you deploy correctly, both `GET` and `POST` requests can be accessed. The actual display is as follows
  - `Interface`: `http://your domain/api` or `http://127.0.0.1:8080/api` can be accessed.
  - `Parameter`: image  `value`: a picture
  - `Return value`: the base64 data stream after processing the image
![](https://pcdn.wxiou.cn/20210221141131.png)
![](https://pcdn.wxiou.cn/20210221141230.png)

## Other
  Thanks for the work of the original author and the revised author. If you like, please give a `star`.








