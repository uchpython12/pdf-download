import os
import random
import shutil

pdf_name = ''
# 指定要打亂檔案名稱的資料夾
folder_path = pdf_name + '_下載'  # 替換成你的資料夾路徑
output_folder = pdf_name + '_原圖'  # 新資料夾的路徑

# 如果新資料夾不存在，則建立新資料夾
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 取得資料夾內所有檔案名稱列表
file_names = os.listdir(folder_path)

# 打亂檔案名稱列表
random.shuffle(file_names)

# 將打亂的檔案複製到新資料夾中，並使用隨機值作為新的檔案名稱
for idx, file_name in enumerate(file_names):
    old_file_path = os.path.join(folder_path, file_name)
    # 產生隨機值作為新檔案名稱
    random_name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=8))
    file_extension = os.path.splitext(file_name)[1]  # 取得檔案副檔名
    new_file_name = f"{random_name}_{idx}{file_extension}"
    new_file_path = os.path.join(output_folder, new_file_name)
    shutil.copyfile(old_file_path, new_file_path)
