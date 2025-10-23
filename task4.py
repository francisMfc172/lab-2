import xml.dom.minidom as minido

with open('currency.xml', 'r', encoding='windows-1251') as xml_file:
    xml_data = xml_file.read()

# Parse the XML string into a DOM document object
dom = minidom.parseString(xml_data)

#  Normalize the DOM tree (cleans up text nodes and merges adjacent text nodes
dom.normalize()


valute_elements = dom.getElementsByTagName('Valute')


currency_names = []

#  Loop through each 'Valute' element
for valute_element in valute_elements:
    # Extract the 'Nominal' value (first element, then its text content)
    nominal = valute_element.getElementsByTagName('Nominal')[0].firstChild.data
    
    #  Check if the nominal value is '1'
    if nominal == '1':
        # Extract the 'Name' value (first element, then its text content)
        name = valute_element.getElementsByTagName('Name')[0].firstChild.data
        currency_names.append(name)

# Print all collected currency names
for name in currency_names:
    print(name)
