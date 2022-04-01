import yagmail
import os
import time
import schedule

def send_email():

  sender = 'sheikh212@gmail.com'
  receiver = '35bw29dv@minimail.gq'
  
  subject = "This is the subject"
  
  contents = """
  Here is the content of the email
  Hi!
  """
  
  yag = yagmail.SMTP(user=sender,password= os.getenv('PASSWORD'))
  yag.send(to=receiver,subject=subject,contents=contents)
  print("Email sent")

schedule.every(9).seconds.do(send_email)

while True:
  schedule.run_pending()
  time.sleep(1)
