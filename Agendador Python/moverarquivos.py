import os
import time
import shutil
import schedule
import logging
from datetime import datetime, timedelta

# Diretórios
pasta_downloads = os.path.expanduser(r'>>caminhoaqui<<')
pasta_destino_imagem = os.path.expanduser(r'>>caminhoaqui<<')
pasta_destino_zp = os.path.expanduser(r'>>caminhoaqui<<')
pasta_destino_docs = os.path.expanduser(r'>>caminhoaqui<<')
pasta_outros = os.path.expanduser(r'>>caminhoaqui<<')

# Configuração de logging
log_file = os.path.expanduser(r'C:\Users\USER\OneDrive\Documentos\ArquivoDestinoAgendador\Logs\log.txt')
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s:%(message)s')

# Extensões de arquivos
EXT_IMAGENS = ('.jpeg', '.jpg', '.png', '.gif')
EXT_ZIP = ('.zip', '.rar')
EXT_DOCS = ('.pdf', '.docx', '.csv')

def mover_arquivos():
    try:
        for arquivo in os.listdir(pasta_downloads):
            src_path = os.path.join(pasta_downloads, arquivo)
            if arquivo.endswith(EXT_IMAGENS):
                dest_path = pasta_destino_imagem
            elif arquivo.endswith(EXT_ZIP):
                dest_path = pasta_destino_zp
            elif arquivo.endswith(EXT_DOCS):
                dest_path = pasta_destino_docs
            else:
                dest_path = pasta_outros

            shutil.move(src_path, dest_path)
            logging.info(f'Arquivo {arquivo} movido com sucesso para {dest_path}')
    except Exception as e:
        logging.error(f'Erro ao mover arquivo: {e}')

def limpar_logs_antigos():
    try:
        if os.path.exists(log_file):
            data_modificacao = datetime.fromtimestamp(os.path.getmtime(log_file))
            if datetime.now() - data_modificacao > timedelta(days=7):
                os.remove(log_file)
                logging.info('Log deletado com sucesso')
    except Exception as e:
        logging.error(f'Erro ao deletar arquivo: {e}')

# Agendamento das tarefas
schedule.every().day.at('00:00').do(mover_arquivos)
schedule.every().thursday.at('00:00').do(limpar_logs_antigos)

# Loop principal
while True:
    schedule.run_pending()
    time.sleep(1)
