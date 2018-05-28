import itertools
import numpy as np
import time, os, subprocess
import subprocessmethodrun

percentages = [25, 50, 100]
inputsizes = [20, 40, 60]
ties = [0, 10, 20]

for m_input, w_input in itertools.product(inputsizes, inputsizes):
    for m_percent, w_percent in itertools.product(percentages, percentages):
        for m_ties, w_ties in itertools.product(ties, ties):
            if m_input > w_input or m_percent > w_percent or m_ties > w_ties:
                continue
            else:
                fileprefix = "m-{}-w-{}--m-{}pc-w-{}pc--m-{}pc-w-{}pc".format(m_input, w_input, m_percent, w_percent, m_ties, w_ties)
                inputfilename = "../files-new/" + fileprefix + "--input.lp"

            #### no opt smpti

            if not os.path.isfile("files/{}--result.txt".format(fileprefix)):
                resultfilename = "files" + inputfilename[12:-8] + "result.txt"

                command = "clingo --stats --time-limit=1000 {} ../codes/smpti-v3.lp 1".format(inputfilename)
                retcode, stdout, stderr = subprocessmethodrun.run(command, shell = True, stdout = subprocess.PIPE)
                output = stdout.decode('utf-8')

                if stderr and stderr.decode('utf-8').find("INTERRUPTED") > -1:
                    time = None
                    print("file:  {:80s}\n--> TIMEOUT".format(resultfilename))
                else:
                    lines= [line for line in output.split('\n') if line.find('CPU Time') > -1]
                    if len(lines) > 0: print("file:  {:80s}\n--> {}".format(resultfilename, lines[0]))
                    else: print("file:  {:80s}\n--> ERROR".format(resultfilename))

                with open(resultfilename, "w") as out: out.write(output)

            #### sex equal smpti

            if not os.path.isfile("files/{}--result-sexequal.txt".format(fileprefix)):
                resultfilename = "files" + inputfilename[12:-8] + "result-sexequal.txt"

                command = "clingo --stats --time-limit=1000 {} ../codes/smpti-v3.lp ../codes/sexequal-new.lp 0".format(inputfilename)
                retcode, stdout, stderr = subprocessmethodrun.run(command, shell = True, stdout = subprocess.PIPE)
                output = stdout.decode('utf-8')

                if stderr and stderr.decode('utf-8').find("INTERRUPTED") > -1:
                    time = None
                    print("file:  {:80s}\n--> TIMEOUT".format(resultfilename))
                else:
                    lines= [line for line in output.split('\n') if line.find('CPU Time') > -1]
                    if len(lines) > 0: print("file:  {:80s}\n--> {}".format(resultfilename, lines[0]))
                    else: print("file:  {:80s}\n--> ERROR".format(resultfilename))

                with open(resultfilename, "w") as out: out.write(output)

            #### egalitarian smpti

            if not os.path.isfile("files/{}--result-egalitarian.txt".format(fileprefix)):
                resultfilename = "files" + inputfilename[12:-8] + "result-egalitarian.txt"

                command = "clingo --stats --time-limit=1000 {} ../codes/smpti-v3.lp ../codes/egalitarian-new.lp 0".format(inputfilename)
                retcode, stdout, stderr = subprocessmethodrun.run(command, shell = True, stdout = subprocess.PIPE)
                output = stdout.decode('utf-8')

                if stderr and stderr.decode('utf-8').find("INTERRUPTED") > -1:
                    time = None
                    print("file:  {:80s}\n--> TIMEOUT".format(resultfilename))
                else:
                    lines= [line for line in output.split('\n') if line.find('CPU Time') > -1]
                    if len(lines) > 0: print("file:  {:80s}\n--> {}".format(resultfilename, lines[0]))
                    else: print("file:  {:80s}\n--> ERROR".format(resultfilename))

                with open(resultfilename, "w") as out: out.write(output)

            #### minimum regret smpti

            if not os.path.isfile("files/{}--result-minregret.txt".format(fileprefix)):
                resultfilename = "files" + inputfilename[12:-8] + "result-minregret.txt"

                command = "clingo --stats --time-limit=1000 {} ../codes/smpti-v3.lp ../codes/minregret-new.lp 0".format(inputfilename)
                retcode, stdout, stderr = subprocessmethodrun.run(command, shell = True, stdout = subprocess.PIPE)
                output = stdout.decode('utf-8')

                if stderr and stderr.decode('utf-8').find("INTERRUPTED") > -1:
                    time = None
                    print("file:  {:80s}\n--> TIMEOUT".format(resultfilename))
                else:
                    lines= [line for line in output.split('\n') if line.find('CPU Time') > -1]
                    if len(lines) > 0: print("file:  {:80s}\n--> {}".format(resultfilename, lines[0]))
                    else: print("file:  {:80s}\n--> ERROR".format(resultfilename))

                with open(resultfilename, "w") as out: out.write(output)

            #### maximum cardinality smpti

            if not os.path.isfile("files/{}--result-maxcardinality.txt".format(fileprefix)):
                resultfilename = "files" + inputfilename[12:-8] + "result-maxcardinality.txt"

                command = "clingo --stats --time-limit=1000 {} ../codes/smpti-v3.lp ../codes/maxcardinality-new.lp 0".format(inputfilename)
                retcode, stdout, stderr = subprocessmethodrun.run(command, shell = True, stdout = subprocess.PIPE)
                output = stdout.decode('utf-8')

                if stderr and stderr.decode('utf-8').find("INTERRUPTED") > -1:
                    time = None
                    print("file:  {:80s}\n--> TIMEOUT".format(resultfilename))
                else:
                    lines= [line for line in output.split('\n') if line.find('CPU Time') > -1]
                    if len(lines) > 0: print("file:  {:80s}\n--> {}".format(resultfilename, lines[0]))
                    else: print("file:  {:80s}\n--> ERROR".format(resultfilename))

                with open(resultfilename, "w") as out: out.write(output)

            print("")
