import itertools
import numpy as np
import time, os, subprocess
import subprocessmethodrun

percentages = [25, 50, 100]
inputsizes = [30, 60, 90, 120]
ties = [0, 10, 20]

for m_input, w_input in itertools.product(inputsizes, inputsizes):
    for m_percent, w_percent in itertools.product(percentages, percentages):
        for m_ties, w_ties in itertools.product(ties, ties):
            if m_input > w_input or m_percent > w_percent or m_ties > w_ties:
                continue
            else:
                fileprefix = "m-{}-w-{}--m-{}pc-w-{}pc--m-{}pc-w-{}pc".format(m_input, w_input, m_percent, w_percent, m_ties, w_ties)
                inputfilename = "files/" + fileprefix + "--input.lp"

            #### no opt smpti

            if not os.path.isfile("files/{}--result.txt".format(fileprefix)):            
                resultfilename = inputfilename[:-8] + "result.txt"

                start = time.time()
                command = "clingo --stats {} ../codes/smpti.lp 1".format(inputfilename)
                retcode, stdout, stderr = subprocessmethodrun.run(command, shell = True, stdout = subprocess.PIPE)
                output = stdout.decode('utf-8')
                end = time.time()

                with open(resultfilename, "w") as out:
                    out.write(output)
                    print("file:  {:80s}  time: {:09.2f} seconds".format(resultfilename, end - start))

            #### sex equal smpti

            if not os.path.isfile("files/{}--result-sexequal.txt".format(fileprefix)) and m_input <= 30 and w_input <= 30:
                resultfilename = inputfilename[:-8] + "result-sexequal.txt"

                start = time.time()
                command = "clingo --stats {} ../codes/smpti.lp ../codes/sexequal.lp 0".format(inputfilename)
                retcode, stdout, stderr = subprocessmethodrun.run(command, shell = True, stdout = subprocess.PIPE)
                output = stdout.decode('utf-8')
                end = time.time()

                with open(resultfilename, "w") as out:
                    out.write(output)
                    print("file:  {:80s}  time: {:09.2f} seconds".format(resultfilename, end - start))

            #### egalitarian smpti

            if not os.path.isfile("files/{}--result-egalitarian.txt".format(fileprefix)) and m_input <= 30 and w_input <= 30:
                resultfilename = inputfilename[:-8] + "result-egalitarian.txt"

                start = time.time()
                command = "clingo --stats {} ../codes/smpti.lp ../codes/egalitarian.lp 0".format(inputfilename)
                retcode, stdout, stderr = subprocessmethodrun.run(command, shell = True, stdout = subprocess.PIPE)
                output = stdout.decode('utf-8')
                end = time.time()

                with open(resultfilename, "w") as out:
                    out.write(output)
                    print("file:  {:80s}  time: {:09.2f} seconds".format(resultfilename, end - start))

            #### minimum regret smpti

            if not os.path.isfile("files/{}--result-minregret.txt".format(fileprefix)):
                resultfilename = inputfilename[:-8] + "result-minregret.txt"

                start = time.time()
                command = "clingo --stats {} ../codes/smpti.lp ../codes/minregret.lp 0".format(inputfilename)
                retcode, stdout, stderr = subprocessmethodrun.run(command, shell = True, stdout = subprocess.PIPE)
                output = stdout.decode('utf-8')
                end = time.time()

                with open(resultfilename, "w") as out:
                    out.write(output)
                    print("file:  {:80s}  time: {:09.2f} seconds".format(resultfilename, end - start))

            #### maximum cardinality smpti

            if not os.path.isfile("files/{}--result-maxcardinality.txt".format(fileprefix)):
                resultfilename = inputfilename[:-8] + "result-maxcardinality.txt"

                start = time.time()
                command = "clingo --stats {} ../codes/smpti.lp ../codes/maxcardinality.lp 0".format(inputfilename)
                retcode, stdout, stderr = subprocessmethodrun.run(command, shell = True, stdout = subprocess.PIPE)
                output = stdout.decode('utf-8')
                end = time.time()

                with open(resultfilename, "w") as out:
                    out.write(output)
                    print("file:  {:80s}  time: {:09.2f} seconds".format(resultfilename, end - start))

            print("")
