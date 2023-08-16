#!/usr/bin/env python3
from util import post_request


def get_response_output(resp_json):
    result = resp_json['output']['results']

    if len(result):
        print(result[0]['tokens'])


if __name__ == '__main__':
    payload = {
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

    get_response_output(post_request(payload, 'runsync'))
