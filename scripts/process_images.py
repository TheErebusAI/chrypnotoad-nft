#!/usr/bin/env python3
import os
import zipfile
import json
import shutil
from pathlib import Path

SOURCE_DIR = "/home/erebus/usb/chrypnotoad_nft"
DEST_DIR = "/home/erebus/persistent/chrypnotoad_nft_project/assets"
METADATA_DIR = "/home/erebus/persistent/chrypnotoad_nft_project/metadata"

def extract_all_images():
    """Extract all images from zip files and create inventory"""
    raw_dir = Path(DEST_DIR) / "raw"
    raw_dir.mkdir(exist_ok=True)
    
    inventory = []
    
    for zip_file in sorted(Path(SOURCE_DIR).glob("*.zip")):
        print(f"Processing {zip_file.name}")
        with zipfile.ZipFile(zip_file, 'r') as zf:
            for file_info in zf.infolist():
                if file_info.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                    # Extract file
                    zf.extract(file_info, raw_dir)
                    
                    # Add to inventory
                    inventory.append({
                        'original_zip': zip_file.name,
                        'filename': file_info.filename,
                        'size': file_info.file_size,
                        'modified_date': file_info.date_time
                    })
    
    # Save inventory
    Path(METADATA_DIR).mkdir(exist_ok=True)
    with open(Path(METADATA_DIR) / "image_inventory.json", 'w') as f:
        json.dump(inventory, f, indent=2, default=str)
    
    print(f"Total images processed: {len(inventory)}")
    return inventory

if __name__ == "__main__":
    inventory = extract_all_images()