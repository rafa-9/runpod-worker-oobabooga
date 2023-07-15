#!/usr/bin/env bash

echo "Worker Initiated"

echo "Starting RunPod Handler"
export PYTHONUNBUFFERED=1
source /workspace/runpod-worker-oobabooga/venv/bin/activate
cd /workspace/runpod-worker-oobabooga
python -u rp_handler.py
