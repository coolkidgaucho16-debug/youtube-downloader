from flask import Flask, request, send_file, jsonify
import yt_dlp
import os

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download():
    try:
        data = request.get_json()
        url = data.get('url')
        
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'audio.mp3',
            'quiet': True
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=True)
        
        return send_file('audio.mp3', as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
