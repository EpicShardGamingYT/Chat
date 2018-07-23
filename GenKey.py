from werkzeug.serving import make_ssl_devcert
make_ssl_devcert('Keys/ssl', host='localhost')