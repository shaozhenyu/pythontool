def frequencySort(s):
        m = {}
        n = {}
        for i in s:
            if i not in m:
                m[i] = 1
                n[i] = i
            else:
                m[i] += 1
                n[i] += i
        l = sorted(m.iteritems(), key = lambda d:d[1], reverse=True)
        string = ""
        for i in l:
            string += n[i[0]]
        return string
print frequencySort("aanbasdasdasd")
