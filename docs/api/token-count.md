# Chat API

## Request

```json
{
  "input": {
    "api": {
      "method": "POST",
      "endpoint": "/token-count"
    },
    "payload": {
      "prompt": "Please give me a step-by-step guide on how to plant a tree in my backyard."
    }
  }
}
```

## Response

### RUN

```json
{
    "id": "83bbc301-5dcd-4236-9293-a65cdd681858",
    "status": "IN_QUEUE"
}
```

### RUNSYNC

```json
{
    "delayTime": 15955,
    "executionTime": 322,
    "id": "sync-ea3d89bf-c29a-43bb-a465-a516e145b47e",
    "output": {
        "results": [
            {
                "tokens": 22
            }
        ]
    },
    "status": "COMPLETED"
}
```