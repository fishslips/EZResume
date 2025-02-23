from make_html import *

def main():

    with open("./conf/conf.json", "r", encoding="utf-8") as file:
        conf = json.load(file)
        json_resume = conf["json_resume"]
        html_out_path = conf["html_out_path"] 
    # Load resume data from JSON
    
    with open(json_resume, "r", encoding="utf-8") as file:
        resume = json.load(file)
    
    html_content = generate_full_html(resume)
    
    # Example: You could print it or write it to a file
    with open(html_out_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated HTML resume saved to {html_out_path}")

    # # Convert the HTML to PDF
    # css_path = "./css/style.css"
    # output_pdf_path = "./resume_pdf/resume.pdf"
    # html_to_pdf(output_path, css_path, output_pdf_path)
    # print(f"PDF resume saved to {output_pdf_path}")
    

if __name__ == "__main__":
    main()