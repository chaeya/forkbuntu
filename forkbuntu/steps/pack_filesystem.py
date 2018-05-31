from ..step import Step
from munch import munchify
from os import path

class PackFilesystem(Step):
    messages = munchify({
        'past': 'packed filesystem',
        'present': 'packing filesystem',
        'cache': 'using packed filesystem cache'
    })
    requires = [
        'configure_filesystem'
    ]

    def run(self):
        s = self.app.services
        s.pack.filesystem()
