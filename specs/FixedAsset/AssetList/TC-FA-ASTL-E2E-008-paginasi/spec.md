---
id: TC-FA-ASTL-E2E-008-paginasi
title: "Paginasi tabel All Assets"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [F-ASTL-05, "§5#r2", "EB-TBL-7@tabel-all-assets"]
smoke: []
dependsOn: []
trace:
  F-ASTL-05: [5, 7]
  "§5#r2": [3, 12, 14, 16, 18, 20, 22, 34, 35, 41, 43]
  "EB-TBL-7@tabel-all-assets": [10, 24, 26, 29, 31, 51, 52, 53]
anchor: [47]
coverage:
  web: automated
---

# Paginasi tabel All Assets

## Prerequisites
- Aktor: Total Control `Wulan Sari {runId}`.
- Layar awal: Fixed Asset > Assets (tab `Assets`).
- Data:
  - DU-008-1: Entitas `Entitas Paginasi {runId}`, entitas khusus yang tidak dipakai spec lain, tanpa aset sebelum data di bawah.
  - DU-008-2: User `Wulan Sari {runId}`, role Total Control, cakupan seluruh entitas `Entitas Paginasi {runId}`.
  - DU-008-3: 100 aset `Monitor Dell - {n} {runId}` dengan `n` dari 1 sampai 100, Brand `Dell`.
  - DU-008-7: Aset `Monitor Dell - 101 {runId}`, Brand `Dell`, berpenanda lisensi `Unmanaged` dengan Custody `Available` sehingga dapat dihapus; aset ini baris terakhir pada urutan bawaan.
  - DU-008-4: 10 aset `Kursi Rapat - {n} {runId}` dengan `n` dari 1 sampai 10, Brand `Chitose`.
  - Seluruh aset di entitas ini adalah DU-008-3, DU-008-4, dan DU-008-7, sehingga total baris tanpa saringan adalah `111` dan halaman terakhir pada 10 baris per halaman adalah halaman `12` yang berisi satu baris. Dengan Brand `Dell`, total baris adalah `101`. Dengan Search `Kursi Rapat`, total baris adalah `10`.
  - Input nomor halaman yang dicoba: `0`, `-1`, `13` (satu di atas halaman terakhir), dan `abc`.
- Kondisi:
  - Akun `Wulan Sari {runId}` aktif dan kredensialnya tersedia.

## Test Steps

### Halaman bawaan 10 baris dan perpindahan halaman
1. Masuk sebagai `Wulan Sari {runId}`
2. Klik menu `Fixed Asset > Assets` pada sidebar
3. Verifikasi laporan halaman menampilkan `Showing 1 to 10 of 111`
4. Klik tombol halaman `2`
5. Verifikasi laporan halaman menampilkan `Showing 11 to 20 of 111`
6. Klik tombol `Last Page`
7. Verifikasi laporan halaman menampilkan `Showing 111 to 111 of 111`, satu baris pada halaman terakhir

### Ganti page size kembali ke halaman 1
8. Klik tombol halaman `3`
9. Pilih ukuran halaman `25`
10. Verifikasi laporan halaman menampilkan `Showing 1 to 25 of 111`
11. Klik tombol `Last Page`
12. Verifikasi laporan halaman menampilkan `Showing 101 to 111 of 111`
13. Pilih ukuran halaman `50`
14. Verifikasi laporan halaman menampilkan `Showing 1 to 50 of 111`
15. Klik tombol `Last Page`
16. Verifikasi laporan halaman menampilkan `Showing 101 to 111 of 111`
17. Pilih ukuran halaman `100`
18. Verifikasi laporan halaman menampilkan `Showing 1 to 100 of 111`
19. Klik tombol `Last Page`
20. Verifikasi laporan halaman menampilkan `Showing 101 to 111 of 111`
21. Pilih ukuran halaman `10`
22. Verifikasi laporan halaman menampilkan `Showing 1 to 10 of 111`

### Nomor halaman tidak valid
23. Ketik `0` pada field `Jump to page`, tekan Enter
24. Verifikasi laporan halaman menampilkan `Showing 1 to 10 of 111`
25. Ketik `-1` pada field `Jump to page`, tekan Enter
26. Verifikasi laporan halaman menampilkan `Showing 1 to 10 of 111`
27. Klik tombol halaman `3`
28. Ketik `abc` pada field `Jump to page`, tekan Enter
29. Verifikasi laporan halaman menampilkan `Showing 21 to 30 of 111`, tidak berubah
30. Ketik `13` pada field `Jump to page`, tekan Enter
31. Verifikasi laporan halaman menampilkan `Showing 111 to 111 of 111`, yaitu halaman terakhir

### Search dan Apply mengembalikan ke halaman 1
32. Klik tombol halaman `3`
33. Ketik Search `Kursi Rapat`, tekan Enter
34. Verifikasi laporan halaman menampilkan `Showing 1 to 10 of 10`
35. Verifikasi tombol `Next Page` tidak aktif karena seluruh hasil muat dalam satu halaman
36. Klik `(←)` pada kotak Search
37. Klik tombol halaman `3`
38. Klik ikon Filter
39. Pilih Brand `Dell` pada Filter Panel
40. Klik `[Apply]`
41. Verifikasi laporan halaman menampilkan `Showing 1 to 10 of 101`
42. Klik tombol `Last Page`
43. Verifikasi laporan halaman menampilkan `Showing 101 to 101 of 101`, satu baris pada halaman terakhir hasil saringan

### Hapus baris terakhir di halaman terakhir pindah ke halaman terakhir yang masih ada
44. Klik `[Clear Field]`
45. Klik `[Apply]`
46. Klik tombol `Last Page`
47. Verifikasi laporan halaman menampilkan `Showing 111 to 111 of 111`, satu baris `Monitor Dell - 101 {runId}` pada halaman terakhir
48. Klik menu aksi baris `Monitor Dell - 101 {runId}`
49. Pilih `Delete Asset Data`
50. Klik `[Delete]`
51. Verifikasi laporan halaman menampilkan `Showing 101 to 110 of 110`
52. Verifikasi tombol halaman `11` aktif sebagai halaman terakhir yang masih ada
53. Verifikasi tabel memuat `Monitor Dell - 100 {runId}` dan tidak memuat `Monitor Dell - 101 {runId}`
