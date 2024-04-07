
import pandas as pd
from openpyxl import load_workbook
from os import path

def read_excel(*args):
    inputfile = path.join(*args)

    assert path.exists(inputfile), f"Caminho para o arquivo não existe:\n{inputfile}"

    frame = pd.read_excel(inputfile,
                    index_col="DATA",
                    parse_dates=['DATA'],
                    engine='openpyxl')

    return frame


def append_excel(frame, dest):
    writer = pd.ExcelWriter(dest, engine='openpyxl')
    writer.book = load_workbook(dest)

    writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets if ws.title != "Sheet1")

    reader = pd.read_excel(dest, engine="openpyxl")
    reader.dropna(how='all', axis=0)

    frame.to_excel(writer,
                sheet_name="Planilha1",
                index=False,
                header=False,
                startrow=len(reader))

    writer.close()
