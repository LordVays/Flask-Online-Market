from webapp import create_app

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        from webapp.models import db, Product
        
        db.create_all()
        
        if Product.query.count() == 0:
            products = [
                Product(name='Apple Iphone 16 Pro Max', price=148990, description='Большой флагманский смартфон Apple, OLED, 6.9 дюйма, 2868х1320 пикселей, 120 Гц, 8ГБ/1ТБ, Apple A18 Pro, 6 ядер, 48МП/48МП/12МП, 4685 мАч', image='Iphone16ProMax.webp'),
                Product(name='Apple Iphone 16 Pro White', price=137900, description='Смартфон компании Apple, OLED, 6.9 дюйма, 2622х1206 пикселей, 120 Гц, 8ГБ/1ТБ, Apple A18 Pro, 6 ядер, 48МП/48МП/12МП, 3582 мАч', image='Iphone16Pro.webp'),
                Product(name='Apple Iphone 16 Deep Blue', price=112716, description='Смартфон восемнадцатого поколения от компании Apple, OLED, 6.1 дюйма, 2556х1179 пикселей, 60 Гц, 8ГБ/512ГБ, Apple A18, 48МП/12МП, 3561 мАч', image='Iphone16.webp'),
                Product(name='Samsung Galaxy S25 Ultra', price=137999, description='Флагманский смартфон, который установит новые стандарты в мире технологий, Dynamic AMOLED 2X, 6.9 дюйма, 3120×1440 пикселей, 120 Гц, Qualcomm Snapdragon 8 Elite, 16ГБ/1ТБ, 200Мп/50Мп/50Мп/10Мп, 5000 мАч', image='samsunggalaxys25Ultra.jpg'),
                Product(name='Samsung Galaxy S25+', price=114999, description='Флагманская модель 2025 года с широким функционалом, Dynamic AMOLED 2X, 6.7 дюйма, 3120×1440 пикселей, 120 Гц, Qualcomm Snapdragon 8 Elite, 12ГБ/512ГБ, 4900 мАч, 50МП/10МП/12МП', image='samsunggalaxys25+.jpg'),
                Product(name='Samsung Galaxy S25', price=108500, description='Флагманская модель в лаконичном дизайне, Dynamic AMOLED 2X, 6.2 дюйма, 2340×1080 пикселей, 120 Гц, Qualcomm Snapdragon 8 Elite, 12ГБ/512ГБ, 50МП/12МП, 4000 мАч', image='samsunggalaxys25.webp'),
                Product(name='OnePlus 13', price=95999, description=' Смартфон на базе Android производства OnePlus, LTPO AMOLED, 6.82 дюйма, 1440×3168 пикселей, 120 Гц, Qualcomm Snapdragon 8 Elite, 24ГБ/1ТБ, 50Мп/50Мп/50Мп, 6000 мАч', image='OnePlus13.png'),
                Product(name='OnePlus 13R', price=70999, description='Смартфон среднего уровня, AMOLED, 6.78 дюйма, 1264×2780 пикселей, 120 Гц, Qualcomm Snapdragon 8 Gen3, 16ГБ/512ГБ,  50Мп/50Мп, 6000 мАч', image='OnePlus13R.jpg'),
                Product(name='OnePlus 13T', price=45600, description='Компактный флагман с высокой производительностью, 6.3 дюйма, 2700×1200 пикселей, 120 Гц, Qualcomm Snapdragon 8 Elite, 12ГБ/256ГБ, 50Мп/8Мп, 6200 мАч', image='OnePlus13T.jpg'),
                Product(name='Xiaomi Redmi Note 14 Pro+', price=42990, description='Смартфон в среднем сегменте с обтекаемым дизайном, AMOLED, 6.67 дюйма, 1220×2712 пикселей, 120 Гц, Qualcomm Snapdragon 7s Gen3, 12ГБ/256ГБ, 200Мп/8Мп/2Мп, 5110 мАч', image='XiaomiRedmiNote14Pro+.jpg'),
                Product(name='Xiaomi Redmi Note 14 Pro', price=37800, description='Смартфон среднего ценового сегмента, LTPO OLED, 6.67 дюйма, 2400×1080 пикселей, 120 Гц, MediaTek Helio G100-Ultra, 12ГБ/256ГБ, 200Мп/8Мп/2Мп, 5500 мАч', image='XiaomiRedmiNote14Pro.webp'),
                Product(name='Xiaomi Redmi Note 14', price=25900, description='Бюджетный смартфон с плоскими торцами, AMOLED, 6.67 дюйма, 1080×2400 пикселей, 120 Гц, MediaTek Helio G99-Ultra, 8ГБ/256ГБ, 108МП/2МП/2МП, 5500 мАч', image='XiaomiRedmiNote14.webp'),
                Product(name='Honor Magic 7 Pro', price=129999, description='Флагманский смартфон с топовыми характеристиками, LTPO OLED, 6.8 дюйма, 2800х1280 пикселей, 120 Гц, Qualcomm Snapdragon 8 Elite, 16ГБ/1ТБ, 50Мп/50Мп/50Мп, 5850 мАч', image='Honor_Magic7_Pro_3_5EixGon.webp'),
                Product(name='Honor 400 Pro', price=59000, description='Новейший смартфон с отличной камерой, AMOLED, 6.7 дюйма, 2800х1280 пикселей, 120 Гц, Qualcomm Snapdragon 8 Gen 3, 12ГБ/512ГБ, 200Мп/12Мп/50Мп, 5300 мАч,', image='Honor-300-Pro-2-600x600.webp'),
                Product(name='Honor Magic 6 Ultimate', price=68920, description='Флагманский смартфон с отличной камерой, OLED LTPO, 2800×1280 пикселей, 120 Гц, Qualcomm Snapdragon 8 Gen 3, 16ГБ/512ГБ, 50МП/180МП/50МП, 5600 мАч', image='HonorMagic6Ultimate.webp')
            ]
            db.session.bulk_save_objects(products)
            db.session.commit()
    
    app.run(debug=True)

    