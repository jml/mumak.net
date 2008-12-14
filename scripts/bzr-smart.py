import modpywsgi
from bzrlib.transport.http import wsgi

smart_server_app = wsgi.make_app(
    root='/srv/www/mumak.net/code',
    prefix='/code/',
    path_var='REQUEST_URI',
    readonly=True)

def handler(request):
    """Handle a single request."""
    wsgi_server = modpywsgi.WSGIServer(smart_server_app)
    return wsgi_server.run(request)

