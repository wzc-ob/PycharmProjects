import smtplib,email

chst = email.charset.Charset(input_charset='utf-8')
header = ('Form:%s\nTo:%s\nSubject: %s\n\n'%('18772815717@163.com','18772815717@163.com',chst.header_encode('Python smtplib 测试')))
body = 'nihao '
email_con = header.encode('utf-8') + body.encode('utf-8')
smtp = smtplib.SMTP("smtp.163.com")
smtp.login('18772815717@163.com','19960320wzc')
for i in range(2):
    smtp.sendmail('18772815717@163.com','18772815717@163.com',email_con)
smtp.quit()