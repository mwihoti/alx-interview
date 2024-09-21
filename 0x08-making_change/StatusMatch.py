#!/usr/bin/python3
"""
Match http request status
"""

def http_error(status):
    match status:
        case 400:
            return 'Bad Request'
        case 404:
            return 'Not Found'
        case 418:
            return "I'm a teapot"
        case _:
            return 'Somethng went wrong!'

print(http_error(400))