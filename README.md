# Fasta_scripts
Convert UniProt fasta to excel


`fasta_to_excel.py` converts a single fasta file to excel format

`fasta_to_excel_iterate.py` converts all files in the script's directory ending in ".fasta" to excel format

If you'd like csv instead, just swap out `df.to_excel(file + 'uniprot.xlsx', sheet_name='Sheet1', index=False)
` for `df.to_csv(file + 'uniprot.csv', index=False)`
