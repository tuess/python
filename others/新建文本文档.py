import requests

url = "https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg"

querystring = {"g_tk":"1719369966","loginUin":"1571754870","hostUin":"0","format":"json","inCharset":"utf8","outCharset":"GB2312","notice":"0","platform":"yqq.json","needNewCode":"0","cid":"205360772","reqtype":"2","biztype":"1","topid":"237773700","cmd":"8","needmusiccrit":"0","pagenum":"1","pagesize":"25","lasthotcommentid":"song_237773700_1344862860_1568894502","domain":"qq.com","ct":"24","cv":"10101010"}

headers = {
    'authority': "c.y.qq.com",
    'accept': "application/json, text/javascript, */*; q=0.01",
    'dnt': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.0 Safari/537.36 Edg/78.0.276.2",
    'origin': "https://y.qq.com",
    'sec-fetch-site': "same-site",
    'sec-fetch-mode': "cors",
    'referer': "https://y.qq.com/n/yqq/song/001qvvgF38HVc4.html",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    'cookie': "pgv_pvi=6058244096; RK=S2rh0mJoZ9; ptcz=733e8ed94b2c784015011f963fcfdfe1089a533b5f481a8c9395f999d56edd97; eas_sid=T1U5Z559f6N5d0O394a0v3j466; pgv_pvid=8303000354; uin_cookie=o1571754870; ied_qq=o1571754870; LW_uid=9175w5M929Z1V0u2R4W4O5d4C9; tvfe_boss_uuid=46e3f30dec60f483; o_cookie=1571754870; ue_ts=1562761048; ue_uk=4236729c96a7334f4ed555ad24e001cb; ue_uid=ca0d64b6a711183c6a2178d08a9baeb7; ue_skey=f423db912bbe16f4d85038d139504e17; LW_pid=86b1a141565be2e667e887284a0cb3d7; LW_sid=d1v536S3p5C0W4V6M8a4S1W4p7; ptui_loginuin=2601604258; ptisp=ctc; pgv_si=s4564977664; uin=o1571754870; skey=@iAYF7lHBS; yqq_stat=0; pgv_info=ssid=s6384644864; ts_refer=cn.bing.com/; ts_uid=101805516; ts_last=y.qq.com/n/yqq/song/001qvvgF38HVc4.html; userAction=1",
    'Cache-Control': "no-cache",
    'Postman-Token': "97ca5ff0-93c6-43cf-b90e-1abcded56a59,994db190-d2e8-4dc9-8daa-d64efeb11ed0",
    'Host': "c.y.qq.com",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
