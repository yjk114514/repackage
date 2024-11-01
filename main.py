import multiprocessing

import os
import sys


# mitmdump -s main.py --listen-port 7890 --ssl-insecure
if __name__ == '__main__':
    # 与clash配置文件中的端口保持一致
    os.system("mitmdump --listen-port 7890 -s replace_js.py")