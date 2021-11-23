# content of test_sample.py
import json
from lambda_function import func, lambda_handler

def test_answer():
    assert func(3) == 4

def test_handler():
    response = {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    assert lambda_handler("some_event", "some_context") == response