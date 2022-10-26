from html import escape
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config


#http://localhost:6543/

@view_config(route_name='home')
def home_view(request):
    return Response('<p>Cliquer <a href="/view2?name=noemie">ici</a> pour vous faire saluer</p>')


# /howdy?name=alice which links to the next view

@view_config(route_name='hello')
def hello_view(request):
    name = request.params.get('name')
    body = '<p>Bonjour %s,<br>Cliquez <a href="/">ici</a> pour revenir à l\'ancienne vue </p>'
    # Python html.escape to prevent Cross-Site Scripting (XSS) [CWE 79]
    return Response(body % escape(name))
