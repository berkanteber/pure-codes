import itertools
import numpy as np
import time, os, subprocess
import subprocessmethodrun

percentages = [25, 50, 100]
inputsizes = [10, 20, 30, 40, 50, 60]
ties = [0, 10, 20]
stddev = 10

for m_input, w_input in itertools.product(inputsizes, inputsizes):
    for m_percent, w_percent in itertools.product(percentages, percentages):
        for m_ties, w_ties in itertools.product(ties, ties):
            fileprefix = "m-{}-w-{}--m-{}pc-w-{}pc--m-{}pc-w-{}pc".format(m_input, w_input, m_percent, w_percent, m_ties, w_ties)

            #### input generation

            if not os.path.isfile("files/{}--input.lp".format(fileprefix)):
                #### determine length of preference lists

                m_dist = np.full(m_input, w_input) if m_percent == 100 else ((stddev / 100) * np.random.randn(m_input) + (m_percent / 100)) * w_input
                w_dist = np.full(w_input, m_input) if w_percent == 100 else ((stddev / 100) * np.random.randn(w_input) + (w_percent / 100)) * m_input

                m_rounded = [int(round(x)) for x in m_dist]
                w_rounded = [int(round(x)) for x in w_dist]

                for x in m_rounded:
                    if x > w_input: x = w_input
                    elif x < 0: x = 0
                    else: continue

                for x in w_rounded:
                    if x > m_input: x = m_input
                    elif x < 0: x = 0
                    else: continue

                #### create preference lists
 
                m_preflists = []
                for i in range(m_input):
                    w_shuffled = np.arange(1, w_input)
                    np.random.shuffle(w_shuffled)
                    m_preflist = [[None, x] for x in w_shuffled][: m_rounded[i]]

                    last = 1
                    for j, pref in enumerate(m_preflist):
                        rnd = np.random.random_sample()
                        if rnd >= (m_ties / 100):
                            pref[0] = j + 1
                            last = j + 1
                        else:
                            pref[0] = last
                    m_preflists.append(m_preflist)

                w_preflists = []
                for i in range(w_input):
                    m_shuffled = np.arange(1, m_input)
                    np.random.shuffle(m_shuffled)
                    w_preflist = [[None, x] for x in m_shuffled][: w_rounded[i]]

                    last = 1
                    for j, pref in enumerate(w_preflist):
                        rnd = np.random.random_sample()
                        if rnd >= (m_ties / 100):
                            pref[0] = j + 1
                            last = j + 1
                        else:
                            pref[0] = last
                    w_preflists.append(w_preflist)
            
                #### write input to the file

                inputfilename = "files/{}--input.lp".format(fileprefix)
                with open(inputfilename, "w") as out:
                    m_mean = sum([len(m_preflist) for m_preflist in m_preflists]) / (m_input * w_input)
                    w_mean = sum([len(w_preflist) for w_preflist in w_preflists]) / (m_input * w_input)
                    print("file:  {:80s}  man: {:.2f}   woman: {:.2f}".format(inputfilename, m_mean, w_mean))

                    out.write("man(1..{}).\n".format(m_input))
                    out.write("woman(1..{}).\n".format(w_input))
                    out.write("\n")
                    for i in range(m_input):
                        for j in range(len(m_preflists[i])):
                            out.write("mrank({:3d}, {:3d}, {:3d}).\n".format(i + 1, m_preflists[i][j][1], m_preflists[i][j][0]))
                    out.write("\n")
                    for i in range(w_input):
                        for j in range(len(w_preflists[i])):
                            out.write("wrank({:3d}, {:3d}, {:3d}).\n".format(i + 1, w_preflists[i][j][1], w_preflists[i][j][0]))

            #### no optimization

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
