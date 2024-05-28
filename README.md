# Pi-Express-Project-APP
Pi Express is a delivery platform for couriers who accept Pi currency as payment.

## Features

- Register couriers with their details.
- Create delivery orders with pickup and dropoff locations.
- List all delivery orders.
- Accept orders for delivery.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your_username/pi_express_app.git
    cd pi_express_app
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```sh
    pip install Flask
    ```

4. Run the app:
    ```sh
    python app.py
    ```

## API Endpoints

- `GET /` - Welcome message
- `POST /register_courier` - Register a new courier (expects JSON with `name`, `vehicle`, `location`)
- `POST /create_order` - Create a new order (expects JSON with `details`, `pickup_location`, `dropoff_location`)
- `GET /list_orders` - List all orders
- `POST /accept_order/<int:order_id>` - Accept an order by ID

## Example Request

```sh
curl -X POST http://127.0.0.1:5000/register_courier -H "Content-Type: application/json" -d '{"name": "LATHALA", "vehicle": "motorcycle", "location": "DAVAO"}'
```

## Contributing

Feel free to make a pull request or report any issues.

## License

This project is licensed under the MIT License.

You can now copy the provided code and README file to your GitHub repository.
