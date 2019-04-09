import os
from jinja2 import Environment, PackageLoader#, select_autoescape
from flask import url_for
import Run

def render(template_file, response):
    env = Environment(
        loader=PackageLoader('templates', ''),
        #autoescape=select_autoescape(['html'])
    )
    env.globals['url_for'] = dated_url_for

    template = env.get_template(template_file)
    return template.render(response = response)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(Run.app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)