import cv2
import os
import re
import subprocess

def video_to_frames(video_path, output_folder):
    print(f"處理 {video_path} ...")
    if os.path.exists(output_folder):
        print(f"已存在 {output_folder}, 跳過")
        return
    os.makedirs(output_folder, exist_ok=True)
    subprocess.run(["ffmpeg", "-i", video_path, "-vf", "fps=10", f"{output_folder}{os.sep}%05d.png"], check=True)
    print(f"處理 {video_path} 完成")

def get_video_files(folder_path):
    video_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".mp4") or file.endswith(".webm"):
                video_files.append(os.path.join(root, file))
    return video_files

def video_fn_to_folder(video_path):
    video_fn = os.path.basename(video_path)
    txts = re.match(r'BanG Dream! (.*) 第(.*)話', video_fn)
    folder = f"{re.sub(r'[^a-zA-Z]', '', txts.group(1))}_{re.sub(r'[^0-9]', '', txts.group(2))}"
    folder = os.path.join('docs', 'img', folder)
    return folder

if __name__ == "__main__":
    folder_path = 'videos'
    video_files = get_video_files(folder_path)
    for video_path in video_files:
        folder = video_fn_to_folder(video_path)
        video_to_frames(video_path, folder)