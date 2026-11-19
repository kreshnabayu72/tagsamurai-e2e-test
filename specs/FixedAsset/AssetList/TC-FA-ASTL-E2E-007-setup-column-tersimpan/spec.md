---
id: TC-FA-ASTL-E2E-007-setup-column-tersimpan
title: "Konfigurasi Setup Column bertahan per user"
layer: ui-e2e
priority: Critical
caseType: Positive
status: ready-for-automation
sourceRules: [F-ASTL-05, "§5#r8", "EB-SRC-5@tabel-all-assets", "EB-KOL-2@tabel-all-assets"]
smoke: []
dependsOn: []
trace:
  F-ASTL-05: [16, 17]
  "§5#r8": [16, 44, 48, 50]
  "EB-SRC-5@tabel-all-assets": [7, 9]
  "EB-KOL-2@tabel-all-assets": [19, 20, 25, 26, 27, 30, 34, 35, 36, 61, 69, 71, 72, 73]
anchor: [4, 63, 64, 65]
coverage:
  web: automated
---

# Konfigurasi Setup Column bertahan per user

## Prerequisites
- Aktor: Total Control `Ratna Dewi {runId}`, dan Total Control `Bagus Santoso {runId}` sebagai user lain.
- Layar awal: Fixed Asset > Assets (tab `Assets`).
- Data:
  - DU-007-1: User `Ratna Dewi {runId}`, role Total Control, cakupan seluruh client, memakai konfigurasi kolom bawaan.
  - DU-007-2: User `Bagus Santoso {runId}`, role Total Control, cakupan seluruh client, memakai konfigurasi kolom bawaan.
  - DU-007-3: Aset `Tablet Tab A - 1 {runId}` dengan Brand `Samsung {runId}`.
  - Konfigurasi kolom bawaan: kolom `Labels` Visible, kolom `Alias Name` Hidden, dan kolom `Brand` berada sebelum kolom `Group`.
- Kondisi:
  - Akun `Ratna Dewi {runId}` dan `Bagus Santoso {runId}` aktif dan kredensialnya tersedia.

## Test Steps

### Kolom tersembunyi tidak ikut dicari dan cocok lagi saat ditampilkan
1. Masuk sebagai `Ratna Dewi {runId}`
2. Klik menu `Fixed Asset > Assets` pada sidebar
3. Ketik Search `Samsung {runId}`, tekan Enter
4. Verifikasi baris `Tablet Tab A - 1 {runId}` tampil karena `Samsung {runId}` cocok pada kolom `Brand`
5. Klik header kolom `Actions`
6. Lepas centang kolom `Brand` pada panel Column Visibility
7. Verifikasi tabel menampilkan empty state `No results found` karena kolom `Brand` yang disembunyikan tidak lagi dicari
8. Centang kolom `Brand` pada panel Column Visibility
9. Verifikasi baris `Tablet Tab A - 1 {runId}` tampil kembali

### Konfigurasi Setup Column disimpan lewat Save
10. Klik header kolom `Actions`
11. Klik `Setup Column...`
12. Lepas centang kolom `Labels` pada modal Setup Column
13. Centang kolom `Alias Name` pada modal Setup Column
14. Pindahkan kolom `Group` ke posisi sebelum kolom `Brand` pada modal Setup Column
15. Klik `[Save]`
16. Verifikasi tabel tidak memuat kolom `Labels` dan memuat kolom `Alias Name`
17. Verifikasi kolom `Group` berada sebelum kolom `Brand`

### Konfigurasi bertahan sesudah muat ulang, keluar-masuk, dan sesi browser lain
18. Muat ulang halaman
19. Verifikasi tabel tidak memuat kolom `Labels` dan memuat kolom `Alias Name`
20. Verifikasi kolom `Group` berada sebelum kolom `Brand`
21. Ketik Search `Samsung {runId}`, tekan Enter
22. Keluar dari akun
23. Masuk sebagai `Ratna Dewi {runId}`
24. Klik menu `Fixed Asset > Assets` pada sidebar
25. Verifikasi tabel tidak memuat kolom `Labels` dan memuat kolom `Alias Name`
26. Verifikasi kolom `Group` berada sebelum kolom `Brand`
27. Verifikasi kotak Search tidak berisi `Samsung {runId}` karena Search tidak ikut tersimpan di akun
28. Buka sesi browser baru yang terpisah dan masuk sebagai `Ratna Dewi {runId}`
29. Klik menu `Fixed Asset > Assets` pada sidebar
30. Verifikasi tabel tidak memuat kolom `Labels` dan memuat kolom `Alias Name`

### User lain tetap melihat kolom bawaan
31. Keluar dari akun
32. Masuk sebagai `Bagus Santoso {runId}`
33. Klik menu `Fixed Asset > Assets` pada sidebar
34. Verifikasi tabel memuat kolom `Name` dan kolom `Labels`
35. Verifikasi tabel tidak memuat kolom `Alias Name`
36. Verifikasi kolom `Brand` berada sebelum kolom `Group`

### Reset to Default mengembalikan konfigurasi dan kolom terakhir tidak bisa disembunyikan
37. Keluar dari akun
38. Masuk sebagai `Ratna Dewi {runId}`
39. Klik menu `Fixed Asset > Assets` pada sidebar
40. Klik header kolom `Actions`
41. Klik `Setup Column...`
42. Klik `[Reset to Default]`
43. Klik `[Save]`
44. Verifikasi tabel memuat kolom `Labels`, tidak memuat kolom `Alias Name`, dan kolom `Brand` berada sebelum kolom `Group`
45. Klik header kolom `Actions`
46. Klik `Setup Column...`
47. Lepas centang semua kolom selain `Name` pada modal Setup Column
48. Verifikasi checkbox kolom `Name` tidak aktif dan memuat alasan `At least one column must remain visible.`
49. Klik `✕` pada modal Setup Column
50. Verifikasi tabel memuat kolom `Labels` karena perubahan yang tidak disimpan dibuang

### Pin kolom tersimpan di akun, sedangkan Filter, Sort, dan ukuran halaman bertahan sesudah muat ulang tetapi tidak tersimpan di akun
51. Klik ikon Filter
52. Pilih Brand `Samsung {runId}` pada Filter Panel
53. Klik `[Apply]`
54. Klik header kolom `Brand`
55. Pilih ukuran halaman `25`
56. Klik header kolom `Actions`
57. Klik `Setup Column...`
58. Pin kolom `Brand` pada modal Setup Column
59. Klik `[Save]`
60. Muat ulang halaman
61. Verifikasi kolom `Brand` tetap ter-pin sesudah muat ulang
62. Klik ikon Filter
63. Verifikasi field Brand pada Filter Panel masih berisi `Samsung {runId}` karena muat ulang mempertahankan Filter yang sudah di-Apply
64. Verifikasi header kolom `Brand` menampilkan indikator sort aktif karena muat ulang mempertahankan Sort
65. Verifikasi ukuran halaman tetap `25` karena muat ulang mempertahankan ukuran halaman
66. Keluar dari akun
67. Masuk sebagai `Ratna Dewi {runId}`
68. Klik menu `Fixed Asset > Assets` pada sidebar
69. Verifikasi kolom `Brand` tetap ter-pin sesudah keluar dan masuk lagi
70. Klik ikon Filter
71. Verifikasi field Brand pada Filter Panel kosong dengan placeholder `All brands` karena Filter tidak tersimpan di akun
72. Verifikasi header kolom `Brand` tidak menampilkan indikator sort aktif karena Sort tidak tersimpan di akun
73. Verifikasi ukuran halaman kembali `10` karena ukuran halaman tidak tersimpan di akun
