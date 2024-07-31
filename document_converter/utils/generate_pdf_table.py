from io import BytesIO
from typing import List

from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Table, SimpleDocTemplate, TableStyle, Paragraph


def generate_pdf(
        column_names: List[str], table_data: List[List], custom_page_width=2500,
        custom_page_height=1700
) -> BytesIO:
    buffer = BytesIO()
    # Create a PDF document
    custom_page_size = (custom_page_width, custom_page_height)
    pdf_doc = SimpleDocTemplate(buffer, pagesize=custom_page_size)

    # Format text to the pdf file
    for row in table_data:
        for index, col in enumerate(row):
            if isinstance(col, str):
                row[index] = format_col_text(col)

    for idx, col in enumerate(column_names):
        if col.startswith('Unnamed'):
            column_names[idx] = ' - '

    table_data.insert(0, column_names)
    table = Table(table_data)
    # Add style to the table
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 20),
        ('LEADING', (0, 0), (-1, -1), 24),
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    table.setStyle(style)

    pdf_doc.build([table])

    # Rewind the buffer
    buffer.seek(0)
    return buffer


def format_col_text(text: str, max_length=40) -> str:
    length = len(text)
    formatted_text = [char for char in text]
    split_index = max_length - 1
    for i in range(int(length/max_length)):
        lower_boundary = split_index*i
        higher_boundary = split_index*(i + 1)
        sub_text = text[lower_boundary:higher_boundary]
        blank_space_index = sub_text[::-1].find(' ')
        if blank_space_index != -1:
            formatted_text.insert(
                (higher_boundary - 1) - blank_space_index, '\n'
            )
        else:
            formatted_text.insert(higher_boundary, '\n')
    return "".join(formatted_text)
