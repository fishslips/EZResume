import json
from jinja2 import Environment, FileSystemLoader

def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def generate_html(data, template_path, template_name, output_path):
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template(template_name)
    html = template.render(data)
    
    with open(output_path, 'w') as file:
        file.write(html)

def main():
    json_file_path = './resume_jsons/tim_severance_resume.json'
    template_path = './html_templates/'
    template_name = 'jinja_template.html'
    output_path = './resume_html/resume.html'
    
    data = read_json(json_file_path)
    generate_html(data, template_path, template_name, output_path)

if __name__ == "__main__":
    main()