from flask import Flask, request, jsonify
from PIL import Image
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Garante que o diretório 'images' exista
if not os.path.exists('images'):
    os.makedirs('images')

def init_db():
    try:
        conn = sqlite3.connect('images.db')
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS images (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_filename TEXT NOT NULL,
                modified_filename TEXT NOT NULL,
                filter_type TEXT NOT NULL,
                timestamp TEXT NOT NULL
            )
        ''')
        conn.commit()
        print("Banco de dados e tabela 'images' criados ou atualizados com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")
    finally:
        if conn:
            conn.close()

# Inicializa o banco de dados ao iniciar o servidor
init_db()

def apply_filter(image_path):
    img = Image.open(image_path)
    smaller_size = (img.width // 5, img.height // 5)
    img = img.resize(smaller_size, Image.NEAREST)
    img = img.resize((img.width * 5, img.height * 5), Image.NEAREST)
    img = img.convert("L")  # Converte para preto e branco
    return img

def save_metadata(original_filename, modified_filename, filter_type):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        conn = sqlite3.connect('images.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO images (original_filename, modified_filename, filter_type, timestamp)
            VALUES (?, ?, ?, ?)
        ''', (original_filename, modified_filename, filter_type, timestamp))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Erro ao salvar metadados: {e}")
    finally:
        if conn:
            conn.close()

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({"error": "No selected file"}), 400

    original_image_path = os.path.join('images', image.filename)
    image.save(original_image_path)

    filtered_image = apply_filter(original_image_path)
    modified_filename = f"modified_{image.filename}"
    modified_image_path = os.path.join('images', modified_filename)
    filtered_image.save(modified_image_path, quality=95)

    # Salva metadados no banco de dados
    save_metadata(image.filename, modified_filename, "black_and_white")

    return jsonify({"message": "Image uploaded and processed successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
