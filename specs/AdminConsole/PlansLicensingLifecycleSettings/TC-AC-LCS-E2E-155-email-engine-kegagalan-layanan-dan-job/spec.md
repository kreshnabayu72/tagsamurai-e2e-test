---
id: TC-AC-LCS-E2E-155-email-engine-kegagalan-layanan-dan-job
title: "Email Trigger Engine: Email Service Gagal dan Kegagalan Cold Storage pada Transisi Grace ke Archive"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-LCS-546
  - TC-AC-LCS-676
coverage:
  web: automated
---

# Email Trigger Engine: Email Service Gagal dan Kegagalan Cold Storage pada Transisi Grace ke Archive

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Data: subscription PT Maju Jaya (`Fixture.lifecycleSettings.clientMajuJaya`) pada kondisi yang diseed per TC lewat Fixture BE (precondition TC, dibuat dan dibuang per TC). Penerima email: pengguna Total Control produk terdampak PT Maju Jaya; alamatnya disediakan tim FE (tidak tertulis di Pre-setup TC).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): Fixture BE untuk mengatur tanggal data uji, memajukan jam server dan jam browser, memicu eksekusi job, membaca log job, dan memulihkan ketujuh tab ke nilai default. Kemampuan mematikan dan menyalakan layanan email dan layanan cold storage, memaksa pembuangan data client gagal, membaca status penanda pengiriman, serta mail-catcher atau inbox riil dengan baseline jumlah email per alamat (R-11, S-12). Kegagalan yang dipaksa adalah kegagalan sisi server yang tidak dapat di-intercept di browser sehingga mode tetap FE+BE.
- State global dan pemulihan: layanan email, layanan cold storage, kegagalan pembuangan data, jam server dan jam browser, serta ketujuh tab dipulihkan lewat Fixture BE sesudah tiap TC dan di hook `after` (R-08, S-09). Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Fixture `fixtures/lifecycle-settings.json`; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>`.

## Test Steps

### TC-AC-LCS-546: Email service tidak terjangkau: retry terbatas, penanda hanya setelah terkirim, transisi lifecycle tidak menunggu email

1. Atur lewat Fixture BE: subscription Paid PT Maju Jaya berakhir hari ini (T-0) dan First Reminder belum terkirim
2. Matikan layanan email lewat Fixture BE
3. Catat baseline jumlah email di inbox pengguna Total Control produk terdampak PT Maju Jaya
4. Picu eksekusi job Email Trigger Engine lewat Fixture BE
5. Buka Allocation > Client Subscription > List Subscriptions
6. Ketik Search `PT Maju Jaya`, tekan Enter
7. Verifikasi status subscription PT Maju Jaya berubah menjadi `Expired` meski email gagal
8. Baca log job lewat Fixture BE
9. Verifikasi log job mencatat percobaan ulang terbatas
10. Nyalakan layanan email lewat Fixture BE
11. Picu eksekusi job Email Trigger Engine sekali lagi lewat Fixture BE
12. Baca inbox pengguna Total Control produk terdampak PT Maju Jaya
13. Verifikasi inbox menerima tepat satu email
14. Verifikasi penanda pengiriman dicatat setelah terkirim

### TC-AC-LCS-676: Pemindahan data ke cold storage gagal pada transisi Grace ke Archive: transisi tidak dikomit dan dicoba ulang pada eksekusi berikutnya

15. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: subscription Paid PT Maju Jaya berstatus `Grace` dan batas Grace Period Duration (`30` hari) tepat terlewati
16. Matikan layanan cold storage lewat Fixture BE
17. Picu eksekusi job lifecycle lewat Fixture BE
18. Buka Allocation > Client Subscription > List Subscriptions
19. Ketik Search `PT Maju Jaya`, tekan Enter
20. Verifikasi status subscription PT Maju Jaya tetap `Grace`
21. Baca log job lewat Fixture BE
22. Verifikasi log job mencatat kegagalan pemindahan data ke cold storage
23. Nyalakan layanan cold storage lewat Fixture BE
24. Picu eksekusi job lifecycle sekali lagi lewat Fixture BE
25. Muat ulang halaman List Subscriptions
26. Ketik Search `PT Maju Jaya`, tekan Enter
27. Verifikasi status subscription PT Maju Jaya `Archive`

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Atur lewat Fixture BE ..." (precondition TC), "Matikan ... / Nyalakan ...", "Catat baseline ..." (R-11, S-12), "Picu eksekusi job ...", "Baca ...", "Ketik Search `PT Maju Jaya`, tekan Enter" sebelum tiap `Verifikasi` status baris (langkah 6, 19, 26; R-16, bagian 8b butir 13, R-23), dan "Pulihkan ..." antar TC (S-03, S-09).
- Temuan untuk QA: TC-AC-LCS-546 menulis "percobaan ulang terbatas" tanpa jumlah percobaan dan "penanda pengiriman dicatat setelah terkirim" tanpa cara membaca penanda itu; spec mengikuti teks TC tanpa menambah nilai (S-02, S-13). TC-AC-LCS-676 menulis kegagalan pemindahan data ke cold storage tanpa teks log persis (S-02). Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
