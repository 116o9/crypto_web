import pickle
from pathlib import Path
import bcrypt

# قائمة أسماء المستخدمين وكلمات المرور
names = ["abood", "abmmd"]
usernames = ["abood2012", "amfgk2001"]

# تجزئة كلمات المرور باستخدام bcrypt
hashed_passwords = [bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode('utf-8') for password in passwords]

# إنشاء مسار لحفظ كلمات المرور المجزأة
file_path = Path(__file__).parent / "hashed_pw.pkl"

# حفظ كلمات المرور المجزأة في الملف
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)

print("تم حفظ كلمات المرور المجزأة في الملف بنجاح.")
