from typing import List

from HackathonAI2023.objects.indexed_object import IndexedObject
from HackathonAI2023.openai_asker import OpenaiAsker
from HackathonAI2023.descripted_file import DescriptedFile


class FileDescriptor:
    def __init__(self, docs: List[IndexedObject]):
        self.docs = docs

    def describe(self):
        return tuple(map(lambda x: DescriptedFile(x.metadata["path"], OpenaiAsker.describe_file(x)), self.docs))
