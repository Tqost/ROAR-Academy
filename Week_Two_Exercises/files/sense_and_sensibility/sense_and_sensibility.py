import PyPDF2
import os


script_path = os.path.dirname(os.path.abspath(__file__))
sense_and_sensibility_file = "Sense-and-Sensibility-by-Jane-Austen.pdf"
sense_and_sensibility_handle = open(
    script_path + "/" + sense_and_sensibility_file, "rb"
)
pdfReader = PyPDF2.PdfReader(sense_and_sensibility_handle)
page_number_total = len(pdfReader.pages)
frequency_table = {}
list_adjuster = 0

for page_index in range(page_number_total):
    current_page = pdfReader.pages[page_index]
    page_string = current_page.extract_text()
    page_list = list(page_string)
    for i in range(len(page_list)):
        if page_list[i] in [".", ",", ";", "/", "-"]:
            page_list[i] = " "
        # if page_list[i + list_adjuster] in [".", ",", ";", "/"]:
        #     page_list.pop(i + list_adjuster)
        #     list_adjuster -= 1
        # if page_list[i + list_adjuster] == "-":
        #     if page_list[i + list_adjuster + 1] == "-":
        #         page_list[i + list_adjuster] = " "
        #         page_list.pop(i + list_adjuster + 1)
        #         list_adjuster -= 1
        #     else:
        #         page_list[i + list_adjuster] = " "
    # list_adjuster = 0
    page_list = "".join(page_list)
    page_list = page_list.split()
    if "CHAPTER" in page_list:
        page_list.remove("CHAPTER")
    for i in range(len(page_list)):
        if page_list[i + list_adjuster].isalpha():
            page_list[i + list_adjuster] = page_list[i + list_adjuster].lower()
        else:
            page_list.pop(i + list_adjuster)
            list_adjuster -= 1
    list_adjuster = 0
    for i in range(3):
        page_list.pop(0)
    for i in page_list:
        if i in frequency_table:
            frequency_table[i] += 1
        else:
            frequency_table[i] = 1
sorted_frequency_table = dict(
    sorted(frequency_table.items(), key=lambda item: item[1], reverse=True)
)
print(sorted_frequency_table)
