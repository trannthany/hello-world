import xml.etree.ElementTree as ET
import os
xmlfile = 'sample.xml'
full_file = os.path.abspath(os.path.join('working_with_xml', xmlfile) )
tree = ET.parse(full_file)
root = tree.getroot()

#ET.dump(tree)

for elm in root.findall("./country[@name='Panama']/"):
    tag_string = elm.tag
    if(tag_string == 'neighbor'):
        print(f'{tag_string} : {elm.attrib}')
    else:
        print(f'{tag_string} : {elm.text}')
    #print(": " + elm.text)