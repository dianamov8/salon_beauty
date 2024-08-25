import sqlite3

conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#              id INTEGER PRIMARY KEY AUTOINCREMENT,
#              first_name TEXT NOT NULL,
#              email TEXT NOT NULL,
#              phone_num TEXT NOT NULL
#              )''')
# conn.commit()
# conn.close()

# cursor.execute('''CREATE TABLE shop(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 img TEXT NOT NULL,
#                 title TEXT NOT NULL,
#                 desc TEXT NOT NULL,
#                 price REAL NOT NULL
#                 )''')
#
# conn.commit()
# conn.close()

# cursor.execute('''CREATE TABLE cart(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 img TEXT NOT NULL,
#                 title TEXT NOT NULL,
#                 desc TEXT NOT NULL,
#                 price REAL NOT NULL
#                 )''')
#
# conn.commit()
# conn.close()
#
# cursor.execute('''CREATE TABLE users_order(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT NOT NULL,
#                 email TEXT NOT NULL,
#                 address REAL NOT NULL
#                 )''')

# cursor.execute('''CREATE TABLE IF NOT EXISTS main_services (
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        name TEXT NOT NULL,
#        description TEXT NOT NULL,
#        image TEXT NOT NULL
#         )''')

# conn.commit()
# conn.close()

# cursor.execute('''CREATE TABLE IF NOT EXISTS sub_services (
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        main_service_id INTEGER,
#        name TEXT NOT NULL,
#        description TEXT NOT NULL,
#        image TEXT NOT NULL,
#        price REAL NOT NULL,
#        FOREIGN KEY (main_service_id) REFERENCES main_services(id)
#        )''')

# conn.commit()
# conn.close()

# conn.commit()
# conn.close()

def add_product(img, title, desc, price):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO shop(img, title, desc, price) 
            VALUES (?,?,?,?)''', (img, title, desc, price))
    conn.commit()
    conn.close()

# add_product("https://kashalot.gift/image/cachewebp/catalog/For-her/Tiramisu-spa-ua/premium-600x600.webp","Spa box","Подарунковий бокс - набір косметики для догляду за шкірою","1200")

# add_product("https://urepia.ismcdn.jp/mwimgs/8/2/640m/img_82553d0fb72f67bd250bd8a1351af12d447250.jpg","Shover box","Подарунковий бокс - набір для догляду за волоссям","900")

# add_product("https://images.uncommongoods.com/images/items/56600/56697_3_640px.jpg","Body oils box","Подарунковий бокс - набір олій та масел для догляду за тілом","1500")

# add_product("https://aroma.com.ua/content/images/25/51684530_small5.jpg","Aroma oils box","Подарунковий бокс - набір аромамасел для створення атмосфери релаксації у вас дома","600")

# add_product("https://th.bing.com/th/id/OIP.Eynn4zdhr6p5ZipYlU7wyAHaHa?rs=1&pid=ImgDetMain","Makeup brush box","Подарунковий бокс - набір кистей для макіяжу","1000")

# add_product("https://penelopessoapsandsuch.com/wp-content/uploads/2023/08/Untitled-1-1280x1280.jpg","Bath box","Подарунковий бокс - набір пінки та солі для ванни","1200")

# add_product("https://www.countryhillcottage.com/wp-content/uploads/2019/06/How_to_make_a_self_care_package-01-1-500x500-cropped.jpg","Skin care box","Подарунковий бокс - набір для догляду за чистотою вашої шкіри","900")

# add_product("https://www.nathnennia.com.ua/wp-content/uploads/nabir-tasty-care-1-1.jpg","Body care box","Подарунковий бокс - набір для догляду за вашою шкірою з натуральних інгредієнтів","700")

# add_product("https://i.etsystatic.com/10214619/r/il/ab681a/5983514977/il_640xN.5983514977_489o.jpg","Spa box","Подарунковий бокс - набір всього, що вам потрібно для створення справжнього спа у вас дома","1400")

# add_product("https://i.etsystatic.com/17038291/r/il/4a1762/2932485936/il_fullxfull.2932485936_ried.jpg","Body care box","Подарунковий бокс - набір для догляду за шкірою вашого тіла","1300")

# add_product("https://i.pinimg.com/originals/e0/c5/a6/e0c5a662a92f5563a2658fcab162d2d7.jpg","Make up box","Подарунковий бокс - набір косметики для обличчя преміальної якості","1800")

# add_product("https://www.stylebysavina.com/wp-content/uploads/2022/02/best-beauty-gifts-for-her-1024x1024.jpg","Soup box","Подарунковий бокс - набір мил зроблених виключно з натуральних елементів","1000")

# cursor.execute('''DELETE FROM shop''')
# conn.commit()
# conn.close()


def delete_product(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM shop WHERE id=?''', (id,))
    conn.commit()
    conn.close()


def get_product_from_shop(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    good = cursor.execute('''SELECT * FROM shop WHERE id=?''', (id,)).fetchone()
    conn.close()
    return good

def add_to_cart(img, title, desc, price):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO cart(img, title, desc, price) 
            VALUES (?,?,?,?)''', (img, title, desc, price))
    conn.commit()
    conn.close()

def delete_product_from_cart(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM cart WHERE id=?''', (id,))
    conn.commit()
    conn.close()

def get_products_from_cart():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    goods = cursor.execute('''SELECT * FROM cart''').fetchall()
    conn.close()
    return goods

def add_users_order(name,email,address):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO users_order(name,email,address)
                    VALUES(?,?,?)""", (name,email,address))
    conn.commit()
    conn.close()


def add_services():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO main_services (name, description, image) VALUES (?, ?, ?)",
                   ('Волосся', 'У нашому салоні можна отримати повний спектр послуг для догляду за волоссям. Ми пропонуємо професійні стрижки, які підкреслять ваш індивідуальний стиль, а також сучасні техніки фарбування, що додадуть вашому образу яскравості та свіжості. Наші майстри допоможуть вам відновити здоровʼя та блиск волосся за допомогою спеціальних процедур догляду, включаючи відновлення пошкодженого волосся, зволоження та живлення. Також у нас доступна послуга нарощування волосся, яка дозволить вам насолоджуватися довгими та густими пасмами. Ми використовуємо лише якісні засоби та новітні техніки, щоб ваше волосся виглядало бездоганно', 'https://p-de-p.com/wp-content/uploads/2023/07/hairdressing-services-cover.jpg'))
    cursor.execute("INSERT INTO main_services (name, description, image) VALUES (?, ?, ?)",
                   ('Косметологія', 'Наш салон пропонує широкий спектр косметологічних послуг для дбайливого догляду за вашою шкірою. Наші професійні косметологи допоможуть вам досягти здорового та сяючого вигляду шкіри завдяки індивідуально підібраним процедурам. Ми пропонуємо глибоке очищення, яке ефективно видаляє забруднення та відновлює природний баланс шкіри, а також зволожуючі та живильні маски, що повертають шкірі свіжість і еластичність. Крім того, у нас доступні антивікові процедури, спрямовані на зменшення зморшок і підвищення пружності шкіри. Використовуючи новітні технології та якісні засоби, ми гарантуємо вам помітний результат і абсолютний комфорт під час кожної процедури.', 'https://savanna.in.ua/wp-content/uploads/2019/02/piling-ivano-frankivsk-salon-krasy-savanna.jpg'))
    cursor.execute("INSERT INTO main_services (name, description, image) VALUES (?, ?, ?)",
                   ('Манікюр та педікюр', 'Наші майстри манікюру та педикюру забезпечать вашим нігтям догляд, який вони заслуговують. Ми пропонуємо широкий вибір послуг, починаючи від класичного обрізного манікюру та педикюру до сучасних технік нарощування та покриття гель-лаком. Наші спеціалісти дбайливо підберуть для вас індивідуальний дизайн, враховуючи ваші побажання та стиль. Також ми пропонуємо SPA-процедури для рук і ніг, які включають зволоження, масаж та пілінг, що допоможуть відновити шкіру та подарують відчуття свіжості і релаксу. Завдяки використанню високоякісних засобів та стерильних інструментів, ми гарантуємо вам бездоганний результат і максимальний комфорт під час кожної процедури.', 'https://i-visti.com/uploads/posts/2018-10/1538985665_05.jpg'))
    cursor.execute("INSERT INTO main_services (name, description, image) VALUES (?, ?, ?)",
                   ('Макіяж', 'У нашому салоні ви також можете скористатися послугами професійного макіяжу, який підкреслить вашу природну красу та створить ідеальний образ для будь-якої події. Наші візажисти майстерно виконують різні види макіяжу, від легкого денного до яскравого вечірнього, а також спеціалізуються на весільному макіяжі, який забезпечить вам бездоганний вигляд протягом усього святкового дня. Ми використовуємо тільки високоякісну косметику, яка підходить для будь-якого типу шкіри і забезпечує стійкість макіяжу. Завітайте до нас, і наші майстри допоможуть вам відчути себе впевненою та чарівною у будь-якій ситуації.', 'https://img.freepik.com/fotos-gratis/maquiador-aplicando-sombra-no-rosto_23-2148332526.jpg'))
    # cursor.execute("INSERT INTO sub_services (main_service_id, name, description, image, price) VALUES (?, ?, ?, ?, ?)",
    #                (1, 'Стрижка', 'У нашому салоні стрижка — це мистецтво, яке підкреслює ваш стиль. Наші майстри створюють зачіски, що ідеально підходять вам, з урахуванням ваших побажань. Якість і професіоналізм гарантовані.', 'https://alexandraandreeva.ua/wp-content/uploads/2019/12/69519320_2950975335126706_229925129956622336_n.jpg', 700))
    # cursor.execute("INSERT INTO sub_services (main_service_id, name, description, image, price) VALUES (?, ?, ?, ?, ?)",
    #                (1, 'Фарбування', 'Наш салон пропонує професійне фарбування волосся, яке підкреслить вашу індивідуальність і додасть яскравості вашому образу. Ми використовуємо тільки якісні барвники, що забезпечують стійкий колір і здоровий вигляд волосся. Довіртеся нашим майстрам, і ваше волосся засяє новими фарбами!', 'https://wona.com.ua/wp-content/uploads/2021/11/farbuvannia-volossia-u-dva-kolory-10.jpeg', 4900))
    # cursor.execute("INSERT INTO sub_services (main_service_id, name, description, image, price) VALUES (?, ?, ?, ?, ?)",
    #                (1, 'Догляд', 'У нашому салоні догляд за волоссям — це комплекс процедур, які відновлюють здоровʼя і блиск вашого волосся. Ми використовуємо тільки перевірені засоби та індивідуальні підходи, щоб ваше волосся виглядало доглянутим, міцним і шовковистим.', 'https://st3.depositphotos.com/12039412/16352/i/450/depositphotos_163528226-stock-photo-woman-having-hair-wash.jpg', 1100))
    # cursor.execute("INSERT INTO sub_services (main_service_id, name, description, image, price) VALUES (?, ?, ?, ?, ?)",
    #                (1, 'Укладка','У нашому салоні ми створюємо укладки, які підкреслюють вашу індивідуальність та зберігають стійкість протягом усього дня. Наші майстри вміло працюють з будь-яким типом волосся, надаючи йому форму і обʼєм, що підходять саме вам. Довірте нам своє волосся, і ваша укладка буде бездоганною!',
    #                 'https://zmina.in.ua/wp-content/webp-express/webp-images/uploads/2022/08/ukladka1-470x500.jpg.webp',
    #                 600))
    # cursor.execute("INSERT INTO sub_services (main_service_id, name, description, image, price) VALUES (?, ?, ?, ?, ?)",
    #                (2, 'Чистка обличчя',
    #                 'Наш салон пропонує професійну чистку обличчя, яка глибоко очищає шкіру, повертаючи їй свіжість та природний блиск. Наші майстри використовують лише безпечні методи та якісні засоби, щоб ваша шкіра залишалася здоровою і сяючою. Довіртеся нам, і ваше обличчя засяє новою красою!',
    #                 'https://savanna.in.ua/wp-content/uploads/2019/02/kosmetolog-chystka-oblychchya-salon-krasy-savanna-800x500.jpg',
    #                 2500))
    # cursor.execute("INSERT INTO sub_services (main_service_id, name, description, image, price) VALUES (?, ?, ?, ?, ?)",
    #                (2, 'Массаж обличчя',
    #                 'У нашому салоні масаж обличчя — це мистецтво розслаблення та омолодження. Наші професіонали використовують спеціальні техніки, щоб ваша шкіра стала пружною, сяючою та виглядала молодшою. Подаруйте своєму обличчю турботу, на яку воно заслуговує!',
    #                 'https://formula-tila.com.ua/public/uploads/categories/img1/massazh-litsa-img1.jpg', 400))
    # cursor.execute("INSERT INTO sub_services (main_service_id, name, description, image, price) VALUES (?, ?, ?, ?, ?)",
    #                (2, 'Інʼєкції',
    #                 'Наш салон пропонує інʼєкції для обличчя, які ефективно розгладжують зморшки та відновлюють пружність шкіри. Ми використовуємо безпечні, сучасні методи, щоб підкреслити вашу природну красу. Довіртеся нашим спеціалістам, і ваше обличчя засяє молодістю та свіжістю!',
    #                 'https://aichan-clinic.com/wp-content/uploads/2024/02/3e048d7c952142a236728a52e67d4253.jpg',
    #                 250))
    # cursor.execute("INSERT INTO sub_services (main_service_id, name, description, image, price) VALUES (?, ?, ?, ?, ?)",
    #                (3, 'Манікюр',
    #                 'Наш салон пропонує манікюр, який забезпечує здоровʼя і доглянутий вигляд ваших нігтів. Наші майстри дбайливо працюють з вашими руками, створюючи бездоганний результат. Довіртеся нам, і ваші нігті будуть в ідеальному стані!',                                                'https://mb.web.sapo.io/bac677f1b07aa93261936ccd14726066095e99f9.jpg',
    #                 400))
    # cursor.execute("INSERT INTO sub_services (main_service_id, name, description, image, price) VALUES (?, ?, ?, ?, ?)",
    #                (3, 'Нарощування',
    #                 'У нашому салоні нарощення нігтів перетворюється на мистецтво. Ми використовуємо тільки якісні матеріали, щоб створити ідеальну форму і довжину, яка підкреслить вашу індивідуальність.У ціну входить зняття гель лаку, нарощеня та нове покриття . Довіртеся нашим спеціалістам, і ваші нігті стануть справжньою прикрасою рук!',
    #                 'https://i.pinimg.com/736x/29/90/a7/2990a74a5636eec57c0c30ad9b251940.jpg',
    #                 2500))
    # cursor.execute("INSERT INTO sub_services (main_service_id, name, description, image, price) VALUES (?, ?, ?, ?, ?)",
    #                (3, 'Педикюр',
    #                 'Наш салон пропонує педикюр, який перетворює ваші ноги на витвір мистецтва. Ми дбайливо доглядаємо за вашими ступнями, забезпечуючи їм бездоганний вигляд і комфорт. Подаруйте своїм ногам розкішний догляд, на який вони заслуговують!',
    #                 'https://i.pinimg.com/originals/b8/70/a9/b870a9d43b24306e9c3f4ce9bb982b4e.jpg',
    #                 400))
    # cursor.execute("INSERT INTO sub_services (main_service_id, name, description, image, price) VALUES (?, ?, ?, ?, ?)",
    #                (4, 'Макіяж',
    #                 'Наш салон пропонує макіяж, який підкреслює вашу природну красу і підходить до будь-якої події. Ми створюємо індивідуальний образ, який забезпечить вам бездоганний вигляд і впевненість у кожному моменті. Подаруйте собі вражаючий вигляд з нашими професійними послугами!',
    #                 'https://harfetaze.com/wp-content/uploads/2022/01/Bridal-makeup-10.jpg',
    #                 1500))
    # cursor.execute("INSERT INTO sub_services (main_service_id, name, description, image, price) VALUES (?, ?, ?, ?, ?)",
    #                (4, 'Татуаж',
    #                 'аш салон пропонує татуаж, який підкреслить вашу індивідуальність і створить бездоганний вигляд без зайвих зусиль. Ми використовуємо сучасні техніки та якісні пігменти, щоб забезпечити вам стильний і тривалий результат. Довіртеся нам, і ваші брови, губи або повіки завжди виглядатимуть бездоганно!',
    #                 'https://th.bing.com/th/id/R.87c7a99c0a5d1b08e350645471d679e6?rik=fR1S%2beklH4vpqg&riu=http%3a%2f%2fblushbar.com.au%2fcdn%2fshop%2farticles%2fbrow_lamination.jpg%3fv%3d1664154026&ehk=EiE%2b60YV0iD3edMG32xl9r%2f4oM8FaoB4F1YNeOvD0JE%3d&risl=&pid=ImgRaw&r=0',
    #                 7500))
    # cursor.execute("INSERT INTO sub_services (main_service_id, name, description, image, price) VALUES (?, ?, ?, ?, ?)",
    #                (4, 'Нарощення Вій',
    #                 'У нашому салоні нарощення вій — це шлях до виразного погляду і ідеальних вій. Ми використовуємо тільки високоякісні матеріали, щоб забезпечити натуральний вигляд і тривалу стійкість. Подаруйте своїм очам розкішний обʼєм і довжину з нашими професійними послугами!',
    #                 'https://images.prom.ua/3812534467_w600_h600_3812534467.jpg',
    #                 3300))

    conn.commit()
    conn.close()

# add_services()

# cursor.execute("""DROP TABLE main_services""")
# conn.commit()
# conn.close()

# cursor.execute("""DELETE FROM sub_services;""")
# conn.commit()
# conn.close()

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# cursor.execute('''
#    CREATE TABLE IF NOT EXISTS appointments (
#        id INTEGER PRIMARY KEY AUTOINCREMENT,
#        sub_service_id INTEGER,
#        user_id INTEGER,
#        appointment_datetime TEXT,
#        master_name TEXT,
#        FOREIGN KEY (sub_service_id) REFERENCES sub_services(id),
#        FOREIGN KEY (user_id) REFERENCES users(id)
#    )
#    ''')

masters = ['Анастасія','Марина','Христина','Олена','Катерина','Марія','Вікторія','Тетяна','Валерія','Анна']