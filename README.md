# cow.py
![cow.py](https://img.shields.io/badge/cow.py-v.0.5a-%23fce38a) [![Cow Website](https://img.shields.io/website?down_color=lightgrey&down_message=downtime&label=Website&up_color=%230995ec&up_message=uptime&url=https%3A%2F%2Fcow.c-moo.cf)](https://cow.c-moo.cf?test=true)</br>
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/LittleCow-moo/cow.py?label=Commits&style=for-the-badge) [![牛牛的草原](https://img.shields.io/discord/858984157929144321?color=%235865F2&label=Discord&logo=https%3A%2F%2Flogos-world.net%2Fwp-content%2Fuploads%2F2020%2F12%2FDiscord-Logo.png&style=for-the-badge)](https://discord.gg/bQJyuAD9hw)

牛牛跑到 Python 去了！ 快帶牠回家！

## CowLang
CowLang 是一個十分簡單的程式語言，目前版本為 **v.1.0a**。

> **系統需求： [`Python 3`](https://python.org/)**</br>
**大小： `undefined`**
### 如何使用
1. 首先，請先下載執行檔，並新增一個檔案叫做 "CONFIG.clcon"，並**輸入 `run=main.cl`**
> **下載檔案**</br>[原始 | CowLang.py](https://github.com/LittleCow-moo/cow.py/blob/main/cowlang/LAUNCH.py)
```js
// CONFIG.clcon
run=main.cl
```
▲ 新增 CONFIG.clcon 的檔案

2. 接著，我們再新增一個檔案，叫做 "main.cl"，並輸入像這樣的內容：

```js
// main.cl
log Hello World
// !1
[import] cow
[import] process
process.time
// !2
cow.exit
// !3
```
▲ (備註)
> `!1` - 在控制台上顯示 "Hello World" 的文字
> 
> `!2` - 顯示現在的時間 (秒)
> 
> `!3` - 結束程式


3. 最後，直接用 Python 執行 "LAUNCH.py" 即可。

***

[![牛牛](https://cdn.discordapp.com/avatars/836204711454834688/ec51f3aed0943f79239a05124e863dd5.webp?size=512)](https://cow.c-moo.cf?test=true)
> 牛牛： 哞! 好簡單!

## CowDisguise.py
CowDisguise 需要 Discord Webhook 才能運作。
### 如何新增 Webhook 及如何使用
1. 選擇頻道設定

![頻道設定](https://cdn.discordapp.com/attachments/859642024071135282/952550377289560084/unknown.png)
***

2. 選擇整合

![整合](https://cdn.discordapp.com/attachments/859642024071135282/952550593283641394/unknown.png)
***

3. 選擇 Webhook

![Webhook](https://cdn.discordapp.com/attachments/859642024071135282/952552550966640690/unknown.png)
***
4. 按下**新Webhook**

![新 Webhook 按鈕](https://cdn.discordapp.com/attachments/859642024071135282/952552697788256266/unknown.png)
***
5. 複製你的 Webhook 網址

![複製網址](https://user-images.githubusercontent.com/90096971/158060711-51ef61d1-bfa3-4f51-b635-8318f3747ccb.png)
)
***
6. 接著下載我們準備的檔案。
> **下載檔案**</br>[原始 | CowDisguise.py](https://github.com/LittleCow-moo/cow.py/blob/main/disguise/disguise.py)</br>[範本 | Process.json](https://github.com/LittleCow-moo/cow.py/blob/main/disguise/process.json)

然後，將 "process.json" 檔案的值，改成你想要的樣子。

例如：
```json
{
    "username": "牛牛",
    "avatar_url": "https://cdn.discordapp.com/avatars/836204711454834688/ec51f3aed0943f79239a05124e863dd5.webp?size=4096",
    "content": "哞~ 這裡有草吃嗎?",
    "url": "我的 Webhook 連結"
}
```
然後執行 `disguise.py` 即可。

**真的就這麼簡單!**


***
![cowmain](https://user-images.githubusercontent.com/90096971/158060088-fec47b8a-74d9-4684-ad32-ef36a1c53868.gif)
