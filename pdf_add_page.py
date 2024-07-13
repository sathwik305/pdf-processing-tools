from PyPDF2 import PdfReader, PdfWriter

def add_pages_to_pdf(original_pdf, pages_to_add_pdf, output_pdf):
    # Create PDF readers
    original_reader = PdfReader(original_pdf)
    pages_to_add_reader = PdfReader(pages_to_add_pdf)
    
    # Create a PDF writer
    writer = PdfWriter()
    
    # Add pages from the original PDF
    for page in original_reader.pages:
        writer.add_page(page)
    
    # Add pages from the PDF to be added
    for page in pages_to_add_reader.pages:
        writer.add_page(page)
    
    # Write the output PDF
    with open(output_pdf, 'wb') as output_file:
        writer.write(output_file)

# File paths
original_pdf = r"path\to\original.pdf"
pages_to_add_pdf = r"path\to\pages_to_add.pdf"
output_pdf = r"path\to\output.pdf"

# Add pages to the PDF
add_pages_to_pdf(original_pdf, pages_to_add_pdf, output_pdf)

print("Pages have been added successfully.")