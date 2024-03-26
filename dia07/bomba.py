import sys, time

print(sys.argv) #['dia7/bomba.py', '8']
print(sys.argv[0])
print(sys.argv[1])

i = int(sys.argv[1])

while i > 0:
    print(f"El valor de i {i}")
    time.sleep(1)    # tiempo de espera 1 segundo
    i -= 1           # decrementando (restando 1)