#!/bin/bash
N=${1:-1024}
rm -f hasil/matmul.txt
for t in 1 2 4 8; do
  for r in 1 2 3; do
    OMP_NUM_THREADS=$t ./matmul $N >> hasil/matmul.txt
    echo "selesai: thread=$t percobaan=$r"
  done
done
echo "Pengujian matmul selesai. Hasil ada di hasil/matmul.txt"
