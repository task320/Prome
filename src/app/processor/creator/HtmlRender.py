from jinja2 import Environment, PackageLoader, select_autoescape

def render(template_file, response):
    env = Environment(
        loader=PackageLoader('templates', ''),
        #autoescape=select_autoescape(['html'])
    )

    template = env.get_template(template_file)
    return template.render(response = response)
