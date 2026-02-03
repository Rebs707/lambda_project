import json
from lambda_function import lambda_handler
event = {'text': 'Hello world from Lambda dry-run'}
result = lambda_handler(event, None)
print(result)
