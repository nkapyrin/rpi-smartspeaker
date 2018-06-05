# encoding:utf-8
import os
import commands
from subprocess import PIPE, Popen, call, check_output

def say( text):
  process = Popen(['festival', '--tts'], stdin=PIPE)
  process.stdin.write(text + "\n")
  process.stdin.close()
  process.wait()

def rec( seconds=2, filename="test.wav" ):
  os.system('arecord -D hw:1,0 -d %d -f cd -r 16000 test.wav -c 1' % seconds)

def replay( filename="test.wav" ):
  os.system('aplay %s' % filename)

def stt( filename="test.wav" ):
  out = commands.getstatusoutput( 'pocketsphinx_continuous -infile %s -logfn /dev/null' % filename)
  return out[1].decode('utf-8')

def stt_rus( filename="test.wav" ):
  out = commands.getstatusoutput( 'pocketsphinx_continuous -infile %s -logfn /dev/null -hmm ~/Downloads/zero_ru_cont_8k_v3/zero_ru.cd_cont_4000 -dict ~/Downloads/zero_ru_cont_8k_v3/ru.dic -lm ~/Downloads/zero_ru_cont_8k_v3/ru.lm' % filename )
  return out[1].decode('utf-8')

def listen( seconds ):
  rec( seconds )
  return stt()
