from datetime import time, datetime
import time
import random

outputfile = 'Output/output.txt'

runstart = datetime.now()
# Counter variables
totpausetime = 0
loopcount = 0
tot_time = time.time()



# Infinite loop
while runstart <= datetime.now():
    for i in range(1,2):
        loop_start = datetime.now()
        
        # Pause for random intervals
        pausetime = random.uniform(0.0,0.99)**2
        time.sleep(pausetime)

        # Generate random numbers
        number = random.randrange(1000,9999)
        
        # Update counters
        loopcount += 1
        totpausetime += pausetime
        loop_end = datetime.now()
        loop_time = loop_end - loop_start
        tot_time = loop_end - runstart

        # Print random output
        randomoutput = (
                f">>cmd.prmpt/../f/input.csv time={loop_end} "
                f"cdir ip/#!stamp c{loopcount}:{number*2:05d}:{number*1.1:.1f} "
                f"p{totpausetime:.3f}/tot=<{tot_time}s>\n"
                )
        print(randomoutput,end="")
        with open(outputfile,"a") as txt_file:
            txt_file.write(randomoutput)
            


