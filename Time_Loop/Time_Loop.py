from datetime import time, datetime
import time
import random

outputfile = 'Output/output.txt'

runstart = datetime.now()
# Counter variables
totpausetime = 0
loopcount = 0
tot_time = time.time()

def generate_key(length):
    letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers=['0','1','2','3','4','5','6','7','8','9']
    ln=['n','n','n','l','l']
    key = []
    for i in range(length):
        pick=random.choice(ln)
        if pick=='n':
            key.append(random.choice(numbers))
        elif pick == 'l':
            key.append(random.choice(letters))
    fullkey = "".join(key)
    return fullkey

# Infinite loop
while True:
    for i in range(1,2):
        loop_start = datetime.now()
        
        # Pause for random intervals
        pausetime = random.uniform(0.0,0.99)**3
        time.sleep(pausetime)

        # Generate random numbers
        number = random.randrange(1000,9999)
        
        # Update counters
        loopcount += 1
        totpausetime += pausetime
        loop_end = datetime.now()
        loop_time = loop_end - loop_start
        tot_time = loop_end - runstart

        # Function Key
        instance_key = generate_key(8)

        # Print random output
        randomoutput = (
                f">>cmd.prmpt/..st_time={loop_start} "
                f"cdir ip/#!stamp c{loopcount}:{number*2:05d} // {totpausetime:.15f}\n"
                f"   [pw.{instance_key}] time={loop_end}>./input.csv --p{int(number/10)}:{pausetime:.4f}/tot=<{tot_time}s>\n\n"
                )
        print(randomoutput,end="")
        with open(outputfile,"a") as txt_file:
            txt_file.write(randomoutput)
            


