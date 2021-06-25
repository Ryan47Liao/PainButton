import smtplib
import imaplib

#@title Gmail Communication Mod {display-mode: "form"}
def Msg_Editor(mail_subject,mail_body,tail="-Sent From Colab, Powered by Python"):
    body = mail_body + "\n\n" + tail
    message = "Subject:{}\n\n{}".format(mail_subject,body)
    return(message)

def Mail_Send(gmail_user,gmail_password,Receipeints_list,msg):
    msg = "From:{}\nTo:{}\n".format(gmail_user,Receipeints_list[0])+ msg
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com:465')
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, Receipeints_list , msg)
        server.close()
        print ('Email sent!')
    except:
        print ('!ERROR!Something went wrong...')

def MTK_send(okrID,data,mail_info):
    "Send an task from task today's Special Task to MTK's email address"
    gmail_user = mail_info["mail_address"]
    gmail_password = mail_info["mail_password"]
    hashTag = {1:"Health",2:"Family",3:"Personal Development",4:"Career"}
    if True:#try:
        category = int(okrID.split("_")[1][1])
        task_type = okrID.split("_")[0]
        if task_type == "S":
            task_type = "SpecialTasks"
        elif task_type == "R":
            task_type = "RecursiveTasks"
        Receipeints_list = [data["MTK"][category]]
    else:#except:
        print("❌ERROR❌,drop email address not defined")
    try:
        tag = hashTag[category]
        Reward = data["TaskToday"][task_type][okrID]["Reward"]
        task_name = data["TaskToday"][task_type][okrID]["task_name"] 
        task_difficulty = data["TaskToday"][task_type][okrID]["task_difficulty"]
        task_time = data["TaskToday"][task_type][okrID]["task_time"]
        task_description = data["TaskToday"][task_type][okrID]["task_description"]
    except KeyError:
        print("Task {} Does not Exist".format(okrID))
    body = "{}ID:{}\n\n[Reward]\n {}\n[Time]\n {}\n[Difficulty]\n {}\n[Description]\n {}".format(tag,okrID,str(Reward),task_time,task_difficulty,task_description)
    msg = Msg_Editor(task_name,body)
    Mail_Send(gmail_user,gmail_password,Receipeints_list,msg)
    
def Done_today(mail_address,mail_password,SERVER = '(RFC822)',mail_scope = 20 ): 
    "Returns a list of Tasks that are finished Today"
    Task_finished = []
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login("bliao2@uci.edu","321890Ga")
    mail.select('inbox')
    status, data = mail.search(None, 'ALL')
    mail_ids = []
    wk_day_latest = ""  
    wk_day = "" 
    i = 0
    for block in data:
        mail_ids += block.split()
    while True:
        i += -1
        status, data = mail.fetch(mail_ids[i], '(RFC822)')
        if wk_day != wk_day_latest and wk_day_latest != "":
            print("End Reached")
            return(Task_finished)
        for response_part in data:
            if isinstance(response_part, tuple):
                message = mail.message_from_bytes(response_part[1])
                mail_from = message['from']
                mail_subject = message['subject']
                Date = message["Date"]
                wk_day = Date.split(",")[0]
                if wk_day_latest == "":
                    wk_day_latest = wk_day
                if message.is_multipart():
                    mail_content = ''
                    for part in message.get_payload():
                        if part.get_content_type() == 'text/plain':
                            mail_content += part.get_payload()
                else:
                    mail_content = message.get_payload()
                if mail_from == "MeisterTask <reply@meistertask.com>":
                    try:
                        task_name = mail_subject.split("'")[1]
                        task_status = mail_subject.split("'")[3]
                        if task_status == "Done_Today":
                            Task_finished.append(task_name)
                    except:
                        print("Task {} failed to sync, please complete manually.".format(mail_subject))
    

if __name__ == '__main__':
    Mail_Send("bliao2@uci.edu","321890Ga",['leonidas47dario@gmail.com'],'This is Ryan. Sent from Python')