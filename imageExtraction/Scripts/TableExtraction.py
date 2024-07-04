#pip install tabula-py
import tabula
from tabula.io import read_pdf

pdf_path="C:/Users/HP-PC/OneDrive/Documents/git_projects_Repo/Data-Extraction-/imageExtraction/Include/pdf/invoicesample.pdf"
df=tabula.io.read_pdf(pdf_path,stream=True,pages="all")
print(len(df))
print(df[0]) 
dataframe=df[0]
excelFile="C:/Users/HP-PC/OneDrive\Documents/git_projects_Repo/Data-Extraction-/imageExtraction/Include/Excel\Excel1.xlsx"
dataframe.to_excel(excelFile)