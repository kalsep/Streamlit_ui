import time

import pandas as pd
from functions import *
from config import *


def app():
    pre_files_user = {'Regression': 'Logistic Regression', 'Classification': 'Classification'}
    c1, c2 = st.columns([1, 3])  # dividing the page to columns
    file = c1.file_uploader('Upload A dataset')
    # pre_file = c2.selectbox('Select Machine Learning Task', list(pre_files_user.keys()))
    load = c1.button('⬆️ Load Dataset')
    notify = c2.empty()

    if load:
        if file is not None:
            file_details = {"FileName": file.name, "FileType": file.type}
            # notify.write(type(file_details['FileName']))
            # # notify.write(file_details.keys())
            # # notify.write(file_details.values())
            # notify.write('before file upload')
            # time.sleep(2)
            # def save_uploadedfile(file):
            #     notify.success('Inside upload')
            #     with open(os.path.join(path, "files", file.name), "wb") as f:
            #         f.write(file.getbuffer())
            #     return notify.success("Saved File:{} to tempDir".format(file.name))
            #
            # notify.write('after file upload')
            # time.sleep(2)

            if '.csv' in file_details['FileName']:
                # data = pd.read_csv(file)
                columns = csv_work(file, file_details)
                notify.write(type(columns))

            elif '.xlsx' in file_details['FileName']:
                data = pd.read_excel(file)
                excel_work(file, file_details)


            # elif '.json' in file_details['FileName']:
            #     data = pd.read_json(file)
            #     json_work(file, file_details)
