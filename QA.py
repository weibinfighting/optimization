def encode(x_0):
    x_0 = bin(x_0)
    return x_0


def decode(x_0):
    x_0 = int(x_0, 10);
    return x_0

def turnbio(str):
    if str == '1':
        x = '0';
    else:
        x = '1';
    return x
