from flask import Flask, jsonify, request

app = Flask(__name__)

tickets = []

@app.route("/")
def home():
    return jsonify({
        "message": "Enterprise Portal API", "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "operational"
    })

@app.route("/api/employee")
def employee():
    return jsonify({
        "name": "Test Employee", "department": "IT", "role": "Employee"
        })

@app.route("/api/tickets", methods=["GET"])
def get_tickets():
    return jsonify(tickets)

@app.route("/api/tickets", methods=["POST"])
def create_tickets():
    data = request.get_json()

    if not data or not data.get("problem"):
        return jsonify({
        "error": "Problem description is required"
    }), 400

    ticket = {
        "id": len(tickets) + 1,
        "problem": data["problem"],
        "priority": data.get("priority", "Low"),
        "status": "Open"
    }

    tickets.append(ticket)

    return jsonify(ticket),201

if __name__ == '__main__':
    app.run(debug=True)