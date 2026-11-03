---
id: TC-AC-ACTS-E2E-086-add-stock-gps-match-existing-ringkasan-manual-entry-dan-invalid-berulang
title: "Add Stock GPS: IMEI Cocok Unit Existing (Waiting), Ringkasan A/B/C/D, Manual Entry Satu IMEI, Placeholder, Bentuk Tunggal, dan Invalid Format Berulang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-250
  - TC-AC-ACTS-268
  - TC-AC-ACTS-272
  - TC-AC-ACTS-748
  - TC-AC-ACTS-749
  - TC-AC-ACTS-783
coverage:
  web: automated
---

# Add Stock GPS: IMEI Cocok Unit Existing (Waiting), Ringkasan A/B/C/D, Manual Entry Satu IMEI, Placeholder, Bentuk Tunggal, dan Invalid Format Berulang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Toggle ON (Local Registration aktif; jalur approval normal tanpa bypass E2a) `distributorOn_automated_{namaCompany}@qwertysystem.net` (Pre-setup #9), password dari `Spectra.env.AC_DIST_ON_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun ganti di tengah spec: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Halaman awal: halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Import/Manual IMEI), dibuka dari Stock List lewat row action Add Stock pada SKU itu oleh hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- SKU `GPS-TRACK-CORE-G3` (Data Pre-setup #15). Fixture `fixtures/tag-stock.json` belum ada (disediakan tim FE/BE); nilai identifier ditulis literal seperti di TC.
- IMEI Data Dinamis #2 (`356938035643809` sampai `356938035643817`) bersifat tetap dan tidak dapat bersuffix `{runId}`; seeding idempotent dan pemulihan lewat fixture BE sebelum spec ini. IMEI `356938035643810` terdaftar sebagai unit existing berstatus Available (dipakai sebagai precondition TC, tidak diasersi). Spec ini tidak menekan `[Submit]`, sehingga tidak ada unit yang perlu dihapus.
- Env var password akun aktor: `Spectra.env.AC_DIST_ON_PASSWORD`, `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `AC_DIST_ON_PASSWORD` adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-250: IMEI cocok unit existing menjadi Waiting for Approval per baris

1. Tambahkan IMEI baru `356938035643809` lewat Manual Entry (baris pembanding)
2. Tambahkan IMEI `356938035643810` (existing) lewat Manual Entry
3. Verifikasi baris `356938035643810` berstatus Waiting for Approval (warning)
4. Verifikasi baris `356938035643809` tetap berstatus OK (baris Waiting tidak memblokir baris lain)
5. Hover badge Waiting for Approval pada baris `356938035643810`
6. Verifikasi tooltip "TAG 356938035643810 matches an existing registered TAG. It will be sent for approval."
7. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

### TC-AC-ACTS-268: Ringkasan Preview memakai legenda A/B/C/D dan total N

8. Tambahkan IMEI baru `356938035643809` dan `356938035643811` (dua OK), IMEI existing `356938035643810` (satu Waiting), `356938035643809` sekali lagi (satu Duplicate), serta `12345` dan `1234` (dua Invalid)
9. Verifikasi Ringkasan `2 valid, 1 waiting approval, 1 duplicate, 2 invalid of 6 entries`
10. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

### TC-AC-ACTS-272: Manual Entry satu IMEI per entri; Add pada input kosong menjadi Invalid Format

11. Ganti akun: klik Logout
12. Login sebagai Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`)
13. Buka halaman Add Stock SKU `GPS-TRACK-CORE-G3` dari Stock List lewat row action Add Stock
14. Klik `[+ Add]` pada input IMEI kosong
15. Verifikasi satu baris Preview berstatus Invalid Format (IMEI kosong)
16. Tempel teks berisi tiga IMEI dipisah baris baru ke input IMEI (`356938035643809`, `356938035643811`, `356938035643812`)
17. Verifikasi input IMEI hanya satu baris (tidak multi-baris)
18. Klik `[+ Add]` satu kali
19. Verifikasi satu klik `[+ Add]` menambah tepat satu baris Preview (total 2 baris), bukan tiga
20. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

### TC-AC-ACTS-748: Placeholder dan helper text baku input Manual Entry IMEI

21. Amati input Manual Entry IMEI saat kosong
22. Verifikasi label `IMEI`
23. Verifikasi placeholder `Enter IMEI` tampil saat input kosong
24. Verifikasi helper text `Digits only, exactly 15 digits.` tampil di bawah input
25. Verifikasi default state input adalah placeholder
26. Ketik `3569380` di input IMEI
27. Verifikasi placeholder `Enter IMEI` hilang saat mengetik
28. Verifikasi helper text `Digits only, exactly 15 digits.` tetap tampil
29. Kosongkan isi input IMEI

### TC-AC-ACTS-749: Ringkasan Preview memakai bentuk tunggal untuk satu entri

30. Tambahkan satu IMEI valid baru `356938035643813` lewat Manual Entry
31. Verifikasi Ringkasan `1 valid, 0 waiting approval, 0 duplicate, 0 invalid of 1 entry`
32. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

### TC-AC-ACTS-783: IMEI kosong atau tidak valid yang berulang tetap Invalid Format pada tiap kemunculan

33. Ketik `12345` di input IMEI, klik `[+ Add]`; ketik `12345` lagi, klik `[+ Add]`
34. Kosongkan input IMEI, klik `[+ Add]`; kosongkan input lagi, klik `[+ Add]`
35. Ketik IMEI valid baru `356938035643816`, klik `[+ Add]`; ketik `356938035643816` lagi, klik `[+ Add]`
36. Verifikasi kedua baris `12345` berstatus Invalid Format (bukan Duplicate in File/List)
37. Verifikasi kedua baris kosong berstatus Invalid Format
38. Verifikasi kemunculan pertama IMEI valid berstatus OK
39. Verifikasi kemunculan kedua IMEI valid berstatus Duplicate in File/List
40. Verifikasi Ringkasan `1 valid, 0 waiting approval, 1 duplicate, 4 invalid of 6 entries`
41. Hapus seluruh baris Preview lewat ikon hapus pada tiap baris

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (41 langkah); alasan: semua blok satu kelas harness (kelas f, mekanisme impor Preview) dan satu dataset, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC: TC-AC-ACTS-250 dan TC-AC-ACTS-268 (Distributor Toggle ON, hook `before`) lebih dulu, lalu satu kali ganti akun ke Total Control di langkah 11 untuk TC-AC-ACTS-272, TC-AC-ACTS-748, TC-AC-ACTS-749, dan TC-AC-ACTS-783 (S-07, S-10).
- Langkah penghubung tanpa Verifikasi (S-03): "Hapus seluruh baris Preview lewat ikon hapus pada tiap baris" sesudah tiap TC (S-09), langkah mengosongkan input IMEI pada TC-AC-ACTS-748, serta langkah ganti akun dan buka halaman Add Stock.
- Tooltip TC-AC-ACTS-250 menuliskan `[Identifier]` sebagai nilai IMEI baris itu.
- Temuan untuk QA:
  - TC-AC-ACTS-250 menyebut Waiting "tanpa memblokir baris lain" tetapi Langkah TC hanya menambah satu IMEI; spec menambah satu IMEI baru sebagai baris pembanding.
  - TC-AC-ACTS-268 menyebut data "2+1+1+2" tanpa nilai; spec memakai nilai dari rentang Data Dinamis #2 dan nilai invalid `12345` dan `1234`.
  - TC-AC-ACTS-783 mengamati status baris dan Ringkasan hanya sesudah semua penambahan (Langkah 4 TC); spec menambahkan tiap pasangan entri sesuai Langkah 1 sampai 3 TC dan memverifikasi per kelompok baris sesudahnya. TC tidak menyebut apakah Preview sudah kosong sebelum langkah 1; spec mengosongkannya di langkah 32 (sesudah TC-AC-ACTS-749).
  - TC-AC-ACTS-272 menyebut paste "tiga IMEI dipisah baris baru" tanpa nilai; spec memakai tiga IMEI dari rentang Data Dinamis #2.
