---
id: TC-AC-LCS-E2E-154-notifikasi-plan-owner-penerima-dan-deduplikasi
title: "Notifikasi Plan Owner dalam Aplikasi: Penerima per Level, Deduplikasi, dan Client Direct"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-540
  - TC-AC-LCS-541
  - TC-AC-LCS-542
coverage:
  web: automated
---

# Notifikasi Plan Owner dalam Aplikasi: Penerima per Level, Deduplikasi, dan Client Direct

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Akun tambahan (ganti akun eksplisit), semua berizin Update "Manage allocation" (Pre-setup 15, usulan; keberadaan akun dan env password disediakan tim FE, sama dengan spec 157, 159, 160, 162): pengguna Partner `manageAllocationPartner_automated_{namaCompany}@qwertysystem.net`, pengguna Distributor `manageAllocationDistributor_automated_{namaCompany}@qwertysystem.net`, dan Principal `manageAllocationPrincipal_automated_{namaCompany}@qwertysystem.net`. Pengguna yang memenuhi syarat pada dua level (TC-AC-LCS-541, langkah 24): akun disediakan tim FE sebagai pengguna dengan Update "Manage allocation" di level Distributor dan Principal; nama akun belum ada di TC maupun `fixtures/lifecycle-settings.json` (lihat Notes, Temuan untuk QA).
- Data: Client PT Maju Jaya (`Fixture.lifecycleSettings.clientMajuJaya`), Partner PT Mitra Satu, dan Distributor PT Distribusi Utama diseed per TC lewat Fixture BE dengan struktur level dan pengguna berizin sesuai precondition TC (dibuat dan dibuang per TC).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): Fixture BE untuk mengatur tanggal data uji, memajukan jam server dan jam browser, memicu eksekusi job, membaca log job, dan memulihkan ketujuh tab ke nilai default. Kemampuan membaca jumlah notifikasi per penerima dan email di inbox pengguna Total Control produk terdampak sebagai baseline (R-11, S-12).
- Jendela absence notifikasi in-app: "Tunggu 5 detik tanpa memuat ulang halaman" sebelum asersi absence adalah pilihan spec (bukan nilai TC atau PRD) sampai TC menyatakan durasinya (bagian 6).
- Waktu: tanggal data uji diatur lewat Fixture BE; jam server tidak digeser. Hook `after` mengembalikan sesi ke akun default suite (Total Control) dan memulihkan data uji. Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Fixture `fixtures/lifecycle-settings.json`; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>`.

## Test Steps

### TC-AC-LCS-540: Notifikasi Plan Owner dikirim sebagai notifikasi dalam aplikasi ke pengguna Partner, Distributor, dan Principal berizin Manage allocation

1. Atur lewat Fixture BE: Client PT Maju Jaya di bawah Partner PT Mitra Satu dan Distributor PT Distribusi Utama, masing-masing satu pengguna Partner (`manageAllocationPartner_automated_{namaCompany}@qwertysystem.net`), Distributor (`manageAllocationDistributor_automated_{namaCompany}@qwertysystem.net`), dan Principal (`manageAllocationPrincipal_automated_{namaCompany}@qwertysystem.net`) memiliki Update pada role "Manage allocation" untuk Group client tersebut, dan subscription Paid PT Maju Jaya berakhir 45 hari lagi
2. Catat baseline jumlah email di inbox pengguna Total Control produk terdampak PT Maju Jaya
3. Catat baseline jumlah notifikasi pengguna Partner
4. Catat baseline jumlah notifikasi pengguna Distributor
5. Catat baseline jumlah notifikasi Principal berizin
6. Picu eksekusi job Email Trigger Engine lewat Fixture BE
7. Ganti akun: login sebagai pengguna Partner berizin `manageAllocationPartner_automated_{namaCompany}@qwertysystem.net`
8. Buka Overlay Notifikasi
9. Verifikasi jumlah notifikasi pengguna Partner bertambah tepat satu dari baseline
10. Verifikasi notifikasi baru pengguna Partner adalah pengingat perpanjangan langganan untuk subscription PT Maju Jaya
11. Ganti akun: login sebagai pengguna Distributor berizin `manageAllocationDistributor_automated_{namaCompany}@qwertysystem.net`
12. Buka Overlay Notifikasi
13. Verifikasi jumlah notifikasi pengguna Distributor bertambah tepat satu dari baseline
14. Verifikasi notifikasi baru pengguna Distributor adalah pengingat perpanjangan langganan untuk subscription PT Maju Jaya
15. Ganti akun: login sebagai Principal berizin Update "Manage allocation" `manageAllocationPrincipal_automated_{namaCompany}@qwertysystem.net`
16. Buka Overlay Notifikasi
17. Verifikasi jumlah notifikasi Principal berizin bertambah tepat satu dari baseline
18. Verifikasi notifikasi baru Principal berizin adalah pengingat perpanjangan langganan untuk subscription PT Maju Jaya
19. Baca inbox pengguna Total Control produk terdampak PT Maju Jaya
20. Verifikasi inbox pengguna Total Control produk terdampak PT Maju Jaya tidak menerima email dari tahapan Notifikasi Plan Owner (jumlah email sama dengan baseline)

### TC-AC-LCS-541: Pengguna yang memenuhi syarat pada dua level menerima satu notifikasi (deduplikasi)

21. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Client PT Maju Jaya di bawah Distributor PT Distribusi Utama, satu pengguna dua level (akun disediakan tim FE, lihat Prerequisites) memiliki Update pada role "Manage allocation" di level Distributor dan level Principal, dan subscription Paid PT Maju Jaya berakhir 45 hari lagi
22. Catat baseline jumlah notifikasi pengguna yang memenuhi syarat pada dua level
23. Picu eksekusi job Email Trigger Engine lewat Fixture BE
24. Ganti akun: login sebagai pengguna yang memenuhi syarat pada dua level
25. Buka Overlay Notifikasi
26. Verifikasi jumlah notifikasi pengguna bertambah tepat satu dari baseline
27. Verifikasi notifikasi baru pengguna adalah pengingat perpanjangan langganan untuk subscription PT Maju Jaya

### TC-AC-LCS-542: Client Direct tanpa Partner: level Partner dilewati dan level lain tetap menerima notifikasi Plan Owner

28. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Client PT Maju Jaya sebagai client Direct di bawah Distributor PT Distribusi Utama tanpa Partner, pengguna Distributor (`manageAllocationDistributor_automated_{namaCompany}@qwertysystem.net`) dan Principal (`manageAllocationPrincipal_automated_{namaCompany}@qwertysystem.net`) berizin Manage allocation tersedia, pengguna Partner berizin Update "Manage allocation" (`manageAllocationPartner_automated_{namaCompany}@qwertysystem.net`) disiapkan sebagai pengamat, dan subscription Paid PT Maju Jaya berakhir 45 hari lagi
29. Catat baseline jumlah notifikasi pengguna Distributor berizin dan Principal berizin
30. Catat baseline jumlah notifikasi pengguna Partner berizin Update "Manage allocation" `manageAllocationPartner_automated_{namaCompany}@qwertysystem.net`
31. Picu eksekusi job Email Trigger Engine lewat Fixture BE
32. Ganti akun: login sebagai pengguna Distributor berizin `manageAllocationDistributor_automated_{namaCompany}@qwertysystem.net`
33. Buka Overlay Notifikasi
34. Verifikasi jumlah notifikasi pengguna Distributor berizin bertambah tepat satu dari baseline
35. Ganti akun: login sebagai Principal berizin Update "Manage allocation" `manageAllocationPrincipal_automated_{namaCompany}@qwertysystem.net`
36. Buka Overlay Notifikasi
37. Verifikasi jumlah notifikasi Principal berizin bertambah tepat satu dari baseline
38. Ganti akun: login sebagai pengguna Partner berizin Update "Manage allocation" `manageAllocationPartner_automated_{namaCompany}@qwertysystem.net`
39. Buka Overlay Notifikasi
40. Tunggu 5 detik tanpa memuat ulang halaman
41. Verifikasi tidak ada notifikasi untuk level Partner (jumlah notifikasi pengguna Partner sama dengan baseline)
42. Verifikasi tidak ada notifikasi fallback ke level lain (jumlah notifikasi hanya bertambah satu per penerima yang berizin dibanding baseline)

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Atur lewat Fixture BE ..." (precondition TC), "Catat baseline ..." (langkah 2 sampai 5, 22, 29, 30; R-11, S-12; baseline notifikasi per penerima sebelum pemicu agar `Verifikasi` memakai selisih satu), "Ganti akun ..." (S-07), "Buka Overlay Notifikasi", "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 40, jendela absence notifikasi; bagian 6), dan "Pulihkan ..." antar TC (S-03, S-09).
- Asersi tidak adanya notifikasi atau email (TC-AC-LCS-540 butir b dan TC-AC-LCS-542 butir c) didahului `Verifikasi` notifikasi yang membuktikan surface yang sama sudah berisi hasil dari pemicu yang sama dan memakai baseline (bagian 8b butir 2, S-12).
- Temuan untuk QA: TC-AC-LCS-540 sampai 542 tidak menyebut akun grantee Update "Manage allocation"; spec memakai akun Pre-setup 15 `manageAllocationPartner`, `manageAllocationDistributor`, `manageAllocationPrincipal` (usulan, sama dengan spec 157, 159, 160, 162) sebagai grantee di langkah 1, 21, dan 28. TC-AC-LCS-542 tidak menyebut pengguna Partner yang diamati untuk "tidak ada notifikasi untuk level Partner"; langkah 30 dan 38 memakai `manageAllocationPartner` (berizin, sehingga absence tidak lulus semu karena tak berizin) sebagai pengamat. TC-AC-LCS-541 tidak menyebut akun pengguna yang memenuhi syarat pada dua level dan fixture tidak memuat akun itu; langkah 24 memakai akun yang perlu disediakan tim FE dan namanya perlu ditetapkan di TC dan Pre-setup; TC-AC-LCS-542 menyebut "tidak ada notifikasi untuk level Partner" tanpa menyebut cara mengamatinya pada client tanpa Partner (spec memakai pembacaan jumlah notifikasi lewat kemampuan baca). Mekanisme membaca log job dan notifikasi tidak didefinisikan di TC, PRD, atau LLD (S-13).
- Temuan untuk QA: Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
- Alasan di atas sekitar 35 langkah: ketiga blok TC (540, 541, 542) memakai pola yang sama (state diatur lewat Fixture BE, baseline notifikasi per penerima dicatat, pemicu dijalankan, Overlay Notifikasi dibaca), semuanya satu kelas harness, dan tiap blok memakai state dan baseline sendiri yang dipulihkan langkah penghubung; memecahnya hanya mengulang pengaturan Fixture BE dan ganti akun yang sama, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
