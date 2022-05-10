FILE=llsc.log
if test -f "$FILE"; then
    rm $FILE
fi
for ((i=6;i<11;i+=1));
  do echo "running -- GenSym/FS with ${i} Symbolic inputs"
  ./PureLLSC_echo_llsc_linked_reproduce --cons-indep --argv="./echo.bc #{${i}}" | tail -1 >> llsc.log;
done

