def bytes_to_int(ba, a):
    ia = [ba[a + i] for i in range(4)]
    return ia[0] | (ia[1] << 8) | (ia[2] << 16) | (ia[3] << 24)


def zero_fill_right_shift(val, n):
    return (val % 0x100000000) >> n


def string_to_code_value(val):
    return val.lower().replace(" ", "_")


def get_base_byte_value(b, bf):
    return (b // bf) * bf
