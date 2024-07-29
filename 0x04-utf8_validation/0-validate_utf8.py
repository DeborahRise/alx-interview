#!/usr/bin/python3

def validUTF8(data):
    """ Returns True if data is a valid UTF-8 encode
    else: You know whatsup
    """
    number_bytes = 0

    mask_first = 1 << 7
    mask_second = 1 << 6
    for byte in data:
        mask = 1 << 7
        if number_bytes == 0:
            while mask & byte:
                number_bytes += 1
                mask = mask >> 1
            if number_bytes == 1 or number_bytes > 4:
                return False
        else:
            if not (byte & mask_first and not (byte & mask_second)):
                return False
        number_bytes -= 1
    return number_bytes == 0