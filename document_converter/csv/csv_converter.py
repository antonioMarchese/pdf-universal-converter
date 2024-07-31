import pandas as pd

from ..utils import generate_pdf, save_pdf
from ..decorators import validate_file_type


@validate_file_type(['csv'])
def convert_csv_to_pdf(file_path: str, output_file_path: str):
    try:
        content = pd.read_csv(file_path).fillna(' ')
        columns = content.columns.tolist()
        rows = content.values.tolist()
        pdf_content = generate_pdf(
            table_data=rows, column_names=columns, custom_page_width=len(columns)*250
        )
        save_pdf(pdf_data=pdf_content, file_path=output_file_path)
        return True
    except Exception as ex:
        print(ex)
        return False
