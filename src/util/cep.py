"""CEP Util"""


def process(cep):
    """Process CEP"""
    return cep.replace("-", "").replace(".", "").replace(" ", "")
