from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest


phones = [
    {"id": 1, "name": "iPhone 14 Pro", "brand": "Apple", "price": 12499000,
     "description": "Dynamic Island va 48MP asosiy kamera bilan eng yangi iPhone.",
     "image": "myapp/images/iphone14pro.jpg", "stock": 10, "rating": 4.9,
     "ram": "6 GB", "storage": "128 GB", "soc": "Apple A16 Bionic",
     "display": "6.1\" OLED, 2556×1179, ProMotion 120Hz", "battery": "3200 mAh",
     "camera": "48 MP (main) + 12 MP (ultrawide) + 12 MP (telephoto)", "os": "iOS"},
    {"id": 2, "name": "iPhone 13", "brand": "Apple", "price": 9999000,
     "description": "A15 Bionic chip va 12MP kamera bilan ishonchli ishlash.",
     "image": "myapp/images/iphone13.jpg", "stock": 8, "rating": 4.8,
     "ram": "4 GB", "storage": "128 GB", "soc": "Apple A15 Bionic",
     "display": "6.1\" OLED, 2532×1170", "battery": "3240 mAh",
     "camera": "12 MP + 12 MP (dual)", "os": "iOS"},
    {"id": 3, "name": "iPhone 12", "brand": "Apple", "price": 8599000,
     "description": "5G va Super Retina XDR displey bilan jihozlangan.",
     "image": "myapp/images/iphone12.jpg", "stock": 12, "rating": 4.7,
     "ram": "4 GB", "storage": "64 GB", "soc": "Apple A14 Bionic",
     "display": "6.1\" OLED, 2532×1170", "battery": "2815 mAh",
     "camera": "12 MP + 12 MP (dual)", "os": "iOS"},
    {"id": 4, "name": "iPhone SE (2022)", "brand": "Apple", "price": 5899000,
     "description": "Kichik korpusda kuchli A15 chip.",
     "image": "myapp/images/iphonese.jpg", "stock": 15, "rating": 4.6,
     "ram": "4 GB", "storage": "64 GB", "soc": "Apple A15 Bionic",
     "display": "4.7\" Retina HD", "battery": "2018 mAh",
     "camera": "12 MP (single)", "os": "iOS"},

    {"id": 5, "name": "Samsung Galaxy S23 Ultra", "brand": "Samsung", "price": 13999000,
     "description": "200MP kamera va Snapdragon 8 Gen 2 chip.",
     "image": "myapp/images/s23ultra.jpg", "stock": 6, "rating": 4.9,
     "ram": "12 GB", "storage": "256 GB", "soc": "Snapdragon 8 Gen 2",
     "display": "6.8\" AMOLED, 3088×1440, 120Hz", "battery": "5000 mAh",
     "camera": "200 MP (main) + 12 MP (ultrawide) + 10 MP (periscope) + 10 MP (tele)", "os": "Android"},
    {"id": 6, "name": "Samsung Galaxy S23", "brand": "Samsung", "price": 10999000,
     "description": "Kuchli protsessor va mukammal ekran sifati.",
     "image": "myapp/images/s23.jpg", "stock": 9, "rating": 4.8,
     "ram": "8 GB", "storage": "128 GB", "soc": "Snapdragon 8 Gen 2",
     "display": "6.1\" AMOLED, 2340×1080, 120Hz", "battery": "3900 mAh",
     "camera": "50 MP (main) + 12 MP (ultrawide) + 10 MP (tele)", "os": "Android"},
    {"id": 7, "name": "Samsung Galaxy Z Flip 5", "brand": "Samsung", "price": 12999000,
     "description": "Katlanadigan dizayn va yuqori texnologiyalar.",
     "image": "myapp/images/zflip5.jpg", "stock": 5, "rating": 4.7,
     "ram": "8 GB", "storage": "256 GB", "soc": "Snapdragon 8 Gen 2",
     "display": "6.7\" Foldable AMOLED (main) + 3.4\" cover", "battery": "3700 mAh",
     "camera": "12 MP + 12 MP (dual)", "os": "Android"},
    {"id": 8, "name": "Samsung Galaxy A54", "brand": "Samsung", "price": 5499000,
     "description": "Yuqori sifatli o‘rta toifa smartfon.",
     "image": "myapp/images/a54.jpg", "stock": 20, "rating": 4.5,
     "ram": "6 GB", "storage": "128 GB", "soc": "Exynos / MediaTek (region)", 
     "display": "6.4\" Super AMOLED, 2400×1080, 120Hz", "battery": "5000 mAh",
     "camera": "50 MP + 12 MP + 5 MP", "os": "Android"},

    {"id": 9, "name": "Xiaomi 13 Pro", "brand": "Xiaomi", "price": 8799000,
     "description": "Leica kamera hamkorligi va 120W tez zaryad.",
     "image": "myapp/images/xiaomi13pro.jpg", "stock": 10, "rating": 4.8,
     "ram": "12 GB", "storage": "256 GB", "soc": "Snapdragon 8 Gen 2",
     "display": "6.73\" AMOLED, 3200×1440, 120Hz", "battery": "4820 mAh",
     "camera": "50 MP (main) + 50 MP (ultrawide) + 50 MP (tele)", "os": "Android"},
    {"id": 10, "name": "Xiaomi 12T Pro", "brand": "Xiaomi", "price": 7299000,
     "description": "200MP kamera va 120W zaryad bilan jihozlangan.",
     "image": "myapp/images/xiaomi12tpro.jpg", "stock": 14, "rating": 4.7,
     "ram": "8 GB", "storage": "256 GB", "soc": "Snapdragon 8+ Gen 1",
     "display": "6.67\" AMOLED, 2712×1220, 120Hz", "battery": "5000 mAh",
     "camera": "200 MP (main) + 8 MP + 2 MP", "os": "Android"},
    {"id": 11, "name": "Redmi Note 12 Pro", "brand": "Xiaomi", "price": 4499000,
     "description": "108MP kamera va AMOLED displey bilan.",
     "image": "myapp/images/redmi12pro.jpg", "stock": 25, "rating": 4.5,
     "ram": "6 GB", "storage": "128 GB", "soc": "MediaTek Dimensity 1080",
     "display": "6.67\" AMOLED, 2400×1080, 120Hz", "battery": "5000 mAh",
     "camera": "108 MP + 8 MP + 2 MP", "os": "Android"},
    {"id": 12, "name": "Poco F5", "brand": "Xiaomi", "price": 4799000,
     "description": "Snapdragon 7+ Gen 2 bilan kuchli ishlash.",
     "image": "myapp/images/pocof5.jpg", "stock": 18, "rating": 4.6,
     "ram": "8 GB", "storage": "128 GB", "soc": "Snapdragon 7+ Gen 2",
     "display": "6.67\" AMOLED, 2400×1080, 120Hz", "battery": "5000 mAh",
     "camera": "64 MP + 8 MP + 2 MP", "os": "Android"},

    {"id": 13, "name": "Huawei P60 Pro", "brand": "Huawei", "price": 8999000,
     "description": "Raqobatsiz kamera va kuchli dizayn.",
     "image": "myapp/images/p60pro.jpg", "stock": 7, "rating": 4.8,
     "ram": "8 GB", "storage": "256 GB", "soc": "Kirin/Qualcomm (region)", 
     "display": "6.6\" OLED, 1220×2700", "battery": "4800 mAh",
     "camera": "50 MP + 48 MP + 13 MP (periscope variantlarda)", "os": "HarmonyOS/Android (region)"},
    {"id": 14, "name": "Huawei Nova 11", "brand": "Huawei", "price": 5799000,
     "description": "O‘rta sinf uchun kuchli performans.",
     "image": "myapp/images/nova11.jpg", "stock": 16, "rating": 4.5,
     "ram": "8 GB", "storage": "128 GB", "soc": "Qualcomm/MediaTek (region)",
     "display": "6.67\" OLED, 120Hz", "battery": "4500 mAh",
     "camera": "50 MP + 8 MP + macro", "os": "HarmonyOS/Android (region)"},

    {"id": 15, "name": "Google Pixel 7 Pro", "brand": "Google", "price": 9499000,
     "description": "Tensor G2 chip va ajoyib kamera tizimi.",
     "image": "myapp/images/pixel7pro.jpg", "stock": 9, "rating": 4.9,
     "ram": "12 GB", "storage": "128 GB", "soc": "Google Tensor G2",
     "display": "6.7\" LTPO OLED, 3120×1440, 120Hz", "battery": "5000 mAh",
     "camera": "50 MP + 12 MP + 48 MP (tele)", "os": "Android"},
    {"id": 16, "name": "Google Pixel 7", "brand": "Google", "price": 7499000,
     "description": "Eng toza Android tajribasi.",
     "image": "myapp/images/pixel7.jpg", "stock": 11, "rating": 4.7,
     "ram": "8 GB", "storage": "128 GB", "soc": "Google Tensor G2",
     "display": "6.3\" AMOLED, 2400×1080, 90Hz", "battery": "4355 mAh",
     "camera": "50 MP + 12 MP", "os": "Android"},

    {"id": 17, "name": "OnePlus 11", "brand": "OnePlus", "price": 7999000,
     "description": "Snapdragon 8 Gen 2 va 120Hz AMOLED displey.",
     "image": "myapp/images/oneplus11.jpg", "stock": 8, "rating": 4.7,
     "ram": "8/16 GB", "storage": "128/256 GB", "soc": "Snapdragon 8 Gen 2",
     "display": "6.7\" AMOLED, 3216×1440, 120Hz", "battery": "5000 mAh",
     "camera": "50 MP + 48 MP + 32 MP (varies)", "os": "Android"},
    {"id": 18, "name": "OnePlus Nord 3", "brand": "OnePlus", "price": 5699000,
     "description": "Balansli narx va kuchli ishlash.",
     "image": "myapp/images/nord3.jpg", "stock": 15, "rating": 4.6,
     "ram": "8 GB", "storage": "128 GB", "soc": "Mediatek Dimensity 9000",
     "display": "6.7\" AMOLED, 120Hz", "battery": "5000 mAh",
     "camera": "50 MP + 8 MP + 2 MP", "os": "Android"},

    {"id": 19, "name": "Oppo Reno 10 Pro", "brand": "Oppo", "price": 6599000,
     "description": "Yorqin dizayn va kuchli kamera.",
     "image": "myapp/images/reno10pro.jpg", "stock": 13, "rating": 4.6,
     "ram": "8 GB", "storage": "256 GB", "soc": "Mediatek Dimensity 8200",
     "display": "6.7\" AMOLED, 120Hz", "battery": "5000 mAh",
     "camera": "50 MP + 8 MP + 2 MP", "os": "Android"},
    {"id": 20, "name": "Oppo Find X5", "brand": "Oppo", "price": 9499000,
     "description": "Flagman dizayn va premium kamera.",
     "image": "myapp/images/findx5.jpg", "stock": 9, "rating": 4.7,
     "ram": "8/12 GB", "storage": "128/256 GB", "soc": "Snapdragon 8 Gen 1",
     "display": "6.7\" AMOLED, 120Hz", "battery": "4800 mAh",
     "camera": "50 MP + 50 MP + 13 MP", "os": "Android"},

    {"id": 21, "name": "Realme GT Neo 5", "brand": "Realme", "price": 4999000,
     "description": "240W tez zaryadlash texnologiyasi.",
     "image": "myapp/images/gtneo5.jpg", "stock": 17, "rating": 4.6,
     "ram": "8 GB", "storage": "256 GB", "soc": "Snapdragon 8+ Gen 1",
     "display": "6.7\" AMOLED, 120Hz", "battery": "5500 mAh",
     "camera": "50 MP + 8 MP + 2 MP", "os": "Android"},
    {"id": 22, "name": "Realme 11 Pro+", "brand": "Realme", "price": 4399000,
     "description": "100MP kamera va AMOLED displey.",
     "image": "myapp/images/realme11pro.jpg", "stock": 22, "rating": 4.5,
     "ram": "8 GB", "storage": "128 GB", "soc": "MediaTek/Dimensity (variant)",
     "display": "6.7\" AMOLED, 120Hz", "battery": "5000 mAh",
     "camera": "100 MP + 8 MP + 2 MP", "os": "Android"},

    {"id": 23, "name": "Honor 90", "brand": "Honor", "price": 5199000,
     "description": "200MP kamera va zamonaviy dizayn.",
     "image": "myapp/images/honor90.jpg", "stock": 14, "rating": 4.6,
     "ram": "8 GB", "storage": "256 GB", "soc": "Snapdragon 7 Gen 1",
     "display": "6.7\" OLED, 120Hz", "battery": "4600 mAh",
     "camera": "200 MP + 8 MP + 2 MP", "os": "Android"},
    {"id": 24, "name": "Honor Magic5 Pro", "brand": "Honor", "price": 9799000,
     "description": "Flagman kamera tizimi bilan.",
     "image": "myapp/images/magic5pro.jpg", "stock": 7, "rating": 4.8,
     "ram": "12 GB", "storage": "256 GB", "soc": "Snapdragon 8 Gen 2",
     "display": "6.8\" OLED, 120Hz", "battery": "5100 mAh",
     "camera": "50 MP + 50 MP + 50 MP (triple)", "os": "Android"},

    {"id": 25, "name": "Vivo V29", "brand": "Vivo", "price": 4799000,
     "description": "108MP kamera va yorqin displey.",
     "image": "myapp/images/vivo29.jpg", "stock": 18, "rating": 4.6,
     "ram": "8 GB", "storage": "128 GB", "soc": "MediaTek/Qualcomm variant",
     "display": "6.7\" AMOLED, 120Hz", "battery": "4600 mAh",
     "camera": "108 MP + 8 MP + 2 MP", "os": "Android"},
    {"id": 26, "name": "Vivo X90 Pro", "brand": "Vivo", "price": 9499000,
     "description": "MediaTek Dimensity 9200 bilan flagman tajriba.",
     "image": "myapp/images/x90pro.jpg", "stock": 9, "rating": 4.8,
     "ram": "12 GB", "storage": "256 GB", "soc": "MediaTek Dimensity 9200",
     "display": "6.78\" AMOLED, 120Hz", "battery": "4700 mAh",
     "camera": "50 MP + 50 MP + 50 MP", "os": "Android"},

    {"id": 27, "name": "Infinix Zero 30", "brand": "Infinix", "price": 3299000,
     "description": "O‘rta toifa uchun kuchli xususiyatlar.",
     "image": "myapp/images/zero30.jpg", "stock": 25, "rating": 4.4,
     "ram": "8 GB", "storage": "128 GB", "soc": "MediaTek Dimensity 8200",
     "display": "6.67\" AMOLED, 120Hz", "battery": "4500 mAh",
     "camera": "50 MP + 8 MP + 2 MP", "os": "Android"},
    {"id": 28, "name": "Tecno Camon 20 Pro", "brand": "Tecno", "price": 2999000,
     "description": "Arzon narxda sifatli smartfon.",
     "image": "myapp/images/camon20pro.jpg", "stock": 28, "rating": 4.3,
     "ram": "8 GB", "storage": "128 GB", "soc": "MediaTek Helio/G95 variant",
     "display": "6.67\" AMOLED, 90/120Hz", "battery": "5000 mAh",
     "camera": "64 MP + 8 MP + 2 MP", "os": "Android"},

    {"id": 29, "name": "Nokia G60", "brand": "Nokia", "price": 3599000,
     "description": "Uzoq muddatli yangilanishlar va mustahkam korpus.",
     "image": "myapp/images/nokiag60.jpg", "stock": 20, "rating": 4.4,
     "ram": "6 GB", "storage": "128 GB", "soc": "Qualcomm Snapdragon (midrange)",
     "display": "6.58\" LCD/POLED (modelga bog'liq)", "battery": "4500 mAh",
     "camera": "50 MP + 8 MP + 2 MP", "os": "Android"},
    {"id": 30, "name": "Asus ROG Phone 7", "brand": "Asus", "price": 12999000,
     "description": "Geymerlar uchun yaratilgan kuchli smartfon.",
     "image": "myapp/images/rog7.jpg", "stock": 5, "rating": 4.9,
     "ram": "16 GB", "storage": "512 GB", "soc": "Snapdragon 8 Gen 2",
     "display": "6.78\" AMOLED, 2448×1080, 165Hz", "battery": "6000 mAh",
     "camera": "50 MP + 13 MP + 8 MP", "os": "Android"}
]



def home(requests:HttpRequest):
    return render(request=requests, template_name="index.html")

def telephones(requests:HttpRequest):
    phone = {
        "phones": phones
    }
    return render(request=requests, template_name="telephones.html", context=phone)

def contact(requests:HttpRequest):
    return render(request=requests, template_name="contact.html")

def register(requests: HttpRequest):
    return render(request=requests, template_name="register.html")

def basket(requests: HttpRequest):
    return render(request=requests, template_name="savatcha.html")

def tel_detail(requests: HttpRequest, tel_id:int):
    for tel in phones:
        if tel['id'] == tel_id:
            return render(request=requests, template_name="telephone_detail.html", context={"tel": tel} )
    return HttpRequest("bizning dokonimizda mavjud emas")

def add_basket(requests:HttpRequest, tel_id:int):
    savatcha = []
    for phone in phones:
        if phone['id'] == tel_id:
            savatcha.append(phone)
            return render(request=requests, template_name="savatcha.html", context={"savat": savatcha} )
    return render(request=requests, template_name="savatcha.html")   
    