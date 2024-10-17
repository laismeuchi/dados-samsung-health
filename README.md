# Ingestão de dados de email

Nesse projeto a ideia era utiliziar uma fonte de dados que em alguns casos é a única saída para a ingestão de dados que não estão em nenhum sistema ou fonte de armazenamento: o envio de dados por email.

Em alguns projetos que trabalhei, a leitura de emails e seus anexos foi utilizada como solução para importar desse tipo, como por exemplo parâmetros de regras de negócio a serem aplicadas nos processamentos e que não existiam em nenhum sistema. E geralmente eram dados que podiam ser alterados pelo usuário a qualquer momento para o reprocessamento.

## Arquitetura

Para simular o cenário descrito anteriormente, fiz esse projeto em que eu exporto os dados das minhas atividades físicas no aplicativo de celular Samsung Health e envio para meu email.

O email é monitorado por um Logic Apps que detecta o email e envia o anexo para uma storage na Azure.

Essa storage foi registrada no Databricks como uma external location e um job é disparado quando um novo arquivo é adicionado nela.

O job faz o carregamento do csv para as camdas bronze, silver e gold.
Assim o processo ficou todo automatizado com base no recebimento do email

![image](https://github.com/user-attachments/assets/8dad523b-a2de-4e69-a8b3-d2be381717be)

