from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p> Hello, World!</p>"


"""
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_image():
    # Access uploaded image file and save it (replace with your logic)
    image_file = request.files["image"]
    # ... (save image_file)
    return "Image uploaded successfully!"  # Placeholder response


@app.route("/style", methods=["POST"])
def select_style():
    selected_style = request.form["style"]
    # Store selected style (replace with your logic)
    return "Style selected: " + selected_style


@app.route("/style/<selected_style>")
def select_style(selected_style):
    # Store selected style and proceed (replace with your logic)
    return "Style selected: " + selected_style


@app.route("/generate", methods=["POST"])
def generate_audio():
    # Placeholder message while functionality is implemented
    return "Audio generation in progress..."

"""
