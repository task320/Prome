import os
from jinja2 import Environment, PackageLoader#, select_autoescape
from flask import url_for
import Run

class HtmlRender():
    @classmethod
    def render(cls, template_file, param):
        env = Environment(
            loader=PackageLoader('templates', ''),
            #autoescape=select_autoescape(['html'])
        )
        env.globals['url_for'] = cls.dated_url_for

        template = env.get_template(template_file)
        return template.render(param = param)

    @staticmethod
    def dated_url_for(endpoint, **values):
        if endpoint == 'static':
            filename = values.get('filename', None)
            if filename:
                file_path = os.path.join(Run.app.root_path,
                                        endpoint, filename)
                values['q'] = int(os.stat(file_path).st_mtime)
        return url_for(endpoint, **values)