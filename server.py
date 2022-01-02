from flask import Flask, request
from write_to_acep import AcepController
from wombo import Wombo
from bitmap import make_bitmap

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
    # prompt = request.form['prompt']
    # style = request.form['style']


    # make an api call to generate a GAN image
    # image = api.generate(prompt, style)
    # render_pic(image)

    return('', 204)

if __name__ == '__main__':
    controller = AcepController()
    controller.init_display()
    app.run(host='0.0.0.0', port=8090)
