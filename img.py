from flask import Flask, request, jsonify

app = Flask(__name__)

app.route('/upload', methods = ['POST'])
def upload_img():
    if 'image' not in request.files:
        return jsonify({"error " : "No image Provided"}), 400
    

    image_file = request.files['image']
    if image_file.image == '':
        return jsonify({"error":"image file name is empty"}), 400
    
    return jsonify({'message':'image uploaded successfully'}), 200

if __name__=="__main__":
    app.run(debug=True)
    

