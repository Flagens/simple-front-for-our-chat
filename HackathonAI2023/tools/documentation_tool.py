from langchain.tools import BaseTool
from HackathonAI2023.globals import Globals
from HackathonAI2023 import config
from HackathonAI2023.code_splitter import CodeSplitter
from HackathonAI2023.objects.indexed_object import IndexedObject
from HackathonAI2023.file_descriptor import FileDescriptor
from HackathonAI2023.code_descriptor import CodeDescriptor
from HackathonAI2023.git_manager import GitManager
from HackathonAI2023.descripted_file import DescriptedFile


class DocumentTool(BaseTool):
    name: str = "DescriptionTool"
    description: str = "Use this tool only when asked to document code."

    def _run(self, query: str) -> str:
        Globals.used_tool_message = "Documentation created at project location"

        splitter = CodeSplitter(config.PROJECT_REPO_LOCATION)

        split_contents = splitter.to_indexed_objects()
        # CodeSplitter.print_indexed_objects(split_contents)
        paths = [IndexedObject.create_object("abc", path="agent_manager.py"),
                 IndexedObject.create_object("abc", path="code_descriptor.py")
                 ]

        paths = GitManager.get_all_files_in_directory(config.PROJECT_REPO_LOCATION)
        new_paths = []
        for path in paths:
            new_paths.append(IndexedObject.create_object("", path=path))

        file_descriptor = FileDescriptor(new_paths)
        desc_file = file_descriptor.describe()
        code_descriptor = CodeDescriptor(split_contents, desc_file)
        desc_code = code_descriptor.describe()
        DescriptedFile.initialize_documents(DescriptedFile.get_ai_doc_location(), desc_code)
        return "Documentation created at project location"
