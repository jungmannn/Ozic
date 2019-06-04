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
            sql_str = '''select * from user_tb where uid=%s and upw=%s;'''
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

def signUp( data ):
    db_session   = None
    affected_row = 0 # 영향을 받은 로의 수
    try:    
        db_session = sql.connect( host='localhost',
                                user='root',
                                password='12341234',
                                db='ozic_db',
                                charset='utf8',
                                cursorclass=sql.cursors.DictCursor)
        
        with db_session.cursor() as cursor:
            sql_str = '''
                insert into user_tb(`uname`, `uid`, `upw`, `it`, `manufacturing`, `service`, `management`, `design`, `medical`, `media`, `p200`, `p300`, `p400`, `p500`, `none1`, `none2`, `none3`, `seoul`, `capital`, `gg`,`busan`,`daejeon`,`ulsan`,`incheon`,`mon`,`tue`,`wed`, `thu`, `fri`, `sat`, `sun`, `w16`, `w24`, `w32`, `w40`, `w50`, `none4`, `none5`, `dedu`, `gradu`, `master`, `hgradu`, `career`, `none6`, `none7`, `major`, `medium`, `small`, `startup`, `public`, `Listed`, `none8`)
                value (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0, 0, 0, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 0, 0, %s, %s, %s, %s, %s, 0, 0, %s, %s, %s, %s, %s, %s, 0);
            '''
            cursor.execute( sql_str, 
              (
                data.get('uname'),
                data.get('uid'),
                data.get('upw'),
                data.get('it'),
                data.get('manu'),
                data.get('serv'),
                data.get('mana'),
                data.get('design'),
                data.get('med'),
                data.get('media'),
                data.get('p100'),
                data.get('p200'),
                data.get('p300'),
                data.get('p400'),
                data.get('seo'),
                data.get('cap'),
                data.get('gg'),
                data.get('bu'),
                data.get('dae'),
                data.get('ul'),
                data.get('inc'),
                data.get('mon'),
                data.get('tue'),
                data.get('wed'),
                data.get('thu'),
                data.get('fri'),
                data.get('sat'),
                data.get('sun'),
                data.get('w16'),
                data.get('w24'),
                data.get('w32'),
                data.get('w40'),
                data.get('w50'),
                data.get('dedu'),
                data.get('gra'),
                data.get('mas'),
                data.get('hi'),
                data.get('car'),
                data.get('major'),
                data.get('medium'),
                data.get('small'),
                data.get('start'),
                data.get('public'),
                data.get('listed')
              ) )
        # 실제 반영 => commit()
        db_session.commit()
        affected_row = db_session.affected_rows()
    except Exception as e:
        print( e )
    finally:    
        if db_session:
            db_session.close()            
    # 영향을 받은 로의 수를 반환
    return affected_row
def dataMod( data ):
    db_session   = None
    affected_row = 0 # 영향을 받은 로의 수
    try:    
        db_session = sql.connect( host='localhost',
                                user='root',
                                password='12341234',
                                db='ozic_db',
                                charset='utf8',
                                cursorclass=sql.cursors.DictCursor)
        
        with db_session.cursor() as cursor:
            sql_str = '''
                UPDATE user_tb
                SET `it` = %s, `manufacturing` = %s, `service` = %s, `management` = %s, `design` = %s, `medical` = %s, `media` = %s, `p200` = %s, `p300` = %s, `p400` = %s, `p500` = %s, `seoul` = %s, `capital` = %s, `gg` = %s,`busan` = %s,`daejeon` = %s,`ulsan` = %s,`incheon` = %s,`mon` = %s,`tue` = %s,`wed` = %s, `thu` = %s, `fri` = %s, `sat` = %s, `sun` = %s, `w16` = %s, `w24` = %s, `w32` = %s, `w40` = %s, `w50` = %s, `dedu` = %s, `gradu` = %s, `master` = %s, `hgradu` = %s, `career` = %s, `major` = %s, `medium` = %s, `small` = %s, `startup` = %s, `public` = %s, `Listed` = %s
                WHERE `uid` = %s;
                ;
            '''
            cursor.execute( sql_str, 
              (
                data.get('it'),
                data.get('manu'),
                data.get('serv'),
                data.get('mana'),
                data.get('design'),
                data.get('med'),
                data.get('media'),
                data.get('p100'),
                data.get('p200'),
                data.get('p300'),
                data.get('p400'),
                data.get('seo'),
                data.get('cap'),
                data.get('gg'),
                data.get('bu'),
                data.get('dae'),
                data.get('ul'),
                data.get('inc'),
                data.get('mon'),
                data.get('tue'),
                data.get('wed'),
                data.get('thu'),
                data.get('fri'),
                data.get('sat'),
                data.get('sun'),
                data.get('w16'),
                data.get('w24'),
                data.get('w32'),
                data.get('w40'),
                data.get('w50'),
                data.get('dedu'),
                data.get('gra'),
                data.get('mas'),
                data.get('hi'),
                data.get('car'),
                data.get('major'),
                data.get('medium'),
                data.get('small'),
                data.get('start'),
                data.get('public'),
                data.get('listed'),
                data.get('uname')
              ) )
        # 실제 반영 => commit()
        db_session.commit()
        affected_row = db_session.affected_rows()
    except Exception as e:
        print( e )
    finally:    
        if db_session:
            db_session.close()            
    # 영향을 받은 로의 수를 반환
    return affected_row



