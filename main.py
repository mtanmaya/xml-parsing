import xml.etree.ElementTree as ET


def parse_xml(xml_file):
    # create element tree object
    tree = ET.parse(xml_file)

    # get root element
    root = tree.getroot()

    # create empty list for news items
    newsitems = []

    # iterate news items
    for item in root.findall('./channel/item'):
        # empty news dictionary
        news = {}

        # iterate child elements of item
        for child in item:
            # special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']

        # append news dictionary to news items list
        newsitems.append(news)

    # return news items list
    return newsitems


def main():
    # parse xml file
    newsitems = parse_xml('topnewsfeed.xml')
    print(newsitems)


if __name__ == "__main__":
    # calling main function
    main()
