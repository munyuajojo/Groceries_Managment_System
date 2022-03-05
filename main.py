from flask import Flask, render_template, request, flash, redirect, url_for, flash
#from sassutils.wsgi import SassMiddleware


app = Flask(__name__)


#app.wsgi_app = SassMiddleware(app.wsgi_app, {
 #   'myapp': ('static/sass', 'static/css', '/static/css')
#})


@app.route('/')
def index():
    return render_template("/landing/index.html")


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    return render_template("/landing/cart.html")

if __name__ =="__main__":

    app.run(debug = True)
