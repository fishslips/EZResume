from make_html import *
from html_to_pdf import *

def main():
    # Load resume data from JSON
    resume_json_path = "./resume_jsons/default_resume.json"
    with open(resume_json_path, "r", encoding="utf-8") as file:
        resume = json.load(file)
    
    html_content = generate_full_html(resume)
    
    # Example: You could print it or write it to a file
    output_path = "./resume_html/html_out.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated HTML resume saved to {output_path}")

    # # Convert the HTML to PDF
    # css_path = "./css/style.css"
    # output_pdf_path = "./resume_pdf/resume.pdf"
    # html_to_pdf(output_path, css_path, output_pdf_path)
    # print(f"PDF resume saved to {output_pdf_path}")
    

if __name__ == "__main__":
    main()