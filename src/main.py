from ruamel.yaml import YAML
from make_html import *

def main():
    yaml = YAML(typ="rt")
    with open("./conf/conf.yaml", "r", encoding="utf-8") as file:
        conf = yaml.load(file)
        # Assuming your YAML configuration has entries 'yaml_resume' and 'html_out_path'
        yaml_resume = conf["yaml_resume"]
        html_out_path = conf["html_out_path"]

    # Load resume data from YAML
    with open(yaml_resume, "r", encoding="utf-8") as file:
        resume = yaml.load(file)
        

    html_content = generate_full_html(resume)

    # Write the generated HTML to a file
    with open(html_out_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Generated HTML resume saved to {html_out_path}")

if __name__ == "__main__":
    main()
