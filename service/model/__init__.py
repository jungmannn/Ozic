import pymysql as sql

def selectLogin(uid,upw):
    db_session = None
    row = None
    try:    
        db_session = sql.connect( host='localhost',
                                user='root',
                                password='12341234',
                                db='ozic_db',
                                charset='utf8',
                                cursorclass=sql.cursors.DictCursor)
        print('디비접속성공')    
        with db_session.cursor() as cursor:
            sql_str = '''select * from oziclogin where uid=%s and upw=%s;'''
            cursor.execute( sql_str, (uid,upw) )
            row = cursor.fetchone()
    except Exception as e:
        print( e )
    finally:
        if db_session:
            db_session.close()
            print('디비접속해제성공')
    #쿼리결과인회원정보리턴
    return row

def searchJob(row):
    db_session = None
    rows = None
    try:    
        db_session = sql.connect( host='localhost',
                                user='root',
                                password='12341234',
                                db='ozic_db',
                                charset='utf8',
                                cursorclass=sql.cursors.DictCursor)
        print('디비접속성공')    
        with db_session.cursor() as cursor:
            sql_str = '''   select *
                            From ozicTest as a
                            Where a.it in(select b.it from oziclogin as b) and a.it = %s;
                    '''
            cursor.execute( sql_str, (row))
            rows = cursor.fetchall()
            print(rows)
    except Exception as e:
        print( e )
    finally:
        if db_session:
            db_session.close()            
    return rows

    
    



