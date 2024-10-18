# Ingestão de dados de email

Nesse projeto a ideia era utilizar uma fonte de dados que em alguns casos é a única saída para a ingestão de dados que não estão em nenhum sistema ou fonte de armazenamento: o envio de dados por email.

Em alguns projetos que trabalhei, a leitura de emails e seus anexos foi utilizada como solução para importar desse tipo, como por exemplo parâmetros de regras de negócio a serem aplicadas nos processamentos e que não existiam em nenhum sistema. E geralmente eram dados que podiam ser alterados pelo usuário a qualquer momento para o reprocessamento.

## Arquitetura

Para simular o cenário descrito anteriormente, fiz esse projeto em que eu exporto os dados das minhas atividades físicas no aplicativo de celular [Samsung Health](https://www.samsung.com/br/apps/samsung-health/) e envio para meu email.

O email é monitorado por um [Logic Apps](https://learn.microsoft.com/pt-br/azure/logic-apps/logic-apps-overview) que detecta o email e envia o anexo para uma _storage_ na Azure.

Essa _storage_ foi registrada no [Databricks](https://www.databricks.com/br) como uma _external location_ e um _job_ é disparado quando um novo arquivo é adicionado nela.

O _job_ faz o carregamento do _csv_ para as camdas _bronze_, _silver_ e _gold_.
Assim o processo ficou todo automatizado com base no recebimento do email.

![image](https://github.com/user-attachments/assets/f860889c-f8d7-4a43-9d45-f056c298345f)


## Demonstração

Fiz esse vídeo para apresentar o funcionamento do projeto ao vivo:

<div>
    <a href="https://www.loom.com/share/4f6bd833f2124609b722481f4c5bb378">
      <p>Samsung Health data analysis - Watch Video</p>
    </a>
    <a href="https://www.loom.com/share/4f6bd833f2124609b722481f4c5bb378">
      <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/4f6bd833f2124609b722481f4c5bb378-f0c7c565dc0c883c-full-play.gif">
    </a>
  </div>

## Painel

Com os dados a _bronze_ fiz esse painel simples no Databricks mesmo para apresentar os resultados.

![image](https://github.com/user-attachments/assets/c470f403-5f30-41f4-bacf-9235b8447143)


## Códigos

Aqui nesse projeto esta o código utilzado no _job_ do Databricks.
