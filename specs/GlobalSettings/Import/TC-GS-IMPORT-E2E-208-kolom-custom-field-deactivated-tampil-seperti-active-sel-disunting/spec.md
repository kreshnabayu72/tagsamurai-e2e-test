---
id: TC-GS-IMPORT-E2E-208-kolom-custom-field-deactivated-tampil-seperti-active-sel-disunting
title: "Kolom Custom Field Deactivated tampil seperti Active, sel disunting dengan Select, validasi Decimal Places, Append"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-950
  - TC-GS-IMPORT-951
  - TC-GS-IMPORT-960
coverage:
  web: automated
---

# Kolom Custom Field Deactivated tampil seperti Active, sel disunting dengan Select, validasi Decimal Places, Append

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec memutasi Custom Field Client A (state global) dan memulihkannya (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`.
- Pelaku kedua (pemicu via sesi API, bukan sesi UI): Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC2_PASSWORD` (nama env baru). Sesi API menonaktifkan Custom Field di Custom Field User; klien HTTP dan kontrak endpoint disediakan tim FE/BE (tidak tertulis di TC).
- Layar awal: hook `beforeEach` membuka Import > User Login Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true, lihat `suite.md`.
- Data Dinamis D-05: draft User Login 8 baris `pending` dari `user-login-8.csv` pada Client A (Shift `Siang` pada Row # 1 dan 2, `Pagi` pada Row # 3, kosong pada Row # 4 sampai 8; Overtime Hours `1.25` pada Row # 4), disiapkan lewat skrip seed dan dibuat ulang sebelum tiap TC (Kontrak Fixture R2).
- Nilai uji: Shift Row # 1 `Pagi` (TC-GS-IMPORT-950); Overtime Hours Row # 4 `1.255` lalu `2.25` (TC-GS-IMPORT-951). Berkas Append `shift-append.csv` (header First Name; Last Name; Email; Division; Access; Shift; 1 baris: Oka, Wibowo, `oka.wibowo+{runId}-208@example.com`, Engineering, Global Settings, `Malam`); Email diberi suffix per run (TC menulis tanpa suffix).
- Custom Field Client A (Pre-setup, Optional, Active): Shift (Dropdown Pagi/Siang/Malam), Overtime Hours (Numeric 2 desimal). Nama literal dipakai (pengecualian S-12 butir (ii): nama field menentukan teks Banner dan pesan error).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): `Shift` dan `Overtime Hours` diaktifkan kembali (Optional, Active), draft User Login Client A dipulihkan ke D-05. Pemulihan antar blok dilakukan sebagai langkah aksi.
- Kemampuan teknis: skrip seed D-05; sesi API Admin kedua; pemilihan berkas.
- State global: Custom Field Client A (dipulihkan), flag Guided Tooltip (dipulihkan hook suite `after`).

## Test Steps

### Kolom Deactivated tampil dan sel disunting dengan Select (TC-GS-IMPORT-950)

1. Admin kedua Client A (sesi API) menonaktifkan Custom Field `Shift` hingga tersimpan
2. Tekan `F5` pada halaman Import
3. Verifikasi header memuat kolom Shift setelah kolom atribut dan sebelum Status tanpa lencana
4. Verifikasi sel Shift Row # 1 menampilkan `Siang`
5. Verifikasi Banner Custom Field (severity warning) tampil dengan teks "Shift is deactivated. Its values stay hidden on users until it is activated."
6. Klik row action `⋯` pada Row # 1 lalu Edit
7. Verifikasi sel Shift Row # 1 menjadi Select pencarian dengan nilai terpilih `Siang` (bukan sel read-only)
8. Klik sel Shift Row # 1 dan pilih `Pagi` dari daftar
9. Klik `[Save]`
10. Verifikasi muncul toast sukses: "Success, row has been updated."
11. Verifikasi sel Shift Row # 1 menampilkan `Pagi`
12. Verifikasi Row # 1 berstatus `pending`
13. Verifikasi Staging Metric Cards: Total Rows 8, Ready to Import 8, Errors 0
14. Pulihkan: Admin kedua mengaktifkan kembali `Shift`, buat ulang draft D-05, muat ulang halaman

### Validasi Decimal Places pada Custom Field Deactivated (TC-GS-IMPORT-951)

15. Admin kedua Client A (sesi API) menonaktifkan Custom Field `Overtime Hours` hingga tersimpan
16. Tekan `F5` pada halaman Import
17. Verifikasi kolom Overtime Hours tampil tanpa lencana
18. Verifikasi sel Overtime Hours Row # 4 menampilkan `1.25`
19. Verifikasi Banner Custom Field (severity warning) tampil dengan teks "Overtime Hours is deactivated. Its values stay hidden on users until it is activated."
20. Klik row action `⋯` pada Row # 4 lalu Edit
21. Ubah sel Overtime Hours Row # 4 menjadi `1.255`
22. Klik `[Save]`
23. Verifikasi `[Save]` ditolak dan sesi edit tetap terbuka
24. Verifikasi sel Overtime Hours Row # 4 berborder `danger` dengan pesan `Overtime hours must have at most 2 decimal places`
25. Ubah sel Overtime Hours Row # 4 menjadi `2.25`
26. Klik `[Save]`
27. Verifikasi muncul toast sukses: "Success, row has been updated."
28. Verifikasi sel Overtime Hours Row # 4 menampilkan `2.25`
29. Pulihkan: Admin kedua mengaktifkan kembali `Overtime Hours`, buat ulang draft D-05, muat ulang halaman

### Append saat Custom Field Deactivated (TC-GS-IMPORT-960)

30. Admin kedua Client A (sesi API) menonaktifkan Custom Field `Shift` hingga tersimpan
31. Tekan `F5` pada halaman Import
32. Upload `shift-append.csv`
33. Klik `[Append Records]` pada Dialog Append to Draft
34. Klik `[Confirm Mapping]`
35. Verifikasi muncul toast sukses: "Success, row has been added."
36. Verifikasi Row # 9 berstatus `pending`
37. Verifikasi sel Shift Row # 9 kosong tanpa border `danger`
38. Verifikasi kolom Shift tetap tampil dengan nilai Row # 1 sampai 3
39. Verifikasi Banner Custom Field Deactivated tampil
40. Verifikasi Staging Metric Cards: Total Rows 9, Ready to Import 9, Errors 0
41. Pulihkan: Admin kedua mengaktifkan kembali `Shift`, buat ulang draft D-05

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Panjang spec: 41 langkah, di atas 35 langkah. Alasan: tiga blok berpola sama (nonaktifkan Custom Field lewat sesi API, F5, baca dan sunting Staging Table User Login) pada satu Sub-Tab dan satu dataset D-05; tiap blok berdiri sendiri dan dipulihkan eksplisit (langkah 14, 29, 41).
- P-2: Admin kedua hanya memicu penonaktifan Custom Field lewat sesi API; hasil diasersi hanya di sesi admin pertama.
- Langkah 14, 29, dan 41 adalah langkah pemulihan tanpa `Verifikasi` (S-09); hook `after` adalah cadangan.
- Langkah 21 sampai 24 menguji penolakan `[Save]` sebelum nilai valid pada langkah 25 (validasi diblokir sebelum aksi sukses, bagian 3 prinsip 3).
- Temuan untuk QA:
  - TC-GS-IMPORT-960 Expected b menyebut nilai `Malam` tidak dipetakan karena Shift tidak ditawarkan; spec mengasersi sel Shift Row # 9 kosong, tidak mengasersi alasan pemetaan.
  - TC-GS-IMPORT-960 Data Uji menulis Email tanpa suffix per run; spec memakai suffix per run.
  - TC tidak menyebut password per akun; tiap akun memakai env `<APP>_<ROLE>_PASSWORD` yang tercantum di Prerequisites (satu env hanya satu akun, S-11); env yang belum terdaftar didaftarkan di `spectra.config.ts` dan `.env.example` pada tahap script.
