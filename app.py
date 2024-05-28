from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for orders and couriers
orders = []
couriers = []

@app.route('/')
def home():
    return "Welcome to Pi Express!"

@app.route('/register_courier', methods=['POST'])
def register_courier():
    data = request.json
    couriers.append({
        'id': len(couriers) + 1,
        'name': data['name'],
        'vehicle': data['vehicle'],
        'location': data['location']
    })
    return jsonify({'message': 'Courier registered successfully!', 'courier': couriers[-1]}), 201

@app.route('/create_order', methods=['POST'])
def create_order():
    data = request.json
    orders.append({
        'id': len(orders) + 1,
        'details': data['details'],
        'pickup_location': data['pickup_location'],
        'dropoff_location': data['dropoff_location'],
        'payment': 'Pi',
        'status': 'pending'
    })
    return jsonify({'message': 'Order created successfully!', 'order': orders[-1]}), 201

@app.route('/list_orders', methods=['GET'])
def list_orders():
    return jsonify(orders), 200

@app.route('/accept_order/<int:order_id>', methods=['POST'])
def accept_order(order_id):
    for order in orders:
        if order['id'] == order_id:
            order['status'] = 'accepted'
            return jsonify({'message': 'Order accepted!', 'order': order}), 200
    return jsonify({'message': 'Order not found!'}), 404

if __name__ == '__main__':
    app.run(debug=True)
