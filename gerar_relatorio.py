import pandas as pd
import matplotlib.pyplot as plt
import smtplib
import json
from email.message import EmailMessage

# Ler configuração
with open("config.json", "r") as f:
    config = json.load(f)

# Ler dados do Excel
df = pd.read_excel("relatorio.xlsx")
print("Dados carregados:")
print(df)

# Criar gráfico
plt.figure(figsize=(8, 4))
plt.plot(df['Mês'], df['Vendas'], marker='o')
plt.title("Relatório de Vendas")
plt.xlabel("Mês")
plt.ylabel("Vendas")
plt.grid(True)
plt.tight_layout()
plt.savefig("grafico.png")
plt.close()

# Enviar e-mail com o gráfico
msg = EmailMessage()
msg['Subject'] = 'Relatório Automático de Vendas'
msg['From'] = config["email"]
msg['To'] = config["destinatario"]
msg.set_content("Segue em anexo o gráfico de vendas.")

with open("grafico.png", "rb") as f:
    msg.add_attachment(f.read(), maintype='image', subtype='png', filename="grafico.png")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(config["email"], config["senha"])
    smtp.send_message(msg)

print("Relatório enviado por e-mail!")