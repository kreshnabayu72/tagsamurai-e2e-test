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
6. Hapus Client baru hasil langkah 3 lewat Fixture BE

### TC-AC-LCS-562: Email Client baru cocok dengan indeks arsip dalam retensi, Client dibuat normal, notifikasi view-only ke Principal berizin, penanda pada Client

7. Atur lewat Fixture BE: Company PT Lama Sejahtera sudah di-Hard Purge 100 hari lalu (retensi 730 hari) dengan email `ops@ptlamasejahtera.example` pada indeks arsip; Principal berizin Update pada role "Manage archived client" tersedia pada Group tempat Client baru PT Baru Mandiri ditempatkan (atau salah satu ancestor-nya)
8. Catat baseline jumlah notifikasi Principal berizin
9. Buat Client baru PT Baru Mandiri dengan email User `ops@ptlamasejahtera.example`
10. Verifikasi Client PT Baru Mandiri berhasil dibuat tanpa gangguan
11. Ganti akun ke Principal berizin lalu buka Overlay Notifikasi
12. Verifikasi jumlah notifikasi Principal berizin bertambah tepat satu dari baseline
13. Verifikasi notifikasi baru dalam aplikasi view-only memuat nama Client baru, email yang cocok, nama perusahaan lama, dan tanggal pembersihannya
14. Klik notifikasi tersebut
15. Verifikasi Detail Client PT Baru Mandiri terbuka
16. Verifikasi penanda match internal tampil pada Client

### TC-AC-LCS-563: Satu email cocok dengan lebih dari satu baris indeks, satu notifikasi memuat semua baris yang cocok

17. Atur lewat Fixture BE; hapus Client PT Baru Mandiri hasil TC sebelumnya (data milik spec) lewat Fixture BE: email `ops@ptlamasejahtera.example` pada dua baris indeks arsip dari dua company yang pernah di-purge (PT Lama Sejahtera dan PT Lama Makmur) dengan retensi masih berlaku
18. Ganti akun ke Total Control
19. Catat baseline jumlah notifikasi Principal berizin
20. Buat Client baru PT Baru Mandiri dengan email User `ops@ptlamasejahtera.example`
21. Ganti akun ke Principal berizin lalu buka Overlay Notifikasi
22. Verifikasi jumlah notifikasi Principal berizin bertambah tepat satu dari baseline
23. Verifikasi notifikasi baru memuat nama perusahaan lama dan tanggal pembersihan dari kedua baris indeks yang cocok

### TC-AC-LCS-564: Kecocokan indeks arsip yang masa retensinya sudah lewat tidak menghasilkan notifikasi maupun penanda

24. Atur lewat Fixture BE; hapus Client PT Baru Mandiri hasil TC sebelumnya (data milik spec) lewat Fixture BE: Company PT Lama Sejahtera sudah di-Hard Purge 800 hari lalu (retensi 730 hari sudah lewat); catat baseline jumlah notifikasi Principal berizin
25. Ganti akun ke Total Control
26. Buat Client baru dengan email User milik PT Lama Sejahtera
27. Verifikasi Client dibuat normal
28. Ganti akun ke Principal berizin lalu buka Overlay Notifikasi
29. Buka Detail Client yang baru dibuat sebagai Principal berizin
30. Verifikasi tidak ada notifikasi baru (selisih terhadap baseline 0) dan tidak ada penanda match

### TC-AC-LCS-565: Email Client baru berbeda dari data riwayat, tidak ada pencocokan otomatis

31. Atur lewat Fixture BE; hapus Client PT Baru Mandiri hasil TC sebelumnya (data milik spec) lewat Fixture BE: Company PT Lama Sejahtera sudah di-Hard Purge 100 hari lalu; catat baseline jumlah notifikasi Principal berizin
32. Ganti akun ke Total Control
33. Buat Client baru dengan email User yang tidak ada pada indeks arsip
34. Verifikasi Client dibuat normal
35. Ganti akun ke Principal berizin lalu buka Overlay Notifikasi
36. Buka Detail Client yang baru dibuat sebagai Principal berizin
37. Verifikasi tidak ada notifikasi baru (selisih terhadap baseline 0) dan tidak ada penanda match

## Notes

- Mode: FE+BE. Sumber: `admin-console/plans-licensing-lifecycle-settings/TestCases/tc-plans-licensing-lifecycle-settings.md`. Kelas harness d.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC mengikuti urutan nomor kolom `sourceTc`.
- TC 564 dan 565 memuat satu `Verifikasi` untuk dua klausa absence (tidak ada notifikasi dan tidak ada penanda match) yang disebut utuh dalam satu butir Expected TC (daftar elemen yang sama-sama tidak ada, S-01); anchor positifnya `Verifikasi` Client dibuat normal dan Overlay Notifikasi yang dibuka.
- Temuan untuk QA:
  - TC 562 Expected b menyebut "klik membuka Detail Client baru" tanpa langkah klik di kolom Langkah Uji; spec menambah satu aksi klik notifikasi (langkah penghubung) sebagai pemicu asersi tersebut.
  - TC 562 langkah 4 membuka Detail Client PT Baru Mandiri sebagai Principal berizin, sedangkan klik notifikasi (langkah 14) sudah membuka Detail Client yang sama; spec tidak mengulang pembukaan Detail dan memverifikasi penanda match pada Detail yang terbuka dari klik notifikasi (langkah 16).
  - TC 565 Expected b menyebut "tidak ada penanda match" tanpa langkah yang membuka Detail Client; spec membuka Detail Client sebagai langkah penghubung seperti TC 564.
  - Form pembuatan Client (menu, field wajib selain nama dan email) tidak dirinci di TC; spec menulis satu langkah ringkas dan field wajib lain disediakan tim FE.
  - Akun Principal berizin tertulis di Pre-setup 15 (usulan pola Pre-setup 6; keberadaan akun perlu dikonfirmasi tim FE); env password tidak terdaftar sehingga disediakan tim FE.
  - Post Condition TC 561 (Client baru hasil langkah 2 dihapus sebagai cleanup) dilaksanakan di langkah 6; Post Condition TC lain ("Tidak ada perubahan data") tanpa langkah observasi tidak diasersi.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`; pemulihan state, pembukaan tab, pengaturan data lewat Fixture BE, baseline notifikasi, klik notifikasi, dan ganti akun): langkah 1-2, 6-8, 11, 14, 17-19, 21, 24-25, 28-29, 31-32, 35-36. Baseline notifikasi Principal berizin (langkah 8, 19) dicatat sebelum pemicu agar `Verifikasi` jumlah notifikasi memakai selisih satu (S-12).
- Alasan di atas sekitar 35 langkah: kelima blok TC (561 sampai 565) satu kelas harness d tentang pencocokan arsip post-purge, memakai Detail Client dan Overlay Notifikasi yang sama, dan tiap blok memakai data arsip dan baseline notifikasi sendiri yang diatur lewat Fixture BE dan dipulihkan langkah penghubung; memecahnya hanya mengulang pengaturan Fixture BE dan ganti akun yang sama, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
