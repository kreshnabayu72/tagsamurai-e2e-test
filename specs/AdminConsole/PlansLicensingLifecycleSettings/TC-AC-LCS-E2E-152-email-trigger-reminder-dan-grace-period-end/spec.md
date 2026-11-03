---
id: TC-AC-LCS-E2E-152-email-trigger-reminder-dan-grace-period-end
title: "Email Trigger Engine: First Reminder, Second Reminder, Final Reminder, dan Grace Period End"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-533
  - TC-AC-LCS-534
  - TC-AC-LCS-535
  - TC-AC-LCS-536
coverage:
  web: automated
---

# Email Trigger Engine: First Reminder, Second Reminder, Final Reminder, dan Grace Period End

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Data: subscription PT Maju Jaya (`Fixture.lifecycleSettings.clientMajuJaya`) pada kondisi milestone yang diseed per TC lewat Fixture BE (precondition TC, dibuat dan dibuang per TC). Penerima email: pengguna Total Control produk terdampak PT Maju Jaya; alamatnya disediakan tim FE (tidak tertulis di Pre-setup TC).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): Fixture BE untuk mengatur tanggal data uji, memajukan jam server dan jam browser, memicu eksekusi job, membaca log job, dan memulihkan ketujuh tab ke nilai default. Mail-catcher atau inbox riil yang dapat dibaca penguji dengan baseline jumlah email per alamat sebelum aksi (R-11, S-12).
- Waktu: tanggal data uji diatur lewat Fixture BE; jam server tidak digeser. Pemulihan: ketujuh tab dan data subscription uji dipulihkan lewat Fixture BE di hook `after`. Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Fixture `fixtures/lifecycleSettings.json` belum ada dan disediakan tim FE; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tersedia.

## Test Steps

### TC-AC-LCS-533: Email Trigger Engine mengirim email First Reminder satu kali ke pengguna Total Control Client

1. Atur lewat Fixture BE: subscription Paid PT Maju Jaya berakhir 30 hari lagi
2. Catat baseline jumlah email di inbox pengguna Total Control produk terdampak PT Maju Jaya
3. Picu eksekusi job Email Trigger Engine lewat Fixture BE
4. Baca inbox pengguna Total Control produk terdampak PT Maju Jaya
5. Verifikasi inbox menerima tepat satu email milestone First Reminder (pemicu: tanggal kedaluwarsa dikurangi 30 hari)
6. Picu eksekusi job Email Trigger Engine sekali lagi lewat Fixture BE
7. Baca inbox pengguna Total Control produk terdampak PT Maju Jaya
8. Verifikasi tidak ada email milestone tambahan (penanda pengiriman mencegah pengiriman ulang)

### TC-AC-LCS-534: Email Trigger Engine mengirim email Second Reminder satu kali ke pengguna Total Control Client

9. Atur lewat Fixture BE: subscription Paid PT Maju Jaya berakhir 7 hari lagi dan First Reminder sudah terkirim
10. Catat baseline jumlah email di inbox pengguna Total Control produk terdampak PT Maju Jaya
11. Picu eksekusi job Email Trigger Engine lewat Fixture BE
12. Baca inbox pengguna Total Control produk terdampak PT Maju Jaya
13. Verifikasi inbox menerima tepat satu email milestone Second Reminder (pemicu: tanggal kedaluwarsa dikurangi 7 hari)
14. Picu eksekusi job Email Trigger Engine sekali lagi lewat Fixture BE
15. Baca inbox pengguna Total Control produk terdampak PT Maju Jaya
16. Verifikasi tidak ada email milestone tambahan (penanda pengiriman mencegah pengiriman ulang)

### TC-AC-LCS-535: Email Trigger Engine mengirim email Final Reminder satu kali ke pengguna Total Control Client

17. Atur lewat Fixture BE: subscription Paid PT Maju Jaya berakhir 1 hari lagi dan First serta Second Reminder sudah terkirim
18. Catat baseline jumlah email di inbox pengguna Total Control produk terdampak PT Maju Jaya
19. Picu eksekusi job Email Trigger Engine lewat Fixture BE
20. Baca inbox pengguna Total Control produk terdampak PT Maju Jaya
21. Verifikasi inbox menerima tepat satu email milestone Final Reminder (pemicu: tanggal kedaluwarsa dikurangi 1 hari)
22. Picu eksekusi job Email Trigger Engine sekali lagi lewat Fixture BE
23. Baca inbox pengguna Total Control produk terdampak PT Maju Jaya
24. Verifikasi tidak ada email milestone tambahan (penanda pengiriman mencegah pengiriman ulang)

### TC-AC-LCS-536: Email Trigger Engine mengirim email Grace Period End satu kali ke pengguna Total Control Client

25. Atur lewat Fixture BE: subscription PT Maju Jaya berstatus `Grace` dan hari ke-30 masa tenggang tercapai
26. Catat baseline jumlah email di inbox pengguna Total Control produk terdampak PT Maju Jaya
27. Picu eksekusi job Email Trigger Engine lewat Fixture BE
28. Baca inbox pengguna Total Control produk terdampak PT Maju Jaya
29. Verifikasi inbox menerima tepat satu email milestone Grace Period End (pemicu: tanggal kedaluwarsa ditambah 30 hari (akhir masa tenggang))
30. Picu eksekusi job Email Trigger Engine sekali lagi lewat Fixture BE
31. Baca inbox pengguna Total Control produk terdampak PT Maju Jaya
32. Verifikasi tidak ada email milestone tambahan (penanda pengiriman mencegah pengiriman ulang)

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Atur lewat Fixture BE ..." (precondition TC), "Catat baseline ..." (R-11, S-12), "Picu eksekusi job ...", dan "Baca inbox ..." (S-03).
- Temuan untuk QA: TC menyerahkan template email per milestone ke `email-format.md` §3 dan §3a; Expected TC hanya memuat jumlah email per milestone dan pemicunya, sehingga spec tidak mengasersi isi template (R-14). Mekanisme mengatur kondisi data, memicu job Email Trigger Engine, dan membaca inbox tidak didefinisikan di TC, PRD, atau LLD (S-13).
- Temuan untuk QA: Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
