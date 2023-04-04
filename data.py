import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from functions import *

# Create a dictionary of button information
button_data = {
    "Prompt Creator": {"bootstyle": INFO, "command": open_prompt_creator},
    "MJ": {"bootstyle": PRIMARY, "command": open_MJ},
    "MJ Profile": {"bootstyle": PRIMARY, "command": open_MJ_profile},
    "Extractor": {"bootstyle": INFO, "command": run_extractor},
    "Gigapixel": {"bootstyle": INFO, "command": run_gigapixel},
    "Lightroom": {"bootstyle": PRIMARY, "command": process_in_lightroom},
    "Property Releases": {"bootstyle": PRIMARY, "command": property_releases},
    "WP2JPG": {"bootstyle": INFO, "command": run_WP2JPG},
    "Open Folders": {"bootstyle": INFO, "command": open_folders},
    "Delete Folder Contents": {"bootstyle": PRIMARY, "command": delete_folder_contents},
}