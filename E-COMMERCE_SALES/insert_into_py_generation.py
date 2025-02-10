import pandas as pd
import numpy as np

# Wczytaj plik CSV
file_path = r"C:\Users\walcz\Downloads\archive (15)\data.csv"  # <-- Zmień na swoją ścieżkę
df = pd.read_csv(file_path, encoding="ISO-8859-1")  # Lub encoding="latin1"

# Zamiana NaN na None (SQL NULL)
df = df.replace({np.nan: None})

# Nazwa tabeli w SQL
table_name = "ecommerce_sales"
insert_statements = []

# Przetwarzanie każdego wiersza
for _, row in df.iterrows():
    query = "INSERT INTO {} (InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country) VALUES (".format(table_name)
    
    values = [
        "'{}'".format(row['InvoiceNo']) if row['InvoiceNo'] else "NULL",
        "'{}'".format(row['StockCode']) if row['StockCode'] else "NULL",
        "'{}'".format(row['Description'].replace("'", "''")) if row['Description'] else "NULL",
        str(row['Quantity']) if row['Quantity'] is not None else "NULL",
        "TO_DATE('{}', 'YYYY-MM-DD HH24:MI:SS')".format(row['InvoiceDate']) if row['InvoiceDate'] else "NULL",
        str(row['UnitPrice']) if row['UnitPrice'] is not None else "NULL",
        "'{}'".format(row['CustomerID']) if row['CustomerID'] else "NULL",
        "'{}'".format(row['Country']) if row['Country'] else "NULL"
    ]
    
    query += ", ".join(values) + ");"
    insert_statements.append(query)

# Zapisz wynik do pliku SQL
sql_file_path = r"C:\Users\walcz\Downloads\insert_data.sql"
with open(sql_file_path, "w", encoding="utf-8") as f:
    f.write("\n".join(insert_statements))

print(f"Plik {sql_file_path} został wygenerowany!")
