import json
from jinja2 import Environment, FileSystemLoader

def load_config():
    with open("./conf/conf.json", "r") as file:
        return json.load(file)
    
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
    conf = load_config()
    json_resume = conf.get("json_resume")
    template_path = conf.get("template_path")
    template_name = conf.get("template_name")
    out_path = conf.get("html_out_path")
    

    data = read_json(json_resume)
    generate_html(data, template_path, template_name, out_path)

if __name__ == "__main__":
    main()