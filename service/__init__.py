from flask import Flask, render_template, request, redirect, url_for, session, make_response, jsonify
from service.model import selectLogin, searchJob, signUp
import os

def createApp():
    app = Flask(__name__)
    # 1. 세션키 생성 => 통상 값은 해쉬값(중복되지 않는 임의값)사용
    app.secret_key = 'sdgddsgjhgfkhmrtjhrtgwety47y6u5erbr'
    initRoute( app )
    return app
    
def initRoute(app):
    @app.route('/')
    def home():
        if not 'uid' in session:# 세션체크
            return redirect( url_for('login') )
        # 로그인 성공 => 쿠키 설정
        resp = make_response( render_template('index.html', name=session['uname']))
        # 쿠키 세팅
        resp.set_cookie('uid', session['uid'])
        return resp
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method=='GET':
            # 쿠키를 읽어와서 아이디창에 채운다
            uid = request.cookies.get('uid')
            if not uid:# 쿠키 없으면
                uid = ''
            return render_template('login.html', uid=uid)
        else:
            # 잘 넘어오는지 체크
            uid = request.form.get('uid')
            upw = request.form.get('upw')
            #return uid + " : " + upw
            if not uid or not upw:
                return render_template('alert.html', msg='정확하게입력하세요')
            else:
                row = selectLogin(uid, upw)
                if row:# 회원이다
                    
                    session['uid']  = uid
                    session['uname'] = row['uname']
                    session['it'] = row['it']
                    return redirect( url_for('home'))
                else:
                    return render_template('alert.html', msg='회원아님')

    @app.route('/logout')
    def logout():
        # 세션 없이 접근했을 경우 -> 홈페이지로 리다이렉트
        if not 'uid' in session:# 세션체크
            return redirect( url_for('home') )
        # 세션 제거
        if 'uid' in session:
            session.pop('uid', None)
        if 'name' in session:
            session.pop('name', None)
        # 홈페이지 리다이렉트
        return redirect( url_for('home') )
    
    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method=='GET':
            print(request.method)
            
            return render_template('signup.html')
        else:
            uname = request.form.get('uname')
            uid = request.form.get('uid')
            upw = request.form.get('upw')
            it = request.form.get('it')
            ad = request.form.get('ad')
            doc = request.form.get('doc')
            p50 = request.form.get('p50')
            p100 = request.form.get('p100')
            p150 = request.form.get('p150')
            seo = request.form.get('s')
            gg = request.form.get('g')
            inc = request.form.get('i')
            if it == None:
                it = '0'
            if ad == None:
                ad = '0'
            if doc == None:
                doc = '0'
            if p50 == None:
                p50 = '0'
            if p100 == None:
                p100 = '0'
            if p150 == None:
                p150 = '0'
            if seo == None:
                seo = '0'
            if gg == None:
                gg = '0'
            if inc == None:
                it = '0'
            filter1 = dict()
            filter1 = {
                'uname' : uname,
                'uid' : uid,
                'upw' : upw,
                'it' : it,
                'ad' : ad,
                'doc' : doc,
                'p50' : p50,
                'p100' : p100,
                'p150' : p150,
                'seo' : seo,
                'gg' : gg,
                'inc' : inc
            }
            print(filter1)
            signUp(filter1)
            return redirect(url_for('login'))
    
    @app.route('/search')
    def search():
        # 1. 전달된 데이터 획득 -> print로 출력
        row = session['it']
        pay = request.form.get('pay')
        print( row )
        print( pay )
        # 2. 데이터를 d8로 보내서 쿼리 수행
        rows = searchJob(row)
        return render_template('searchJob.html', rows = rows)

    @app.route('/mypage')
    def mypage():
        
        return render_template('mypage.html')