from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import mysql.connector

# 建立 Flask 應用程式
app = Flask(__name__, static_folder='static')  # 'static' 資料夾存放前端文件
CORS(app)  # 啟用跨域支援

# 資料庫配置
db_config = {
    'user': 'root',         # MySQL 使用者名稱
    'password': '12345678',  # MySQL 密碼
    'host': '127.0.0.1',    # MySQL 主機（通常為本地）
    'database': 'object'    # 資料庫名稱
}

# API 定義，從 MySQL 資料庫獲取資料
@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        # 建立資料庫連接
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # 查詢資料庫中的表格資料
        cursor.execute("SELECT name, city, quote FROM fun_facts;")
        rows = cursor.fetchall()

        # 格式化資料為 JSON 格式
        data = [{"name": row[0], "city": row[1], "quote": row[2]} for row in rows]
        return jsonify(data)
    except mysql.connector.Error as err:
        return jsonify({"error": f"資料庫錯誤：{err}"}), 500
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

# 提供靜態文件
@app.route('/', defaults={'path': 'index.html'})
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run(debug=True)
