#!/usr/bin/python3

def validUTF8(data):
    """ Returns True if data is a valid UTF-8 code"""
    number_bytes = 0

    mask_first = 1 << 7
    mask_second = 1 << 6
    for byte in data:
        