#!/usr/bin/python3
"""UTF-8 validation module"""


def validUTF8(data):
    """Determines if the given data is a valid UTF-8 encoding"""
    if any(val < 0 or val >= 256 for val in data):
        return False

    try:
        decoded_text = bytes(data).decode('utf-8')
        return True
    except UnicodeDecodeError:
        return False
