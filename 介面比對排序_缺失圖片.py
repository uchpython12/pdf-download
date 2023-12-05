import shutil
import os
import imagehash
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


def compare_images():
    current_directory = os.getcwd()  # 取得當前目錄路徑
    folder_a_path = filedialog.askdirectory(title="選擇下載資料夾", initialdir=current_directory)
    folder_b_path = filedialog.askdirectory(title="選擇原圖資料夾", initialdir=current_directory)
    folder_name = os.path.basename(folder_b_path)
    output_folder = folder_name + '排序好的資料夾'

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    images_a = os.listdir(folder_a_path)
    images_b = os.listdir(folder_b_path)

    progress_bar["maximum"] = len(images_a)
    count = 0

    missing_images = []

    for image_a_name in images_a:
        image_a_path = os.path.join(folder_a_path, image_a_name)
        with Image.open(image_a_path) as img:
            image_a_hash = imagehash.average_hash(img)

        found = False
        for image_b_name in images_b:
            image_b_path = os.path.join(folder_b_path, image_b_name)
            with Image.open(image_b_path) as img:
                image_b_hash = imagehash.average_hash(img)

            if image_a_hash == image_b_hash:
                found = True
                new_image_name = f"{image_a_name}"
                new_image_path = os.path.join(output_folder, new_image_name)
                shutil.copyfile(image_b_path, new_image_path)
                status_label.config(text=f"找到相同圖像 '{image_a_name}' 並已保存到新資料夾")
                break

        if not found:
            missing_images.append(image_a_name)

        count += 1
        progress_bar["value"] = count
        progress_bar.update()

    if missing_images:
        missing_images_sorted = sorted(missing_images)  # 對找不到的圖片列表進行排序
        missing_images_str = ", ".join(missing_images_sorted)
        save_to_file(missing_images_str, folder_name)  # 傳遞 folder_name 參數給 save_to_file 函數

    tk.messagebox.showinfo("完成", "圖片比對已完成！")


def save_to_file(missing_images_str, folder_name):
    file_name = folder_name + ".txt"  # 將檔案名稱設定為資料夾名稱加上 .txt
    with open(file_name, 'w') as file:
        file.write(f"缺失圖片: {missing_images_str}")

root = tk.Tk()
root.title("圖片比對")

compare_button = tk.Button(root, text="比對圖片", command=compare_images)
compare_button.pack(padx=20, pady=10)

status_label = tk.Label(root, text="")
status_label.pack(padx=20, pady=5)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.pack(padx=20, pady=5)

root.mainloop()
