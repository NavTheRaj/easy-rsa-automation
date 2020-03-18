#!/home/navraj/env/bin/python
from subprocess import Popen,PIPE
#import shutil

def run_easyrsa(username):
	proc_private=Popen(['./easyrsa','gen-req',username,'nopass'],stdin=PIPE,stdout=PIPE)
	proc_private.communicate(username+'\n')


	proc_pub=Popen(['./easyrsa','sign-req','client',username],stdin=PIPE,stdout=PIPE)
	proc_pub.communicate('yes\n')

def make_zip(username):
#	shutil.make_archive(username,'zip','VPN-FILE/'+username+'/') #ZIPPING USER FOLDER
	proc_make_zip=Popen(['zip','-r',username+'.zip','VPN-FILE/'+username+'/'])  #MAKING ZIP FOLDE
	proc_move_zip=Popen(['mv',username+'.zip','VPN-FILE/'+username+'/'])  #MOVING ZIP FOLDER TO USER FOLDER

def make_folder(username):
	proc_make_dir=Popen(['mkdir','VPN-FILE/'+username]) #MAKING USER-SPECIFIC DIRECTORY
	proc_copy_usercrt=Popen(['cp','pki/issued/'+username+'.crt','VPN-FILE/'+username+'/']) #COPYING .crt FILE TO USER FOLDER
	proc_copy_guide=Popen(['cp','pki/vpnConnectionGuide.txt','VPN-FILE/'+username+'/']) #COPYING GUIDE TEXT FILE TO USER FOLDER
	proc_copy_crt=Popen(['cp','pki/ca.crt','VPN-FILE/'+username+'/']) # COPYING .crt FILE TO USER FOLDER
	proc_copy_ovpn=Popen(['cp','pki/client.ovpn','VPN-FILE/'+username+'/']) #COPYING .ov[pn FILE TO USER FOLDER
	proc_copy_userkey=Popen(['cp','pki/private/'+username+'.key','VPN-FILE/'+username+'/']) #COPYING .key FILE TO USER FOLDER
	#shutil.make_archive(username,'zip','VPN-FILE/'+username+'/') #ZIPPING USER FOLDER
	#proc_move_zip=Popen(['mv',username+'.zip','VPN-FILE/'+username+'/'])  #MOVING ZIP FOLDER TO USER FOLDER
	
def main():
	f=open("user.txt","r+") #CHANGE THE USER INFO TEXT FILE AS REQUIREMENT [IT MUST BE IN FORMAT <username> <useremail>]
	user_list=[x.split() for x in f]
	for i in range(len(user_list)):
		print("<----------Making RSA certificate----->")
		run_easyrsa(user_list[i][0]) #passing client name to make its rsa files
		print("<-----------------RSA Operation Completed!--------------------->")
		print("<-----------------ZIPPING THE FILES--------------------->")
		make_folder(user_list[i][0])
		make_zip(user_list[i][0])

main()
