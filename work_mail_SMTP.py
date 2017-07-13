# send mail
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# from_addr = input('From:')
# password = input('Password:')
# to_addr = input('To:')
# smtp_server = input('SMTP server:')

# 163
# from_addr = 'xindy138@163.com'
# password = '*******'
# to_addr = '373128869@qq.com'
# smtp_server = 'smtp.163.com'
# smtp_port = 25

# qq 特殊端口465 和验证码
from_addr = '373128869@qq.com'
password = 'qhhtlbcexpnzcbac'
to_addr = 'demiyuhongjun@gmail.com'
smtp_server = 'smtp.qq.com'
smtp_port = 465

# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')
msg = MIMEMultipart('alternative')  # 同时支持HTML和Plain格式 如果收件人无法查看HTML格式的邮件，就可以自动降级查看纯文本邮件
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
                    '<p><img src="cid:0"></p>' +
                    '</body></html>', 'html', 'utf-8'))
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

with open('test33.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test33.png')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test33.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP_SSL(smtp_server, smtp_port)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
