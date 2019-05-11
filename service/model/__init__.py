import pymysql as sql

def selectLogin(uid,upw):
    db_session = None
    row = None
    try:    
        db_session = sql.connect( host='localhost',
                                user='root',
                                password='12341234',
                                db='python_db',
                                charset='utf8',
                                cursorclass=sql.cursors.DictCursor)
        print('디비접속성공')    
        with db_session.cursor() as cursor:
            sql_str = '''select * from users where uid=%s and upw=%s;'''
            cursor.execute( sql_str, (uid,upw) )
            row = cursor.fetchone() 
            # 디비쿼리문은판단하지않는다
            # 오직수행의결과만을제시한다
            # (단,쿼리상으로어느정도로직을해결할수있다)               
    except Exception as e:
        print( e )
    finally:    
        if db_session:
            db_session.close()
            print('디비접속해제성공')
    #쿼리결과인회원정보리턴
    return row

    
    



