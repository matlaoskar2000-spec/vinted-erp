import streamlit as st
import json
import os
import time
from PIL import Image

# Konfiguracja strony
st.set_page_config(page_title="Vinted ERP Web Pro", page_icon="⚡", layout="wide")

BAZA_PLIK = "baza_magazyn_web.json"
TARGET_MIESIECZNY = 3000.0

def wczytaj_dane():
    if os.path.exists(BAZA_PLIK):
        try:
            with open(BAZA_PLIK, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []

def zapisz_dane(dane):
    with open(BAZA_PLIK, "w", encoding="utf-8") as f:
        json.dump(dane, f, ensure_ascii=False, indent=4)

baza = wczytaj_dane()

# Stylizacja Dark Mode (CSS)
st.markdown("""
    <style>
    .main { background-color: #080C14; color: #F8FAFC; }
    .stMetric { background-color: #0F172A; padding: 15px; border-radius: 10px; border: 1px solid #1E293B; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ VINTED RESELLER ERP - WEB & MOBILE")
st.markdown("Zarządzaj swoim magazynem, cenami i zyskami z komputera lub telefonu w podróży!")

# --- STATYSTYKI / DASHBOARD ---
do_wystawienia = len([x for x in baza if x["status"] == "Do wystawienia"])
sprzedane = [x for x in baza if x["status"] == "Sprzedane"]
zysk_calkowity = sum((x["cena_sprzedazy"] - x["cena_zakupu"] - 5.0) for x in sprzedane)

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="📦 W magazynie (Do wystawienia)", value=f"{do_wystawienia} szt.")
with col2:
    st.metric(label="🎯 Misyjny Zysk / Cel", value=f"{zysk_calkowity:.2f} / {TARGET_MIESIECZNY:.0f} PLN")
with col3:
    st.metric(label="📈 Prognoza Przychodu", value=f"{zysk_calkowity * 1.35:.2f} PLN")

st.divider()

# --- PANEL BOCZNY (FORMULARZ DODAWANIA) ---
st.sidebar.header("➕ Dodaj Nowy Przedmiot")
with st.sidebar.form("form_dodawania", clear_on_submit=True):
    t_nazwa = st.text_input("Tytuł / Nazwa przedmiotu")
    t_marka = st.text_input("Marka (np. Nike, Adidas)")
    t_rozmiar = st.text_input("Rozmiar (np. L, 42)")
    t_stan = st.text_input("Stan (np. Bardzo dobry)", value="Bardzo dobry")
    t_lokalizacja = st.text_input("Lokalizacja / Półka", value="K1-P1")
    t_zakup = st.number_input("Cena zakupu (PLN)", min_value=0.0, value=15.0)
    t_vinted = st.number_input("Cena sprzedaży Vinted (PLN)", min_value=0.0, value=50.0)
    
    zdjecie_plik = st.file_uploader("Zdjęcie przedmiotu", type=["jpg", "jpeg", "png"])
    
    submit = st.form_submit_button("Zapisz w magazynie")
    
    if submit and t_nazwa:
        sciezka_zdj = ""
        if zdjecie_plik:
            os.makedirs("zdjecia_web", exist_ok=True)
            sciezka_zdj = os.path.join("zdjecia_web", zdjecie_plik.name)
            with open(sciezka_zdj, "wb") as f:
                f.write(zdjecia_plik.getbuffer())

        # Generowanie opisu AI
        tagi = f"#{t_marka.lower().replace(' ', '')} #{t_rozmiar.lower()} #vinted #vintage #streetwear #y2k"
        opis_ai = f"🔥 MUST-HAVE: {t_nazwa.upper()} 🔥\n\n📌 Marka: {t_marka}\n📌 Rozmiar: {t_rozmiar}\n📌 Stan: {t_stan}\n\n🚚 Szybka wysyłka w 24h!\n\n{tagi}"

        nowy_item = {
            "id": max([x["id"] for x in baza], default=0) + 1,
            "nazwa": t_nazwa,
            "marka": t_marka,
            "rozmiar": t_rozmiar,
            "stan": t_stan,
            "lokalizacja": t_lokalizacja,
            "cena_zakupu": t_zakup,
            "cena_sprzedazy": t_vinted,
            "koszt_paliwa_pakowania": 5.0,
            "zdjecie": sciezka_zdj,
            "opis": opis_ai,
            "status": "Do wystawienia"
        }
        baza.append(nowy_item)
        zapisz_dane(baza)
        st.sidebar.success("Dodano pomyślnie!")
        st.rerun()

# --- GŁÓWNA TABELA MAGAZYNU ---
st.subheader("📋 Twoje Zasoby Magazynowe")

if not baza:
    st.info("Magazyn jest pusty. Dodaj pierwszy przedmiot za pomocą panelu po lewej stronie!")
else:
    for item in baza:
        with st.expander(f"#{item['id']} | {item['nazwa']} ({item['marka']} - {item['rozmiar']}) | Status: **{item['status']}**"):
            c1, c2, c3 = st.columns([1, 2, 1])
            with c1:
                if item.get("zdjecie") and os.path.exists(item["zdjecie"]):
                    st.image(item["zdjecie"], width=150)
                else:
                    st.write("Brak zdjęcia")
            with c2:
                st.write(f"🏷️ **Marka:** {item['marka']}")
                st.write(f"📏 **Rozmiar:** {item['rozmiar']} | 📍 **Półka:** {item['lokalizacja']}")
                st.write(f"💰 **Zakup:** {item['cena_zakupu']} zł | 🚀 **Vinted:** {item['cena_sprzedazy']} zł")
                czysty_zysk = item['cena_sprzedazy'] - item['cena_zakupu'] - item['koszt_paliwa_pakowania']
                st.write(f"💎 **Szacowany Czysty Zysk:** {czysty_zysk:.2f} zł")
                
                # Przycisk kopiowania opisu
                st.text_area(f"Opis AI do skopiowania (ID: {item['id']})", item['opis'], height=100)
            
            with c3:
                st.write("### Akcje")
                if item['status'] == "Do wystawienia":
                    if st.button(f"Oznacz jako Wystawione #{item['id']}", key=f"wyst_{item['id']}"):
                        item['status'] = "Wystawione"
                        zapisz_dane(baza)
                        st.rerun()
                elif item['status'] == "Wystawione":
                    if st.button(f"Oznacz jako Sprzedane #{item['id']}", key=f"sprz_{item['id']}"):
                        item['status'] = "Sprzedane"
                        zapisz_dane(baza)
                        st.rerun()
                
                if st.button(f"🗑️ Usuń #{item['id']}", key=f"del_{item['id']}"):
                    baza.remove(item)
                    zapisz_dane(baza)
                    st.rerun()