from borneo.iam import SignatureProvider
from borneo import NoSQLHandle, NoSQLHandleConfig, Regions, PutRequest
from flask import Flask, request
from datetime import datetime
#import oci
#from oci.nosql import NosqlClient, models

app = Flask(__name__)

at_provider =SignatureProvider(tenant_id="""ocid1.tenancy.oc1..aaaaaaaa3epwpfrm2lqzabu6lvt2dggy7mixxirw3o4x34s2y23rhh34n6oq',
                               user_id= 'ocid1.user.oc1..aaaaaaaawyygyja6timgy2wvdb5v7kok7d5jmjsoktyxh2ciulip5hnvmomq',
                               private_key='/app/.oci/oci_api_key.pem""",
                                fingerprint= '32:5e:ab:23:3e:2e:b5:91:41:fc:8f:c5:ea:7d:30:6e')
region = Regions.US_CHICAGO_1
config = NoSQLHandleConfig(region, at_provider)
handle = NoSQLHandle(config)
@app.route('/',methods=['POST'])
def poner():
    bus = PutRequest().set_table_name(table_name='ic4302_logs')
    bus.set_value({'logId': 3,'title': 'hola', 'bagInfo':{'time':'hola'}})
    result = handle.put(bus)
    print(request.url)
    print(datetime.now())
    if result.get_version() is not None:
        return 'Si funciona'
    else:
        return 'error'
    
if __name__== '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    at_provider.close()
    



