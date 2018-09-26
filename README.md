# RTR105
*Datormācības kursa elektroniskā klāde*  
CTRL + ALT + T - atvēras loga "Terminal"  
CTRL + SHIFT + T - atvēras papildloga logā "Terminal"  
U + TAB x2 - komandu saraksts  
CTRL + L - nodzēst visu logā  
  
***
  *12.09.2018*  
**uname** - command  
**man uname** - print certain system information  
**uname -a** - print all information, in the following order  
**echo $0** - bash / shell language or a 'friendly'one
**sh** - 'unfriendly'shell language  
**whoami** - prints the effective user ID  
**who** - reports which users are logged in to the system  
**pwd** - prints the name of the working directory  
**ls** - is a Linux shell command that lists directory contents of files and directories  
**ls -l** - list with long format - show permissions  
**ls -a** - list all files including hidden file starting with '.'  
**ls -ls** - list with long format with file size  
**ls -la** - list long format including hidden files  
**history** - a history command  

***
  *17.09.2018*  
**cd** - pārvietošanas komanda  
*example: cd /Music*    
LAI PĀRIETU UZ HOME:  
**home/user/**  
*example 1: cd /home/user/*  
*example 2: cd + enter*  
*example 3: cd +* ~  
**~** - relatīva adrese  
**/** - absolūta adrese  
**mkdir** - mapes izveidošanas komanda  
**rmdir** - mapes dzēšanas komanda  
**rm** - remove files or directory  
**echo** - komanda,kura attēlo tekstu  
*example 1: echo "Teksts"*  
*example 2: echo "Teksts + enter  
Teksts  
Teksts  
"  
=>  Teksts  
    Teksts  
    Teksts*    
vai  
*example 3: echo -e "Teksts\nTeksts\nTeksts"*  
Izmantojot >> , mēs varam papildināt jau ēsošo tekstu.  
*example: echo "Teksts" >> fails1.txt*  
**cat** - teksta attēlošanas komanda  
**more** vai **less** - citas komandas, kuras uzrada tekstu dažādos veidos  
**nano** - komanda lai modificētu tekstu  
*example: nano fails1.txt*  
**chmod** - lai edītu tiesības  
*example: chmod 540 fails1.txt*  
Un vairs mēs to nevaram modificēt.  
**cp** - komanda, kura nokopē mapi  
*example: cp fails1.txt fails101.txt*  
**mv** - komanda, kura pārnes failus un mapes / var nomainīt nosaukumu  
*example: mv *1*.txt Music/* (pārnesa)  
*example: mv fails101.txt fails103.txt* (nomainīja nosaukumu)  
**rm** - komanda lai nodzēstu failu  
*example: rm Music/fails101.txt*  
*example: rm fails**.*txt* (nodzēsa visus failus ar nosaukumu "fails")  

***  
 *26.09.2018*  
**nano mans_skripts.sh** - komanda, lai izveidotu savu skriptu ar Shell valodu  
**#!/bin/bash/** - kāds interpriators, kas nosaka mūsu darbības  
**$PATH** - tells the shell which directories to search for executable files  
**PATH=$PATH:~** - izdara tā, lai komanda būtu pieejama no home/user  


   
