from string import Template
import re

with open('liste_commande.txt') as f:
    a = f.readlines()

find_dic = re.compile('{.*}')

s="""class VerdiQueryClass(object):
"""

liste_cmd = []
liste_name = []

for line in a:
    args = line.split(';')
    cmd = args[0]
    liste_cmd.append(cmd)
    name = args[1].strip().replace(' ','_')
    liste_name.append(name)
    doc = args[2].strip()
    if find_dic.search(doc):
        dico = find_dic.search(doc).group(0)
        s+="""    @property
    def $name(self):
        \"\"\"$doc\"\"\"
        dico = $dico
        return self.read_dict_number("$cmd", dico)
"""
    else:
        dico = None    
        s+="""    @property
    def $name(self):
        \"\"\"$doc\"\"\"
        return self.read_number("$cmd")
        
"""
    s=Template(s).safe_substitute(name = name, doc=doc, cmd=cmd, dico=dico)

s+= """
VerdiRS232QueryList = $listecmd

VerdiQueryList = $listename
"""

s = Template(s).safe_substitute(listecmd=liste_cmd, listename=str(liste_name).replace(', ',',\n\t'))                

with open('VerdiQuery.py','w') as f:
    f.write(s)                