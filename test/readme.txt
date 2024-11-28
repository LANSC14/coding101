安裝以下 Python 庫：
    pip install Flask flask-cors google-cloud-vision Pillow

申請兩個 API 金鑰：
    Google Maps API 金鑰，用於顯示地圖。
    Google Cloud Vision API 金鑰，用於圖片辨識。

1. Google Maps API 金鑰
用途：用於顯示地圖並標註位置。
步驟：
前往 Google Cloud Console.

創建一個新的專案或選擇現有專案。

啟用 Maps JavaScript API：

在左側菜單中選擇 API & Services > Library。
搜尋並啟用 Maps JavaScript API。
創建 API 金鑰：

在 API & Services > Credentials 頁面中，選擇 Create Credentials 並選擇 API Key。
複製金鑰並將其放入您的前端代碼中。
例如：
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY"></script>
限制金鑰的使用範圍（建議）：

點擊金鑰名稱，設置 IP 或 HTTP 引用網址限制來保護金鑰，防止未授權使用。    

2. Google Cloud Vision API 金鑰
用途：用於圖片辨識，識別圖片中的社區名稱、建築等標籤。
步驟：
在 Google Cloud Console 中，創建一個新的專案或選擇現有專案。

啟用 Vision API：

在左側菜單中選擇 API & Services > Library。
搜尋並啟用 Cloud Vision API。
創建 服務帳戶金鑰：

在 API & Services > Credentials 頁面，選擇 Create Credentials 並選擇 Service account。
按照提示創建服務帳戶並下載 JSON 格式的金鑰。
配置金鑰：

將下載的 JSON 金鑰文件放在項目中（如 path/to/your/credentials.json）。
設置環境變數來告訴應用程式金鑰位置：
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"