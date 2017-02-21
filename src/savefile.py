import subprocess


def salvaImagemCodificada(nomeArquivo, imagemCodificada):
    subprocess.check_call(['/home/pi/Desktop/scripts/savefile.sh', nomeArquivo,imagemCodificada])
    return
