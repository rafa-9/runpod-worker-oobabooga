#!/usr/bin/env bash

MODEL="TheBloke/Pygmalion-13B-SuperHOT-8K-GPTQ"

echo "Worker Initiated"

echo "Symlinking files from Network Volume"
ln -s /runpod-volume /workspace

echo "Starting Oobabooga Text Generation Server"
source /workspace/text-generation-webui/venv/bin/activate
mkdir -p /workspace/logs
nohup python server.py \
  --listen \
  --api \
  --model ${MODEL} \
  --listen-port 3001 \
  --api-blocking-port 5001 \
  --api-streaming-port 5006 &> /workspace/logs/textgen.log &

echo "Starting RunPod Handler"
export PYTHONUNBUFFERED=1
python -u /rp_handler.py
