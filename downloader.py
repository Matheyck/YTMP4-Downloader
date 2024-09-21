import yt_dlp
import os
import argparse

def create_output_directory(output_path):
    os.makedirs(output_path, exist_ok=True)

def download_video(url, output_path='video', format='mp4'):
    create_output_directory(output_path)

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': format,
        }],
        'ffmpeg_location': './bin/',
        'progress_hooks': [hook],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"Vídeo baixado e convertido com sucesso para {output_path}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def hook(d):
    if d['status'] == 'finished':
        print(f"\nDownload concluído: {d['filename']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Baixar vídeos do YouTube.')
    parser.add_argument('url', type=str, help='URL do vídeo do YouTube')
    parser.add_argument('--output', type=str, default='video', help='Diretório de saída')
    parser.add_argument('--format', type=str, default='mp4', help='Formato de saída do vídeo')

    args = parser.parse_args()
    download_video(args.url, args.output, args.format)
