import urllib

id_list = ['B4E2N9', 'B5BUK7', 'B7Z3W6']

no_isoform_list = [x for x in id_list if '-' not in x]

print(id_list)
print(no_isoform_list)

for i in no_isoform_list:
    urllib.request.urlretrieve('http://www.uniprot.org/uniprot/' + i + '.xml', i + '.xml')


