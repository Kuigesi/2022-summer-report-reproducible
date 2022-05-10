import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import table

with open('klee-time.log') as fklee:
    textklee = fklee.readlines()
with open('klee-path.log') as fkleepath:
    textkleepath = fkleepath.readlines()
with open('posix.log') as fposix:
    textposix = fposix.readlines()
with open('llsc.log') as fllsc:
    textllsc = fllsc.readlines()
patk = re.compile(r'\|klee-last\|(\s*)(\d+)\|(\s*)([\d\.]+)\|(\s*)([\d\.]+)\|(\s*)([\d\.]+)\|(\s*)([\d\.]+)\|(\s*)([\d\.]+)\|')
pathkp = re.compile(r'KLEE: done: completed paths = (\d+)')
patl = re.compile(r'\[([\d\.]+)s\/([\d\.]+)s\].+#paths: (\d+).+')
textsym = [[idx + 6] for idx in range(len(textklee))]
textk = [[re.match(patk, textklee[idx]).groups()[i] for i in [3]] + [re.match(pathkp, textkleepath[idx]).groups()[i] for i in [0]] for idx in range(len(textklee))]
textp = [[re.match(patl, ln).groups()[i] for i in [1, 2]] for ln in textposix]
textl = [[re.match(patl, ln).groups()[i] for i in [1, 2]] for ln in textllsc]
textfinal = [textsym[i] + textk[i]+ textp[i]+textl[i] for i in range(len(textklee))]
odf = pd.DataFrame(textfinal, columns=["symbolic inputs", "klee", "klee-path", "posix model", "posix-path", "llsc model", "llsc-path"])
odf = odf.apply(lambda col: pd.to_numeric(col, 'ignore'))
odf.index = np.arange(6, len(textfinal)+6)
tdf = odf.filter(['symbolic inputs', 'klee-path', "klee", "posix model", "llsc model"], axis=1)
df = tdf.rename({'symbolic inputs': '#Sym', 'klee-path': '#Path', 'klee': 'KLEE/POSIX', 'posix model': 'GenSym/POSIX', 'llsc model': 'GenSym/FS'}, axis='columns')
#df.pivot_table(index='#Sym', values=['#Path', 'KLEE/POSIX', 'GenSym/POSIX', 'GenSym/FS'])

df['#Sym'] = df['#Sym'].astype(int).convert_dtypes()
df['#Path'] = df['#Path'].astype(int).convert_dtypes()
df['KLEE/POSIX'] = df['KLEE/POSIX'].convert_dtypes() .apply(lambda x: round(x, 2))
df['GenSym/POSIX'] = df['GenSym/POSIX'].convert_dtypes() .apply(lambda x: round(x, 2))
df['GenSym/FS'] = df['GenSym/FS'].convert_dtypes() .apply(lambda x: round(x, 2))

finaldf = df.rename({'KLEE/POSIX': 'KLEE/POSIX time(s)', 'GenSym/POSIX': 'GenSym/POSIX time(s)', 'GenSym/FS': 'GenSym/FS time(s)'}, axis='columns')


tfig, tax = plt.subplots()

tax.axis('tight')
tax.axis('off')
tax.table(cellText=finaldf.values,colLabels=finaldf.columns,loc="center")
tfig.savefig('table.pdf', format="pdf", bbox_inches="tight")

ddfn = df.filter(['KLEE/POSIX', 'GenSym/POSIX', 'GenSym/FS'], axis=1)

fig, ax = plt.subplots()
plt.xticks(range(6,11))
#fig.set_size_inches(6.4, 4.8)
ddfn.plot(ylabel='running time (s)', xlabel="symbolic argument number", ax=ax)
ax.set_yscale('log', base=2)
#ax.set_xscale('log', base=2)
fig.savefig('figure.pdf', bbox_inches='tight')