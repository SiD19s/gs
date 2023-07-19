from flask import Flask,request,jsonify
import json
from sql_connection import get_sql_connection
import products_dao
import uom_dao


connection = get_sql_connection()

app = Flask(__name__)

@app.route('/getProducts')
def get_products():
    products = products_dao.get_all_products(connection)
    response = jsonify(products)
    response.headers.add('Acess-Control-Allow-Origin','*') #Now frontend can call this
    return response

@app.route('/getUOM',methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Acess-Control-Allow-Origin','*') #Now frontend can call this
    return response

@app.route('/insertProduct',methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection,request_payload)
    response = jsonify({
        'product_id':product_id
    })
    response.headers.add('Acess-Control-Allow-Origin','*')
    return response



@app.route('/deleteProduct', methods=['POST']) 
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response




if __name__ == "__main__": 
    print("starting pyhton flask server")
    app.run(port=5000)