# app.py  
from flask import Flask, request, jsonify  
  
app = Flask(__name__)  
  
# 模拟的用户数据库  
users = {  
    'admin': {'password': 'admin123', 'role': 'admin'},  
    'user1': {'password': 'user123', 'role': 'user'}  
}  
  
# 登录函数（仅用于模拟）  
def login(username, password):  
    user = users.get(username)  
    if user and user['password'] == password:  
        return user  
    return None  
  
# 受保护的路由  
@app.route('/admin', methods=['GET'])  
def admin_route():  
    user = request.get_json().get('user')  # 假设用户信息通过JSON传递（这是不安全的，仅用于模拟）  
    if user and user['role'] == 'admin':  
        return jsonify({'message': 'Welcome to the admin area!'})  
    return jsonify({'error': 'Access denied'}), 403  
  
# 登录路由（用于获取模拟的会话/令牌，但在这个简单示例中未使用）  
@app.route('/login', methods=['POST'])  
def login_route():  
    data = request.get_json()  
    user = login(data['username'], data['password'])  
    if user:  
        # 在实际应用中，这里会返回一个会话令牌或cookie  
        return jsonify({'message': 'Logged in successfully', 'role': user['role']})  
    return jsonify({'error': 'Invalid username or password'}), 401  
  
if __name__ == '__main__':  
    app.run(debug=True)
