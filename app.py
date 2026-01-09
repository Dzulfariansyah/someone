import streamlit as st
import base64
import streamlit.components.v1 as components

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Wanda Maharani 🖤💖",
    page_icon="🖤",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- FUNGSI LOAD GAMBAR & AUDIO ---
def get_file_base64(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return None

imgs = []
for i in range(1, 7):
    img_code = get_file_base64(f"{i}.jpg")
    if img_code:
        imgs.append(f"data:image/jpeg;base64,{img_code}")
    else:
        imgs.append("https://source.unsplash.com/random/400x600?neon")

audio_b64 = get_file_base64("lagu.mp3")

# --- CSS TEMA BLACKPINK (RESPONSIVE) ---
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
        background-image: radial-gradient(circle at 50% 50%, #1a1a1a 0%, #000000 100%);
        color: #ff69b4;
    }

    /* Judul Utama */
    .main-title {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 900;
        font-size: 6rem; /* Ukuran Laptop */
        text-align: center;
        text-transform: uppercase;
        letter-spacing: 5px;
        margin-top: 20px;
        margin-bottom: 50px;
        color: #ff69b4; 
        -webkit-text-stroke: 2px #fff; 
        text-shadow: 0 0 20px #ff1493, 0 0 40px #ff1493;
    }

    /* Frame Foto */
    .photo-frame {
        border: 4px solid #ff69b4;
        padding: 5px;
        background: #111;
        box-shadow: 0 0 15px rgba(255, 105, 180, 0.5);
        transition: transform 0.5s ease;
        margin-bottom: 20px; /* Jarak antar elemen di HP */
    }

    .photo-frame:hover {
        transform: scale(1.05) rotateY(15deg) rotateX(5deg);
        box-shadow: 0 0 50px rgba(255, 20, 147, 0.8);
        border-color: white;
        z-index: 10;
    }

    /* Kotak Teks */
    .text-box {
        background: rgba(255, 255, 255, 0.1); 
        color: #eee; 
        padding: 25px;
        border-left: 6px solid #ff69b4;
        border-radius: 0 20px 20px 0;
        font-size: 1.3rem; /* Ukuran Laptop */
        line-height: 1.6;
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }
    
    .highlight { color: #ff69b4; font-weight: bold; font-size: 1.5rem; }

    /* --- KHUSUS TAMPILAN HP (RESPONSIVE) --- */
    @media only screen and (max-width: 600px) {
        .main-title {
            font-size: 3rem !important; /* Judul mengecil di HP */
            letter-spacing: 2px;
        }
        .text-box {
            font-size: 1rem !important; /* Teks mengecil dikit biar muat */
            padding: 15px;
            border-radius: 10px; /* Sudut lebih kecil */
            border-left: 4px solid #ff69b4;
        }
        .highlight {
            font-size: 1.2rem !important;
        }
    }

    .stButton>button {
        color: white; background: transparent; border: 2px solid #ff69b4;
        border-radius: 50px; padding: 10px 30px; font-size: 1.2rem;
        transition: 0.3s; display: block; margin: 0 auto;
    }
    .stButton>button:hover { background: #ff69b4; box-shadow: 0 0 20px #ff69b4; }

    #MainMenu, header, footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.markdown('<h1 class="main-title">ABOUT YOU</h1>', unsafe_allow_html=True)
st.write("---")

# --- KONTEN ---

# 1. SECTION KIRI
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown(f'<div class="photo-frame"><img src="{imgs[0]}" style="width:100%;"></div>', unsafe_allow_html=True)
with col2:
    st.write("")
    st.markdown("""
    <div class="text-box">
        <span class="highlight">Hai Kamu,</span><br>
        Website ini dibuat untuk menunjukkan betapa bangganya aku memilikimu dan gabungan warna favorit kita masing - masing black and pink,
        yang melambangkan pertemuan kita.
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# 2. SECTION KANAN
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.write("")
    st.markdown("""
    <div class="text-box" style="border-left:none; border-right: 6px solid #ff69b4; border-radius: 20px 0 0 20px; text-align: right;">
        <span class="highlight">Senyummu,</span><br>
        Merupakan hal yang sangat kusukai, bisa membuatku melayang dan menjadi semangatku dalam menjalani kehidupan, SUKAAAA BANGET SAMAAA SENYUMAN KAMU SAYANGG!!!!
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="photo-frame"><img src="{imgs[1]}" style="width:100%;"></div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ============================================================
# 3. SECTION MUSIK (CUSTOM PINK PLAYER - RESPONSIVE)
# ============================================================
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown(f'<div class="photo-frame"><img src="{imgs[2]}" style="width:100%;"></div>', unsafe_allow_html=True)

with col2:
    st.write("")
    
    # Player ini sudah diset CSS-nya agar aman di HP (Overflow hidden)
    custom_player_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        body {{ background: transparent; margin: 0; font-family: 'Poppins', sans-serif; overflow: hidden; }}
        
        .player-card {{
            background: rgba(20, 20, 20, 0.8);
            border: 2px solid #ff69b4;
            border-radius: 20px;
            padding: 15px; /* Padding lebih aman utk HP */
            color: white;
            display: flex;
            align-items: center;
            gap: 10px;
            box-shadow: 0 0 15px rgba(255, 105, 180, 0.2);
            backdrop-filter: blur(5px);
        }}
        
        .play-btn {{
            width: 45px; height: 45px; /* Sedikit lebih kecil */
            background: #ff69b4;
            border-radius: 50%;
            border: none;
            cursor: pointer;
            display: flex; justify-content: center; align-items: center;
            box-shadow: 0 0 10px #ff69b4;
            flex-shrink: 0; /* Biar tombol gak gepeng di HP */
        }}
        
        .play-icon {{
            width: 0; height: 0;
            border-top: 7px solid transparent; border-bottom: 7px solid transparent;
            border-left: 12px solid white;
            margin-left: 3px;
        }}
        
        .pause-icon {{
            width: 10px; height: 12px;
            border-left: 3px solid white; border-right: 3px solid white;
        }}
        
        .track-info {{ flex-grow: 1; min-width: 0; /* Mencegah teks nabrak */ }}
        .title {{ font-size: 14px; font-weight: 600; color: #ff69b4; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
        .subtitle {{ font-size: 10px; color: #ccc; }}
        
        input[type="range"] {{
            width: 100%; -webkit-appearance: none; height: 4px; background: #444;
            border-radius: 5px; outline: none; margin-top: 5px;
        }}
        input[type="range"]::-webkit-slider-thumb {{
            -webkit-appearance: none; width: 10px; height: 10px;
            background: #ff69b4; border-radius: 50%; cursor: pointer;
            box-shadow: 0 0 10px #ff69b4;
        }}
        
        /* Equalizer disembunyikan di HP layar sangat kecil biar gak penuh */
        .equalizer {{ display: flex; gap: 3px; height: 20px; align-items: flex-end; }}
        @media (max-width: 350px) {{ .equalizer {{ display: none; }} }}
        
        .bar {{ width: 3px; background: #ff69b4; animation: bounce 1s infinite ease-in-out; }}
        .bar:nth-child(2) {{ animation-delay: 0.1s; height: 15px; }}
        .bar:nth-child(3) {{ animation-delay: 0.2s; height: 20px; }}
        .bar:nth-child(4) {{ animation-delay: 0.3s; height: 10px; }}
        @keyframes bounce {{ 0%, 100% {{ height: 5px; }} 50% {{ height: 100%; }} }}
    </style>
    </head>
    <body>
        <div class="player-card">
            <button class="play-btn" onclick="togglePlay()" id="pBtn">
                <div class="play-icon" id="pIcon"></div>
            </button>
            <div class="track-info">
                <div class="title">🎶 Sound of You</div>
                <div class="subtitle">Our Special Song</div>
                <input type="range" id="progressBar" value="0" max="100" onchange="seekAudio()">
            </div>
            <div class="equalizer">
                <div class="bar"></div><div class="bar"></div><div class="bar"></div><div class="bar"></div>
            </div>
        </div>

        <audio id="audio" src="data:audio/mp3;base64,{audio_b64}"></audio>

        <script>
            var audio = document.getElementById("audio");
            var pBtn = document.getElementById("pBtn");
            var pIcon = document.getElementById("pIcon");
            var progressBar = document.getElementById("progressBar");
            var isPlaying = false;

            function togglePlay() {{
                if (isPlaying) {{
                    audio.pause();
                    pIcon.className = "play-icon";
                    pIcon.style.borderLeft = "12px solid white";
                    pIcon.style.borderRight = "none";
                    pIcon.style.height = "0";
                    isPlaying = false;
                }} else {{
                    audio.play();
                    pIcon.className = "pause-icon";
                    pIcon.style.borderTop = "none";
                    pIcon.style.borderBottom = "none";
                    pIcon.style.height = "12px";
                    pIcon.style.marginLeft = "0";
                    isPlaying = true;
                }}
            }}
            
            audio.ontimeupdate = function() {{
                var percentage = (audio.currentTime / audio.duration) * 100;
                progressBar.value = percentage;
            }};
            
            function seekAudio() {{
                var time = (progressBar.value / 100) * audio.duration;
                audio.currentTime = time;
            }}
        </script>
    </body>
    </html>
    """
    
    if audio_b64:
        components.html(custom_player_html, height=100)
    else:
        st.error("File lagu.mp3 tidak ditemukan!")
    
    st.markdown("""
    <div style="text-align: left; color: #ccc; font-size: 0.9rem; margin-top: 0px;">
        <i>"Lagu ini selalu ngingetin akuu tentang kamuu..."</i>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
# ============================================================

# 4. SECTION KANAN
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.write("")
    st.markdown("""
    <div class="text-box" style="border-left:none; border-right: 6px solid #ff69b4; border-radius: 20px 0 0 20px; text-align: right;">
        <span class="highlight">Sederhana,</span><br>
        Aku cuma ingin mengucapkan makasih karena kamu telah menjadi warna "Pink" di kehidupan aku yang "Black" ini, sehingga
        aku dapat menjalani kehidupanku dengan berwarna.
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="photo-frame"><img src="{imgs[3]}" style="width:100%;"></div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# 5. SECTION KIRI
col1, col2 = st.columns([1, 1], gap="large")
with col1:
    st.markdown(f'<div class="photo-frame"><img src="{imgs[4]}" style="width:100%;"></div>', unsafe_allow_html=True)
with col2:
    st.write("")
    st.markdown("""
    <div class="text-box">
        <span class="highlight">Harapanku?</span><br>
        Semoga kita bisa terus sama-sama, sukses bersama dan saling mendukung satu sama lain, ngelewatin segala rintangan
        dan tantangan yang ada, btw CONGRATSSS SUDAH DAPAT KERJA SAYANGG, i am very proud of youu ❤️.
    </div>
    """, unsafe_allow_html=True)

# --- PENUTUP ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.write("---")
st.markdown("<h3 style='text-align:center; color:#ff69b4;'>I Love You 🖤</h3>", unsafe_allow_html=True)

col_btn1, col_btn2, col_btn3 = st.columns([1,1,1])
with col_btn2:
    if st.button("KIWWWW LOVE UU SO MUCHHH BABYYY ❤️"):

        st.balloons()

