import pdfkit
config = pdfkit.configuration(wkhtmltopdf='C:\\Users\\surfl\\Downloads\\wkhtmltox-0.12.5-1.mxe-cross-win32.7z')

pdfkit.from_file('computerInformation.html', 'computerinfo.pdf', configuration= config)