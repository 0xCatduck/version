import requests
current_version = "0.0.4"
def check_version(current_version):
    version_url = "https://github.com/dc3n/bybit_risk_management_tool/blob/main/main/version/version.txt"
    try:
        response = requests.get(version_url)
        latest_version = response.text.strip()
        if latest_version > current_version:
            print(f"發現新版本: {latest_version}，您正在運行的版本是: {current_version}")
            
        else:
            print("您的版本是最新的。")
    except Exception as e:
        print(f"版本檢查失敗: {e}")

check_version(current_version)