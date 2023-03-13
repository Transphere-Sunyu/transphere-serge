import requests
import json
import argparse

def add_translation(project_id, api_key, locale, namespace, keys, translations):
    headers = {
        'Content-Type': 'application/json',
        'x-locize-projectid': project_id,
        'x-locize-apikey': api_key
    }

    data = {}
    for i in range(len(keys)):
        data[keys[i]] = translations[i]

    url = "https://api.locize.app/missing/" + project_id + "/latest/" + locale + "/" + namespace

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("Translation added successfully")
    else:
        print("Translation not added. Error code:", response.status_code)

def read_json(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
        keys = []
        translations = []
        for key, value in data.items():
            keys.append(key)
            translations.append(value)
        return keys, translations

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Add translations to Locize API')
    parser.add_argument('--project_id', required=True, help='The ID of your Locize project')
    parser.add_argument('--api_key', required=True, help='Your Locize API key')
    parser.add_argument('--locale', default='en', help='The locale for the translations (default: en)')
    parser.add_argument('--namespace', default='default', help='The namespace for the translations (default: default)')
    parser.add_argument('--file_name', default='translations.json', help='The name of the JSON file containing the translations (default: translations.json)')
    args = parser.parse_args()

    keys, translations = read_json(args.file_name)
    add_translation(args.project_id, args.api_key, args.locale, args.namespace, keys, translations)
