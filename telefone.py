# Link com as referências de como escrever a mensagem
# https://www.twilio.com/docs/voice/twiml
from secrets import numero_kaue,account_sid,token
from twilio.rest import Client


account_sid = account_sid
auth_token = token
meu_numero = numero_kaue
numero_twilio = "+19706763223"

cliente = Client(account_sid, token)

mensagem = """
<Response>
<Say language="pt-BR">
 Olá
</Say>
</Response>
"""

ligacao = cliente.calls.create(
    to=meu_numero,
    from_=numero_twilio,
    twiml=mensagem
)


