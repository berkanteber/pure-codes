import numpy as np

percentages = [.25, .50, .75, 1]
inputsizes = [20]
stddev = .05

for m_input in inputsizes:
    for w_input in inputsizes:
        for m_percent in percentages:
            for w_percent in percentages:
                m_dist = np.full(m_input, m_input) if m_percent == 1 else (stddev * np.random.randn(m_input) + m_percent) * m_input
                w_dist = np.full(w_input, w_input) if w_percent == 1 else (stddev * np.random.randn(w_input) + w_percent) * w_input

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

                m_preferencelists = []
                for i in range(m_input):
                    m_preferencelist = np.arange(m_input) + 1
                    np.random.shuffle(m_preferencelist)
                    m_preferencelists.append(m_preferencelist[: m_rounded[i] + 1])

                w_preferencelists = []
                for i in range(w_input):
                    w_preferencelist = np.arange(w_input) + 1
                    np.random.shuffle(w_preferencelist)
                    w_preferencelists.append(w_preferencelist[: w_rounded[i] + 1])

                filename = "files/m-{}-w-{}--m-{}-w-{}--input.lp".format(m_input, w_input, m_percent, w_percent)
                with open(filename, "w") as out:
                    m_mean = sum([len(m_preferencelist) for m_preferencelist in m_preferencelists]) / m_input / m_input
                    w_mean = sum([len(w_preferencelist) for w_preferencelist in w_preferencelists]) / w_input / w_input
                    print("file:  {:40s} man:  {:.5f}  woman:  {:.5f}".format(filename[filename.index('/') + 1 :], m_mean, w_mean))

                    out.write("man(1..{}).\n".format(m_input))
                    out.write("woman(1..{}).\n".format(w_input))
                    out.write("\n")

                    for i in range(m_input):
                        for j in range(len(m_preferencelists[i])):
                            out.write("mpref({:4d}, {:4d}, {:4d}).\n".format(i + 1, m_preferencelists[i][j], j + 1))

                    out.write("\n")

                    for i in range(w_input):
                        for j in range(len(w_preferencelists[i])):
                            out.write("wpref({:4d}, {:4d}, {:4d}).\n".format(i + 1, w_preferencelists[i][j], j + 1))
