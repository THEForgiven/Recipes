from flask import Flask, render_template, request, send_file
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        directions = request.form['directions']

        filename = f"{title}.pdf"
        file_path = os.path.join("/home/myname/Downloads/Recipes", filename)
        create_pdf(file_path, title, ingredients, directions)

        return send_file(file_path, as_attachment=True)

    return render_template('index.html')

def create_pdf(file_path, title, ingredients, directions):
    c = canvas.Canvas(file_path, pagesize=letter)

    c.setFont('Helvetica', 24)
    c.drawString(50, 750, title)

    c.setFont('Helvetica', 16)
    c.drawString(50, 700, 'Ingredients:')
    y = 675
    for ingredient in ingredients.split('\n'):
        c.drawString(70, y, ingredient)
        y -= 20

    c.drawString(50, y-25, 'Directions:')
    y -= 50
    for direction in directions.split('\n'):
        c.drawString(70, y, direction)
        y -= 20

    c.save()

if __name__ == '__main__':
    app.run(debug=True)
