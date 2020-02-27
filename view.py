from app import *
from flask import request, render_template, redirect
from models import *
from hashlib import md5

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/createlink', methods=['POST'])
def create_link():
    req = request.get_json()
    if req and 'url' in req and isinstance(req['url'], str):
        hashed_url = md5(bytearray(req['url'], encoding='utf8')).hexdigest()[:12]
        duplicate = db.session.query(Urls_and_token).filter(Urls_and_token.token == hashed_url).first()

        if duplicate:
            return {'result': hashed_url}, 200

        new_link = Urls_and_token(url=req['url'],
                                  token=hashed_url)
        db.session.add(new_link)
        db.session.commit()

        return {'result': hashed_url}, 201
    else:
        return {'result': None}, 405


@app.route('/<string:token>', methods=['GET'])
def redirtolink(token):
    url = db.session.query(Urls_and_token.url).filter(Urls_and_token.token == token).first()
    if url:
        return redirect(url[0], 302)
    else:
        return {'error': None}, 405
