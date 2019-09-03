# Bem vindo a nossa documentação


## Projeto

Reprodução automática de propagandas em dispositivo embarcado.


## Desenvolvedor

Gabriel Mauly

## Arquitetura

O projeto foi construído na seguinte arquitetura

    bus-advertising/
         docs/
         app.py
         mkdocs.yml
         README.md
         video.mp4

Onde:

<b> docs</b>

Pasta que contém a documentação do projeto.

<b>old</b>

Pasta que armazena os vídeos anteriores.

<b> app.py </b>

Algoritmo responsável pela atualização e reprodução dos vídeos.

<b> mkdocs.yml</b>

Arquivo de configuração da documentação.

<b> README.md</b>

Arquivo inicial do git hub.

<b>video.mp4</b>

Arquivo com as propagandas a serem reproduzidas.


## Algoritmo

O algoritmo foi desenvolvido da seguinte maneira:

    import os
    
    
    def send_video():
        os.system('git commit -m "update video on repository" ')
    
    
    def update_video():
        os.system('git pull')
    
    
    def run_video():
        os.system('vlc -f --repeat video.mp4')
    
    
    if __name__ == '__main__':
        run_video()
