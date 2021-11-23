# Pytest with Lambda
A very simple example for testing lambda function with pytest (no calls to AWS services, just testing of functions and the handler).

# Setup
```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Test function
```
pytest tests/test_sample.py

Output:

====================================================== test session starts ======================================================
platform linux -- Python 3.9.5, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /mnt/c/Users/shuraosipov/git/examples/pytest_examples
collected 2 items                                                                                                               

tests/test_sample.py ..
```

