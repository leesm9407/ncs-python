from dataclasses import dataclass

@dataclass
class FileReader(object):
    context: str = ''
    fname: str = ''
    train: object = None
    test: object = None
    id: str = ''
    label: str = ''