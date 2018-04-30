import copy
import itertools
import numpy as np
import time, os, subprocess
import subprocessmethodrun

percentages = [25, 50, 100]
inputsizes = [30, 60, 90, 120]
ties = [0, 10, 20]

def writetofile(m_input, w_input, m_ties, w_ties, m_percent, w_percent, m_preflists, w_preflists):
    inputfilename = "files/m-{}-w-{}--m-{}pc-w-{}pc--m-{}pc-w-{}pc--input.lp".format(m_input, w_input, m_percent, w_percent, m_ties, w_ties)
    
    with open(inputfilename, "w") as out:
        print("file:  {:80s}".format(inputfilename))

        out.write("man(1..{}).\nwoman(1..{}).\n".format(m_input, w_input))
        out.write("\n")
        for i in range(m_input):
            for j in range(len(m_preflists[i])):
                out.write("mrank({:3d}, {:3d}, {:3d}).\n".format(i + 1, m_preflists[i][j][1], m_preflists[i][j][0]))
        out.write("\n")
        for i in range(w_input):
            for j in range(len(w_preflists[i])):
                out.write("wrank({:3d}, {:3d}, {:3d}).\n".format(i + 1, w_preflists[i][j][1], w_preflists[i][j][0]))

def incomplete(m_input, w_input, m_ties, w_ties, m_preflists, w_preflists):
    m100, w100 = copy.deepcopy(m_preflists), copy.deepcopy(w_preflists)

    m50 = []
    for i in range(m_input):
        tmp = []
        for j in range(len(m100[i])):
            rnd = np.random.random_sample()
            if rnd >= 0.5:
                tmp.append(m100[i][j])
        m50.append(tmp)

    w50 = []
    for i in range(w_input):
        tmp = []
        for j in range(len(w100[i])):
            rnd = np.random.random_sample()
            if rnd >= 0.5:
                tmp.append(w100[i][j])
        w50.append(tmp)

    m25 = []
    for i in range(m_input):
        tmp = []
        for j in range(len(m50[i])):
            rnd = np.random.random_sample()
            if rnd >= 0.5:
                tmp.append(m50[i][j])
        m25.append(tmp)

    w25 = []
    for i in range(w_input):
        tmp = []
        for j in range(len(w50[i])):
            rnd = np.random.random_sample()
            if rnd >= 0.5:
                tmp.append(w50[i][j])
        w25.append(tmp)

    writetofile(m_input, w_input, m_ties, w_ties, 25, 25, m25, w25)
    writetofile(m_input, w_input, m_ties, w_ties, 25, 50, m25, w50)
    writetofile(m_input, w_input, m_ties, w_ties, 25, 100, m25, w100)
    writetofile(m_input, w_input, m_ties, w_ties, 50, 50, m50, w50)
    writetofile(m_input, w_input, m_ties, w_ties, 50, 100, m50, w100)
    writetofile(m_input, w_input, m_ties, w_ties, 100, 100, m100, w100)

def withties(m_input, w_input):
    m_ties, w_ties = 0, 0

    m_preflists = []
    for i in range(m_input):
        w_shuffled = np.arange(0, w_input)
        np.random.shuffle(w_shuffled)
        m_preflist = [[None, x + 1] for x in w_shuffled]

        for j, pref in enumerate(m_preflist):
            pref[0] = j + 1
        m_preflists.append(m_preflist)

    w_preflists = []
    for i in range(w_input):
        m_shuffled = np.arange(0, m_input)
        np.random.shuffle(m_shuffled)
        w_preflist = [[None, x + 1] for x in m_shuffled]

        for j, pref in enumerate(w_preflist):
            pref[0] = j + 1
        w_preflists.append(w_preflist)

    m0, w0 = copy.deepcopy(m_preflists), copy.deepcopy(w_preflists)

    for i in range(m_input):
        for j in range(1, w_input):
            if m_preflists[i][j][0] != m_preflists[i][j - 1][0] and (j == w_input - 1 or m_preflists[i][j][0] != m_preflists[i][j + 1][0]):
                rnd = np.random.random_sample()
                if rnd < (10 / 100):
                    m_preflists[i][j][0] = m_preflists[i][j - 1][0]

    for i in range(w_input):
        for j in range(1, m_input):
            if w_preflists[i][j][0] != w_preflists[i][j - 1][0] and (j == m_input - 1 or w_preflists[i][j][0] != w_preflists[i][j + 1][0]):
                rnd = np.random.random_sample()
                if rnd < (10 / 100):
                    w_preflists[i][j][0] = w_preflists[i][j - 1][0]

    m10, w10 = copy.deepcopy(m_preflists), copy.deepcopy(w_preflists)
    
    for i in range(m_input):
        for j in range(1, w_input):
            if m_preflists[i][j][0] != m_preflists[i][j - 1][0] and (j == w_input - 1 or m_preflists[i][j][0] != m_preflists[i][j + 1][0]):
                rnd = np.random.random_sample()
                if rnd < (11 / 100):
                    m_preflists[i][j][0] = m_preflists[i][j - 1][0]

    for i in range(w_input):
        for j in range(1, m_input):
            if w_preflists[i][j][0] != w_preflists[i][j - 1][0] and (j == m_input - 1 or w_preflists[i][j][0] != w_preflists[i][j + 1][0]):
                rnd = np.random.random_sample()
                if rnd < (11 / 100):
                    w_preflists[i][j][0] = w_preflists[i][j - 1][0]

    m20, w20 = copy.deepcopy(m_preflists), copy.deepcopy(w_preflists)

    incomplete(m_input, w_input, 0, 0, copy.deepcopy(m0), copy.deepcopy(w0))
    incomplete(m_input, w_input, 0, 10, copy.deepcopy(m0), copy.deepcopy(w10))
    incomplete(m_input, w_input, 0, 20, copy.deepcopy(m0), copy.deepcopy(w20))
    incomplete(m_input, w_input, 10, 10, copy.deepcopy(m10), copy.deepcopy(w10))
    incomplete(m_input, w_input, 10, 20, copy.deepcopy(m10), copy.deepcopy(w20))
    incomplete(m_input, w_input, 20, 20, copy.deepcopy(m20), copy.deepcopy(w20))

for m_input, w_input in itertools.product(inputsizes, inputsizes):
    if m_input > w_input: continue
    withties(m_input, w_input)
