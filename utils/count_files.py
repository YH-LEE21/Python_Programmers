from collections import Counter
from datetime import datetime
import os

home_url = "https://github.com/YH-LEE21/Python_Programmers/tree/main"

def count_files():
    files_info = []
    total_file_count = 0
    directory_list = [directory for directory in os.listdir("./") if directory.find(".") == -1]
    directory_list.sort()
    directory_list.remove("utils")
    for directory in directory_list:
        file_list = os.listdir(f"./{directory}")
        file_count = len(file_list)
        file_url = home_url+"/"+directory
        temp = [directory, file_count,file_url]
        files_info.append(temp)
        total_file_count += file_count
    return files_info, total_file_count
  
  
# 내가 보여주고 싶은 모든 파일 수, 각 폴더마다 있는 폴더 수   
def make_info(files_info, total_file_count):
    info = f"## Files Count In Folders\nTotal File Count: {total_file_count}\n"
    for directory_files_info in files_info:
        temp = f"""- <a href={directory_files_info[2]}>{directory_files_info[0]}</a> : {directory_files_info[1]}\n"""
        info += temp
    return info
    


# README.md에 보여지는 내용
def make_read_me(info):
    return f"""# Programmers with Python
Push할 때마다 폴더 별 파일 수를 리드미에 자동으로 업데이트<br>
Automatically update the number of files per folder to Readme whenever you push.<br><br>
{info}
"""


# push 할때
def update_readme():
    files_info, total_file_count = count_files()
    info = make_info(files_info, total_file_count)
    readme = make_read_me(info)
    return readme


if __name__ == "__main__":
    readme = update_readme()
    with open("./README.md", 'w', encoding='utf-8') as f:
        f.write(readme)
