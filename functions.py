from TextRedirector import *
import time, webbrowser, shutil
import data, os
import subprocess

def get_config_value(key):
    with open('config.txt', 'r') as file:
        for line in file:
            if line.startswith(key):
                return line.split('= ')[1].strip()
    return ''

def open_prompt_creator():
    btn_name = data.btn_name['pmt']
    try:
        print("LOG:: Opening prompt creator...")
        url = get_config_value('promptSheet')
        webbrowser.open(url)
        print("SUCCESS:: Prompt creator opened!")
    except Exception as e:
        print("ERROR:: Could not open prompt creator due to:", e)
    setProcessStatus(btn_name, "SUCCESS")

def open_MJ():
    btn_name = data.btn_name['mj']
    try:
        print("LOG:: Opening MJ...")
        url = get_config_value('mjURL')
        webbrowser.open(url)
        print("INFO:: MJ Opened in browser")
        time.sleep(10)
        print("LOG:: Running bat file...")
        fh = os.popen(get_config_value('mjbatdirectory'))
        output = fh.read()
        print(output)
        fh.close()
        print("INFO:: Bat file completed successfully")
        print("SUCCESS:: process completed!")
    except FileNotFoundError:
        print("ERROR:: directory "+get_config_value('mjbatdirectory')+" not found")
    setProcessStatus(btn_name, "SUCCESS")

def open_MJ_profile():
    btn_name = data.btn_name['mj_profile']
    try:
        print("LOG:: Opening MJ profile...")
        url = get_config_value('mjProfile')
        print("LOG:: url: "+ url)
        webbrowser.open(url)
        print("SUCCESS:: MJ profile opened!")
    except Exception as e:
        print("ERROR:: Could not open MJ profile due to:", e)
    setProcessStatus(btn_name, "SUCCESS")

def run_extractor():
    btn_name = data.btn_name['extractor']
    try:
        print("LOG:: Running Extractor bat file...")
        fh = os.popen(get_config_value('extractorDirectory'))
        output = fh.read()
        print(output)
        fh.close()
        print("INFO:: Bat file completed successfully")
        print("SUCCESS:: process completed!")
    except FileNotFoundError:
        print("ERROR:: directory "+get_config_value('extractorDirectory')+" not found")
    setProcessStatus(btn_name, "SUCCESS")

def run_gigapixel():
    btn_name = data.btn_name['gigapixel']
    try:
        print("LOG:: Running Gigapixel...")
        exe_path = get_config_value('gigapixelDirectory')
        subprocess.Popen(exe_path)
        print("SUCCESS: Gigapixel AI app opened!")
    except FileNotFoundError:
        print("ERROR:: Directory "+get_config_value('gigapixelDirectory')+" not found")

    setProcessStatus(btn_name, "SUCCESS")

def process_in_lightroom():
    btn_name = data.btn_name['lightroom']
    try:
        print("LOG:: Running Lightroom...")
        exe_path = get_config_value('lightroomDirectory')
        subprocess.Popen(exe_path)
        print("SUCCESS: Lightroom app opened!")
    except FileNotFoundError:
        print("ERROR:: Directory "+get_config_value('lightroomDirectory')+" not found")

    setProcessStatus(btn_name, "SUCCESS")

def property_releases():
    btn_name = data.btn_name['property_releases']
    try:
        print("LOG:: Running Property Release bat file...")
        fh = os.popen(get_config_value('propertyDirectory'))
        output = fh.read()
        print(output)
        fh.close()
        print("INFO:: Bat file started")
        print("SUCCESS:: Property Release process started!")
    except FileNotFoundError:
        print("ERROR:: directory "+get_config_value('propertyDirectory')+" not found")
    
    setProcessStatus(btn_name, "SUCCESS")

def run_WP2JPG():
    btn_name = data.btn_name['wp2jpg']
    try:
        print("LOG:: Running WP2JPG...")
        exe_path = get_config_value('wp2jpgDirectory')
        subprocess.Popen(exe_path)
        print("SUCCESS: WP2JPG app opened!")
    except FileNotFoundError:
        print("ERROR:: Directory "+get_config_value('wp2jpgDirectory')+" not found")
    
    setProcessStatus(btn_name, "SUCCESS")

def delete_folder_contents():
    btn_name = data.btn_name['delete_contents']
    print("LOG:: Deleting folder contents...")
    # Get folders_to_clear list from config.txt
    folders_to_clear = get_config_value('foldersToClear').split(', ')

    # Loop through each folder
    for folder in folders_to_clear:
        print("INFO:: Deleting "+folder)

        # Check if folder exists
        if not os.path.exists(folder):
            print("ERROR:: Folder does not exist\n")
            continue

        # Loop through files in folder and delete them
        for root, dirs, files in os.walk(folder):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                try:
                    os.unlink(file_path)
                    print("LOG:: Deleted file: " + file_name + "\n")
                except Exception as e:
                    print("LOG:: Failed to delete: " + file_name + "\n")
                    print("LOG:: Error message: " + str(e) + "\n")

            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                try:
                    shutil.rmtree(dir_path)
                    print("LOG:: Deleted directory: " + dir_name + "\n")
                except Exception as e:
                    print("LOG:: Failed to delete: " + dir_name + "\n")
                    print("LOG:: Error message: " + str(e) + "\n")

    print("SUCCESS:: Task Completed.")
    setProcessStatus(btn_name, "SUCCESS")

def reset():
    # btn_name = data.btn_name['reset_process']
    with open("server.txt", "w") as f:
        f.write("Success:\n")
        f.write("Error:\n")
    
    # setProcessStatus(btn_name, "SUCCESS")

def setProcessStatus(button_name, status):
    # Create the file if it doesn't exist
    if not os.path.exists("server.txt"):
        with open("server.txt", "w") as f:
            f.write("Success:\n")
            f.write("Error:\n")
    
    # Read the contents of the file
    with open("server.txt", "r") as f:
        contents = f.readlines()
    
    # Get the success and error lists from the file
    success_list = [s.strip() for s in contents[0].split(":")[1].split(",") if s.strip()]
    error_list = [s.strip() for s in contents[1].split(":")[1].split(",") if s.strip()]
    
    # Add the button name to the appropriate list based on the status
    if status == "SUCCESS" and button_name not in success_list:
        success_list.append(button_name)
    elif status == "ERROR" and button_name not in error_list:
        error_list.append(button_name)
    
    # Write the updated lists back to the file
    with open("server.txt", "w") as f:
        f.write("Success: " + ", ".join(success_list) + "\n")
        f.write("Error: " + ", ".join(error_list) + "\n")
