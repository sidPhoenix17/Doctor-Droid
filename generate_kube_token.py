import os
import time
import json

import subprocess

create_run = subprocess.run(["kubectl", "create", "serviceaccount", "drdroid"],  stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
create_output = create_run.stdout

get_run = subprocess.run(["kubectl", "get", "serviceaccounts", "drdroid", "-o", "json"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
get_output = get_run.stdout

get_output_json = json.loads(get_output)
# print(get_output_json)

secret_name = get_output_json.get('secrets', [])[0].get('name', None)
if not secret_name:
	print('Trouble creating service account')

describe_run = subprocess.run(["kubectl", "describe", "secret", secret_name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
describe_output = describe_run.stdout

describe_output_token = list(filter(lambda x: x.startswith('token:'), str(describe_output).split('\\n')))[0].replace('token:', '').strip()

print('### - This is your Kube token that you need to pass when droid configure asks for Kube Token... ###')
print(describe_output_token)
	