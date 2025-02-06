# organizadorarquivos
Desenvolvi esse agendador de tarefa para o windows para mover alguns arquivos de uma pasta de origem para outra pasta organizador por tipo de arquivo (imagens, arquivos compactos, documentos e outros) e gravar log em caso de sucesso ou falha utilizando a biblioteca logging, além de implementar uma rotina na tarefa para deletar logs com mais de uma semana.

Em caso da máquina não estar ativa no horário designado para tarefa foi configurado no windows pelo task scheduler do Windows 10 para executar a tarefa assim que possível e em caso de falha na tarefa reiniciar a cada 5 minutos até 10 tentativas, e também interromper a tarefa se ela for executada por mais de 1 hora.

Fiz essa tarefa pois diariamente lido com muitos arquivos de extensões específicas em função do meu trabalho, criei o agendador para automatizar a rotina de organização dos arquivos.
