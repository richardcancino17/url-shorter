import string
import random

KEY = '0893478NASDUYASKKDASJDNMXNbxnashasdh788727HhwuHhJ898'


def build_key_url_shorter(size):
    key = ''.join(random.choice(KEY) for _ in range(size))
    return key


def url_generator_shorter(size=6):
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase + \
            build_key_url_shorter(size)
    return ''.join(random.choice(chars) for _ in range(size))
