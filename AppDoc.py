from docx import Document
import re
from pathlib import Path

class AppDoc:
    def __init__(self, document_path:str|Path) -> None:
        self.doc = Document(document_path)

    def replace_string(self, paragraph, pattern: str, replacement: str) -> str:
        pattern = re.compile(pattern)
        return re.sub(pattern, replacement, paragraph.text)

    def replace_handler(self, company_name:str, job_name:str) -> None:
        ## Make this extendable by leveraging hydra/cookiecutter
        for paragraph in self.doc.paragraphs:
            paragraph.text = self.replace_string(paragraph, "{Company Name}", company_name)
            paragraph.text = self.replace_string(paragraph, "{Job Title}", job_name)
    def save(self, new_path):
        self.doc.save(new_path)
    
x = AppDoc("doc_test.docx")
x.replace_handler("Apple", "Janitor")
x.save("testing_class.docx")