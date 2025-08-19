from flask import Flask

app = Flask(__name__)

@app.get('/')
def home():
    return """
    <html>
        <h1>Welcome to the CSV transformer page!</h1>
        <p>Click here to transform your CSV file into a beautiful format!</p>
        <form action="/transform" method="POST" enctype="multipart/form-data">
            <input type="file" name="file" accept=".csv">
            <input type="submit" value="Transform CSV">
        </form>
    </html>
    """

@app.post('/transform')
def transform():
    print("Transforming CSV...")
    csv_file = """
    somethign,somehting
    "sometihsl",5
    """
    return csv_file
