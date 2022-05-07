from flask import render_template, request, redirect
from visafy_frontend import if_local
from visafy_frontend.util import *
from datetime import datetime
import urllib.parse
import locale
import uuid


locale.setlocale(locale.LC_ALL, "it_IT")


@app.context_processor
def inject_now():

    if 'sid' in request.cookies and request.cookies['sid']:
        sid = request.cookies['sid']
    else:
        sid = datetime.utcnow().strftime('%Y%m%d%H%M%S') + uuid.uuid4().hex[:11]

    # Initial source storing

    initial_source = ''

    if 'initialSource' in request.cookies:
        initial_source = urllib.parse.unquote(request.cookies['initialSource'])
    else:
        if 'gclid' in request.args and request.args['gclid']:
            initial_source = 'Google Ads'
        elif 'fbclid' in request.args and request.args['fbclid']:
            initial_source = 'Facebook'
        elif request.referrer:
            referrer_domain = request.referrer.split('/')[2]
            if not referrer_domain.startswith('localhost') and referrer_domain.startswith('localhost') and referrer_domain.startswith('127.0.0.1'):
                initial_source = referrer_domain

    # Internal id storing
    if 'internal_id' in request.cookies:
        internal_id = request.cookies['internal_id']
    elif 'internal_id' in request.args and request.args['internal_id']:
        internal_id = request.args['internal_id']
    else:
        internal_id = None

    return {'now': datetime.now(), 'if_local': if_local, 'sid': sid,
            'internal_id': internal_id, 'initial_source': initial_source}


@app.before_request
def clear_trailing():
    rp = request.path
    if rp != '/' and rp.endswith('/'):
        return redirect(rp[:-1], code=301)


@app.route('/')
def frontend_home():
    return render_template('index.html',
                           title='Visafy | The digital platform for consular visas online',
                           review_count=0)


@app.route('/contatti')
def frontend_contact():
    return render_template('contact.html', title='Contacts')

# # # Error pages

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', title='La pagina non esiste', country_name=''), 404
