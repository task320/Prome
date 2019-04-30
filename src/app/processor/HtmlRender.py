import os
from jinja2 import Environment, PackageLoader#, select_autoescape
from flask import url_for

class HtmlRender():
    @classmethod
    def render(cls, template_file, param):
        env = Environment(
            loader=PackageLoader('templates', ''),
            #autoescape=select_autoescape(['html'])
        )
        env.globals['url_for'] = url_for

        template = env.get_template(template_file)
        return template.render(param = param)