# YouTube Video Downloader

Um simples script em Python que permite baixar vídeos do YouTube e convertê-los para o formato MP4 e MP3 usando a biblioteca `yt-dlp`.

## Funcionalidade
Download de Vídeos: O script baixa o vídeo ou áudio no melhor formato disponível.

Conversão para MP3 e MP4: O áudio pode ser baixado diretamente em formato MP3, e o vídeo é baixado no melhor formato de áudio e vídeo disponível. Se o formato MP4 for escolhido, o vídeo é convertido usando FFmpeg.

Diretório de Saída: Os vídeos e áudios baixados serão salvos em um diretório ``downloads``. Este diretório será criado automaticamente se não existir.

## Pré-requisitos

Antes de executar o script, certifique-se de ter as seguintes dependências instaladas:

- Python 3.x
- yt-dlp
- FFmpeg

Você pode instalar o `yt-dlp` usando pip:

```bash
pip install yt-dlp
```
E, para instalar o FFmpeg, siga as instruções de instalação para seu sistema operacional [neste link](https://ffmpeg.org/download.html)

## Observações
O caminho para o FFmpeg é definido na variável `ffmpeg_location` no código. Certifique-se de atualizar este caminho se necessário, de acordo com a localização do FFmpeg em seu sistema.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.