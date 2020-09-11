from handEl import handEl
from pprint import pprint as pp

ELASTICSEARCH_HOST  = "192.168.1.132"
ELASTICSEARCH_PORT  = "8080"
ELASTICSEARCH_INDEX = "nori_analyzer"

# 품사 태그 설명
# https://docs.google.com/spreadsheets/d/1-9blXKjtjeKZqsf4NzHeYJCrr49-nXeRF6D80udfcwY/edit#gid=589544265

def analyze(he, text) :
    options = ["rightPOS", "-f"]
    return he.analyze(text, options)

def main() :
    he = handEl(
        host  = ELASTICSEARCH_HOST, 
        port  = ELASTICSEARCH_PORT,
        index = ELASTICSEARCH_INDEX)
    
    # https://search.shopping.naver.com/detail/lite.nhn?nvMid=19318896974&NaPm=ct%3Dkdy2mauo%7Cci%3D987c95070ec54eb8d3d777d1331f6c14d51d4e82%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3Deaecc241a834a012c2f8a88267c0fb6804fd640d
    texts = [
        '오늘 노란색 옷을 입었는 데 빨간색 여성 상의를 보여줘',
        '어플로 찍은거라 실제 색감과 다르게 나왔으니 핏만 봐주세요',
        '사진에서는 라벤더컬러가 약간 더 보랏빛돌고 생기있어보이는데 실제로는 차분하고 아주 은은한 라벤더컬러라 린넨바지랑 같이 입기 좋을것 같아요',
        '소재가 엄청 까끌한건 아닌데 누워있으면 자잘하게 자국나는 그런 니트소재에요!',
        '두께가 얇아서 상의 속옷 반쯤 비침있는데 확 드러나는건 아니라 그냥 입고 다녀도 될듯해요'
    ]

    user_dict = {
        '어플':'앱'
    }

    try :
        tinx = 0
        text = texts[tinx]
        for udkey in user_dict : 
            if udkey in text : text = text.replace(udkey, user_dict[udkey])
        results = analyze(he, text)
        for result in results :
            if 'E(Verbal endings)' in result['rightPOS'] :
                print("{0}({1}) ".format(result['token'], 'E'))
            else :
                print("{0}({1}) ".format(result['token'], result['rightPOS'][:result['rightPOS'].index("(")]), end="")
    except KeyboardInterrupt as ki :
        print("Detect ctrl+c, Bye!")

if __name__=="__main__" :
    main()