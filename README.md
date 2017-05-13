## Fasta scripts
Convert UniProt fasta to excel


`fasta_to_excel.py` converts a single fasta file to excel format

`fasta_to_excel_iterate.py` converts all files in the script's directory ending in ".fasta" to excel format

If you'd like csv instead, just swap out `df.to_excel(file + 'uniprot.xlsx', sheet_name='Sheet1', index=False)
` for `df.to_csv(file + 'uniprot.csv', index=False)`


The scripts do not parse out sequence version 'SV=' or protein existence 'PE=' for TrEMBL entries, but this would only need some slight modification to accomplish.


## Download XML
Download individual XML files for each uniprot ID entered

Edit the list inside `download_uniprot_xml_pages.py` and run.
Or modify the code to open a list from a txt or csv file.


## Parse the XML files
Create a folder called XML with all of your uniprot xml files contained.
`parse_individual_xml_working.py` will navigate to this folder and extract the UniProt ID, protein, gene name, description, sequence,and is currently set up to extract information from any features that include ATP binding. If this seems useful, it could be modified to extract any other information that is contained within the XML.
