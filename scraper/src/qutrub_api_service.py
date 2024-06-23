import requests
import requests_cache
import subprocess
import json

requests_cache.install_cache('qutrub_cache', expire_after=None)

def call_qutrub_api(verb):
    url = f"https://qutrub.arabeyes.org/api?verb={verb}&haraka=u&trans=1"

    try:
        response = requests.get(url)
        response.raise_for_status() 

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error calling Qutrub API: {e}")
        return None


def pretty_print_json(json_data):
    json_str = json.dumps(json_data)
    process_pbcopy = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    process_pbcopy.communicate(input=json_str)
