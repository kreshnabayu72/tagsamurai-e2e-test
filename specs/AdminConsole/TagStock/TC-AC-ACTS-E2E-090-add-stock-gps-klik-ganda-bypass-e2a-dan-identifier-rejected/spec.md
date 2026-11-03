---
id: TC-AC-ACTS-E2E-090-add-stock-gps-klik-ganda-bypass-e2a-dan-identifier-rejected
title: "Add Stock GPS: Klik Ganda Submit, Bypass E2a oleh Total Control, dan IMEI Hanya Dipegang Unit Rejected"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-266
  - TC-AC-ACTS-734
  - TC-AC-ACTS-741
coverage:
  web: automated
---

# Add Stock GPS: Klik Ganda Submit, Bypass E2a oleh Total Control, dan IMEI Hanya Dipegang Unit Rejected

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Akun ganti di tengah spec: Distributor Toggle ON (Local Registration aktif; jalur approval normal tanpa bypass E2a) `distributorOn_automated_{namaCompany}@qwertysystem.net` (Pre-setup #9), password dari `Spectra.env.AC_DIST_ON_PASSWORD`. Pergantian akun ditulis sebagai langkah eksplisit.
- Halaman awal: halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Import/Manual IMEI), dibuka dari Stock List lewat row action Add Stock pada SKU itu oleh hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- SKU `GPS-TRACK-CORE-G3` (Data Pre-setup #15). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script; nilai identifier ditulis literal seperti di TC dan dipetakan ke kunci fixture di tahap script.
- IMEI Data Dinamis #2 dan #4 bersifat tetap dan tidak dapat bersuffix `{runId}`; seeding idempotent dan pemulihan lewat fixture BE sebelum spec ini. IMEI `356938035643810` terdaftar sebagai unit existing berstatus Available; IMEI `356938035643811` hanya dipegang unit Rejected (Data Dinamis #4); keduanya dipakai sebagai precondition TC, tidak diasersi. Unit yang didaftarkan spec ini (`356938035643809`, `356938035643812`, `356938035643810` sebagai unit baru, `356938035643811`) dihapus lewat fixture BE di hook `after`.
- Kemampuan teknis disediakan tim FE/BE: kemampuan baca jumlah baris Event Log SKU, jumlah unit Available SKU, dan jumlah Subject Tab Active (baseline, S-12).
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`, `Spectra.env.AC_DIST_ON_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `AC_DIST_ON_PASSWORD` adalah nama baru yang didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-266: Klik ganda [Submit] GPS hanya memproses satu request

1. Catat baseline jumlah baris Event Log SKU
2. Tambahkan IMEI `356938035643809` dan `356938035643812` lewat Manual Entry (dua baris OK; dipakai sebagai precondition TC, tidak diasersi)
3. Klik `[Submit]` dua kali cepat
4. Verifikasi `[Submit]` disabled dengan loading setelah klik pertama
5. Verifikasi satu batch terdaftar (jumlah baris Event Log SKU bertambah tepat 1 terhadap baseline)

### TC-AC-ACTS-734: Bypass E2a pada Import/Manual GPS, requester Total Control Principal tidak membuat Subject

6. Buka kembali halaman Add Stock SKU `GPS-TRACK-CORE-G3` (Stock List, row action Add Stock)
7. Catat baseline jumlah unit Available SKU dan jumlah Subject di Approvals > TAG Stock > Tab Active
8. Ketik `356938035643810` di input Manual Entry IMEI, klik `[+ Add]`
9. Verifikasi baris Preview berstatus OK
10. Hover badge OK pada baris itu
11. Verifikasi tooltip match tidak tampil
12. Klik `[Submit]`
13. Verifikasi toast "Success, TAG has been registered."
14. Verifikasi tidak ada dialog `Partial Register`
15. Verifikasi toast "Success, 1 TAG has been sent for approval." (T-04) tidak tampil
16. Verifikasi unit baru berstatus Available dengan TAG Code baru (jumlah unit Available SKU bertambah 1 terhadap baseline)
17. Buka Approvals > TAG Stock > Tab Active
18. Verifikasi tidak ada Subject baru di Tab Active (jumlah Subject tidak berubah terhadap baseline)

### TC-AC-ACTS-741: IMEI yang hanya dipegang unit Rejected menjadi baris OK, IMEI milik unit live tetap Waiting

19. Ganti akun: klik Logout
20. Login sebagai Distributor Toggle ON (`distributorOn_automated_{namaCompany}@qwertysystem.net`)
21. Buka halaman Add Stock SKU `GPS-TRACK-CORE-G3` dari Stock List lewat row action Add Stock
22. Catat baseline jumlah Subject pending (kemampuan baca, Distributor tidak punya menu Approvals)
23. Ketik `356938035643811` di input Manual Entry IMEI, klik `[+ Add]`
24. Ketik `356938035643810` di input Manual Entry IMEI, klik `[+ Add]`
25. Verifikasi baris IMEI `356938035643811` berstatus OK (success)
26. Hover badge OK pada baris `356938035643811`
27. Verifikasi tooltip match tidak tampil
28. Verifikasi baris IMEI `356938035643810` berstatus Waiting for Approval (warning)
29. Verifikasi Ringkasan `1 valid, 1 waiting approval, 0 duplicate, 0 invalid of 2 entries`
30. Klik `[Submit]`, lalu klik `[Continue]` pada dialog `Partial Register`
31. Tunggu aksi selesai (dialog `Partial Register` tertutup)
32. Ganti akun: klik Logout
33. Login sebagai Total Control (`totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`)
34. Buka Detail SKU `GPS-TRACK-CORE-G3` > Tab Available, ketik Search `356938035643811`, tekan Enter
35. Verifikasi IMEI `356938035643811` terdaftar sebagai unit baru Available dengan TAG Code baru
36. Buka Approvals > TAG Stock > Tab Active
37. Verifikasi jumlah Subject baru di Tab Active bertambah tepat 1 terhadap baseline, untuk IMEI `356938035643810` dengan Existing Record unit Available
38. Verifikasi tidak ada Subject untuk IMEI `356938035643811`

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (38 langkah); alasan: semua blok satu kelas harness (kelas f, mekanisme impor) dan satu dataset, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; 8 langkah adalah penggantian akun dua kali yang dituntut TC-AC-ACTS-741 (Distributor memicu, Total Control membaca Approvals).
- Urutan TC: TC-AC-ACTS-266 dan TC-AC-ACTS-734 (Total Control) lebih dulu, TC-AC-ACTS-741 terakhir dengan dua kali ganti akun di langkah 19 dan 32 (S-07, S-10).
- Langkah penghubung tanpa Verifikasi (S-03): langkah mencatat baseline (S-12), buka kembali halaman Add Stock, langkah ganti akun, dan "Tunggu aksi selesai" sebelum Logout (langkah 31, bagian 8b butir 8). Asersi hanya Total Control bypass E2a pada TC-AC-ACTS-734 (langkah 12) tidak menghasilkan Subject; Distributor memakai jalur approval normal pada TC-AC-ACTS-741.
- Absence tooltip match dan toast T-04 didahului anchor positif (baris OK tampil, toast sukses tampil; 8b butir 2).
- Temuan untuk QA:
  - TC-AC-ACTS-266 tidak menyebut cara mengamati "satu batch terdaftar"; spec memakai selisih jumlah baris Event Log SKU terhadap baseline.
  - TC-AC-ACTS-741 menyebut klik `[Continue]` tanpa Expected untuk teks dialog; spec tidak mengasersi teks dialog itu.
