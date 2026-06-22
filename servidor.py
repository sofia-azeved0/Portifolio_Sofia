from flask import Flask, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import traceback # <-- Nova biblioteca para rastrear o erro exato!

app = Flask(__name__)

MEU_EMAIL = "s.leitaoazevedo@gmail.com" 
MINHA_SENHA_APP = "qkuq mkgv xebw tjfc"

@app.route('/', methods=['GET'])
def pagina_inicial():
    return "<h1>Servidor Online! 🚀</h1><p>O servidor de e-mails da Sofia está a funcionar perfeitamente.</p>"

@app.route('/enviar', methods=['POST', 'GET'])
def receber_contato():
    # Envolvemos absolutamente TUDO num bloco de teste
    try:
        if request.method == 'GET':
            return "<h1>Rota de Envio Ativa ✉️</h1><p>Esta rota está pronta para receber as mensagens do seu portefólio.</p>"

        nome = request.form.get('nome', 'Visitante')
        email_remetente = request.form.get('email', 'Não informado')
        mensagem_texto = request.form.get('mensagem', '')

        msg = MIMEMultipart()
        msg['From'] = MEU_EMAIL
        msg['To'] = MEU_EMAIL
        msg['Subject'] = f"Novo Contato do Portfólio de: {nome}"

        corpo_email = f"Recebeu uma nova mensagem do seu site!\n\nNome: {nome}\nE-mail de contacto: {email_remetente}\n\nMensagem:\n{mensagem_texto}"
        msg.attach(MIMEText(corpo_email, 'plain', 'utf-8'))

        servidor_smtp = smtplib.SMTP('smtp.gmail.com', 587)
        servidor_smtp.starttls()
        servidor_smtp.login(MEU_EMAIL, MINHA_SENHA_APP)
        servidor_smtp.send_message(msg)
        servidor_smtp.quit()
        
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
                <p>A sua mensagem foi enviada diretamente para o meu e-mail com sucesso. Retornarei o mais breve possível.</p>
                <a href="javascript:history.back()" class="btn-voltar">Voltar para o Portefólio</a>
            </div>
        </body>
        </html>
        """
    except Exception as e:
        # Se QUALQUER erro acontecer, mostramos no ecrã em vez de dar o Internal Server Error!
        erro_completo = traceback.format_exc()
        return f"<h2>Puxa! O código Python quebrou.</h2><p>Aqui está o erro exato para partilhar comigo:</p><pre style='text-align: left; background: #eee; padding: 15px; border-radius: 10px; font-size: 13px; color: #d9534f; overflow-x: auto;'>{erro_completo}</pre>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)