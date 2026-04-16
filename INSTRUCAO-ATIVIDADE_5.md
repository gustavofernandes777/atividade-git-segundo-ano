# ATIVIDADE 5
Crie um programa que simule um sistema de missões de um jogo. Cada missão será representada por um vetor: 
(nome_da_missao, dificuldade, status).

dificuldade: "Fácil", "Média" ou "Difícil"
status: "Pendente" ou "Concluída"

O programa deve ter um menu:
* Adicionar missão
* Remover missão
* Concluir missão
* Listar missões
* Mostrar missões por dificuldade
* Sair

## Regras para adicionar
### Adicionar missão:
* O usuário informa nome e dificuldade
* Verificar e validar a dificuldade
* Se não for "Fácil", "Média" ou "Difícil", mostrar erro
### Remover missão
* Remover pelo nome (se existir)
*  Se não existir, informar mensagem de erro
### Concluir missão
*  Alterar o status para "Concluída"
*  Criar um novo vetor com status atualizado
### Listar missões
*  Mostrar todas as missões
### Mostrar por dificuldade
*  Perguntar uma dificuldade
*  Verificar, filtrar e mostrar apenas aquelas missões com a dificuldade selecionada
