#%%
from handEl import handEl
from pprint import pprint as pp
import numpy as np

ELASTICSEARCH_HOST  = "192.168.1.132"
ELASTICSEARCH_PORT  = "8080"
ELASTICSEARCH_INDEX = "nori_analyzer"

he = handEl(
        host  = ELASTICSEARCH_HOST, 
        port  = ELASTICSEARCH_PORT,
        index = ELASTICSEARCH_INDEX)

# 품사 태그 설명
# https://docs.google.com/spreadsheets/d/1-9blXKjtjeKZqsf4NzHeYJCrr49-nXeRF6D80udfcwY/edit#gid=589544265

#%%

def get_text_analyzed(text) :
    global he
    options = ["rightPOS", "-f"]
    return he.analyze(text, options)

def get_texts_split_by_E(results) :
    texts = [[]]
    tags  = [[]]
    for result in results :
        text = result['token']
        tag  = result['rightPOS'][:result['rightPOS'].index("(")]
        if 'E(Verbal endings)' in result['rightPOS'] :
            texts.append([text])
            tags.append([tag])
        else : 
            texts[-1].append(text)
            tags[-1].append(tag)
    return texts, tags

#%%
# Tags
lblN = [
    'NNB', 'NNBC', 'NNG', 'NNP', 'NP', 'NR',
    'VA', 'VCN', 'VCP', 'VV', 'VX',
    'MAG', 'MM',
    'J',
    'XSA', 'XSV',
    'SF', 'E'
]
lblT = [
    np.zeros(shape=(len(lblN)))
    for i in range(len(lblN))
]
for linx in range(len(lblT)) : lblT[linx][linx] = 1
lblD = {k:lblT[i] for i,k in enumerate(lblN)}

# Morpheme Patterns Dictionary
morp_patn_dict = {
    2:[
        ['NNG', 'NNG'], 
    ],
    3:[
        ['NP', 'J', 'VA'],
    ]
}

#%%
# Matrix Compositions - Patterns
matP = dict()
for k,p in morp_patn_dict.items() :
    matP[k] = np.array([ np.array(list(map(lambda x:lblD[x], pattern))).reshape(1, -1)[0] for pattern in p ]).T
    print(matP[k].shape)

#%%
# Morpheme Analysis
text = '오늘 노란색 티셔츠를 입었는데 입을 만한 청바지가 뭐가 있을까?'
azed_texts, azed_tags = get_texts_split_by_E(get_text_analyzed(text))
print("- Text : {0}\n ㄴ texts : {1}\n ㄴ tags : {2}".format(text, azed_texts, azed_tags))

#%%
# Matrix Compositions - Tags
matTarr = dict()
for k in morp_patn_dict :
    matTarr[k] = [np.array(
        [
            np.array(
                list(
                    map(lambda x:lblD[x], [tags[i+j] for j in range(k)]))).reshape(1, -1)[0] 
            for i in range(0, len(tags)-k+1, 1)
        ]
    ) for tags in azed_tags]
    print(matTarr[k][0].shape)
    # print(matTarr[k])
# pp(matTarr)

#%%
# Patterns finding
def find_patterns(matTarr :np.ndarray, matP :np.ndarray, cry :bool = True) : 
    founds = dict()
    for k in matP :
        founds[k] = dict(filter(lambda e: len(e[1][0])>0, {
            mtinx : np.where((matTarr[k][mtinx] @ matP[k]) == k) \
            for mtinx in range(len(matTarr[k])) if matTarr[k][mtinx].shape[0] > 0 
        }.items()))
    if cry :
        for k in founds :
            for tinx in founds[k] :
                for i in range(len(founds[k][tinx][0])) :
                    print([azed_texts[tinx][founds[k][tinx][0][i]+j] for j in range(k)])
                    print([ azed_tags[tinx][founds[k][tinx][0][i]+j] for j in range(k)])
                    print("Found Pattern :", morp_patn_dict[k][founds[k][tinx][1][i]], end="\n\n")
    return founds    

#%%
found_patterns = find_patterns(matTarr, matP, cry=True)
pp(found_patterns)

#%%
prop_dict = {
    'clothing':{
        'category':'clo_prop_category',
        'color':'clo_prop_color',
        'market':'clo_prop_market', 
        'brand':'clo_prop_brand', 
        'textile':'clo_prop_textile', 
    },
    'user':{
        'age':'clo_prop_age', 
        'gender':'clo_prop_gender'
    }
}

#%%
# Pattern Dictionary 
'''
{
    pattern_length(int) : {
        pattern_number(int) : {
            find_order(head:h, tail:t) : [
                patterns(tuple)
            ]
        }
    }
}
# Regular Expressions
    - Find from dictionaries
        @ : Dictionary Index
    
    - word
        %(number) : Exactily match with number of character.
        - : Prefix- or -Suffix 
'''
patt_dict = {
    2:{
        0:{
            "t":[
                ("@clothing,color", "%1색", "CVA"),
                ("@clothing,color", "%2색상", "CVA"),
                ("@clothing,color", "%2색깔", "CVA"),
                ("@clothing,color", "@clothing,category", "CNNG")
            ]
        },
    },
    3:{
        0:{
            "h":[   
                ("%1뭣", "%1가", "%1있", "Q")
            ]
        }
    }
}

#%%
import re

#%%
def search_from_dictionary(index, keyword) :
    he.indexing(index)
    return he.search(keyword)

def match(patt :str, text :str) :
    global prop_dict

    # Exactily match with number of character.
    if patt.startswith("%") :
        n = int(re.findall("[0-9]+", patt)[0])
        p = "%([0-9]+)([가-힣]{{{0}}})".format(n)
        meta = re.search(p, patt)
        if not meta : raise ValueError("Pattern Dictionary has wrong pattern : {0}".format(patt))
        else        : return meta.groups()[-1] == text

    # Dictionary Index
    if patt.startswith("@") :
        p = "@([a-zA-Z]+),([a-zA-Z]+)"
        meta = re.search(p, patt)
        if not meta : raise ValueError("Pattern Dictionary has wrong pattern : {0}".format(patt))
        else        : 
            meta = meta.groups()
            result = search_from_dictionary(prop_dict[meta[0]][meta[1]], text)
            return list(meta)+result['match_ids'] if result else False

def find_expressions(find_order :str, patt_list, texts) :
    # print(("\n--- Expression Param\n * Pattern Type : {0},\n * Pattern List : {1}\n * Given Text : {2}\n").format(
    #         find_order, patt_list, texts))
    order = range(0, len(texts), 1) if find_order == "h" else range(len(texts)-1, -1, -1)
    for pinx in range(len(patt_list)) :
        match_history = []
        for tinx in order : 
            # one text - many patterns
            patt, text = patt_list[pinx][tinx], texts[tinx]
            match_result = match(patt, text)
            if match_result : match_history.append(match_result)
            else            : break
        if len(match_history) == len(texts) : return match_history+[patt_list[pinx][-1]]
    return False

def patEx(azed_texts :list, patt_data :dict) :
    global patt_dict
    for lk in patt_data : # lk : length key
        if not lk in patt_dict : continue
        for tk in patt_data[lk] : # tk : text key
            for i in range(len(patt_data[lk][tk][1])) : # (array([1, 2]), array([0, 0]))
                text_number    = patt_data[lk][tk][0][i]
                pattern_number = patt_data[lk][tk][1][i]
                if not pattern_number in patt_dict[lk] : continue # Pattern number is exists in dictionary?
                
                for find_order in patt_dict[lk][pattern_number] :
                    found_result = find_expressions(
                        find_order, 
                        patt_dict[lk][pattern_number][find_order],
                        [azed_texts[tk][text_number+j] for j in range(lk)]
                    )
                    if found_result : 
                        print("I finally found the expression : {0}".format(found_result))
                        print("from {0}".format([azed_texts[tk][text_number+j] for j in range(lk)]))
patEx(azed_texts, found_patterns)            


#%%
text = "<clothing@color<hello%what%가거도"
print(list(re.finditer("<[a-zA-Z]+", text)))
print(re.findall("@[a-zA-Z]+", text))
print(re.findall("%[가-힣]", text))

#%%    
texts = [
    '휴가 때 입을 빨간 반팔 옷 보여주세요.',
    '오늘 입을 만한 청바지가 뭐가 있을까?',
    '자라에서 추운 날 입을 만한 옷이 있을까?',
    '운동할 때 입기 좋은 트레이닝 바지 알려줘',
]