 
import platform , os
import sys, time
import getpass
from configparser import ConfigParser 



def hprint(s , speed=8/5000 ):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(speed)




__platform = ((platform.system()))



color = {
    'white':    "\033[1;37m",
    'yellow':   "\033[1;33m",
    'green':    "\033[1;32m",
    'blue':     "\033[1;34m",
    'cyan':     "\033[1;36m",
    'red':      "\033[1;31m",
    'magenta':  "\033[1;35m",
    'black':      "\033[1;30m",
    'darkwhite':  "\033[0;37m",
    'darkyellow': "\033[0;33m",
    'darkgreen':  "\033[0;32m",
    'darkblue':   "\033[0;34m",
    'darkcyan':   "\033[0;36m",
    'darkred':    "\033[0;31m",
    'darkmagenta':"\033[0;35m",
    'darkblack':  "\033[0;30m",
    'off':        "\033[0;0m"
}


R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'




CEND      = '\33[0m'
CBOLD     = '\33[1m'
CITALIC   = '\33[3m'
CURL      = '\33[4m'
CBLINK    = '\33[5m'
CBLINK2   = '\33[6m'
CSELECTED = '\33[7m'


CBLACKBG  = '\33[40m'
CREDBG    = '\33[41m'
CGREENBG  = '\33[42m'
CYELLOWBG = '\33[43m'
CBLUEBG   = '\33[44m'
CVIOLETBG = '\33[45m'
CBEIGEBG  = '\33[46m'
CWHITEBG  = '\33[47m'

CGREY    = '\33[90m'
CRED2    = '\33[91m'
CGREEN2  = '\33[92m'
CYELLOW2 = '\33[93m'
CBLUE2   = '\33[94m'
CVIOLET2 = '\33[95m'
CBEIGE2  = '\33[96m'
CWHITE2  = '\33[97m'

CGREYBG    = '\33[100m'
CREDBG2    = '\33[101m'
CGREENBG2  = '\33[102m'
CYELLOWBG2 = '\33[103m'
CBLUEBG2   = '\33[104m'
CVIOLETBG2 = '\33[105m'
CBEIGEBG2  = '\33[106m'
CWHITEBG2  = '\33[107m'

fistlogoclor = "\033[1;37m"
fistlogoclor = "\033[1;34m"

secondlogocolor= "\033[1;94m"
secondlogocolor= "\033[1;94m"

CBLACK  = '\33[30m'
CRED    = '\33[31m'
CGREEN  = '\33[32m'
CYELLOW = '\33[33m'
CBLUE   = '\33[34m'
CVIOLET = '\33[35m'
CBEIGE  = '\33[36m'
CWHITE  = '\33[37m'


name =f"""

        ██╗███████╗ ███████╗   ██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗     
        ██║██╔════╝ ██╔════╝   ██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗    
        ██║███████╗ █████╗     ███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝    
        ██║╚════██║ ██╔══╝     ██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗    
        ██║███████║ ███████╗   ██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║    
        ╚═╝╚══════╝ ╚══════╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    
                                                                  

    {W}"""


def main()  : 

	exit = False 
	if __platform =="Windows" : 
		os.system('cls')
	else : 
		os.system('clear')
    # print(exit
	# while not exit : 

	print(name)
	hprint(f'                        {C}Switch Port Authentication Based Hunter{W}')                        
	print('\n'*2)
	hprint(f'                         {G} Initial Configuration  {W}                           ')



	print(''*4)

def decrypt(file,password ):
    global leghtpath
    import pyAesCrypt

    # print('-' * 80)
    # password = "'''+str(password)+'''"
    buffer_size = 512 * 1024
    pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, buffer_size)

    filename = W+str(file[:-4]) 
    # path ="C:/Users/Brahim/Desktop/programming/pytho/test-encry/fsocity - Copie (10).jpg.crp"

    # print(path)
    # left  = "[ Encrypt ]" 
    # left = '[ Decrypting ]' 

    # right = '[ ok ]'

    # filename=f'{filename[:10]}..........{filename[-25:]}'
    # # print('password: ', password)
    # if platform.platform()=='Windows' :

    #     print( f'{left:<10}  {filename :<30} {right:<10}')
    # else :
    #     print( f'{left:<10}  {filename :<50} {right:<10}')
    os.remove(file)



def crypt(file,password):
    global leghtpath
    # global password , lenfile
    import pyAesCrypt
    # lenfile = len(file)

    # print(file) 
    # print(password)
    # print('-' * lenfile)
    password = str(password)
    buffer_size = 512*1024
    pyAesCrypt.encryptFile((file), (file) + ".crp", password, buffer_size)
    
    # filename = W+str(file)+".crp" 
    # # path ="C:/Users/Brahim/Desktop/programming/pytho/test-encry/fsocity - Copie (10).jpg.crp"

    # left = '[ Encryting ]' 

    # right = '[ Ok ]'

    # filename=f'{filename[:10]}..........{filename[-25:]}'
    # # print('password: ', password)
    # if platform.platform()=='Windows' :

    #     print( f'{left:<10}  {filename :<30} {right:<10}')
    # else :
    #     print( f'{left:<10}  {filename :<50} {right:<10}')
  

    os.remove(file)


 


def Configuration_init() : 
	username   = input(f'{CRED} [{CWHITE} + {CRED}] {C}Please Provide your Radius username: '+W)
	password   = getpass.getpass(prompt=R+f'{CRED} [{CWHITE} + {CRED}] {C} Please Provide Your Radius Password : ' +C)
	password1  = getpass.getpass(prompt=R+f'{CRED} [{CWHITE} + {CRED}] {C} Please Confirme Your Radius Password : ' +C)

	while password !=  password1 : 
		print()
		print(f'{CWHITE} [ {CRED}Error {W}]   {CRED}The Provided Password Doesn\'t match') 
		password   = getpass.getpass(prompt=R+f'{CRED} [{CWHITE} + {CRED}] {C} Please Provide Your Radius Password : ' +C)
		password1  = getpass.getpass(prompt=R+f'{CRED} [{CWHITE} + {CRED}] {C} Please Confirme Your Radius Password : ' +C)


	with open ('parametre.ini','w') as f : 
			f.write('[credentials]\n')
			f.write('fisttimeinprogram =\n')
			f.write('username =\n')
			f.write('password =')
			
	# 	crypt('parametre.ini','P@55w0rd')
	# decrypt('parametre.ini.crp','P@55w0rd')

	config = ConfigParser()
	config.read('parametre.ini')

	firstTime = config.set('credentials','fistTimeInProgram','False')
	username  = config.set('credentials','username',username)
	password  = config.set('credentials','password',password)
		
	with open('parametre.ini', 'w') as configfile:
		config.write(configfile)


	crypt('parametre.ini','P@55w0rd')

	print(f'{G}[{W}+{G}]{W} The Username And Password has been Sent ...! {G}[{W}+{G}]{W}')
	print()
	input('[ + ] Press Any key To Exit .... ! ')
main()
Configuration_init()
