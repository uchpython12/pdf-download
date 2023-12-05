import fitz  # PyMuPDF
import os
import tkinter as tk
from tkinter import filedialog

def extract_images_from_pdf(pdf_file, output_folder):
    # 打開 PDF 檔案
    pdf_document = fitz.open(pdf_file)

    # 逐頁提取圖片
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        images = page.get_images(full=True)

        for img_index, img_info in enumerate(images):
            xref = img_info[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image = open(f"{output_folder}/{page_num + 1}.png", "wb")
            image.write(image_bytes)
            image.close()

    # 關閉 PDF 檔案
    pdf_document.close()

def select_pdf_file():
    # 使用檔案選擇器來選擇 PDF 檔案
    pdf_file_path = filedialog.askopenfilename(title="選擇 PDF 檔案")
    entry.delete(0, tk.END)
    entry.insert(0, pdf_file_path)

def extract_images():
    # 提取圖片
    pdf_file_path = entry.get()
    pdf_name = os.path.splitext(os.path.basename(pdf_file_path))[0]
    output_folder_path = pdf_name + "_下載"

    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    extract_images_from_pdf(pdf_file_path, output_folder_path)
    status_label.config(text="圖片提取完成！")

# 創建 Tkinter 的根視窗
root = tk.Tk()
root.title("PDF 圖片提取器")

# 創建選擇 PDF 檔案的按鈕和輸入框
select_button = tk.Button(root, text="選擇 PDF 檔案", command=select_pdf_file)
select_button.pack(padx=20, pady=10)

entry = tk.Entry(root, width=50)
entry.pack(padx=20, pady=5)

# 創建提取圖片的按鈕
extract_button = tk.Button(root, text="提取圖片", command=extract_images)
extract_button.pack(padx=20, pady=10)

# 顯示狀態的標籤
status_label = tk.Label(root, text="")
status_label.pack(padx=20, pady=5)

# 啟動主循環
root.mainloop()
