# CoreSentinel
## v1.0

Monitor de saúde do sistema para Windows e Linux, desenvolvido em Python. O
programa acompanha o uso de memória RAM e CPU, grava as medições em
`system_health.log` e exibe notificações nativas quando os limites de uso são
atingidos.

## Funcionalidades

- Monitoramento contínuo do uso de RAM.
- Monitoramento do uso de CPU.
- Tentativa de leitura da temperatura da CPU quando o sistema operacional e o
  `psutil` disponibilizam essa informação.
- Alertas no log e notificações nativas para:
  - RAM igual ou superior a 90%.
  - CPU igual ou superior a 90%.
- Encerramento seguro com `Ctrl+C`.

## Requisitos

- Python 3.10 ou superior.
- Windows ou Linux.
- Um ambiente de desktop capaz de exibir notificações nativas.

As dependências do projeto estão em [requirements.txt](requirements.txt):

- `psutil==7.2.2`
- `plyer==2.1.0`

## Instalação

Clone o projeto e entre na pasta:

```powershell
git clone <URL_DO_REPOSITORIO>
cd coresentinel
```

Crie e ative um ambiente virtual:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativação do ambiente, execute uma vez:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

Depois, instale as dependências:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Uso

Inicie o monitor com:

```powershell
python main.py
```

Enquanto estiver em execução, o terminal exibirá uma mensagem de inicialização
e o programa continuará registrando medições. Para encerrar, pressione
`Ctrl+C`.

Para executar no Linux, use os comandos equivalentes:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 main.py
```

## Logs

As medições são gravadas em `system_health.log`, no diretório de execução do
programa. Cada registro contém:

- data e hora;
- nível do registro (`INFO`, `WARNING` ou `ERROR`);
- percentual de RAM;
- percentual de CPU;
- temperatura da CPU, quando disponível.

O arquivo de log é gerado automaticamente e está listado no
[.gitignore](.gitignore) para não ser versionado.

## Configuração

Os limites e o intervalo de verificação podem ser ajustados no início de
[main.py](main.py):

```python
THRESHOLD_RAM_PERCENT = 90.0
THRESHOLD_CPU_PERCENT = 90.0
INTERVALO_VERIFICACAO_SEGUNDOS = 0.5
```

O uso de CPU é medido pelo intervalo interno de um segundo do `psutil`. Por
isso, o tempo real entre medições pode ser maior que o intervalo configurado.

## Estrutura do projeto

```text
.
├── main.py
├── requirements.txt
├── system_health.log
└── .gitignore
```

## Observações

- O suporte a temperatura depende do sistema operacional, dos sensores
  disponíveis e das permissões do ambiente. Quando a leitura não está
  disponível, ela é omitida do log.
- Falhas na leitura do sistema ou no envio de notificações são registradas
  como erros e não encerram automaticamente o monitor.
- No Windows, as notificações dependem do suporte do ambiente de desktop e da
  implementação disponível pelo `plyer`.

## Licença

Este projeto ainda não define uma licença. Adicione uma licença ao repositório
antes de distribuí-lo publicamente.
