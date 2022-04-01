import yagmail
import os
import time

sender = 's******2@gmail.com'
receiver = '35bw29dv@minimail.gq'
  
subject = "This is the subject"
  
contents = """Here is the content of the email
Hi!
"""

while True:
  yag = yagmail.SMTP(user=sender,password= os.getenv('PASSWORD'))
  yag.send(to=receiver,subject=subject,contents=contents)
  print("Email sent")
  time.sleep(10)
