from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Folder tempat menyimpan file txt
UPLOAD_FOLDER = 'saved_files'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/save', methods=['POST'])
def save_text():
    data = request.json
    filename = data.get('filename', 'note.txt')
    content = data.get('content', '')

    # Pastikan ekstensi file adalah .txt
    if not filename.endswith('.txt'):
        filename += '.txt'

    filepath = os.path.join(UPLOAD_FOLDER, filename)
    
    # Menyimpan konten ke dalam file txt
    with open(filepath, 'w') as f:
        f.write(content)

    return jsonify({"message": f"File {filename} berhasil disimpan di server!"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)