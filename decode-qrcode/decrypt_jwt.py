import jwt

public_key = '''-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAxwI0izb2Zn5GBLUop/Az
yE9+79xkF4J7m+Nw9nOqTPixtg6fiKvlH7Mqz+NarljTvWjMVm9MGuf2GcmXNmIh
WzjUyj7Wq5EOQPRAQykbM6ekjsXGUa/P2TLlVoogFxlipMD0ge1AFaBcOlZ+Ov+y
oJS7qYw3w0577nnHIupZB1YAbPo8ZeOYQCkiU6UiTe9SaCBLpUFuIZdrcvoGWs3k
BRz60UtIswMIuYFj1JaK9EGdpEhoTc114yDx6IFtTOccGBMN32Ysw4IVlWJ2iiIW
uKJRvUjXbYsu42hokW3lHd9N/djt7qL+l2vM1dDyi9TG+zhuBS8hOGWU1GCZPtik
VFQUjAaHJ33xaDE3qtkUw7nK/wIPYJNqJqVDQoQk7oGpRZYIh6sVuDc1CFeMj/9V
wGKD+X32SW4ZOs+hEojaAeDw0a/TSGbsy1lodZvLwAPFLvgsNovF6YOL6LbMremK
NP119ghYfnCL968+osTPY89ZWQQ/SdBf8ixU8doYAX2OWJ0e9EqUrORkmW1qdOpZ
dUl7RkDpRJ/zjK7yuKymFAKFiQadmKISHGhjSdTAdvgtFLJDb0RKsltiWNCO3aVc
pT3t+JL+ltg83nsSNvclAKPAPL0NRchHwah0k+nn4rGdEKZvWJAEDOE5yMXZSBIb
61DZHDpnI2oIaAguh4jEBOsCAwEAAQ==
-----END PUBLIC KEY-----'''

def decrypt(token):
    dec = jwt.decode(token, public_key, verify = True, algorithms=['RS256'])
    return dec
