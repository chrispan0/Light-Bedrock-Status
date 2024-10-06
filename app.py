from flask import Flask, render_template
import requests

app = Flask(__name__)

# Fetch the server status using the API
def get_minecraft_server_status():
    try:
        response = requests.get(f'https://api.mcsrvstat.us/bedrock/3/minecraft.chrispanetta.com')
        data = response.json()
        if data['online']:
            return {
                'server_version': data['version'],
                'motd': data['motd']['clean'][0],
                'max_players': data['players']['max'],
                'connected_players': data['players']['online'],
                'hostname': data['hostname'],
                'map': data['map']['clean'] if 'map' in data else 'N/A',
                'gamemode': data['gamemode'] if 'gamemode' in data else 'N/A',
                'server_id': data['serverid'],
            }
    except Exception as e:
        print(f"Error: {e}")
    return None

# Define the route for the index page
@app.route('/')
def index():
    server_info = get_minecraft_server_status()
    return render_template('index.html', server_info=server_info)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
