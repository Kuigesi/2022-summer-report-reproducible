if test -f temp.log; then
    rm temp.log
fi
if test -f klee-path.log; then
    rm klee-path.log
fi
if test -f klee-time.log; then
    rm klee-time.log
fi
for ((i=6;i<11;i+=1))
  do echo "running -- KLEE/POSIX with ${i} Symbolic inputs"
  klee -switch-type=simple ./assembly.ll --sym-stdout -sym-arg ${i} &> temp.log;
  tail -3 temp.log | head -1 >> klee-path.log;
  klee-stats klee-last | tail -2 | head -1 >> klee-time.log
  rm -rf klee-last
  rm -rf klee-out-*
done
rm temp.log