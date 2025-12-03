from flask import Blueprint, render_template, request, redirect, url_for, flash
from database import get_db
from database_functions import *
import random

mathmagician_bp = Blueprint("mathmagician", __name__)


@mathmagician_bp.route("/maths")
def index():
    # Get current xp (successes) and xp to level up (attempts)
    db = get_db()
    cursor = db.cursor()
    nextlevel, currentxp = get_xp_and_level()

    if nextlevel == 0:
        cursor.execute("UPDATE stats SET attempts = attempts + 1000 WHERE id = 'xp'")
        db.commit()

    if currentxp > nextlevel:
        # Increase xp for nextlevel 
        cursor.execute("UPDATE stats SET attempts = attempts + 1000 WHERE id = 'xp'")
        db.commit()
        nextlevel += 1000
                    
    # Calculate level (for template to render users rank and "profile picture")
    level = currentxp // 1000

    ranks = ["Apprentice", "Magician", "Mage", "Grand Mage", "Archmage"]

    if level < len(ranks):
        rank = ranks[level]
    else:
        rank = ranks[len(ranks)-1]

    db.close()
    return render_template("mathmagician.html", nextlevel=nextlevel, currentxp=currentxp, rank=rank)

class Matrix():
    def __init__(self):
        self.new_random_matrix()
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])


    def new_random_matrix(self):
        self.rows = random.randint(2, 3)
        self.columns = random.randint(2, 3)
        # Create new matrix
        self.matrix = []
        for row in range(self.rows):
            self.matrix.append([])
            for column in range(self.columns):
                self.matrix[row].append(random.randint(0, 9))


    def multiply(self, m2):
        #if self.columns == m2.rows:

        m3 = Matrix()
        m3.matrix = []
        for row in range(self.rows):
            m3.matrix.append([])
            for column in range(m2.columns):
                value = 0
                for element in range(self.columns): #or in range m2.rows
                    value += (self.matrix[row][element] * m2.matrix[element][column]) 
                m3.matrix[row].append(value)

        m3.rows = self.rows
        m3.columns = m2.columns
        return m3

class MultipliedMatrix(Matrix):
    def __init__(self, m1c):
        self.matrix = self.new_random_matrix(m1c)
        self.rows = m1c # First matrix's number of columns, this is so that they can be multiplied
        self.columns = len(self.matrix[0])

    def new_random_matrix(self, m1c):
        self.rows = m1c 
        self.columns = random.randint(2, 3)
        # Create new matrix
        self.matrix = []
        for row in range(self.rows):
            self.matrix.append([])
            for column in range(self.columns):
                self.matrix[row].append(random.randint(0, 9))

        return self.matrix


@mathmagician_bp.route("/mm", methods=["GET", "POST"])
def mm():
    if request.method == "POST":
        db = get_db()
        cursor = db.cursor()

        if "mm-correct" in request.form:
            cursor.execute("UPDATE stats SET attempts = attempts +1 , successes = successes + 1 WHERE id = 'mm'")
            cursor.execute("UPDATE stats SET successes = successes + 10 WHERE id = 'xp'")
            db.commit()
            nextlevel, currentxp = get_xp_and_level()
            flash("Matrix Multiplication spell successful! +10 mana")
        
        if "mm-incorrect" in request.form:
            cursor.execute("UPDATE stats SET attempts = attempts +1 WHERE id = 'mm'")
            cursor.execute("UPDATE stats SET successes = successes + 5 WHERE id = 'xp'")
            db.commit()
            nextlevel, currentxp = get_xp_and_level()
            flash("Matrix Multiplication spell failed! +5 mana")

        if "mm-reset" in request.form:
            cursor.execute("UPDATE stats SET attempts = 0, successes = 0 WHERE id = 'mm'")
            db.commit()
            nextlevel, currentxp = get_xp_and_level()
            flash("Matrix spell statistics reset.")
            
        db.commit()
        db.close()      

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT attempts, successes FROM stats WHERE id = 'mm'")
    stats = cursor.fetchone()
    attempts = stats[0]
    successes = stats[1]
    
    db.commit()
    db.close()

    m1 = Matrix()
    m2 = MultipliedMatrix(m1.columns)
    m3 = m1.multiply(m2)

    nextlevel, currentxp = get_xp_and_level()

    return render_template("mm.html", m1=m1, m2=m2, m3=m3, attempts=attempts, successes=successes, nextlevel=nextlevel, currentxp=currentxp)


@mathmagician_bp.route("/eli", methods=["GET", "POST"])
def eli():
    if request.method == "POST":
        db = get_db()
        cursor = db.cursor()

        if "eli-correct" in request.form:
            cursor.execute("UPDATE stats SET attempts = attempts +1 , successes = successes + 1 WHERE id = 'eli'")
            cursor.execute("UPDATE stats SET successes = successes + 10 WHERE id = 'xp'")
            db.commit()
            nextlevel, currentxp = get_xp_and_level()
            flash("Easy integration spell successful! +10 mana")
        
        if "eli-incorrect" in request.form:
            cursor.execute("UPDATE stats SET attempts = attempts +1 WHERE id = 'eli'")
            cursor.execute("UPDATE stats SET successes = successes + 5 WHERE id = 'xp'")
            db.commit()
            nextlevel, currentxp = get_xp_and_level()
            flash("Easy integration spell successful! +5 mana")

        if "eli-reset" in request.form:
            cursor.execute("UPDATE stats SET attempts = 0, successes = 0 WHERE id = 'eli'")
            db.commit()
            nextlevel, currentxp = get_xp_and_level()
            flash("Easy integration spell statistics reset.")
            
        
        db.commit()
        db.close()      

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT attempts, successes FROM stats WHERE id = 'eli'")
    stats = cursor.fetchone()
    attempts = stats[0]
    successes = stats[1]
    
    db.commit()
    db.close()

    nextlevel, currentxp = get_xp_and_level()
    le = LinearEquation()
    return render_template("eli.html", m=le.m, c=le.c, mo2=le.mo2, attempts=attempts, successes=successes, nextlevel=nextlevel, currentxp=currentxp)

class LinearEquation():
    def __init__(self):
        self.m = random.randint(2, 6)
        self.c = random.randint(1, 20)
        self.mo2 = self.m/2


@mathmagician_bp.route("/eqd", methods=["GET", "POST"])
def eqd():
    if request.method == "POST":
        db = get_db()
        cursor = db.cursor()

        if "eqd-correct" in request.form:
            cursor.execute("UPDATE stats SET attempts = attempts +1 , successes = successes + 1 WHERE id = 'eqd'")
            cursor.execute("UPDATE stats SET successes = successes + 10 WHERE id = 'xp'")
            db.commit()
            nextlevel, currentxp = get_xp_and_level()
            flash("Easy quadratic differentiation spell successful! +10 mana")
        
        if "eqd-incorrect" in request.form:
            cursor.execute("UPDATE stats SET attempts = attempts +1 WHERE id = 'eqd'")
            cursor.execute("UPDATE stats SET successes = successes + 5 WHERE id = 'xp'")
            db.commit()
            nextlevel, currentxp = get_xp_and_level()
            flash("Easy quadratic differentiation spell failed! +5 mana")

        if "eqd-reset" in request.form:
            cursor.execute("UPDATE stats SET attempts = 0, successes = 0 WHERE id = 'eqd'")
            db.commit()
            nextlevel, currentxp = get_xp_and_level()
            flash("Easy quadratic differentiation spell statistics reset.")
        
        db.commit()
        db.close()      

    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT attempts, successes FROM stats WHERE id = 'eqd'")
    stats = cursor.fetchone()
    attempts = stats[0]
    successes = stats[1]
    
    db.commit()
    db.close()
    nextlevel, currentxp = get_xp_and_level()
    qe = QuadraticEquation()
    return render_template("eqd.html", a=qe.a, b=qe.b, c=qe.c, an=qe.an, attempts=attempts, successes=successes, nextlevel=nextlevel, currentxp=currentxp)

class QuadraticEquation():
    def __init__(self):
        self.a = random.randint(2, 6)
        self.b = random.randint(1, 20)
        self.c = random.randint(1, 20)
        self.an = 2*self.a


