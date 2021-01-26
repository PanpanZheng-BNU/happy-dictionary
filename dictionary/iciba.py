import urllib.request
import json
import xml.dom.minidom
import xmltodict
from urllib.parse import quote

def iciba(input_text):
    input_text = quote(input_text, 'utf-8')

    url_preString = "http://dict-co.iciba.com/api/dictionary.php?w="
    url_postString_json = "&key=BACC496E7F9A1E527D004E6D4F563417&type=json"
    url_postString_xml = "&key=BACC496E7F9A1E527D004E6D4F563417"

    word_url_xml = url_preString + input_text + url_postString_xml
    xml_codes = urllib.request.urlopen(word_url_xml).read()
    xml_result_to_dict = xmltodict.parse(xml_codes)

    word_url_json = url_preString + input_text + url_postString_json
    json_codes = urllib.request.urlopen(word_url_json).read()
    json_result_to_dict = json.loads(json_codes)

    translate_result = json.dumps({"xml": xml_result_to_dict, "json": json_result_to_dict})

    return translate_result
