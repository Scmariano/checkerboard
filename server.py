from flask import Flask, render_template  
app = Flask(__name__)  

@app.route('/')
def index():
    return render_template("index.html",row=8,col=8,first_color= "red",second_color= "black")

@app.route('/<int:row>')
def box(row):
    return render_template("index.html",row=row,col=8,first_color= "red",second_color= "black")

@app.route('/<int:row>/<int:col>')
def box2(row, col):
    return render_template("index.html",row=row,col=col,first_color= "red",second_color= "black")

@app.route('/<int:row>/<int:col>/<string:color>')
def color1(row, col, color ):
    return render_template("index.html",row=row,col=col,first_color=color,second_color= "black")

@app.route('/<int:row>/<int:col>/<string:first_color>/<string:second_color>')
def color2(row, col, first_color, second_color ):
    return render_template("index.html",row=row,col=col,first_color=first_color,second_color= second_color)

if __name__=="__main__":      
    app.run(debug=True)    