from PyPDF2 import PdfReader, PdfWriter

def reorder_pages(input_pdf, output_pdf, order):
    # Create a PDF reader
    reader = PdfReader(input_pdf)
    
    # Create a PDF writer
    writer = PdfWriter()
    
    # Add pages to the writer in the specified order
    for page_num in order:
        writer.add_page(reader.pages[page_num])
    
    # Write the output PDF
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)

# File paths
input_pdf = r"path\to\input.pdf"
output_pdf = r"path\to\output.pdf"

# Specify the desired order of pages (0-based index)
# For example, to reorder the pages to be in the order: 2nd, 1st, 3rd
order = [0, 4, 1, 2, 3]

# Reorder the pages in the PDF
reorder_pages(input_pdf, output_pdf, order)

print("Pages have been reordered successfully.")