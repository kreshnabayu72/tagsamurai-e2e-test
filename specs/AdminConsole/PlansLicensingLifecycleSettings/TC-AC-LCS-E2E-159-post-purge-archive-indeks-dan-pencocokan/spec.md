---
id: TC-AC-LCS-E2E-159-post-purge-archive-indeks-dan-pencocokan
title: "Post-Purge Archive Matching: Indeks Arsip, Pencocokan Email Client Baru, dan Masa Retensi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-561
  - TC-AC-LCS-562
  - TC-AC-LCS-563
  - TC-AC-LCS-564
  - TC-AC-LCS-565
coverage:
  web: automated
---

# Post-Purge Archive Matching: Indeks Arsip, Pencocokan Email Client Baru, dan Masa Retensi

## Prerequisites

- Mode: FE+BE. Kelas harness d (harness eksternal: job lifecycle Hard Purge, jam server, dan pencocokan indeks arsip sebagai objek uji).
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`), password dari `Spectra.env.AC_TC_PASSWORD` (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Data Pre-setup yang dipakai: Company PT Lama Sejahtera (purged), PT Lama Makmur, Client baru PT Baru Mandiri (Pre-setup 10) dan Principal berizin Update pada role "Manage archived client" (Pre-setup 11). Email `ops@ptlamasejahtera.example` dan nama Client PT Baru Mandiri adalah data TC yang dicocokkan dengan indeks arsip (literal, bukan data bersuffix); seeding indeks dan pembuangan Client hasil spec deterministik lewat Fixture BE antar-TC dan di hook `after` suite. Email pengguna PT Lama Sejahtera dicatat pada indeks arsip lewat Fixture BE. Form pembuatan Client memakai field wajib lain yang disediakan tim FE.
- Akun Partner, Distributor, dan Principal berizin "Manage allocation" atau "Manage archived client" (Pre-setup 11) tertulis di Pre-setup 15 sebagai usulan pola Pre-setup 6 (keberadaan akun perlu dikonfirmasi tim FE): `manageAllocationPrincipal_automated_{namaCompany}@qwertysystem.net`, `manageArchivedClientPrincipal_automated_{namaCompany}@qwertysystem.net`, `manageAllocationPartner_automated_{namaCompany}@qwertysystem.net`, `manageAllocationDistributor_automated_{namaCompany}@qwertysystem.net`; env password akun-akun itu belum terdaftar, jadi disediakan tim FE. Email pengguna Total Control produk terdampak tidak tertulis di Pre-setup TC: disediakan tim FE (lihat Temuan untuk QA). Ganti akun ke Principal berizin memakai kredensial yang disediakan tim FE.
- Kemampuan teknis (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan endpoint-nya): Fixture BE untuk mengatur tanggal data uji subscription, mengatur jam server dan jam browser, memicu eksekusi job lifecycle dan job Email Trigger Engine, serta membaca log job; mail-catcher atau inbox riil dengan baseline jumlah email per alamat sebelum aksi (S-12). Indeks arsip dibaca lewat Fixture BE.
- Notifikasi view-only yang diasersi memakai baseline jumlah notifikasi Principal berizin sebelum aksi (S-12).
- State global: jam server dan jam browser digeser, subscription uji PT Maju Jaya, antrean job, dan konfigurasi tab diubah spec ini; dipulihkan di hook `beforeEach` dan `after` suite lewat Fixture BE; suite berjalan serial.
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab Lifecycle Settings ke nilai default, jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings; flag Guided Tooltip halaman ini diset true oleh hook `before` suite; hook `after` suite memulihkan state global. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (akun aktor, nilai default tujuh tab, dataset Changelog, daftar client; tanpa password) dirujuk lewat `Fixture.lifecycleSettings.<kunci>` (`fixtures/lifecycle-settings.json`); nilai uji yang diketik atau dikirim di langkah sama dengan TC (S-02).

## Test Steps

### TC-AC-LCS-561: Hard Purge mencatat indeks arsip dan melepas email pengguna sehingga dapat dipakai ulang

1. Atur lewat Fixture BE: Company PT Lama Sejahtera dengan dua pengguna aktif mencapai Hard Purge; Principal berizin Update pada role "Manage archived client" tersedia
2. Picu eksekusi job lifecycle hingga Hard Purge PT Lama Sejahtera lewat Fixture BE
3. Buat Client baru dengan email salah satu pengguna PT Lama Sejahtera
4. Verifikasi pembuatan Client baru berhasil (email sudah dilepas dari klaim unik)
5. Verifikasi indeks arsip (dibaca lewat Fixture BE) memuat nama perusahaan, tanggal pembersihan, dan batas kedaluwarsa retensi untuk kedua email

### TC-AC-LCS-562: Email Client baru cocok dengan indeks arsip dalam retensi, Client dibuat normal, notifikasi view-only ke Principal berizin, penanda pada Client

6. Atur lewat Fixture BE: Company PT Lama Sejahtera sudah di-Hard Purge 100 hari lalu (retensi 730 hari) dengan email `ops@ptlamasejahtera.example` pada indeks arsip; Principal berizin Update pada role "Manage archived client" tersedia pada Group tempat Client baru PT Baru Mandiri ditempatkan (atau salah satu ancestor-nya)
7. Buat Client baru PT Baru Mandiri dengan email User `ops@ptlamasejahtera.example`
8. Verifikasi Client PT Baru Mandiri berhasil dibuat tanpa gangguan
9. Ganti akun ke Principal berizin lalu buka Overlay Notifikasi
10. Verifikasi satu notifikasi dalam aplikasi view-only memuat nama Client baru, email yang cocok, nama perusahaan lama, dan tanggal pembersihannya
11. Klik notifikasi tersebut
12. Verifikasi Detail Client PT Baru Mandiri terbuka
13. Buka Detail Client PT Baru Mandiri sebagai Principal berizin
14. Verifikasi penanda match internal tampil pada Client

### TC-AC-LCS-563: Satu email cocok dengan lebih dari satu baris indeks, satu notifikasi memuat semua baris yang cocok

15. Atur lewat Fixture BE; hapus Client PT Baru Mandiri hasil TC sebelumnya (data milik spec) lewat Fixture BE: email `ops@ptlamasejahtera.example` pada dua baris indeks arsip dari dua company yang pernah di-purge (PT Lama Sejahtera dan PT Lama Makmur) dengan retensi masih berlaku
16. Ganti akun ke Total Control
17. Buat Client baru PT Baru Mandiri dengan email User `ops@ptlamasejahtera.example`
18. Ganti akun ke Principal berizin lalu buka Overlay Notifikasi
19. Verifikasi satu notifikasi memuat nama perusahaan lama dan tanggal pembersihan dari kedua baris indeks yang cocok

### TC-AC-LCS-564: Kecocokan indeks arsip yang masa retensinya sudah lewat tidak menghasilkan notifikasi maupun penanda

20. Atur lewat Fixture BE; hapus Client PT Baru Mandiri hasil TC sebelumnya (data milik spec) lewat Fixture BE: Company PT Lama Sejahtera sudah di-Hard Purge 800 hari lalu (retensi 730 hari sudah lewat); catat baseline jumlah notifikasi Principal berizin
21. Ganti akun ke Total Control
22. Buat Client baru dengan email User milik PT Lama Sejahtera
23. Verifikasi Client dibuat normal
24. Ganti akun ke Principal berizin lalu buka Overlay Notifikasi
25. Buka Detail Client yang baru dibuat sebagai Principal berizin
26. Verifikasi tidak ada notifikasi baru (selisih terhadap baseline 0) dan tidak ada penanda match

### TC-AC-LCS-565: Email Client baru berbeda dari data riwayat, tidak ada pencocokan otomatis

27. Atur lewat Fixture BE; hapus Client PT Baru Mandiri hasil TC sebelumnya (data milik spec) lewat Fixture BE: Company PT Lama Sejahtera sudah di-Hard Purge 100 hari lalu; catat baseline jumlah notifikasi Principal berizin
28. Ganti akun ke Total Control
29. Buat Client baru dengan email User yang tidak ada pada indeks arsip
30. Verifikasi Client dibuat normal
31. Ganti akun ke Principal berizin lalu buka Overlay Notifikasi
32. Buka Detail Client yang baru dibuat sebagai Principal berizin
33. Verifikasi tidak ada notifikasi baru (selisih terhadap baseline 0) dan tidak ada penanda match

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness d.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti urutan nomor kolom `sourceTc`.
- TC 564 dan 565 memuat satu `Verifikasi` untuk dua klausa absence (tidak ada notifikasi dan tidak ada penanda match) yang disebut utuh dalam satu butir Expected TC (daftar elemen yang sama-sama tidak ada, S-01); anchor positifnya `Verifikasi` Client dibuat normal dan Overlay Notifikasi yang dibuka.
- Temuan untuk QA:
  - TC 562 Expected b menyebut "klik membuka Detail Client baru" tanpa langkah klik di kolom Langkah Uji; spec menambah satu aksi klik notifikasi (langkah penghubung) sebagai pemicu asersi tersebut.
  - TC 565 Expected b menyebut "tidak ada penanda match" tanpa langkah yang membuka Detail Client; spec membuka Detail Client sebagai langkah penghubung seperti TC 564.
  - Form pembuatan Client (menu, field wajib selain nama dan email) tidak dirinci di TC; spec menulis satu langkah ringkas dan field wajib lain disediakan tim FE.
  - Akun Principal berizin kini tertulis di Pre-setup 15 (usulan pola Pre-setup 6; keberadaan akun perlu dikonfirmasi tim FE); env password tidak terdaftar sehingga disediakan tim FE.
  - Post Condition seluruh TC ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, dan ganti akun): langkah 1-2, 6, 9, 13, 15-16, 18, 20-21, 24-25, 27-28, 31-32.
