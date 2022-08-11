from flask import Flask
from flask_cdn import CDN
import os

if_local = False if os.popen('hostname').read().replace('\n', '') == 'visafy_server' else True

if 'IF_EB' in os.environ and os.environ['IF_EB']:
    if_eb = True
    if 'DEVELOP' in os.environ and os.environ['DEVELOP']:
        if_local = True
    else:
        if_local = False
else:
    if_eb = False

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.do')
app.url_map.strict_slashes = False

app.config['CDN_HTTPS'] = True
app.config['CDN_DOMAIN'] = 'd19lykljep210s.cloudfront.net'
app.config['CDN_TIMESTAMP'] = False

CDN(app)

from visafy_frontend import routes