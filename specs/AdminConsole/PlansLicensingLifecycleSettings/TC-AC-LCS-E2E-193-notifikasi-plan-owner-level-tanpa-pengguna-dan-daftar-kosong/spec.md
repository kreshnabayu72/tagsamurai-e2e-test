---
id: TC-AC-LCS-E2E-193-notifikasi-plan-owner-level-tanpa-pengguna-dan-daftar-kosong
title: "Notifikasi Plan Owner dalam Aplikasi: Level Tanpa Pengguna Berizin dan Daftar Penerima Kosong"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-543
  - TC-AC-LCS-544
  - TC-AC-LCS-545
coverage:
  web: automated
---

# Notifikasi Plan Owner dalam Aplikasi: Level Tanpa Pengguna Berizin dan Daftar Penerima Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Akun tambahan (ganti akun eksplisit): pengguna Partner `partnerUser_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.AC_PARTNER_PASSWORD`), pengguna Distributor `distributorUser_automated_{namaCompany}@qwertysystem.net` (`Spectra.env.AC_DIST_PASSWORD`), dan Principal berizin Update "Manage allocation" (Pre-setup 11) beserta pengguna yang memenuhi syarat pada dua level; akun Principal berizin `manageAllocationPrincipal_automated_{namaCompany}@qwertysystem.net` (Pre-setup 15, usulan pola Pre-setup 6; keberadaan akun perlu dikonfirmasi tim FE), env password disediakan tim FE.
- Data: Client PT Maju Jaya (`Fixture.lifecycleSettings.clientMajuJaya`), Partner PT Mitra Satu, dan Distributor PT Distribusi Utama diseed per TC lewat Fixture BE dengan struktur level dan pengguna berizin sesuai precondition TC (dibuat dan dibuang per TC).
- Jendela absence notifikasi in-app: "Tunggu 5 detik tanpa memuat ulang halaman" sebelum asersi absence notifikasi level Partner adalah pilihan spec (bukan nilai TC atau PRD) sampai TC menyatakan durasinya (8b.11, bagian 6).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): Fixture BE untuk mengatur tanggal data uji, memajukan jam server dan jam browser, memicu eksekusi job, membaca log job, dan memulihkan ketujuh tab ke nilai default. Kemampuan membaca jumlah notifikasi per penerima dan email di inbox pengguna Total Control produk terdampak sebagai baseline (R-11, S-12).
- Waktu: tanggal data uji diatur lewat Fixture BE; jam server tidak digeser. Hook `after` mengembalikan sesi ke akun default suite (Total Control) dan memulihkan data uji. Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Fixture `fixtures/lifecycleSettings.json` belum ada dan disediakan tim FE; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tersedia.

## Test Steps

### TC-AC-LCS-543: Level tanpa pengguna berizin dilewati tanpa fallback; level lain tetap menerima

1. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: Client PT Maju Jaya di bawah Partner PT Mitra Satu dan Distributor PT Distribusi Utama, tidak ada pengguna Partner yang memiliki Update pada role "Manage allocation", pengguna Distributor dan Principal berizin tersedia, dan subscription Paid PT Maju Jaya berakhir 45 hari lagi
2. Catat baseline jumlah notifikasi pengguna Partner, Distributor berizin, dan Principal berizin
3. Picu eksekusi job Email Trigger Engine lewat Fixture BE
4. Ganti akun: login sebagai pengguna Distributor berizin `distributorUser_automated_{namaCompany}@qwertysystem.net`
5. Buka Overlay Notifikasi
6. Verifikasi jumlah notifikasi pengguna Distributor berizin bertambah tepat satu dari baseline
7. Ganti akun: login sebagai Principal berizin Update "Manage allocation"
8. Buka Overlay Notifikasi
9. Verifikasi jumlah notifikasi Principal berizin bertambah tepat satu dari baseline
10. Tunggu 5 detik tanpa memuat ulang halaman
11. Verifikasi tidak ada notifikasi tambahan untuk level Partner (tidak ada fallback; jumlah notifikasi pengguna Partner sama dengan baseline)

### TC-AC-LCS-544: Daftar penerima Plan Owner kosong di seluruh level: tahapan ditandai tanpa penerima tanpa retry

12. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: tidak ada pengguna berizin Update pada role "Manage allocation" di level Partner, Distributor, maupun Principal untuk client ini, dan subscription Paid PT Maju Jaya berakhir 45 hari lagi
13. Catat baseline jumlah notifikasi yang relevan untuk daftar penerima Plan Owner lewat kemampuan baca notifikasi Fixture BE
14. Picu eksekusi job Email Trigger Engine lewat Fixture BE
15. Baca notifikasi dan log job lewat Fixture BE
16. Verifikasi log job mencatat tahapan Plan Owner ditandai tanpa penerima
17. Verifikasi tidak ada notifikasi yang terkirim (jumlah notifikasi yang relevan sama dengan baseline)
18. Picu eksekusi job sekali lagi lewat Fixture BE
19. Verifikasi tidak ada percobaan ulang (log job tidak menambah percobaan)

### TC-AC-LCS-545: Tidak ada pengguna Total Control aktif pada produk terdampak: tidak ada email dan tahapan ditandai tanpa penerima

20. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: seluruh pengguna Total Control produk terdampak PT Maju Jaya berstatus nonaktif dan subscription Paid PT Maju Jaya berakhir 30 hari lagi
21. Catat baseline jumlah email di inbox pengguna Total Control produk terdampak PT Maju Jaya
22. Picu eksekusi job Email Trigger Engine lewat Fixture BE
23. Baca inbox pengguna Total Control produk terdampak PT Maju Jaya dan log job lewat Fixture BE
24. Verifikasi log job mencatat tahapan ditandai tanpa penerima (sekali, tanpa retry)
25. Verifikasi tidak ada email First Reminder terkirim (jumlah email sama dengan baseline)

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Atur lewat Fixture BE ..." (precondition TC), "Catat baseline ..." (langkah 2, 13, 21 sebelum pemicu job; R-11, S-12), "Ganti akun ..." (S-07), "Buka Overlay Notifikasi", "Tunggu 5 detik tanpa memuat ulang halaman" (langkah 10, jendela absence notifikasi in-app sebelum langkah 11; anchor positif: `Verifikasi` jumlah notifikasi Principal berizin bertambah satu pada langkah 9; bagian 8b butir 11, bagian 6), dan "Pulihkan ..." antar TC (S-03, S-09).
- Asersi tidak adanya notifikasi atau email (TC-AC-LCS-543 butir b, TC-AC-LCS-544, dan TC-AC-LCS-545) didahului `Verifikasi` notifikasi atau log yang membuktikan surface yang sama sudah berisi hasil dari pemicu yang sama dan memakai baseline: TC-AC-LCS-543 baseline langkah 2 dan anchor langkah 6 dan 9; TC-AC-LCS-544 baseline langkah 13 dan anchor `Verifikasi` log job langkah 16 sebelum absence notifikasi langkah 17; TC-AC-LCS-545 baseline langkah 21 dan anchor log job langkah 24 sebelum absence email langkah 25 (bagian 8b butir 2, S-12).
- Temuan untuk QA: TC-AC-LCS-543 menyebut "tidak ada notifikasi tambahan untuk level Partner" tanpa menyebut cara mengamatinya pada level yang tidak memiliki pengguna berizin (spec memakai pembacaan jumlah notifikasi lewat kemampuan baca). Mekanisme membaca log job dan notifikasi tidak didefinisikan di TC, PRD, atau LLD (S-13).
- Temuan untuk QA: TC-AC-LCS-544 tidak menyebut penerima mana yang diamati dan tidak menulis baseline; langkah baseline (langkah 13) memakai formulasi netral "notifikasi yang relevan untuk daftar penerima Plan Owner" dan dicatat sebagai langkah penghubung (S-12); penerima perlu dilengkapi di TC.
- Temuan untuk QA: Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
