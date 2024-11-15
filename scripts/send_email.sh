apt-get install mailutils -y
echo "O pipeline do atendimento no Jenkins foi executado com sucesso!" | mail -s "Notificação do Jenkins" "${EMAIL}"
echo "EMAIL ENVIADO para ${EMAIL}"