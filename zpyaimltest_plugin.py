#===istalismanplugin===
# -*- coding: utf-8 -*-

#  Talisman plugin
#  zpyaiml_plugin.py

#  edited by planb(planb@talkonaut.com)

#  Initial Copyright © 2002-2005 Mike Mintz <mikemintz@gmail.com>
#  Modifications Copyright © 2007 Als <Als@exploit.in>

#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

import aiml
import string
from string import *
import os.path
import os
import sys
import marshal

global k
k = aiml.Kernel()

def load_session():
   sessionFile = file("sesid.ses", "rb")
   marshal.load(sessionFile)
   session = 
   for pred,value in session.items():
       k.setPredicate(pred, value, "_global")
#       print 'loaded sesid.ses'

def save_session():
    session = k.getSessionData()
    sessionFile = file("sesid.ses", "wb")
    marshal.dump(session, sessionFile)
#    sessionFile.close()

def chat_pyaiml(type, source, body):
    replyy = k.respond(body, get_true_jid(source))
    reply(type, source, replyy)
    save_session()

def handler_pyaiml(type, source, body):
    if type == 'private': 
		if not COMMANDS.has_key(string.split(body)[0]):
                    chat_pyaiml(type, source, body)
    if type == 'public'and get_bot_nick(source[1])!=source[2] and source[2]!='' and re.search('^'+get_bot_nick(source[1])+':',body)!=None:
                if not COMMANDS.has_key(string.split(body)[1]):
                    chat_pyaiml(type, source, body.replace(get_bot_nick(source[1])+':','').strip())

register_message_handler(handler_pyaiml)

if os.path.isfile("alice.brn"):
    k.bootstrap(brainFile = "alice.brn")
    pass
    k.setBotPredicate("name","Alice")
    k.getBotPredicate("Alice")
    

if __name__ == "__main__":
	load_session()
	pass
