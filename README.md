# Automação de Relatório com Envio por E-mail

Este projeto automatiza a geração de um gráfico a partir de uma planilha Excel e envia por e-mail automaticamente.

## Requisitos

- Python 3
- pandas
- matplotlib

Instale com:
```
pip install pandas matplotlib openpyxl
```

## Como usar

1. Edite o arquivo `config.json` com seu e-mail, senha de app e destinatário.
2. Adicione dados ao `relatorio.xlsx`.
3. Execute:
```
python gerar_relatorio.py
```

O gráfico será salvo e enviado por e-mail automaticamente!

> ⚠️ Recomendado usar senha de app no Gmail (não a senha principal).
