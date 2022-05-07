from visafy_frontend import app, if_local

if __name__ == '__main__':
    if if_local:
        app.run(host='localhost', debug=True, port=8000)
    else:
        app.run(host='0.0.0.0')
