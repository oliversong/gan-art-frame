from flask import Flask
from write_to_acep import AcepController
from wombo import Wombo

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
    w = Wombo()
    w.generate(request.form['prompt'], request.form['style'])
    w.download_image(url)
    bitmap_path = make_bitmap(w.filepath)
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
