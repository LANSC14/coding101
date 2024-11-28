#pip install Flask flask-cors google-cloud-vision Pillow

import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from google.cloud import vision
from PIL import Image
import io

app = Flask(__name__)
CORS(app)  # 允許跨域請求

# 設定 Google Vision API
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/credentials.json"  # 設定 API 金鑰路徑
vision_client = vision.ImageAnnotatorClient()

@app.route('/api/upload', methods=['POST'])
def upload_image():
    # 確認請求是否包含圖片
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image_file = request.files['image']
    try:
        # 打開圖片並轉換為 Google Vision API 可用格式
        image_content = image_file.read()
        image = vision.Image(content=image_content)

        # 使用 Google Vision API 進行地點辨識
        response = vision_client.label_detection(image=image)
        labels = response.label_annotations

        # 模擬結果（應結合實際數據庫匹配）
        community_name = None
        for label in labels:
            if "building" in label.description.lower() or "community" in label.description.lower():
                community_name = label.description
                break

        if not community_name:
            return jsonify({'error': 'Community not recognized'}), 404

        # 模擬位置結果（可用更進階方法整合地理資訊）
        location = {'lat': 25.0330, 'lng': 121.5654}  # 假設位置為台北 101

        return jsonify({
            'communityName': community_name,
            'location': location
        })

    except Exception as e:
        print(e)
        return jsonify({'error': 'Image processing failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
