import sys, time
import os, subprocess
import subprocessmethodrun

lines = []
with open(sys.argv[2], "r") as inp:
    for line in inp:
        lines.append(line)

if (sys.argv[1] == "pref"):
    m_size = int(lines[0])
    w_size = int(lines[1])
    
    m_preflists = []
    for i in range(m_size):
        split_gt = lines[i + 2][:-1].split(" > ")

        curr = 1
        preflist = []
        for outer_split in split_gt:
            split_eq = outer_split.split(" = ")
            for inner_split in split_eq:
                preflist.append((int(inner_split), curr))
            curr += len(split_eq)

        m_preflists.append(preflist)

    w_preflists = []
    for i in range(w_size):
        split_gt = lines[i + 2 + m_size][:-1].split(" > ")

        curr = 1
        preflist = []
        for outer_split in split_gt:
            split_eq = outer_split.split(" = ")
            for inner_split in split_eq:
                preflist.append((int(inner_split), curr))
            curr += len(split_eq)

        w_preflists.append(preflist)

elif (sys.argv[1] == "util"):
    m_size = int(lines[0].split()[-1])
    w_size = int(lines[1].split()[-1])

    m_preflists = []
    for i in range(m_size):
        splitted = lines[i + 2][:-1].split()[1:]
        preflist = []
        for j, s in enumerate(splitted):
            if s != 0:
                preflist.append((j + 1, int(s)))
        m_preflists.append(preflist)

    w_preflists = []
    for i in range(w_size):
        splitted = lines[i + 2 + m_size][:-1].split()[1:]
        preflist = []
        for j, s in enumerate(splitted):
            if s != 0:
                preflist.append((j + 1, int(s)))
        w_preflists.append(preflist)

with open("input.lp", "w") as out:
    out.write("man(1..{}).\n".format(m_size))
    out.write("woman(1..{}).\n".format(w_size))
    out.write("\n")
    for i in range(m_size):
        for elem, val in m_preflists[i]:
            out.write("mrank({:3d}, {:3d}, {:3d}).\n".format(i + 1, elem, val))
    out.write("\n")
    for i in range(w_size):
        for elem, val in w_preflists[i]:
            out.write("wrank({:3d}, {:3d}, {:3d}).\n".format(i + 1, elem, val))

if len(sys.argv) == 3:
    optimize = "noopt"
    command = "clingo --stats input.lp ../codes/smpti.lp 1"
elif sys.argv[3] == "sexeq":
    optimize = "sexeq"
    command = "clingo --stats input.lp ../codes/smpti.lp ../codes/sexequal.lp 0"
elif sys.argv[3] == "egal":
    optimize = "egal"
    command = "clingo --stats input.lp ../codes/smpti.lp ../codes/egalitarian.lp 0"
elif sys.argv[3] == "minreg":
    optimize = "minreg"
    command = "clingo --stats input.lp ../codes/smpti.lp ../codes/minregret.lp 0"
elif sys.argv[3] == "maxcar":
    optimize = "maxcar"
    command = "clingo --stats input.lp ../codes/smpti.lp ../codes/maxcardinality.lp 0"

start = time.time()
retcode, stdout, stderr = subprocessmethodrun.run(command, shell = True, stdout = subprocess.PIPE)
output = stdout.decode('utf-8')
end = time.time()

resultfile = "result.txt"
with open(resultfile, "w") as out:
    out.write(output)

if optimize != "noopt":
    lines = output.split('\n')
    for i, line in enumerate(lines):
        if line == "OPTIMUM FOUND":
            optval = lines[i - 1].split()[-1]
            break

    print("time: {:09.2f} seconds\noptimization: {}".format(end - start, optval))
