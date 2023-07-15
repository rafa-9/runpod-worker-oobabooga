#!/usr/bin/env python3
import json

USER_INPUT = 'Please give me a step-by-step guide on how to plant a tree in my backyard.'


if __name__ == '__main__':
    # Create the payload dictionary
    payload = {
        "input": {
            "user_input": USER_INPUT
        }
    }

    # Save the payload to a JSON file
    with open('test_input.json', 'w') as output_file:
        json.dump(payload, output_file)

    print('Payload saved to: test_input.json')

