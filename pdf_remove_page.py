from PyPDF2 import PdfReader, PdfWriter

def remove_page_from_pdf(input_pdf, output_pdf, page_to_remove):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    for i in range(len(reader.pages)):
        if i != page_to_remove:
            writer.add_page(reader.pages[i])

    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)

input_pdf = r"path\to\input.pdf"
output_pdf = r"path\to\output.pdf"
page_to_remove = 1  # Page index to remove (0-based index)

remove_page_from_pdf(input_pdf, output_pdf, page_to_remove)