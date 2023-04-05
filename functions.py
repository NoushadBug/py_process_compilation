from TextRedirector import *
import time, webbrowser, shutil
import os
import subprocess

def get_config_value(key):
    with open('config.txt', 'r') as file:
        for line in file:
            if line.startswith(key):
                return line.split('= ')[1].strip()
    return ''

def open_prompt_creator():
    try:
        print("LOG:: Opening prompt creator...")
        url = get_config_value('promptSheet')
        webbrowser.open(url)
        print("SUCCESS:: Prompt creator opened!")
    except Exception as e:
        print("ERROR:: Could not open prompt creator due to:", e)

def open_MJ():
    try:
        print("LOG:: Opening MJ...")
        url = get_config_value('mjURL')
        webbrowser.open(url)
        print("INFO:: MJ Opened in browser")
        time.sleep(10)
        print("LOG:: Running bat file...")
        subprocess.call([get_config_value('mjbatdirectory')])
        print("INFO:: Bat file completed successfully")
        print("SUCCESS:: process completed!")
    except FileNotFoundError:
        print("ERROR:: directory "+get_config_value('mjbatdirectory')+" not found")


def open_MJ_profile():
    try:
        print("LOG:: Opening MJ profile...")
        url = get_config_value('mjProfile')
        print("LOG:: url: "+ url)
        webbrowser.open(url)
        print("SUCCESS:: MJ profile opened!")
    except Exception as e:
        print("ERROR:: Could not open MJ profile due to:", e)

def run_extractor():
    try:
        print("LOG:: Running Extractor bat file...")
        subprocess.call([get_config_value('extractorDirectory')])
        print("INFO:: Bat file completed successfully")
        print("SUCCESS:: process completed!")
    except FileNotFoundError:
        print("ERROR:: directory "+get_config_value('extractorDirectory')+" not found")

def run_gigapixel():
    try:
        print("LOG:: Running Gigapixel...")
        exe_path = get_config_value('gigapixelDirectory')
        subprocess.Popen(exe_path)
        print("SUCCESS: Gigapixel AI app opened!")
    except FileNotFoundError:
        print("ERROR:: Directory "+get_config_value('gigapixelDirectory')+" not found")

def process_in_lightroom():
    try:
        print("LOG:: Running Lightroom...")
        exe_path = get_config_value('lightroomDirectory')
        subprocess.Popen(exe_path)
        print("SUCCESS: Lightroom app opened!")
    except FileNotFoundError:
        print("ERROR:: Directory "+get_config_value('lightroomDirectory')+" not found")

def property_releases():
    try:
        print("LOG:: Running Property Release bat file...")
        subprocess.call([get_config_value('propertyDirectory')])
        print("INFO:: Bat file completed successfully")
        print("SUCCESS:: Property Release process completed!")
    except FileNotFoundError:
        print("ERROR:: directory "+get_config_value('propertyDirectory')+" not found")

def run_WP2JPG():
    try:
        print("LOG:: Running WP2JPG...")
        exe_path = get_config_value('wp2jpgDirectory')
        subprocess.Popen(exe_path)
        print("SUCCESS: WP2JPG app opened!")
    except FileNotFoundError:
        print("ERROR:: Directory "+get_config_value('wp2jpgDirectory')+" not found")


def delete_folder_contents():
    print("LOG:: Deleting folder contents...")
    # Get folders_to_clear list from config.txt
    folders_to_clear = get_config_value('foldersToClear').split(',')

    # Loop through each folder
    for folder in folders_to_clear:
        print("INFO:: Deleting "+folder)

        # Check if folder exists
        if not os.path.exists(folder):
            print("ERROR:: Folder does not exist\n")
            continue

        # Loop through files in folder and delete them
        for file_name in os.listdir(folder):
            file_path = os.path.join(folder, file_name)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                    print("LOG:: Deleted file: " + file_name + "\n")
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    print("LOG:: Deleted directory: " + file_name + "\n")
            except Exception as e:
                print("LOG:: Failed to delete: " + file_name + "\n")
                print("LOG:: Error message: " + str(e) + "\n")
    print("SUCCESS:: Task Completed.")

