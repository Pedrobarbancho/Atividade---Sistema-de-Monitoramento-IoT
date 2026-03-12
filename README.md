# Sistema de Monitoramento IoT

## Resumo
Este projeto implementa um sistema de monitoramento de dispositivos IoT distribuídos em diferentes locais. Sensores instalados nos equipamentos coletam dados ambientais como temperatura, umidade, pressão e luminosidade. Os dados são armazenados em um banco MySQL, e uma aplicação Python permite consultar os alertas registrados no banco.

## Banco de Dados
O banco de dados possui cinco tabelas principais:
- **locais**: armazena os ambientes onde os dispositivos estão instalados.
- **equipamentos**: guarda os dispositivos IoT e seu local de instalação.
- **sensores**: contém os sensores vinculados a cada equipamento.
- **medicoes**: registra as leituras feitas pelos sensores.
- **alertas**: armazena notificações geradas quando valores ultrapassam limites pré-definidos.

As tabelas estão relacionadas por meio de chaves estrangeiras que garantem integridade referencial.

## Como criar o banco no MySQL Workbench
1. Abra o MySQL Workbench e conecte no servidor local.  
2. Crie o banco de dados com:
   ```sql
   CREATE DATABASE bancoDB;
   USE bancoDB;
3. Copie e execute todo o script de criação das tabelas (CREATE TABLE) na ordem:
- locais
- equipamentos
- sensores
- medicoes
- alertas
4. Insira os dados iniciais com os INSERT INTO, seguindo a ordem:
- locais
- equipamentos
- sensores
- medicoes
- alertas
> Seguindo esta ordem você evita erros de foreign key

## Código Python
O código Python conecta ao banco MySQL e permite:
- Listar os alertas registrados no banco.
> Obs: atualmente o código apenas lista alertas. Futuras melhorias podem incluir cadastro de equipamentos, sensores e medições.
## como usar
1. Abra o PowerShell (ou terminal) e instale a biblioteca MySQL:
```bash
pip install mysql-connector-python
```
Se quiser atualizar o pip:
```bash
python -m pip install --upgrade pip
```
2. Certifique-se de que o banco bancoDB e as tabelas já foram criados com o script SQL.
3. Execute o código Python:
```bash
python app.py
```
4. O programa exibirá os alertas armazenados no banco de dados.
## autores
- pedro arthur b. santos
- lucas rodrigues sousa
