###
# Gerekli kutuphaneleri ekliyoruz
###
from asyncio.windows_events import NULL
import cv2
import pytesseract
import cv2
import streamlit as st

# pytesseract'ın calismasi icin tesseractin yuklu oldugu yeri belirtiyoruz
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# GUI olarak streamlit kullandigimiz icin input ile dosya yolunu aliyoruz
file_path = st.text_input('File path')
# Aldigimiz dosya yolunda varsa tirnak isaretlerini kaldiriyoruz
file_path = file_path.replace('"','')

# Streamlit ile buton olusturup, butona tiklandiginda img_to_string islemini yapiyoruz 
if st.button('Start Process',):
    img = cv2.imread(file_path) # resmi yukluyoruz
    st.write('Image:') # streamlit ile ekrana yazi yazdiriyoruz
    st.image(img,width=200) # streamlit ile resmi ekrana basiyoruz
    img = cv2.GaussianBlur(img,(5,5),0) # resim uzerindeki yazilarin daha belirgin olmasi icin blur ekliyoruz
    img = cv2.medianBlur(img,5) # resim uzerindeki yazilarin daha belirgin olmasi icin blur ekliyoruz
    retval, img = cv2.threshold(img,150,255, cv2.THRESH_BINARY) # resimin renk ayalarıi ile oynuyoruz. boylelikle beyaz kısımlar on plana cikiyor
    txt = pytesseract.image_to_string(img, lang='english') # pytesseract kullanarak hali hazirda egitilmis bir .traineddata dosyasi ile yaziyi texte donusturuyoruz
    #txt = pytesseract.image_to_string(img, lang='turkish') # pytesseract kullanarak hali hazirda egitilmis bir .traineddata dosyasi ile yaziyi texte donusturuyoruz
    st.write('Recognition: ', txt) # pytesseract'in dondurdugu yaziyi yazdiriyoruz