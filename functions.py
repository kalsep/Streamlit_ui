from config import *

def csv_work(file, file_details):
    data = pd.read_csv(file)
    d_columns = data.columns.to_list()
    data.to_csv(os.path.join(path, "files", file.name), columns=d_columns)
    # return d_columns

def excel_work(file, file_details):
    wb_df = load_workbook(file)
    wb_df.save(os.path.join(path, "files", file.name))
    # api_logs(response, tool_user, ist_date_format, filename, notify)

# def json_work(file, file_details):
#     data = pd.read_json(file)
#     d_columns = data.columns.to_list()
#     data.to_json(os.path.join(path, "files", file.name), columns=d_columns)
#     # return d_columns