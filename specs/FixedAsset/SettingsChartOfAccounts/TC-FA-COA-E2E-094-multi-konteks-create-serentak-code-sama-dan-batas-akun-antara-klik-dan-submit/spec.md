---
id: TC-FA-COA-E2E-094-multi-konteks-create-serentak-code-sama-dan-batas-akun-antara-klik-dan-submit
title: "Multi-Konteks: Create Serentak Dua Sesi dengan Account Code Sama dan Batas Jumlah Akun Tercapai antara Klik dan Submit"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-COA-281
  - TC-FA-COA-160
coverage:
  web: automated
---

# Multi-Konteks: Create Serentak Dua Sesi dengan Account Code Sama dan Batas Jumlah Akun Tercapai antara Klik dan Submit

## Prerequisites

- Mode: FE+BE (backend nyata; tanpa intercept).
- Akun aktor sesi A: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun sesi B pada TC-FA-COA-281 (konteks browser kedua yang hasilnya diasersi): Default User `defaultUserFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_DU_PASSWORD` (terdaftar di `spectra.config.ts` dan `.env.example`). Default User adalah Total Control permanen (asumsi Pre-setup TC, lihat Temuan untuk QA). Login sesi B ditulis sebagai langkah eksplisit (S-07).
- Sesi API aktor: pelaku kedua pada TC-FA-COA-160 (membuat akun hingga jumlah 1000) memakai sesi API sesuai butir "Sesi API aktor" di `suite.md`.
- Seed dan pemulihan lewat API: mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`.
- Flag Guided Tooltip halaman Chart of Accounts: di-set true oleh hook `before` suite (lihat `suite.md`), termasuk untuk akun Total Control pada client P25.
- Data Pre-setup dan client:
  - TC-FA-COA-281: client default suite; tanpa akun Pre-setup.
  - TC-FA-COA-160: client uji race batas akun P25 (plan Growth, Master Data Count Limit 1000, 999 akun disiapkan lewat seed atau API; disediakan tim FE). Login Total Control pada client P25 memakai email `totalControlFixedAsset_automated_{namaCompany P25}@qwertysystem.net` (email tidak tertulis di Pre-setup TC; lihat Temuan untuk QA) dengan `Spectra.env.FA_TC_PASSWORD`. Kuota Master Data Count Limit menjadi pemicu state pada spec multi-konteks, bukan objek uji kelas e.
- Data Dinamis (Code literal karena Account Code maksimal 15 karakter tidak memuat suffix `{runId}`; Name memuat suffix; dibersihkan di hook `before` dan `after` lewat API, R-13):
  - TC-FA-COA-281: Code `CAP-8400` (D9), Name sesi A `Race Code A {runId}-094`, Name sesi B `Race Code B {runId}-094`, Function Capitalization Offset. Hanya satu dari dua akun yang tersimpan; akun itu dihapus langkah 14.
  - TC-FA-COA-160: Code `CAP-7000`, Name `Capitalization Clearing – Race {runId}-094`, Function Capitalization Offset (tidak tersimpan); akun pengisi slot terakhir Code `CAP-7001`, Name `Race Filler {runId}-094`, Function Capitalization Offset (dibuat sesi API, dihapus langkah 35).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): membuat dan menghapus akun lewat sesi API; membersihkan akun `CAP-8400`, `CAP-7000`, dan `CAP-7001` di hook `before` dan `after`; memulihkan hitungan 999 akun pada client P25.
- Suite berjalan serial (`parallel: false`): spec memakai satu slot terakhir Master Data Count Limit pada client P25 dan Account Code literal.
- Env var yang dipakai: `FA_TC_PASSWORD` (terdaftar), `FA_DU_PASSWORD` (terdaftar).

## Test Steps

### TC-FA-COA-281: Dua admin membuat Account Code yang sama hampir bersamaan: yang kedua ditolak

1. Ganti akun: buka konteks browser kedua (sesi B), login sebagai Default User `defaultUserFixedAsset_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.FA_DU_PASSWORD`, lalu buka Fixed Asset > Settings > Accounting > Chart of Accounts
2. Sesi A dan sesi B masing-masing klik `+ Account`
3. Sesi A: isi Account Code `CAP-8400`, Account Name `Race Code A {runId}-094`, Account Function Capitalization Offset; sesi B: isi Account Code `CAP-8400`, Account Name `Race Code B {runId}-094`, Account Function Capitalization Offset
4. Klik `[Submit]` di sesi A lalu segera di sesi B (hampir bersamaan)
5. Verifikasi tepat satu sesi (sesi pemenang) menampilkan toast "Success, account has been created."
6. Verifikasi sesi lainnya (sesi kalah) menampilkan penolakan "Account code already exists"
7. Sesi kalah: klik `✕` pada modal Add Account
8. Verifikasi dialog `Unsaved Changes` tampil di sesi kalah
9. Klik `[Leave]` di sesi kalah
10. Sesi A: ketik Search `CAP-8400`, tekan Enter
11. Verifikasi hanya satu baris Account Code `CAP-8400` ada di tabel
12. Verifikasi baris `CAP-8400` itu bernama Account Name milik sesi pemenang, bukan milik sesi kalah (sesi kalah tidak membuat akun)
13. Klik `(←)` pada kotak Search di sesi A
14. Hapus akun `CAP-8400` lewat sesi API hingga penghapusan tersimpan
15. Tutup konteks browser sesi B dan hapus sesi login browser sesi B

### TC-FA-COA-160: Batas jumlah akun tercapai antara klik `+ Account` dan Submit: Submit ditolak dengan dialog blok D-13 dan form tetap terbuka

16. Ganti akun: sesi A logout, lalu login sebagai Total Control pada client P25 dengan `Spectra.env.FA_TC_PASSWORD`, lalu buka Fixed Asset > Settings > Accounting > Chart of Accounts
17. Sesi A: klik `+ Account`
18. Verifikasi modal Add Account terbuka
19. Sesi A: isi Account Code `CAP-7000`, Account Name `Capitalization Clearing – Race {runId}-094`, Account Function Capitalization Offset
20. Buat satu akun (Code `CAP-7001`, Name `Race Filler {runId}-094`, Function Capitalization Offset) pada client P25 lewat sesi API hingga jumlah akun menjadi 1000 tersimpan
21. Sesi A: klik `[Submit]`
22. Verifikasi dialog `Cannot Add Account` dengan teks "You've reached the platform limit of 1000 records. Contact support if you need a higher limit." tampil
23. Verifikasi tidak ada toast tambahan
24. Klik `[OK]`
25. Verifikasi modal Add Account tetap terbuka
26. Verifikasi Account Code tetap terisi `CAP-7000`
27. Verifikasi Account Name tetap terisi `Capitalization Clearing – Race {runId}-094`
28. Verifikasi Account Function tetap terisi Capitalization Offset
29. Klik `✕` pada modal Add Account
30. Verifikasi dialog `Unsaved Changes` tampil
31. Klik `[Leave]`
32. Ketik Search `CAP-7000`, tekan Enter
33. Verifikasi empty state `No results found` tampil (akun `CAP-7000` tidak dibuat)
34. Klik `(←)` pada kotak Search
35. Hapus akun `CAP-7001` lewat sesi API hingga hitungan akun kembali 999 tersimpan

## Notes

- Mode: FE+BE (kelas c, multi-konteks). Dua blok berdiri sendiri dan satu kelas harness (konflik dua sesi dan perubahan state antara dialog dan Submit); jumlah langkah 35.
- Pelaku kedua pada TC-FA-COA-160 adalah sesi API yang hanya memicu perubahan state; sesi UI kedua dipakai hanya pada TC-FA-COA-281 karena penolakan di sesi B ikut diasersi.
- Langkah penghubung (S-03, S-09): langkah 10 dan 32 (Search untuk menemukan akun target, R-16, butir 8b.13) serta 13 dan 34 (mengosongkan Search); langkah 7, 8, 9, 29, 30, 31 (menutup form dirty dengan `✕`, `Unsaved Changes`, `[Leave]`, S-08); langkah 14 dan 35 (membersihkan akun yang dibuat dan memulihkan hitungan slot); langkah 15 (menutup konteks kedua); langkah 1 dan 16 (ganti akun eksplisit, S-07).
- Pemenang tidak dapat ditentukan sebelumnya (nondeterministik); langkah 5 sampai 12 memakai istilah "sesi pemenang" (sesi yang menerima toast sukses) dan "sesi kalah" (sesi A atau B), idiom race tak deterministik butir 8b.15 yang dipakai TC-FA-COA-281. Pencarian pada langkah 10 selalu di sesi A, sesudah form sesi kalah dipulihkan pada langkah 7 sampai 9.
- Asersi absence: "tidak ada toast tambahan" (langkah 23) didahului dialog sebagai anchor positif (butir 8b.2 dan 8b.11); "akun `CAP-7000` tidak dibuat" (langkah 33) memakai empty state `No results found` hasil Search sebagai anchor. Post Condition "tidak ada log L-01 untuk `CAP-7000`" (TC-FA-COA-160) dan "satu entri L-01 per surface" (TC-FA-COA-281) tidak punya langkah observasi di TC sehingga tidak diasersi.
- Temuan untuk QA:
  - TC-FA-COA-281 menulis "Account Name dan Account Function valid" tanpa nilai; spec memilih Name berbeda per sesi (`Race Code A/B {runId}-094`) agar penolakan hanya berasal dari Account Code dan Function Capitalization Offset.
  - TC-FA-COA-281 Expected b ("penolakan 'Account code already exists'") tidak menyatakan bentuk penolakan (error inline atau toast); spec mengasersi teksnya tanpa menyebut bentuknya. TC juga tidak menyatakan keadaan form sesi kalah sesudah penolakan; spec memulihkannya dengan `✕`, `Unsaved Changes`, `[Leave]`.
  - TC-FA-COA-281 menyebut "tepat satu sesi berhasil" tanpa menentukan pemenang; spec tidak mengasumsikan pemenang. Sesi B memakai Default User sebagai asumsi: dua sesi web Total Control yang sama dapat terkena batas satu sesi web dan TC tidak menyatakan perilakunya (Default User adalah asumsi Pre-setup TC).
  - TC-FA-COA-160 langkah 3 ("buat satu akun sehingga jumlah akun menjadi 1000") tidak menyebut data akun pengisi; spec memakai Code `CAP-7001` dan Name `Race Filler {runId}-094` (pilihan spec). Email Total Control untuk client P25 tidak tertulis di Pre-setup TC; spec memakai pola email dengan `{namaCompany P25}` yang perlu dikonfirmasi tim FE.
  - TC-FA-COA-160 Expected a menulis "karena jumlah akun masih 999" sebagai alasan; spec hanya mengasersi modal terbuka. Expected d dipecah per field (S-01).
  - TC-FA-COA-160 Expected b menulis teks dialog dengan `[Limit]`; spec mengasersi dengan nilai 1000 dari Data Uji TC.
  - TC-FA-COA-160 dan 281 tidak menyebut kolom yang dicari Search; spec mencari berdasarkan Account Code.
