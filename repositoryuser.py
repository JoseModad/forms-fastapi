from sqlalchemy.orm import Session
from models import UserModel
import smtplib 
from email.message import EmailMessage
import os
from dotenv import load_dotenv


load_dotenv()


class UserRepository:
    def __init__(self, sess: Session):
        self.sess: Session = sess
        
    def create_user(self, signup: UserModel) -> bool:
        try:
            self.sess.add(signup)
            self.sess.commit()
        except:
            return False
        return True
    
    def get_user(self):
        return self.sess.query(UserModel).all()
    
    def get_user_by_username(self, username: str):
        return self.sess.query(UserModel).filter(UserModel.username == username).first()
    

class SendEmailVerify:
    def sendVerify(token):
        email_address = os.getenv("EMAIL_ADDRESS")
        email_password = os.getenv("EMAIL_PASSWORD")
        
        # Create email
        
        msg = EmailMessage()
        msg["Subjet"] = "Email subjet"
        msg["From"] = email_address
        msg["To"] = "turko1073@gmail.com"
        msg.set_content(
            f"""\
            verify account
            http://localhost:8000/user/verify/{token}
            """,
        )
        
        # Send email
        
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg)