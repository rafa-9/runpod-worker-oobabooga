# oobabooga | RunPod Serverless Worker

This is the source code for a [RunPod](https://runpod.io?ref=w18gds2n)
Serverless worker that uses [Oobabooga Text Generation](
https://github.com/oobabooga/text-generation-webui) API for
LLM text generation AI tasks.

## Model

The worker uses the [Pygmalion-13B-SuperHOT-8K-GPTQ](
https://huggingface.co/TheBloke/Pygmalion-13B-SuperHOT-8K-GPTQ)
model by [TheBloke](https://huggingface.co/TheBloke).  Feel free to fork
the repo and switch it to an alternate model.

## Building the Worker

There are two options:

1. Network Volume
2. Standalone

### Option 1: Network Volume

This will store your application on a Runpod Network Volume and
build a light weight Docker image that runs everything
from the Network volume without installing the application
inside the Docker image.

You can either launch a new pod with a Network Volume attached
by using my [Text Generation Web UI and API](
https://runpod.io/gsc?template=el5m58e1to&ref=w18gds2n) custom
[RunPod](https://runpod.io?ref=w18gds2n) template, or alternatively,
you can install it manually following instructions below.  If you
choose to use my custom template, it is **VERY IMPORTANT** to
ensure that you first create a Network Volume and then attach
it when launching the new pod in **Secure Cloud**.  You cannot
launch a pod with a Network Volume in Community Cloud.

1. [Create a RunPod Account](https://runpod.io?ref=w18gds2n).
2. Create a [RunPod Network Volume](https://www.runpod.io/console/user/storage).
3. Attach the Network Volume to a Secure Cloud [GPU pod](https://www.runpod.io/console/gpu-secure-cloud).
4. Select a light-weight template such as RunPod Pytorch.
5. Deploy the GPU Cloud pod.
6. Once the pod is up, open a Terminal and install the required
   dependencies if you have opted for a manual installation
   (you can skip to step 7 below if you have opted to use my
   custom template):
```bash
cd /workspace
git clone https://github.com/oobabooga/text-generation-webui.git
cd text-generation-webui
python3 -m venv /workspace/venv
source /workspace/venv/bin/activate
pip3 install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip3 install -r requirements.txt
bash -c 'for req in extensions/*/requirements.txt ; do pip3 install -r "$req" ; done'
mkdir -p repositories
cd repositories
git clone https://github.com/turboderp/exllama
pip3 install -r exllama/requirements.txt
export AUTOGPTQ_VERSION="0.2.2"
export CUDA_VERSION=""
export TORCH_CUDA_ARCH_LIST="8.0;8.6+PTX;8.9;9.0"
pip3 uninstall -y auto-gptq && \
    pip3 install --no-cache-dir auto-gptq==${AUTOGPTQ_VERSION}
```
7. Install the Serverless dependencies:
```bash
deactivate
cd /workspace/text-generation-webui
source /workspace/venv/bin/activate
pip3 install huggingface_hub runpod>=0.10.0
```
7. Download a model, for example `TheBloke/Pygmalion-13B-SuperHOT-8K-GPTQ`:
```bash
python3 download-model.py TheBloke/Pygmalion-13B-SuperHOT-8K-GPTQ \
  --output /workspace/text-generation-webui/models
```
8. Sign up for a Docker hub account if you don't already have one.
9. Build the Docker image on your local machine and push to Docker hub:
```bash
docker build -t dockerhub-username/runpod-worker-oobabooga:1.0.0 -f Dockerfile.Network_Volume .
docker login
docker push dockerhub-username/runpod-worker-oobabooga:1.0.0
```

### Option 2: Standalone

This is the simpler option.  No network volume is required.
The entire application will be stored within the Docker image
but will obviously create a more bulky Docker image as a result.

```bash
docker build -t dockerhub-username/runpod-worker-oobabooga:1.0.0 -f Dockerfile.Standalone .
docker login
docker push dockerhub-username/runpod-worker-oobabooga:1.0.0
```

## Dockerfile

There are 2 different Dockerfile configurations

1. Network_Volume - See Option 1 Above.
2. Standalone - See Option 2 Above (No Network Volume is required for this option).

The worker is built using one of the two Dockerfile configurations
depending on your specific requirements.

## API

The worker provides an API for inference. The API payload looks like this:

```json
{
  "input": {
    "user_input": "Please give me a step-by-step guide on how to plant a tree in my backyard."
  }
}
```

## Serverless Handler

The serverless handler (`rp_handler.py`) is a Python script that handles
inference requests.  It defines a function handler(event) that takes an
inference request, runs the inference using the [oobabooba](
https://github.com/oobabooga/text-generation-webui) Text Generation API,
and returns the output as a JSON response in the following format:

```json
{
  "output": {
     "results": [
        {
           "history": {
              "internal": [
                 [
                    "Please give me a step-by-step guide on how to plant a tree in my backyard.",
                    "Sure! First you need to dig a hole that is about 1 foot deep by 2 feet wide. Then put some soil into it so there are no air pockets inside of it. Next, place your seedling or sapling into the hole with its roots facing downwards. Finally, cover up the hole with more dirt until only the top few inches of the root ball remain exposed above ground level."
                 ]
              ],
              "visible": [
                 [
                    "Please give me a step-by-step guide on how to plant a tree in my backyard.",
                    "Sure! First you need to dig a hole that is about 1 foot deep by 2 feet wide. Then put some soil into it so there are no air pockets inside of it. Next, place your seedling or sapling into the hole with its roots facing downwards. Finally, cover up the hole with more dirt until only the top few inches of the root ball remain exposed above ground level."
                 ]
              ]
           }
        }
     ]
  }
}
```

## Acknowledgements

- [oobabooga](https://github.com/oobabooga/text-generation-webui)

## Community and Contributing

Pull requests and issues on [GitHub](https://github.com/ashleykleynhans/runpod-worker-oobabooga)
are welcome. Bug fixes and new features are encouraged.

You can contact me and get help with deploying your Serverless
worker to RunPod on the RunPod Discord Server below,
my username is **ashleyk**.

<a target="_blank" href="https://discord.gg/pJ3P2DbUUq">![Discord Banner 2](https://discordapp.com/api/guilds/912829806415085598/widget.png?style=banner2)</a>

## Appreciate my work?

<a href="https://www.buymeacoffee.com/ashleyk" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
