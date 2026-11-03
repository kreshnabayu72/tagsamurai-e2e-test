---
id: TC-GS-NLU-E2E-072-email-aktivasi-convert-terkirim-email-terkini-dan-kegagalan-kirim
title: "Email Aktivasi Convert: Terkirim, Email Terkini, dan Kegagalan Kirim"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-235
  - TC-GS-NLU-443
  - TC-GS-NLU-463
coverage:
  web: automated
---

# Email Aktivasi Convert: Terkirim, Email Terkini, dan Kegagalan Kirim

## Prerequisites

- Mode: FE+BE (backend nyata). Spec mengamati email aktivasi di mail-catcher dan memakai kegagalan pengiriman email sisi server.
- Aktor: Total Control Siti Nurhaliza `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD` (env `GS_TC_PASSWORD`; tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Global Settings > User > User List > sub-tab Non-Login User dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_gs-non-login-user` akun aktor diatur true oleh hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data dinamis (di-seed hook `before` lewat API, Active, Division Operations, Represented By Ahmad Fauzi): `Rani Lestari {runId}-072` (Email `rani.lestari+{runId}-072@qwertysystem.net`), `Email Baru {runId}-072` (Email `emailbaru+{runId}-072@qwertysystem.net`; diubah menjadi `emailbaru2+{runId}-072@qwertysystem.net` oleh langkah Edit), `Konversi Tujuh {runId}-072` (Email `konversitujuh+{runId}-072@qwertysystem.net`). Search `{runId}-072` menyaring tiga baris.
- Mail-catcher: inbox per alamat email dapat dibaca dan jumlah email per alamat dapat dicatat sebelum aksi (baseline; kemampuan disediakan tim FE/BE). Alamat yang dipantau: `rani.lestari+{runId}-072@qwertysystem.net`, `emailbaru+{runId}-072@qwertysystem.net`, `emailbaru2+{runId}-072@qwertysystem.net`.
- Kemampuan teknis (disediakan tim FE/BE; TC-463 menyebut "intercept" tanpa menyebut endpoint Auth): membuat pengiriman email aktivasi lewat Auth gagal untuk Convert `Konversi Tujuh {runId}-072` dan memulihkannya; kegagalan di sisi server tidak dapat di-intercept di browser sehingga mode tetap FE+BE.
- State global yang diubah: pengiriman email aktivasi dibuat gagal pada TC-463; hook `after` memulihkan pengiriman email dan menghapus lewat API ketiga record serta Login User hasil Convert.
- Seeding dan cleanup: record milik spec dibuat hook `before` lewat API dan dihapus hook `after` (hapus lewat API bila masih ada, tanpa berasumsi seeding berhasil penuh). Data Pre-setup No. 9 sampai 13 tidak diubah spec ini. Mekanisme seeding dan penghapusan disediakan tim FE/BE (lihat `suite.md`).

## Test Steps


### TC-GS-NLU-235: Email aktivasi terkirim saat Convert

1. Catat baseline jumlah email di mail-catcher untuk `rani.lestari+{runId}-072@qwertysystem.net`
2. Ketik Search `{runId}-072`, tekan Enter
3. Klik `⋯` pada baris `Rani Lestari {runId}-072` > `Convert to Login User`
4. Klik `[Convert]`
5. Tunggu aksi selesai (baris `Rani Lestari {runId}-072` hilang dari tabel Non-Login User)
6. Buka inbox email `rani.lestari+{runId}-072@qwertysystem.net` di mail-catcher
7. Verifikasi email aktivasi atau undangan diterima di `rani.lestari+{runId}-072@qwertysystem.net` (jumlah email bertambah satu dari baseline)

### TC-GS-NLU-443: Edit email sebelum Convert, undangan dikirim ke email terkini

8. Catat baseline jumlah email di mail-catcher untuk `emailbaru+{runId}-072@qwertysystem.net` dan `emailbaru2+{runId}-072@qwertysystem.net`
9. Klik `⋯` pada baris `Email Baru {runId}-072` > `Edit`
10. Ubah Email menjadi `emailbaru2+{runId}-072@qwertysystem.net`
11. Klik `[Save]`
12. Tunggu aksi selesai (popup Edit menutup)
13. Klik `⋯` pada baris `Email Baru {runId}-072` > `Convert to Login User`
14. Klik `[Convert]`
15. Tunggu aksi selesai (baris `Email Baru {runId}-072` hilang dari tabel Non-Login User)
16. Buka inbox email `emailbaru2+{runId}-072@qwertysystem.net` di mail-catcher
17. Verifikasi undangan masuk ke `emailbaru2+{runId}-072@qwertysystem.net` (jumlah email bertambah satu dari baseline)
18. Buka inbox email lama `emailbaru+{runId}-072@qwertysystem.net` di mail-catcher
19. Verifikasi jumlah email di `emailbaru+{runId}-072@qwertysystem.net` sama dengan baseline (tidak ada undangan ke email lama)

### TC-GS-NLU-463: Kegagalan pengiriman email aktivasi tidak membatalkan Convert

20. Aktifkan kondisi gagal pengiriman email aktivasi lewat Auth
21. Ketik Search `Konversi Tujuh {runId}-072`, tekan Enter
22. Klik `⋯` pada baris `Konversi Tujuh {runId}-072` > `Convert to Login User`
23. Klik `[Convert]`
24. Verifikasi toast sukses: `Success, Konversi Tujuh {runId}-072 has been converted to a login user.`
25. Klik sub-tab `Login User`
26. Ketik Search `Konversi Tujuh {runId}-072`, tekan Enter
27. Verifikasi `Konversi Tujuh {runId}-072` tampil di sub-tab Login User berstatus Pending Activation
28. Buka row action `⋯` pada baris `Konversi Tujuh {runId}-072`
29. Verifikasi aksi Resend Activation Email tersedia

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan Langkah Uji TC, tanpa awalan `Verifikasi`): langkah 1, 5, 8, 12, 15, 20.
- Search untuk menemukan baris target adalah langkah penghubung: langkah 2, 21, 26.
- Setelah `[Convert]` pada TC-235 dan TC-443 tidak ada toast yang diasersi (Expected hanya email); langkah penghubung "Tunggu aksi selesai" mendahului pindah ke mail-catcher (bagian 8b butir 8).
- Objek uji spec ini adalah email aktivasi (isi, tujuan, dan kegagalan kirim) di harness mail-catcher; TC-463 memakai kegagalan pengiriman sisi server sebagai pemicu sekaligus objek uji dalam harness yang sama.
- Temuan untuk QA:
  - TC-235 dan TC-443 diberi Automation `Manual Only` di sumber karena isi email dibaca di luar aplikasi; tetap ditulis sebagai spec dengan kemampuan baca mail-catcher disediakan tim FE/BE (hambatan teknis bukan alasan mengeluarkan TC).
  - TC-235 Expected a hanya menyebut "Email aktivasi/undangan diterima"; isi email (template) tidak diasersi.
  - TC-463 menyebut "intercept" untuk kegagalan pengiriman email lewat Auth tanpa menyebut endpoint; mekanisme disediakan tim FE/BE.
  - TC-463 Expected c menyebut "Aksi Resend Activation Email tersedia" tanpa menyebut letak aksi; spec memakai row action `⋯` di sub-tab Login User.
