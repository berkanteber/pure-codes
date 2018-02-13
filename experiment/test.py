import itertools
import numpy as np
import time, os, subprocess

percentages = [20, 60, 100]
inputsizes = [10]
stddev = 10

np.random.seed(0)

for m_input, w_input in itertools.product(inputsizes, inputsizes):
    for m_percent, w_percent in itertools.product(percentages, percentages):
        fileprefix = "m-{}-w-{}--m-{}pc-w-{}pc".format(m_input, w_input, m_percent, w_percent)

        #### determine length of preference lists

        m_dist = np.full(m_input, m_input) if m_percent == 100 else ((stddev / 100) * np.random.randn(m_input) + (m_percent / 100)) * m_input
        w_dist = np.full(w_input, w_input) if w_percent == 100 else ((stddev / 100) * np.random.randn(w_input) + (w_percent / 100)) * w_input
        m_rounded = [int(round(x)) for x in m_dist]
        w_rounded = [int(round(x)) for x in w_dist]
        for x in m_rounded:
            if x > m_input: x = m_input
            elif x < 0: x = 0
            else: continue
        for x in w_rounded:
            if x > w_input: x = w_input
            elif x < 0: x = 0
            else: continue

        #### create preference lists

        m_preflists = []
        for i in range(m_input):
            m_preflist = np.arange(m_input) + 1
            np.random.shuffle(m_preflist)
            m_preflists.append(m_preflist[: m_rounded[i] + 1])
        w_preflists = []
        for i in range(w_input):
            w_preflist = np.arange(w_input) + 1
            np.random.shuffle(w_preflist)
            w_preflists.append(w_preflist[: w_rounded[i] + 1])

        #### write input to the file

        inputfilename = "files/{}--input.lp".format(fileprefix)
        with open(inputfilename, "w") as out:
            m_mean = sum([len(m_preflist) for m_preflist in m_preflists]) / m_input / m_input
            w_mean = sum([len(w_preflist) for w_preflist in w_preflists]) / w_input / w_input
            print("file:  {:60s}  man: {:.2f}   woman: {:.2f}".format(inputfilename, m_mean, w_mean))

            out.write("man(1..{}).\n".format(m_input))
            out.write("woman(1..{}).\n".format(w_input))
            out.write("\n")
            for i in range(m_input):
                for j in range(len(m_preflists[i])):
                    out.write("mpref({:3d}, {:3d}, {:3d}).\n".format(i + 1, m_preflists[i][j], j + 1))
            out.write("\n")
            for i in range(w_input):
                for j in range(len(w_preflists[i])):
                    out.write("wpref({:3d}, {:3d}, {:3d}).\n".format(i + 1, w_preflists[i][j], j + 1))

        #### no optimization

        resultfilename = inputfilename[:-8] + "result.txt"

        start = time.time()
        command = "../clingo/clingo --stats {} codes/smpti.lp 1".format(inputfilename)
        process = subprocess.run(command, shell = True, stdout = subprocess.PIPE)
        output = process.stdout.decode('utf-8')
        end = time.time()

        with open(resultfilename, "w") as out:
            out.write(output)
            print("file:  {:60s}  time: {:09.2f} seconds".format(resultfilename, end - start))

        #### sex equal smpti

        resultfilename = inputfilename[:-8] + "result-sexequal.txt"

        start = time.time()
        command = "../clingo/clingo --stats {} codes/smpti.lp codes/sexequal.lp 0".format(inputfilename)
        process = subprocess.run(command, shell = True, stdout = subprocess.PIPE)
        output = process.stdout.decode('utf-8')
        end = time.time()

        with open(resultfilename, "w") as out:
            out.write(output)
            print("file:  {:60s}  time: {:09.2f} seconds".format(resultfilename, end - start))

        #### egalitarian smpti

        resultfilename = inputfilename[:-8] + "result-egalitarian.txt"

        start = time.time()
        command = "../clingo/clingo --stats {} codes/smpti.lp codes/egalitarian.lp 0".format(inputfilename)
        process = subprocess.run(command, shell = True, stdout = subprocess.PIPE)
        output = process.stdout.decode('utf-8')
        end = time.time()

        with open(resultfilename, "w") as out:
            out.write(output)
            print("file:  {:60s}  time: {:09.2f} seconds".format(resultfilename, end - start))

        #### minimum regret smpti

        resultfilename = inputfilename[:-8] + "result-minregret.txt"

        start = time.time()
        command = "../clingo/clingo --stats {} codes/smpti.lp codes/minregret.lp 0".format(inputfilename)
        process = subprocess.run(command, shell = True, stdout = subprocess.PIPE)
        output = process.stdout.decode('utf-8')
        end = time.time()

        with open(resultfilename, "w") as out:
            out.write(output)
            print("file:  {:60s}  time: {:09.2f} seconds".format(resultfilename, end - start))

        #### maximum cardinality smpti

        resultfilename = inputfilename[:-8] + "result-maxcardinality.txt"

        start = time.time()
        command = "../clingo/clingo --stats {} codes/smpti.lp codes/maxcardinality.lp 0".format(inputfilename)
        process = subprocess.run(command, shell = True, stdout = subprocess.PIPE)
        output = process.stdout.decode('utf-8')
        end = time.time()

        with open(resultfilename, "w") as out:
            out.write(output)
            print("file:  {:60s}  time: {:09.2f} seconds".format(resultfilename, end - start))

        print("")
