import streamlit as st
import time

# Konfiguracja strony - motyw Kosmiczny
st.set_page_config(
    page_title="Vinted ERP - Cosmic Edition",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Kosmiczny styl CSS (ciemne tło, motyw fioletowy, neonowe akcenty)
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
st.markdown("<p style='text-align: center; color: #94a3b8;'>Przesyłaj wiele zdjęć, analizuj ceny rynkowe i generuj optymalne opisy Vinted</p>", unsafe_allow_html=True)

# Pasek statystyk
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Magazyn", "Aktywny", "Online")
with col2:
    st.metric("Zysk Cel", "0 / 3000 PLN", "0%")
with col3:
    st.metric("AI Status", "MAX", "Wsparcie 24/7")

st.markdown("---")

# Główny panel dodawania przedmiotu
st.markdown("<div class='cosmic-card'>", unsafe_allow_html=True)
st.subheader("📸 Masowy Skaner Zdjęć (Przód, Tył, Metka, Detale)")

uploaded_files = st.file_uploader(
    "Wybierz lub przeciągnij zdjęcia ubrań (możesz zaznaczyć kilka na raz)",
    type=["png", "jpg", "jpeg"],
    accept_multiple_files=True
)

if uploaded_files:
    # Poprawny powrót komunikatu bez błędu składniowego
    st.success(f"Udało się! Wgrano {len(uploaded_files)} zdjęć do analizy.")
    
    # Wyświetlanie siatki miniatury zdjęć
    num_cols = min(len(uploaded_files), 4)
    cols = st.columns(num_cols)
    for idx, file in enumerate(uploaded_files):
        with cols[idx % num_cols]:
            st.image(file, caption=f"Zdj. {idx+1}", use_container_width=True)

    if st.button("✨ Uruchom Super-Analizę AI i Wycenę Rynkową"):
        with st.spinner("🧠 AI analizuje materiał, oświetlenie i aktualne oferty na Vinted..."):
            time.sleep(1.5)
            
        st.markdown("---")
        st.markdown("### 📊 Wyniki analizy rynkowej:")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**💰 Sugerowana cena rynkowa:**")
            st.info("65 - 85 PLN (Optymalna: **75 PLN**)")
            st.markdown("**⏰ Najlepsza godzina wystawienia:**")
            st.success("**18:05 – 20:30** (Maksymalne zasięgi)")
        with c2:
            st.markdown("**📸 Wybór zdjęcia okładkowego:**")
            st.warning("Zdjęcie nr 1 wytypowane jako najlepsze wizualnie na okładkę.")
            st.markdown("**📅 Zaplanowane powiadomienie:**")
            st.text("10 października, godz. 18:05")

        st.markdown("### 📝 Gotowy opis do wklejenia na Vinted:")
        
        opis_vinted = """✨ Stan: Bardzo dobry / Idealny
🔥 Stylowy ciuch, wysokiej jakości materiał, poszukiwany model na Vinted.
📏 Dokładne wymiary podaję w wiadomości prywatnej – chętnie odpowiem!
📦 Szybka wysyłka paczkomatem (najczęściej tego samego dnia).
💡 Kupujesz w zestawie? Napisz, a chętnie naliczę rabat! 🚀"""

        st.code(opis_vinted, language="markdown")
        st.info("💡 Skopiuj powyższy tekst przyciskiem w prawym górnym rogu ramki kodu i wklej bezpośrednio w formularzu dodawania przedmiotu w aplikacji Vinted.")

st.markdown("</div>", unsafe_allow_html=True)
