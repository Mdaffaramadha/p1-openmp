# Praktikum 1: OpenMP

Nama: M. Daffa Ramadhan
NIM: 09011382429133

## Isi repositori
- `src/matmul.c`: perkalian matriks, diparalelkan dengan `#pragma omp parallel for`
- `src/prima.c`: bilangan prima sampai 10^7, dengan `reduction` dan `schedule(runtime)`
- `jalan_matmul.sh`, `prima.sh`: skrip pengujian
- `rekap.py`: menghitung median, speedup, dan efisiensi
- `hasil/`: keluaran mentah pengujian
- `A05_09011382429133_MDaffaR.pdf`: laporan

## Cara kompilasi dan menjalankan

    gcc -O2 -fopenmp src/matmul.c -o matmul -lm
    gcc -O2 -fopenmp src/prima.c -o prima

    OMP_NUM_THREADS=4 ./matmul 1024
    OMP_NUM_THREADS=4 OMP_SCHEDULE="dynamic,1000" ./prima

    ./jalan_matmul.sh 1024
    ./prima.sh
    python3 rekap.py

## Lingkungan
Intel Core i5-12500H, Ubuntu pada WSL2, GCC 15.2.0, opsi `-O2 -fopenmp`.
