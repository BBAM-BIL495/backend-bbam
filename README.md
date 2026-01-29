# backend-posest
<img width="541" height="959" alt="Ekran görüntüsü 2026-01-16 210311" src="https://github.com/user-attachments/assets/6b105520-34e2-48e3-baa3-48197ef993f8" />

db kurulumu: postgresql içerisinde default servera giriş yapın ve içine bbam_db adında database oluşturun. sırayla bbam_database.sql ve mock_data.sql i query sekmesinden open file ile açıp f5 ile çalıştırın. db bilgilerini settings.py'a girdiğinizden emin olun.

python manage.py inspectdb > models.py yapılmış halini commitledim, db değişikliğinde generate edilmeli ve models.py'lar değiştirilmelidir.
python manage.py migrate --fake-initial yaptım ki olanı güncellesin eskiye ekleme yapmaya çalışmasın

genel build alımı:
python manage.py makemigrations  
python manage.py migrate --fake
opsiyonel: python manage.py shell ile dbnin baglandıgı kontrol edilebilir
python manage.py createsuperuser ile admin üyeliği oluşturulur
python manage.py runserver
http://127.0.0.1:8000/admin e gidilip superuser bilgileri girilir ve dbnin geldiği kontrol edilebilir

settings.py içindeki db syntaxı:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

todo: model isimlendirmelerini değiştireceğim