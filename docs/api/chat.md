# Chat API

## Request

```json
{
  "input": {
    "api": {
      "method": "POST",
      "endpoint": "/chat"
    },
    "payload": {
      "user_input": "Please give me a step-by-step guide on how to plant a tree in my backyard."
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
    "delayTime": 20275,
    "executionTime": 43997,
    "id": "sync-a3b54383-e671-4e24-a7bd-c5fec16fda3b",
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
    },
    "status": "COMPLETED"
}
```