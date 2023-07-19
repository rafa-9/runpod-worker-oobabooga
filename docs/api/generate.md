# Chat API

## Request

```json
{
  "input": {
    "api": {
      "method": "POST",
      "endpoint": "/generate"
    },
    "payload": {
      "prompt": "In order to make homemade bread, follow these steps:\n1)"
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
  "delayTime": 15318,
  "executionTime": 27809,
  "id": "sync-ce2d3e58-6168-49c1-a038-9c62b369ae1e",
  "output": {
    "results": [
      {
        "text": " Mix the dry ingredients together in a large bowl. This includes flour, yeast, salt and any other spices you may want to add. Make sure that all of your ingredients are well mixed before moving on to step 2)."
      }
    ]
  },
  "status": "COMPLETED"
}
```