import time
import requests
import runpod
from runpod.serverless.utils.rp_validator import validate
from runpod.serverless.modules.rp_logger import RunPodLogger
from requests.adapters import HTTPAdapter, Retry


session = requests.Session()
retries = Retry(total=10, backoff_factor=0.1, status_forcelist=[502, 503, 504])
session.mount('http://', HTTPAdapter(max_retries=retries))
logger = RunPodLogger()


INPUT_SCHEMA = {
    'user_input': {
        'type': str,
        'required': True
    },
    'max_new_tokens': {
        'type': int,
        'required': False,
        'default': 250,
    },
    'history': {
        'type': dict,
        'required': False,
        'default': {
            'internal': [],
            'visible': []
        }
    },
    'mode': {
        'type': str,
        'required': False,
        'default': 'instruct',
        'constraints': lambda model: model in [
            'chat',
            'chat-instruct',
            'instruct',
        ]
    },
    'character': {
        'type': str,
        'required': False,
        'default': 'Example'
    },
    'instruction_template': {
        'type': str,
        'required': False,
        'default': 'Vicuna-v1.1'
    },
    'your_name': {
        'type': str,
        'required': False,
        'default': 'You'
    },
    'regenerate': {
        'type': bool,
        'required': False,
        'default': False
    },
    '_continue': {
        'type': bool,
        'required': False,
        'default': False
    },
    'stop_at_newline': {
        'type': bool,
        'required': False,
        'default': False
    },
    'chat_generation_attempts': {
        'type': int,
        'required': False,
        'default': 1,
    },
    'chat-instruct_command': {
        'type': str,
        'required': False,
        'default': 'Continue the chat dialogue below. Write a single reply for the character "<|character|>".\n\n<|prompt|>'
    },
    'preset': {
        'type': str,
        'required': False,
        'default': 'None'
    },
    'do_sample': {
        'type': bool,
        'required': False,
        'default': True
    },
    'temperature': {
        'type': float,
        'required': False,
        'default': 0.7,
    },
    'top_p': {
        'type': float,
        'required': False,
        'default': 0.1,
    },
    'typical_p': {
        'type': float,
        'required': False,
        'default': 1,
    },
    'epsilon_cutoff': {
        'type': float,
        'required': False,
        'default': 0,
    },
    'eta_cutoff': {
        'type': float,
        'required': False,
        'default': 0,
    },
    'top_a': {
        'type': float,
        'required': False,
        'default': 0,
    },
    'repetition_penalty': {
        'type': float,
        'required': False,
        'default': 1.18,
    },
    'repetition_penalty_range': {
        'type': float,
        'required': False,
        'default': 1.18,
    },
    'top_k': {
        'type': float,
        'required': False,
        'default': 40,
    },
    'min_length': {
        'type': int,
        'required': False,
        'default': 0,
    },
    'no_repeat_ngram_size': {
        'type': int,
        'required': False,
        'default': 0,
    },
    'penalty_alpha': {
        'type': int,
        'required': False,
        'default': 0,
    },
    'length_penalty': {
        'type': int,
        'required': False,
        'default': 1,
    },
    'early_stopping': {
        'type': bool,
        'required': False,
        'default': False,
    },
    'mirostat_mode': {
        'type': int,
        'required': False,
        'default': 0,
    },
    'mirostat_tau': {
        'type': int,
        'required': False,
        'default': 5,
    },
    'mirostat_eta': {
        'type': float,
        'required': False,
        'default': 0.1,
    },
    'seed': {
        'type': int,
        'required': False,
        'default': -1,
    },
    'add_bos_token': {
        'type': bool,
        'required': False,
        'default': True,
    },
    'truncation_length': {
        'type': int,
        'required': False,
        'default': 2048,
    },
    'ban_eos_token': {
        'type': bool,
        'required': False,
        'default': False,
    },
    'skip_special_tokens': {
        'type': bool,
        'required': False,
        'default': True,
    },
    'stopping_strings': {
        'type': list,
        'required': False,
        'default': [],
    }
}


# ---------------------------------------------------------------------------- #
# Application Functions                                                        #
# ---------------------------------------------------------------------------- #
def wait_for_service(url):
    while True:
        try:
            requests.get(url)
            return
        except requests.exceptions.RequestException:
            print('Service not ready yet. Retrying...')
        except Exception as err:
            print(f'Error: {err}')

        time.sleep(0.2)


def run_inference(inference_request):
    response = session.post(
        url='http://127.0.0.1:5000/api/v1/chat',
        json=inference_request,
        timeout=600
    )

    return response.json()


# ---------------------------------------------------------------------------- #
# RunPod Handler                                                               #
# ---------------------------------------------------------------------------- #
def handler(event):
    validated_input = validate(event['input'], INPUT_SCHEMA)

    if 'errors' in validated_input:
        return {
            'errors': validated_input['errors']
        }

    return run_inference(validated_input['validated_input'])


if __name__ == '__main__':
    wait_for_service(url='http://127.0.0.1:5000/api/v1/model')
    logger.log('Oobabooga API is ready', 'INFO')
    logger.log('Starting RunPod Serverless...', 'INFO')
    runpod.serverless.start(
        {
            'handler': handler
        }
    )