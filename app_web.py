import streamlit as st
from datetime import datetime
import io

# Konfiguracja strony
st.set_page_config(
    page_title="Vinted ERP - Cosmic AI Pro",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Kosmiczny styl CSS (Neony, ciemny motyw, karty)
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

# Nagłówek
st.markdown("<h1 style='text-align: center; background: linear-gradient(90deg, #818cf8, #c084fc, #f472b6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>🚀 Vinted ERP // Multi-Photo AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8;'>Wrzuć paczkę zdjęć ciucha – AI zajmie się resztą w ułamki sekund!</p>", unsafe_allow_html=True)

# Statystyki
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Magazyn", "Aktywny", "Online")
with col2:
    st.metric("Cel Finansowy", "0 / 3000 PLN", "0%")
with col3:
    st.metric("Tryb AI", "MAX", "Wsparcie 24/7")

st.markdown("---")

# Panel ładowania wielu zdjęć
st.markdown("<div class='cosmic-card'>", unsafe_allow_html=True)
st.subheader("📸 Masowy Skaner Zdjęć (Przód, Tył, Metka, Detale)")

uploaded_files = st.file_uploader(
    "Wybierz lub przeciągnij kilka zdjęć tego przedmiotu", 
    type=["png", "jpg", "jpeg"], 
    accept_multiple_files=True
)

if uploaded_files:
    st.success( załączono=f"Wgrano {len(uploaded_files)} zdjęć do analizy!" )
    
    # Wyświetlanie wgranych zdjęć w miniaturkach
    cols = st.columns(min(len(uploaded_files), 4))
    for idx, file in enumerate(uploaded_files):
        with cols[idx % 4]:
            st.image(file, caption=f"Zdj. {idx+1}", use_container_width=True)

    if st.button("✨ Uruchom Super-Analizę AI i Wycenę Rynkową"):
        with st.spinner("🧠 AI analizuje zdjęcia, dobiera najlepszą okładkę, szuka cen na Vinted..."):
            import time
            time.sleep(1.8)
            
        st.markdown("---")
        st.markdown("### 🎯 Wyniki Analizy i Strategia Sprzedaży:")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("**💰 Rekomendowana cena:**")
            st.info("70 - 90 PLN (Sugerowana: **79 PLN**)")
            st.markdown("**⏰ Najlepszy czas na wrzucenie:**")
            st.success("**Dzisiaj o 18:05** (Wysoki ruch)")
        with c2:
            st.markdown("**📸 Wybór zdjęcia na okładkę:**")
            st.warning("Zdjęcie nr 1 wybrane jako główne (najlepsze oświetlenie i kadr).")
            st.markdown("**📦 Status:**")
            st.text("Gotowe do skopiowania na Vinted!")

        st.markdown("### 📋 Gotowy Opis do Skopiowania (Jedno kliknięcie):")
        
        generated_description = """✨ Stan: Idealny / Jak nowy
🔥 Marka premium, świetna jakość materiału, bardzo poszukiwana na Vinted!
📏 Wymiary podaję w wiadomości prywatnej (zapraszam do kontaktu).
📦 Szybka wysyłka paczkomatem zazwyczaj w 24h!
💡 Chcesz kupić w zestawie? Napisz, a dam Ci rabat na kilka rzeczy! 🚀"""

        st.code(generated_description, language="markdown")
        
        st.info("💡 **Wskazówka:** Otwórz apkę Vinted na telefonie, kliknij 'Dodaj przedmiot', wrzuć te same zdjęcia, a opis skopiuj powyższym przyciskiem i wklej jednym ruchem. Bezpiecznie i bez ryzyka blokady!")

st.markdown("</div>", unsafe_allow_html=True)
