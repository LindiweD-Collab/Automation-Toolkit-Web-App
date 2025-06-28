import io
import pandas as pd

def batch_rename(files, prefix):
    renamed_files = []
    for idx, file in enumerate(files, start=1):
        renamed_files.append(f"{prefix}_{idx}.{file.name.split('.')[-1]}")
    return renamed_files

def csv_to_excel(file):
    df = pd.read_csv(file)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)
    return output.getvalue()

