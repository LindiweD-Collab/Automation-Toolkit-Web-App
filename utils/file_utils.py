import os
import shutil
import zipfile
import io
import pandas as pd
from datetime import datetime

def batch_rename_and_save(files, prefix, save_dir="renamed_files", log_dir="logs"):
    os.makedirs(save_dir, exist_ok=True)
    os.makedirs(log_dir, exist_ok=True)

    renamed_paths = []
    log_entries = []

    for idx, file in enumerate(files, start=1):
        ext = file.name.split('.')[-1]
        new_name = f"{prefix}_{idx}.{ext}"
        save_path = os.path.join(save_dir, new_name)

        with open(save_path, "wb") as f:
            f.write(file.getbuffer())

        renamed_paths.append(save_path)
        log_entries.append(f"[{datetime.now()}] Renamed '{file.name}' to '{new_name}'")

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_path = os.path.join(log_dir, f"rename_log_{timestamp}.txt")
    with open(log_path, "w") as log_file:
        log_file.write("\n".join(log_entries))

    return renamed_paths, log_path


def zip_files(file_paths, zip_name="renamed_files.zip"):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as zipf:
        for path in file_paths:
            zipf.write(path, arcname=os.path.basename(path))
    buffer.seek(0)
    return buffer

def csv_to_excel(file):
    df = pd.read_csv(file)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')
    output.seek(0)
    return output.getvalue()
