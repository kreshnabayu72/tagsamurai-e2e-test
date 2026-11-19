---
id: TC-FA-ASSIGN-E2E-005-transactions-paginasi
title: "Paginasi pada tab Transactions"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§5#r3"]
smoke: []
dependsOn: []
trace:
  "§5#r3": [1, 3, 4, 6, 8, 10, 12, 14, 16, 19, 21, 23, 25, 27, 29, 31, 34, 35, 37, 39]
coverage:
  web: automated
---

# Paginasi pada tab Transactions

## Prerequisites
- Aktor: Total Control `Hendra Kusuma {runId}` pada entitas khusus `Entitas Paginasi {runId}`.
- Layar awal: Transactions > Assignment.
- Data:
  - DU-005-1: Entitas khusus `Entitas Paginasi {runId}`, tidak dipakai spec lain; daftar Transactions-nya hanya berisi 101 ASG pada entri DU-005-7 sampai DU-005-10.
  - DU-005-2: User `Hendra Kusuma {runId}`, role Total Control, cakupan seluruh client; ia aktor spec ini.
  - DU-005-3: Group `Head Office {runId}`.
  - DU-005-4: User `Agus Prasetyo {runId}`, role Asset Admin pada Group `Head Office {runId}`; ia pengaju semua ASG.
  - DU-005-5: User `Dewi Anggraini {runId}`, karyawan aktif ber-akun login tanpa akses menu Assignment; PIC aktif keempat Division pada entri ASG di bawah.
  - DU-005-6: Division `Tim Sepuluh {runId}`, `Tim Sebelas {runId}`, `Tim Dua Enam {runId}`, dan `Tim Lainnya {runId}`.
  - DU-005-7: Sepuluh ASG berstatus `Assigned` untuk Assignee Division `Tim Sepuluh {runId}`, aset `Aset Sepuluh {n} {runId}`, Total Asset `1`.
  - DU-005-8: Sebelas ASG berstatus `Assigned` untuk Assignee Division `Tim Sebelas {runId}`, aset `Aset Sebelas {n} {runId}`, Total Asset `1`.
  - DU-005-9: Dua puluh enam ASG berstatus `Assigned` untuk Assignee Division `Tim Dua Enam {runId}`, aset `Aset Dua Enam {n} {runId}`, Total Asset `1`.
  - DU-005-10: Lima puluh empat ASG berstatus `Assigned` untuk Assignee Division `Tim Lainnya {runId}`, aset `Aset Lainnya {n} {runId}`, Total Asset `1`; bersama tiga entri sebelumnya jumlah ASG seluruh entitas tepat 101.

## Test Steps

### Ukuran halaman bawaan dan pilihannya
1. Verifikasi tabel pada halaman pertama memuat tepat 10 baris dan laporan `Showing 1 to 10 of 101`
2. Klik dropdown rows per page
3. Verifikasi pilihan ukuran halaman `10`, `25`, `50`, dan `100` tampil
4. Verifikasi ukuran halaman yang terpilih saat halaman dibuka adalah `10`

### Halaman terakhir berisi satu baris
5. Klik `Last Page`
6. Verifikasi halaman terakhir memuat tepat satu baris dan laporan `Showing 101 to 101 of 101`
7. Klik `Previous Page`
8. Verifikasi halaman sebelumnya memuat tepat 10 baris dan laporan `Showing 91 to 100 of 101`

### Ukuran halaman 100 dengan 101 baris
9. Pilih ukuran halaman `100`
10. Verifikasi halaman pertama memuat tepat 100 baris dan laporan `Showing 1 to 100 of 101`
11. Klik `Next Page`
12. Verifikasi halaman kedua memuat tepat satu baris dan laporan `Showing 101 to 101 of 101`
13. Pilih ukuran halaman `10`
14. Verifikasi tabel kembali ke halaman pertama dengan tepat 10 baris

### Nomor halaman yang tidak valid
15. Isi `Jump to page` dengan `0`, tekan Enter
16. Verifikasi tabel tetap berada di halaman pertama
17. Klik `Next Page`
18. Isi `Jump to page` dengan `-1`, tekan Enter
19. Verifikasi tabel pindah ke halaman pertama
20. Isi `Jump to page` dengan `12`, tekan Enter
21. Verifikasi tabel pindah ke halaman terakhir dengan laporan `Showing 101 to 101 of 101`
22. Ketik `abc` pada `Jump to page`
23. Verifikasi kolom `Jump to page` tetap berisi nomor halaman terakhir dan tidak menerima huruf

### Hasil saringan lebih dari satu halaman
24. Ganti isi kotak search dengan `Tim Dua Enam {runId}`, tekan Enter
25. Verifikasi tabel kembali ke halaman pertama dengan laporan `Showing 1 to 10 of 26`
26. Klik `Last Page`
27. Verifikasi halaman terakhir memuat tepat 6 baris dan laporan `Showing 21 to 26 of 26`
28. Pilih ukuran halaman `25`
29. Verifikasi halaman pertama memuat tepat 25 baris dan laporan `Showing 1 to 25 of 26`
30. Klik `Next Page`
31. Verifikasi halaman kedua memuat tepat satu baris dan laporan `Showing 26 to 26 of 26`

### Ukuran halaman tepat sama dengan jumlah baris
32. Pilih ukuran halaman `10`
33. Ganti isi kotak search dengan `Tim Sepuluh {runId}`, tekan Enter
34. Verifikasi tabel memuat tepat 10 baris dengan laporan `Showing 1 to 10 of 10`
35. Verifikasi `Next Page` dan `Last Page` dinonaktifkan karena hanya ada satu halaman

### Satu baris melebihi ukuran halaman
36. Ganti isi kotak search dengan `Tim Sebelas {runId}`, tekan Enter
37. Verifikasi halaman pertama memuat tepat 10 baris dengan laporan `Showing 1 to 10 of 11`
38. Klik `Next Page`
39. Verifikasi halaman kedua memuat tepat satu baris dengan laporan `Showing 11 to 11 of 11`
