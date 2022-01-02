from flask import Flask, request
from write_to_acep import AcepController
from wombo import Wombo
from bitmap import make_bitmap
from Levenshtein import distance as lev

app = Flask(__name__)
controller = None

@app.route("/")
def hello_world():
    return("<p>Hello, World!</p>")

@app.route("/render")
def render():
    controller.render_pic()
    return('', 204)

@app.route("/generate", methods=['POST'])
def generate():
    request_data = request.get_json()
    print(request_data)
    prompt = request_data['prompt']
    style = request_data['style']
    if not prompt:
        print('missing prompt')
    if not style:
        print('missing style')
    w = Wombo()
    w.generate(prompt, style)
    w.download_image()
    make_bitmap()
    bitmap_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'bitmap.bmp')
    controller.render_pic(bitmap_path)
    return('', 204)

@app.route("/voice_hook", methods=['POST'])
def voice_hook():
    # voice prompt sends something like
    # "man fighting a dragon in a field"
    # style something like
    # "cyberpunk"

    request_data = request.get_json()
    params = request_data["requestJson"]["session"]["params"]
    style = params["style"]
    prompt = params["prompt"]
    if not style:
        print("missing style in voice hook params")
        return('', 204)
    if not prompt:
        print("missing prompt in voice hook params")
        return('', 204)

    styles_map = {
        "synthwave": 1,
        "ukiyoe": 2,
        "steampunk": 4,
        "fantasy": 5,
        "vibrant": 6,
        "HD": 7,
        "pastel": 8,
        "psychic": 9,
        "dark fantasy": 10,
        "festive": 12,
        "mystical": 11,
        "baroque": 13,
        "etching": 14
    }

    if style not in styles_map.keys():
        keys = styles_map.keys()
        lev_distances = [lev(style, s) for s in keys]
        lowest = None
        lowest_key = None
        for key, val in enumerate(lev_distances):
            if lowest is None or val < lowest:
                lowest = val
                lowest_key = key
        style = keys[lowest_key]

    style_id = styles_map[style]
    print("found prompt and style", prompt, style_id)

    # w = Wombo()
    # w.generate(prompt, style)
    # w.download_image()
    # make_bitmap()
    # bitmap_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'bitmap.bmp')
    # controller.render_pic(bitmap_path)
    return('', 204)

if __name__ == '__main__':
    controller = AcepController()
    controller.init_display()
    app.run(host='0.0.0.0', port=8090)
