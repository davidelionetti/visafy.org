from visafy_frontend import app, if_local

if if_local:
    app.config['IF_EB'] = False
else:
    app.config['SERVER_NAME'] = 'visafy.it'
    app.config['IF_EB'] = True

application = app

if __name__ == '__main__':
    if if_local:
        application.run(host='localhost', debug=True, port=8000)
    else:
        application.run(host='0.0.0.0')
