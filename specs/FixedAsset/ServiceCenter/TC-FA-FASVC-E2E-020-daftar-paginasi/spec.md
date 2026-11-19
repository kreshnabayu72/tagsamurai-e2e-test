---
id: TC-FA-FASVC-E2E-020-daftar-paginasi
title: "Daftar Service Center: Paginasi 10 per Halaman, Ukuran Halaman, dan Hapus Baris Terakhir Halaman"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§9.5#r11", "§5#b6", "EB-TBL-7@tabel-service-center"]
smoke: []
dependsOn: []
trace:
  "§9.5#r11": [1, 2, 4, 39]
  "§5#b6": [1, 2, 4, 7, 8, 11, 13, 39]
  "EB-TBL-7@tabel-service-center": [19, 21, 25, 27, 31, 35, 36, 37]
anchor: []
coverage:
  web: automated
---

# Daftar Service Center: Paginasi 10 per Halaman, Ukuran Halaman, dan Hapus Baris Terakhir Halaman

## Prerequisites
- Aktor: Total Control `Dian Halaman {runId}`, user milik entitas khusus.
- Layar awal: Add-ons > Service Center (halaman daftar).
- Data:
  - Spec ini memakai entitas khusus yang tidak dipakai spec lain, sehingga daftar hanya memuat 26 Service Center di bawah.
  - DU-020-1: Entitas `Entitas Halaman {runId}`, berisi data di bawah dan tidak memuat Service Center lain.
  - DU-020-2: User `Dian Halaman {runId}`, role Total Control, cakupan seluruh Group di `Entitas Halaman {runId}`, Status `Active`.
  - DU-020-3: Group `Cabang Halaman {runId}`, anak langsung dari root pohon Group.
  - DU-020-4: 12 Service Center `Pagin 01 {runId}` sampai `Pagin 12 {runId}`, Service type `Routine`, Available to `Cabang Halaman {runId}`, City `Kota Halaman Satu {runId}`, Usage `0`, Status `Active`.
  - DU-020-5: 13 Service Center `Pagin 13 {runId}` sampai `Pagin 25 {runId}`, Service type `Routine`, Available to `Cabang Halaman {runId}`, City `Kota Halaman Dua {runId}`, Usage `0`, Status `Active`.
  - DU-020-6: Service Center `Pagin 26 {runId}`, Service type `Routine`, Available to `Cabang Halaman {runId}`, City `Kota Halaman Dua {runId}`, Usage `0`, Status `Active`; dihapus oleh langkah spec ini.
  - DU-020-7: Parameter Jump to page: `99` dan `0`.
- Kondisi: client memiliki lisensi addon Maintenance berstatus aktif.

## Test Steps

### Daftar memakai 10 baris per halaman dengan pilihan 10, 25, 50, dan 100
1. Verifikasi laporan paginasi `Showing 1 to 10 of 26` tampil
2. Verifikasi baris pertama pada halaman 1 adalah `Pagin 01 {runId}`
3. Klik dropdown `Rows per page`
4. Verifikasi opsi `10`, `25`, `50`, dan `100` tampil berurutan
5. Tekan Esc untuk menutup daftar opsi `Rows per page`
6. Klik halaman `3` pada paginasi daftar
7. Verifikasi laporan paginasi `Showing 21 to 26 of 26` tampil
8. Verifikasi baris terakhir pada halaman 3 adalah `Pagin 26 {runId}`

### Ukuran halaman 25 membagi 26 baris menjadi dua halaman dan kembali ke halaman 1
9. Klik dropdown `Rows per page`
10. Pilih `25`
11. Verifikasi laporan paginasi `Showing 1 to 25 of 26` tampil
12. Klik halaman `2` pada paginasi daftar
13. Verifikasi laporan paginasi `Showing 26 to 26 of 26` tampil

### Filter City dengan lebih dari 10 hasil menghasilkan dua halaman
14. Klik dropdown `Rows per page`
15. Pilih `10`
16. Klik ikon `Filter` pada toolbar daftar
17. Pilih `Kota Halaman Satu {runId}` pada filter `City`
18. Klik `[Apply]`
19. Verifikasi laporan paginasi `Showing 1 to 10 of 12` tampil
20. Klik halaman `2` pada paginasi daftar
21. Verifikasi laporan paginasi `Showing 11 to 12 of 12` tampil
22. Klik `[Clear Field]`
23. Klik `[Apply]`

### Nomor halaman tidak valid pada field Jump to page
24. Isi field `Jump to page` dengan `99`, tekan Enter
25. Verifikasi laporan paginasi `Showing 21 to 26 of 26` tampil, yaitu halaman terakhir[^drift-1]
26. Isi field `Jump to page` dengan `0`, tekan Enter
27. Verifikasi laporan paginasi `Showing 1 to 10 of 26` tampil, yaitu halaman 1[^drift-1]

### Hapus baris terakhir di halaman terakhir berpindah ke halaman terakhir yang masih ada
28. Klik dropdown `Rows per page`
29. Pilih `25`
30. Klik halaman `2` pada paginasi daftar
31. Verifikasi baris `Pagin 26 {runId}` satu-satunya baris pada halaman 2
32. Klik `⋯` pada baris `Pagin 26 {runId}`
33. Klik `Delete`
34. Klik `[Delete]` pada dialog `Delete Service Center`
35. Verifikasi laporan paginasi `Showing 1 to 25 of 25` tampil, yaitu halaman terakhir yang masih ada, halaman 1
36. Verifikasi baris `Pagin 26 {runId}` tidak tampil pada halaman 1
37. Verifikasi tombol `Next Page` dan `Last Page` nonaktif, karena jumlah baris tepat sama dengan ukuran halaman

### Modal Changelog memakai ukuran halaman bawaan yang sama
38. Klik ikon `Changelog` pada toolbar daftar
39. Verifikasi dropdown `Rows per page` pada modal menampilkan `10`
40. Tutup modal Changelog lewat icon close

[^drift-1]: Drift foundation vs kontrak. Foundation `prd-conventions.md` §9.18: «Nomor halaman tidak valid diabaikan» (unit EB-TBL-7, bagian yang dimiliki spec ui-client), PRD §9.5 r11 yang mengikuti `prd-conventions.md` §9.11 tidak menyebut perilaku field ini. Kontrak `Paginator#9` dan `Paginator#50`: halaman di atas jumlah halaman pindah ke halaman terakhir, halaman di bawah 1 pindah ke halaman 1. Diasersi: kontrak, karena memberi hasil yang bisa diamati; bila foundation dimaksud tetap di halaman sekarang, kedua langkah itu berubah.
