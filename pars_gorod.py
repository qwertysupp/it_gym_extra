goroda = []
index = 0
one_proba ={
    'day':'2022-10-19',
    'city':'Moscow',
    'prob':{
        'morning': -7,
        'afternoon': -2,
        'evening': -3,
    }
}
one_proba_2 ={
    'day':'2022-10-19',
    'city':'Saratov',
    'prob':{
        'morning': 7,
        'afternoon': 3,
        'evening': 4,
    }
}
one_proba_3 ={
    'day':'2022-10-19',
    'city':'Moreypals',
    'prob':{
        'morning': -7000,
        'afternoon': 6,
        'evening': 3000,
    }
}


def find_city(name_city):
    for city in goroda:
        if name_city == city:
            return False
    return True




def find_max_min__by_city(goroda, page_pogoda):
    max: float
    min: float
    data: str
    for one_prob in page_pogoda:
        if one_prob['city'] == goroda:
            a=one_prob['prob']['morning']
            b=one_prob['prob']['afternoon']
            c=one_prob['prob']['evening']
            d=one_prob['day']
            if a>b and a>c:
                maxt=a 
                if b<c:
                    mint=b 
                else:
                    mint=c
            elif b>a and b>c:
                maxt=b
                if a<c:
                    mint=a
                else:
                    mint=c
            else:
                maxt=c 
                if a<b:
                    mint=a
                else:
                    mint=b
                    
            try:
                if maxt>max:
                    max=maxt
                    data=d
                elif mint<min:
                    min=mint
            except UnboundLocalError:
                max = maxt
                min = mint
                data = d
    return max,min,data

def name_city():
    page_pogoda=[one_proba,one_proba_2,one_proba_3]
    index=0
    while index<len(page_pogoda):
        new_gorod = page_pogoda[index]['city']
        if find_city(page_pogoda[index]['city']):
            goroda.append((page_pogoda[index]['city']))
            print(find_max_min__by_city(new_gorod, page_pogoda), new_gorod)
        index += 1
name_city()
