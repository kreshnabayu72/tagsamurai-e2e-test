---
id: TC-AC-LCS-E2E-194-email-engine-hard-purge-gagal-dan-email-tetap-gagal
title: "Email Trigger Engine: Hard Purge Gagal dan Email Service Tetap Tidak Terjangkau Setelah Percobaan Habis"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-677
  - TC-AC-LCS-679
coverage:
  web: automated
---

# Email Trigger Engine: Hard Purge Gagal dan Email Service Tetap Tidak Terjangkau Setelah Percobaan Habis

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Data: subscription PT Maju Jaya (`Fixture.lifecycleSettings.clientMajuJaya`) pada kondisi yang diseed per TC lewat Fixture BE (precondition TC, dibuat dan dibuang per TC). Penerima email: pengguna Total Control produk terdampak PT Maju Jaya; alamatnya disediakan tim FE (tidak tertulis di Pre-setup TC).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): Fixture BE untuk mengatur tanggal data uji, memajukan jam server dan jam browser, memicu eksekusi job, membaca log job, dan memulihkan ketujuh tab ke nilai default. Kemampuan mematikan dan menyalakan layanan email dan layanan cold storage, memaksa pembuangan data client gagal, membaca status penanda pengiriman, serta mail-catcher atau inbox riil dengan baseline jumlah email per alamat (R-11, S-12). Kegagalan yang dipaksa adalah kegagalan sisi server yang tidak dapat di-intercept di browser sehingga mode tetap FE+BE.
- State global dan pemulihan: layanan email, layanan cold storage, kegagalan pembuangan data, jam server dan jam browser, serta ketujuh tab dipulihkan lewat Fixture BE sesudah tiap TC dan di hook `after` (R-08, S-09). Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Fixture `fixtures/lifecycleSettings.json` belum ada dan disediakan tim FE; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tersedia.

## Test Steps

### TC-AC-LCS-677: Hard Purge gagal dieksekusi: Hard Purge tidak ditandai selesai, email Purge Confirmation tidak dikirim, dicoba ulang pada eksekusi berikutnya

1. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: subscription Paid PT Maju Jaya berada pada akhir masa Archive (Hard Purge jatuh tempo) dengan tahapan Purge Warning dan Purge Urgent Warning sudah diproses, dan pembuangan data client dipaksa gagal
2. Catat baseline jumlah email di inbox pengguna Total Control produk terdampak PT Maju Jaya
3. Picu eksekusi job lifecycle lewat Fixture BE
4. Baca status subscription, data client, log job, dan inbox pengguna Total Control produk terdampak PT Maju Jaya
5. Verifikasi Hard Purge tidak ditandai selesai: status subscription tidak berubah
6. Verifikasi data client masih ada
7. Verifikasi log job mencatat kegagalan Hard Purge
8. Verifikasi inbox tidak menerima email Purge Confirmation (jumlah email sama dengan baseline)
9. Hapus kegagalan pembuangan data lewat Fixture BE
10. Picu eksekusi job lifecycle sekali lagi lewat Fixture BE
11. Baca status subscription dan inbox pengguna Total Control produk terdampak PT Maju Jaya
12. Verifikasi Hard Purge dieksekusi
13. Verifikasi inbox menerima tepat satu email Purge Confirmation

### TC-AC-LCS-679: Email service tetap tidak terjangkau setelah seluruh percobaan habis: tahapan ditandai gagal dan dicoba lagi pada eksekusi harian berikutnya

14. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: subscription Paid PT Maju Jaya berakhir 30 hari lagi dan First Reminder belum terkirim
15. Matikan layanan email lewat Fixture BE
16. Catat baseline jumlah email di inbox pengguna Total Control produk terdampak PT Maju Jaya
17. Picu eksekusi job Email Trigger Engine hingga seluruh percobaan ulang habis lewat Fixture BE
18. Baca log job dan inbox pengguna Total Control produk terdampak PT Maju Jaya
19. Verifikasi log job mencatat tahapan First Reminder ditandai gagal (butuh reprocessing)
20. Verifikasi tidak ada email terkirim (jumlah email sama dengan baseline)
21. Nyalakan layanan email lewat Fixture BE
22. Majukan jam server dan jam browser satu hari lewat Fixture BE
23. Picu eksekusi job Email Trigger Engine lewat Fixture BE
24. Baca log job dan inbox pengguna Total Control produk terdampak PT Maju Jaya
25. Verifikasi inbox menerima tepat satu email First Reminder (tahapan masih terbaru dan penanda belum terisi)
26. Verifikasi penanda pengiriman dicatat setelah terkirim

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Atur lewat Fixture BE ..." (precondition TC), "Matikan ... / Nyalakan ...", "Catat baseline ..." (R-11, S-12), "Picu eksekusi job ...", "Baca ...", "Majukan jam ...", dan "Pulihkan ..." antar TC (S-03, S-09).
- Temuan untuk QA: TC-AC-LCS-679 menulis "butuh reprocessing" sebagai teks log tanpa teks persis dan "penanda pengiriman dicatat setelah terkirim" tanpa cara membaca penanda itu; spec mengikuti teks TC tanpa menambah nilai (S-02, S-13). Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
