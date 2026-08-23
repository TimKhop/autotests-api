import xml.etree.ElementTree as ET

xml_data = """
<user>
    <id>1</id>
    <name>Lord Jim</name>
    <email>jim@mail.ru</email>
</user>
"""

root = ET.fromstring(xml_data)

