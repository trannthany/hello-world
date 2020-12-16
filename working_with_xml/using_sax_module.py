import xml.sax

class group_handler(xml.sax.ContentHandler):
    def start_element(self, name, attrs):
        print(name)

handler = group_handler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)