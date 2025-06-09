import os
import shutil

# ==========================================
# 【設定】 ここで仕分け対象フォルダを指定
# ==========================================

TARGET_FOLDER = "test_folder"

# キーワードと分類先フォルダの対応表
KEYWORD_MAP = {
    "履歴書": "Job",
    "職務経歴": "Job",
    "第五": "Game",
    "大会": "Game",
    "ゲーム": "Game",
    "犬": "Pets",
    "猫": "Pets",
    "ペット": "Pets",
    "todo": "Tasks",
    "タスク": "Tasks",
}

# ==========================================
# 【分類ロジック】 ファイル名からカテゴリを判定
# ==========================================

def categorize_file(filename):
    for keyword, category in KEYWORD_MAP.items():
        if keyword in filename:
            return category
    return "Others"

# ==========================================
# 【移動処理】 指定カテゴリにファイル移動
# ==========================================

def move_file(filepath, category):
    dest_folder = os.path.join(TARGET_FOLDER, category)
    os.makedirs(dest_folder, exist_ok=True)
    dest_path = os.path.join(dest_folder, os.path.basename(filepath))
    shutil.move(filepath, dest_path)

# ==========================================
# 【メイン処理】 フォルダ内の全ファイルを処理
# ==========================================

def process_files():
    for filename in os.listdir(TARGET_FOLDER):
        filepath = os.path.join(TARGET_FOLDER, filename)
        if os.path.isfile(filepath):
            category = categorize_file(filename)
            move_file(filepath, category)
            print(f"✅ {filename} → {category}")

# ==========================================
# 【プログラム実行部】
# ==========================================

if __name__ == "__main__":
    try:
        process_files()
        print("✨ 仕分け処理 完了")
    except Exception as e:
        print(f"❌ エラー発生: {e}")
