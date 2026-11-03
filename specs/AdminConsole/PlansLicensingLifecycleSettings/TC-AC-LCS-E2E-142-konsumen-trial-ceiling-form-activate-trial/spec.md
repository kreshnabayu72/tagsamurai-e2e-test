---
id: TC-AC-LCS-E2E-142-konsumen-trial-ceiling-form-activate-trial
title: "Konsumen Trial: Ceiling Max Trial Duration, Asset Quota, dan Concurrent User Quota pada Form Activate Trial"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LCS-499
  - TC-AC-LCS-500
  - TC-AC-LCS-501
coverage:
  web: automated
---

# Konsumen Trial: Ceiling Max Trial Duration, Asset Quota, dan Concurrent User Quota pada Form Activate Trial

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (nama tampil `Andi Wijaya`, Principal), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`).
- Hook suite (`suite.md`): `beforeEach` memulihkan ketujuh tab ke nilai default (Trial 30, 50, 10, OFF, 7, 1; Free 365; License Timing 24, 2, 2; Client Lifecycle 45, 30, 7, 1, 30, 30, 10, 2, 730; Recycle Bin 30; Approval 3; System Limits 1000, 1000, 1000, 50, 10000, 20), jam server dan jam browser, General Settings (Date Format `dd MMM yy`, Time Format 24 jam, Time Zone UTC), dan intercept, lalu membuka Plans & Licensing > Lifecycle Settings dengan tab Trial Settings aktif; hook `before` suite menyetel flag Guided Tooltip halaman ini true dan menyatakan sesi API aktor.
- Data: Client PT Cahaya Baru (`Fixture.lifecycleSettings.clientCahayaBaru`) tanpa trial aktif dan Client PT Bintang Timur (`Fixture.lifecycleSettings.clientBintangTimur`) memiliki trial aktif yang diaktifkan sebelum perubahan; keduanya diseed lewat Fixture BE di hook `before` spec ini. Nilai default tab Trial Settings: Max Trial Duration `30`, Max Trial Asset Quota `50`, Max Trial Concurrent User Quota `10`.
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk menyeed trial aktif, menghapus trial PT Cahaya Baru yang dibuat spec, dan memulihkan ketujuh tab ke nilai default.
- Pemulihan: trial PT Cahaya Baru yang dibuat spec dihapus dan ketujuh tab dipulihkan ke nilai default lewat Fixture BE di langkah penghubung antar TC dan hook `after`.
- Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Fixture `fixtures/lifecycleSettings.json` belum ada dan disediakan tim FE; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>` setelah tersedia.

## Test Steps

### TC-AC-LCS-499: Ceiling Max Trial Duration pada form Activate Trial mengikuti nilai Lifecycle Settings terbaru

1. Ubah Max Trial Duration dari `30` menjadi `10`
2. Klik `[Save]` dan tunggu toast sukses
3. Buka Allocation > Client Subscription > List Subscriptions
4. Klik `+ Activate Trial` untuk PT Cahaya Baru
5. Isi Duration dengan `10`
6. Klik `[Submit]`
7. Verifikasi Duration `10` diterima oleh validasi ceiling
8. Klik `+ Activate Trial` untuk PT Cahaya Baru
9. Isi Duration dengan `11`
10. Klik `[Submit]`
11. Verifikasi Duration `11` tidak diterima: field menampilkan error validasi dan aktivasi tidak terkirim (teks error diuji pada TC modul license-allocation-subscription)
12. Buka trial aktif PT Bintang Timur
13. Verifikasi nilai trial aktif PT Bintang Timur tidak berubah (tidak retroaktif)
14. Pulihkan ketujuh tab dan hapus trial PT Cahaya Baru yang dibuat spec lewat Fixture BE, lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-500: Ceiling Max Trial Asset Quota pada form Activate Trial mengikuti nilai Lifecycle Settings terbaru

15. Ubah Max Trial Asset Quota dari `50` menjadi `20`
16. Klik `[Save]` dan tunggu toast sukses
17. Buka Allocation > Client Subscription > List Subscriptions
18. Klik `+ Activate Trial` untuk PT Cahaya Baru
19. Isi Asset Quota dengan `20`
20. Klik `[Submit]`
21. Verifikasi Asset Quota `20` diterima oleh validasi ceiling
22. Klik `+ Activate Trial` untuk PT Cahaya Baru
23. Isi Asset Quota dengan `21`
24. Klik `[Submit]`
25. Verifikasi Asset Quota `21` tidak diterima: field menampilkan error validasi dan aktivasi tidak terkirim (teks error diuji pada TC modul license-allocation-subscription)
26. Buka trial aktif PT Bintang Timur
27. Verifikasi nilai trial aktif PT Bintang Timur tidak berubah (tidak retroaktif)
28. Pulihkan ketujuh tab dan hapus trial PT Cahaya Baru yang dibuat spec lewat Fixture BE, lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-501: Ceiling Max Trial Concurrent User Quota pada form Activate Trial mengikuti nilai Lifecycle Settings terbaru

29. Ubah Max Trial Concurrent User Quota dari `10` menjadi `5`
30. Klik `[Save]` dan tunggu toast sukses
31. Buka Allocation > Client Subscription > List Subscriptions
32. Klik `+ Activate Trial` untuk PT Cahaya Baru
33. Isi Concurrent User Quota dengan `5`
34. Klik `[Submit]`
35. Verifikasi Concurrent User Quota `5` diterima oleh validasi ceiling
36. Klik `+ Activate Trial` untuk PT Cahaya Baru
37. Isi Concurrent User Quota dengan `6`
38. Klik `[Submit]`
39. Verifikasi Concurrent User Quota `6` tidak diterima: field menampilkan error validasi dan aktivasi tidak terkirim (teks error diuji pada TC modul license-allocation-subscription)
40. Buka trial aktif PT Bintang Timur
41. Verifikasi nilai trial aktif PT Bintang Timur tidak berubah (tidak retroaktif)

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Pulihkan ketujuh tab dan hapus trial PT Cahaya Baru ... lalu buka Plans & Licensing > Lifecycle Settings" antar TC (S-03, S-09).
- Alasan lebih dari sekitar 35 langkah: tiga blok memakai pola yang sama (satu ceiling per field di form Activate Trial), semuanya satu topik, dan tiap blok diseed ulang oleh langkah penghubung sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA: TC mengulang `+ Activate Trial` untuk PT Cahaya Baru sesudah Duration (atau kuota) yang valid disubmit; TC tidak menyebut apakah aktivasi pertama sudah membuat trial aktif yang menghalangi aktivasi kedua. Spec mengikuti urutan TC.
- Temuan untuk QA: teks error validasi ceiling tidak ada di TC ini (diuji pada TC modul license-allocation-subscription); spec hanya mengasersi bahwa error validasi tampil dan aktivasi tidak terkirim sesuai Expected TC (S-02).
- Temuan untuk QA: Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
