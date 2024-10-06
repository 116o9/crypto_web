import requests
from PIL import Image
import streamlit as st
import bcrypt
from streamlit_lottie import st_lottie
import os
from pathlib import Path
import pickle

# إعدادات الصفحة
st.set_page_config(page_title='Abood New Page', page_icon=':tada:', layout='wide')

# تحميل الصورة
image_contact_from = Image.open("C:\\Users\\abood\\first\\pythonProject\\.venv\\images\\Screenshot (1).png")

# تحميل أنماط CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("C:\\Users\\abood\\first\\pythonProject\\.venv\\style\\style.css")

# تحميل الرسوم المتحركة
lottie_code = "https://lottie.host/f6bfe2fe-fa8f-4c75-8ccd-84123c8e67d3/PB8kvEVfB1.json"

# بيانات المستخدم
names = ["abood", "abmmd"]
usernames = ["abood2012", "amfgk2001"]
passwords = ["asd123", "dsas321"]

# تشفير كلمات المرور باستخدام bcrypt وحفظها
hashed_passwords = [bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() for password in passwords]
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

# تحميل كلمات المرور المجزأة
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

# مصادقة المستخدم
def authenticate(username_input, password_input):
    if username_input in usernames:
        index = usernames.index(username_input)
        hashed = hashed_passwords[index].encode()
        return bcrypt.checkpw(password_input.encode(), hashed)
    return False

# واجهة تسجيل الدخول
with st.container():
    st.header("تسجيل الدخول")
    username_input = st.text_input("اسم المستخدم")
    password_input = st.text_input("كلمة المرور", type="password")
    if st.button("تسجيل الدخول"):
        if authenticate(username_input, password_input):
            st.success("تم تسجيل الدخول بنجاح!")

            # المحتوى الرئيسي للتطبيق
            st.subheader('Hi, I am abood')
            st.title("A new test web page")
            st.write('I am trying to make this web page using Python')
            st.write("[Instagram account](http://localhost:8501/)")

            # القسم الثاني
            with st.container():
                st.write("---")
                left_column, right_column = st.columns(2)
                with left_column:
                    st.header("شو بعمل؟")
                    st.write("##")
                    st.write("يمكنك استبدال [ARGUMENTS] بأي معطيات إضافية قد يتطلبها التطبيق الخاص بك.")

                with right_column:
                    st_lottie(lottie_code, height=300, key="coding")

            # القسم الثالث
            with st.container():
                st.write("---")
                st.header("My project")
                st.write("##")
                image_column, text_column = st.columns((1, 2))
                with image_column:
                    st.image(image_contact_from)

                with text_column:
                    st.subheader("Make your first website with us")
                    st.write("To create websites, there are several approaches and tools you can use depending on your experience level.")

            # قسم الاتصال
            with st.container():
                st.write("---")
                st.header("Get In Touch with me!")
                st.write("##")

                contact_form = """
                <form action="https://formsubmit.co/aboodpremium01@gmail.com" method="POST">
                 <input type="hidden" name="_captcha" value="false">
                 <input type="text" name="name" placeholder="Your name" required>
                 <input type="email" name="email" placeholder="Your Email" required>
                 <textarea name="message" placeholder="Your message here" required></textarea>
                 <button type="submit">Send</button>
                </form>
                """
                st.markdown(contact_form, unsafe_allow_html=True)
        else:
            st.error("اسم المستخدم أو كلمة المرور غير صحيحة")
