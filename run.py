import uvicorn
import os,sys
import getopt
import uvicorn
import pathlib
from multiprocessing import freeze_support
# 获取当前脚本所在的目录
current_dir = os.path.dirname(os.path.realpath(__file__))
# 将项目根目录添加到 Python 路径中
sys.path.append(current_dir)




if __name__ == "__main__":
    freeze_support()
    uvicorn.run("app:app", host="localhost", port=9999, reload=True, log_config="uvicorn_loggin_config.json")
