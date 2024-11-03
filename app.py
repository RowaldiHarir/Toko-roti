from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from datetime import datetime

app = Flask(__name__)
api = Api(app)

# Data awal roti (total 15) dengan detail lengkap
breads = {
    "1": {
        "name": "Roti Tawar",
        "type": "White Bread",
        "quantity": 50,
        "price": 20000,
        "bakery": "Bakery A",
        "production_date": "2024-01-15",
        "category": "Bread"
    },
    "2": {
        "name": "Roti Gandum",
        "type": "Whole Wheat Bread",
        "quantity": 30,
        "price": 25000,
        "bakery": "Bakery B",
        "production_date": "2024-01-10",
        "category": "Bread"
    },
    "3": {
        "name": "Croissant",
        "type": "Pastry",
        "quantity": 20,
        "price": 30000,
        "bakery": "Bakery C",
        "production_date": "2024-01-12",
        "category": "Pastry"
    }
    # Tambahkan data produk roti lainnya jika diperlukan
}

# Endpoint untuk mendapatkan daftar roti
class BreadList(Resource):
    def get(self):
        return jsonify(breads)

# Endpoint untuk mendapatkan roti berdasarkan ID
class Bread(Resource):
    def get(self, bread_id):
        bread = breads.get(bread_id)
        if bread:
            return jsonify(bread)
        else:
            return {"message": "Roti tidak ditemukan"}, 404

    def post(self, bread_id):
        if bread_id in breads:
            return {"message": f"Roti dengan ID {bread_id} sudah ada"}, 400
        else:
            data = request.get_json()
            breads[bread_id] = data
            return data, 201

    def put(self, bread_id):
        data = request.get_json()
        if bread_id in breads:
            breads[bread_id].update(data)
            return jsonify(breads[bread_id])
        else:
            breads[bread_id] = data
            return data, 201

    def delete(self, bread_id):
        if bread_id in breads:
            del breads[bread_id]
            return {"message": "Roti berhasil dihapus"}, 200
        else:
            return {"message": "Roti tidak ditemukan"}, 404

# Menambahkan endpoint ke API
api.add_resource(BreadList, '/breads')
api.add_resource(Bread, '/breads/<bread_id>')

# Menjalankan server
if __name__ == '__main__':
    app.run(debug=True)
