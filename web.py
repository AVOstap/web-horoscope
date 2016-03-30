from bottle import route, run, view, static_file
import datetime
from horo import get_sentence_generator

zodiacDict = {'Aries': ('Овен', 'a'),
              'Taurus': ('Телец', 'b'),
              'Gemini': ('Близнецы', 'c'),
              'Cancer': ('Рак', 'd'),
              'Leo': ('Лев', 'e'),
              'Virgo': ('Дева', 'f'),
              'Libra': ('Весы', 'g'),
              'Scorpio': ('Скорпион', 'h'),
              'Sagittarius': ('Стрелец', 'i'),
              'Capricorn': ('Козерог', 'j'),
              'Aquarius': ('Водолей', 'k'),
              'Pisces': ('Рыбы', 'l')}

month = {1: "января",
         2: "февраля",
         3: "марта",
         4: "апреля",
         5: "мая",
         6: "июня",
         7: "июля",
         8: "августа",
         9: "сентября",
         10: "октября",
         11: "ноября",
         12: "декабря"}


@route('/')
@view('view')
def index():
    return create_response()


@route('/<zodiacName>')
@view('view')
def zodiacPage(zodiacName):
    return create_response(zodiacName)


@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./static')


def create_response(zodiacName =''):
    """
        Create response dictionary for index (zodiacName = Null) and zodiac page
    :type zodiacName: dict
    """
    now = datetime.datetime.now()
    responseDict = {}
    if zodiacName:
        responseDict['title'] = zodiacName
        responseDict['header'] = "{}. {} {}".format(zodiacDict[zodiacName][0], now.day, month[now.month])
        responseDict['text'] = sentenceGen.generate_text()
        responseDict['day'] = zodiacDict[zodiacName][1]
    else:
        responseDict['day'] = now.day
        responseDict['month'] = month[now.month]
        responseDict['header'] = "Узнай свою судьбу"
        responseDict['zodiac'] = [(zodiacDict[z][0], z) for z in zodiacDict.keys()]
    return responseDict

sentenceGen = get_sentence_generator('h.txt')

run(host='localhost', port=8080, debug=True)
