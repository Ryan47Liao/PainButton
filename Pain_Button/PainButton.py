from datetime import datetime
import pickle


#@title Mistake Class {display-mode: "form"}
class mistakes:
    def __init__(self,title):
        self.title = title
        self.date = "tba"
        self.result = "tba"
        self.cause = "tba"
        self.log = "tba"
        self.take_away = "tba"
        self.category = "tba"
        
    def set_category(self,category):
        self.category = category

    def set_date(self,date):
        self.date = date
        
    def set_cause(self,cause):
        self.cause = cause
        
    def set_result(self,result):
        self.result = result
    
    def set_log (self,log):
        self.log = log
        
    def set_take_away (self,tw):
        self.take_away = tw
        
        
    def __repr__(self):
        return("[Title]:{}\n[Date]:{}\n[Category]:\n{}\n[Cause]:\n{}\n[Result]:\n{}\n[Log]:\n{}\n[Take_Away]:\n{}".format(str(self.title),
            self.date,self.category,self.cause,self.result,self.log,self.take_away))
        
    def sort_by_date(self,List, increasing_order = False):
        "Sort a list of mistakes in order by date"
        if increasing_order:
            for j in range(len(List),0,-1):
                for i in range(j-1):
                    if DATE(List[i].date) > DATE(List[i+1].date):
                        List[i],List[i+1] = List[i+1],List[i]
        else:
            for j in range(len(List),0,-1):
                for i in range(j-1):
                    if DATE(List[i].date) < DATE(List[i+1].date):
                        List[i],List[i+1] = List[i+1],List[i]
        return(List)
    
#@title Pain_Button Class {display-mode: "form"}
#@title Pain_Button Class {display-mode: "form"}
from datetime import date

class Pain_Button(mistakes):
    def __init__(self,ACC,PW):
        self.Acc = ACC
        self.Pw = PW
        self.Logs = {}
        self.CAT = ["Academic","HumanRelationship","Financial"]
        self.Cursor = Cursor()
    
    def merge(self,pb_object):
        self.Logs.update(pb_object.Logs)
        for i in pb_object.CAT:
            if i not in self.CAT:
                self.CAT.append(i)
    
    def reset_cursor(self):
        self.Cursor = Cursor(len(self.Logs))
        self.Cursor.cursor = 0
        
        
    def add_mistake(self,title,date,category,cause,result,log,tw):
        self.Logs[title] = mistakes(title)
        self.Logs[title].set_date(date)
        self.Logs[title].set_cause(cause)
        self.Logs[title].set_result(result)
        self.Logs[title].set_log(log)
        self.Logs[title].set_take_away(tw)
        self.Logs[title].set_category(category)
        self.Cursor.length += 1
        
    def delete_mistake(self,title):
        try:
            Q = input("Are you sure that you want to delete the following mistake? [Y] or [N]:\n",self.Logs[title])
            if Q == "Y":
                self.Logs.pop(title)
                self.Cursor.length -= 1
        except:
            print("Syntax Error")
            
    def __repr__(self):
        rep = ''
        for key in list(self.Logs.keys()):
            rep += "{:13} | {:13} |{}\n".format(self.Logs[key].date,self.Logs[key].category,key,) 
        return(rep)
    
    def show_by_date(self,n,increasing_order = False):
        "display the latest n mistakes from the Logs"
        self.sorted_date = self.sort_by_date(list(self.Logs.values()),increasing_order)
        for i in range(min(n,len(self.sorted_date))):

            print( "{:13} | {:13} |{}".format(self.sorted_date[i].date,self.sorted_date[i].category,self.sorted_date[i].title) )
        
    def find_by_date(self,date):
        "Find all the mistakes under given date"
        finded = False
        for mistake in self.Logs:
            if self.Logs[mistake].date == date:
                print(self.Logs[mistake])
                finded = True
        if not finded:
            print("Sorry, No mistake under such date was found.")

    def CAT_Add(self,CT_name):
        if CT_name not in self.CAT:
            self.CAT.append(CT_name)
            print("Category {} added.".format(CT_name))
        else: 
            print("Category already exist")

    def CAT_Delete(self,CT_name):
        if CT_name in self.CAT:
            self.CAT.remove(CT_name)
            print("Category {} Deleted.".format(CT_name))
        else:
            print("There is no such Category to delete.")

    def set_mail(self,mail_address,mail_pw):
        self.mail_address = mail_address
        self.mail_pw = mail_pw 
    
    def mistake_today(self,n,send_to_mail = False):
        pass
        # "Send n random mistakes to the predefined mail address"
        # index_list = []
        # Mistakes = str()
        # while len(index_list) < n:
        #     idx = random.randint(0,-1+len(list(self.Logs.values())))
        #     if idx not in index_list:
        #         index_list.append(idx)
        # for idx in index_list:
        #     Mistakes += str(list(self.Logs.values())[idx]) + "\n" + "_"*150 + "\n"
        # msg = Msg_Editor("Pain Botton daily review of {}".format(str(datetime.date.today())),Mistakes,"END")
        # print(msg)
        # # Message Ready
        # if send_to_mail:
        #     Mail_Send(self.mail_address,self.mail_pw,list(self.mail_address),msg)
                
            
class Cursor:
    def __init__(self,n):
        self.cursor = 0
        self.length = n
        self.base = "▶️"
        self.pointer = "🔻"
        
    def set_length(self,n):
        self.length = n
        
    def set_base(self,base):    
        self.base = base
        
    def set_pointer(self,pointer):   
        self.pointer = pointer
        
    def set_cursor(self,m):
        self.cursor = m
        
    def __repr__(self,item = 20):
        position = round(self.cursor/self.length*item)
        RPR = "[NEW]"+self.base*position+self.pointer+self.base*(round((self.length-self.cursor-1)/self.length*item))+"[END]"
        return RPR
    
#@title Extra Mods {display-mode: "form"}
def input_splited(instruction , sep = "[]"):
    entry = input(instruction)
    entry = entry.split(sep)
    output = str()
    for i in entry:
        output += i + "\n"
    return(output)
    
def DATE(String):
    try:
        String = String.split("-")
        Y = int(String[0])
        M = int(String[1])
        D = int(String[2])
        return(datetime(Y,M,D))
    except:
        return("Syntax Error!")
    
#@title Pain_Button UI {display-mode: "form"}
#@title Pain_Button UI {display-mode: "form"}
def PB(file_path):
    acc_file_path = file_path
    # LogIn and retrieve Data
    # Read Data
    try:
        INfile = open( file_path ,"rb")
        data = pickle.load(INfile)
        INfile.close()
    except:
        print("Error! data not located")
        return
    #Cmds
    while True:
        cmd = input("Please Enter cmds, enter anything to summon menu:\n").upper()
        if cmd == "A":
            category = None
            title = input("What would be the title of the mistake\n")
            if title not in data.Logs:
                dt = input("When did it happen? Enter by form 'Y-M-D'\n")
                while type(DATE(dt)) != datetime.date:
                    print("Syntax Error, enter the date in the form of '2020-01-04'")
                    dt = input()
                while category not in data.CAT:
                    for avaliable_cat in data.CAT:
                        print(avaliable_cat,end = ";")
                    category = input("Which Category does this task belongs to?\n")
                    
                    
                cause = input_splited("What lead to the mistake?\n")
                result = input_splited("What was the Consequence?\n")
                log = input_splited("Anything else to say?\n")
                tw = input_splited("What's the Take Away?\n")
                try:#try
                    data.add_mistake(title,dt,category,cause,result,log,tw)
                    okr_save(acc_file_path,data)
                except:
                    print("Syntax Error!")
            else:
                print("Mistake title already exist, use another one!")

        elif cmd == "S":
            try:
                print(data)
            except AttributeError:
                print("Pain Log is Empty, Enter [A] to add mistakes")
        elif cmd == "F":
            find_type = input("Would you like to find by [D]ate or by [C]ategory?\n").upper()
            if find_type == "D":
                dt = input("Please enter the correct date in the form of 'Y-M-D'\n")
                for mistake in data.Logs:
                    if data.Logs[mistake].date == dt:
                        print(data.Logs[mistake])
                        Q = input("Would You Like to Edit? [Y] or [N]\n")
                        if Q == "Y":
                            while True:
                                type_to_change = input("Which Part to change?\n"
                                            "【D】ate or 【C】ause or 【CAT】egory or 【R】esult or 【T】akea【W】ay ?\n"
                                            "【Exit】 to return to the Main Menu\n").upper()
                                if type_to_change == "EXIT":
                                    break
                                elif type_to_change == "CAT":
                                    print("Here are the avaliable categories:")
                                    for c in data.CAT:
                                        print(c,end=";")
                                    data.Logs[mistake].set_category(input("Change Category to:\n"))
                                elif type_to_change == "D":
                                    data.Logs[mistake].set_date(input("Change date to:\n"))
                                elif type_to_change == "C":
                                    data.Logs[mistake].set_cause(input("Change Cause to:\n"))
                                elif type_to_change == "R":
                                    data.Logs[mistake].set_result(input("Change Result to:\n"))
                                elif type_to_change == "TW":
                                    data.Logs[mistake].set_take_away(input("Change take_away to:\n"))
                                else: 
                                    print("Syntax Error")

            if find_type == "C":
                for c in data.CAT:
                    print(c,end=";")
                cat = input("Please enter the correct category from above:\n")
                for mistake in data.Logs:
                    if data.Logs[mistake].category == cat:
                        print(data.Logs[mistake])
                        print("*"*150)
        elif cmd == "CLEAR":
            Q = input("Are you sure that you wish to Empty the logs? [Y] or [N]\n")
            if Q == "Y":
                data.Logs = []
                print("Pain Logs Empted")

        elif cmd == "D":
            title = input("Please enter the title of the mistake you wish to delete:\n")
            try:
                Q = input("To delete the following mistake [Y] or [N] \n {}\n".format(data.Logs[title]))
                if Q == "Y":
                    data.Logs.pop(title)
                    OUTfile = open(file_path,"wb")
                    pickle.dump(data,OUTfile)
                    OUTfile.close()
                    print("Item {} Deleted".format(title))
            except:
                "Syntax Error"

        elif cmd == "SBD":
            n = int(input("How many days would you like to see?\n"))
            data.show_by_date(n)

        elif cmd == "V":
            menu_script = '''
            Welcome to Stream Mode, You will be reviewing all Mistakes in a chronological order.
            Feel free to make comments along the way, it will be stored at Log part.
            Enter 【C】omment to make comments
            Enter 【]】to view the Next one
            Enter 【[】revious to view the last one
            Enter 【R】eturn to Exit the Stream Mode.
            '''
            
            print(menu_script)
            PRINT = True
            while True:
                print("cmd is {}".format(cmd))
                try:
                    if PRINT:
                        print(data.Cursor)
                        print(data.sorted_date[data.Cursor.cursor])
                    else:
                        PRINT = True
                except :
                    data.reset_cursor()
                    print("‼️‼️__CURSOR RESET__‼️‼️")


                cmd = input("Enter Stream Mode CMD:(M for Menu)\n").upper()
                try:
                    cmd = int(cmd)
                except:
                    pass
                try:
                    cmd[0]
                except:
                    if type(cmd)!= int:
                        cmd = "NONE"
                if type(cmd) == int:
                    data.Cursor.cursor = cmd
                elif cmd[0] == "[":
                    data.Cursor.cursor -= len(cmd)
                elif cmd[0] == "]":
                    data.Cursor.cursor += len(cmd)
                elif cmd == "M":
                    PRINT = False
                    print(menu_script)
                elif cmd == "C":
                    Comment = input("Say something...\n")
                    data.sorted_date[data.Cursor.cursor].log = data.sorted_date[data.Cursor.cursor].log + "\n{}\n{}".format(str(date.today()),Comment)
                elif cmd == "R":
                    break

        elif cmd == "C":
            print("Here are the avaliable categories:")
            for c in data.CAT:
                print(c,end=";")
            Q = input("Would you like to [A]dd or [D]elete a category？\n")
            spec = input("please enter the name of the category.\n")
            if Q == "A":
                data.CAT_Add(spec)
                okr_save(acc_file_path,data)
            elif Q == "D":
                data.CAT_Delete(spec)
                okr_save(acc_file_path,data)

            
        elif cmd == "EXIT":
            # Save Data
            OUTfile = open(file_path,"wb")
            pickle.dump(data,OUTfile)
            OUTfile.close()
            return
        
        else:
            print("Command Menu:\n"
                "Enter [A]dd to add mistake to the pain logs\n"
                "Enter [S]how to show everything in the pain logs\n"
                "Enter [F] to find a specific mistake from the log\n"
                "Enter [CLEAR] to deafult the mistake logs\n"
                "Enter [D]elete to delete a specific mistake by its name\n"
                "Enter [S]how[B]y[D]ate to show everything ordered by date\n"
                "Enter [V]iew to Enter View Stream Mode\n"
                "Enter [C]ategory to eidt category. \n"
                "Enter [EXIT] to quit the program\n")
            

def okr_save(file_path,data):
    try:
        OUTfile = open(file_path,"wb")
        pickle.dump(data,OUTfile)
        OUTfile.close()
        print("Saved")
    except:
        print("Save Error")            
        
if __name__ == '__main__':
    PB(input("Input the file path of the PB save:\n"))