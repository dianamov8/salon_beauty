from database import *
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mail import Mail, Message
import os
import random
# from secret import *

app = Flask(__name__)
app.secret_key = '1234567899'

app.config['MAIL_SERVER'] = 'smtp.ukr.net'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'movcanukdiana@ukr.net'
app.config['MAIL_PASSWORD'] = 'GNOEEBfeLBSJAAQI'
app.config['MAIL_DEFAULT_SENDER'] = 'movcanukdiana@ukr.net'

mail = Mail(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/r/', methods=['POST', 'GET'])
def rgstrtn():
    if request.method == 'POST':
        first_name = request.form['first_name']
        email = request.form['email']
        phone_num = request.form['phone_num']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute("INSERT INTO users (first_name, email, phone_num) VALUES (?, ?, ?)",(first_name, email, phone_num))
        conn.commit()
        conn.close()
        return redirect('/')
    else:
        return render_template('rgstr.html')

@app.route("/shop/")
def shop():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    goods = cursor.execute("""SELECT * FROM shop""").fetchall()
    conn.close()
    return render_template('shop.html', goods=goods)

@app.route("/<int:id>/",methods=["POST","GET"])
def one_product(id):
    good = get_product_from_shop(id)
    if request.method == "POST":
        add_to_cart(good[1],good[2],good[3],good[4])
        return redirect("/cart/")
    if good:
        return render_template("one.html",good=good)
    else:
        return f"<h1> Товар не знайдено :( </h1>"


@app.route('/cart/',methods=["POST","GET"])
def cart():
    goods = get_products_from_cart()
    return render_template("cart.html", goods=goods)

@app.route("/delete/<int:id>/", methods=["POST"])
def delete_from_cart(id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM cart WHERE id=?''', (id,))
    conn.commit()
    conn.close()
    return redirect("/cart/")

@app.route("/form/<int:id>/", methods=["POST","GET"])
def form(id):
    if request.method == "POST":
        return render_template('form.html', id=id)

@app.route("/form_order/<int:id>/", methods=["POST","GET"])
def form_order(id):
    if request.method == "POST":
        name = request.form['name']
        email = request.form["email"]
        address = request.form["address"]
        add_users_order(name,email,address)
        delete_product_from_cart(id)
        return redirect("/cart/")
    return render_template('form.html')

@app.route("/services/")
def services():
    conn = get_db_connection()
    main_services = conn.execute('SELECT * FROM main_services').fetchall()
    conn.close()
    return render_template('services.html', main_services=main_services)

@app.route('/services/<int:service_id>')
def service(service_id):
    conn = get_db_connection()
    main_service = conn.execute('SELECT * FROM main_services WHERE id = ?', (service_id,)).fetchone()
    sub_services = conn.execute('SELECT * FROM sub_services WHERE main_service_id = ?', (service_id,)).fetchall()
    conn.close()
    return render_template('one_service.html', main_service=main_service, sub_services=sub_services,service=service)


@app.route('/book/<int:sub_service_id>', methods=['GET', 'POST'])
def book(sub_service_id):
    conn = get_db_connection()
    sub_service = conn.execute('SELECT * FROM sub_services WHERE id = ?', (sub_service_id,)).fetchone()

    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        date_time = request.form['date_time']

        user = conn.execute('SELECT * FROM users WHERE first_name = ? AND phone_num = ?', (name, phone)).fetchone()


        if user:
            to_email = user['email']
            subject = "Підтвердження запису на послугу"
            body = f"Дякуємо за запис на {sub_service['name']}! Майстер: Майстер {random.choice(masters)}, Дата та час: {date_time}"

            msg = Message(subject, recipients=[to_email])
            msg.body = body

            try:
                mail.send(msg)
                flash('Запис успішно створено та підтвердження відправлено на вашу електронну адресу!')
            except Exception as e:
                flash(f'Помилка при відправці листа: {e}')
        else:
            flash('Користувач не знайдений або введені дані неправильні.')

        conn.close()
        return redirect(url_for('index'))

    return render_template('book.html', sub_service=sub_service)



if __name__ == '__main__':
    app.run(debug=True)