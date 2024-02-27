import os

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

"""
@app.route("/")
def hello_world():
    return "<p> Hello, World!</p>"
"""
app.config['UPLOAD_FOLDER'] = os.path.join(app.instance_path, 'uploads')

# Create the upload folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_image():

    # Access uploaded image file
    uploaded_image = request.files["image"]

    # Check if a file was uploaded
    if uploaded_image.filename == "":
        return "No image selected for upload.", 400

    # Get filename and extension
    filename = secure_filename(uploaded_image.filename)
    file_ext = os.path.splitext(filename)[1]  # Get extension

    # Allowed file extensions
    ALLOWED_EXTENSIONS = set(['.png', '.jpg', '.jpeg', '.gif'])


    # Validate file extension
    if file_ext.lower() not in ALLOWED_EXTENSIONS:
        return "Invalid image format. Please upload a PNG, JPG, JPEG, or GIF image.", 400

    # Create a unique filename (optional)
    # You can use libraries like uuid to generate unique identifiers
    # filename = str(uuid.uuid4()) + file_ext

    # Save the uploaded image (replace with your desired location)
    uploaded_image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    # Update the "upload-message" element in your HTML using JavaScript
    # (You'll need JavaScript code to handle this communication)

    # Return a success message (or redirect to another route)
    return "Image uploaded successfully!", 200

"""
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
