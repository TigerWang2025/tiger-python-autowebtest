import pandas as pd


class ExcelReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_excel(file_path, sheet_name=None)

    def get_sheet_by_name(self, sheet_name):
        return self.data.get(sheet_name, None)

    def get_sheet_by_index(self, sheet_index):
        sheet_names = list(self.data.keys())
        if 0 <= sheet_index < len(sheet_names):
            return self.data[sheet_names[sheet_index]]
        return None

    def excel_to_dict(self, sheet_name):
        if isinstance(sheet_name, int):
            sheet = self.get_sheet_by_index(sheet_name)
        else:
            sheet = self.get_sheet_by_name(sheet_name)

        if sheet is None:
            raise ValueError(f"Sheet '{sheet_name}' not found")

        sheet = sheet.fillna('')
        return sheet.to_dict(orient='records')
