# 使用するモジュールのインポート
import btncon
import js

# ボタンのコントローラーを発動
btn = btncon.ButtonController()


# ボタン発動時
async def btn_click(event) -> None:
    ### 5秒待つ ###
    await btn.sleep(5)  # ○秒待つ

    ### ボタンを成功マークにする ###
    js.btn_success()