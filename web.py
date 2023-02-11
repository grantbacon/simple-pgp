import bottle

@bottle.route('/')
def index():
    return bottle.static_file('index.htm', root='.', mimetype='text/html')

@bottle.route('/openpgp.min.js')
def openpgpjs_lib():
    return bottle.static_file('openpgp.min.js', root='.', mimetype='text/javascript')


app = application = bottle.default_app()

if __name__ == "__main__":
    try:
        bottle.debug(True)
        bottle.run(app=app, host='127.0.0.1', port=12345)
    except KeyboardInterrupt:
        exit()
