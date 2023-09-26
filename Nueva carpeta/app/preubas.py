from borneo.iam import SignatureProvider
from borneo import NoSQLHandle, NoSQLHandleConfig, Regions, PutRequest
from flask import Flask
#import oci
#from oci.nosql import NosqlClient, models

app = Flask(__name__)

at_provider =SignatureProvider(tenant_id="""ocid1.tenancy.oc1..aaaaaaaa3epwpfrm2lqzabu6lvt2dggy7mixxirw3o4x34s2y23rhh34n6oq',
                               user_id= 'ocid1.user.oc1..aaaaaaaawyygyja6timgy2wvdb5v7kok7d5jmjsoktyxh2ciulip5hnvmomq',
                               private_key='MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAlcqDngFy/rsMUYrkrQWM\
                                TOSGWZnb2fi7dE3agIUszlNok1WxFnSL5c0Pwevi7z5N/hFD6vysGtlJeZZEOxNU\
                                /lkl8Rr7HX5ASjZBigf/nciuPrwjhSeyS433Zxc0Xf0JhZJ9EaC6stEPjU/p6kkm\
                                Nv/0y1UUiKF4riykeOZzDbtNsbgIw2mLB55e5np6tAn7qlk1oeebVMhFQiWVzeq7\
                                YOC/TKZaYD7DPCXAbDei4ab2+OCSMODvVVhTK7X1cEC+yS2RtIxUCestF7or1JbF\
                                c+++EeY8YqMZ8jr8ysY95+Wn7h/uBdZf+clKqWvMWjCF8lGQuN+JppEWJSqqCBgp\
                                ywIDAQAB""",
                                fingerprint= '32:5e:ab:23:3e:2e:b5:91:41:fc:8f:c5:ea:7d:30:6e')
region = Regions.US_CHICAGO_1
config = NoSQLHandleConfig(region, at_provider)
handle = NoSQLHandle(config)
@app.route('/',methods=['POST'])
def poner():
    request= PutRequest().set_table_name(table_name='ic4302_logs')
    request.set_value({'logId': 3,'title': 'hola', 'bagInfo':{'time':'hola'}})
    result = handle.put(request)
    if result.get_version() is not None:
        return 'Si funciona'
    else:
        return 'error'
    
if __name__== '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    



