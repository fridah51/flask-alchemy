from flask import Flask, render_template ,request,redirect ,flash,session
from flask_login import LoginManager, login_user, login_required,  logout_user, current_user
from functools import wraps 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import  Numeric, DateTime, func,extract
from flask.helpers import url_for
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime,date,time

from config.config import  Production ,Development  

app = Flask(__name__)
db = SQLAlchemy(app)
app.config.from_object(Production)

from models.inventory import Products
from models.salesinv import Sales
from models.stock import Stock
from models.users import User

@app.before_first_request
def create_tables():
    #db.drop_all()
    db.create_all()
    
    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))
    


@app.route('/')
def home():
    
    #return html file
    return render_template('index.html' )


@app.route('/login')
def login():
    
    return render_template('login.html' )

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/signup')
def signup():
    
    return render_template('sign-up.html' )

@app.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
    
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('login'))

@app.route('/login', methods=['POST'])
def login_post():
   
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('home'))


@app.route('/inventory')
@login_required
def inventory():

    # #query the database and obtain data as python 
    records =Products.query.all()

    #call sql driver and pull/get data
    return render_template('inventory.html',name=current_user.name, myData=records)

@app.route('/stock')
def stock():

    records =Stock.query.all()
    return render_template('stock.html',myStock=records)


@app.route('/sales/<int:id>')
def view_sales(id):
   
    #cur.execute('SELECT * FROM sales WHERE product_id=%s;',[pid])
    recordss = Sales.query.filter_by(product_id =id)
    
    return render_template('sales.html',mySales=recordss)

@app.route('/stock/<int:id>')
def view_stock(id):
   
    #cur.execute('SELECT * FROM sales WHERE product_id=%s;',[pid])
    recordss = Stock.query.filter_by(product_id =id)
    
    return render_template('stock.html',myStock=recordss)



@app.route('/save_products',methods=['post','get'])
def save_products():

    name =request.form['name']
    bp = request.form['bp']
    sp = request.form['sp']
    
    
    rows = Products(name=name,bp=bp,sp=sp)
    db.session.add(rows)
    db.session.commit()

    return redirect('/inventory')


@app.route('/make_sale',methods=['post','get'])
def make_sale():

    # query = """INSERT INTO sales (quantity,product_id,created_at) VALUES (%s,%s,%s)"""
    quantity = request.form['quantity']
    id = request.form['product_id']
    created_at ='NOW()'
   
    rows = Sales(quantity = quantity,product_id=id,created_at=created_at)
    db.session.add(rows)  
    db.session.commit()
    
    return redirect('/inventory')

@app.route('/add_stock',methods=['post','get'])
def add_stock():

    quantity = request.form['quantity']
    product_id = request.form['product_id']
    created_at ='NOW()'
   
    rows = Stock(quantity = quantity,product_id=product_id,created_at=created_at)
    db.session.add(rows)  
    db.session.commit()
    
    return redirect('/inventory')


@app.route('/edit_item',methods=['post','get'])
def edit_item():

    #query = """UPDATE products SET name = %s,bp=%s,sp=%s,serial_no=%s WHERE id=%s """  
    pid = request.form['pid']
    row = Products.query.filter_by(id = pid).one()
    row.name = request.form['pname']
    row.bp = request.form['pbp']
    row.sp = request.form['psp']
      
    db.session.merge(row)   
    db.session.commit()

    return redirect('/inventory')

@app.route('/delete_item',methods=['post','get'])
def delete_item():

    pid = request.form['product_id']
    row = Products.query.filter_by(id = pid).one()
     
    db.session.delete(row)
    db.session.commit()

    return redirect('/inventory')


@app.route('/dashboard')
def dashboard():
    
    #query the database and obtain sales per month as python 
#   cur.execute("SELECT extract(month from s.created_at) AS monthly,sum(s.quantity * p.sp) AS sales FROM sales s JOIN products p ON p.id = s.product_id GROUP BY monthly ORDER BY monthly ;")
#   spm = cur.fetchall()
    spm = Sales.query.with_entities(func.sum(Sales.quantity * Products.sp), extract('month',Sales.created_at)).join(Products).group_by( extract('month',Sales.created_at)) 
    #convert spm to how chartjs expects
    monthspm=[]
    dataspm=[]
    for x in spm :
        monthspm.append(x[1])
        dataspm.append(int(x[0]))
    print("dataspm" ,dataspm )
        
#   cur.execute(" SELECT sum(s.quantity * p.sp) AS sales, p.name FROM sales s JOIN products p ON p.id = s.product_id GROUP BY p.name ;")
    sbp = Sales.query.with_entities(func.sum(Sales.quantity * Products.sp), Products.name).join(Products).group_by(Products.name ).order_by(func.sum(Sales.quantity * Products.sp))
    
    namesbp=[]
    salesbp=[]
    for x in sbp:
        namesbp.append(x[1])
        salesbp.append(float(x[0])) 
    print(salesbp) 
  
#   cur.execute("SELECT sum(s.quantity * p.sp) AS sales,DATE(created_at) AS today FROM sales s JOIN products p ON p.id = s.product_id WHERE DATE(created_at) = current_date GROUP BY today;")
    ds =  Sales.query.with_entities(func.sum(Sales.quantity * Products.sp),func.date(Sales.created_at)).join(Products).filter(func.date(Sales.created_at) == date.today()).group_by(func.date(Sales.created_at)) 
                
    dailys = 0
    today = []
    for i in ds:
        dailys=(float(i[0]))
        today=(i[1])
    print(dailys)
    
#   monthly sales
    ms = Sales.query.with_entities(func.sum(Sales.quantity * Products.sp),extract('month',Sales.created_at)).join(Products).filter(extract('month',Sales.created_at) == date.today().month).group_by(extract('month',Sales.created_at)) 
    monthsales = 0
    thismonth = []
    for i in ms:
        monthsales=(float(i[0]))
        thismonth=(i[1])
    print(monthsales)


#   profit per month   
#   cur.execute("SELECT sum(p.sp - p.bp) AS profit,extract(month from s.created_at) AS monthly FROM sales s JOIN products p ON p.id = s.product_id GROUP BY monthly ORDER BY monthly ;")

    
#   cur.execute('SELECT p.name,sum(s.quantity) AS most_sold FROM sales s JOIN products p ON p.id = s.product_id GROUP BY p.name ORDER BY (sum(s.quantity)) DESC LIMIT 5;')
    prod=[]
    data5=[]
    top5 = Sales.query.with_entities(Products.name, func.sum(Sales.quantity)).join(Products ).group_by(Products.name ).order_by(func.sum(Sales.quantity)).limit(5) 
    
    for i in top5:
        prod.append(i[0])
        data5.append(int(i[1]))
    print(data5)
        
        
    #return html file   
    return render_template('dashboard.html',prod=prod,data5=data5,dailys = dailys,today=today,monthspm=monthspm,dataspm=dataspm,namesbp=namesbp,salesbp= salesbp,monthsales=monthsales,thismonth=thismonth)



if __name__ == '__main__':
    app.run(debug=True)