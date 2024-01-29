from pypdf import PdfMerger
import sys

args = sys.argv
arg_len = len(sys.argv)

pdfs = [ args[i] for i in range(1, arg_len - 1)]
result_name = args[arg_len - 1]
print(pdfs)
print(result_name)

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write(result_name)
merger.close()
