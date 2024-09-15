from PyPDF2 import PdfWriter, PdfReader
import sys

args = sys.argv
arg_len = len(sys.argv)

pages_to_delete = [ int(args[i]) for i in range(1, arg_len - 1)]
pdf = args[arg_len - 1]
print(f"Input: {pdf}")
print(f"Pages to delete: {pages_to_delete}")
infile = PdfReader(pdf, 'rb')
output = PdfWriter()

for i in range(len(infile.pages)):
    if i not in pages_to_delete:
        p = infile.pages[i]
        output.add_page(p)

pdf_name, pdf_ext = pdf.split(".")
with open(f'{pdf_name}-out.{pdf_ext}', 'wb') as f:
    output.write(f)
