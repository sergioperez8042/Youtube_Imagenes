#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from urllib import response
import requests


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youtube_search.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


client_id = '94f6223e3d12ebc97496'
client_secret = 'bc3cef87db608b19a880b6da7ed24fb67025fa08'
code = 'e17ae0634f7c88d4a277'

if __name__ == '__main__':
    url = ' https://github.com/login/oauth/access_token'
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code
    }
    headers = {'Accept': 'application/json'}
    response = requests.post(url, json=params, headers=headers)

    main()
