from flask import Flask, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

MEU_EMAIL = "s.leitaoazevedo@gmail.com" 
MINHA_SENHA_APP = "qkuq mkgv xebw tjfc"

@app.route('/enviar', methods=['POST'])
def receber_contato():
    nome = request.form.get('nome')
    email_remetente = request.form.get('email')
    mensagem_texto = request.form.get('mensagem')

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

        return f"""
        <!DOCTYPE html>
        <html lang="pt_BR">
        <head>
            <meta charset="UTF-8">
            <title>Mensagem Enviada</title>
            <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
            <style>
                body {{
                    background-color: #0a0a16;
                    color: #f8fafc;
                    font-family: 'Poppins', sans-serif;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    height: 100vh;
                    margin: 0;
                    background-image: radial-gradient(circle at 50% 0%, #1e1b4b 0%, #0a0a16 60%);
                }}
                .card-sucesso {{
                    background: rgba(30, 41, 59, 0.7);
                    padding: 40px;
                    border-radius: 15px;
                    border: 1px solid rgba(255, 77, 166, 0.3);
                    text-align: center;
                    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
                    max-width: 500px;
                    backdrop-filter: blur(10px);
                }}
                h2 {{
                    color: #ff4da6;
                    margin-top: 0;
                    font-size: 2rem;
                }}
                p {{
                    color: #94a3b8;
                    line-height: 1.6;
                }}
                .btn-voltar {{
                    display: inline-block;
                    margin-top: 25px;
                    padding: 12px 30px;
                    background-color: transparent;
                    color: #ff4da6;
                    border: 2px solid #ff4da6;
                    text-decoration: none;
                    border-radius: 30px;
                    font-weight: bold;
                    transition: 0.4s;
                    text-transform: uppercase;
                    letter-spacing: 1px;
                }}
                .btn-voltar:hover {{
                    background-color: #ff4da6;
                    color: #0a0a16;
                    box-shadow: 0 0 20px rgba(255, 77, 166, 0.5);
                }}
            </style>
        </head>
        <body>
            <div class="card-sucesso">
                <h2>Obrigada, {nome}!</h2>
                <p>Sua mensagem foi enviada diretamente para o meu e-mail com sucesso. Retornarei o mais breve possível!</p>
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