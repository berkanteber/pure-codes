import time
import os, subprocess

for inputfilename in os.listdir('../inputs/files'):
    if inputfilename[-3:] != ".lp": continue

    resultfilename = inputfilename[:-8] + "result-sexequal.txt"

    start = time.time()
    command = "../../clingo/clingo --stats ../inputs/files/{} ../codes/smpti.lp ../codes/sexequal.lp 0".format(inputfilename)
    process = subprocess.run(command, shell = True, stdout = subprocess.PIPE)
    output = process.stdout.decode('utf-8')
    end = time.time()

    with open("files/{}".format(resultfilename), "w") as out:
        out.write(output)
        print("file:  {:50s}  time: {:09.2f} seconds".format(resultfilename, end - start))

    resultfilename = inputfilename[:-8] + "result-egalitarian.txt"

    start = time.time()
    command = "../../clingo/clingo --stats ../inputs/files/{} ../codes/smpti.lp ../codes/egalitarian.lp 0".format(inputfilename)
    process = subprocess.run(command, shell = True, stdout = subprocess.PIPE)
    output = process.stdout.decode('utf-8')
    end = time.time()

    with open("files/{}".format(resultfilename), "w") as out:
        out.write(output)
        print("file:  {:50s}  time: {:09.2f} seconds".format(resultfilename, end - start))

    resultfilename = inputfilename[:-8] + "result-minregret.txt"

    start = time.time()
    command = "../../clingo/clingo --stats ../inputs/files/{} ../codes/smpti.lp ../codes/minregret.lp 0".format(inputfilename)
    process = subprocess.run(command, shell = True, stdout = subprocess.PIPE)
    output = process.stdout.decode('utf-8')
    end = time.time()

    with open("files/{}".format(resultfilename), "w") as out:
        out.write(output)
        print("file:  {:50s}  time: {:09.2f} seconds".format(resultfilename, end - start))

    print("")
