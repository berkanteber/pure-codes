import itertools

percentages = [25, 50, 100]
inputsizes = [20, 40, 60]
ties = [0, 10, 20]

def parsefile(m_input, w_input, m_percent, w_percent, m_ties, w_ties):
    fileprefix = "m-{}-w-{}--m-{}pc-w-{}pc--m-{}pc-w-{}pc".format(m_input, w_input, m_percent, w_percent, m_ties, w_ties)
    tobeprinted = "{},{},{} %,{} %,{} %,{} %,".format(m_input, w_input, m_percent, w_percent, m_ties, w_ties)
    
    for opt in ["Sex-equal", "Egalitarian", "Minimum Regret", "Maximum Cardinality", "No Optimization"]:
        if opt == "No Optimization": filename = "results-article/{}--result.txt".format(fileprefix)
        elif opt == "Sex-equal": filename = "results-article/{}--result-sexequal.txt".format(fileprefix)
        elif opt == "Egalitarian": filename = "results-article/{}--result-egalitarian.txt".format(fileprefix)
        elif opt == "Minimum Regret": filename = "results-article/{}--result-minregret.txt".format(fileprefix)
        elif opt == "Maximum Cardinality": filename = "results-article/{}--result-maxcardinality.txt".format(fileprefix)

        with open(filename) as inp:
            timeout, cputime = False, None
            for line in inp:
                if line[:-1].find("TIME LIMIT") > -1: timeout = True
                if line[:-1].find("CPU Time") > -1: cputime = line[:-1].split()[-1][:-1]                
            if timeout: tobeprinted += "Timeout,"
            elif cputime is None: tobeprinted += "Missing,"
            else: tobeprinted += cputime + " sec,"

    print(tobeprinted[:-1])


print("# of Men,# of Women,Completeness in Men's Pref.,Completeness in Women's Pref.,Ties in Men's Pref.,Ties in Women's Pref.,Exec. Time of Sex-equal Opt.,Exec. Time of Egalitarian Opt., Exec. Time of Minimum Regret Opt.,Exec. Time of Maximum Cardinality Opt.,Exec. Time without Opt.")

for m_input, w_input in itertools.product(inputsizes, inputsizes):
    for m_percent, w_percent in itertools.product(percentages, percentages):
        for m_ties, w_ties in itertools.product(ties, ties):
            if m_input > w_input or m_percent > w_percent or m_ties > w_ties: continue
            
            parsefile(m_input, w_input, m_percent, w_percent, m_ties, w_ties)
