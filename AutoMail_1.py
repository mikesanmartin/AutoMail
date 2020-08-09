#Auto Mail 
#Version 1.0
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = input('Por favor, ingrese su correo: ')
PASSWORD = input('Por favor, ingrese su contraseña: ')

def get_contacts(filename):
    """
    Obtiene los contactos y nombres desde archivo
    """

    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contact_file:
        for a_contact in contact_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):
    """
    Devuelve un template, desde un archivo especificado
    """
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    names, emails = get_contacts('D:\Documents\Programación\Proyectos\AutoMail\contactos.txt')
    # Leer contactos desde archivo
    message_template = read_template('D:\Documents\Programación\Proyectos\AutoMail\mensaje_prueba1.txt')
    # Leer Template de mail

    # Preparando SMTP Server
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # Para cada contacto, enviar mail
    for name, email in zip(names, emails):
        msg = MIMEMultipart() # Crea mensaje

        # Agregar nombre de destinatario al template
        message = message_template.substitute(PERSON_NAME=name.title())

        print(message)

        # configurando parametros de mensaje
        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject']='Esta es una prueba'

        # Agregar mensaje al cuerpo del mail
        msg.attach(MIMEText(message, 'plain'))

        # Enviar mensaje via el servidor configurado anteriormente
        s.send_message(msg)
        del msg

    # Terminar sesión SMTP y cerrar conexión.
    s.quit()

if __name__ == '__main__':
    main()

