# Fasta scripts
Convert UniProt fasta to excel


`fasta_to_excel.py` converts a single fasta file to excel format

`fasta_to_excel_iterate.py` converts all files in the script's directory ending in ".fasta" to excel format

If you'd like csv instead, just swap out `df.to_excel(file + 'uniprot.xlsx', sheet_name='Sheet1', index=False)
` for `df.to_csv(file + 'uniprot.csv', index=False)`


The scripts do not parse out sequence version 'SV=' or protein existence 'PE=' for TrEMBL entries, but this would only need some slight modification to accomplish.


# Download XML
Download individual XML files for each uniprot ID entered

Edit the list for `download_uniprot_xml_pages.py`
Or modify the code to open a list from a txt or csv file.
