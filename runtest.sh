function setup() {
  module load anaconda/2020.11
  cp /scratch1/gao606/spring-2022-report-reproduce/sai/dev-clean/llsc_gen/PureLLSC_echo_linked_posix_reproduce/PureLLSC_echo_linked_posix_reproduce ./
  cp /scratch1/gao606/spring-2022-report-reproduce/sai/dev-clean/llsc_gen/PureLLSC_echo_llsc_linked_reproduce/PureLLSC_echo_llsc_linked_reproduce ./
  cp /scratch1/gao606/coreutils_dev/obj-llvm/src/echo.bc ./
  klee --libc=uclibc --posix-runtime ./echo.bc --sym-stdout --sym-arg 3 &> /dev/null
  cp ./klee-last/assembly.ll ./
  rm -rf klee-last
  rm -rf klee-out-*
}

function runtest() {
  bash test-klee.sh
  bash posix-test.sh
  bash llsc-test.sh
  rm ./PureLLSC_echo_linked_posix_reproduce
  rm ./PureLLSC_echo_llsc_linked_reproduce
  rm assembly.ll
  rm echo.bc
  rm -rf tests
}

function plot() {
  if test -f figure.pdf; then
    rm figure.pdf
  fi
  if test -f table.pdf; then
    rm table.pdf
  fi
  conda activate
  python3 ./plot.py
}

setup
runtest
plot