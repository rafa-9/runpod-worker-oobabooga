GENERATE_SCHEMA = {
    'prompt': {
        'type': str,
        'required': True
    },
    'max_new_tokens': {
        'type': int,
        'required': False,
        'default': 250,
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
        'default': 0,
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
    'num_beams': {
        'type': int,
        'required': False,
        'default': 1,
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
