
def generate_basics_section(resume):
    basics = resume.get("basics", {})
    if not basics:
        return ""
    html = '<section id="basics">\n'
    html += f"  <h1>{basics.get('name', '')}</h1>\n"
    contact = basics.get("contact", {})
    html += "  <div class='contact'>\n"
    if "email" in contact:
        html += f"    <p>{contact['email']}</p>\n"
    if "phone" in contact:
        html += f"    <p>{contact['phone']}</p>\n"
    if "address" in contact:
        html += f"    <p>{contact['address']}</p>\n"
    social = contact.get("social", [])
    if social:
        html += "    <ul class='social'>\n"
        for network in social:
            html += f"      <li><a href='{network.get('url', '#')}'>{network.get('display', '')}</a></li>\n"
        html += "    </ul>\n"
    html += "  </div>\n"
    html += "  <hr>\n"
    if "summary" in basics:
        html += f"  <p class='summary'>{basics['summary']}</p>\n"
    html += "</section>\n"
    return html

def generate_education_section(resume):
    education = resume.get("education", [])
    if not education:
        return ""
    
    html = "<section id='education'>\n  <h2>Education</h2>\n  <hr>\n"
    for school in education:
        html += "  <div class='education-item'>\n"
        html += f"    <h3>{school.get('institution', '')}</h3>\n"
        html += f"    <p>{school.get('year')}</p>\n"
        html += f"    <p><em>{school.get('degree', '')}</em></p>\n"
        if school.get("courses"):
            courses = ", ".join(school["courses"])
            html += f"    <p>Courses: {courses}</p>\n"
        if "gpa" in school:
            html += f"    <p>GPA: {school['gpa']}</p>\n"
        if school.get("honors"):
            honors = ", ".join(school["honors"])
            html += f"    <p>Honors: {honors}</p>\n"
        html += "  </div>\n"
    html += "</section>\n"
    return html

def generate_experience_section(resume):
    experience = resume.get("experience", [])
    if not experience:
        return ""

    html = "<section id='experience'>\n  <h2>Experience</h2>\n  <hr>\n"
    for exp in experience:
        html += "  <div class='experience-item'>\n"
        html += f"    <h3>{exp.get('organization', '')} - {exp.get('title', '')}</h3>\n"
        html += f"    <p>{exp.get('start_date', '')} to {exp.get('end_date', '')}</p>\n"
        highlights = exp.get("highlights", [])
        if highlights:
            html += "    <ul>\n"
            for point in highlights:
                html += f"      <li>{point}</li>\n"
            html += "    </ul>\n"
        html += "  </div>\n"
    html += "</section>\n"
    return html

def generate_skills_section(resume):
    skills = resume.get("skills", {})
    if not skills:
        return ""
    
    html = "<section id='skills'>\n  <h2>Skills</h2>\n  <hr>\n"
    for category, items in skills.items():
        html += f"  <h3>{category.replace('_', ' ').title()}</h3>\n"
        html += "  <p>" + ", ".join(items) + "</p>\n"
    html += "</section>\n"
    return html

def generate_projects_section(resume):
    projects = resume.get("projects", [])
    if not projects:
        return ""

    html = "<section id='projects'>\n  <h2>Project Experience</h2>\n  <hr>\n"
    for project in projects:
        html += "  <div class='project-item'>\n"
        html += f"    <h3>{project.get('name', '')}</h3>\n"
        # Dates are now directly below the project title.
        html += f"    <p>{project.get('start_date', '')} to {project.get('end_date', '')}</p>\n"
        html += f"    <p class='project-description'>{project.get('description', '')}</p>\n"
        technologies = project.get("technologies", [])
        if technologies:
            html += "    <div class='project-technologies'>\n"
            html += "      <span class='tech-label'>Skills:</span>\n"
            for tech in technologies:
                html += f"      <span class='tech-item'>{tech}</span>\n"
            html += "    </div>\n"
        highlights = project.get("highlights", [])
        if highlights:
            html += "    <ul>\n"
            for point in highlights:
                html += f"      <li>{point}</li>\n"
            html += "    </ul>\n"
        html += "  </div>\n"
    html += "</section>\n"
    return html

def generate_publications_section(resume):
    publications = resume.get("publications", [])
    if not publications:
        return ""

    html = "<section id='publications'>\n  <h2>Publications</h2>\n  <hr>\n"
    for pub in publications:
        html += "  <div class='publication-item'>\n"
        html += f"    <h3><a href='{pub.get('url', '#')}'>{pub.get('title', '')}</a></h3>\n"
        # Publication date moved directly under the title.
        html += f"    <p>Publication Date: {pub.get('publication_date', '')}</p>\n"
        html += f"    <p>Authors: {', '.join(pub.get('authors', []))}</p>\n"
        html += f"    <p>Publisher: {pub.get('publisher', '')}</p>\n"
        html += "  </div>\n"
    html += "</section>\n"
    return html

def generate_certifications_section(resume):
    certifications = resume.get("certifications", [])
    if not certifications:
        return ""
    html = "<section id='certifications'>\n  <h2>Certifications</h2>\n  <hr>\n"
    for cert in certifications:
        html += "  <div class='certification-item'>\n"
        html += f"    <h3>{cert.get('name', '')}</h3>\n"
        # Date moved directly under the certification title.
        html += f"    <p>Date: {cert.get('date', '')}</p>\n"
        html += f"    <p>Institution: {cert.get('institution', '')}</p>\n"
        html += "  </div>\n"
    html += "</section>\n"
    return html

def apply_css(html, css_path):
    # Load CSS from a local file and apply it to the HTML string.
    with open(css_path, 'r') as css_file:
        css_content = css_file.read()
    html = html.replace("</head>", f"  <style>{css_content}</style>\n</head>")
    return html

def generate_full_html(resume):
    # Concatenate all section html strings into one full html document.
    html = "<!DOCTYPE html>\n<html lang='en'>\n<head>\n"
    html += "  <meta charset='UTF-8'>\n"
    html += "  <meta name='viewport' content='width=device-width, initial-scale=1.0'>\n"
    html += "  <title>Resume</title>\n"
    html += "</head>\n<body>\n"
    html += generate_basics_section(resume)
    html += generate_experience_section(resume)
    html += generate_projects_section(resume)
    html += generate_education_section(resume)
    html += generate_publications_section(resume)
    html += generate_certifications_section(resume)
    html += generate_skills_section(resume)
    html += "</body>\n</html>"
    html = apply_css(html, "./css/style.css")
    return html

