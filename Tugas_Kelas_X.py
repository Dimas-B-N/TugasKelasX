import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Dibuat dengan Python",page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open (file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

lottie_coding = load_lottieurl("https://lottie.host/dc349099-df43-4896-9145-852272b77317/pbvp2Qsk6C.json")


with st.container():   
    st.subheader("Assalamu'alaikum 👋")
    st.title("Tugas Bab 1 dan 2, Informatika Kelas X")
    st.write("Petunjuk: Baca di Buku Paket Informatika Kelas X, Bab 1 dan 2")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Jawablah pertanyaan di bawah ini di Buku Kerja Siswa masing-masing.")
        st.subheader("Setelah selesai, silakan dikumpulkan di meja saya di Labkom 4.")
        st.write(
            """
            1. Jelaskan pengertian istilah-istilah di bawah ini !
                 - Informatika
                 - Berpikir Komputasional
                 - Transformasi Digital
                 - Artificial Intelligence (Kecerdasan Buatan)
            2. Jelaskan tentang Sejarah Perkembangan Industri 1.0 s.d 4.0 !
            3. Deskripsikan situasi Masyarakat 5.0 (Society 5.0), dan berilah contoh dalam kehidupan sehari-hari (minimal 5) !
            4. Di Era Digital, banyak orang kehilangan pekerjaan karena kemajuan teknologi mengambil alih hal-hal yang mereka kerjakan, lalu bagaimana sikap kamu menghadapi situasi tersebut ? (Deskripsikan minimal dalam 50 kata)
            5. Bagaimanakah cara berkolaborasi dalam menyelesaikan permasalahan dalam kelompok menjadi lebih efektif dan efisien yang akhirnya dapat menghasilkan solusi terbaik dan tepat waktu ?
            6. Apa perbedaan dari Peran dan Tugas dalam suatu Kelompok ?
            7. Apa pengertian dan tujuan Berpikir Komputasional dalam kehidupan sehari-hari ? Beri contohnya minimal 4 !
            8. Jelaskan tentang 4 Pondasi Berpikir Komputasional dan berikan contoh dalam kehidupan sekitarmu !
            9. Sebutkan dan Jelaskan 4 Pondasi Berpikir Komputasional dalam penyelesaian permasalahan berikut ini :
                - Menggoreng Pisang
                - Mencuci Baju
             """
        )
    with right_column:
        st_lottie(lottie_coding, height=500, key="coding")
with st.container():
    st.write("---")