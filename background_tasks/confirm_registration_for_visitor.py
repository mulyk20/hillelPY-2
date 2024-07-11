from utils.email_sender import create_welcome_letter, send_email

def confirm_registration_for_visitor(created_visitor, base_url):
    email_body = create_welcome_letter(
        {
            'name': created_visitor.name,
            'link': f'{base_url}api/visitors/verify/{created_visitor.visitor_uuid}'
        }
    )
    send_email([created_visitor.email], mail_body=email_body, mail_subject='Verification')
