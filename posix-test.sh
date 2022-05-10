FILE=posix.log
if test -f "$FILE"; then
    rm $FILE
fi
for ((i=6;i<11;i+=1));
  do echo "running -- GenSym/POSIX with ${i} Symbolic inputs"
  ./PureLLSC_echo_linked_posix_reproduce --cons-indep --argv="./echo.bc --sym-stdout -sym-arg ${i}" | tail -1 >> posix.log;
done
