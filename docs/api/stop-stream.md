# Chat API

## Request

```json
{
  "input": {
    "api": {
      "method": "POST",
      "endpoint": "/stop-stream"
    },
    "payload": {
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
    "delayTime": 15451,
    "executionTime": 318,
    "id": "sync-aec3ad39-4245-4713-a764-4c766562af9f",
    "output": {
        "results": "success"
    },
    "status": "COMPLETED"
}
```