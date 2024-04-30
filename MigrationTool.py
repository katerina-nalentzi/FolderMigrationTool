import os
import shutil

def copy_matching_folders(source_directory, destination_directory, folder_names_file):
    
    os.makedirs(destination_directory, exist_ok=True)

    with open(folder_names_file, 'r') as file:
        folder_names = [line.strip() for line in file.readlines()]

    for folder_name in folder_names:
        source_folder_path = os.path.join(source_directory, folder_name)
        destination_folder_path = os.path.join(destination_directory, folder_name)
        
        
        if os.path.exists(destination_folder_path):
            continue  # Skip to the next folder_name in the loop if folder exists

        if os.path.exists(source_folder_path):
            shutil.copytree(source_folder_path, destination_folder_path)

folder_names_file = r'path\to\ids.txt'  
source_directory = r'path\to\dataset'  
destination_directory = r'new\directory'  

copy_matching_folders(source_directory, destination_directory, folder_names_file)
