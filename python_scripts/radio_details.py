import sys;
import urllib.request;
import codecs;
import xml.etree.ElementTree as ET;

elementToFind = sys.argv[1];

#url = 'http://20873.live.streamtheworld.com/RFMAAC_SC?DIST=TuneIn&TGT=TuneIn&maxServers=2&partnertok=eyJhbGciOiJIUzI1NiIsImtpZCI6InR1bmVpbiIsInR5cCI6IkpXVCJ9.eyJ0cnVzdGVkX3BhcnRuZXIiOnRydWUsImlhdCI6MTYxOTExMzEwMiwiaXNzIjoidGlzcnYifQ.FjRBrU7cSjG50bqljECMOlXPSAPIr5xDeP5yZH2kWXY';
url = 'https://configsa01.blob.core.windows.net/rfm/rfmOnAir.xml';
filename = '/config/www/downloads/rfm.xml';

urllib.request.urlretrieve(url, filename);
with codecs.open(filename, 'r', encoding='utf16') as f: text = f.read();
with codecs.open(filename, 'w', encoding='utf8') as f: f.write(text);

root = ET.fromstring(text);

for name in root.iter(elementToFind):
    print(name.text)