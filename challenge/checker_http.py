import pycurl
import re
from io import BytesIO

def get(path, regex, code):
    buffer = BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, 'http://' + target + path)
    c.setopt(c.WRITEDATA, buffer)
    c.perform()
    retcode = c.getinfo(pycurl.HTTP_CODE)
    c.close()
    body = buffer.getvalue()
    if code != retcode:
        print("Bad retcode")
        return(False)
    if not re.search(regex, body.decode('iso-8859-1')):
        print("Regex not found")
        return(False)
    return(True)

target = '127.0.0.1:8000'
get('/foo.php', 'bar', 200)
