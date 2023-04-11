from avoid_special_characters import avoid_spc_char
from Visuallize_process_saving import visualize
from General_saving import general_saving
from Save_to_json import save_to_json
from make_path import mkdir, mkjson


working_on = 0
def download_videos(get_m3u8, title, video_id, page,working_on,url):
    ts_list = get_m3u8[0]
    # print('ts列表',ts_list)    # 用于调试
    for index, ts in enumerate(ts_list):
        video_url = get_m3u8[1].rsplit("/", 1)[0] + '/' + ts    # ts link for saving

        # print(f'正在保存第{page}页 第{working_on}个视频 {title}第{index+1}个部分...')    # 用于调试

        # 去除特殊字符
        title = avoid_spc_char(title)
        file_path = f'download\\p{page}v{working_on}_{title}.mp4'

        ### 保存方式：
        # 下载视频片段并保存到本地 + 可视化下载进度
        # visualize(ts,page,working_on,title,index + 1,file_path,video_url)

        # 普通保存
        general_saving(file_path, video_url,page,working_on,title,index)

    # 保存到json
    # save_to_json(page=page, position=working_on, title=title,preview=get_m3u8[2])

    print(f'{title}.mp4 保存成功！\n')