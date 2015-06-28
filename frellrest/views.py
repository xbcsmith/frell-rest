from pyramid.view import view_config

_templates = { 'default': 'default_template',
               'foo': 'foo_template',
               'bar': 'bar_template',
               'buz': 'buz_template',
            }

@view_config(route_name='fetch', renderer='json')
def fetch(request):
    name = request.matchdict.get('name') or 'default'
    return _templates.get(name) 

@view_config(route_name='templates', renderer='json')
def templates(request):
    return _templates
