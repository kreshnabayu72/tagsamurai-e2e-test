---
id: TC-GS-FILEMGR-E2E-017-bulk-action-bar-seleksi-select-all-dan-retensi
title: "Bulk Action Bar Tabel Utama: Counter, Checkbox Header, Select All, dan Retensi Seleksi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-71
  - TC-GS-FILEMGR-72
  - TC-GS-FILEMGR-73
  - TC-GS-FILEMGR-74
  - TC-GS-FILEMGR-77
  - TC-GS-FILEMGR-78
coverage:
  web: automated
---

# Bulk Action Bar Tabel Utama: Counter, Checkbox Header, Select All, dan Retensi Seleksi

## Prerequisites

- Mode: FE+BE.
- Akun aktor (seluruh spec): Total Control Sinta Maharani `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel A1 TC), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Data Pre-setup (hanya dibaca; spec tidak membuat, mengubah, maupun menghapus data): Tabel A2, 33 file aktif (4 halaman pada ukuran halaman 10), termasuk F01 `budi-avatar.jpg` dan F02 `siti-profile.png`. Hook `before` memastikan Tabel A2 tersedia secara idempotent dan tidak ada baris aktif lain di tabel utama (total tepat 33; spec lain membersihkan seed-nya sendiri).
- State global yang dibaca: Selection Limit di Lifecycle Settings > System Limits harus lebih besar dari 33 (TC-GS-FILEMGR-74). Spec tidak mengubah nilai itu; bila nilai environment tidak memenuhi, tim FE menyetelnya di hook `before` dan memulihkannya di `after`.
- Kemampuan teknis: tidak ada tambahan.
- Suite serial (`parallel: false`). Guided Tooltip: mengikuti pernyataan hook suite di `suite.md`.
- Hook `beforeEach`: kosongkan seleksi dan kembali ke Global Settings > File Manager.

## Test Steps

### TC-GS-FILEMGR-71: Screening Bulk Action Bar

1. Centang checkbox baris `budi-avatar.jpg`
2. Verifikasi Bulk Action Bar tampil di atas tabel rata kiri
3. Verifikasi urutan elemen bar: tombol `Bulk Action`, teks `1 File selected`, tombol `Select All (33 records)`, ikon `×`
4. Klik tombol `Bulk Action` untuk membuka overlay
5. Verifikasi overlay memuat satu aksi: `Delete` (ikon DeleteBin6Line, severity danger)
6. Verifikasi toolbar Table Tools tetap tampil rata kanan pada baris yang sama dengan bar
7. Tutup overlay `Bulk Action` dengan Esc

### TC-GS-FILEMGR-72: Siklus counter dan penutupan bar lewat `×`

8. Klik ikon `×` pada bar untuk mengosongkan seleksi
9. Centang baris `budi-avatar.jpg`
10. Verifikasi bar menampilkan `1 File selected`
11. Centang baris `siti-profile.png`
12. Verifikasi bar menampilkan `2 Files selected`
13. Hapus centang baris `siti-profile.png`
14. Verifikasi bar menampilkan `1 File selected`
15. Klik ikon `×` di bar
16. Verifikasi semua centang terhapus
17. Verifikasi bar hilang

### TC-GS-FILEMGR-73: Checkbox header memilih seluruh baris halaman aktif

18. Centang checkbox baris pertama saja
19. Verifikasi checkbox header berstatus indeterminate (`[-]`)
20. Verifikasi bar menampilkan `1 File selected`
21. Klik checkbox header
22. Verifikasi 10 baris halaman aktif tercentang dan checkbox header checked
23. Verifikasi bar menampilkan `10 Files selected`
24. Klik checkbox header lagi
25. Verifikasi semua baris tidak tercentang
26. Verifikasi bar hilang

### TC-GS-FILEMGR-74: Select All lintas halaman dan Unselect All

27. Centang satu baris
28. Klik tombol `Select All (33 records)`
29. Verifikasi bar menampilkan `33 Files selected`
30. Verifikasi tombol berubah menjadi `Unselect All`
31. Pindah ke halaman 2
32. Verifikasi baris pada halaman 2 tercentang
33. Hapus centang satu baris pada halaman 2
34. Verifikasi bar menampilkan `32 Files selected`
35. Verifikasi tombol kembali menjadi `Select All (33 records)`
36. Klik tombol `Select All (33 records)`, lalu klik `Unselect All`
37. Verifikasi seluruh seleksi dibatalkan
38. Verifikasi bar hilang

### TC-GS-FILEMGR-77: Seleksi bertahan saat pindah halaman dan sort

39. Pindah ke halaman 1
40. Centang baris `budi-avatar.jpg`
41. Pindah ke halaman 2
42. Verifikasi bar menampilkan `1 File selected`
43. Klik header File Name sekali (Ascending)
44. Pindah ke halaman yang memuat `budi-avatar.jpg`
45. Verifikasi baris `budi-avatar.jpg` tetap tercentang
46. Verifikasi bar menampilkan `1 File selected`
47. Klik ikon `×` pada bar, lalu reset sort ke urutan default (klik header File Name sampai kembali ke urutan default)

### TC-GS-FILEMGR-78: Seleksi bertahan saat Search diubah

48. Centang baris `budi-avatar.jpg` dan `siti-profile.png`
49. Ketik Search `siti`, tekan Enter
50. Verifikasi sedikitnya satu baris tampil pada tabel
51. Verifikasi tabel hanya memuat `siti-profile.png`
52. Verifikasi bar menampilkan `2 Files selected`
53. Klik `✕` pada Search, tekan Enter pada input kosong
54. Verifikasi baris `budi-avatar.jpg` dan `siti-profile.png` tetap tercentang
55. Verifikasi bar menampilkan `2 Files selected`
56. Klik ikon `×` pada bar untuk mengosongkan seleksi

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular. Spec tidak menghabisi data; urutan TC mengikuti TC sumber.
- Spec melewati sekitar 35 langkah (56 langkah nominal, tanpa blok yang diulang). Alasan pertahanan: seluruh blok satu kelas (fungsional murni FE tanpa mutasi data) pada dataset yang sama (prinsip 1: topik satu dataset yang tetap digabung; Bulk Action Bar, Select All, dan retensi seleksi berbagi Tabel A2), dan setiap blok dimulai dari seleksi kosong (langkah 8, 18, 27, 39, 48 didahului pembersihan seleksi) sehingga asersi soft tetap bermakna walau blok sebelumnya gagal; kegagalan keras pada elemen Bulk Action Bar sendiri akan menutup seluruh blok.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): 7 (menutup overlay), 8 (mengosongkan seleksi), 31 (pindah halaman TC-GS-FILEMGR-74 butir 2), 39 (kembali ke halaman 1), 47 dan 56 (mengosongkan seleksi dan mereset sort, S-09), 49 (Search atomik "ketik, tekan Enter").
- Asersi tambahan di luar Expected TC (S-03): langkah 50 (baris pembanding sebelum asersi universal "hanya memuat", butir 2 bagian 8b).
- Langkah 36 melakukan dua klik berurutan (`Select All (33 records)` lalu `Unselect All`) sesuai langkah 4 TC-GS-FILEMGR-74.
- Langkah 44 menyebut "halaman yang memuat `budi-avatar.jpg`" seperti TC sumber; posisi halamannya mengikuti sort Ascending File Name dan tidak ditetapkan angka (S-14: halaman dicari setelah sort).
- Temuan untuk QA:
  - Q-2: precondition TC-GS-FILEMGR-74 menyatakan "Selection Limit lebih besar dari 33" tanpa menyebut nilai Selection Limit; PRD Lifecycle Settings menetapkan default 1.000 dengan rentang 100 sampai 5.000, sehingga spec memperlakukannya sebagai state global yang dibaca dan dipastikan lebih besar dari 33 di hook `before`, disediakan tim FE bila perlu.
  - Q-7: TC-GS-FILEMGR-71 s.d. 78 menghitung total 33 baris; hitungan itu valid hanya bila tidak ada baris aktif lain (D05, D06, D08 menambah baris pada TC tertentu di spec lain). Spec ini mengandalkan hook `before` dan suite serial.
  - TC-GS-FILEMGR-78 langkah 3 menyebut "ikon (✕) di input Search lalu tekan Enter pada input kosong"; spec menulis "Klik `✕` pada Search, tekan Enter" sesuai bagian 8b butir 9.
  - Post Condition semua TC bernilai `-`.
