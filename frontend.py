import flet as ft
from main import df
import pandas as pd

def main(page:ft.Page):
    page.title = "Albuns Stray Kids"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = 'auto'
    
    
    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nome")),
            ft.DataColumn(ft.Text("Data de Lançamento")),
            ft.DataColumn(ft.Text("Total de Músicas")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(row["Nome"])),
                    ft.DataCell(ft.Text(row["Data de Lançamento"])),
                    ft.DataCell(ft.Text(str(row["Total de Musicas"]))),                
                    ]
            )
            for _, row in df.iterrows()
        ],
    )
    
    page.add(tabela)
    
if __name__ == "__main__":
    ft.app(target=main)
    

    