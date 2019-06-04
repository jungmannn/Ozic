from flask import Flask, render_template, request, redirect, url_for, session, make_response, jsonify
from service.model import selectLogin, searchJob, signUp, dataMod
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
            manu = request.form.get('manu')
            serv = request.form.get('serv')
            mana = request.form.get('mana')
            design = request.form.get('design')
            med = request.form.get('med')
            media = request.form.get('media')

            major = request.form.get('major')
            medium = request.form.get('medium')
            small = request.form.get('small')
            start = request.form.get('start')
            public = request.form.get('public')
            listed = request.form.get('listed')

            seo = request.form.get('seo')
            cap = request.form.get('cap')
            gg = request.form.get('gg')
            bu = request.form.get('bu')
            dae = request.form.get('dae')
            ul = request.form.get('ul')
            inc = request.form.get('inc')

            p100 = request.form.get('p100')
            p200 = request.form.get('p200')
            p300 = request.form.get('p300')
            p400 = request.form.get('p400')

            w16 = request.form.get('w16')
            w24 = request.form.get('w16')
            w32 = request.form.get('w16')
            w40 = request.form.get('w40')
            w50 = request.form.get('w50')

            mon = request.form.get('mon')
            tue = request.form.get('tue')
            wed = request.form.get('wed')
            thu = request.form.get('thu')
            fri = request.form.get('fri')
            sat = request.form.get('sat')
            sun = request.form.get('sun')

            dedu = request.form.get('it')
            gra = request.form.get('gra')
            mas = request.form.get('mas')
            hi = request.form.get('hi')
            car = request.form.get('car')

            if it == None:
                it = '0'
            if manu == None:
                manu = '0'
            if serv == None:
                serv = '0'
            if mana == None:
                mana = '0'
            if design == None:
                design = '0'
            if med == None:
                med = '0'
            if media == None:
                media = '0'
                
            if major == None:
                major = '0'
            if medium == None:
                medium = '0'
            if small == None:
                small = '0'
            if start == None:
                start = '0'
            if public == None:
                public = '0'
            if listed == None:
                listed = '0'

            if seo == None:
                seo = '0'
            if cap == None:
                cap = '0'
            if gg == None:
                gg = '0'
            if bu == None:
                bu = '0'
            if dae == None:
                dae = '0'
            if ul == None:
                ul = '0'
            if inc == None:
                inc = '0'
            
            if p100 == None:
                p100 = '0' 
            if p200 == None:
                p200 = '0'
            if p300 == None:
                p300 = '0'
            if p400 == None:
                p400 = '0'

            if w16 == None:
                w16 = '0'
            if w24 == None:
                w24 = '0'
            if w32 == None:
                w32 = '0'
            if w40 == None:
                w40 = '0' 
            if w50 == None:
                w50 = '0'
            
            if mon == None:
                mon = '0'
            if tue == None:
                tue = '0'
            if wed == None:
                wed = '0'
            if thu == None:
                thu = '0'
            if fri == None:
                fri = '0'
            if sat == None:
                sat = '0'
            if sun == None:
                sun = '0'
            
            if dedu == None:
                dedu = '0'
            if mas == None:
                mas = '0'
            if gra == None:
                gra = '0'
            if hi == None:
                hi = '0'
            if car == None:
                car = '0'  
            filter1 = dict()
            filter1 = {
                'uname' : uname,
                'uid' : uid,
                'upw' : upw,
                'it' : it,
                'manu' : manu,
                'serv' : serv,
                'mana' : mana,
                'design' : design,
                'med' : med,
                'media' : media,
                'p100' : p100,
                'p200' : p200,
                'p300' : p300,
                'p400' : p400,
                'seo' : seo,
                'cap' : cap,
                'gg' : gg,
                'bu' : bu,
                'dae' : dae,
                'ul' : ul,
                'inc' : inc,
                'mon' : mon,
                'tue' : tue,
                'wed' : wed,
                'thu' : thu,
                'fri' : fri,
                'sat' : sat,
                'sun' : sun,
                'w16' : w16,
                'w24' : w24,
                'w32' : w32,
                'w40' : w40,
                'w50' : w50,
                'dedu' : dedu,
                'gra' : gra,
                'mas' : mas,
                'hi' : hi,
                'car' : car,
                'major' : major,
                'medium' : medium,
                'small' : small,
                'start' : start,
                'public' : public,
                'listed' : listed
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

    @app.route('/mypage', methods=['GET', 'POST'])
    def mypage():
        if request.method=='GET':
            return render_template('mypage.html', name=session['uname'], uid = session['uid'])
        else:
            uname = session['uname']
            it = request.form.get('it')
            manu = request.form.get('manu')
            serv = request.form.get('serv')
            mana = request.form.get('mana')
            design = request.form.get('design')
            med = request.form.get('med')
            media = request.form.get('media')

            major = request.form.get('major')
            medium = request.form.get('medium')
            small = request.form.get('small')
            start = request.form.get('start')
            public = request.form.get('public')
            listed = request.form.get('listed')

            seo = request.form.get('seo')
            cap = request.form.get('cap')
            gg = request.form.get('gg')
            bu = request.form.get('bu')
            dae = request.form.get('dae')
            ul = request.form.get('ul')
            inc = request.form.get('inc')

            p100 = request.form.get('p100')
            p200 = request.form.get('p200')
            p300 = request.form.get('p300')
            p400 = request.form.get('p400')

            w16 = request.form.get('w16')
            w24 = request.form.get('w16')
            w32 = request.form.get('w16')
            w40 = request.form.get('w40')
            w50 = request.form.get('w50')

            mon = request.form.get('mon')
            tue = request.form.get('tue')
            wed = request.form.get('wed')
            thu = request.form.get('thu')
            fri = request.form.get('fri')
            sat = request.form.get('sat')
            sun = request.form.get('sun')

            dedu = request.form.get('it')
            gra = request.form.get('gra')
            mas = request.form.get('mas')
            hi = request.form.get('hi')
            car = request.form.get('car')

            if it == None:
                it = '0'
            if manu == None:
                manu = '0'
            if serv == None:
                serv = '0'
            if mana == None:
                mana = '0'
            if design == None:
                design = '0'
            if med == None:
                med = '0'
            if media == None:
                media = '0'
                
            if major == None:
                major = '0'
            if medium == None:
                medium = '0'
            if small == None:
                small = '0'
            if start == None:
                start = '0'
            if public == None:
                public = '0'
            if listed == None:
                listed = '0'

            if seo == None:
                seo = '0'
            if cap == None:
                cap = '0'
            if gg == None:
                gg = '0'
            if bu == None:
                bu = '0'
            if dae == None:
                dae = '0'
            if ul == None:
                ul = '0'
            if inc == None:
                inc = '0'
            
            if p100 == None:
                p100 = '0' 
            if p200 == None:
                p200 = '0'
            if p300 == None:
                p300 = '0'
            if p400 == None:
                p400 = '0'

            if w16 == None:
                w16 = '0'
            if w24 == None:
                w24 = '0'
            if w32 == None:
                w32 = '0'
            if w40 == None:
                w40 = '0' 
            if w50 == None:
                w50 = '0'
            
            if mon == None:
                mon = '0'
            if tue == None:
                tue = '0'
            if wed == None:
                wed = '0'
            if thu == None:
                thu = '0'
            if fri == None:
                fri = '0'
            if sat == None:
                sat = '0'
            if sun == None:
                sun = '0'
            
            if dedu == None:
                dedu = '0'
            if mas == None:
                mas = '0'
            if gra == None:
                gra = '0'
            if hi == None:
                hi = '0'
            if car == None:
                car = '0'  
            filter2 = dict()
            filter2 = {
                'uname' : uname,
                'it' : it,
                'manu' : manu,
                'serv' : serv,
                'mana' : mana,
                'design' : design,
                'med' : med,
                'media' : media,
                'p100' : p100,
                'p200' : p200,
                'p300' : p300,
                'p400' : p400,
                'seo' : seo,
                'cap' : cap,
                'gg' : gg,
                'bu' : bu,
                'dae' : dae,
                'ul' : ul,
                'inc' : inc,
                'mon' : mon,
                'tue' : tue,
                'wed' : wed,
                'thu' : thu,
                'fri' : fri,
                'sat' : sat,
                'sun' : sun,
                'w16' : w16,
                'w24' : w24,
                'w32' : w32,
                'w40' : w40,
                'w50' : w50,
                'dedu' : dedu,
                'gra' : gra,
                'mas' : mas,
                'hi' : hi,
                'car' : car,
                'major' : major,
                'medium' : medium,
                'small' : small,
                'start' : start,
                'public' : public,
                'listed' : listed
            }
            print(filter2)
            dataMod(filter2)
            return redirect(url_for('home'))
        