---
id: TC-FA-COA-E2E-079-state-tenant-suspended-expired-dan-plan-starter
title: "State Tenant: Client Suspended atau Expired Menolak Aksi Tulis dan Plan Starter Menonaktifkan Menu Accounting"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-COA-112
  - TC-FA-COA-113
  - TC-FA-COA-277
  - TC-FA-COA-278
  - TC-FA-COA-279
  - TC-FA-COA-280
  - TC-FA-COA-142
coverage:
  web: automated
---

# State Tenant: Client Suspended atau Expired Menolak Aksi Tulis dan Plan Starter Menonaktifkan Menu Accounting

## Prerequisites

- Mode: FE+BE.
- Kelas harness h (state tenant: write-lockdown Client Suspended atau Expired dan plan Starter). Permintaan langsung ke server dipakai sebagai cara memverifikasi lockdown, bukan sebagai objek kelas a.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah status client atau plan, hanya memakai client yang sudah berstatus demikian.
- Akun login hook `before` spec ini: Total Control `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` pada client Suspended (`Fixture.settingsChartOfAccounts.clientSuspended`), password dari `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite. Satu ganti akun eksplisit pada langkah 33 ke Total Control client plan Starter (`Fixture.settingsChartOfAccounts.clientStarter`). Hook `after` mengembalikan sesi ke akun default suite.
- Env var `FA_TC_PASSWORD` sudah terdaftar. Kecocokan akun Total Control pada kedua client uji perlu dikonfirmasi tim FE.
- Data client (disediakan tim FE, lihat Temuan untuk QA):
  - Client Suspended: dua akun milik spec yang di-seed hook `before` lewat kemampuan seed backend (tidak melewati lockdown aksi tulis tenant; disediakan tim FE/BE, lihat Temuan untuk QA) dan dihapus hook `before` dan `after`: akun A Code `DID079A`, Account Name `Akun Suspended A {runId}-079`, Function Depreciation Expense, Active, Used By 0 (padanan P1); akun B Code `DID079B`, Account Name `Akun Suspended B {runId}-079`, Function Gain on Disposal, Inactive, Used By 0 (padanan P3). Semua permintaan tulis ditolak, tidak ada data yang berubah.
  - Client plan Starter: client berplan Starter dengan akun Total Control.
- Data Dinamis (tidak pernah tersimpan karena ditolak): Create memakai Code `SUSP-079` (literal, maksimal 15 karakter sehingga tidak diberi suffix `{runId}`; memuat nomor spec supaya unik per spec, seperti `DID079A` dan `DID079B`), Name `Suspended Create {runId}-079`, Function Depreciation Expense; Edit memakai Name `Suspended Edit {runId}-079`. Hook `before` dan `after` memastikan akun Code `SUSP-079` tidak ada pada client Suspended (pembersihan idempotent).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): sesi API aktor Total Control untuk permintaan langsung (butir "Sesi API aktor" di `suite.md`); klien HTTP; kemampuan membaca dari server daftar akun beserta Account Name, Status, dan jumlah akun per client; pengamatan berkas unduhan CSV pada browser (disediakan tim FE).
- Seed dan pemulihan client lewat API mengikuti butir "Seed dan pemulihan lewat API" di `suite.md`; flag Guided Tooltip mengikuti hook suite. Pengecualian layar awal: langkah 33 sampai 40 tidak memakai halaman Chart of Accounts karena menu Accounting pada client Starter tidak dapat dibuka.
- Pengecualian A-18 (butir "Data bersama" di `suite.md`): Account Code literal `DID079A`, `DID079B`, dan `SUSP-079` dipakai spec ini saja tanpa suffix `{runId}` (batas 15 karakter); seed idempotent dan pemulihan dijalankan di hook `before` dan `after` spec ini (disediakan tim FE/BE); suite berjalan serial.

## Test Steps

### TC-FA-COA-112: Client Suspended menolak aksi tulis

1. Catat jumlah akun client Suspended dari server (baseline)
2. Klik `+ Account`
3. Verifikasi Toast T-11 tampil sesuai copy baku `entity_isolation()` §18.8
4. Kirim permintaan langsung Create akun Code `SUSP-079`, Name `Suspended Create {runId}-079`, Function Depreciation Expense ke server menggunakan sesi API aktor Total Control hingga respons diterima
5. Verifikasi aksi tulis ditolak dengan 403
6. Verifikasi respons penolakan memuat copy baku `entity_isolation()` §18.8
7. Verifikasi daftar akun dari server memuat akun A `DID079A` dengan Account Name `Akun Suspended A {runId}-079`
8. Verifikasi tidak ada perubahan data: jumlah akun sama dengan langkah 1 dan daftar tidak memuat Code `SUSP-079`

### TC-FA-COA-113: Client Suspended tetap dapat membaca

9. Buka tab Chart of Accounts
10. Verifikasi daftar akun tampil dengan sedikitnya satu baris
11. Klik icon Changelog
12. Verifikasi Modal Changelog tampil
13. Tutup Modal Changelog
14. Klik icon Download, lalu pilih `Download as CSV`
15. Verifikasi berkas CSV terunduh

### TC-FA-COA-277: Permintaan langsung Edit

16. Catat Account Name akun A dari server
17. Kirim permintaan langsung Edit Account Name akun A menjadi `Suspended Edit {runId}-079` ke server menggunakan sesi API aktor Total Control hingga respons diterima
18. Verifikasi aksi tulis ditolak dengan 403
19. Verifikasi respons penolakan memuat copy baku `entity_isolation()` §18.8
20. Verifikasi tidak ada perubahan data: Account Name akun A pada server sama dengan langkah 16

### TC-FA-COA-278: Permintaan langsung Activate

21. Kirim permintaan langsung Activate akun B ke server menggunakan sesi API aktor Total Control hingga respons diterima
22. Verifikasi aksi tulis ditolak dengan 403
23. Verifikasi respons penolakan memuat copy baku `entity_isolation()` §18.8
24. Verifikasi tidak ada perubahan data: akun B pada server tetap Inactive

### TC-FA-COA-279: Permintaan langsung Deactivate

25. Kirim permintaan langsung Deactivate akun A ke server menggunakan sesi API aktor Total Control hingga respons diterima
26. Verifikasi aksi tulis ditolak dengan 403
27. Verifikasi respons penolakan memuat copy baku `entity_isolation()` §18.8
28. Verifikasi tidak ada perubahan data: akun A pada server tetap Active

### TC-FA-COA-280: Permintaan langsung Delete

29. Kirim permintaan langsung Delete akun A ke server menggunakan sesi API aktor Total Control hingga respons diterima
30. Verifikasi aksi tulis ditolak dengan 403
31. Verifikasi respons penolakan memuat copy baku `entity_isolation()` §18.8
32. Verifikasi tidak ada perubahan data: akun A masih ada pada daftar akun dari server dengan Status Active

### TC-FA-COA-142: Plan Starter

33. Ganti akun: logout, lalu login sebagai Total Control pada client plan Starter dengan `Spectra.env.FA_TC_PASSWORD`
34. Catat jumlah akun client Starter dari server (baseline)
35. Periksa menu Settings di Fixed Asset
36. Verifikasi menu `Accounting` Disabled
37. Verifikasi menu `Accounting` memuat chip "Upgrade" sesuai plan Starter (`None`)
38. Klik menu `Accounting`
39. Verifikasi tab Chart of Accounts tidak dapat dibuka dari navigasi
40. Verifikasi tidak ada perubahan data: jumlah akun client Starter sama dengan langkah 34

## Notes

- `K-1`: TC-FA-COA-112, TC-FA-COA-277, TC-FA-COA-278, TC-FA-COA-279, dan TC-FA-COA-280 berkelas h dengan Expected respons API; tetap di spec FE+BE karena TC granular tetap sumber dan tiap TC tepat satu spec.
- Alasan di atas sekitar 35 langkah (40 langkah): semua blok satu kelas harness (state tenant), tiap blok berdiri sendiri, dan empat blok permintaan langsung (langkah 16 sampai 32) berpola sama (kirim, 403, copy baku, data tidak berubah) dengan parameter berbeda; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (S-03): langkah 9 membuka ulang tab (TC-FA-COA-113 langkah 1), langkah 13 menutup Modal Changelog, langkah 1, 16, 34 mencatat baseline dari server, langkah 33 ganti akun, langkah 35 (periksa menu Settings di Fixed Asset) dan langkah 38 (klik menu `Accounting`) memuat aksi yang tidak ada di TC-FA-COA-142. Langkah 7 (daftar memuat akun A) menjadi anchor positif sebelum asersi tidak adanya `SUSP-079` pada langkah 8 (bagian 8b butir 2).
- Pembagian lockdown: Toast T-11 hanya diasersi pada klik UI `+ Account` (langkah 3; TC-FA-COA-112 butir b: "Setelah langkah 1 (klik `+ Account`)"). Butir a dan c TC-FA-COA-112 diasersi pada permintaan langsung (langkah 5 sampai 8). Expected TC-FA-COA-277 sampai 280 tidak memuat toast, sehingga permintaan langsung (tidak melewati browser, bagian 8b butir 1) hanya mengasersi 403, copy baku, dan data tidak berubah.
- Asersi "tidak ada log" tidak ada di spec ini; Post Condition TC-FA-COA-112 sampai 280 tidak memuatnya.
- `A-18`: Account Code literal tanpa suffix menjadi objek asersi: `DID079A` (TC-FA-COA-112; langkah 7) dan `SUSP-079` (TC-FA-COA-112; langkah 8, tidak ada pada daftar akun). `DID079A` dan `DID079B` di-seed lalu dihapus di hook `before` dan `after`; `SUSP-079` hanya diketik pada Create yang selalu ditolak 403 dan tidak pernah tersimpan.
- Temuan untuk QA:
  - TC-FA-COA-112, 113, 277 sampai 280: kolom ACC hanya menyebut "Entitas berstatus Suspended". Judul menyebut "atau Expired" tetapi tidak ada data uji client Expired; spec hanya menguji Suspended. Client Suspended, Expired, dan Starter tidak punya identitas di Pre-setup TC (disediakan tim FE, kunci fixture ditetapkan tim FE).
  - TC-FA-COA-112 tidak menyatakan apakah Modal Add Account terbuka sesudah klik `+ Account` di client Suspended; langkah 3 hanya mengasersi Toast T-11 tanpa asersi modal.
  - Copy baku `entity_isolation()` §18.8 dan teks Toast T-11 tidak ditulis di TC; spec mengasersi "sesuai copy baku" tanpa teks literal. Perlu dikutip di TC.
  - TC-FA-COA-277 sampai 280 memakai P1 dan P3 sebagai target permintaan langsung; spec memakai akun milik spec `DID079A` dan `DID079B` pada client Suspended (S-06). Meng-seed akun pada client Suspended membutuhkan kemampuan seed backend yang tidak terkena lockdown; perlu dikonfirmasi tim FE/BE.
  - TC-FA-COA-113 Expected "Download tetap berfungsi" tidak menyebut format; spec memakai `Download as CSV` (sama dengan TC-FA-COA-87).
  - TC-FA-COA-112 tidak menyebut payload Create; Code `SUSP-079` literal (Account Code maksimal 15 karakter, tidak dapat diberi suffix `{runId}`), Name bersuffix.
  - TC-FA-COA-142 Expected c ("Tidak ada perubahan data") tanpa langkah observasi; spec membandingkan jumlah akun lewat kemampuan baca dari server (disediakan tim FE/BE).
  - Nama env var password tidak ada tambahan pada spec ini (hanya `FA_TC_PASSWORD`).
