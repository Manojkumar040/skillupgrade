import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# List of common phishing email templates
PHISHING_TEMPLATES = [
    {
        "subject": "Urgent: Account Security Alert!",
        "body": """Dear User,

We have detected unusual activity on your account. To secure your account, please log in immediately by clicking the link below.

[CLICK HERE TO SECURE YOUR ACCOUNT]

If you don't act within 24 hours, your account may be suspended.

Sincerely,
Your Service Team"""
    },
    {
        "subject": "Congratulations! You've Won a Reward",
        "body": """Dear Valued User,

Congratulations! You've won a $500 gift card. To claim your prize, click the link below and complete the form.

[CLICK HERE TO CLAIM YOUR PRIZE]

Best regards,
The Promotions Team"""
    },
    {
        "subject": "Action Required: Verify Your Email",
        "body": """Dear User,

Please verify your email address to ensure your account remains active. Click the link below to confirm.

[CLICK HERE TO VERIFY EMAIL]

Thank you,
Your Support Team"""
    }
]

# Function to send phishing emails
def send_phishing_email(recipient_email, sender_email, sender_password, template_choice):
    """Send phishing email based on template choice."""
    # Choose a phishing email template
    template = PHISHING_TEMPLATES[template_choice]
    subject = template["subject"]
    body = template["body"]
    
    # Setup the email server and login credentials (use secure methods in production)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Using Gmail's SMTP server
        server.starttls()
        server.login(sender_email, sender_password)

        # Craft the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print(f"Phishing email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Simulating tracking of phishing responses (click-through)
def track_phishing_responses(user_id, clicked_link):
    """Simulate tracking user responses to phishing emails."""
    if clicked_link:
        print(f"User {user_id} clicked the phishing link.")
    else:
        print(f"User {user_id} did not click the phishing link.")

# Main function to simulate phishing campaign for one user
def phishing_simulation():
    # Accept a single user's email address
    recipient_email = input("Enter the email address to simulate phishing: ").strip()
    user_id = 1  # You can set this to any unique ID for the user being tested

    # Email sender credentials (replace with your own credentials)
    sender_email = "youremail@example.com"
    sender_password = "yourpassword"  # Use an app-specific password for Gmail or other services

    # Randomly choose a phishing email template
    template_choice = random.choice([0, 1, 2])  # Randomly choose one phishing template
    
    # Send phishing email to the user
    send_phishing_email(recipient_email, sender_email, sender_password, template_choice)
    
    # Simulate user response to the phishing email (random click-through simulation)
    clicked_link = random.choice([True, False])  # Randomly simulate whether the user clicked the link
    track_phishing_responses(user_id, clicked_link)

# Run the phishing simulation for one user
if __name__ == "__main__":
    phishing_simulation()
