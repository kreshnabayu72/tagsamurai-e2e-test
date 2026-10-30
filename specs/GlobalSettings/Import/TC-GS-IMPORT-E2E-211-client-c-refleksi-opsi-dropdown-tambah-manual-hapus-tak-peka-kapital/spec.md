---
id: TC-GS-IMPORT-E2E-211-client-c-refleksi-opsi-dropdown-tambah-manual-hapus-tak-peka-kapital
title: "Client C: refleksi opsi Dropdown (tambah manual, hapus, tak peka kapital) dan tipe diubah ke Phone, termasuk Custom Field Deactivated dengan Create Missing Options"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-513
  - TC-GS-IMPORT-519
  - TC-GS-IMPORT-521
  - TC-GS-IMPORT-934
  - TC-GS-IMPORT-963
coverage:
  web: automated
---

# Client C: refleksi opsi Dropdown (tambah manual, hapus, tak peka kapital) dan tipe diubah ke Phone, termasuk Custom Field Deactivated dengan Create Missing Options

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memutasi Custom Field Client C (state global) dan memulihkannya (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net`, password `Spectra.env.GS_CLIENTC_TC_PASSWORD`.
- Pelaku kedua (pemicu via sesi API, bukan sesi UI): Admin kedua Client C (Oki Setiawan) `totalControlSecond_automated_qaTeam3@qwertysystem.net`, password `Spectra.env.GS_CLIENTC_TC2_PASSWORD` (nama env baru). Sesi API mengubah Custom Field di Custom Field User (tipe, opsi, status Active); klien HTTP dan kontrak endpoint disediakan tim FE/BE (tidak tertulis di TC).
- Layar awal: hook `beforeEach` membuka Import > User Login Client C; Sub-Tab User Non Login dibuka di langkah.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Pre-setup: Client C tanpa draft di Tab User Login dan User Non Login (Kontrak Fixture R1; reset oleh hook `beforeEach` suite dan oleh langkah pemulihan). Custom Field Active Client C: Shift (Dropdown Pagi/Siang/Malam, Optional), Shift Notes (Text Area), Overtime Hours, Emergency Phone, Join Date, Tax ID (Text, Optional); User Login aktif `rina.admin.c@example.com` dan `budi.manager.c@example.com`; Division `Engineering` ada. Nama field dan opsi literal dipakai (pengecualian S-12 butir (ii): nama dan opsi menentukan nilai sel dan teks error). Opsi `Lembur` dan `Piket` belum menjadi opsi `Shift`.
- Berkas uji (pembuat data lewat upload UI; draft tidak di-commit; Email diberi suffix per run `+{runId}-211` sebelum `@` bila berkas dibuat per run):
  - `user-login-shift-case.csv`: header First Name; Last Name; Email; Division; Access; Shift; 2 baris, Division `Engineering`, Access `Global Settings`, Shift `siang` (baris 1) dan `MALAM` (baris 2).
  - `user-login-shift-notes-phone.csv`: header First Name; Last Name; Email; Division; Access; Shift Notes; 1 baris, Division `Engineering`, Access `Global Settings`, Shift Notes `081234567`.
  - `user-non-login-shift-3rows.csv`: header First Name; Last Name; Email; Division; Represented By; Shift; 3 baris, Division `Engineering`, Represented By `rina.admin.c@example.com`, Shift `Siang` (baris 1 dan 3), `Pagi` (baris 2).
  - D-79 `user-login-shift-lembur.csv`: header First Name,Last Name,Email,Division,Position,Access,Shift; #1 Siti Rahmawati Shift `Lembur`; #2 Budi Santoso Shift `lembur ` (huruf kecil dengan spasi di akhir); #3 Andi Pratama Shift `Siang`; Division `Engineering`, Position kosong, Access `Global Settings`.
- Nilai uji: Number `812345678` (TC-GS-IMPORT-519); Shift `Pagi` (TC-GS-IMPORT-963 baris #1).
- Urutan TC: 513, 519, 521, 934, 963. Pemulihan (Custom Field, draft) dilakukan sebagai langkah aksi di akhir tiap blok (Kontrak Fixture R2) dan oleh hook `after` sebagai cadangan.
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): opsi `Lembur` dan `Piket` dihapus dari `Shift`; opsi `Siang` ditambahkan kembali bila hilang; `Shift` diaktifkan kembali; tipe `Shift Notes` dikembalikan ke Text Area; draft Tab User Login dan User Non Login Client C dibuang.
- Kemampuan teknis: pemilihan berkas; skrip reset draft Client C; sesi API Admin kedua.
- State global: Custom Field Client C (dipulihkan), flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Pencocokan opsi tak peka kapital (TC-GS-IMPORT-513)

1. Klik `[Upload File]` dan pilih `user-login-shift-case.csv`
2. Klik `[Confirm Mapping]`
3. Verifikasi Modal Column Mapping tertutup
4. Verifikasi tidak ada Error Banner
5. Verifikasi muncul toast sukses: "Success, row has been added."
6. Verifikasi kedua baris berstatus `pending` (Errors 0)
7. Verifikasi nilai Shift `siang` dan `MALAM` diterima
8. Pulihkan: buang draft Tab User Login Client C lewat skrip reset, muat ulang halaman

### Tipe diubah ke Phone (TC-GS-IMPORT-519)

9. Klik `[Upload File]` dan pilih `user-login-shift-notes-phone.csv`
10. Klik `[Confirm Mapping]`
11. Verifikasi Row # 1 berstatus `pending`
12. Admin kedua Client C (sesi API) mengubah tipe Custom Field `Shift Notes` dari Text Area ke Phone hingga tersimpan
13. Tekan `F5` pada halaman Import
14. Verifikasi Row # 1 berstatus `error`
15. Verifikasi Error Summary Callout memuat `Shift notes must include a valid country code` dengan badge "1 row"
16. Klik `⋯` pada Row # 1 lalu pilih Edit
17. Verifikasi input sel dibuka dengan Country Code default `🇮🇩 +62`
18. Verifikasi Number berisi `081234567`
19. Ganti isi input Number dengan `812345678`
20. Klik `[Save]`
21. Verifikasi Row # 1 berstatus `pending`
22. Verifikasi Staging Metric Cards menunjukkan Errors 0
23. Pulihkan: Admin kedua mengembalikan tipe `Shift Notes` ke Text Area, buang draft Tab User Login Client C lewat skrip reset, muat ulang halaman

### Opsi dihapus pada Tab User Non Login (TC-GS-IMPORT-521)

24. Pindah ke Sub-Tab User Non Login
25. Klik `[Upload File]` dan pilih `user-non-login-shift-3rows.csv`
26. Klik `[Confirm Mapping]`
27. Verifikasi ketiga baris berstatus `pending`
28. Admin kedua Client C (sesi API) menghapus opsi `Siang` dari Custom Field `Shift` hingga tersimpan
29. Tekan `F5` pada halaman Import
30. Verifikasi Row # 1 dan 3 berstatus `error`
31. Verifikasi Error Summary Callout memuat `Shift: Invalid option` dengan badge "2 rows"
32. Verifikasi Row # 2 (`Pagi`) tetap `pending`
33. Pulihkan: Admin kedua menambahkan kembali opsi `Siang` ke `Shift`, buang draft Tab User Non Login Client C lewat skrip reset, buka Sub-Tab User Login

### Opsi ditambahkan manual (TC-GS-IMPORT-934)

34. Total Control Client C: klik `[Upload File]` di toolbar dan pilih `user-login-shift-lembur.csv` (D-79)
35. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
36. Admin kedua Client C (sesi API) menambahkan opsi `Lembur` ke Custom Field `Shift` hingga tersimpan
37. Total Control Client C: tekan `F5` pada halaman Import
38. Verifikasi baris #1 dan #2 (Shift `Lembur` dan `lembur `) pulih ke `pending`
39. Verifikasi baris #3 (Shift `Siang`) tetap `pending`
40. Verifikasi Staging Metric Cards: Total Rows 3, Ready to Import 3, Errors 0
41. Verifikasi Error Summary Callout tidak tampil
42. Pulihkan: Admin kedua menghapus opsi `Lembur` dari `Shift`, buang draft Tab User Login Client C lewat skrip reset, muat ulang halaman

### Custom Field Deactivated, opsi tidak valid (TC-GS-IMPORT-963)

43. Total Control Client C: klik `[Upload File]` di toolbar dan pilih `user-login-shift-lembur.csv` (D-79)
44. Biarkan seluruh dropdown File Column pada nilai auto-match, klik `[Confirm Mapping]`
45. Admin kedua Client C (sesi API) menonaktifkan Custom Field `Shift` hingga tersimpan
46. Total Control Client C: muat ulang halaman Import > User Login
47. Verifikasi sel Shift baris #1 dan #2 menampilkan `Lembur`
48. Verifikasi baris #1 dan #2 berstatus `error`
49. Verifikasi Error Summary Callout memuat "Shift: Invalid option" dengan badge "2 rows"
50. Verifikasi Error Summary Callout tanpa tombol `[Create Missing Options]`
51. Klik `⋯` pada baris #1
52. Verifikasi menu `⋯` baris #1 tidak memuat `[Create Missing Options]`
53. Pilih Edit, pilih `Pagi` pada sel Shift baris #1, klik `[Save]`
54. Verifikasi muncul toast sukses: "Success, row has been updated."
55. Verifikasi baris #1 berstatus `pending`
56. Verifikasi Error Summary Callout memuat "Shift: Invalid option" dengan badge "1 row"
57. Verifikasi Error Summary Callout tanpa tombol `[Create Missing Options]`
58. Verifikasi Staging Metric Cards: Total Rows 3, Ready to Import 2, Errors 1
59. Klik `⋯` pada baris #2 lalu Edit, kosongkan sel Shift baris #2 (hapus pilihan pada Select), klik `[Save]`
60. Verifikasi muncul toast sukses: "Success, row has been updated." walau sel Shift baris #2 kosong
61. Verifikasi baris #2 berstatus `pending` tanpa border `danger`
62. Verifikasi Error Summary Callout tidak tampil
63. Verifikasi Staging Metric Cards: Total Rows 3, Ready to Import 3, Errors 0
64. Pulihkan: Admin kedua mengaktifkan kembali `Shift`, buang draft Tab User Login Client C lewat skrip reset

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 64 langkah, di atas 35 langkah. Alasan: lima blok berpola sama (upload UI, mutasi Custom Field Client C lewat sesi API, F5, baca Staging Table) pada satu client dan satu akun; tiap blok berdiri sendiri dan dipulihkan eksplisit (langkah 8, 23, 33, 42, 64).
- P-2: Admin kedua hanya memicu perubahan Custom Field lewat sesi API; hasil diasersi hanya di sesi admin pertama.
- Langkah 8, 23, 33, 42, dan 64 adalah langkah pemulihan tanpa `Verifikasi` (S-09); hook `after` adalah cadangan. Langkah 24 dan 33 adalah pemindahan Sub-Tab (penghubung, S-03).
- Judul TC-GS-IMPORT-963 menyebut "Create Missing Options" sebagai tombol yang tidak ada; langkah 50, 52, dan 57 mengasersi ketiadaannya (anchor positif: Error Summary Callout dan menu `⋯` tampil lebih dulu).
- Temuan untuk QA:
  - TC-GS-IMPORT-519 Expected c menyebut Number berisi `081234567`, sedangkan langkah 6 mengganti isi dengan `812345678`; tidak jelas mana nilai berkas dan mana nilai tampil (kemungkinan salah ketik; lihat Data Uji TC). Spec mengasersi `081234567` sesuai Expected dan mengetik `812345678` sesuai langkah.
  - TC-GS-IMPORT-934 dan 963 Langkah 3 menulis "lewat fixture permintaan" untuk Admin kedua; spec memakai sesi API Admin kedua (kemampuan disediakan tim FE/BE).
  - TC-GS-IMPORT-513, 519, 521 Data Uji menulis "Email unik"; spec memakai suffix per run.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
