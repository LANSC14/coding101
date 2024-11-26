from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

# 建立 Flask 應用程式
app = Flask(__name__, static_folder='static')  # 'static' 資料夾存放前端文件
CORS(app)  # 啟用跨域支援

# API 定義
@app.route('/api/data', methods=['GET'])
def get_data():
    # 模擬資料庫返回的資料
    data = [
        {"column1": 1, "column2": "阿爾伯特·愛因斯坦"},
        {"column1": 2, "column2": "列奧納多·達·芬奇"},
        {"column1": 3, "column2": "艾薩克·牛頓"},
        {"column1": 4, "column2": "查爾斯·達爾文"},
        {"column1": 5, "column2": "尼古拉·特斯拉"},
    ]
    return jsonify(data)

# 提供靜態文件
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
