from flask import Flask, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

MEU_EMAIL = "s.leitaoazevedo@gmail.com" 
MINHA_SENHA_APP = "qkuq mkgv xebw tjfc" # Dica de segurança: como você compartilhou essa senha, o ideal é gerar uma nova lá no Google depois! 😉

@app.route('/enviar', methods=['POST', 'GET'])
def receber_contato():
    # 1. Trata o caso de você acessar o link diretamente no navegador (GET)
    if request.method == 'GET':
        return "<h1>Servidor Online! 🚀</h1><p>O servidor está funcionando perfeitamente. Para testar o e-mail, volte ao seu portfólio e envie pelo formulário.</p>"

    # 2. Trata o envio real do formulário (POST)
    nome = request.form.get('nome', 'Visitante')
    email_remetente = request.form.get('email', 'Não informado')
    mensagem_texto = request.form.get('mensagem', '')

    msg = MIMEMultipart()
    msg['From'] = MEU_EMAIL
    msg['To'] = MEU_EMAIL
    msg['Subject'] = f"Novo Contato do Portfólio de: {nome}"

    corpo_email = f"Você recebeu uma nova mensagem do seu site!\n\nNome: {nome}\nE-mail de contato: {email_remetente}\n\nMensagem:\n{mensagem_texto}"
    msg.attach(MIMEText(corpo_email, 'plain', 'utf-8'))

    try:
        servidor_smtp = smtplib.SMTP('smtp.gmail.com', 587)
        servidor_smtp.starttls() # Liga a segurança
        servidor_smtp.login(MEU_EMAIL, MINHA_SENHA_APP)
        servidor_smtp.send_message(msg)
        servidor_smtp.quit()
        
        print(f"Sucesso! E-mail de {nome} enviado para a sua caixa de entrada.")

        # Nova tela de sucesso combinando com o design Editorial Clean!
        return f"""
        <!DOCTYPE html>
        <html lang="pt_BR">
        <head>
            <meta charset="UTF-8">
            <title>Mensagem Enviada</title>
            <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500&family=Playfair+Display:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
            <style>
                body {{
                    background-color: #FDFBF9;
                    color: #2D2A28;
                    font-family: 'Inter', sans-serif;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    margin: 0;
                }}
                .card-sucesso {{
                    background: #FFFFFF;
                    padding: 50px;
                    border-radius: 24px;
                    border: 1px solid #EAE5E1;
                    text-align: center;
                    box-shadow: 0 15px 35px rgba(45, 42, 40, 0.04);
                    max-width: 500px;
                }}
                h2 {{
                    font-family: 'Playfair Display', serif;
                    color: #A67C8E;
                    margin-top: 0;
                    font-size: 2.5rem;
                    font-weight: 400;
                }}
                p {{
                    color: #8A8582;
                    line-height: 1.6;
                    font-weight: 300;
                    font-size: 16px;
                    margin-bottom: 30px;
                }}
                .btn-voltar {{
                    display: inline-block;
                    padding: 14px 30px;
                    background-color: transparent;
                    color: #2D2A28;
                    border: 1px solid #EAE5E1;
                    text-decoration: none;
                    border-radius: 30px;
                    font-weight: 500;
                    transition: all 0.3s;
                    font-size: 14px;
                }}
                .btn-voltar:hover {{
                    background-color: #A67C8E;
                    color: #FFFFFF;
                    border-color: #A67C8E;
                }}
            </style>
        </head>
        <body>
            <div class="card-sucesso">
                <h2>Obrigada, {nome}!</h2>
                <p>Sua mensagem foi enviada diretamente para o meu e-mail com sucesso. Retornarei o mais breve possível.</p>
                <a href="javascript:history.back()" class="btn-voltar">Voltar para o Portfólio</a>
            </div>
        </body>
        </html>
        """

    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        return f"<h2>Puxa! Ocorreu um erro no servidor ao tentar enviar a mensagem.</h2><p>{e}</p>"

if __name__ == '__main__':
    app.run(debug=True, port=5000)