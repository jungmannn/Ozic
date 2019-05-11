from flask import Flask, render_template, request, redirect, url_for, session, make_response, jsonify
from service.model import selectLogin
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
    # @app.route('/loginProc', methods=['GET', 'POST'])
    # def loginProc():
    #     if request.method == 'GET': # get
    #         return render_template('login.html')
    #     else:
    #         uid = request.form.get('uid')
    #         upw = request.form.get('upw')
    #         if not uid or not upw:
    #             return render_template('alert.html', msg='정확하게입력하세요')
    #         else:
    #             row = selectLogin(uid, upw)
    #             if row:#회원이다
    #                 return redirect('/')
    #             else:#회원아니다
    #                 return render_template('alert.html', 
    #                         msg='회원아님')
    # # POST 전용
    # @app.route('/search', methods=['POST'])
    # def search():
    #     info = dict()
    #     info['points']   = request.form.get('points')
    #     info['type']     = request.form.get('type')
    #     info['category'] = request.form.get('category')
    #     info['rating']   = request.form.get('rating')
    #     rows = searchInPlaystore( info )
    #     print(rows)
    #     if not rows:
    #         rows = "결과 없음"
    #     return render_template("search.html", rows= rows)
    # if __name__ == '__main__':
    #     app.run(debug=True)
    
    # @app.route('/search2', methods=['POST'])
    # def search2():
    #     info = dict()
    #     info['points']   = request.form.get('points')
    #     info['type']     = request.form.get('type')
    #     info['category'] = request.form.get('category')
    #     info['rating']   = request.form.get('rating')
    #     rows = searchInAppstore( info )
    #     print(rows)
    #     if not rows:
    #         rows = "{}" 
    #     return render_template("search2.html", rows= rows)
        
    # @app.route('/chart', methods=['POST'])
    # def chart():
    #     info = dict()
    #     info['category'] = request.form.get('category')
    #     return render_template("chart.html", info= info)
    # if __name__ == '__main__':
    #     app.run(debug=True)
    # @app.route('/predict')
    # def predict():
    #     return render_template("predictionModel.html")
    if __name__ == '__main__':
        app.run(debug=True)