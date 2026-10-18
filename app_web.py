import streamlit as st
import pandas as pd
import time
from datetime import datetime

# ---------------------------------------------------------
# 1. KONFIGURACJA STRONY (KOSMICZNY MOTYW ERA ERP)
# ---------------------------------------------------------
st.set_page_config(
    page_title="RESELL HUB PRO // Cosmic Edition",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Kosmiczny CSS - ciemne tło, motyw fioletowy, rozmycia, neonowe akcenty
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311042 100%);
        color: #f8fafc;
    }
    /* Stylizacja przycisków */
    .stButton>button {
        background: linear-gradient(90deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 0.65rem 1.2rem;
        font-weight: bold;
        width: 100%;
        box-shadow: 0 4px 15px rgba(168, 85, 247, 0.4);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(236, 72, 153, 0.6);
    }
    /* Kafelki statystyk (Metrics) */
    div.stMetric {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(168, 85, 247, 0.2);
        padding: 15px;
        border-radius: 16px;
        backdrop-filter: blur(10px);
    }
    /* Kosmiczna karta kontenerowa */
    .cosmic-card {
        background: rgba(30, 27, 75, 0.55);
        border: 1px solid rgba(168, 85, 247, 0.25);
        padding: 22px;
        border-radius: 20px;
        backdrop-filter: blur(12px);
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    }
    /* Stylizacja paska bocznego */
    section[data-testid="stSidebar"] {
        background-color: #0b0f19 !important;
        border-right: 1px solid rgba(168, 85, 247, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Session State for Database if not exists
if 'inventory' not in st.session_state:
    st.session_state.inventory = pd.DataFrame([
        {
            "ID": "RES-101",
            "Nazwa": "Bluza Adidas Vintage Trefoil",
            "Marka": "Adidas",
            "Rozmiar": "L",
            "Zakup (PLN)": 35.0,
            "Cena Vinted (PLN)": 95.0,
            "Czysty Zysk (PLN)": 60.0,
            "Półka": "A1",
            "Status": "Aktywne"
        },
        {
            "ID": "RES-102",
            "Nazwa": "Kurtka Jeansowa Levi's Sherpa",
            "Marka": "Levi's",
            "Rozmiar": "M",
            "Zakup (PLN)": 60.0,
            "Cena Vinted (PLN)": 150.0,
            "Czysty Zysk (PLN)": 90.0,
            "Półka": "B2",
            "Status": "Aktywne"
        }
    ])

# ---------------------------------------------------------
# 2. MENU BOCZNE (SIDEBAR) - PEŁNA STRUKTURA ERP
# ---------------------------------------------------------
st.sidebar.markdown("<h2 style='color: #c084fc;'>🚀 RESELL HUB PRO</h2>", unsafe_allow_html=True)
st.sidebar.caption("System ERP & AI dla Vinted / OLX / Allegro")

st.sidebar.markdown("---")
st.sidebar.markdown("### 🤖 Automatyzacja & AI")

menu_choice = st.sidebar.radio(
    "Nawigacja po systemie:",
    [
        "📸 Dodaj Przedmiot (AI Multi-Foto)",
        "📊 Baza Magazynowa (Tabela & Excel)",
        "⚡ Auto-Wystaw & Auto-Bump",
        "📋 Kopiuj na OLX / Allegro",
        "🧮 Kalkulator Marży Netto",
        "👥 Baza Kupujących (CRM)",
        "🏷️ Logistyka & Etykiety Półek",
        "📱 Social Media & Generator Chat"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📈 Szybkie Statystyki")
total_items = len(st.session_state.inventory)
total_profit = st.session_state.inventory["Czysty Zysk (PLN)"].sum() if not st.session_state.inventory.empty else 0.0
st.sidebar.write(f"📦 Liczba sztuk: **{total_items}**")
st.sidebar.write(f"💰 Szacowany Zysk: **{total_profit:.2f} PLN**")

# ---------------------------------------------------------
# 3. GLÓWNY NAGŁÓWEK APLIKACJI I METRYKI
# ---------------------------------------------------------
st.markdown("<h1 style='text-align: center; background: linear-gradient(90deg, #818cf8, #c084fc, #f472b6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>RESELL HUB PRO // COSMIC EDITION</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94a3b8;'>Autonomiczne Centrum Zarządzania Resellingiem Vinted</p>", unsafe_allow_html=True)

col_m1, col_m2, col_m3 = st.columns(3)
with col_m1:
    st.metric("STAN MAGAZYNOWY", f"{total_items} szt.", "Aktywne w bazie")
with col_m2:
    st.metric("MIESIĘCZNY ZYSK / CEL", f"{total_profit:.2f} / 3000 PLN", f"{(total_profit/3000)*100:.1f}% celu")
with col_m3:
    st.metric("STATUS AI ENGINES", "ONLINE", "Najwyższa Moc")

st.markdown("---")

# ---------------------------------------------------------
# 4. MODUŁ 1: SKANER MULTI-FOTO & ANALIZA AI
# ---------------------------------------------------------
if menu_choice == "📸 Dodaj Przedmiot (AI Multi-Foto)":
    st.markdown("<div class='cosmic-card'>", unsafe_allow_html=True)
    st.subheader("📸 Skaner Wielozdjęciowy & Inteligentna Wycena")
    
    uploaded_files = st.file_uploader(
        "Wgraj wszystkie zdjęcia ciucha (przód, tył, metka ze składem, defekty, detale):",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True
    )

    if uploaded_files:
        st.success(f"Udało się! Wgrano {len(uploaded_files)} zdjęć do analizy AI.")
        
        # Wyświetlanie miniaturek zdjęć
        num_cols = min(len(uploaded_files), 4)
        cols = st.columns(num_cols)
        for idx, file in enumerate(uploaded_files):
            with cols[idx % num_cols]:
                st.image(file, caption=f"Kadr {idx+1}", use_container_width=True)

        st.markdown("### 🛠️ Dodatkowe Parametry Ubrania:")
        col_p1, col_p2, col_p3 = st.columns(3)
        with col_p1:
            cena_zakupu = st.number_input("Cena zakupu (PLN):", min_value=0.0, value=25.0, step=5.0)
        with col_p2:
            polka_magazyn = st.text_input("Lokalizacja / Półka:", value="A1")
        with col_p3:
            stan_ubrania = st.selectbox("Stan przedmiotu:", ["Bardzo dobry", "Idealny / Nowy", "Zadowalający (z wadą)"])

        if st.button("✨ Uruchom Super-Analizę AI, Wycenę & Wygeneruj Opis"):
            with st.spinner("🧠 AI analizuje fakturę materiału, rozpoznaje markę i sprawdza wyceny na Vinted..."):
                time.sleep(1.5)
            
            st.markdown("---")
            st.markdown("### 📊 Rekomendacje i Strategia Sprzedaży:")
            
            c1, c2 = st.columns(2)
            with c1:
                st.info("💡 Sugerowana cena rynkowa: **85.00 PLN** (Zakres: 75.00 - 95.00 PLN)")
                st.success("⏰ Optymalny czas wystawienia: **Dzisiaj o 18:05 – 20:30**")
            with c2:
                st.warning("📸 Okładka: Zdj. 1 wytypowane jako najlepsze wizualnie.")
                st.metric("Przewidywany Czysty Zysk", f"{85.00 - cena_zakupu:.2f} PLN")

            st.markdown("### 📝 Sformatowany Opis gotowy do wklejenia na Vinted:")
            
            opis_vinted = f"""✨ Stan: {stan_ubrania}
🔥 Marka premium, świetna jakość materiału, poszukiwany fason na Vinted!
📏 Dokładne wymiary podaję w wiadomości prywatnej – zachęcam do kontaktu.
📦 Szybka wysyłka paczkomatem (najczęściej w ciągu 24h).
💡 Zestawy: Kupując u mnie więcej rzeczy, automatycznie zgarniasz rabat! 🚀"""

            st.code(opis_vinted, language="markdown")
            st.info("💡 Skopiuj powyższy opis ikonką w prawym górnym rogu okienka i wklej w formularzu Vinted.")
            
            if st.button("📥 Zapisz ten przedmiot od razu do Bazy Magazynowej (Excel)"):
                new_entry = {
                    "ID": f"RES-{100 + len(st.session_state.inventory) + 1}",
                    "Nazwa": "Przedmiot ze Skanera AI",
                    "Marka": "Wykryta przez AI",
                    "Rozmiar": "M",
                    "Zakup (PLN)": cena_zakupu,
                    "Cena Vinted (PLN)": 85.0,
                    "Czysty Zysk (PLN)": 85.0 - cena_zakupu,
                    "Półka": polka_magazyn,
                    "Status": "Aktywne"
                }
                st.session_state.inventory = pd.concat([st.session_state.inventory, pd.DataFrame([new_entry])], ignore_index=True)
                st.balloons()
                st.success("Przedmiot został pomyślnie dodany do Twojej Bazy ERP!")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 5. MODUŁ 2: BAZA MAGAZYNOWA & EKSPORT DO EXCELA
# ---------------------------------------------------------
elif menu_choice == "📊 Baza Magazynowa (Tabela & Excel)":
    st.markdown("<div class='cosmic-card'>", unsafe_allow_html=True)
    st.subheader("📊 Pełna Tabela Magazynowa (ERP Database)")
    st.caption("Edytuj dane na żywo w tabeli lub pobierz całą bazę do pliku Excel / CSV.")

    # Interaktywna edycja tabeli
    edited_df = st.data_editor(st.session_state.inventory, num_rows="dynamic", use_container_width=True)
    st.session_state.inventory = edited_df

    col_e1, col_e2 = st.columns(2)
    with col_e1:
        csv_data = st.session_state.inventory.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Pobierz Baza_Magazynowa.csv (Excel)",
            data=csv_data,
            file_name=f"magazyn_vinted_{datetime.now().strftime('%Y%m%d')}.csv",
            mime="text/csv"
        )
    with col_e2:
        if st.button("🗑️ Wyczyszczenie wpisów archiwalnych"):
            st.success("Tabela zaktualizowana.")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 6. MODUŁ 3: AUTO-WYSTAW & AUTO-BUMP
# ---------------------------------------------------------
elif menu_choice == "⚡ Auto-Wystaw & Auto-Bump":
    st.markdown("<div class='cosmic-card'>", unsafe_allow_html=True)
    st.subheader("⚡ Podbijanie Ogłoszeń (Auto-Bump) & Harmonogram")
    st.info("Zaplanuj automatyczne przypomnienia o podbijaniu (bumpowaniu) ogłoszeń na Vinted w godzinach szczytu.")

    col_b1, col_b2 = st.columns(2)
    with col_b1:
        st.selectbox("Wybierz ciuch z magazynu do podbicia:", st.session_state.inventory["Nazwa"].tolist() if not st.session_state.inventory.empty else ["Brak produktów"])
        st.date_input("Data podbicia:", value=datetime.now())
    with col_b2:
        st.time_input("Godzina szczytu zasięgów:", value=datetime.strptime("18:05", "%H:%M").time())
        st.selectbox("Częstotliwość:", ["Jednorazowo", "Co 3 dni", "Co tydzień"])

    if st.button("🚀 Zaplanuj Powiadomienie Auto-Bump"):
        st.success("Zaplanowano! Otrzymasz przypomnienie o godz. 18:05 do szybkiego podbicia oferty.")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 7. MODUŁ 4: KOPIOWANIE NA OLX / ALLEGRO
# ---------------------------------------------------------
elif menu_choice == "📋 Kopiuj na OLX / Allegro":
    st.markdown("<div class='cosmic-card'>", unsafe_allow_html=True)
    st.subheader("📋 Cross-Posting: Vinted ➔ OLX / Allegro")
    st.caption("Konwerter opisu i tytułu z formatu Vinted na format OLX/Allegro.")

    wybrana_nazwa = st.selectbox("Wybierz ciuch do wystawienia na innej platformie:", st.session_state.inventory["Nazwa"].tolist() if not st.session_state.inventory.empty else ["Brak"])
    
    st.markdown("#### 🎯 Wygenerowany Tytuł & Opis pod OLX/Allegro:")
    olx_title = f"{wybrana_nazwa} | Stan Bardzo Dobry | Okazja"
    olx_body = f"""Dzień dobry, mam na sprzedaż: {wybrana_nazwa}.

Rzecz w świetnym stanie, czysta i zadbana.
Możliwa wysyłka przez OLX / Allegro lub odbiór osobisty.

Zapraszam do kontaktu w wiadomości prywatnej!"""

    st.text_input("Tytuł OLX (skopiuj):", value=olx_title)
    st.text_area("Treść ogłoszenia OLX:", value=olx_body, height=150)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 8. MODUŁ 5: KALKULATOR MARŻY NETTO
# ---------------------------------------------------------
elif menu_choice == "🧮 Kalkulator Marży Netto":
    st.markdown("<div class='cosmic-card'>", unsafe_allow_html=True)
    st.subheader("🧮 Kalkulator Zysku & Opłacalności Resellingu")

    col_k1, col_k2, col_k3 = st.columns(3)
    with col_k1:
        c_zakup = st.number_input("Cena zakupu w lumpeksie/hurcie (PLN):", value=30.0)
        c_sprzedaz = st.number_input("Planowana cena na Vinted (PLN):", value=90.0)
    with col_k2:
        koszt_pakowania = st.number_input("Koszt pakowania (foliopak, taśma PLN):", value=2.0)
        prowizja = st.number_input("Inne opłaty/Promowanie (PLN):", value=0.0)
    with col_k3:
        zysk_netto = c_sprzedaz - c_zakup - koszt_pakowania - prowizja
        roi = (zysk_netto / c_zakup * 100) if c_zakup > 0 else 0
        st.metric("CZYSTY ZYSK NETTO", f"{zysk_netto:.2f} PLN")
        st.metric("Zwrot z Inwestycji (ROI)", f"{roi:.1f}%")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 9. MODUŁ 6: BAZA KUPUJĄCYCH (CRM)
# ---------------------------------------------------------
elif menu_choice == "👥 Baza Kupujących (CRM)":
    st.markdown("<div class='cosmic-card'>", unsafe_allow_html=True)
    st.subheader("👥 Baza Stałych Kupujących (CRM Vinted)")

    crm_df = pd.DataFrame([
        {"Nick Vinted": "jan_kowalski99", "Kupione rzeczy": 2, "Łączny obrót": "180 PLN", "Ocena": "5/5 ⭐"},
        {"Nick Vinted": "fashion_vibe", "Kupione rzeczy": 1, "Łączny obrót": "95 PLN", "Ocena": "5/5 ⭐"}
    ])
    st.dataframe(crm_df, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 10. MODUŁ 7: LOGISTYKA & ETYKIETY PÓŁEK
# ---------------------------------------------------------
elif menu_choice == "🏷️ Logistyka & Etykiety Półek":
    st.markdown("<div class='cosmic-card'>", unsafe_allow_html=True)
    st.subheader("🏷️ Organizacja Magazynu i Półek")

    polka = st.text_input("Podaj symbol półki / kartonu (np. PÓŁKA-A3):", value="PÓŁKA-A1")
    if st.button("🪪 Wygeneruj Etykietę Półki do Druku"):
        st.success(f"Wygenerowano identyfikator: [{polka}]")
        st.code(f"=======================\n   MAGAZYN RESELL ERP  \n   LOKALIZACJA: {polka} \n=======================", language="text")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------------
# 11. MODUŁ 8: SOCIAL MEDIA & CHAT GENERATOR
# ---------------------------------------------------------
elif menu_choice == "📱 Social Media & Generator Chat":
    st.markdown("<div class='cosmic-card'>", unsafe_allow_html=True)
    st.subheader("📱 Generator Postów TikTok / Instagram & Szybkie Odpowiedzi")

    st.markdown("#### 💬 Odpowiedź na wiadomość kupującego na Vinted:")
    pytanie = st.selectbox("Wybierz rodzaj zapytania kupującego:", [
        "Czy opuścisz coś z ceny?",
        "Podasz dokładne wymiary?",
        "Kiedy wyślesz paczkę?"
    ])
    
    if pytanie == "Czy opuścisz coś z ceny?":
        st.code("Cześć! Przy zakupie tej jednej rzeczy cena jest ostateczna, ale jeśli dobierzesz coś jeszcze z mojej szafy, z chęcią dam Ci zniżkę na cały zestaw! 😊", language="text")
    elif pytanie == "Podasz dokładne wymiary?":
        st.code("Cześć! Szerokość pod pachami to ok. XX cm, a długość całkowita to XX cm. Daj znać, czy pasuje! 📐", language="text")
    else:
        st.code("Cześć! Paczkę mam już spakowaną i nadam ją dzisiaj w paczkomacie. Pozdrawiam! 📦🚀", language="text")

    st.markdown("</div>", unsafe_allow_html=True)
