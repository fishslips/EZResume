# from weasyprint import HTML

# def html_to_pdf(html_path, css_path, output_pdf_path):
#     # Load HTML and CSS from local files
#     with open(html_path, 'r') as html_file:
#         html_content = html_file.read()

#     with open(css_path, 'r') as css_file:
#         css_content = css_file.read()

#     # Create a WeasyPrint HTML object
#     html = HTML(string=html_content)

#     # Render the PDF with the provided CSS
#     pdf = html.write_pdf(stylesheets=[css_content])

#     # Save the PDF to the output path
#     with open(output_pdf_path, 'wb') as output_pdf:
#         output_pdf.write(pdf)
