---
id: TC-AC-PP-E2E-041-pagination-preservasi-state-dan-modal
title: "Pagination, Preservasi State, dan Reset Tabel Version History"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PP-29
  - TC-AC-PP-148
  - TC-AC-PP-149
  - TC-AC-PP-150
  - TC-AC-PP-151
  - TC-AC-PP-152
  - TC-AC-PP-153
coverage:
  web: automated
---

# Pagination, Preservasi State, dan Reset Tabel Version History

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, nama tampil Andi Wijaya, env var `AC_TC_PASSWORD`). Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Dataset: Riwayat B (Version 1 sampai 120; Published By bergantian, ganjil `John Doe` dan genap `Jane Smith`; Version 120 Active). Hook `before` men-seed Riwayat B lewat Fixture BE (kemampuan teknis: membuat ulang dataset Riwayat; riwayat append-only sehingga tidak bisa dihapus lewat UI). Hook `after` mengembalikan dataset ke Riwayat A.
- General Settings: Date Format `dd MMM yy`, Time Format 24-hour, Time Zone UTC (tidak diubah spec ini).
- Suite berjalan serial (`parallel: false`) karena dokumen Privacy Policy bersifat tunggal platform-wide; spec ini tidak membuat atau mengubah versi.
- Tidak ada fixture nilai tetap: halaman dibuka lewat sidebar (Settings > Privacy Policy).

## Test Steps

### TC-AC-PP-148: Default 10 baris per halaman dan pilihan page size 10, 25, 50, 100

1. Buka Settings > Privacy Policy lewat sidebar
2. Verifikasi footer menampilkan `1–10 of 120`
3. Verifikasi tabel menampilkan 10 baris
4. Buka pilihan page size
5. Verifikasi pilihan page size adalah 10, 25, 50, 100
6. Verifikasi tidak ada opsi "All"
7. Tutup pilihan page size tanpa mengubah nilai

### TC-AC-PP-149: Navigasi halaman lewat next, previous, nomor halaman, dan input nomor halaman

8. Klik next
9. Verifikasi footer menampilkan `11–20 of 120`
10. Klik previous
11. Verifikasi footer menampilkan `1–10 of 120`
12. Ketik 12 pada input nomor halaman lalu tekan Enter
13. Verifikasi footer menampilkan `111–120 of 120`
14. Verifikasi tabel menampilkan 10 baris
15. Ketik 0 pada input nomor halaman lalu tekan Enter
16. Verifikasi input `0` diabaikan
17. Verifikasi tabel tetap di halaman 12
18. Ketik 13 pada input nomor halaman lalu tekan Enter
19. Verifikasi input `13` diabaikan
20. Verifikasi tabel tetap di halaman 12
21. Ketik `abc` pada input nomor halaman lalu tekan Enter
22. Verifikasi input `abc` diabaikan
23. Verifikasi tabel tetap di halaman 12

### TC-AC-PP-151: Badge Active hanya tampil bila baris Active berada pada hasil yang tampil

24. Klik item "Privacy Policy" pada sidebar untuk kembali ke halaman 1 dengan page size 10
25. Verifikasi baris `Version 120` memiliki badge `Active`
26. Verifikasi tidak ada baris lain berbadge `Active` pada halaman 1
27. Klik halaman 2
28. Verifikasi tidak ada badge `Active` pada seluruh baris halaman 2
29. Klik halaman 1
30. Klik icon Search, ketik "doe", lalu tekan Enter
31. Verifikasi hasil hanya memuat Version ganjil sehingga `Version 120` tidak tampil
32. Verifikasi tidak ada badge `Active` di tabel

### TC-AC-PP-150: Mengganti page size mengembalikan tabel ke halaman 1

33. Klik item "Privacy Policy" pada sidebar untuk mereset Search dan paginasi ke default
34. Klik halaman 3
35. Ubah page size menjadi 25
36. Verifikasi tabel kembali ke halaman 1
37. Verifikasi footer menampilkan `1–25 of 120`
38. Verifikasi tabel menampilkan 25 baris

### TC-AC-PP-29: Menutup Modal View lewat [✕] kembali ke tabel tanpa mereset halaman dan page size

39. Klik item "Privacy Policy" pada sidebar untuk mereset ke default (page size 10, halaman 1)
40. Ubah page size menjadi 25
41. Klik halaman 2
42. Catat nomor Version pada seluruh baris halaman 2 (page size 25) sebagai baseline
43. Klik teks tautan pada baris pertama halaman 2 sehingga modal View terbuka
44. Klik `[✕]` di header modal
45. Verifikasi modal tertutup
46. Verifikasi tidak ada dialog yang tampil
47. Verifikasi tabel tetap menampilkan halaman 2
48. Verifikasi tabel tetap menampilkan page size 25
49. Verifikasi tabel menampilkan baris yang sama dengan baseline yang dicatat sebelum modal dibuka

### TC-AC-PP-152: Refresh F5 mempertahankan Search, halaman aktif, dan page size

50. Klik item "Privacy Policy" pada sidebar untuk mereset ke default
51. Ubah page size menjadi 25
52. Klik icon Search, ketik "doe", lalu tekan Enter
53. Klik halaman 2
54. Tekan F5
55. Verifikasi input Search tetap `doe`
56. Verifikasi halaman aktif tetap 2
57. Verifikasi page size tetap 25
58. Verifikasi tabel menampilkan baris halaman 2 hasil pencarian `doe`

### TC-AC-PP-153: Klik ulang menu Privacy Policy di sidebar mereset Search dan paginasi ke default

59. Klik item "Privacy Policy" pada sidebar
60. Verifikasi input Search kosong
61. Verifikasi tabel menampilkan data tanpa penyaringan
62. Verifikasi tabel di halaman 1
63. Verifikasi page size 10
64. Verifikasi footer menampilkan `1–10 of 120`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-privacy-policy/TestCases/tc-settings-privacy-policy.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC di spec ini 148, 149, 151, 150, 29, 152, 153 (TC sumber bernomor 29, 148 sampai 153). Alasan: screening dan navigasi dulu (148, 149), TC yang membaca badge Active pada page size default (151) sebelum page size diubah, lalu 150 dan 29 yang mengubah page size, dan 153 terakhir karena precondition-nya (Search `doe` aktif pada halaman 2) sama dengan akhir TC-152 (S-05, S-10).
- Langkah penghubung (tanpa `Verifikasi`; S-03, S-09): langkah 7, 24, 29, 33, 39, 50 (kembalikan tabel ke default lewat klik ulang menu sidebar; perilaku reset ini adalah objek uji TC-153), langkah 40 (page size 25 sebagai precondition TC-29), dan langkah 42 (catat baris halaman 2 sebagai baseline sebelum modal dibuka, S-12).
- Langkah 59 (TC-153) melanjutkan state akhir TC-152 (Search `doe`, halaman 2, page size 25) sesuai precondition TC-153, tanpa membuka ulang halaman.
- Spec tidak membuat data dan tidak mengubah Pre-setup; hook `after` hanya mengembalikan dataset ke Riwayat A dan sesi ke akun default.
- Temuan untuk QA: precondition TC-153 hanya menyebut Search `doe` aktif pada halaman 2 dan tidak menyebut page size; Expected `1–10 of 120` mengasumsikan page size kembali ke default 10. Spec melanjutkan state akhir TC-152 (page size 25) sehingga reset page size ikut teruji. Spec mengikuti TC.
- Panjang spec (64 langkah) melewati perkiraan 35 langkah karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Alasan tidak dipecah: TC dalam spec satu topik, satu akun, dan satu dataset; tiap bagian dipisah subjudul TC dan tetap bermakna walau bagian sebelumnya gagal karena state dikembalikan di langkah penghubung (batas ukuran konvensi bagian 3 bukan jumlah langkah).
