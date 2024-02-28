#!/usr/bin/env bash

MODEL="LoneStriker/Air-Striker-Mixtral-8x7B-Instruct-ZLoss-3.75bpw-h6-exl2"

echo "Running Python version:"
python3 --version

echo "Worker Initiated"

echo "Symlinking files from Network Volume"
ln -s /runpod-volume /workspace

echo "Starting Oobabooga Text Generation Server"
cd /workspace/text-generation-webui
source /workspace/venv/bin/activate
mkdir -p /workspace/logs
nohup python3 server.py \
  --listen \
  --api \
  --model ${MODEL} \
  --loader exllamav2_hf \
  --listen-port 3000 \
  --api-blocking-port 5000 \
  --api-streaming-port 5005 &> /workspace/logs/textgen.log &

echo "Starting RunPod Handler"
export PYTHONUNBUFFERED=1
python3 -u /rp_handler.py