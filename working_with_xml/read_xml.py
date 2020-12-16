# reference https://www.guru99.com/manipulating-xml-with-python.html
import xml.dom.minidom
import xml.etree.ElementTree as ET
import os

file_name = '145101699.xml'
#full_file = os.path.join('working_with_xml', file_name)
full_file = os.path.abspath(os.path.join('working_with_xml', file_name))
def main():
    # doc = xml.dom.minidom.parse("working_with_xml/145101699.xml")
    # print(doc.nodeName)
    # print(doc.firstChild.tagName)
    my_tag_tuple = ('QUOTEID', 'QUOTEDESC', 'CLIENTID', 'REVISIONDATE', 'DELADDR1', 'DELADDR2', 'DELADDR3',
     'SALESPERSON', 'CONTACTPERSON', 'COSTPRICE', 'GROSSPRICE', 'JOBDISCPCNT', 'NETQUOTATION', 'SUBTOTAL', 
     'GSTAMT', 'SELLPRICE', 'DEPOSIT', 'HOURS', 'EXTRCOST', 'SUNEXTRCOST', 'COMPCOST', 'SUNCOMPCOST', 'GLASSCOST', 
     'LINERCOST', 'HARDWARECOST', 'LABOURCOST', 'MISCCOST', 'MATERIALCOST', 'OVERHEADCOST', 'DELIVERYDATE', 'PRODREADYDATE','INVOICECREATED',
     'COMPLETEDATE', 'INVOICEDATE')
    root_node = ET.parse("working_with_xml/145101699.xml").getroot()
    #print(root_node)
    quote_header = root_node.find('QuoteHeader')
    # quote_id = quote_header.find('QUOTEID').text
    # print(f'QUOTEID : {quote_id}')
    # quote_desc = quote_header.find('QUOTEDESC').text
    # print(f'QUOTEDESC : {quote_desc}')
   # print(quote_header.__len__())
    
    #counter = 0
    counter2 = 0
    #while counter < quote_header.__len__():
        #counter += 1
        
    while len(my_tag_tuple)> counter2:
        a = quote_header.find(my_tag_tuple[counter2])
        counter2 += 1
        print(a.text)

    print(root_node.find('QFrames').find('QFrame').find('QFrameHeader').find('QCOLOUR').text)
    


if __name__ == "__main__":
    main()