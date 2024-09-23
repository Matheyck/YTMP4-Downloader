import yt_dlp
import os
import argparse

def create_output_directory(output_path):
    os.makedirs(output_path, exist_ok=True)

def download_video(url, output_path='download', format='mp4'):
    create_output_directory(output_path)

    if format == 'mp3':
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'ffmpeg_location': './bin/',
        }
    else:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'ffmpeg_location': './bin/',
        }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url)
            ydl.download([url])
        
        # Se for MP3, renomeia a extensão
        if format == 'mp3':
            original_filename = ydl.prepare_filename(info_dict)
            new_filename = os.path.splitext(original_filename)[0] + '.mp3'
            os.rename(original_filename, new_filename)

        print(f"Arquivo baixado com sucesso para {output_path}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def hook(d):
    if d['status'] == 'finished':
        print(f"\nDownload concluído: {d['filename']}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Baixar vídeos do YouTube.')
    parser.add_argument('--output', type=str, default='video', help='Diretório de saída')

    args = parser.parse_args()

    while True:
        video_url = input("Digite a URL do vídeo do YouTube (ou 'sair' para encerrar): ")
        if video_url.lower() == 'sair':
            print("Encerrando o programa.")
            break
        
        # Escolha do formato
        format = input("Escolha o formato de saída (mp4 ou mp3): ").strip().lower()
        while format not in ['mp4', 'mp3']:
            print("Formato inválido! Escolha 'mp4' ou 'mp3'.")
            format = input("Escolha o formato de saída (mp4 ou mp3): ").strip().lower()

        download_video(video_url, args.output, format)
