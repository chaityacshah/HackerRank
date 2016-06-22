n = int(input())
uniqc = set([])
[uniqc.add(input()) for i in range(n)]

print(len(uniqc))