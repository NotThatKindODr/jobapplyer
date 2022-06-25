from docx import Document
import re
from pathlib import Path
from enum import Enum
from cookiecutter.main import cookiecutter
from itertools import product
replacements ={
    "{Company Name}": "{{cookiecutter.company_name}}",
    "{Job Title}": "{{cookiecutter.job_title}}",
    "{Hiring Manager}": "{{cookiecutter.hiring_manager}}"
}

class AppDoc:
    def __init__(self, document_path:str|Path) -> None:
        self.doc = Document(document_path)

    def replace_string(self, paragraph, pattern: str, replacement: str) -> str:
        pattern = re.compile(pattern)
        return re.sub(pattern, replacement, paragraph.text)

    def replace_handler(self) -> None:
        ## Make this extendable by leveraging hydra/cookiecutter
        for paragraph, replacement in product(self.doc.paragraphs, replacements.items()):
            paragraph.text = self.replace_string(paragraph, replacement[0], replacement[1])
           
    def save(self, new_path):
        self.doc.save(new_path)


cover_letter_path = "{{cookiecutter.company_name}}" + "_" + "{{cookiecutter.job_title}}" + "_CL.docx"
x = AppDoc(cover_letter_path)
x.replace_handler()
x.save(cover_letter_path)