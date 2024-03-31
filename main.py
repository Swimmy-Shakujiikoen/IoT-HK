"""スマホのボタン側のプログラム

© 2024 Swimmy石神井公園校
"""

import js

import btncon

# ボタンのコントローラーを発動
btn = btncon.ButtonController()

# 準備OKでないなら、ボタンを失敗マークにする
if not btn.is_ready():
    js.btn_failure()


# ボタン発動時
async def btn_click(event) -> None:
    ### IoTに信号を送る ###
    await btn.send_trigger()

    # 信号の送信に失敗した場合はボタンを失敗マークにする
    js.btn_failure()
    
    if not btn.is_send_ok():
        ### 信号の送信に成功した確認する ###:
    
        ### ボタンを失敗マークにする ###
        js.btn_failure()
        return

    # IoT側が動作完了するまで10秒ごとに確認する
    while not await btn.is_done():  # 信号受け取り
        ### 10秒待つ ###
        await btn.sleep(10)
    ### ボタンを成功マークにする ###
    js.btn_success()