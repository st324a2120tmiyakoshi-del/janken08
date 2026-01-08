import streamlit as st
import random
from PIL import Image

# アプリの基本設定（タイトル / アイコン / レイアウト）
st.set_page_config(page_title="じゃんけん（スーパーサイヤ人風）", page_icon="🐉", layout="centered")

# ===== 戦績の初期化（Streamlitのsession_stateを使用）=====
if "wins" not in st.session_state:
    st.session_state.wins = 0     # 勝ち数
    st.session_state.losses = 0   # 負け数
    st.session_state.draws = 0    # あいこ数

st.title("🐉 じゃんけん（スーパーサイヤ人風エネルギー波）")
st.write("勝ったら **スーパーサイヤ人風エネルギー波エフェクト** が発動する！⚡🔥")

# ===== じゃんけんの選択肢 =====
hands = ["グー", "チョキ", "パー"]

# ボタンを3列で表示
col1, col2, col3 = st.columns(3)
player = None  # プレイヤーの手を一時的に保持

with col1:
    if st.button("✊ グー"):
        player = "グー"
with col2:
    if st.button("✌ チョキ"):
        player = "チョキ"
with col3:
    if st.button("🖐 パー"):
        player = "パー"

# ===== 結果処理 =====
if player:
    cpu = random.choice(hands)  # CPUの手をランダム決定

    st.subheader("【勝負結果】")
    st.write(f"あなた：**{player}**")
    st.write(f"コンピュータ：**{cpu}**")

    # ===== あいこ =====
    if player == cpu:
        st.session_state.draws += 1
        st.info("😐 あいこ！ 風がふわっと流れる… 🌪")
        result = "😐 あいこ！"

    # ===== プレイヤーが勝ち =====
    elif (player == "グー" and cpu == "チョキ") or \
         (player == "チョキ" and cpu == "パー") or \
         (player == "パー" and cpu == "グー"):

        st.session_state.wins += 1
        st.success("⚡💥 **エネルギー波ーーーーっ！！！** 💥⚡")
        result = "🔥 勝ち！エネルギー波発射！！"

        # 画像（エネルギー波）を表示する部分
        # 読み込みエラーにも対応
        try:
            img = Image.open("images/super_kame.png")
            st.image(img, use_container_width=True)
        except Exception as e:
            st.error("画像が読み込めませんでした。'images/super_kame.png' を確認してください。")
            st.code(str(e))

    # ===== プレイヤーが負け =====
    else:
        st.session_state.losses += 1
        st.error("💥 負け… 衝撃が走る！ 🟥")
        result = "💥 負け…衝撃が走る！"

    st.subheader(result)

# ===== 戦績表示 =====
st.markdown("## 📊 戦績")
c1, c2, c3 = st.columns(3)

c1.metric("勝ち", st.session_state.wins)
c2.metric("負け", st.session_state.losses)
c3.metric("あいこ", st.session_state.draws)

# ===== リセットボタン =====
if st.button("戦績をリセット"):
    st.session_state.wins = 0
    st.session_state.losses = 0
    st.session_state.draws = 0
    st.toast("戦績をリセットしました！")
