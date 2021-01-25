import hashlib, binascii, os
import datetime

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///konsultantai.db")

@app.route("/")
@login_required
def index():
    return render_template("/index.html")

@app.route("/index_k")
@login_required
def index_k():
    return render_template("/index_k.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    # pamiršti vartotojo ID
    session.clear()

    error = None;

    if request.method == "POST":

    # užtikrinti, kad nurodytas vartotojo vardas
        if not request.form.get("username"):
            return apology("Nenurodytas vartotojo vardas")

    # užtiktinti, kad nurodytas slaptažodis
        elif not request.form.get("password"):
            return apology("Nenurodytas slaptažodis")

    # tikrinti vardą duomenų bazėje
        rows = db.execute("SELECT * FROM vartotojai WHERE username = :username",username=request.form.get("username"))

    # tikrinti, ar egzistuoja vartotojas bei tikrinti slaptažodį
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash("Neteisingas vartotojo vardas arba slaptažodis!")
            return redirect("/prisijungti")

    # prisiminti, kuris vartotojas prisijungė

        session["user_id"] = rows[0]["id"]
        session["user_type"] = rows[0]["type"]
        return redirect("/")

    else:
        return render_template("prisijungti.html")


@app.route("/logout")
def logout():
    """Log user out"""

    #Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/rezervacija1", methods=["GET", "POST"])
@login_required
def rezervacija1():
    if request.method=="GET":
        now = datetime.now()
        now_year = now.year
        now_month = now.month

        kab1_rows_1 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 1", now_year, now_month)
        kab1_rows_2 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 2", now_year, now_month)
        kab1_rows_3 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 3", now_year, now_month)
        kab1_rows_4 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 4", now_year, now_month)
        kab1_rows_5 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 5", now_year, now_month)
        kab1_rows_6 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 6", now_year, now_month)
        kab1_rows_7 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 7", now_year, now_month)
        kab1_rows_8 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 8", now_year, now_month)
        kab1_rows_9 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 9", now_year, now_month)
        kab1_rows_10 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 10", now_year, now_month)
        kab1_rows_11 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 11", now_year, now_month)
        kab1_rows_12 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 12", now_year, now_month)
        kab1_rows_13 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 13", now_year, now_month)
        kab1_rows_14 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 14", now_year, now_month)
        kab1_rows_15 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 15", now_year, now_month)
        kab1_rows_16 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 16", now_year, now_month)
        kab1_rows_17 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 17", now_year, now_month)
        kab1_rows_18 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 18", now_year, now_month)
        kab1_rows_19 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 19", now_year, now_month)
        kab1_rows_20 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 20", now_year, now_month)
        kab1_rows_21 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 21", now_year, now_month)
        kab1_rows_22 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 22", now_year, now_month)
        kab1_rows_23 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 23", now_year, now_month)
        kab1_rows_24 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 24", now_year, now_month)
        kab1_rows_25 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 25", now_year, now_month)
        kab1_rows_26 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 26", now_year, now_month)
        kab1_rows_27 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 27", now_year, now_month)
        kab1_rows_28 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 28", now_year, now_month)
        kab1_rows_29 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 29", now_year, now_month)
        kab1_rows_30 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 30", now_year, now_month)
        kab1_rows_31 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 31", now_year, now_month)

        return render_template("/rezervacija1.html", now_year=now_year, now_month=now_month, kab1_rows_1=kab1_rows_1, kab1_rows_2=kab1_rows_2, kab1_rows_3=kab1_rows_3, kab1_rows_4=kab1_rows_4, kab1_rows_5=kab1_rows_5, kab1_rows_6=kab1_rows_6, kab1_rows_7=kab1_rows_7, kab1_rows_8=kab1_rows_8, kab1_rows_9=kab1_rows_9, kab1_rows_10=kab1_rows_10, kab1_rows_11=kab1_rows_11, kab1_rows_12=kab1_rows_12, kab1_rows_13=kab1_rows_13, kab1_rows_14=kab1_rows_14, kab1_rows_15=kab1_rows_15, kab1_rows_16=kab1_rows_16, kab1_rows_17=kab1_rows_17, kab1_rows_18=kab1_rows_18, kab1_rows_19=kab1_rows_19, kab1_rows_20=kab1_rows_20, kab1_rows_21=kab1_rows_21, kab1_rows_22=kab1_rows_22, kab1_rows_23=kab1_rows_23, kab1_rows_24=kab1_rows_24, kab1_rows_25=kab1_rows_25, kab1_rows_26=kab1_rows_26, kab1_rows_27=kab1_rows_27, kab1_rows_28=kab1_rows_28, kab1_rows_29=kab1_rows_29, kab1_rows_30=kab1_rows_30, kab1_rows_31=kab1_rows_31)

    if request.method=="POST":
        now = datetime.now()
        now_year = now.year
        now_month = now.month
        rezervuota = "Rezervuota"

        booked_time = request.form.get("time_kab1_1")
        booked_client = request.form.get("client_1")
        booked_day = 1
        if not request.form.get("time_kab1_1"):
            booked_time = request.form.get("time_kab1_2")
            booked_client = request.form.get("client_2")
            booked_day = 2
            if not request.form.get("time_kab1_2"):
                booked_time = request.form.get("time_kab1_3")
                booked_client = request.form.get("client_3")
                booked_day = 3
                if not request.form.get("time_kab1_3"):
                    booked_time = request.form.get("time_kab1_4")
                    booked_client = request.form.get("client_4")
                    booked_day = 4
                    if not request.form.get("time_kab1_4"):
                        booked_time = request.form.get("time_kab1_5")
                        booked_client = request.form.get("client_5")
                        booked_day = 5
                        if not request.form.get("time_kab1_5"):
                            booked_time = request.form.get("time_kab1_6")
                            booked_client = request.form.get("client_6")
                            booked_day = 6
                            if not request.form.get("time_kab1_6"):
                                booked_time = request.form.get("time_kab1_7")
                                booked_client = request.form.get("client_7")
                                booked_day = 7
                                if not request.form.get("time_kab1_7"):
                                    booked_time = request.form.get("time_kab1_8")
                                    booked_client = request.form.get("client_8")
                                    booked_day = 8
                                    if not request.form.get("time_kab1_8"):
                                        booked_time = request.form.get("time_kab1_9")
                                        booked_client = request.form.get("client_9")
                                        booked_day = 9
                                        if not request.form.get("time_kab1_9"):
                                            booked_time = request.form.get("time_kab1_10")
                                            booked_client = request.form.get("client10")
                                            booked_day = 10
                                            if not request.form.get("time_kab1_10"):
                                                booked_time = request.form.get("time_kab1_11")
                                                booked_client = request.form.get("client_11")
                                                booked_day = 11
                                                if not request.form.get("time_kab1_11"):
                                                    booked_time = request.form.get("time_kab1_12")
                                                    booked_client = request.form.get("client_12")
                                                    booked_day = 12
                                                    if not request.form.get("time_kab1_12"):
                                                        booked_time = request.form.get("time_kab1_13")
                                                        booked_client = request.form.get("client_13")
                                                        booked_day = 13
                                                        if not request.form.get("time_kab1_13"):
                                                            booked_time = request.form.get("time_kab1_14")
                                                            booked_client = request.form.get("client_14")
                                                            booked_day = 14
                                                            if not request.form.get("time_kab1_14"):
                                                                booked_time = request.form.get("time_kab1_15")
                                                                booked_client = request.form.get("client_15")
                                                                booked_day = 15
                                                                if not request.form.get("time_kab1_15"):
                                                                    booked_time = request.form.get("time_kab1_16")
                                                                    booked_client = request.form.get("client_16")
                                                                    booked_day = 16
                                                                    if not request.form.get("time_kab1_17"):
                                                                        booked_time = request.form.get("time_kab1_17")
                                                                        booked_client = request.form.get("client_17")
                                                                        booked_day = 17
                                                                        if not request.form.get("time_kab1_18"):
                                                                            booked_time = request.form.get("time_kab1_18")
                                                                            booked_client = request.form.get("client_18")
                                                                            booked_day = 18
                                                                            if not request.form.get("time_kab1_18"):
                                                                                booked_time = request.form.get("time_kab1_19")
                                                                                booked_client = request.form.get("client_19")
                                                                                booked_day = 19
                                                                                if not request.form.get("time_kab1_19"):
                                                                                    booked_time = request.form.get("time_kab1_20")
                                                                                    booked_client = request.form.get("client_20")
                                                                                    booked_day = 20
                                                                                    if not request.form.get("time_kab1_20"):
                                                                                        booked_time = request.form.get("time_kab1_21")
                                                                                        booked_client = request.form.get("client_21")
                                                                                        booked_day = 21
                                                                                        if not request.form.get("time_kab1_21"):
                                                                                            booked_time = request.form.get("time_kab1_22")
                                                                                            booked_client = request.form.get("client_22")
                                                                                            booked_day = 22
                                                                                            if not request.form.get("time_kab1_22"):
                                                                                                booked_time = request.form.get("time_kab1_23")
                                                                                                booked_client = request.form.get("client_23")
                                                                                                booked_day = 23
                                                                                                if not request.form.get("time_kab1_23"):
                                                                                                    booked_time = request.form.get("time_kab1_24")
                                                                                                    booked_client = request.form.get("client_24")
                                                                                                    booked_day = 24
                                                                                                    if not request.form.get("time_kab1_24"):
                                                                                                        booked_time = request.form.get("time_kab1_25")
                                                                                                        booked_client = request.form.get("client_25")
                                                                                                        booked_day = 25
                                                                                                        if not request.form.get("time_kab1_25"):
                                                                                                            booked_time = request.form.get("time_kab1_26")
                                                                                                            booked_client = request.form.get("client_26")
                                                                                                            booked_day = 26
                                                                                                            if not request.form.get("time_kab1_26"):
                                                                                                                booked_time = request.form.get("time_kab1_27")
                                                                                                                booked_client = request.form.get("client_27")
                                                                                                                booked_day = 27
                                                                                                                if not request.form.get("time_kab1_27"):
                                                                                                                    booked_time = request.form.get("time_kab1_28")
                                                                                                                    booked_client = request.form.get("client_28")
                                                                                                                    booked_day = 28
                                                                                                                    if not request.form.get("time_kab1_28"):
                                                                                                                        booked_time = request.form.get("time_kab1_29")
                                                                                                                        booked_client = request.form.get("client_29")
                                                                                                                        booked_day = 29
                                                                                                                        if not request.form.get("time_kab1_29"):
                                                                                                                            booked_time = request.form.get("time_kab1_30")
                                                                                                                            booked_client = request.form.get("client_30")
                                                                                                                            booked_day = 30
                                                                                                                            if not request.form.get("time_kab1_30"):
                                                                                                                                booked_time = request.form.get("time_kab1_31")
                                                                                                                                booked_client = request.form.get("client_31")
                                                                                                                                booked_day = 31
                                                                                                                                if not request.form.get("time_kab1_31"):
                                                                                                                                    return apology("nepasirinktas laikas")


        if booked_time == "09:00":
            booked_time = "09:00 - 10:00"

        if booked_time == "10:00":
            booked_time = "10:00 - 11:00"

        if booked_time == "11:00":
            booked_time = "11:00 - 12:00"

        if booked_time == "12:00":
            booked_time = "12:00 - 13:00"

        if booked_time == "13:00":
            booked_time = "13:00 - 14:00"

        if booked_time == "14:00":
            booked_time = "14:00 - 15:00"

        if booked_time == "15:00":
            booked_time = "15:00 - 16:00"

        if booked_time == "16:00":
            booked_time = "16:00 - 17:00"

        if booked_time == "17:00":
            booked_time = "17:00 - 18:00"

        rows = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND day = %s AND time = %s AND cabinet = 1", now_year, now_month, booked_day, booked_time)
        for row in rows:
            if row["booked"] == "Rezervuota":
                return apology ("Šis laikas jau rezervuotas")

        db.execute("UPDATE kalendorius SET user_id = %s, client = %s WHERE year = %s AND month = %s AND day = %s AND time = %s AND cabinet = 1", session["user_id"], booked_client, now_year, now_month, booked_day, booked_time)
        db.execute("UPDATE kalendorius SET booked = %s WHERE year = %s AND month = %s AND day = %s AND time = %s AND cabinet = 1", rezervuota, now_year, now_month, booked_day, booked_time)

        flash("Konsultacija užregistruota!")

        return render_template("/rezervacijos_patvirtinimas.html", booked_client=booked_client, booked_time=booked_time, booked_day=booked_day, now_year=now_year, now_month=now_month)

@app.route("/rezervacija1_next", methods=["GET", "POST"])
@login_required
def rezervacija1_next():
    if request.method=="GET":
        now = datetime.now()
        now_year = now.year
        now_month = now.month
        if now_month == 12:
            now_year = now_year + 1

        next_month = now_month + 1

        kab1_next_rows_1 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 1", now_year, next_month)
        kab1_next_rows_2 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 2", now_year, next_month)
        kab1_next_rows_3 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 3", now_year, next_month)
        kab1_next_rows_4 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 4", now_year, next_month)
        kab1_next_rows_5 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 5", now_year, next_month)
        kab1_next_rows_6 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 6", now_year, next_month)
        kab1_next_rows_7 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 7", now_year, next_month)
        kab1_next_rows_8 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 8", now_year, next_month)
        kab1_next_rows_9 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 9", now_year, next_month)
        kab1_next_rows_10 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 10", now_year, next_month)
        kab1_next_rows_11 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 11", now_year, next_month)
        kab1_next_rows_12 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 12", now_year, next_month)
        kab1_next_rows_13 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 13", now_year, next_month)
        kab1_next_rows_14 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 14", now_year, next_month)
        kab1_next_rows_15 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 15", now_year, next_month)
        kab1_next_rows_16 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 16", now_year, next_month)
        kab1_next_rows_17 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 17", now_year, next_month)
        kab1_next_rows_18 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 18", now_year, next_month)
        kab1_next_rows_19 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 19", now_year, next_month)
        kab1_next_rows_20 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 20", now_year, next_month)
        kab1_next_rows_21 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 21", now_year, next_month)
        kab1_next_rows_22 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 22", now_year, next_month)
        kab1_next_rows_23 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 23", now_year, next_month)
        kab1_next_rows_24 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 24", now_year, next_month)
        kab1_next_rows_25 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 25", now_year, next_month)
        kab1_next_rows_26 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 26", now_year, next_month)
        kab1_next_rows_27 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 27", now_year, next_month)
        kab1_next_rows_28 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 28", now_year, next_month)
        kab1_next_rows_29 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 29", now_year, next_month)
        kab1_next_rows_30 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 30", now_year, next_month)
        kab1_next_rows_31 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 1 AND day = 31", now_year, next_month)

        return render_template("/rezervacija1_next.html", now_year=now_year, next_month=next_month, kab1_next_rows_1=kab1_next_rows_1, kab1_next_rows_2=kab1_next_rows_2, kab1_next_rows_3=kab1_next_rows_3, kab1_next_rows_4=kab1_next_rows_4, kab1_next_rows_5=kab1_next_rows_5, kab1_next_rows_6=kab1_next_rows_6, kab1_next_rows_7=kab1_next_rows_7, kab1_next_rows_8=kab1_next_rows_8, kab1_next_rows_9=kab1_next_rows_9, kab1_next_rows_10=kab1_next_rows_10, kab1_next_rows_11=kab1_next_rows_11, kab1_next_rows_12=kab1_next_rows_12, kab1_next_rows_13=kab1_next_rows_13, kab1_next_rows_14=kab1_next_rows_14, kab1_next_rows_15=kab1_next_rows_15, kab1_next_rows_16=kab1_next_rows_16, kab1_next_rows_17=kab1_next_rows_17, kab1_next_rows_18=kab1_next_rows_18, kab1_next_rows_19=kab1_next_rows_19, kab1_next_rows_20=kab1_next_rows_20, kab1_next_rows_21=kab1_next_rows_21, kab1_next_rows_22=kab1_next_rows_22, kab1_next_rows_23=kab1_next_rows_23, kab1_next_rows_24=kab1_next_rows_24, kab1_next_rows_25=kab1_next_rows_25, kab1_next_rows_26=kab1_next_rows_26, kab1_next_rows_27=kab1_next_rows_27, kab1_next_rows_28=kab1_next_rows_28, kab1_next_rows_29=kab1_next_rows_29, kab1_next_rows_30=kab1_next_rows_30, kab1_next_rows_31=kab1_next_rows_31)

    if request.method=="POST":
        now = datetime.now()
        now_year = now.year
        now_month = now.month
        if now_month == 12:
            now_year = now_year + 1

        next_month = now_month + 1

        rezervuota = "Rezervuota"

        booked_time = request.form.get("time_kab1_next_1")
        booked_client = request.form.get("client_1")
        booked_day = 1
        if not request.form.get("time_kab1_next_1"):
            booked_time = request.form.get("time_kab1_next_2")
            booked_client = request.form.get("client_2")
            booked_day = 2
            if not request.form.get("time_kab1_next_2"):
                booked_time = request.form.get("time_kab1_next_3")
                booked_client = request.form.get("client_3")
                booked_day = 3
                if not request.form.get("time_kab1_next_3"):
                    booked_time = request.form.get("time_kab1_next_4")
                    booked_client = request.form.get("client_4")
                    booked_day = 4
                    if not request.form.get("time_kab1_next_4"):
                        booked_time = request.form.get("time_kab1_next_5")
                        booked_client = request.form.get("client_5")
                        booked_day = 5
                        if not request.form.get("time_kab1_next_5"):
                            booked_time = request.form.get("time_kab1_next_6")
                            booked_client = request.form.get("client_6")
                            booked_day = 6
                            if not request.form.get("time_kab1_next_6"):
                                booked_time = request.form.get("time_kab1_next_7")
                                booked_client = request.form.get("client_7")
                                booked_day = 7
                                if not request.form.get("time_kab1_next_7"):
                                    booked_time = request.form.get("time_kab1_next_8")
                                    booked_client = request.form.get("client_8")
                                    booked_day = 8
                                    if not request.form.get("time_kab1_next_8"):
                                        booked_time = request.form.get("time_kab1_next_9")
                                        booked_client = request.form.get("client_9")
                                        booked_day = 9
                                        if not request.form.get("time_kab1_next_9"):
                                            booked_time = request.form.get("time_kab1_next_10")
                                            booked_client = request.form.get("client10")
                                            booked_day = 10
                                            if not request.form.get("time_kab1_next_10"):
                                                booked_time = request.form.get("time_kab1_next_11")
                                                booked_client = request.form.get("client_11")
                                                booked_day = 11
                                                if not request.form.get("time_kab1_next_11"):
                                                    booked_time = request.form.get("time_kab1_next_12")
                                                    booked_client = request.form.get("client_12")
                                                    booked_day = 12
                                                    if not request.form.get("time_kab1_next_12"):
                                                        booked_time = request.form.get("time_kab1_next_13")
                                                        booked_client = request.form.get("client_13")
                                                        booked_day = 13
                                                        if not request.form.get("time_kab1_next_13"):
                                                            booked_time = request.form.get("time_kab1_next_14")
                                                            booked_client = request.form.get("client_14")
                                                            booked_day = 14
                                                            if not request.form.get("time_kab1_next_14"):
                                                                booked_time = request.form.get("time_kab1_next_15")
                                                                booked_client = request.form.get("client_15")
                                                                booked_day = 15
                                                                if not request.form.get("time_kab1_next_15"):
                                                                    booked_time = request.form.get("time_kab1_next_16")
                                                                    booked_client = request.form.get("client_16")
                                                                    booked_day = 16
                                                                    if not request.form.get("time_kab1_next_17"):
                                                                        booked_time = request.form.get("time_kab1_next_17")
                                                                        booked_client = request.form.get("client_17")
                                                                        booked_day = 17
                                                                        if not request.form.get("time_kab1_next_18"):
                                                                            booked_time = request.form.get("time_kab1_next_18")
                                                                            booked_client = request.form.get("client_18")
                                                                            booked_day = 18
                                                                            if not request.form.get("time_kab1_next_18"):
                                                                                booked_time = request.form.get("time_kab1_next_19")
                                                                                booked_client = request.form.get("client_19")
                                                                                booked_day = 19
                                                                                if not request.form.get("time_kab1_next_19"):
                                                                                    booked_time = request.form.get("time_kab1_next_20")
                                                                                    booked_client = request.form.get("client_20")
                                                                                    booked_day = 20
                                                                                    if not request.form.get("time_kab1_next_20"):
                                                                                        booked_time = request.form.get("time_kab1_next_21")
                                                                                        booked_client = request.form.get("client_21")
                                                                                        booked_day = 21
                                                                                        if not request.form.get("time_kab1_next_21"):
                                                                                            booked_time = request.form.get("time_kab1_next_22")
                                                                                            booked_client = request.form.get("client_22")
                                                                                            booked_day = 22
                                                                                            if not request.form.get("time_kab1_next_22"):
                                                                                                booked_time = request.form.get("time_kab1_next_23")
                                                                                                booked_client = request.form.get("client_23")
                                                                                                booked_day = 23
                                                                                                if not request.form.get("time_kab1_next_23"):
                                                                                                    booked_time = request.form.get("time_kab1_next_24")
                                                                                                    booked_client = request.form.get("client_24")
                                                                                                    booked_day = 24
                                                                                                    if not request.form.get("time_kab1_next_24"):
                                                                                                        booked_time = request.form.get("time_kab1_next_25")
                                                                                                        booked_client = request.form.get("client_25")
                                                                                                        booked_day = 25
                                                                                                        if not request.form.get("time_kab1_next_25"):
                                                                                                            booked_time = request.form.get("time_kab1_next_26")
                                                                                                            booked_client = request.form.get("client_26")
                                                                                                            booked_day = 26
                                                                                                            if not request.form.get("time_kab1_next_26"):
                                                                                                                booked_time = request.form.get("time_kab1_next_27")
                                                                                                                booked_client = request.form.get("client_27")
                                                                                                                booked_day = 27
                                                                                                                if not request.form.get("time_kab1_next_27"):
                                                                                                                    booked_time = request.form.get("time_kab1_next_28")
                                                                                                                    booked_client = request.form.get("client_28")
                                                                                                                    booked_day = 28
                                                                                                                    if not request.form.get("time_kab1_next_28"):
                                                                                                                        booked_time = request.form.get("time_kab1_next_29")
                                                                                                                        booked_client = request.form.get("client_29")
                                                                                                                        booked_day = 29
                                                                                                                        if not request.form.get("time_kab1_next_29"):
                                                                                                                            booked_time = request.form.get("time_kab1_next_30")
                                                                                                                            booked_client = request.form.get("client_30")
                                                                                                                            booked_day = 30
                                                                                                                            if not request.form.get("time_kab1_next_30"):
                                                                                                                                booked_time = request.form.get("time_kab1_next_31")
                                                                                                                                booked_client = request.form.get("client_31")
                                                                                                                                booked_day = 31
                                                                                                                                if not request.form.get("time_kab1_next_31"):
                                                                                                                                    return apology("nepasirinktas laikas")


        if booked_time == "09:00":
            booked_time = "09:00 - 10:00"

        if booked_time == "10:00":
            booked_time = "10:00 - 11:00"

        if booked_time == "11:00":
            booked_time = "11:00 - 12:00"

        if booked_time == "12:00":
            booked_time = "12:00 - 13:00"

        if booked_time == "13:00":
            booked_time = "13:00 - 14:00"

        if booked_time == "14:00":
            booked_time = "14:00 - 15:00"

        if booked_time == "15:00":
            booked_time = "15:00 - 16:00"

        if booked_time == "16:00":
            booked_time = "16:00 - 17:00"

        if booked_time == "17:00":
            booked_time = "17:00 - 18:00"

        rows = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND day = %s AND time = %s AND cabinet = 1", now_year, next_month, booked_day, booked_time)
        for row in rows:
            if row["booked"] == "Rezervuota":
                return apology ("Šis laikas jau rezervuotas")

        db.execute("UPDATE kalendorius SET user_id = %s, client = %s WHERE year = %s AND month = %s AND day = %s AND time = %s AND cabinet = 1", session["user_id"], booked_client, now_year, next_month, booked_day, booked_time)
        db.execute("UPDATE kalendorius SET booked = %s WHERE year = %s AND month = %s AND day = %s AND time = %s AND cabinet = 1", rezervuota, now_year, next_month, booked_day, booked_time)

        flash("Konsultacija užregistruota!")

        return render_template("/rezervacijos_patvirtinimas.html", booked_client=booked_client, booked_time=booked_time, booked_day=booked_day, now_year=now_year, next_month=next_month)


@app.route("/rezervacija2", methods=["GET", "POST"])
@login_required
def rezervacija2():
    if request.method=="GET":
        now = datetime.now()
        now_year = now.year
        now_month = now.month

        kab2_rows_1 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 1", now_year, now_month)
        kab2_rows_2 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 2", now_year, now_month)
        kab2_rows_3 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 3", now_year, now_month)
        kab2_rows_4 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 4", now_year, now_month)
        kab2_rows_5 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 5", now_year, now_month)
        kab2_rows_6 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 6", now_year, now_month)
        kab2_rows_7 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 7", now_year, now_month)
        kab2_rows_8 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 8", now_year, now_month)
        kab2_rows_9 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 9", now_year, now_month)
        kab2_rows_10 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 10", now_year, now_month)
        kab2_rows_11 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 11", now_year, now_month)
        kab2_rows_12 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 12", now_year, now_month)
        kab2_rows_13 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 13", now_year, now_month)
        kab2_rows_14 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 14", now_year, now_month)
        kab2_rows_15 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 15", now_year, now_month)
        kab2_rows_16 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 16", now_year, now_month)
        kab2_rows_17 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 17", now_year, now_month)
        kab2_rows_18 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 18", now_year, now_month)
        kab2_rows_19 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 19", now_year, now_month)
        kab2_rows_20 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 20", now_year, now_month)
        kab2_rows_21 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 21", now_year, now_month)
        kab2_rows_22 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 22", now_year, now_month)
        kab2_rows_23 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 23", now_year, now_month)
        kab2_rows_24 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 24", now_year, now_month)
        kab2_rows_25 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 25", now_year, now_month)
        kab2_rows_26 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 26", now_year, now_month)
        kab2_rows_27 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 27", now_year, now_month)
        kab2_rows_28 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 28", now_year, now_month)
        kab2_rows_29 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 29", now_year, now_month)
        kab2_rows_30 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 30", now_year, now_month)
        kab2_rows_31 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 31", now_year, now_month)

        return render_template("/rezervacija2.html", now_year=now_year, now_month=now_month, kab2_rows_1=kab2_rows_1, kab2_rows_2=kab2_rows_2, kab2_rows_3=kab2_rows_3, kab2_rows_4=kab2_rows_4, kab2_rows_5=kab2_rows_5, kab2_rows_6=kab2_rows_6, kab2_rows_7=kab2_rows_7, kab2_rows_8=kab2_rows_8, kab2_rows_9=kab2_rows_9, kab2_rows_10=kab2_rows_10, kab2_rows_11=kab2_rows_11, kab2_rows_12=kab2_rows_12, kab2_rows_13=kab2_rows_13, kab2_rows_14=kab2_rows_14, kab2_rows_15=kab2_rows_15, kab2_rows_16=kab2_rows_16, kab2_rows_17=kab2_rows_17, kab2_rows_18=kab2_rows_18, kab2_rows_19=kab2_rows_19, kab2_rows_20=kab2_rows_20, kab2_rows_21=kab2_rows_21, kab2_rows_22=kab2_rows_22, kab2_rows_23=kab2_rows_23, kab2_rows_24=kab2_rows_24, kab2_rows_25=kab2_rows_25, kab2_rows_26=kab2_rows_26, kab2_rows_27=kab2_rows_27, kab2_rows_28=kab2_rows_28, kab2_rows_29=kab2_rows_29, kab2_rows_30=kab2_rows_30, kab2_rows_31=kab2_rows_31)

    if request.method=="POST":
        now = datetime.now()
        now_year = now.year
        now_month = now.month
        rezervuota = "Rezervuota"

        booked_time = request.form.get("time_kab2_1")
        booked_client = request.form.get("client_1")
        booked_day = 1
        if not request.form.get("time_kab2_1"):
            booked_time = request.form.get("time_kab2_2")
            booked_client = request.form.get("client_2")
            booked_day = 2
            if not request.form.get("time_kab2_2"):
                booked_time = request.form.get("time_kab2_3")
                booked_client = request.form.get("client_3")
                booked_day = 3
                if not request.form.get("time_kab2_3"):
                    booked_time = request.form.get("time_kab2_4")
                    booked_client = request.form.get("client_4")
                    booked_day = 4
                    if not request.form.get("time_kab2_4"):
                        booked_time = request.form.get("time_kab2_5")
                        booked_client = request.form.get("client_5")
                        booked_day = 5
                        if not request.form.get("time_kab2_5"):
                            booked_time = request.form.get("time_kab2_6")
                            booked_client = request.form.get("client_6")
                            booked_day = 6
                            if not request.form.get("time_kab2_6"):
                                booked_time = request.form.get("time_kab2_7")
                                booked_client = request.form.get("client_7")
                                booked_day = 7
                                if not request.form.get("time_kab2_7"):
                                    booked_time = request.form.get("time_kab2_8")
                                    booked_client = request.form.get("client_8")
                                    booked_day = 8
                                    if not request.form.get("time_kab2_8"):
                                        booked_time = request.form.get("time_kab2_9")
                                        booked_client = request.form.get("client_9")
                                        booked_day = 9
                                        if not request.form.get("time_kab2_9"):
                                            booked_time = request.form.get("time_kab2_10")
                                            booked_client = request.form.get("client10")
                                            booked_day = 10
                                            if not request.form.get("time_kab2_10"):
                                                booked_time = request.form.get("time_kab2_11")
                                                booked_client = request.form.get("client_11")
                                                booked_day = 11
                                                if not request.form.get("time_kab2_11"):
                                                    booked_time = request.form.get("time_kab2_12")
                                                    booked_client = request.form.get("client_12")
                                                    booked_day = 12
                                                    if not request.form.get("time_kab2_12"):
                                                        booked_time = request.form.get("time_kab2_13")
                                                        booked_client = request.form.get("client_13")
                                                        booked_day = 13
                                                        if not request.form.get("time_kab2_13"):
                                                            booked_time = request.form.get("time_kab2_14")
                                                            booked_client = request.form.get("client_14")
                                                            booked_day = 14
                                                            if not request.form.get("time_kab2_14"):
                                                                booked_time = request.form.get("time_kab2_15")
                                                                booked_client = request.form.get("client_15")
                                                                booked_day = 15
                                                                if not request.form.get("time_kab2_15"):
                                                                    booked_time = request.form.get("time_kab2_16")
                                                                    booked_client = request.form.get("client_16")
                                                                    booked_day = 16
                                                                    if not request.form.get("time_kab2_17"):
                                                                        booked_time = request.form.get("time_kab2_17")
                                                                        booked_client = request.form.get("client_17")
                                                                        booked_day = 17
                                                                        if not request.form.get("time_kab2_18"):
                                                                            booked_time = request.form.get("time_kab2_18")
                                                                            booked_client = request.form.get("client_18")
                                                                            booked_day = 18
                                                                            if not request.form.get("time_kab2_18"):
                                                                                booked_time = request.form.get("time_kab2_19")
                                                                                booked_client = request.form.get("client_19")
                                                                                booked_day = 19
                                                                                if not request.form.get("time_kab2_19"):
                                                                                    booked_time = request.form.get("time_kab2_20")
                                                                                    booked_client = request.form.get("client_20")
                                                                                    booked_day = 20
                                                                                    if not request.form.get("time_kab2_20"):
                                                                                        booked_time = request.form.get("time_kab2_21")
                                                                                        booked_client = request.form.get("client_21")
                                                                                        booked_day = 21
                                                                                        if not request.form.get("time_kab2_21"):
                                                                                            booked_time = request.form.get("time_kab2_22")
                                                                                            booked_client = request.form.get("client_22")
                                                                                            booked_day = 22
                                                                                            if not request.form.get("time_kab2_22"):
                                                                                                booked_time = request.form.get("time_kab2_23")
                                                                                                booked_client = request.form.get("client_23")
                                                                                                booked_day = 23
                                                                                                if not request.form.get("time_kab2_23"):
                                                                                                    booked_time = request.form.get("time_kab2_24")
                                                                                                    booked_client = request.form.get("client_24")
                                                                                                    booked_day = 24
                                                                                                    if not request.form.get("time_kab2_24"):
                                                                                                        booked_time = request.form.get("time_kab2_25")
                                                                                                        booked_client = request.form.get("client_25")
                                                                                                        booked_day = 25
                                                                                                        if not request.form.get("time_kab2_25"):
                                                                                                            booked_time = request.form.get("time_kab2_26")
                                                                                                            booked_client = request.form.get("client_26")
                                                                                                            booked_day = 26
                                                                                                            if not request.form.get("time_kab2_26"):
                                                                                                                booked_time = request.form.get("time_kab2_27")
                                                                                                                booked_client = request.form.get("client_27")
                                                                                                                booked_day = 27
                                                                                                                if not request.form.get("time_kab2_27"):
                                                                                                                    booked_time = request.form.get("time_kab2_28")
                                                                                                                    booked_client = request.form.get("client_28")
                                                                                                                    booked_day = 28
                                                                                                                    if not request.form.get("time_kab2_28"):
                                                                                                                        booked_time = request.form.get("time_kab2_29")
                                                                                                                        booked_client = request.form.get("client_29")
                                                                                                                        booked_day = 29
                                                                                                                        if not request.form.get("time_kab2_29"):
                                                                                                                            booked_time = request.form.get("time_kab2_30")
                                                                                                                            booked_client = request.form.get("client_30")
                                                                                                                            booked_day = 30
                                                                                                                            if not request.form.get("time_kab2_30"):
                                                                                                                                booked_time = request.form.get("time_kab2_31")
                                                                                                                                booked_client = request.form.get("client_31")
                                                                                                                                booked_day = 31
                                                                                                                                if not request.form.get("time_kab2_31"):
                                                                                                                                    return apology("nepasirinktas laikas")


        if booked_time == "09:00":
            booked_time = "09:00 - 10:00"

        if booked_time == "10:00":
            booked_time = "10:00 - 11:00"

        if booked_time == "11:00":
            booked_time = "11:00 - 12:00"

        if booked_time == "12:00":
            booked_time = "12:00 - 13:00"

        if booked_time == "13:00":
            booked_time = "13:00 - 14:00"

        if booked_time == "14:00":
            booked_time = "14:00 - 15:00"

        if booked_time == "15:00":
            booked_time = "15:00 - 16:00"

        if booked_time == "16:00":
            booked_time = "16:00 - 17:00"

        if booked_time == "17:00":
            booked_time = "17:00 - 18:00"

        rows = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND day = %s AND time = %s AND cabinet = 2", now_year, now_month, booked_day, booked_time)
        for row in rows:
            if row["booked"] == "Rezervuota":
                return apology ("Šis laikas jau rezervuotas")

        db.execute("UPDATE kalendorius SET user_id = %s, client = %s WHERE year = %s AND month = %s AND day = %s AND time = %s AND cabinet = 2", session["user_id"], booked_client, now_year, now_month, booked_day, booked_time)
        db.execute("UPDATE kalendorius SET booked = %s WHERE year = %s AND month = %s AND day = %s AND time = %s AND cabinet = 2", rezervuota, now_year, now_month, booked_day, booked_time)

        flash("Konsultacija užregistruota!")

        return render_template("/rezervacijos_patvirtinimas.html", booked_client=booked_client, booked_time=booked_time, booked_day=booked_day, now_year=now_year, now_month=now_month)

@app.route("/rezervacija2_next", methods=["GET", "POST"])
@login_required
def rezervacija2_next():
    if request.method=="GET":
        now = datetime.now()
        now_year = now.year
        now_month = now.month
        if now_month == 12:
            now_year = now_year + 1

        next_month = now_month + 1

        kab2_next_rows_1 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 1", now_year, next_month)
        kab2_next_rows_2 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 2", now_year, next_month)
        kab2_next_rows_3 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 3", now_year, next_month)
        kab2_next_rows_4 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 4", now_year, next_month)
        kab2_next_rows_5 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 5", now_year, next_month)
        kab2_next_rows_6 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 6", now_year, next_month)
        kab2_next_rows_7 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 7", now_year, next_month)
        kab2_next_rows_8 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 8", now_year, next_month)
        kab2_next_rows_9 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 9", now_year, next_month)
        kab2_next_rows_10 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 10", now_year, next_month)
        kab2_next_rows_11 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 11", now_year, next_month)
        kab2_next_rows_12 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 12", now_year, next_month)
        kab2_next_rows_13 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 13", now_year, next_month)
        kab2_next_rows_14 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 14", now_year, next_month)
        kab2_next_rows_15 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 15", now_year, next_month)
        kab2_next_rows_16 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 16", now_year, next_month)
        kab2_next_rows_17 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 17", now_year, next_month)
        kab2_next_rows_18 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 18", now_year, next_month)
        kab2_next_rows_19 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 19", now_year, next_month)
        kab2_next_rows_20 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 20", now_year, next_month)
        kab2_next_rows_21 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 21", now_year, next_month)
        kab2_next_rows_22 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 22", now_year, next_month)
        kab2_next_rows_23 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 23", now_year, next_month)
        kab2_next_rows_24 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 24", now_year, next_month)
        kab2_next_rows_25 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 25", now_year, next_month)
        kab2_next_rows_26 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 26", now_year, next_month)
        kab2_next_rows_27 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 27", now_year, next_month)
        kab2_next_rows_28 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 28", now_year, next_month)
        kab2_next_rows_29 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 29", now_year, next_month)
        kab2_next_rows_30 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 30", now_year, next_month)
        kab2_next_rows_31 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 2 AND day = 31", now_year, next_month)

        return render_template("/rezervacija2_next.html", now_year=now_year, next_month=next_month, kab2_next_rows_1=kab2_next_rows_1, kab2_next_rows_2=kab2_next_rows_2, kab2_next_rows_3=kab2_next_rows_3, kab2_next_rows_4=kab2_next_rows_4, kab2_next_rows_5=kab2_next_rows_5, kab2_next_rows_6=kab2_next_rows_6, kab2_next_rows_7=kab2_next_rows_7, kab2_next_rows_8=kab2_next_rows_8, kab2_next_rows_9=kab2_next_rows_9, kab2_next_rows_10=kab2_next_rows_10, kab2_next_rows_11=kab2_next_rows_11, kab2_next_rows_12=kab2_next_rows_12, kab2_next_rows_13=kab2_next_rows_13, kab2_next_rows_14=kab2_next_rows_14, kab2_next_rows_15=kab2_next_rows_15, kab2_next_rows_16=kab2_next_rows_16, kab2_next_rows_17=kab2_next_rows_17, kab2_next_rows_18=kab2_next_rows_18, kab2_next_rows_19=kab2_next_rows_19, kab2_next_rows_20=kab2_next_rows_20, kab2_next_rows_21=kab2_next_rows_21, kab2_next_rows_22=kab2_next_rows_22, kab2_next_rows_23=kab2_next_rows_23, kab2_next_rows_24=kab2_next_rows_24, kab2_next_rows_25=kab2_next_rows_25, kab2_next_rows_26=kab2_next_rows_26, kab2_next_rows_27=kab2_next_rows_27, kab2_next_rows_28=kab2_next_rows_28, kab2_next_rows_29=kab2_next_rows_29, kab2_next_rows_30=kab2_next_rows_30, kab2_next_rows_31=kab2_next_rows_31)

    if request.method=="POST":
        now = datetime.now()
        now_year = now.year
        now_month = now.month
        rezervuota = "Rezervuota"

        if now_month == 12:
            now_year = now_year + 1

        next_month = now_month + 1

        booked_time = request.form.get("time_kab2_next_1")
        booked_client = request.form.get("client_1")
        booked_day = 1
        if not request.form.get("time_kab2_next_1"):
            booked_time = request.form.get("time_kab2_next_2")
            booked_client = request.form.get("client_2")
            booked_day = 2
            if not request.form.get("time_kab2_next_2"):
                booked_time = request.form.get("time_kab2_next_3")
                booked_client = request.form.get("client_3")
                booked_day = 3
                if not request.form.get("time_kab2_next_3"):
                    booked_time = request.form.get("time_kab2_next_4")
                    booked_client = request.form.get("client_4")
                    booked_day = 4
                    if not request.form.get("time_kab2_next_4"):
                        booked_time = request.form.get("time_kab2_next_5")
                        booked_client = request.form.get("client_5")
                        booked_day = 5
                        if not request.form.get("time_kab2_next_5"):
                            booked_time = request.form.get("time_kab2_next_6")
                            booked_client = request.form.get("client_6")
                            booked_day = 6
                            if not request.form.get("time_kab2_next_6"):
                                booked_time = request.form.get("time_kab2_next_7")
                                booked_client = request.form.get("client_7")
                                booked_day = 7
                                if not request.form.get("time_kab2_next_7"):
                                    booked_time = request.form.get("time_kab2_next_8")
                                    booked_client = request.form.get("client_8")
                                    booked_day = 8
                                    if not request.form.get("time_kab2_next_8"):
                                        booked_time = request.form.get("time_kab2_next_9")
                                        booked_client = request.form.get("client_9")
                                        booked_day = 9
                                        if not request.form.get("time_kab2_next_9"):
                                            booked_time = request.form.get("time_kab2_next_10")
                                            booked_client = request.form.get("client10")
                                            booked_day = 10
                                            if not request.form.get("time_kab2_next_10"):
                                                booked_time = request.form.get("time_kab2_next_11")
                                                booked_client = request.form.get("client_11")
                                                booked_day = 11
                                                if not request.form.get("time_kab2_next_11"):
                                                    booked_time = request.form.get("time_kab2_next_12")
                                                    booked_client = request.form.get("client_12")
                                                    booked_day = 12
                                                    if not request.form.get("time_kab2_next_12"):
                                                        booked_time = request.form.get("time_kab2_next_13")
                                                        booked_client = request.form.get("client_13")
                                                        booked_day = 13
                                                        if not request.form.get("time_kab2_next_13"):
                                                            booked_time = request.form.get("time_kab2_next_14")
                                                            booked_client = request.form.get("client_14")
                                                            booked_day = 14
                                                            if not request.form.get("time_kab2_next_14"):
                                                                booked_time = request.form.get("time_kab2_next_15")
                                                                booked_client = request.form.get("client_15")
                                                                booked_day = 15
                                                                if not request.form.get("time_kab2_next_15"):
                                                                    booked_time = request.form.get("time_kab2_next_16")
                                                                    booked_client = request.form.get("client_16")
                                                                    booked_day = 16
                                                                    if not request.form.get("time_kab2_next_17"):
                                                                        booked_time = request.form.get("time_kab2_next_17")
                                                                        booked_client = request.form.get("client_17")
                                                                        booked_day = 17
                                                                        if not request.form.get("time_kab2_next_18"):
                                                                            booked_time = request.form.get("time_kab2_next_18")
                                                                            booked_client = request.form.get("client_18")
                                                                            booked_day = 18
                                                                            if not request.form.get("time_kab2_next_18"):
                                                                                booked_time = request.form.get("time_kab2_next_19")
                                                                                booked_client = request.form.get("client_19")
                                                                                booked_day = 19
                                                                                if not request.form.get("time_kab2_next_19"):
                                                                                    booked_time = request.form.get("time_kab2_next_20")
                                                                                    booked_client = request.form.get("client_20")
                                                                                    booked_day = 20
                                                                                    if not request.form.get("time_kab2_next_20"):
                                                                                        booked_time = request.form.get("time_kab2_next_21")
                                                                                        booked_client = request.form.get("client_21")
                                                                                        booked_day = 21
                                                                                        if not request.form.get("time_kab2_next_21"):
                                                                                            booked_time = request.form.get("time_kab2_next_22")
                                                                                            booked_client = request.form.get("client_22")
                                                                                            booked_day = 22
                                                                                            if not request.form.get("time_kab2_next_22"):
                                                                                                booked_time = request.form.get("time_kab2_next_23")
                                                                                                booked_client = request.form.get("client_23")
                                                                                                booked_day = 23
                                                                                                if not request.form.get("time_kab2_next_23"):
                                                                                                    booked_time = request.form.get("time_kab2_next_24")
                                                                                                    booked_client = request.form.get("client_24")
                                                                                                    booked_day = 24
                                                                                                    if not request.form.get("time_kab2_next_24"):
                                                                                                        booked_time = request.form.get("time_kab2_next_25")
                                                                                                        booked_client = request.form.get("client_25")
                                                                                                        booked_day = 25
                                                                                                        if not request.form.get("time_kab2_next_25"):
                                                                                                            booked_time = request.form.get("time_kab2_next_26")
                                                                                                            booked_client = request.form.get("client_26")
                                                                                                            booked_day = 26
                                                                                                            if not request.form.get("time_kab2_next_26"):
                                                                                                                booked_time = request.form.get("time_kab2_next_27")
                                                                                                                booked_client = request.form.get("client_27")
                                                                                                                booked_day = 27
                                                                                                                if not request.form.get("time_kab2_next_27"):
                                                                                                                    booked_time = request.form.get("time_kab2_next_28")
                                                                                                                    booked_client = request.form.get("client_28")
                                                                                                                    booked_day = 28
                                                                                                                    if not request.form.get("time_kab2_next_28"):
                                                                                                                        booked_time = request.form.get("time_kab2_next_29")
                                                                                                                        booked_client = request.form.get("client_29")
                                                                                                                        booked_day = 29
                                                                                                                        if not request.form.get("time_kab2_next_29"):
                                                                                                                            booked_time = request.form.get("time_kab2_next_30")
                                                                                                                            booked_client = request.form.get("client_30")
                                                                                                                            booked_day = 30
                                                                                                                            if not request.form.get("time_kab2_next_30"):
                                                                                                                                booked_time = request.form.get("time_kab2_next_31")
                                                                                                                                booked_client = request.form.get("client_31")
                                                                                                                                booked_day = 31
                                                                                                                                if not request.form.get("time_kab2_next_31"):
                                                                                                                                    return apology("nepasirinktas laikas")


        if booked_time == "09:00":
            booked_time = "09:00 - 10:00"

        if booked_time == "10:00":
            booked_time = "10:00 - 11:00"

        if booked_time == "11:00":
            booked_time = "11:00 - 12:00"

        if booked_time == "12:00":
            booked_time = "12:00 - 13:00"

        if booked_time == "13:00":
            booked_time = "13:00 - 14:00"

        if booked_time == "14:00":
            booked_time = "14:00 - 15:00"

        if booked_time == "15:00":
            booked_time = "15:00 - 16:00"

        if booked_time == "16:00":
            booked_time = "16:00 - 17:00"

        if booked_time == "17:00":
            booked_time = "17:00 - 18:00"

        rows = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND day = %s AND time = %s AND cabinet = 2", now_year, next_month, booked_day, booked_time)
        for row in rows:
            if row["booked"] == "Rezervuota":
                return apology ("Šis laikas jau rezervuotas")

        db.execute("UPDATE kalendorius SET user_id = %s, client = %s WHERE year = %s AND month = %s AND day = %s AND time = %s AND cabinet = 2", session["user_id"], booked_client, now_year, next_month, booked_day, booked_time)
        db.execute("UPDATE kalendorius SET booked = %s WHERE year = %s AND month = %s AND day = %s AND time = %s AND cabinet = 2", rezervuota, now_year, next_month, booked_day, booked_time)

        flash("Konsultacija užregistruota!")

        return render_template("/rezervacijos_patvirtinimas.html", booked_client=booked_client, booked_time=booked_time, booked_day=booked_day, now_year=now_year, next_month=next_month)


@app.route("/rezervacija3", methods=["GET", "POST"])
@login_required
def rezervacija3():
    if request.method=="GET":
        now = datetime.now()
        now_year = now.year
        now_month = now.month

        kab3_rows_1 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 1", now_year, now_month)
        kab3_rows_2 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 2", now_year, now_month)
        kab3_rows_3 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 3", now_year, now_month)
        kab3_rows_4 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 4", now_year, now_month)
        kab3_rows_5 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 5", now_year, now_month)
        kab3_rows_6 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 6", now_year, now_month)
        kab3_rows_7 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 7", now_year, now_month)
        kab3_rows_8 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 8", now_year, now_month)
        kab3_rows_9 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 9", now_year, now_month)
        kab3_rows_10 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 10", now_year, now_month)
        kab3_rows_11 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 11", now_year, now_month)
        kab3_rows_12 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 12", now_year, now_month)
        kab3_rows_13 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 13", now_year, now_month)
        kab3_rows_14 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 14", now_year, now_month)
        kab3_rows_15 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 15", now_year, now_month)
        kab3_rows_16 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 16", now_year, now_month)
        kab3_rows_17 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 17", now_year, now_month)
        kab3_rows_18 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 18", now_year, now_month)
        kab3_rows_19 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 19", now_year, now_month)
        kab3_rows_20 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 20", now_year, now_month)
        kab3_rows_21 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 21", now_year, now_month)
        kab3_rows_22 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 22", now_year, now_month)
        kab3_rows_23 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 23", now_year, now_month)
        kab3_rows_24 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 24", now_year, now_month)
        kab3_rows_25 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 25", now_year, now_month)
        kab3_rows_26 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 26", now_year, now_month)
        kab3_rows_27 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 27", now_year, now_month)
        kab3_rows_28 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 28", now_year, now_month)
        kab3_rows_29 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 29", now_year, now_month)
        kab3_rows_30 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 30", now_year, now_month)
        kab3_rows_31 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 31", now_year, now_month)

        return render_template("/rezervacija3.html", now_year=now_year, now_month=now_month, kab3_rows_1=kab3_rows_1, kab3_rows_2=kab3_rows_2, kab3_rows_3=kab3_rows_3, kab3_rows_4=kab3_rows_4, kab3_rows_5=kab3_rows_5, kab3_rows_6=kab3_rows_6, kab3_rows_7=kab3_rows_7, kab3_rows_8=kab3_rows_8, kab3_rows_9=kab3_rows_9, kab3_rows_10=kab3_rows_10, kab3_rows_11=kab3_rows_11, kab3_rows_12=kab3_rows_12, kab3_rows_13=kab3_rows_13, kab3_rows_14=kab3_rows_14, kab3_rows_15=kab3_rows_15, kab3_rows_16=kab3_rows_16, kab3_rows_17=kab3_rows_17, kab3_rows_18=kab3_rows_18, kab3_rows_19=kab3_rows_19, kab3_rows_20=kab3_rows_20, kab3_rows_21=kab3_rows_21, kab3_rows_22=kab3_rows_22, kab3_rows_23=kab3_rows_23, kab3_rows_24=kab3_rows_24, kab3_rows_25=kab3_rows_25, kab3_rows_26=kab3_rows_26, kab3_rows_27=kab3_rows_27, kab3_rows_28=kab3_rows_28, kab3_rows_29=kab3_rows_29, kab3_rows_30=kab3_rows_30, kab3_rows_31=kab3_rows_31)


    if request.method=="POST":
        now = datetime.now()
        now_year = now.year
        now_month = now.month
        rezervuota = "Rezervuota"

        booked_time = request.form.get("time_kab3_1")
        booked_client = request.form.get("client_1")
        booked_day = 1
        if not request.form.get("time_kab3_1"):
            booked_time = request.form.get("time_kab3_2")
            booked_client = request.form.get("client_2")
            booked_day = 2
            if not request.form.get("time_kab3_2"):
                booked_time = request.form.get("time_kab3_3")
                booked_client = request.form.get("client_3")
                booked_day = 3
                if not request.form.get("time_kab3_3"):
                    booked_time = request.form.get("time_kab3_4")
                    booked_client = request.form.get("client_4")
                    booked_day = 4
                    if not request.form.get("time_kab3_4"):
                        booked_time = request.form.get("time_kab3_5")
                        booked_client = request.form.get("client_5")
                        booked_day = 5
                        if not request.form.get("time_kab3_5"):
                            booked_time = request.form.get("time_kab3_6")
                            booked_client = request.form.get("client_6")
                            booked_day = 6
                            if not request.form.get("time_kab3_6"):
                                booked_time = request.form.get("time_kab3_7")
                                booked_client = request.form.get("client_7")
                                booked_day = 7
                                if not request.form.get("time_kab3_7"):
                                    booked_time = request.form.get("time_kab3_8")
                                    booked_client = request.form.get("client_8")
                                    booked_day = 8
                                    if not request.form.get("time_kab3_8"):
                                        booked_time = request.form.get("time_kab3_9")
                                        booked_client = request.form.get("client_9")
                                        booked_day = 9
                                        if not request.form.get("time_kab3_9"):
                                            booked_time = request.form.get("time_kab3_10")
                                            booked_client = request.form.get("client10")
                                            booked_day = 10
                                            if not request.form.get("time_kab3_10"):
                                                booked_time = request.form.get("time_kab3_11")
                                                booked_client = request.form.get("client_11")
                                                booked_day = 11
                                                if not request.form.get("time_kab3_11"):
                                                    booked_time = request.form.get("time_kab3_12")
                                                    booked_client = request.form.get("client_12")
                                                    booked_day = 12
                                                    if not request.form.get("time_kab3_12"):
                                                        booked_time = request.form.get("time_kab3_13")
                                                        booked_client = request.form.get("client_13")
                                                        booked_day = 13
                                                        if not request.form.get("time_kab3_13"):
                                                            booked_time = request.form.get("time_kab3_14")
                                                            booked_client = request.form.get("client_14")
                                                            booked_day = 14
                                                            if not request.form.get("time_kab3_14"):
                                                                booked_time = request.form.get("time_kab3_15")
                                                                booked_client = request.form.get("client_15")
                                                                booked_day = 15
                                                                if not request.form.get("time_kab3_15"):
                                                                    booked_time = request.form.get("time_kab3_16")
                                                                    booked_client = request.form.get("client_16")
                                                                    booked_day = 16
                                                                    if not request.form.get("time_kab3_17"):
                                                                        booked_time = request.form.get("time_kab3_17")
                                                                        booked_client = request.form.get("client_17")
                                                                        booked_day = 17
                                                                        if not request.form.get("time_kab3_18"):
                                                                            booked_time = request.form.get("time_kab3_18")
                                                                            booked_client = request.form.get("client_18")
                                                                            booked_day = 18
                                                                            if not request.form.get("time_kab3_18"):
                                                                                booked_time = request.form.get("time_kab3_19")
                                                                                booked_client = request.form.get("client_19")
                                                                                booked_day = 19
                                                                                if not request.form.get("time_kab3_19"):
                                                                                    booked_time = request.form.get("time_kab3_20")
                                                                                    booked_client = request.form.get("client_20")
                                                                                    booked_day = 20
                                                                                    if not request.form.get("time_kab3_20"):
                                                                                        booked_time = request.form.get("time_kab3_21")
                                                                                        booked_client = request.form.get("client_21")
                                                                                        booked_day = 21
                                                                                        if not request.form.get("time_kab3_21"):
                                                                                            booked_time = request.form.get("time_kab3_22")
                                                                                            booked_client = request.form.get("client_22")
                                                                                            booked_day = 22
                                                                                            if not request.form.get("time_kab3_22"):
                                                                                                booked_time = request.form.get("time_kab3_23")
                                                                                                booked_client = request.form.get("client_23")
                                                                                                booked_day = 23
                                                                                                if not request.form.get("time_kab3_23"):
                                                                                                    booked_time = request.form.get("time_kab3_24")
                                                                                                    booked_client = request.form.get("client_24")
                                                                                                    booked_day = 24
                                                                                                    if not request.form.get("time_kab3_24"):
                                                                                                        booked_time = request.form.get("time_kab3_25")
                                                                                                        booked_client = request.form.get("client_25")
                                                                                                        booked_day = 25
                                                                                                        if not request.form.get("time_kab3_25"):
                                                                                                            booked_time = request.form.get("time_kab3_26")
                                                                                                            booked_client = request.form.get("client_26")
                                                                                                            booked_day = 26
                                                                                                            if not request.form.get("time_kab3_26"):
                                                                                                                booked_time = request.form.get("time_kab3_27")
                                                                                                                booked_client = request.form.get("client_27")
                                                                                                                booked_day = 27
                                                                                                                if not request.form.get("time_kab3_27"):
                                                                                                                    booked_time = request.form.get("time_kab3_28")
                                                                                                                    booked_client = request.form.get("client_28")
                                                                                                                    booked_day = 28
                                                                                                                    if not request.form.get("time_kab3_28"):
                                                                                                                        booked_time = request.form.get("time_kab3_29")
                                                                                                                        booked_client = request.form.get("client_29")
                                                                                                                        booked_day = 29
                                                                                                                        if not request.form.get("time_kab3_29"):
                                                                                                                            booked_time = request.form.get("time_kab3_30")
                                                                                                                            booked_client = request.form.get("client_30")
                                                                                                                            booked_day = 30
                                                                                                                            if not request.form.get("time_kab3_30"):
                                                                                                                                booked_time = request.form.get("time_kab3_31")
                                                                                                                                booked_client = request.form.get("client_31")
                                                                                                                                booked_day = 31
                                                                                                                                if not request.form.get("time_kab3_31"):
                                                                                                                                    return apology("nepasirinktas laikas")


        if booked_time == "09:00":
            booked_time = "09:00 - 10:00"

        if booked_time == "10:00":
            booked_time = "10:00 - 11:00"

        if booked_time == "11:00":
            booked_time = "11:00 - 12:00"

        if booked_time == "12:00":
            booked_time = "12:00 - 13:00"

        if booked_time == "13:00":
            booked_time = "13:00 - 14:00"

        if booked_time == "14:00":
            booked_time = "14:00 - 15:00"

        if booked_time == "15:00":
            booked_time = "15:00 - 16:00"

        if booked_time == "16:00":
            booked_time = "16:00 - 17:00"

        if booked_time == "17:00":
            booked_time = "17:00 - 18:00"

        rows = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND day = %s AND time = %s AND cabinet = 3", now_year, now_month, booked_day, booked_time)
        for row in rows:
            if row["booked"] == "Rezervuota":
                return apology ("Šis laikas jau rezervuotas")

        db.execute("UPDATE kalendorius SET user_id = %s, client = %s WHERE year = %s AND month = %s AND day = %s AND time = %s AND cabinet = 3", session["user_id"], booked_client, now_year, now_month, booked_day, booked_time)
        db.execute("UPDATE kalendorius SET booked = %s WHERE year = %s AND month = %s AND day = %s AND time = %s AND cabinet = 3", rezervuota, now_year, now_month, booked_day, booked_time)

        flash("Konsultacija užregistruota!")

        return render_template("/rezervacijos_patvirtinimas.html", booked_client=booked_client, booked_time=booked_time, booked_day=booked_day, now_year=now_year, now_month=now_month)

@app.route("/rezervacija3_next", methods=["GET", "POST"])
@login_required
def rezervacija3_next():
    if request.method=="GET":
        now = datetime.now()
        now_year = now.year
        now_month = now.month

        if now_month == 12:
            now_year = now_year + 1

        next_month = now_month + 1

        kab3_next_rows_1 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 1", now_year, next_month)
        kab3_next_rows_2 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 2", now_year, next_month)
        kab3_next_rows_3 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 3", now_year, next_month)
        kab3_next_rows_4 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 4", now_year, next_month)
        kab3_next_rows_5 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 5", now_year, next_month)
        kab3_next_rows_6 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 6", now_year, next_month)
        kab3_next_rows_7 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 7", now_year, next_month)
        kab3_next_rows_8 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 8", now_year, next_month)
        kab3_next_rows_9 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 9", now_year, next_month)
        kab3_next_rows_10 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 10", now_year, next_month)
        kab3_next_rows_11 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 11", now_year, next_month)
        kab3_next_rows_12 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 12", now_year, next_month)
        kab3_next_rows_13 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 13", now_year, next_month)
        kab3_next_rows_14 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 14", now_year, next_month)
        kab3_next_rows_15 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 15", now_year, next_month)
        kab3_next_rows_16 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 16", now_year, next_month)
        kab3_next_rows_17 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 17", now_year, next_month)
        kab3_next_rows_18 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 18", now_year, next_month)
        kab3_next_rows_19 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 19", now_year, next_month)
        kab3_next_rows_20 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 20", now_year, next_month)
        kab3_next_rows_21 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 21", now_year, next_month)
        kab3_next_rows_22 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 22", now_year, next_month)
        kab3_next_rows_23 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 23", now_year, next_month)
        kab3_next_rows_24 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 24", now_year, next_month)
        kab3_next_rows_25 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 25", now_year, next_month)
        kab3_next_rows_26 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 26", now_year, next_month)
        kab3_next_rows_27 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 27", now_year, next_month)
        kab3_next_rows_28 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 28", now_year, next_month)
        kab3_next_rows_29 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 29", now_year, next_month)
        kab3_next_rows_30 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 30", now_year, next_month)
        kab3_next_rows_31 = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND cabinet = 3 AND day = 31", now_year, next_month)

        return render_template("/rezervacija3_next.html", now_year=now_year, next_month=next_month, kab3_next_rows_1=kab3_next_rows_1, kab3_next_rows_2=kab3_next_rows_2, kab3_next_rows_3=kab3_next_rows_3, kab3_next_rows_4=kab3_next_rows_4, kab3_next_rows_5=kab3_next_rows_5, kab3_next_rows_6=kab3_next_rows_6, kab3_next_rows_7=kab3_next_rows_7, kab3_next_rows_8=kab3_next_rows_8, kab3_next_rows_9=kab3_next_rows_9, kab3_next_rows_10=kab3_next_rows_10, kab3_next_rows_11=kab3_next_rows_11, kab3_next_rows_12=kab3_next_rows_12, kab3_next_rows_13=kab3_next_rows_13, kab3_next_rows_14=kab3_next_rows_14, kab3_next_rows_15=kab3_next_rows_15, kab3_next_rows_16=kab3_next_rows_16, kab3_next_rows_17=kab3_next_rows_17, kab3_next_rows_18=kab3_next_rows_18, kab3_next_rows_19=kab3_next_rows_19, kab3_next_rows_20=kab3_next_rows_20, kab3_next_rows_21=kab3_next_rows_21, kab3_next_rows_22=kab3_next_rows_22, kab3_next_rows_23=kab3_next_rows_23, kab3_next_rows_24=kab3_next_rows_24, kab3_next_rows_25=kab3_next_rows_25, kab3_next_rows_26=kab3_next_rows_26, kab3_next_rows_27=kab3_next_rows_27, kab3_next_rows_28=kab3_next_rows_28, kab3_next_rows_29=kab3_next_rows_29, kab3_next_rows_30=kab3_next_rows_30, kab3_next_rows_31=kab3_next_rows_31)


    if request.method=="POST":
        now = datetime.now()
        now_year = now.year
        now_month = now.month
        if now_month == 12:
            now_year = now_year + 1

        next_month = now_month + 1

        rezervuota = "Rezervuota"

        booked_time = request.form.get("time_kab3_next_1")
        booked_client = request.form.get("client_1")
        booked_day = 1
        if not request.form.get("time_kab3_next_1"):
            booked_time = request.form.get("time_kab3_next_2")
            booked_client = request.form.get("client_2")
            booked_day = 2
            if not request.form.get("time_kab3_next_2"):
                booked_time = request.form.get("time_kab3_next_3")
                booked_client = request.form.get("client_3")
                booked_day = 3
                if not request.form.get("time_kab3_next_3"):
                    booked_time = request.form.get("time_kab3_next_4")
                    booked_client = request.form.get("client_4")
                    booked_day = 4
                    if not request.form.get("time_kab3_next_4"):
                        booked_time = request.form.get("time_kab3_next_5")
                        booked_client = request.form.get("client_5")
                        booked_day = 5
                        if not request.form.get("time_kab3_next_5"):
                            booked_time = request.form.get("time_kab3_next_6")
                            booked_client = request.form.get("client_6")
                            booked_day = 6
                            if not request.form.get("time_kab3_next_6"):
                                booked_time = request.form.get("time_kab3_next_7")
                                booked_client = request.form.get("client_7")
                                booked_day = 7
                                if not request.form.get("time_kab3_next_7"):
                                    booked_time = request.form.get("time_kab3_next_8")
                                    booked_client = request.form.get("client_8")
                                    booked_day = 8
                                    if not request.form.get("time_kab3_next_8"):
                                        booked_time = request.form.get("time_kab3_next_9")
                                        booked_client = request.form.get("client_9")
                                        booked_day = 9
                                        if not request.form.get("time_kab3_next_9"):
                                            booked_time = request.form.get("time_kab3_next_10")
                                            booked_client = request.form.get("client10")
                                            booked_day = 10
                                            if not request.form.get("time_kab3_next_10"):
                                                booked_time = request.form.get("time_kab3_next_11")
                                                booked_client = request.form.get("client_11")
                                                booked_day = 11
                                                if not request.form.get("time_kab3_next_11"):
                                                    booked_time = request.form.get("time_kab3_next_12")
                                                    booked_client = request.form.get("client_12")
                                                    booked_day = 12
                                                    if not request.form.get("time_kab3_next_12"):
                                                        booked_time = request.form.get("time_kab3_next_13")
                                                        booked_client = request.form.get("client_13")
                                                        booked_day = 13
                                                        if not request.form.get("time_kab3_next_13"):
                                                            booked_time = request.form.get("time_kab3_next_14")
                                                            booked_client = request.form.get("client_14")
                                                            booked_day = 14
                                                            if not request.form.get("time_kab3_next_14"):
                                                                booked_time = request.form.get("time_kab3_next_15")
                                                                booked_client = request.form.get("client_15")
                                                                booked_day = 15
                                                                if not request.form.get("time_kab3_next_15"):
                                                                    booked_time = request.form.get("time_kab3_next_16")
                                                                    booked_client = request.form.get("client_16")
                                                                    booked_day = 16
                                                                    if not request.form.get("time_kab3_next_17"):
                                                                        booked_time = request.form.get("time_kab3_next_17")
                                                                        booked_client = request.form.get("client_17")
                                                                        booked_day = 17
                                                                        if not request.form.get("time_kab3_next_18"):
                                                                            booked_time = request.form.get("time_kab3_next_18")
                                                                            booked_client = request.form.get("client_18")
                                                                            booked_day = 18
                                                                            if not request.form.get("time_kab3_next_18"):
                                                                                booked_time = request.form.get("time_kab3_next_19")
                                                                                booked_client = request.form.get("client_19")
                                                                                booked_day = 19
                                                                                if not request.form.get("time_kab3_next_19"):
                                                                                    booked_time = request.form.get("time_kab3_next_20")
                                                                                    booked_client = request.form.get("client_20")
                                                                                    booked_day = 20
                                                                                    if not request.form.get("time_kab3_next_20"):
                                                                                        booked_time = request.form.get("time_kab3_next_21")
                                                                                        booked_client = request.form.get("client_21")
                                                                                        booked_day = 21
                                                                                        if not request.form.get("time_kab3_next_21"):
                                                                                            booked_time = request.form.get("time_kab3_next_22")
                                                                                            booked_client = request.form.get("client_22")
                                                                                            booked_day = 22
                                                                                            if not request.form.get("time_kab3_next_22"):
                                                                                                booked_time = request.form.get("time_kab3_next_23")
                                                                                                booked_client = request.form.get("client_23")
                                                                                                booked_day = 23
                                                                                                if not request.form.get("time_kab3_next_23"):
                                                                                                    booked_time = request.form.get("time_kab3_next_24")
                                                                                                    booked_client = request.form.get("client_24")
                                                                                                    booked_day = 24
                                                                                                    if not request.form.get("time_kab3_next_24"):
                                                                                                        booked_time = request.form.get("time_kab3_next_25")
                                                                                                        booked_client = request.form.get("client_25")
                                                                                                        booked_day = 25
                                                                                                        if not request.form.get("time_kab3_next_25"):
                                                                                                            booked_time = request.form.get("time_kab3_next_26")
                                                                                                            booked_client = request.form.get("client_26")
                                                                                                            booked_day = 26
                                                                                                            if not request.form.get("time_kab3_next_26"):
                                                                                                                booked_time = request.form.get("time_kab3_next_27")
                                                                                                                booked_client = request.form.get("client_27")
                                                                                                                booked_day = 27
                                                                                                                if not request.form.get("time_kab3_next_27"):
                                                                                                                    booked_time = request.form.get("time_kab3_next_28")
                                                                                                                    booked_client = request.form.get("client_28")
                                                                                                                    booked_day = 28
                                                                                                                    if not request.form.get("time_kab3_next_28"):
                                                                                                                        booked_time = request.form.get("time_kab3_next_29")
                                                                                                                        booked_client = request.form.get("client_29")
                                                                                                                        booked_day = 29
                                                                                                                        if not request.form.get("time_kab3_next_29"):
                                                                                                                            booked_time = request.form.get("time_kab3_next_30")
                                                                                                                            booked_client = request.form.get("client_30")
                                                                                                                            booked_day = 30
                                                                                                                            if not request.form.get("time_kab3_next_30"):
                                                                                                                                booked_time = request.form.get("time_kab3_next_31")
                                                                                                                                booked_client = request.form.get("client_31")
                                                                                                                                booked_day = 31
                                                                                                                                if not request.form.get("time_kab3_next_31"):
                                                                                                                                    return apology("nepasirinktas laikas")


        if booked_time == "09:00":
            booked_time = "09:00 - 10:00"

        if booked_time == "10:00":
            booked_time = "10:00 - 11:00"

        if booked_time == "11:00":
            booked_time = "11:00 - 12:00"

        if booked_time == "12:00":
            booked_time = "12:00 - 13:00"

        if booked_time == "13:00":
            booked_time = "13:00 - 14:00"

        if booked_time == "14:00":
            booked_time = "14:00 - 15:00"

        if booked_time == "15:00":
            booked_time = "15:00 - 16:00"

        if booked_time == "16:00":
            booked_time = "16:00 - 17:00"

        if booked_time == "17:00":
            booked_time = "17:00 - 18:00"

        rows = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND day = %s AND time = %s AND cabinet = 3", now_year, next_month, booked_day, booked_time)
        for row in rows:
            if row["booked"] == "Rezervuota":
                return apology ("Šis laikas jau rezervuotas")

        db.execute("UPDATE kalendorius SET user_id = %s, client = %s WHERE year = %s AND month = %s AND day = %s AND time = %s AND cabinet = 3", session["user_id"], booked_client, now_year, next_month, booked_day, booked_time)
        db.execute("UPDATE kalendorius SET booked = %s WHERE year = %s AND month = %s AND day = %s AND time = %s AND cabinet = 3", rezervuota, now_year, next_month, booked_day, booked_time)

        flash("Konsultacija užregistruota!")

        return render_template("/rezervacijos_patvirtinimas.html", booked_client=booked_client, booked_time=booked_time, booked_day=booked_day, now_year=now_year, next_month=next_month)

@app.route("/mano_rezervacijos", methods=["GET", "POST"])
@login_required
def mano_rezervacijos():
    if request.method=="GET":
        now = datetime.now()
        now_year = now.year
        now_month = now.month
        now_day = now.day
        next_month = now_month + 1

        if now_month == 12:
            next_year = now_year + 1
            next_month == 1

            rows = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND day >= %s AND user_id = %s ORDER BY day, time", now_year, now_month, now_day, session["user_id"])
            next_rows = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND user_id = %s ORDER BY day, time", next_year, next_month, session["user_id"])

        else:

            rows = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND day >= %s AND user_id = %s ORDER BY day, time", now_year, now_month, now_day, session["user_id"])
            next_rows = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND user_id = %s ORDER BY day, time", now_year, next_month, session["user_id"])

        vartotojai = db.execute("SELECT * FROM vartotojai WHERE id = %s", session["user_id"])
        name = vartotojai[0]["name"]
        surname = vartotojai[0]["surname"]

        # return render_template("/test.html", rows=rows, next_rows=next_rows)

        return render_template("/mano_rezervacijos.html", rows=rows, next_rows=next_rows, now_month=now_month, next_month=next_month, name=name, surname=surname)

    if request.method=="POST":
        booking_id = request.form.get("booking_id")
        laisva = "Laisva"
        client = "-"

        db.execute("UPDATE kalendorius SET booked = %s, user_id = NULL, client = %s WHERE id = %s AND user_id = %s", laisva, client, booking_id, session["user_id"])

        flash("Rezervacijos laikas ištrintas!")

        return render_template("/index.html")

@app.route("/visos_rezervacijos", methods=["GET", "POST"])
@login_required
def visos_rezervacijos():
    if session["user_type"] == "ADM":
        if request.method=="GET":
            now = datetime.now()
            now_year = now.year
            now_month = now.month
            now_day = now.day
            next_month = now_month + 1
            rezervuota = "Rezervuota"

            if now_month == 12:
                next_year = now_year + 1
                next_month == 1

                rows = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND day >= %s AND booked = %s ORDER BY day, time", now_year, now_month, now_day, rezervuota)
                next_rows = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND booked = %s ORDER BY day, time", next_year, next_month, rezervuota)

            else:

                rows = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND day >= %s AND booked = %s ORDER BY day, time", now_year, now_month, now_day, rezervuota)
                next_rows = db.execute("SELECT * FROM kalendorius WHERE year = %s AND month = %s AND booked = %s ORDER BY day, time", now_year, next_month, rezervuota)

            return render_template("/visos_rezervacijos.html", rows=rows, next_rows=next_rows, now_month=now_month, next_month=next_month)

        if request.method=="POST":
            booking_id = request.form.get("booking_id")
            laisva = "Laisva"
            client = "-"

            db.execute("UPDATE kalendorius SET booked = %s, user_id = NULL, client = %s WHERE id = %s", laisva, client, booking_id)

            flash("Rezervacijos laikas ištrintas!")

            return render_template("/index.html")
    else:
        return render_template("/index.html")

@app.route("/istorija", methods=["GET", "POST"])
@login_required
def istorija():
    if request.method=="GET":

        vartotojai = db.execute("SELECT * FROM vartotojai WHERE id = %s", session["user_id"])
        name = vartotojai[0]["name"]
        surname = vartotojai[0]["surname"]

        rows = db.execute("SELECT * FROM po_konsultacijos WHERE user_id = %s ORDER BY consultation_date DESC", session["user_id"])

        return render_template("/istorija.html", rows=rows, name=name, surname=surname)

@app.route("/visa_istorija", methods=["GET", "POST"])
@login_required
def visa_istorija():
    if session["user_type"] == "ADM":
        if request.method=="GET":
            rows = db.execute("SELECT * FROM po_konsultacijos ORDER BY consultation_date DESC")

            return render_template("/visa_istorija.html", rows=rows)
    else:
        return render_template("/index.html")

@app.route("/vartotojai", methods=["GET", "POST"])
@login_required
def vartotojai():
    if session["user_type"] == "ADM":
        if request.method=="GET":
            rows = db.execute("SELECT * FROM vartotojai ORDER BY surname")

            return render_template("/vartotojai.html", rows=rows)
    else:
        return render_template("/index.html")

@app.route("/neaprasytos_konsultacijos", methods=["GET", "POST"])
@login_required
def neaprasytos_konsultacijos():
    if request.method=="GET":
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day

        vartotojai = db.execute("SELECT * FROM vartotojai WHERE id = %s", session["user_id"])
        name = vartotojai[0]["name"]
        surname = vartotojai[0]["surname"]
        yes = "Taip"

        rows = db.execute("SELECT * FROM kalendorius WHERE user_id = %s AND year <= %s AND month <= %s AND day <= %s and reported IS NOT %s ORDER BY year, month, day DESC", session["user_id"], year, month, day, yes)

        return render_template("/neaprasytos_konsultacijos.html", rows=rows, name=name, surname=surname)

@app.route("/visos_neaprasytos_konsultacijos", methods=["GET", "POST"])
@login_required
def visos_neaprasytos_konsultacijos():
    if session["user_type"] == "ADM":
        if request.method=="GET":
            now = datetime.now()
            year = now.year
            month = now.month
            day = now.day

            yes = "Taip"
            rezervuota = "Rezervuota"

            rows = db.execute("SELECT * FROM kalendorius WHERE year <= %s AND month <= %s AND day <= %s AND booked = %s and reported IS NOT %s ORDER BY year, month, day DESC", year, month, day, rezervuota, yes)

            return render_template("/visos_neaprasytos_konsultacijos.html", rows=rows)
    else:
        return render_template("/index.html")

@app.route("/ivesti_kalendoriu", methods=["GET", "POST"])
@login_required
def ivesti_kalendoriu():
    if session["user_type"] == "ADM":
        if request.method=="GET":
            return render_template("/ivesti_kalendoriu.html")

        if request.method=="POST":
            year = request.form.get("year")
            month = request.form.get("month")
            kab = request.form.get("kab")

            if not request.form.get("booked"):
                booked = "Laisva"

            days = []
            day1 = request.form.get("1")
            if day1 != None:
                days.append(day1)

            day2 = request.form.get("2")
            if day2 != None:
                days.append(day2)

            day3 = request.form.get("3")
            if day3 != None:
                days.append(day3)

            day4 = request.form.get("4")
            if day4 != None:
                days.append(day4)

            day5 = request.form.get("5")
            if day5 != None:
                days.append(day5)

            day6 = request.form.get("6")
            if day6 != None:
                days.append(day6)

            day7 = request.form.get("7")
            if day7 != None:
                days.append(day7)

            day8 = request.form.get("8")
            if day8 != None:
                days.append(day8)

            day9 = request.form.get("9")
            if day9 != None:
                days.append(day9)

            day10 = request.form.get("10")
            if day10 != None:
                days.append(day10)

            day11 = request.form.get("11")
            if day11 != None:
                days.append(day11)

            day12 = request.form.get("12")
            if day12 != None:
                days.append(day12)

            day13 = request.form.get("13")
            if day13 != None:
                days.append(day13)

            day14 = request.form.get("14")
            if day14 != None:
                days.append(day14)

            day15 = request.form.get("15")
            if day15 != None:
                days.append(day15)

            day16 = request.form.get("16")
            if day16 != None:
                days.append(day16)

            day17 = request.form.get("17")
            if day17 != None:
                days.append(day17)

            day18 = request.form.get("18")
            if day18 != None:
                days.append(day18)

            day19 = request.form.get("19")
            if day19 != None:
                days.append(day19)

            day20 = request.form.get("20")
            if day20 != None:
                days.append(day20)

            day21 = request.form.get("21")
            if day21 != None:
                days.append(day21)

            day22 = request.form.get("22")
            if day22 != None:
                days.append(day22)

            day23 = request.form.get("23")
            if day23 != None:
                days.append(day23)

            day24 = request.form.get("24")
            if day24 != None:
                days.append(day24)

            day25 = request.form.get("25")
            if day25 != None:
                days.append(day25)

            day26 = request.form.get("26")
            if day26 != None:
                days.append(day26)

            day27 = request.form.get("27")
            if day27 != None:
                days.append(day27)

            day28 = request.form.get("28")
            if day28 != None:
                days.append(day28)

            day29 = request.form.get("29")
            if day29 != None:
                days.append(day29)

            day30 = request.form.get("30")
            if day30 != None:
                days.append(day30)

            day31 = request.form.get("31")
            if day31 != None:
                days.append(day31)

            hours = []
            hour9 = request.form.get("9val")
            if hour9 != None:
                hours.append(hour9)

            hour10 = request.form.get("10val")
            if hour10 != None:
                hours.append(hour10)

            hour11 = request.form.get("11val")
            if hour11 != None:
                hours.append(hour11)

            hour12 = request.form.get("12val")
            if hour12 != None:
                hours.append(hour12)

            hour13 = request.form.get("13val")
            if hour13 != None:
                hours.append(hour13)

            hour14 = request.form.get("14val")
            if hour14 != None:
                hours.append(hour14)

            hour15 = request.form.get("15val")
            if hour15 != None:
                hours.append(hour15)

            hour16 = request.form.get("16val")
            if hour16 != None:
                hours.append(hour16)

            hour17 = request.form.get("17val")
            if hour17 != None:
                hours.append(hour17)

            length_days = len(days)
            length_hours = len(hours)
            client = "-"

            for j in range(length_days):
                day = days[j]
                for k in range(length_hours):
                    hour = hours[k]
                    db.execute("INSERT INTO kalendorius (year, month, cabinet, day, time, booked, client) VALUES (%s, %s, %s, %s, %s, %s, %s)", year, month, kab, day, hour, booked, client)

            flash("Kalendorius papildytas nurodytomis dienomis ir laikais!")

            return render_template("/index.html")
    else:
        return render_template("/index.html")

@app.route("/registruoti", methods=["GET", "POST"])
@login_required
def register():
    if session["user_type"] == "ADM":
        if request.method=="GET":
            return render_template("/registruoti.html")

        else:
            username = request.form.get("username")
            if not request.form.get("username"):
                return apology("nurodykite vartotojo vardą", 403)

            rows = db.execute("SELECT * FROM vartotojai WHERE username = :username",username=request.form.get("username"))
            if len(rows) != 0:
                if rows[0]["username"] == username:
                    return apology("toks vartotojas jau yra", 403)

            password = request.form.get("password")
            if not request.form.get("password"):
                return apology("nurodykite slaptažodį", 403)

            password_again = request.form.get("password_again")
            if not request.form.get("password_again"):
                return apology("nurodykite slaptažodį dar kartą", 403)

            if request.form.get("password") != request.form.get("password_again"):
                return apology("nesutampa slaptažodžiai", 403)

            name = request.form.get("name")
            if not request.form.get("name"):
                return apology("nurodykite asmens vardą", 403)

            surname = request.form.get("surname")
            if not request.form.get("surname"):
                return apology("nurodykite asmens pavardę", 403)

            phone = request.form.get("phone")
            if not request.form.get("phone"):
                return apology("nurodykite telefono numerį", 403)

            email = request.form.get("email")
            if not request.form.get("email"):
                return apology("nurodykite el. pašo adresą", 403)

            type1 = request.form.get("tipas")
            if not request.form.get("tipas"):
                return apology("pasirinkite vartotojo tipą", 403)

            hash = generate_password_hash(password)

            db.execute("INSERT INTO vartotojai (username, name, surname, phone, email, hash, type) VALUES (:username, :name, :surname, :phone, :email, :hash, :type)", username=username, name=name, surname=surname, phone=phone, email=email, type=type1, hash=hash)

            flash("Vartotojas užregistruotas!")

            #Redirect user to home page
            return redirect("/")
    else:
        return render_template("/index.html")

@app.route("/po_konsultacijos", methods=["GET", "POST"])
@login_required
def po_konsultacijos():
    if request.method=="GET":
        return render_template("/po_konsultacijos.html")

    if request.method=="POST":
        id = session["user_id"]

        client_name = request.form.get("client_name")
        client_surname = request.form.get("client_surname")
        consultation_date = request.form.get("consultation_date")
        consultation_time = request.form.get("consultation_time")
        consultation_duration = request.form.get("consultation_duration")
        consultation_type = request.form.get("consultation_type")
        consultation_price= request.form.get("consultation_price")
        comments = request.form.get("comments")

        db.execute("INSERT INTO po_konsultacijos (user_id, client_name, client_surname, consultation_date, consultation_time, consultation_duration, consultation_type, consultation_price, comments) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", session["user_id"], client_name, client_surname, consultation_date, consultation_time, consultation_duration, consultation_type, consultation_price, comments)

        consultation_date = request.form.get("consultation_date")
        consultation_time = request.form.get("consultation_time")
        date = datetime.strptime(consultation_date, '%Y-%m-%d')
        year = date.year
        month = date.month
        day = date.day

        if consultation_time == "09:00":
            consultation_time = "09:00 - 10:00"

        if consultation_time == "10:00":
            consultation_time = "10:00 - 11:00"

        if consultation_time == "11:00":
            consultation_time = "11:00 - 12:00"

        if consultation_time == "12:00":
            consultation_time = "12:00 - 13:00"

        if consultation_time == "13:00":
            consultation_time = "13:00 - 14:00"

        if consultation_time == "14:00":
            consultation_time = "14:00 - 15:00"

        if consultation_time == "15:00":
            consultation_time = "15:00 - 16:00"

        if consultation_time == "16:00":
            consultation_time = "16:00 - 17:00"

        if consultation_time == "17:00":
            consultation_time = "17:00 - 18:00"

        yes = "Taip"

        # return render_template("test.html", consultation_date=consultation_date, date=date, year=year, month=month, day=day)

        if consultation_duration == "1":
            db.execute("UPDATE kalendorius SET reported = %s WHERE year = %s AND month = %s AND day = %s AND time = %s AND user_id = %s", yes, year, month, day, consultation_time, session["user_id"])

        if consultation_duration == "2":

            if consultation_time == "09:00 - 10:00":
                second_hour = "10:00 - 11:00"

            if consultation_time == "10:00 - 11:00":
               second_hour = "11:00 - 12:00"

            if consultation_time == "11:00 - 12:00":
                second_hour = "12:00 - 13:00"

            if consultation_time == "12:00 - 13:00":
                second_hour = "13:00 - 14:00"

            if consultation_time == "13:00 - 14:00":
                second_hour = "14:00 - 15:00"

            if consultation_time == "14:00 - 15:00":
                second_hour = "15:00 - 16:00"

            if consultation_time == "15:00 - 16:00":
                second_hour = "16:00 - 17:00"

            if consultation_time == "16:00 - 17:00":
                second_hour = "17:00 - 18:00"

            db.execute("UPDATE kalendorius SET reported = %s WHERE year = %s AND month = %s AND day = %s AND time = %s AND user_id = %s", yes, year, month, day, consultation_time, session["user_id"])
            db.execute("UPDATE kalendorius SET reported = %s WHERE year = %s AND month = %s AND day = %s AND time = %s AND user_id = %s", yes, year, month, day, second_hour, session["user_id"])

        flash("Duomenys apie konsultaciją įvesti!")

        #Redirect user to home page
        return redirect("/")

@app.route("/mano")
@login_required
def mano():
    rows = db.execute("SELECT * FROM vartotojai WHERE id = %s", session["user_id"])
    name = rows[0]["name"]
    surname = rows[0]["surname"]
    phone = rows[0]["phone"]
    email = rows[0]["email"]

    return render_template("/mano.html", name=name, surname=surname, phone=phone, email=email)

@app.route("/redaguoti_mano", methods=["GET", "POST"])
@login_required
def redaguoti_mano():
    if request.method=="GET":
        return render_template("/redaguoti_mano.html")

    else:
        name = request.form.get("name")
        if not request.form.get("name"):
            return apology("nurodykite asmens vardą", 403)

        surname = request.form.get("surname")
        if not request.form.get("surname"):
            return apology("nurodykite asmens pavardę", 403)

        phone = request.form.get("phone")
        if not request.form.get("phone"):
            return apology("nurodykite telefono numerį", 403)

        email = request.form.get("email")
        if not request.form.get("email"):
            return apology("nurodykite el. pašo adresą", 403)

        db.execute("UPDATE vartotojai SET name = %s, surname = %s, phone = %s, email = %s WHERE id = %s", name, surname, phone, email, session["user_id"])

        flash("Duomenys atnaujinti!")

        #Redirect user to home page
        return redirect("/mano")

@app.route("/keisti_slaptazodi", methods=["GET", "POST"])
@login_required
def keisti_slaptazodi():
    if request.method=="GET":
        return render_template("/keisti_slaptazodi.html")

    else:
        if request.method=="POST":

            hash_db = db.execute("SELECT hash FROM vartotojai WHERE username = %s", session["user_id"])

            if check_password_hash(hash_db, request.form.get("password")):
                return apology("neteisingas slaptažodis", 403)

            password_new = request.form.get("password_new")
            if not request.form.get("password_new"):
                return apology("nurodykite naują slaptažodį", 403)

            password_new_again = request.form.get("password_new_again")
            if not request.form.get("password_new_again"):
                return apology("nurodykite naują slaptažodį du kartus", 403)

            if password_new != password_new_again:
                return apology("nauji slaptažodžiai skiriasi", 403)

            hash = generate_password_hash(password_new)

            db.execute("UPDATE vartotojai SET hash = %s WHERE id = %s", hash, session["user_id"])

            flash("Slaptažodis pakeistas!")

            return redirect("/")

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

