#!/usr/bin/env bash

echo "Worker Initiated"

echo "Symlinking files from Network Volume"
ln -s /runpod-volume /workspace
rm -rf /root/.cache
ln -s /runpod-volume/.cache /root/.cache

echo "Starting RunPod Handler"
export PYTHONUNBUFFERED=1
source /workspace/runpod-worker-oobabooga/venv/bin/activate
cd /workspace/runpod-worker-oobabooga
python -u rp_handler.py
