from flask import Flask

app = Flask(__name__)

@app.route("/")
def login():

  username = request.values.get('username')
  password = request.values.get('password')

  # Prepare database connection.
  db = pymysql.connect("localhost")
  cursor = db.cursor()

  # Execute the SQL query concatenating user-provided input.
  
  # Esta dos líneas de código contienen una vulnerabilidad para SQL Injection
  #sql = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
  #cursor.execute(sql)

  # Se modifican con esta nueva escritura empleando placeholders para reemplazar por cadenas de texto
  # que se enviarán como parámetros a la función execute.
  sql = "SELECT * FROM users WHERE username = %s AND password = %s"
  cursor.execute(sql, (username, password))
  

  # If the query returns any matching record, consider the current user logged in.
  record = cursor.fetchone()
  if record:
    session['logged_user'] = username

  # Disconnect from server.
  db.close()
