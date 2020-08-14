from handEl import handEl
from pprint import pprint as pp

ELASTICSEARCH_HOST  = "localhost"
ELASTICSEARCH_PORT  = "8080"
ELASTICSEARCH_INDEX = "nori_analyzer"

# 품사 태그 설명
# https://docs.google.com/spreadsheets/d/1-9blXKjtjeKZqsf4NzHeYJCrr49-nXeRF6D80udfcwY/edit#gid=589544265


def main() :
    he = handEl(
        host  = ELASTICSEARCH_HOST, 
        port  = ELASTICSEARCH_PORT,
        index = ELASTICSEARCH_INDEX)

    text = "하나 둘 셋하면 한 개의 사진이 나온다"
    options = ["rightPOS"]
    results = he.analyze(text, options)
    print("We analyze the '{0}'".format(text))
    print(results)
    
if __name__=="__main__" :
    main()