import requests
from fake_useragent import UserAgent
import json
import pandas as pd
import time
import datetime
import openpyxl
UserAgent = UserAgent().random
headers = {
    'User-Agent':UserAgent,
    'Cookie': 'ttwid=1%7CnJUNFSwm_BkYJmamhjRVnemAxU6mvDwI_CxkOqhD9rk%7C1706507736%7Ca10162781502eb32f86a63e295217a206fad7839e52ac1b11391ff1639cedaa5; passport_csrf_token=c404aadc4d5cde535e3c2487cc716e9f; passport_csrf_token_default=c404aadc4d5cde535e3c2487cc716e9f; bd_ticket_guard_client_web_domain=2; odin_tt=dc8e86a6607f9533ae88907d44651860eae085075288ce644a06334477560e3d0db267a60d2eae0e2139c8e2cd8e343c7dbee3adbc52850be329b886bc5cec0c839a5c87c658a4354bfc6669092b72bf; xgplayer_user_id=206085882355; __ac_signature=_02B4Z6wo00f01W0fyQwAAIDCULbTk.epFz1tP82AAD6Lotpsa2IuuQNQ9ncBFXE3F-5UFt.xrfMZx2mRSq5VetMcXwOw9US3r1WkO5gos9PhWlvmDt1lK5wcmwm2gAXxohOkhBX5bLoaYAuk6d; douyin.com; xg_device_score=7.805605238974122; device_web_cpu_core=32; device_web_memory_size=8; architecture=amd64; dy_swidth=1707; dy_sheight=1067; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%7D; csrf_session_id=f755f562614a85be49abecedd937dec6; strategyABtestKey=%221708239276.741%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.5%7D; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A1%7D%22; pwa2=%220%7C0%7C1%7C0%22; IsDouyinActive=true; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1707%2C%5C%22screen_height%5C%22%3A1067%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A32%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A250%7D%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQnB2ZVc4R1c2c3NLUjNoekk5b0hlVllwSFB2akNJU05VM3h0YXQ1bnhnNFArTzRKQkdVTUpuc2dmTmJERHNVbDkxMFVtSkhzaDZNTFZTQzRDbWthbFE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; msToken=sr7L1evW5taYTwHnOk9MadJx3zCR83BHkJxrxscQYvuAAbb0T5jF4Rh-HPV9mZ5hCvujap1D4m1rWcvXvBvbD4kHAuDVp45qrviEBVJp1fC6fKk_q8QRzqRw_LtT; home_can_add_dy_2_desktop=%221%22; msToken=xbT-knmOtL2HBfyB9Y_km6Bvpq64TcjRwy59p-KnrW7K7Ssx7TmazwqBw0R0kd1ARSJ_VewvjqVHKKCrTH1YZpTkbPNGqwJkwupi0k9BQSIYXLyGRFskPwaUaTYUgw==; tt_scid=hC-pj.3dtY9eL11uCremil0Y9JGXu1K6kqS0HUiEdHxeteKCe3v1lAT8N.1Divpfff3f; download_guide=%221%2F20240218%2F0%22',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.douyin.com',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Referer': 'https://www.douyin.com/hot',
    'Connection': 'keep-alive'
}
url = 'https://www.douyin.com/aweme/v1/web/hot/search/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&detail_list=1&source=6&board_type=0&board_sub_type=&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1707&screen_height=1067&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=122.0.0.0&browser_online=true&engine_name=Blink&engine_version=122.0.0.0&os_name=Windows&os_version=10&cpu_core_num=32&device_memory=8&platform=PC&downlink=10&effective_type=4g&round_trip_time=250&webid=7329394854488032822&msToken=xbT-knmOtL2HBfyB9Y_km6Bvpq64TcjRwy59p-KnrW7K7Ssx7TmazwqBw0R0kd1ARSJ_VewvjqVHKKCrTH1YZpTkbPNGqwJkwupi0k9BQSIYXLyGRFskPwaUaTYUgw==&X-Bogus=DFSzswVuRa2ANCPStoXmMvB9Piz2'
res = requests.get(url,headers=headers)
position_list = []
title_list = []
hot_url = []
time_list = []
hot_value_list = []
json_data = res.json()
data_list = json_data['data']['word_list']
for data in data_list:
    position = data.get('position',0)
    if position == 0:
        continue
    position_list.append(position)
    title = data.get('word', '')
    title_list.append(title)
    hot_value = data.get('hot_value', '')
    hot_value_list.append(hot_value)
    event_time = data.get('event_time', '')
    if event_time:
        timestamp = float(event_time)
        dt_object = datetime.datetime.fromtimestamp(timestamp)
        formatted_date = dt_object.strftime("%Y-%m-%d %H:%M:%S")
        time_list.append(formatted_date)
    else:
        time_list.append('')
    hot_url.append('https://www.douyin.com/hot/' + data.get('sentence_id', ''))
df = pd.DataFrame(
    {
        '热搜排名': position_list,
        '热搜标题': title_list,
        '热搜时间': time_list,
        '热度值': hot_value_list,
        '热搜链接': hot_url,
    }
)
df.to_excel('抖音热搜.xlsx', index=False)
url1 = 'https://v3-web.douyinvod.com/4c32bf677427682dc2064f6a1e281863/65d1dea0/video/tos/cn/tos-cn-ve-15/oAu5Bf2VAixCEvP1wQygiBzIIAeBA8WVjAUuDA/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1104&bt=1104&cs=2&ds=6&ft=bvTKJbQQqUiAfo0ZPo0ORVTYA0pi9jExejKJAtNR1G0P3-I&mime_type=video_mp4&qs=11&rc=ZWg1ZmQzNDY1ZThpPDs6OkBpam9nZnA5cmQ2cTMzNGkzM0BjNWE0YS0xXjYxLWJjMGAuYSNeYWxsMmRzYjFgLS1kLS9zcw%3D%3D&btag=e00030000&dy_q=1708248884&feature_id=c6de0308cacfd993ef282c8e1c646267&l=20240218173443A2DEF54EC26530377321'
res1 = requests.get(url1).content
with open('游戏区.mp4',mode='wb') as f:
    f.write(res1)
url2 = 'https://v3-web.douyinvod.com/ab8091d6f3f9e5786c470977cdbd6d36/65d1df39/video/tos/cn/tos-cn-ve-15/owuQJe7lAnHbhCIc3ge7gyID9AKpgHQbAMBlcg/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=790&bt=790&cs=2&ds=3&ft=bvTKJbQQqUiAfo0ZPo0ORVTYA0piExixejKJAtNR1G0P3-I&mime_type=video_mp4&qs=15&rc=NDQ3ODkzMzg8Zjk7NDlkZUBpM3c1bjg6ZjczbzMzNGkzM0AtYGFeX18xXzIxMy9iMGMyYSNsNWpfcjQwbWtgLS1kLS9zcw%3D%3D&btag=e00028000&dy_q=1708249321&feature_id=e585bce62f14c124a0ac1450c3a95af2&l=20240218174200F8069617D0FBC2FBEFBC'
res2 = requests.get(url2).content
with open('二次元.mp4',mode='wb') as f:
    f.write(res2)
url3 = 'https://v3-web.douyinvod.com/1d9cdce1f851dec520ea8fb9679f9cec/65d1e084/video/tos/cn/tos-cn-ve-15/oUGANHzpfjNTxPJqxeC7ABAAdJiIENQNgyJ6Kh/?a=6383&ch=5&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1099&bt=1099&cs=2&ds=3&ft=bvTKJbQQqUiAfo0ZPo0ORVTYA0piN7ixejKJAtNR1G0P3-I&mime_type=video_mp4&qs=15&rc=PDs6NWU0Zjk0OmY1ZjRpZ0Bpamc7eDw6ZjxscDMzNGkzM0AtMi9jXjAvXmIxMy4uYWI2YSNxLWhicjRnYTFgLS1kLWFzcw%3D%3D&btag=e00030000&dy_q=1708249450&feature_id=768c4eee0a62d19cc9ffc7d17c46e537&l=202402181744097BF45443480BF0113032'
res3 = requests.get(url3).content
with open('音乐区.mp4',mode='wb') as f:
    f.write(res3)