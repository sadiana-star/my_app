import flet as ft


def main(page: ft.Page):
    # 这一步是告诉手机：我是个APP，不是网页
    page.title = "我的第一个App"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.bgcolor = "white"

    # 一个简单的文本
    txt = ft.Text("终于成功了！", color="green", size=30, weight="bold")

    # 一个简单的按钮
    btn = ft.ElevatedButton("点击领取安装包", on_click=lambda e: print("Clicked"))

    page.add(txt, btn)


# 注意：这里不需要 host="0.0.0.0" 了，因为我们是要打包！
ft.app(target=main)