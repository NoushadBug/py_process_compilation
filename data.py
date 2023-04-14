import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from functions import *

global btn_name 

btn_name = {
    "pmt": "Prompt Creator",
    "mj": "MJ",
    "mj_profile": "MJ Profile",
    "extractor": "Extractor",
    "gigapixel": "Gigapixel",
    "lightroom": "Lightroom",
    "property_releases": "Property Releases",
    "wp2jpg": "WP2JPG",
    "delete_contents": "Delete Contents",
    "reset_process": "Reset Process"
}

# Create a dictionary of button information
button_data = {
    btn_name['pmt']: {"bootstyle": INFO, "command": open_prompt_creator},
    btn_name['mj']: {"bootstyle": PRIMARY, "command": open_MJ},
    btn_name['mj_profile']: {"bootstyle": PRIMARY, "command": open_MJ_profile},
    btn_name['extractor']: {"bootstyle": INFO, "command": run_extractor},
    btn_name['gigapixel']: {"bootstyle": INFO, "command": run_gigapixel},
    btn_name['lightroom']: {"bootstyle": PRIMARY, "command": process_in_lightroom},
    btn_name['property_releases']: {"bootstyle": PRIMARY, "command": property_releases},
    btn_name['wp2jpg']: {"bootstyle": INFO, "command": run_WP2JPG},
    btn_name['delete_contents']: {"bootstyle": INFO, "command": delete_folder_contents},
    btn_name['reset_process']: {"bootstyle": PRIMARY, "command": reset},
}
