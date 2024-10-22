from spire.doc import *
from spire.doc.common import *

def doctxt(FilePath: str):
    # Create a Document object
    document = Document()
    # Load a Word document
    document.LoadFromFile(FilePath)

    # Extract the text of the document
    document_text = document.GetText()

    # Write the extracted text into a text file
    with open("src/AutoRes/resources/resume.txt", "w", encoding="utf-8") as file:
        file.write(document_text)

    document.Close()