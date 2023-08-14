#!/usr/bin/env bash

MODEL="TheBloke/airoboros-l2-70B-gpt4-1.4.1-GPTQ"
LOADER="ExLlama_HF"

echo "Worker Initiated"

echo "Symlinking files from Network Volume"
ln -s /runpod-volume /workspace

echo "Starting Oobabooga Text Generation Server"
cd /workspace/text-generation-webui
source /workspace/venv/bin/activate
pip install requests runpod==0.10.0
mkdir -p /workspace/logs
nohup python3 server.py \
  --listen \
  --api \
  --model ${MODEL} \
  --loader ${LOADER} \
  --listen-port 3000 \
  --api-blocking-port 5000 \
  --api-streaming-port 5005 &> /workspace/logs/textgen.log &

echo "Starting RunPod Handler"
export PYTHONUNBUFFERED=1
python -u /rp_handler.py
