import os, time, subprocess
from colorama import Fore, Style
def showpassword(uuid):
  try:
    showkey = subprocess.check_output(f'netsh wlan show profile name="{uuid}" key=clear | findstr Contenu', shell=True)
    f = open("tempfile.txt", "wb")
    f.write(showkey)
    f.close()
    f = open("tempfile.txt", "r")
    for decodekey in f:
      key = str(decodekey).split(": ")[1]
    f.close()
    os.remove("tempfile.txt")
    return key
  except subprocess.CalledProcessError as e:
    key = "invalid"
    return key
  
def uuidporfile():
  showprofile = subprocess.check_output("netsh wlan show profile | findstr Tous", shell=True)
  t1 = time.strftime("%A %d %B %Y %H:%M:%S")
  f = open("tempfile2.txt", "wb")
  f.write(showprofile)
  f.close()
  f = open("tempfile2.txt", "r")
  t2 = time.strftime("%A_%d_%B_%Y")
  flog = open(t2+".txt", "a")
  for profiles in f:
    profiles = profiles.split(": ")[1].strip()
    ps = showpassword(profiles).strip()
    
    if ps == "invalid":
      result = f"[{t1}] | I dont find the password on {profiles}\n"
      print(Fore.RED + result + Style.RESET_ALL)
      flog.write(result)
    else:
      result = f"[{t1}] | Password: {ps} on {profiles}.\n"
      print(Fore.GREEN + result + Style.RESET_ALL)
      flog.write(result)

  
  flog.close()
  f.close()
  os.remove("tempfile2.txt")

def main():
  os.system("cls")
  uuidporfile()




main()
