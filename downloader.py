import yt_dlp
import os

def download_video(url, output_path='video'):
    # Cria o diretório de saída se não existir
    os.makedirs(output_path, exist_ok=True)

    # Define as opções para download do vídeo
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Baixa o melhor vídeo e áudio disponível
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',  # Converte o vídeo para MP4
        }],
        'ffmpeg_location': './bin/',  # Atualize este caminho se necessário
    }
    
    # Baixa o vídeo usando yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    print(f"Vídeo baixado e convertido com sucesso para {output_path}")

if __name__ == "__main__":
    video_url = input("Digite a URL do vídeo do YouTube: ")
    download_video(video_url)
