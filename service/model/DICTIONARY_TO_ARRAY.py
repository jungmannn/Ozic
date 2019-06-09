import numpy as np

def dictionary_to_array(Rows):

    User_data = np.array([
        [int(Rows.get('it')),int(Rows.get('manufacturing')),int(Rows.get('service')),int(Rows.get('management')), int(Rows.get('design')), int(Rows.get('medical')), int(Rows.get('media'))],
        [int(Rows.get('p100')),int(Rows.get('p200')),int(Rows.get('p300')),int(Rows.get('p400')), int(Rows.get('p500')), 0, 0],
        [int(Rows.get('seoul')),int(Rows.get('capital')),int(Rows.get('gg')),int(Rows.get('busan')), int(Rows.get('daejeon')), int(Rows.get('ulsan')), int(Rows.get('incheon'))],
        [int(Rows.get('mon')),int(Rows.get('tue')),int(Rows.get('wed')),int(Rows.get('thu')), int(Rows.get('fri')), int(Rows.get('sat')), int(Rows.get('sun'))],
        [int(Rows.get('w16')),int(Rows.get('w24')),int(Rows.get('w32')),int(Rows.get('w40')), int(Rows.get('wh24')), int(Rows.get('wh32')), int(Rows.get('wh40'))],
        [int(Rows.get('dedu')),int(Rows.get('gradu')),int(Rows.get('master')),int(Rows.get('phd')), int(Rows.get('hgradu')), int(Rows.get('career')), 0],
        [int(Rows.get('major')),int(Rows.get('medium')),int(Rows.get('small')),int(Rows.get('startup')), int(Rows.get('public')), int(Rows.get('Listed')), 0]])
    return User_data