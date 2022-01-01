from flask import Flask
from write_to_acep import render_pic, init_display

app = Flask(__name__)

@app.route("/")
def hello_world():
    return("<p>Hello, World!</p>")

@app.route("/voice_hook", methods=['POST'])
def voice_hook():
    # voice prompt sends something like
    # "man fighting a dragon in a field"
    # style something like
    # "cyberpunk"
    prompt = request.form['prompt']
    style = request.form['style'])


    # make an api call to generate a GAN image
    image = api.generate(prompt, style)
    render_pic(image)

    return('', 204)

if __name__ == '__main__':
    init_display()
