import PyPDF2

file_handle = open("Sense-and-Sensibility-by-Jane-Austen.pdf", "rb")
pdfReader = PyPDF2.PdfReader(file_handle)
frequency_table = {}
