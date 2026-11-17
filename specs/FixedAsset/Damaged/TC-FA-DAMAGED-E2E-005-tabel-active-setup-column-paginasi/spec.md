---
id: TC-FA-DAMAGED-E2E-005-tabel-active-setup-column-paginasi
title: "Konfigurasi Setup Column sub-tab Active bertahan sesudah muat ulang dan paginasi berjalan atas baris ber-{runId}"
layer: ui-e2e
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: [T-DMG-01, "§5#r2", "§5#r8", "§9.5#r4", EB-KOL-2@tabel-active]
smoke: []
dependsOn: []
trace:
  T-DMG-01: [34, 45]
  "§5#r2": [3, 5, 7, 22, 24, 48, 51, 55, 57, 60]
  "§5#r8": [30]
  "§9.5#r4": [3, 5, 7, 9, 11, 17, 18, 48, 51, 55, 57, 60]
  EB-KOL-2@tabel-active: [36, 40, 45]
anchor: []
coverage:
  web: automated
---

# Konfigurasi Setup Column sub-tab Active bertahan sesudah muat ulang dan paginasi berjalan atas baris ber-{runId}

## Prerequisites
- Aktor: Total Control, user `Admin T`.
- Layar awal: halaman Assets.
- Data:
  - DU-005-1: `10` record berstatus `Reported Disposal` di Group `Head Office {runId}`, Name `Paginasi Aset {runId} - {n}`, Asset ID `PGN-1{n}-{runId}`, Source `Manual`, Reported By `Agus P`, Reported Date `T0 − 5 hari, pukul 10:00`, Days Damaged `5 days`.
  - DU-005-2: `16` record berstatus `Damaged` di Group `Warehouse {runId}`, Name `Paginasi Aset {runId} - {n}`, Asset ID `PGN-2{n}-{runId}`, Source `Manual`, Reported By `Agus P`, Reported Date `T0 − 6 hari, pukul 10:00`, Days Damaged `6 days`.
  - DU-005-3: konfigurasi kolom yang diubah: kolom `Source` disembunyikan, kolom `Brand` ditambahkan, dan kolom `Last Holder` disembunyikan lewat panel cepat.
  - Seluruh `26` record berjalan itu tampil pada pencarian kata kunci runId dengan ukuran halaman bawaan `10`; user `Agus P` adalah user ber-runId, Pelapor admin.
- Kondisi:
  - Selection Limit bernilai `1000`.

## Test Steps

### Paginasi dengan ukuran halaman bawaan
1. Buka tab `Damaged` pada halaman Assets
2. Ketik Search `{runId}`, tekan Enter
3. Verifikasi halaman `1` memuat `10` baris
4. Pindah ke halaman `2`
5. Verifikasi halaman `2` memuat `10` baris
6. Pindah ke halaman `3`
7. Verifikasi halaman `3` memuat `6` baris

### Paginasi dengan ukuran halaman 25
8. Ubah ukuran halaman menjadi `25`
9. Verifikasi halaman `1` memuat `25` baris
10. Pindah ke halaman `2`
11. Verifikasi halaman `2` memuat `1` baris
12. Ubah ukuran halaman menjadi `10`

### Penyaringan mereset halaman dan membentuk jumlah halaman baru
13. Pindah ke halaman `2`
14. Klik ikon `Filter`
15. Pilih Group `Head Office {runId}` pada field `Group`
16. Klik `[Apply]`
17. Verifikasi tabel kembali ke halaman `1` dan memuat `10` baris
18. Verifikasi tidak ada halaman `2` karena jumlah baris sama dengan ukuran halaman
19. Klik `[Clear Field]`
20. Pilih opsi `Damaged` pada field `Status`
21. Klik `[Apply]`
22. Verifikasi halaman `1` memuat `10` baris
23. Pindah ke halaman `2`
24. Verifikasi halaman `2` memuat `6` baris
25. Klik `[Clear Field]`
26. Klik `[Apply]`
27. Klik ikon `Filter` untuk menutup Filter Panel

### Setup Column menyimpan konfigurasi kolom
28. Klik header kolom Actions `⋯`
29. Klik `Setup Column...`
30. Verifikasi modal `Setup Column` memuat kolom `Purchase Cost`, `Asset Value (Commercial)`, dan `Asset Value (Fiscal)` bagi aktor yang berhak
31. Hapus centang `Source`
32. Centang `Brand`
33. Klik `[Save]`
34. Verifikasi kolom `Source` tidak tampil dan kolom `Brand` tampil
35. Muat ulang halaman
36. Verifikasi kolom `Source` tetap tidak tampil dan kolom `Brand` tetap tampil sesudah muat ulang
37. Klik header kolom Actions `⋯`
38. Hapus centang `Last Holder`
39. Muat ulang halaman
40. Verifikasi kolom `Last Holder` tetap tidak tampil sesudah muat ulang karena perubahan dari panel cepat langsung tersimpan

### Reset to Default mengembalikan kolom bawaan
41. Klik header kolom Actions `⋯`
42. Klik `Setup Column...`
43. Klik `[Reset to Default]`
44. Klik `[Save]`
45. Verifikasi kolom `Source` dan `Last Holder` tampil dan kolom `Brand` tidak tampil

### Search yang mengubah kriteria mereset halaman ke halaman 1
46. Pindah ke halaman `2`
47. Ganti isi kotak search dengan `Paginasi Aset {runId}`, tekan Enter
48. Verifikasi tabel kembali ke halaman `1` dan memuat `10` baris sesudah Search dijalankan dari halaman `2`
49. Pindah ke halaman `2`
50. Klik `(←)` pada kotak Search
51. Verifikasi tabel kembali ke halaman `1` sesudah Search dikosongkan dari halaman `2`

### Pengosongan saringan mereset halaman ke halaman 1
52. Klik ikon `Filter`
53. Pilih Group `Warehouse {runId}` pada field `Group`
54. Klik `[Apply]`
55. Verifikasi halaman `1` memuat `10` baris
56. Pindah ke halaman `2`
57. Verifikasi halaman `2` memuat `6` baris
58. Klik `[Clear Field]`
59. Klik `[Apply]`
60. Verifikasi tabel kembali ke halaman `1` sesudah saringan dikosongkan dari halaman `2`
61. Klik ikon `Filter` untuk menutup Filter Panel
