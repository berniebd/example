import shutil
from PIL import Image
from pytesseract import pytesseract
import requests

__author__ = 'bida'


def get_random_code():
    resp = requests.get("http://10.3.254.23:8080/dangwebx/randCodeImage?a=1444784364985", stream=True)
    with open("tmp.png", "wb") as f:
        f.write(resp.raw.read())
        # or
        shutil.copyfileobj(resp.raw, f)

    image = Image.open("tmp.png")
    return pytesseract.image_to_string(image)


if __name__ == '__main__':
    session = requests.Session()

    data = dict()
    data['username_'] = 'bida'
    data['password_'] = '123456!qwert'
    data['userKey'] = 'D1B5CC2FE46C4CC983C073BCA897935608D926CD32992B5900'
    rand_code = get_random_code()
    print rand_code
    data['randCode'] = rand_code

    resp = session.post('http://10.3.254.23:8080/dangwebx/security_check_', data=data)
    print resp.content

    print session.post('http://10.3.254.23:8080/dangwebx/tms/base/baseEntrepotController.do?datagrid&field=id,no,name,type,provinceTxt,cityTxt,areaTxt,streetTxt,address,comment,status,chinesename,updateTime,updateTime_begin,updateTime_end,',
                       data={'page': 1, 'rows': 10}).content

