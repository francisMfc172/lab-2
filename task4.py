import xml.dom.minidom as minidom

with open('currency.xml', 'r', encoding='windows-1251') as xml_file:
    xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

valute_elements = dom.getElementsByTagName('Valute')

currency_names = []

for valute_element in valute_elements:
    nominal = valute_element.getElementsByTagName('Nominal')[0].firstChild.data
    if nominal == '1':
        name = valute_element.getElementsByTagName('Name')[0].firstChild.data
        currency_names.append(name)

for name in currency_names:
    print(name)
