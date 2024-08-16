from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='static')

# Print ASCII art from file before starting the server
try:
    with open('art.txt', 'r') as file:
        art = file.read()
        print(art)
except FileNotFoundError:
    print("art.txt not found.")

@app.route('/')
def serve_index():
    print("Serving index.html")
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    print(f"Serving static file: {filename}")
    return send_from_directory(app.static_folder, filename)

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=False)