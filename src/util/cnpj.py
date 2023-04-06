"""CNPJ Util"""


def process(cnpj):
    """Process CNPJ"""
    return (
        cnpj.replace("-", "")
        .replace(".", "")
        .replace(" ", "")
        .replace("/", "")
    )
