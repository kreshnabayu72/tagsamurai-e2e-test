---
id: TC-AC-ACTS-E2E-091-add-stock-gps-volume-5000-baris-sinkron-dan-background
title: "Add Stock GPS Volume: Tepat 5.000 Baris Sinkron, Lebih dari 5.000 Baris di Background (Toast T-23 dan Notifikasi), Campuran Partial Register, dan Tanpa Baris OK"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-269
  - TC-AC-ACTS-270
  - TC-AC-ACTS-769
  - TC-AC-ACTS-770
coverage:
  web: automated
---

# Add Stock GPS Volume: Tepat 5.000 Baris Sinkron, Lebih dari 5.000 Baris di Background (Toast T-23 dan Notifikasi), Campuran Partial Register, dan Tanpa Baris OK

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun ganti di tengah spec: Distributor Toggle ON (Local Registration aktif; jalur approval normal tanpa bypass E2a) `distributorOn_automated_{namaCompany}@qwertysystem.net` (Pre-setup #9), password dari `Spectra.env.AC_DIST_ON_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Halaman awal: halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Import/Manual IMEI), dibuka dari Stock List lewat row action Add Stock pada SKU itu oleh hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- SKU `GPS-TRACK-CORE-G3` (Data Pre-setup #15). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script. IMEI `356938035643810` terdaftar sebagai unit existing berstatus Available (dipakai sebagai precondition TC-AC-ACTS-769, tidak diasersi).
- Kelas harness e (volume 5.000 dan 5.001 baris). Berkas CSV berisi 5.000 dan 5.001 IMEI valid baru, serta 5.001 baris Invalid Format, dibuat oleh pembuat berkas dengan IMEI yang belum terdaftar (disediakan tim FE; IMEI massal tidak mengikuti rentang Data Dinamis #2).
- Kemampuan teknis disediakan tim FE/BE: kemampuan baca jumlah unit Available SKU dan status job background; unit yang didaftarkan spec ini (5.000 + 5.001 + 5.000 unit baru) dihapus lewat fixture BE di hook `before` dan `after`.
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`, `Spectra.env.AC_DIST_ON_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `AC_DIST_ON_PASSWORD` adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-269: Import GPS tepat 5.000 baris diproses sinkron

1. Unggah file CSV berisi 5.000 IMEI valid baru
2. Klik `[Submit]`
3. Verifikasi diproses sinkron dengan spinner biasa
4. Verifikasi toast "Preparing your import. We'll notify you when it's ready." tidak tampil

### TC-AC-ACTS-270: Import GPS lebih dari 5.000 baris berjalan di background dengan toast T-23 dan notifikasi progres

5. Buka kembali halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Stock List, row action Add Stock)
6. Catat baseline jumlah unit Available SKU
7. Unggah file CSV berisi 5.001 IMEI valid baru
8. Klik `[Submit]`
9. Verifikasi Preview tetap tampil
10. Verifikasi request langsung kembali dengan toast "Preparing your import. We'll notify you when it's ready."
11. Verifikasi tidak ada dialog `Partial Register`
12. Verifikasi toast "Success, TAG has been registered." dan toast "Success, [N] TAGs have been sent for approval." tidak tampil
13. Klik `[Cancel]`
14. Verifikasi dialog Unsaved Changes tampil
15. Klik `[Leave]` (pindah ke halaman lain)
16. Buka Notification Center
17. Verifikasi notifikasi saat berjalan dengan Title `Importing GPS...` dan Body `[N] of [Total] records processed.` (angka bertambah)
18. Muat ulang halaman setiap 5 detik sampai notifikasi `Import GPS completed` tampil (batas tunggu 2 menit)
19. Verifikasi notifikasi saat selesai dengan Title `Import GPS completed` dan Body `5001 valid, 0 waiting approval, 0 duplicate, 0 invalid of 5001 entries`
20. Verifikasi 5.001 unit baru terdaftar dengan TAG Code baru (jumlah unit Available SKU bertambah 5.001 terhadap baseline)

### TC-AC-ACTS-770: Import GPS lebih dari 5.000 baris tanpa baris OK maupun Waiting, V-07 dari Preview tanpa toast T-23

21. Buka kembali halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Stock List, row action Add Stock)
22. Catat baseline jumlah unit Available SKU
23. Unggah file CSV berisi 5.001 baris Invalid Format
24. Klik `[Submit]`
25. Verifikasi pesan "No TAGs to register. Add at least one IMEI."
26. Verifikasi toast "Preparing your import. We'll notify you when it's ready." tidak tampil
27. Verifikasi tidak ada job background dan tidak ada unit tersimpan (status job tidak ada, jumlah unit Available SKU tidak berubah terhadap baseline)
28. Klik `[Cancel]`
29. Verifikasi dialog Unsaved Changes tampil
30. Klik `[Leave]`

### TC-AC-ACTS-769: Import GPS lebih dari 5.000 baris campuran OK dan Waiting, Partial Register dari badge Preview lalu toast T-23

31. Ganti akun: klik Logout
32. Login sebagai Distributor Toggle ON (`distributorOn_automated_{namaCompany}@qwertysystem.net`)
33. Buka halaman Add Stock SKU `GPS-TRACK-CORE-G3` dari Stock List lewat row action Add Stock
34. Unggah file CSV berisi 5.001 IMEI: 5.000 IMEI baru valid dan IMEI `356938035643810`
35. Verifikasi Ringkasan `5000 valid, 1 waiting approval, 0 duplicate, 0 invalid of 5001 entries`
36. Klik `[Submit]`
37. Verifikasi dialog `Partial Register` tampil sebelum request dikirim: "1 IMEI matched an existing record and will be sent for approval. Register the remaining 5000 IMEIs?"
38. Klik `[Continue]`
39. Verifikasi request langsung kembali dengan toast "Preparing your import. We'll notify you when it's ready."
40. Verifikasi toast "Success, TAG has been registered." dan toast "Success, [N] TAGs have been sent for approval." tidak tampil
41. Klik `[Cancel]`
42. Verifikasi dialog Unsaved Changes tampil
43. Klik `[Leave]`

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (43 langkah); alasan: semua blok satu kelas harness (kelas e, volume 5.000 dan 5.001 baris) dan satu dataset berkas, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC: TC-AC-ACTS-269, TC-AC-ACTS-270, dan TC-AC-ACTS-770 (Total Control) lebih dulu, lalu satu kali ganti akun ke Distributor Toggle ON untuk TC-AC-ACTS-769 (S-07, S-10).
- Langkah penghubung tanpa Verifikasi (S-03): buka kembali halaman Add Stock, mencatat baseline (S-12), `[Cancel]` lalu `[Leave]` untuk menutup Preview yang tetap tampil setelah Submit atau V-07 (S-08), dan langkah ganti akun. Muat ulang tiap 5 detik sampai notifikasi tampil memakai idiom baku "polling worker commit" (bagian 6 konvensi, batas tunggu 2 menit).
- Absence toast T-23 pada TC-AC-ACTS-770 didahului pesan V-07 sebagai anchor positif; absence toast `Preparing your import` pada TC-AC-ACTS-269 didahului spinner sebagai anchor positif (8b butir 2 dan 11).
- Temuan untuk QA:
  - TC-AC-ACTS-270 menyebut "Pindah ke halaman lain" tanpa menyebut apakah dialog Unsaved Changes tampil saat Preview tetap tampil setelah Submit; spec menutup halaman lewat `[Cancel]` dan `[Leave]` secara deterministik (S-08).
  - TC-AC-ACTS-269 tidak menyebut hasil akhir (toast atau navigasi) setelah Submit sinkron; spec hanya mengasersi spinner dan absence toast.
  - Cara membuat 5.000 dan 5.001 IMEI valid baru tidak didefinisikan di TC, PRD, atau LLD (disediakan tim FE).
