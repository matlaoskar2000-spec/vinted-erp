import streamlit as st
from datetime import datetime

# Konfiguracja strony - kosmiczny styl
st.set_page_config(
    page_title="Vinted ERP - Cosmic Edition",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Kosmiczny styl CSS (ciemny motyw, neony, zaokrąglenia, przejrzystość)
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311042 100%);
        color: #f8fafc;
    }
    .stButton>button {
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.75rem 1.5rem;
        font-weight: bold;
        width: 100%;
        box-shadow: 0 4px 15px rgba(168, 85, 247, 0.4);
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(236, 72, 153, 0.6);
    }
    div.stMetric {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 15px;
        backdrop-filter: blur(10px);
    }
    .cosmic-card {
        background: rgba(30, 27, 75, 0.6);
        border: 1px solid rgba(168, 85, 247, 0.3);
        padding: 20px;
        border-radius: 20px;
        backdrop-filter: blur(12px);
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    </style>
""", unsafe_allow_html=True)

# Nagłówek aplikacji
st.markdown("<h1 style='text-align: center; background: linear-gradient(90deg, #818cf8, #c084fc, #f472b6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>🚀 Vinted ERP // Cosmic AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8;'>Twój autonomiczny system resellingowy wspierany przez sztuczną inteligencję</p>", unsafe_allow_html=True)

# Pasek statystyk
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Magazyn", "0 szt.", "Aktywne")
with col2:
    st.metric("Zysk Cel", "0 / 3000 PLN", "0%")
with col3:
    st.metric("AI Status", "ONLINE", "Najwyższa moc")

st.markdown("---")

# Główny panel dodawania przedmiotu
st.markdown("<div class='cosmic-card'>", unsafe_allow_html=True)
st.subheader("📸 Kosmiczny Skaner & AI Analyzer")
uploaded_file = st.file_uploader("Wrzuć surowe zdjęcie ciucha (np. z lumpeksu)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Wgrane zdjęcie przedmiotu", use_container_width=True)
    
    with st.spinner("✨ AI analizuje tkaninę, markę, rynkowe trendy i optymalną cenę..."):
        # Symulacja inteligentnej analizy AI
        import time
        time.sleep(1.5)
        
    st.success("Analiza zakończona sukcesem!")
    
    st.markdown("### 📊 Wyniki analizy AI & Vinted Market:")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("**💡 Sugerowana cena:**")
        st.info("65 - 85 PLN (Optymalna: **75 PLN**)")
        st.markdown("**⏰ Najlepsza godzina publikacji:**")
        st.success("**18:05 – 20:30** (Największy ruch w aplikacji)")
    with col_b:
        st.markdown("**📸 Porada dotycząca zdjęcia:**")
        st.warning("Zrób jasne zdjęcie w świetle dziennym na jednolitym tle. Dodaj zbliżenie na metkę ze składem.")
        st.markdown("**📅 Zaplanowane przypomnienie:**")
        st.text("10 października, godz. 18:05")

    st.markdown("### 📝 Gotowy opis wygenerowany przez AI:")
    st.code("""✨ [Stan jak nowy / Idealny] Stylowy ciuch w świetnym stanie!
🔥 Marka premium, bardzo poszukiwana na Vinted.
📏 Wymiary na priv / Zapraszam do zestawów (rabat na wiecej rzeczy!).
📦 Szybka wysyłka tego samego dnia! 🚀""", language="markdown")
    
    if st.button("🚀 Zapisz w systemie i ustaw przypomnienie"):
        st.balloons()
        st.success("Przedmiot dodany do bazy! Powiadomienie ustawione na 10 października o 18:05.")

st.markdown("</div>", unsafe_allow_html=True)
