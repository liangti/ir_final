import urllib2
import json

data_list=list(range(530000,530100))
# data=data+list(range(20160201,20160229))
# data=data+list(range(20160301,20160331))
# data=data+list(range(20160401,20160430))
# data=data+list(range(20160501,20160531))
# data=data+list(range(20160601,20160630))
# data=data+list(range(20160701,20160731))
# data=data+list(range(20160801,20160831))
# data=data+list(range(20160901,20160930))
# data=data+list(range(20161001,20161031))
# data=data+list(range(20161101,20161130))
# data=data+list(range(20171201,20161231))
# data=data+list(range(20170101,20170131))
# data=data+list(range(20170201,20170228))
# data=data+list(range(20170301,20170331))
# obj = open('data.txt', 'wb')
# out={}
# for i in data:
# key='p2ELF989mf4Se9T2V53SOcaUBTnM7y28'
# for data in data_list:
#     f = urllib2.urlopen('http://api2.bigoven.com/recipe/'+data+'?api_key='+key)
#     json_string = f.read()
#     parse=json.loads(json_string)
#
#     f.close()
#     json_d=json.dumps(parse)
# obj = open('data.txt', 'ab')
# obj.write(json_d)
# obj.close

import urllib2
import json
import traceback
data=list(range(100000,101000))
# data=data+list(range(20160201,20160229))
# data=data+list(range(20160301,20160331))
# data=data+list(range(20160401,20160430))
# data=data+list(range(20160501,20160531))
# data=data+list(range(20160601,20160630))
# data=data+list(range(20160701,20160731))
# data=data+list(range(20160801,20160831))
# data=data+list(range(20160901,20160930))
# data=data+list(range(20161001,20161031))
# data=data+list(range(20161101,20161130))
# data=data+list(range(20171201,20161231))
# data=data+list(range(20170101,20170131))
# data=data+list(range(20170201,20170228))
# data=data+list(range(20170301,20170331))
obj = open('data.txt', 'wb')
out={}
key='p2ELF989mf4Se9T2V53SOcaUBTnM7y28'
for i in data:

    try:
        f = urllib2.urlopen('http://api2.bigoven.com/recipe/'+str(i)+'?api_key='+key)

        json_string = f.read()
        parse=json.loads(json_string)
        out[str(i)]=parse
        f.close()
        print i
    except:
        pass
        # traceback.print_exc()

json_d=json.dumps(out)
obj = open('data_100000_101000.txt', 'wb')
obj.write(json_d)
obj.close
