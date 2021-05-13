from PyDictionary import PyDictionary
from deep_translator import GoogleTranslator
import threading
import time
import math
import concurrent.futures
from threading import Timer
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS, cross_origin

dictionary = PyDictionary()
translator = GoogleTranslator(src='auto')

def setInterval(timer, task):
    isStop = task()
    if not isStop:
        Timer(timer, setInterval, [timer, task]).start()

is_running = False

cod = [
    'af',
    'sq',
    'am',
    'ar',
    'hy',
    'az',
    'eu',
    'be',
    'bn',
    'bs',
    'bg',
    'ca',
    'ceb',
    'ny',
    'zh-cn',
    'zh-tw',
    'co',
    'hr',
    'cs',
    'da',
    'nl',
    'eo',
    'et',
    'tl',
    'fi',
    'fr',
    'fy',
    'gl',
    'ka',
    'de',
    'el',
    'gu',
    'ht',
    'ha',
    'haw',
    'iw',
    'he',
    'hi',
    'hmn',
    'hu',
    'is',
    'ig',
    'id',
    'ga',
    'it',
    'ja',
    'jw',
    'kn',
    'kk',
    'km',
    'ko',
    'ku',
    'ky',
    'lo',
    'la',
    'lv',
    'lt',
    'lb',
    'mk',
    'mg',
    'ms',
    'ml',
    'mt',
    'mi',
    'mr',
    'mn',
    'my',
    'ne',
    'no',
    'or',
    'ps',
    'fa',
    'pl',
    'pt',
    'pa',
    'ro',
    'ru',
    'sm',
    'gd',
    'sr',
    'st',
    'sn',
    'sd',
    'si',
    'sk',
    'sl',
    'so',
    'es',
    'su',
    'sw',
    'sv',
    'tg',
    'ta',
    'te',
    'th',
    'tr',
    'uk',
    'ur',
    'ug',
    'uz',
    'vi',
    'cy',
    'xh',
    'yi',
    'yo',
    'zu'
]

codes = [
    'af',
    'sq',
    'am',
    'ar'
]

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def synonymize():
    s_time = time.time()
    is_running = True

    stop = False

    global dictionary
    output = dictionary.synonym("Hello")
    taken = ["Hello"]
    l_in = 0
    delay = 2
    lt = time.time()

    while not stop:
        
        if lt - time.time() >= 2:
            print(f'{len(output)}')
            lt = time.time()

        for i in output:
            if i not in taken:
                try:
                    for word in dictionary.synonym(i):
                        if word not in output:
                            output.append(word)
                        else:
                            continue
                except:
                    continue
            else:
                continue

            print(f'{len(output)}')
            file_obj = open("output.txt", "w+")
            file_obj.write('\n'.join(output))
            file_obj.close()

            if len(output) >= 1000000:
                stop = True
                break
            else:
                continue
    
    tdiff = time.time() - s_time

    print(time.strftime("%H:%M:%S", time.gmtime(tdiff)))


            # print(f'{round(time.time() - s_time, 2)} : {len(output)}')

def measurement():
    f = open("output.txt", "r+")
    output = f.read().split('\n')
    print(f'{round(time.time() - s_time, 2)} : {len(output)}')
    f.close()

def translate_lang():
    is_running = True

    try:
        fs = open("output.txt", "r")
    except:
        fs = open("output.txt", "w+")
    word_li = fs.read().split('\n')
    fs.close()

    print(word_li)
    result = []

    if word_li[0] == '':
        return
    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            res = [[result.append(x) for x in [v for v in executor.map(lambda l: GoogleTranslator(src="auto", target=l).translate(w), codes)]] for w in word_li]
        
    except:
        return

    print(res)
    fs = open("output.txt", "a+")
    output = '\n'.join(result)
    fs.write(output)
    fs.close()

def translate_list(li, target):
    output = []
    for word in li:
        print(word)
        new_word = GoogleTranslator(src='auto', target=target).translate(word)
        output.append(new_word)
        print(new_word)
    return output

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
@cross_origin()
def run():
    with open("output.txt", "r") as f:
        return '\n'.join(render_template("index.html", text=f.read()).split('\n'))

@app.route('/api')
@cross_origin()
def run_api():
    with open("output.txt", "r") as f:
        return jsonify(text = f.read())

# @blueprint.after_request # blueprint can also be app~~
# def after_request(response):
#     header = response.headers
#     header['Access-Control-Allow-Origin'] = '*'
#     return response
