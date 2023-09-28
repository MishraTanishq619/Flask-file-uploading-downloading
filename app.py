from flask import Flask, flash, render_template, redirect, request, send_from_directory
import os, secrets

key = secrets.token_hex(16)



app = Flask(__name__)
app.secret_key = key
app.config['UPLOAD_FOLDER'] = 'uploaded_files'

@app.route('/')
def index():
    filenames = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', filenames=filenames)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        # return "No selected file"

        flash("No selected file","warning")
        return redirect('/')
    
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        flash("File uploaded successfully","success")
        return redirect('/')
    

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
