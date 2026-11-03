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
- Akun tambahan (ganti akun eksplisit): pengguna Partner `partnerUser_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.AC_PARTNER_PASSWORD`), pengguna Distributor `distributorUser_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.AC_DIST_PASSWORD`), dan Principal berizin Update "Manage allocation" (Pre-setup 11) beserta pengguna yang memenuhi syarat pada dua level; akun Principal berizin `manageAllocationPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup 15, usulan pola Pre-setup 6; keberadaan akun perlu dikonfirmasi tim FE), env password disediakan tim FE.
- Data: Client PT Maju Jaya (`Fixture.lifecycleSettings.clientMajuJaya`), Partner PT Mitra Satu, dan Distributor PT Distribusi Utama diseed per TC lewat Fixture BE dengan struktur level dan pengguna berizin sesuai precondition TC (dibuat dan dibuang per TC).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): Fixture BE untuk mengatur tanggal data uji, memajukan jam server dan jam browser, memicu eksekusi job, membaca log job, dan memulihkan ketujuh tab ke nilai default. Kemampuan membaca jumlah notifikasi per penerima dan email di inbox pengguna Total Control produk terdampak sebagai baseline (R-11, S-12).
- Waktu: tanggal data uji diatur lewat Fixture BE; jam server tidak digeser. Hook `after` mengembalikan sesi ke akun default suite (Total Control) dan memulihkan data uji. Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Fixture `fixtures/lifecycleSettings.json` belum ada dan disediakan tim FE; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tersedia.

## Test Steps

### TC-AC-LCS-540: Notifikasi Plan Owner dikirim sebagai notifikasi dalam aplikasi ke pengguna Partner, Distributor, dan Principal berizin Manage allocation

1. Atur lewat Fixture BE: Client PT Maju Jaya di bawah Partner PT Mitra Satu dan Distributor PT Distribusi Utama, masing-masing satu pengguna Partner, Distributor, dan Principal memiliki Update pada role "Manage allocation" untuk Group client tersebut, dan subscription Paid PT Maju Jaya berakhir 45 hari lagi
2. Catat baseline jumlah email di inbox pengguna Total Control produk terdampak PT Maju Jaya
3. Picu eksekusi job Email Trigger Engine lewat Fixture BE
4. Ganti akun: login sebagai pengguna Partner berizin `partnerUser_automated_{namaCompany}@qwertysystem.net`
5. Buka Overlay Notifikasi
6. Verifikasi pengguna Partner menerima tepat satu notifikasi dalam aplikasi pengingat perpanjangan langganan untuk subscription PT Maju Jaya
7. Ganti akun: login sebagai pengguna Distributor berizin `distributorUser_automated_{namaCompany}@qwertysystem.net`
8. Buka Overlay Notifikasi
9. Verifikasi pengguna Distributor menerima tepat satu notifikasi dalam aplikasi pengingat perpanjangan langganan untuk subscription PT Maju Jaya
10. Ganti akun: login sebagai Principal berizin Update "Manage allocation"
11. Buka Overlay Notifikasi
12. Verifikasi Principal berizin menerima tepat satu notifikasi dalam aplikasi pengingat perpanjangan langganan untuk subscription PT Maju Jaya
13. Baca inbox pengguna Total Control produk terdampak PT Maju Jaya
14. Verifikasi inbox pengguna Total Control produk terdampak PT Maju Jaya tidak menerima email dari tahapan Notifikasi Plan Owner (jumlah email sama dengan baseline)

### TC-AC-LCS-541: Pengguna yang memenuhi syarat pada dua level menerima satu notifikasi (deduplikasi)

15. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Client PT Maju Jaya di bawah Distributor PT Distribusi Utama, satu pengguna memiliki Update pada role "Manage allocation" di level Distributor dan level Principal, dan subscription Paid PT Maju Jaya berakhir 45 hari lagi
16. Picu eksekusi job Email Trigger Engine lewat Fixture BE
17. Ganti akun: login sebagai pengguna yang memenuhi syarat pada dua level
18. Buka Overlay Notifikasi
19. Verifikasi pengguna menerima tepat satu notifikasi pengingat perpanjangan langganan untuk subscription PT Maju Jaya

### TC-AC-LCS-542: Client Direct tanpa Partner: level Partner dilewati dan level lain tetap menerima notifikasi Plan Owner

20. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Client PT Maju Jaya sebagai client Direct di bawah Distributor PT Distribusi Utama tanpa Partner, pengguna Distributor dan Principal berizin Manage allocation tersedia, dan subscription Paid PT Maju Jaya berakhir 45 hari lagi
21. Catat baseline jumlah notifikasi pengguna Distributor berizin dan Principal berizin
22. Picu eksekusi job Email Trigger Engine lewat Fixture BE
23. Ganti akun: login sebagai pengguna Distributor berizin `distributorUser_automated_{namaCompany}@qwertysystem.net`
24. Buka Overlay Notifikasi
25. Verifikasi pengguna Distributor berizin menerima satu notifikasi
26. Ganti akun: login sebagai Principal berizin Update "Manage allocation"
27. Buka Overlay Notifikasi
28. Verifikasi Principal berizin menerima satu notifikasi
29. Verifikasi tidak ada notifikasi untuk level Partner dan tidak ada notifikasi fallback ke level lain (jumlah notifikasi sesuai baseline ditambah satu per penerima yang berizin)

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Atur lewat Fixture BE ..." (precondition TC), "Catat baseline ..." (R-11, S-12), "Ganti akun ..." (S-07), "Buka Overlay Notifikasi", dan "Pulihkan ..." antar TC (S-03, S-09).
- Asersi tidak adanya notifikasi atau email (TC-AC-LCS-540 butir b dan TC-AC-LCS-542 butir c) didahului `Verifikasi` notifikasi yang membuktikan surface yang sama sudah berisi hasil dari pemicu yang sama dan memakai baseline (bagian 8b butir 2, S-12).
- Temuan untuk QA: TC-AC-LCS-541 tidak menyebut akun pengguna yang memenuhi syarat pada dua level; TC-AC-LCS-542 menyebut "tidak ada notifikasi untuk level Partner" tanpa menyebut cara mengamatinya pada client tanpa Partner (spec memakai pembacaan jumlah notifikasi lewat kemampuan baca). Mekanisme membaca log job dan notifikasi tidak didefinisikan di TC, PRD, atau LLD (S-13).
- Temuan untuk QA: Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
