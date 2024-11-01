import datetime
import json
import os.path
import sys

from mitmproxy import http


def response(flow: http.HTTPFlow) -> None:
    # 检查是否是我们要替换的 JavaScript

    #http://innopac.lib.xjtu.edu.cn/scripts/common.js
    if "innopac.lib.xjtu.edu.cn/scripts/common.js" in flow.request.pretty_url :
        # and flow.request.pretty_url.endswith(".js"):
        # 读取本地的 JavaScript 文件内容
        with open("changed_script.js", "r",encoding="gbk") as f:
            custom_js = f.read()

        print("script replaced")
        print("---------------------------------------------------------------------------------------------------------")
        # 用自定义的 JavaScript 内容替换响应内容
        flow.response.text = custom_js
        # 设置适当的响应头
        flow.response.headers["content-type"] = "application/javascript"



    with open(f"D:/Project/repackage/flow/{datetime.datetime.now().strftime("%y%m%d-%H%M%S-%f")}-{flow.id}.json", "a"
            ) as f:
        request = {
            "url": flow.request.pretty_url,
            "method": flow.request.method,
            "headers": dict(flow.request.headers),
            "cookie": flow.request.cookies
            # "body": flow.request.text
        }
        response = {
            "status_code": flow.response.status_code,
            "headers": dict(flow.response.headers),
            # "body": flow.response.text
        }
        json.dump({"request": request, "response": response}, f, ensure_ascii=False,indent=1)


# run "mitmproxy --listen-port 7890 --ssl-insecure -s main.py"