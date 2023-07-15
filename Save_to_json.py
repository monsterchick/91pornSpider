import json
import os.path

index = -1

def save_to_json(page, position, title,preview):
    global index
    index += 1
    # print(page,position)
    # page = str(page)
    # position = str(position)
    ti = title
    print(ti)
    json_dic = {
        index: {
            "page": page,
            "position": position,
            "title": title,
            "preview": preview
        }
    }
    path = os.path.join(os.path.abspath(r'save/data.json'))
    # print(path)
    # json_str = json.dumps(json_dic,ensure_ascii=False)
    # print(json_str)
    with open(path,'a') as f:
        json.dump(json_dic,f,ensure_ascii=False)
        # print(a)
        # with open()
    print('写入完成！')
