#!/usr/bin/env python3
from util import post_request


def get_response_output(resp_json):
    print(resp_json['output']['results'])


if __name__ == '__main__':
    payload = {
        "input": {
            "api": {
                "method": "POST",
                "endpoint": "/stop-stream"
            },
            "payload": {
            }
        }
    }

    get_response_output(post_request(payload, 'runsync'))
