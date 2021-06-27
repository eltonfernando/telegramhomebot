[![author](https://img.shields.io/badge/Autor-Elton-blue)](https://www.instagram.com/elton.py/) [![](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/release/python-365/) [![](https://img.shields.io/badge/LIb-Opencv-blue.svg)](https://opencv.org/) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/eltonfernando/telegramhomebot/issues)

# telegramhomebot

Robô do telegram que monitora câmeras de segurança.

O arquivo cam_process.py acessa um fluxo de video da câmera e salva uma imagem na pasta imagem_evento quando houver movimento

o Bote do telegram (bot.py) procura nessa pasta por imagens, se houver, essa imagem é envida para o usuário que iniciou o bot.

Alterações futuras irá rodar o bot na nuvem heroku e usar um sevidor mqtt para comunicar com robô. 

---

Se você gosta de visão computacional baixe grátis meu Guia de visão computacional e receba email quando eu publicar novos artigos. [Baixar](http://visioncompy.com/)

---
Esse é um projeto Open source e contribuição são bem vindas, você pode criar uma issues para discutirmos novas ideas. [![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/eltonfernando/telegramhomebot/issues)

obs:  Utilize por sua própria conta de risco.

## dependências
* python 3.x
* opencv-contrib-python
* python-telegram-bot
* git

# Preparando ambiente (linux)
* ``git clone https://github.com/eltonfernando/telegramhomebot.git``
* ``python3 -m venv telegramhomebot``
* ``source telegramhomebot/venv/bin/activate``
* ``pip3 install opencv-contrib-python``
* ``pip3 install python-telegram-bot``

## excutando bot
  * Primeiro você deve criar um bot no telegram, procure pelo usuário BotFather envie uma mensagem /start. Siga as instruções para criar seu bot, ao final você terá um token.
  * Crie um arquivo de texto na raiz do projeto com nome token e salve seu token, ele dever ser carregado pela chamada  ``TOKEN=open('token',"r").read() `` no arquivo bot.py
   
  *   rodar o arquivo bot.py, ``python3 bot.py`` . Seu robô está em execução. Procure pelo usuário com o nome do seu bot no telegram, e envie ``\start``. Ele deve responder com seu nome.
  
  ## executando Câmera.
  
 No arquivo cam_process.py altere a string video para o link RTSP da sua câmera, ou mantenha como está para executar o vídeo de exemplo. ``python3 cam_process.py``

  ### Link RTSP
  Informações para seu link RTSP 

* IP: Esse é ip que você utiliza para acessar as configurações   da câmera conectada a sua rede (192.168.x.x ou 10.1.1.xxx)
 * ADMIN : usuário de acesso as configuração da câmera
 * SENHA: Senha do usuário
 * PORTA: A porta padrão é 554.

Subistitua as variáveis para criar seu link RTSP

* hikvision "rtsp://ADMIN:SENHA@IP:PORTA/ch1/principal/av_stream"

 * intelbras "rtsp://ADMIN:SENHA@IP:PORTA/cam/realmonitor?channel=1&subtype=1"
 
 Os links RTSP muda de acordo com fabricante você ver procura no manual de instruções. 
 
 
