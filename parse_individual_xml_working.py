from Bio import SeqIO
import re
import xml.etree.cElementTree as ET
import pandas as pd
import os

columns = ['Uniprot_ID', 'protein_name', 'gene_name', 'description', 'ATP_binding',
           'binding_type', 'binding_location_start', 'binding_location_end', 'sequence']

df = pd.DataFrame(columns=columns)


#file2 = 'A7J1Q9.xml'
#file = 'XML/Q8WZ42.xml'
#filename = file.split('/')[-1]
#print(filename)

#columns = ['Uniprot_ID', 'protein_name', 'gene_name', 'description', 'ATP_binding', 'binding_type', 'binding_location', 'sequence']

df_counter = 0  # keep track of the df row we're appending
for file in os.listdir('XML/'):
    if file.endswith(".xml"):
        print(file)
        filepath = 'XML/' + file

        record = SeqIO.read(filepath, "uniprot-xml")
        #print(record)
        
        tree = ET.ElementTree(file=filepath)
        root = tree.getroot()
        
        
        print('---------')
        
        uniprot_ID = re.search(r'ID:\s(.*)', str(record))
        uniprot_ID = uniprot_ID.group(0)
        uniprot_ID = uniprot_ID.split(' ')[1]
        
        #print(uniprot_ID)
        
        try:
            protein_name = re.search(r'Name:\s(.*)', str(record))
            protein_name = protein_name.group(0)
            protein_name = protein_name.split(' ')[1]
        except:
            pass
        #print(protein_name)
        
        try:
            gene_name = re.search(r'gene_name_primary=(.*)', str(record))
            gene_name = gene_name.group(0)
            gene_name = gene_name.split('=')[1]
        except:
            pass
        #print(gene_name)
        
        try:
            uniprot_description = re.search(r'Description:\s(.*)', str(record))
            uniprot_description = uniprot_description.group(0)
            uniprot_description = uniprot_description.split(': ')[1]

        except:
            pass
        #print(uniprot_description)
        
        # extract sequence as a string
        sequence = record.seq
        sequence = str(sequence)
        #print(sequence)
        
        
        # I'm really sorry to whomever tries to untangle this in the future
        # essentially, I'm trying to extract features with 'ATP' binding and get the positions
        # this stuff is buried in the xml file
        
        my_iter = tree.iter()

        for elem in my_iter:
            if elem.tag == '{http://uniprot.org/uniprot}feature':
                try:
                    if elem.attrib['description'] == 'ATP':
                        #print(elem.attrib)
                        ATP_binding = 'ATP'
                        binding_type = elem.attrib['type']
        
                        if binding_type == 'binding site':
                            feature_children = elem.getchildren()
        
                            for feature_child in feature_children:
                                ft_grandchildren = feature_child.getchildren()
        
                                for ft_grandchild in ft_grandchildren:
                                    #print(ft_grandchild.attrib)
                                    binding_location_start = ft_grandchild.attrib['position']
                                    binding_location_end = ft_grandchild.attrib['position']
        
                        elif binding_type == 'nucleotide phosphate-binding region':
                            feature_children = elem.getchildren()
        
                            for feature_child in feature_children:
                                ft_grandchildren = feature_child.getchildren()
                                #binding_location = []
                                region_counter = 0
                                for ft_grandchild in ft_grandchildren:
                                    if region_counter == 0:
                                        binding_location_start = ft_grandchild.attrib['position']
                                    else:
                                        binding_location_end = ft_grandchild.attrib['position']
                                    region_counter +=1
        
                                    #print(ft_grandchild.attrib)
                                    #binding_location.append(ft_grandchild.attrib['position'])
                                    #binding_location = ft_grandchild.attrib['position']
        
                        #print(ATP_binding)
                        #print(binding_type)
                        #print(binding_location)
        
                        row_list = [uniprot_ID, protein_name, gene_name, uniprot_description, ATP_binding,
                                    binding_type, binding_location_start, binding_location_end, sequence]
        
                        print(row_list)
                        df.loc[df_counter] = row_list
                        df_counter += 1
        
                except:
                    pass  # for lines that don't have atp, pass

#df.append(series)
print('')
#print(df.head())
df.to_excel('ATP_binding_sites.xlsx', sheet_name='Sheet1', index=False)




# Structure of features in XML file, pulls out the info for ATP binding sites and regions:
'''
<feature type="binding site" description="ATP" evidence="26">  # elem, extract attrib for type and description
<location>                                                     # child
<position position="32207"/>                                   # grandchild, extract attrib {position:'32207'}
</location>
</feature>
'''

'''
<feature type="nucleotide phosphate-binding region" description="ATP" evidence="26">
<location>
<begin position="32184"/>
<end position="32192"/>
</location>
</feature>
'''
