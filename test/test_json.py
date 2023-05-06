import json

json_dic = {
    'index': {
        'page': 'a',
        'position': 'a',
        'title': 'a',
        'preview': 'a'
    }
}
print('before dumps',type(json_dic))
data_str = json.dumps(json_dic,indent=2)
print('after dumps',type(data_str))