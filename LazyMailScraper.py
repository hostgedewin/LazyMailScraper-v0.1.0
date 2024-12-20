import os
import requests
import tkinter as tk
from tkinter import messagebox

import whois
from threading import Thread
import pyautogui

# Made By Hostgede.win
# Published in 12/18/2024
# https://hostgede.win/
# https://hostgede.win/blogs.php?title=LazyMailScraper+v0.1.0+Documentation&fbclid=IwY2xjawHR22hleHRuA2FlbQIxMAABHYEiJHiT0RUMRYW-lTZ5kyvFYkm2b4FZRYqISrAQVy55134i9nOP0B9K_A_aem_ZgBdKfpzuFEEMKvghdZbIg

def commandLineConsole():
    mainP()

def mainP():
    def findEmails():
        while True:
            try:
                msg = ""
                r = requests.get('https://random-word-api.herokuapp.com/word')
                old_string = str(r.text)
                new_string = old_string.strip('[""]')
                word = str("{}".format(new_string) + ".com")

                try:
                    w = whois.whois(word)
                    wp = str(w.emails)
                    wp = wp.strip('[]')
                    wp = wp.replace("'", "")  # Remove single quotes
                    wp = wp.replace(", ", "\n")  # Separate emails with newline character

                    email_keywords = [
                        '@gmail.com', '@yahoo.com', '@outlook.com', '@hotmail.com', '@aol.com', '@icloud.com', '@protonmail.com',
                        '@yandex.com', '@yandex.ru', '@zoho.com', '@gmx.com', '@mail.com', '@me.com', '@mac.com', '@tutanota.com',
                        '@fastmail.com', '@hushmail.com', '@mail.ru', '@qq.com', '@163.com', '@rediffmail.com', '@comcast.net',
                        '@cox.net', '@charter.net', '@sbcglobal.net', '@verizon.net', '@att.net', '@naver.com', '@daum.net',
                        '@web.de', '@1und1.de', '@t-online.de', '@orange.fr', '@freemail.hu', '@lycos.com', '@earthlink.net',
                        '@netzero.net', '@rocketmail.com', '@inbox.com', '@excite.com', '@hush.com', '@optusnet.com.au', '@blueyonder.co.uk',
                        '@ntlworld.com', '@o2.pl', '@bigpond.com', '@wanadoo.fr', '@centrum.cz', '@abv.bg', '@aim.com', '@alice.it',
                        '@ameritech.net', '@armyspy.com', '@atmc.net', '@bellsouth.net', '@bigpond.net.au', '@bigstring.com',
                        '@bol.com.br', '@boun.edu.tr', '@btinternet.com', '@centrum.sk', '@comporium.net', '@dbmail.com', '@embarqmail.com',
                        '@etisalat.net', '@fastwebnet.it', '@fiber.net.il', '@frontier.com', '@gawab.com', '@gci.net', '@globe.com.ph',
                        '@gmx.at', '@gmx.de', '@go.com', '@grr.la', '@hinet.net', '@home.nl', '@homestead.com', '@ice.is', '@juno.com',
                        '@kpnmail.nl', '@laposte.net', '@libero.it', '@live.com', '@love.com', '@luno.com', '@magma.ca', '@mchsi.com',
                        '@mediacombb.net', '@msn.com', '@neuf.fr', '@o2.pl', '@optonline.net', '@optusnet.com.au', '@orange.fr',
                        '@otenet.gr', '@poczta.fm', '@qwest.net', '@rambler.ru', '@roadrunner.com', '@seznam.cz', '@shentel.net',
                        '@skynet.be', '@sympatico.ca', '@telenet.be', '@telia.com', '@terra.com.br', '@tiscali.co.uk', '@tvcablenet.be',
                        '@ultrashock.com', '@umich.edu', '@usc.edu', '@verizon.net', '@videotron.ca', '@virgin.net', '@vodafone.com',
                        '@wanadoo.fr', '@wayn.com', '@windstream.net', '@wowway.com', '@wp.pl', '@xtra.co.nz', '@y7mail.com', '@ya.ru',
                        '@yahoo.com', '@yandex.ru', '@ymail.com', '@zoho.com'
                    ]

                    for keyword in email_keywords:
                        if keyword in wp:
                            commandLine.insert(tk.END, wp)
                            commandLine.insert(tk.END, "\n")
                            save_emails(wp)  # Save the emails to a text file
                            break
                except:
                    commandLine.insert(tk.END, msg)
            except:
                commandLine.insert(tk.END, msg)

    def save_emails(emails):
        with open('email_list.txt', 'a') as file:
            file.write(emails + '\n')

    t = Thread(target=findEmails)
    t.start()

def select_all():
    commandLine.tag_add("sel", "1.0", "end")
    commandLine.tag_config("sel", background="#000000", foreground="#FFFFFF")

def copy_select():
    pyautogui.hotkey('ctrl', 'c')

def delete():
    commandLine.delete('sel.first', 'sel.last')

root = tk.Tk()
root.resizable(0, 0)
root.title("LazyMailScraper v0.1.0")
root.configure(background="#090909")

label1 = tk.Label(root, text="CLICK ON THE BUTTON TO START SCRAPING THE WEB FOR EMAILS", background="#090909",
                  foreground="#00ff00")
label1.pack()
button1 = tk.Button(root, text="FIND RANDOM EMAILS", background="#090909", foreground="#00ff00",
                    command=commandLineConsole)
button1.pack()

frame1 = tk.Frame(root)
commandLine = tk.Text(frame1, height=15, width=70, background="#2f2f2f", foreground="#00ff00")

scrollbar = tk.Scrollbar(frame1, command=commandLine.yview)

frame1.pack()
scrollbar.pack(side="right", fill=tk.Y)
commandLine.pack()
commandLine['yscrollcommand'] = scrollbar.set

label2 = tk.Label(root, text="hostgede.win", background="#090909", foreground="#00ff00", font=("Arial", 10, "bold")) # LET SEE

label2.pack(side=tk.RIGHT)
button2 = tk.Button(root, text="Select All", background="#090909", foreground="#00ff00", command=select_all)
button2.pack(side=tk.LEFT)
button3 = tk.Button(root, text="Copy All", background="#090909", foreground="#00ff00", command=lambda: copy_select())
button3.pack(side=tk.LEFT)
button4 = tk.Button(root, text="Clean", background="#090909", foreground="#00ff00", command=delete)
button4.pack(side=tk.LEFT)

root.mainloop()
