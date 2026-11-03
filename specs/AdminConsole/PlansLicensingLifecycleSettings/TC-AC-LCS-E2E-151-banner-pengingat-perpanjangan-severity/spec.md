---
id: TC-AC-LCS-E2E-151-banner-pengingat-perpanjangan-severity
title: "Banner Pengingat Perpanjangan: First Reminder, Severity pada Second dan Final Reminder Before Event"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-530
  - TC-AC-LCS-531
  - TC-AC-LCS-532
coverage:
  web: automated
---

# Banner Pengingat Perpanjangan: First Reminder, Severity pada Second dan Final Reminder Before Event

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Akun tambahan (ganti akun eksplisit): Client PT Maju Jaya `clientUser_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_CLIENT_PASSWORD`; akun ini mengamati halaman License FAMS di client console. Hubungan akun itu dengan PT Maju Jaya tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Data: subscription Paid PT Maju Jaya (`Fixture.lifecycleSettings.clientMajuJaya`) yang berakhir 25, 5, atau 2 hari lagi menurut TC, diseed per TC lewat Fixture BE (precondition TC, dibuat dan dibuang per TC).
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan, S-13): Fixture BE untuk mengatur tanggal data uji, memajukan jam server dan jam browser, memicu eksekusi job, membaca log job, dan memulihkan ketujuh tab ke nilai default.
- Waktu: tanggal berakhir diatur lewat Fixture BE; jam server tidak digeser. Jam yang dimajukan dipulihkan lewat Fixture BE sesudah tiap TC dan di hook `after` suite (S-09); suite berjalan serial (`parallel: false`) karena spec ini memakai state global (jam, job, konfigurasi tab). Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Fixture `fixtures/lifecycleSettings.json` belum ada dan disediakan tim FE; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tersedia.

## Test Steps

### TC-AC-LCS-530: Banner pengingat perpanjangan tampil saat First Reminder Before Event tercapai dan hilang saat nilai diturunkan di bawah sisa hari

1. Atur lewat Fixture BE: subscription Paid PT Maju Jaya berakhir 25 hari lagi
2. Ganti akun: logout dari Total Control lalu login sebagai Client PT Maju Jaya `clientUser_automated_{namaCompany}@qwertysystem.net`
3. Buka halaman License FAMS di client console
4. Verifikasi Renewal Reminder Banner tampil (First Reminder `30`, sisa 25 hari)
5. Ganti akun: logout dari Client lalu login kembali sebagai Total Control
6. Klik tab `Client Lifecycle`
7. Ubah First Reminder Before Event dari `30` menjadi `20`
8. Klik `[Save]` dan tunggu toast sukses
9. Ganti akun: logout dari Total Control lalu login sebagai Client PT Maju Jaya `clientUser_automated_{namaCompany}@qwertysystem.net`
10. Muat ulang halaman License FAMS di client console
11. Verifikasi Renewal Reminder Banner tidak tampil (sisa 25 hari belum mencapai batas 20 hari)

### TC-AC-LCS-531: Severity banner naik saat Second Reminder Before Event tercapai

12. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: subscription Paid PT Maju Jaya berakhir 5 hari lagi
13. Buka halaman License FAMS di client console
14. Verifikasi severity banner satu tingkat di atas severity ketika hanya First Reminder tercapai (Second Reminder `7`, sisa 5 hari)
15. Ganti akun: logout dari Client lalu login kembali sebagai Total Control
16. Klik tab `Client Lifecycle`
17. Ubah Second Reminder Before Event dari `7` menjadi `3`
18. Klik `[Save]` dan tunggu toast sukses
19. Ganti akun: logout dari Total Control lalu login sebagai Client PT Maju Jaya `clientUser_automated_{namaCompany}@qwertysystem.net`
20. Muat ulang halaman License FAMS di client console
21. Verifikasi severity banner turun ke severity First Reminder (batas 3 hari belum tercapai)

### TC-AC-LCS-532: Severity banner naik lagi saat Final Reminder Before Event tercapai

22. Pulihkan ketujuh tab, jam server dan jam browser, serta data uji TC sebelumnya lewat Fixture BE, lalu atur: subscription Paid PT Maju Jaya berakhir 2 hari lagi
23. Buka halaman License FAMS di client console
24. Verifikasi severity banner pada tingkat Second Reminder (Second Reminder `7` tercapai, Final Reminder `1` belum tercapai)
25. Ganti akun: logout dari Client lalu login kembali sebagai Total Control
26. Klik tab `Client Lifecycle`
27. Ubah Final Reminder Before Event dari `1` menjadi `3`
28. Klik `[Save]` dan tunggu toast sukses
29. Ganti akun: logout dari Total Control lalu login sebagai Client PT Maju Jaya `clientUser_automated_{namaCompany}@qwertysystem.net`
30. Muat ulang halaman License FAMS di client console
31. Verifikasi severity banner naik satu tingkat (Final Reminder `3` tercapai karena sisa 2 hari)

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Ganti akun ..." (S-07), "Atur lewat Fixture BE ..." (precondition TC), "Klik tab", dan "Pulihkan ..." antar TC (S-03, S-09). Pengamat client console dijalankan sebagai ganti akun berurutan pada satu konteks, bukan konteks kedua.
- Temuan untuk QA: Pre-setup 6 menyebut akun Client tetapi tidak menyatakan akun itu milik PT Maju Jaya; spec memakai akun tersebut. Elemen Renewal Reminder Banner dan tingkat severity tidak diberi teks atau warna di TC; spec mengikuti Expected TC (S-02). Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
