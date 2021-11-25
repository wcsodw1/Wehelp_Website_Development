
# Python MyWebsite.py

from flask import Flask
from flask import request
from flask import render_template
from flask import session

# 建立 Application 物件, 設定靜態檔案的路徑處理
Session = Flask(__name__, static_folder="public",
                static_url_path="/")  # 靜態檔案路徑 -> Public中

# 密秘鑰匙 :
Session.secret_key = "Any string but secret"  # 設定 Session 的秘鑰

# 20210914 加入網站學習相關資訊 :

# 網站的首頁(非本章重點)


@Session.route("/")
def mainlyused():
    return render_template("center.html")


@Session.route("/Wehelp")
def WeHelp():
    return render_template("WeHelp.html")


# Class11.使用GET方法處理路徑 /hello?name=使用者的名字
@Session.route("/hello")
def hello():
    name = request.args.get("name", "")
    session["username"] = name  # 把資料(ex:name)存放到["變數名稱"]中
    return "Hello, " + name


# Class11.使用GET方法處理路徑 / talk

@Session.route("/talk")
def talk():
    name = session["username"]
    return name + ", so so nice to see u !"


''' 2.表單相關 '''
# class9 表單-測試表單路由

# 啟動伺服器 Port-3000
Session.run(port=1100)
