
from flask import Flask, request

app = Flask(__name__)

available_cars = {
    "Toyota": {
        "Camry": {"model_year": 2022, "price_per_day": 50},
        "Corolla": {"model_year": 2021, "price_per_day": 45},
        "Rav4": {"model_year": 2020, "price_per_day": 55}
    },
    "Honda": {
        "Civic": {"model_year": 2022, "price_per_day": 40},
        "Accord": {"model_year": 2021, "price_per_day": 50},
        "CR-V": {"model_year": 2020, "price_per_day": 60}
    },
    "Ford": {
        "Mustang": {"model_year": 2022, "price_per_day": 60},
        "Fusion": {"model_year": 2021, "price_per_day": 45},
        "Escape": {"model_year": 2020, "price_per_day": 55}
    }
}

rented_cars = [] 


def generate_car_options():
    options = ""
    for brand, models in available_cars.items():
        for model in models:
            options += f"<option value='{brand}:{model}'>{brand} - {model}</option>"
    return options


@app.route('/')
def home():
    car_options = generate_car_options()

    html = f"""
        <html>
        <head>
            <title>Car Rental Service</title>
            <style>
                body {{
                    background-color: #F5F5F5;
                    padding: 20px;
                }}
                
                h1 {{
                    color: #333333;
                }}
                
                form {{
                    background-color: #FFFFFF;
                    border-radius: 5px;
                    padding: 20px;
                }}
                
                label {{
                    display: block;
                    margin-bottom: 10px;
                }}
                
                select,
                input[type='number'] {{
                    padding: 10px;
                    border-radius: 5px;
                    border: 1px solid #AAAAAA;
                    width: 200px;
                    margin-bottom: 10px;
                }}
                
                input[type='submit'] {{
                    background-color: #4CAF50;
                    color: #FFFFFF;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 5px;
                    cursor: pointer;
                }}
            </style>
        </head>
        <body>
            <h1>Available Cars:</h1>
            <form action='/rent' method='post'>
                <fieldset>
                    <legend>Car Rental Form</legend>
                    <div>
                        <label for='car'>Select a car:</label>
                        <select name='car' id='car'>
                            {car_options}
                        </select>
                    </div>
                    <div>
                        <label for='days'>Enter number of days for rental (1-365):</label>
                        <input type='number' id='days' name='days' min='1' max='365'>
                    </div>
                    <div>
                        <label for='insurance'>Do you want insurance?</label>
                        <select name='insurance_choice' id='insurance'>
                            <option value='full'>Full</option>
                            <option value='half'>Half</option>
                            <option value='none'>None</option>
                        </select>
                    </div>
                    <div>
                        <input type='submit' value='Rent'>
                    </div>
                </fieldset>
            </form>
        </body>
        </html>
    """

    return html


def calculate_total_cost(brand, model, days, insurance_choice):
    if brand in available_cars and model in available_cars[brand]:
        price_per_day = available_cars[brand][model]["price_per_day"]
        total_cost = price_per_day * days
        if insurance_choice == "full":
            insurance_price_per_day = 10
            insurance_cost = insurance_price_per_day * days
            total_cost += insurance_cost
        elif insurance_choice == "half":
            insurance_price_per_day = 5
            insurance_cost = insurance_price_per_day * days
            total_cost += insurance_cost
        else:
            insurance_cost = 0
        return total_cost, insurance_cost
    else:
        return None, None


total_revenue = lambda rented_cars: sum(cost + insurance_cost for cost, insurance_cost in rented_cars)


@app.route('/rent', methods=['POST'])
def rent():
    selected_car = request.form['car']
    brand, model = selected_car.split(':')
    days = int(request.form['days'])
    insurance_choice = request.form['insurance_choice']

    total_cost, insurance_cost = calculate_total_cost(brand, model, days, insurance_choice)

    if total_cost is not None:
        rented_cars.append((total_cost, insurance_cost))
        return f"<h1>Thank you for renting a {brand} {model}!</h1>" \
               f"<p>Total cost: ${total_cost}</p>" \
               f"<p>Insurance cost: ${insurance_cost}</p>" \
               f"<p>Total revenue: ${total_revenue(rented_cars)}</p>"
    else:
        return "<h1>Invalid car selection! Please try again.</h1>"


if __name__ == '__main__':
    app.run(debug=True)
 