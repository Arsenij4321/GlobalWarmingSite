from flask import Flask, render_template, request
import random


app = Flask(__name__)

advice_list = [
    "Перейдите на импользование возобновлякмых источников энергии.",
    "Снижайте потребление пластика, используйте многоразовые товары.",
    "Делитесь советами с друзьями и знакомыми.",
    "Используейте энергосберегающие лампочки и бытовые приборы.",
    "По возможности используйте общественный транспорт или велосипед вместо автомобиля."
]
@app.route('/', methods=['GET','POST'])
def index():
    advice = None
    if request.method == "POST":
        advice = random.choice(advice_list)
    return render_template('index.html', advice=advice)

if __name__ == '__main__':
    app.run(debug=True)