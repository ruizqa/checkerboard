from flask import Flask, render_template

app = Flask(__name__)   

@app.route('/', defaults={'x':8, 'y':8,'col1':'black','col2':'red'})          
@app.route('/<int:x>', defaults={'y':8,'col1':'black','col2':'red'})
@app.route('/<int:x>/<int:y>', defaults={'col1':'black','col2':'red'})
@app.route('/<int:x>/<int:y>/<string:col1>', defaults={'col2':'red'})
@app.route('/<int:x>/<int:y>/<string:col1>/<string:col2>')
def show_boxes(x,y,col1,col2):
    return render_template("index.html",x=x, y=y,col1=col1,col2=col2)
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.