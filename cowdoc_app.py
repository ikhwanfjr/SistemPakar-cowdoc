import streamlit as st

# === Knowledge Base ===
rules = [
    {
        "penyakit": "Antraks",
        "gejala": ["Nafsu Makan Menurun", "Suhu Tubuh Tinggi", "Luka Pada Kulit", "Lesu dan Tidak Aktif"],
        "solusi": "Segera hubungi dokter hewan."
    },
    {
        "penyakit": "Penyakit Mulut dan Kuku (PMK)",
        "gejala": ["Diare", "Luka Pada Kulit", "Perut Kembung"],
        "solusi": "Cuci luka, hindari kontak dengan ternak lain."
    },
    {
        "penyakit": "Pneumonia",
        "gejala": ["Nafsu Makan Menurun", "Suhu Tubuh Tinggi", "Keluarnya Lendir dari Hidung", "Batuk"],
        "solusi": "Isolasi, beri antibiotik dan vitamin."
    },
    {
        "penyakit": "Diare Akut",
        "gejala": ["Nafsu Makan Menurun", "Suhu Tubuh Tinggi", "Diare"],
        "solusi": "Berikan oralit, dan jaga kebersihan kandang."
    },
    {
        "penyakit": "Mastitis",
        "gejala": ["Produksi Susu Menurun", "Lesu dan Tidak Aktif", "Suhu Tubuh Tinggi"],
        "solusi": "Periksa ambing, kompres hangat, beri antibiotik."
    }
]

# === Inference Engine ===
def diagnosa(gejala_input):
    for rule in rules:
        if all(g in gejala_input for g in rule["gejala"]):
            return rule
    return None

# === User Interface ===
st.title("🐄 CowDoc: Diagnosa Penyakit pada Ternak Sapi")

st.write("Silakan pilih gejala yang dialami oleh ternak sapi:")

gejala_list = [
    "Nafsu Makan Menurun",
    "Suhu Tubuh Tinggi",
    "Diare",
    "Keluarnya Lendir dari Hidung",
    "Batuk",
    "Luka Pada Kulit",
    "Lesu dan Tidak Aktif",
    "Mata Berair",
    "Perut Kembung",
    "Produksi Susu Menurun"
]

selected_gejala = []
for gejala in gejala_list:
    if st.checkbox(gejala):
        selected_gejala.append(gejala)

if st.button("Diagnosa Sekarang"):
    hasil = diagnosa(selected_gejala)
    if hasil:
        st.success(f"### Penyakit: {hasil['penyakit']}")
        st.markdown(f"**Solusi:** {hasil['solusi']}")
    else:
        st.warning("Gejala yang dipilih belum cukup untuk menyimpulkan penyakit tertentu. Silakan periksa kembali.")
