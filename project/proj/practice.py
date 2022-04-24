import time,sys,os

for sr, w in enumerate(['hello', 'bye', 'tata'], start=1):
    # print(f"{sr}# word:" + w, end='\r')
    sys.stdout.write(w)
    sys.stdout.flush()
    time.sleep(2)

os.system('cls')