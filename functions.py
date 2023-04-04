from TextRedirector import *
import time, webbrowser, shutil
import os

def open_prompt_creator():
    print("Opening prompt creator...")
    url = "https://docs.google.com/spreadsheets/d/1yx2szVvLrSoQKk-acKZ2Gpw1ETpYlXj7aHA2fsRWuJk/edit?fbclid=IwAR2MywzMaqBNbeKKHjEbuHf9FJ9bvcKktHLYs_Ljig4QBG0-YeDDxTXSuaY#gid=0"
    webbrowser.open(url)

def open_MJ():
    print("LOG:: Opening MJ...")
    print("INFO:: I have added a time wait to test how the home button will wait until the whole process is completed")
    time.sleep(5)  # Add a delay of 5 seconds
    print("SUCCESS:: MJ profile opened!")
    # Add your code here to open MJ

def open_MJ_profile():
    print("Opening MJ profile...")
    # Add your code here to open MJ profile

def run_extractor():
    print("Running Extractor...")
    # Add your code here to run the extractor

def run_gigapixel():
    print("Running Gigapixel...")
    # Add your code here to run Gigapixel

def process_in_lightroom():
    print("Processing in Lightroom...")
    # Add your code here to process in Lightroom

def property_releases():
    print("Running Property Releases...")
    # Add your code here to run the property releases

def run_WP2JPG():
    print("Running WP2JPG...")
    # Add your code here to run WP2JPG

def open_folders():
    print("Opening folders...")
    # Add your code here to open folders

def delete_folder_contents():
    print("Deleting folder contents...")
    # List of folders to delete contents from
    folders_to_clear = [   
        'I:/streleases/automation/processed-images',
        'I:/streleases/automation/output-releases',
        'I:/streleases/automation/images',
        'I:/Adobe Stock',
        'I:/Extractor/extract_folder',
        'I:/tempLRimport'
    ]
    print("LOG:: Deleting folder contents...")

    print("Deleted folder contents:\n")

    # Loop through each folder
    for folder in folders_to_clear:
        print(folder + "\n")

        # Check if folder exists
        if not os.path.exists(folder):
            print("\tFolder does not exist\n")
            continue

        # Loop through files in folder and delete them
        for file_name in os.listdir(folder):
            file_path = os.path.join(folder, file_name)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                    print("LOG::\tDeleted file: " + file_name + "\n")
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                    print("LOG::\tDeleted directory: " + file_name + "\n")
            except Exception as e:
                print("LOG::\tFailed to delete: " + file_name + "\n")
                print("LOG::\tError message: " + str(e) + "\n")
    print("SUCCESS:: Folder contents deleted.")


