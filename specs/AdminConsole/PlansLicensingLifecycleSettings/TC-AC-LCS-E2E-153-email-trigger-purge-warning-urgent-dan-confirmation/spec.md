---
id: TC-AC-LCS-E2E-153-email-trigger-purge-warning-urgent-dan-confirmation
title: "Email Trigger Engine: Purge Warning, Purge Urgent Warning, dan Purge Confirmation"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-537
  - TC-AC-LCS-538
  - TC-AC-LCS-539
coverage:
  web: automated
---

# Email Trigger Engine: Purge Warning, Purge Urgent Warning, dan Purge Confirmation

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Data: subscription PT Maju Jaya (`Fixture.lifecycleSettings.clientMajuJaya`) pada kondisi milestone yang diseed per TC lewat Fixture BE (precondition TC, dibuat dan dibuang per TC). Penerima email: pengguna Total Control produk terdampak PT Maju Jaya; alamatnya disediakan tim FE (tidak tertulis di Pre-setup TC).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): Fixture BE untuk mengatur tanggal data uji, memajukan jam server dan jam browser, memicu eksekusi job, membaca log job, dan memulihkan ketujuh tab ke nilai default. Mail-catcher atau inbox riil yang dapat dibaca penguji dengan baseline jumlah email per alamat sebelum aksi (R-11, S-12).
- Waktu: tanggal data uji diatur lewat Fixture BE; jam server tidak digeser. Pemulihan: ketujuh tab dan data subscription uji dipulihkan lewat Fixture BE di hook `after`. Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Fixture `fixtures/lifecycleSettings.json` belum ada dan disediakan tim FE; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tersedia.

## Test Steps

### TC-AC-LCS-537: Email Trigger Engine mengirim email Purge Warning satu kali ke pengguna Total Control Client

1. Atur lewat Fixture BE: subscription PT Maju Jaya berstatus `Archive` dan 10 hari menuju pembersihan
2. Catat baseline jumlah email di inbox pengguna Total Control produk terdampak PT Maju Jaya
3. Picu eksekusi job Email Trigger Engine lewat Fixture BE
4. Baca inbox pengguna Total Control produk terdampak PT Maju Jaya
5. Verifikasi inbox menerima tepat satu email milestone Purge Warning (pemicu: tanggal pembersihan dikurangi 10 hari)
6. Picu eksekusi job Email Trigger Engine sekali lagi lewat Fixture BE
7. Baca inbox pengguna Total Control produk terdampak PT Maju Jaya
8. Verifikasi tidak ada email milestone tambahan (penanda pengiriman mencegah pengiriman ulang)

### TC-AC-LCS-538: Email Trigger Engine mengirim email Purge Urgent Warning satu kali ke pengguna Total Control Client

9. Atur lewat Fixture BE: subscription PT Maju Jaya berstatus `Archive` dan 2 hari menuju pembersihan, Purge Warning sudah terkirim
10. Catat baseline jumlah email di inbox pengguna Total Control produk terdampak PT Maju Jaya
11. Picu eksekusi job Email Trigger Engine lewat Fixture BE
12. Baca inbox pengguna Total Control produk terdampak PT Maju Jaya
13. Verifikasi inbox menerima tepat satu email milestone Purge Urgent Warning (pemicu: tanggal pembersihan dikurangi 2 hari)
14. Picu eksekusi job Email Trigger Engine sekali lagi lewat Fixture BE
15. Baca inbox pengguna Total Control produk terdampak PT Maju Jaya
16. Verifikasi tidak ada email milestone tambahan (penanda pengiriman mencegah pengiriman ulang)

### TC-AC-LCS-539: Email Trigger Engine mengirim email Purge Confirmation satu kali ke pengguna Total Control Client

17. Atur lewat Fixture BE: subscription PT Maju Jaya mencapai Hard Purge
18. Catat baseline jumlah email di inbox pengguna Total Control produk terdampak PT Maju Jaya
19. Picu eksekusi job Email Trigger Engine lewat Fixture BE
20. Baca inbox pengguna Total Control produk terdampak PT Maju Jaya
21. Verifikasi inbox menerima tepat satu email milestone Purge Confirmation (pemicu: setelah pembersihan permanen dieksekusi)
22. Picu eksekusi job Email Trigger Engine sekali lagi lewat Fixture BE
23. Baca inbox pengguna Total Control produk terdampak PT Maju Jaya
24. Verifikasi tidak ada email milestone tambahan (penanda pengiriman mencegah pengiriman ulang)

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Atur lewat Fixture BE ..." (precondition TC), "Catat baseline ..." (R-11, S-12), "Picu eksekusi job ...", dan "Baca inbox ..." (S-03).
- Temuan untuk QA: TC menyerahkan template email per milestone ke `email-format.md` §3 dan §3a; Expected TC hanya memuat jumlah email per milestone dan pemicunya, sehingga spec tidak mengasersi isi template (R-14). Mekanisme mengatur kondisi data, memicu job Email Trigger Engine, dan membaca inbox tidak didefinisikan di TC, PRD, atau LLD (S-13).
- Temuan untuk QA: Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
