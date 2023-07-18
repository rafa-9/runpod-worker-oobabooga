#!/usr/bin/env python3
import json
import requests
import time
from dotenv import dotenv_values


def get_response_output(resp_json):
    print(json.dumps(resp_json['output']['result'], indent=4, default=str))


if __name__ == '__main__':
    # Load the .env file which contains the following:
    # RUNPOD_API_KEY=YOUR_API_KEY
    # SERVERLESS_ENDPOINT_ID=YOUR_ENDPOINT_ID
    env = dotenv_values('.env')
    runpod_api_key = env.get('RUNPOD_API_KEY')
    serverless_endpoint_id = env.get('SERVERLESS_ENDPOINT_ID')
    runpod_endpoint_base_url = f'https://api.runpod.ai/v2/{serverless_endpoint_id}'

    # Create the payload dictionary
    payload = {
        "input": {
            "api": {
                "method": "POST",
                "endpoint": "/model"
            },
            "payload": {
                "action": "info"
            }
        }
    }

    r = requests.post(
        f'{runpod_endpoint_base_url}/run',
        headers={
            'Authorization': f'Bearer {runpod_api_key}'
        },
        json=payload
    )

    print(f'Status code: {r.status_code}')

    if r.status_code == 200:
        resp_json = r.json()

        if 'output' in resp_json and 'results' in resp_json['output']:
            get_response_output(resp_json)
        elif 'output' in resp_json and 'errors' in resp_json['output']:
            print(f'ERROR: {json.dumps(resp_json["output"]["errors"], indent=4, default=str)}')
        else:
            job_status = resp_json['status']
            print(f'Job status: {job_status}')

            if job_status == 'IN_QUEUE' or job_status == 'IN_PROGRESS':
                request_id = resp_json['id']
                request_in_queue = True

                while request_in_queue:
                    r = requests.get(
                        f'{runpod_endpoint_base_url}/status/{request_id}',
                        headers={
                            'Authorization': f'Bearer {runpod_api_key}'
                        }
                    )

                    print(f'Status code from RunPod status endpoint: {r.status_code}')

                    if r.status_code == 200:
                        resp_json = r.json()
                        job_status = resp_json['status']

                        if job_status == 'IN_QUEUE' or job_status == 'IN_PROGRESS':
                            print(f'RunPod request {request_id} is {job_status}, sleeping for 5 seconds...')
                            time.sleep(5)
                        elif job_status == 'FAILED':
                            request_in_queue = False
                            print(f'RunPod request {request_id} failed')
                        elif job_status == 'CANCELLED':
                            request_in_queue = False
                            print(f'RunPod request {request_id} cancelled')
                        elif job_status == 'COMPLETED':
                            request_in_queue = False
                            print(f'RunPod request {request_id} completed')
                            get_response_output(resp_json)
                        elif job_status == 'TIMED_OUT':
                            request_in_queue = False
                            print(f'ERROR: RunPod request {request_id} timed out')
                        else:
                            request_in_queue = False
                            print(f'ERROR: Invalid status response from RunPod status endpoint')
                            print(json.dumps(resp_json, indent=4, default=str))
            elif job_status == 'COMPLETED' and 'errors' in resp_json['output']:
                print(f'ERROR: {json.dumps(resp_json["output"]["errors"], indent=4, default=str)}')
            else:
                print(json.dumps(resp_json, indent=4, default=str))
    else:
        print(f'ERROR: {r.content}')
