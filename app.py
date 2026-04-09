from flask import Flask, render_template, request, send_file
from qrcode_generator import QRGenerator
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/generator/qr', methods=['GET'])
def generator():
    return render_template("qrgen.html")

@app.route('/generator/qr', methods=['POST'])
def qrgen():
    qr = QRGenerator(version=2, box_size=10, border=2)
    qr_data = request.form["data"]
    qr.save(qr_data)
    return send_file("qrcode.png", mimetype="image/png", as_attachment=True, download_name="qrcode.png")


if __name__ == '__main__':
    app.run(debug=True)