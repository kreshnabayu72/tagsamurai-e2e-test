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
- Kemampuan teknis (disediakan tim FE/BE): Fixture BE untuk menyeed trial aktif, menghapus trial PT Cahaya Baru yang dibuat spec (juga di tengah TC agar PT Cahaya Baru tanpa trial aktif sebelum aktivasi kedua), dan memulihkan ketujuh tab ke nilai default.
- Pemulihan: trial PT Cahaya Baru yang dibuat spec dihapus dan ketujuh tab dipulihkan ke nilai default lewat Fixture BE di langkah penghubung antar TC dan hook `after`.
- Suite berjalan serial (`parallel: false`) karena spec ini memakai state global yang disebut pada butir pemulihan.
- Fixture `fixtures/lifecycle-settings.json`; nilai Pre-setup dirujuk lewat `Fixture.lifecycleSettings.<kunci>`.

## Test Steps

### TC-AC-LCS-499: Ceiling Max Trial Duration pada form Activate Trial mengikuti nilai Lifecycle Settings terbaru

1. Ubah Max Trial Duration dari `30` menjadi `10`
2. Klik `[Save]` dan tunggu toast sukses
3. Buka Allocation > Client Subscription > List Subscriptions
4. Ketik Search `PT Cahaya Baru`, tekan Enter
5. Klik `+ Activate Trial` untuk PT Cahaya Baru
6. Isi Duration dengan `10`
7. Klik `[Submit]`
8. Verifikasi Duration `10` diterima oleh validasi ceiling
9. Pulihkan PT Cahaya Baru ke keadaan tanpa trial aktif lewat Fixture BE
10. Ketik Search `PT Cahaya Baru`, tekan Enter
11. Klik `+ Activate Trial` untuk PT Cahaya Baru
12. Isi Duration dengan `11`
13. Klik `[Submit]`
14. Verifikasi field Duration menampilkan error validasi (teks error diuji pada TC modul license-allocation-subscription)
15. Verifikasi aktivasi trial PT Cahaya Baru tidak terkirim
16. Ketik Search `PT Bintang Timur`, tekan Enter
17. Buka trial aktif PT Bintang Timur
18. Verifikasi nilai trial aktif PT Bintang Timur tidak berubah (tidak retroaktif)
19. Pulihkan ketujuh tab dan hapus trial PT Cahaya Baru yang dibuat spec lewat Fixture BE, lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-500: Ceiling Max Trial Asset Quota pada form Activate Trial mengikuti nilai Lifecycle Settings terbaru

20. Ubah Max Trial Asset Quota dari `50` menjadi `20`
21. Klik `[Save]` dan tunggu toast sukses
22. Buka Allocation > Client Subscription > List Subscriptions
23. Ketik Search `PT Cahaya Baru`, tekan Enter
24. Klik `+ Activate Trial` untuk PT Cahaya Baru
25. Isi Asset Quota dengan `20`
26. Klik `[Submit]`
27. Verifikasi Asset Quota `20` diterima oleh validasi ceiling
28. Pulihkan PT Cahaya Baru ke keadaan tanpa trial aktif lewat Fixture BE
29. Ketik Search `PT Cahaya Baru`, tekan Enter
30. Klik `+ Activate Trial` untuk PT Cahaya Baru
31. Isi Asset Quota dengan `21`
32. Klik `[Submit]`
33. Verifikasi field Asset Quota menampilkan error validasi (teks error diuji pada TC modul license-allocation-subscription)
34. Verifikasi aktivasi trial PT Cahaya Baru tidak terkirim
35. Ketik Search `PT Bintang Timur`, tekan Enter
36. Buka trial aktif PT Bintang Timur
37. Verifikasi nilai trial aktif PT Bintang Timur tidak berubah (tidak retroaktif)
38. Pulihkan ketujuh tab dan hapus trial PT Cahaya Baru yang dibuat spec lewat Fixture BE, lalu buka Plans & Licensing > Lifecycle Settings

### TC-AC-LCS-501: Ceiling Max Trial Concurrent User Quota pada form Activate Trial mengikuti nilai Lifecycle Settings terbaru

39. Ubah Max Trial Concurrent User Quota dari `10` menjadi `5`
40. Klik `[Save]` dan tunggu toast sukses
41. Buka Allocation > Client Subscription > List Subscriptions
42. Ketik Search `PT Cahaya Baru`, tekan Enter
43. Klik `+ Activate Trial` untuk PT Cahaya Baru
44. Isi Concurrent User Quota dengan `5`
45. Klik `[Submit]`
46. Verifikasi Concurrent User Quota `5` diterima oleh validasi ceiling
47. Pulihkan PT Cahaya Baru ke keadaan tanpa trial aktif lewat Fixture BE
48. Ketik Search `PT Cahaya Baru`, tekan Enter
49. Klik `+ Activate Trial` untuk PT Cahaya Baru
50. Isi Concurrent User Quota dengan `6`
51. Klik `[Submit]`
52. Verifikasi field Concurrent User Quota menampilkan error validasi (teks error diuji pada TC modul license-allocation-subscription)
53. Verifikasi aktivasi trial PT Cahaya Baru tidak terkirim
54. Ketik Search `PT Bintang Timur`, tekan Enter
55. Buka trial aktif PT Bintang Timur
56. Verifikasi nilai trial aktif PT Bintang Timur tidak berubah (tidak retroaktif)

## Notes

- Langkah penghubung tanpa `Verifikasi`: "Ketik Search `<nama client>`, tekan Enter" (langkah 4, 10, 16, 23, 29, 35, 42, 48, 54) sebelum aksi atau pembukaan baris di List Subscriptions agar baris tidak bergantung pada halaman (R-16, R-23); "Pulihkan PT Cahaya Baru ke keadaan tanpa trial aktif lewat Fixture BE" (langkah 9, 28, 47) sesuai langkah 4 TC-AC-LCS-499 sampai 501 agar aktivasi kedua tidak gagal karena trial aktif hasil aktivasi pertama; "Pulihkan ketujuh tab dan hapus trial PT Cahaya Baru ... lalu buka Plans & Licensing > Lifecycle Settings" antar TC (langkah 19, 38) (S-03, S-09).
- Alasan lebih dari sekitar 35 langkah: tiga blok memakai pola yang sama (satu ceiling per field di form Activate Trial), semuanya satu topik, dan tiap blok diseed ulang oleh langkah penghubung sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA: teks error validasi ceiling tidak ada di TC ini (diuji pada TC modul license-allocation-subscription); spec hanya mengasersi bahwa error validasi tampil dan aktivasi tidak terkirim sesuai Expected TC (S-02).
- Temuan untuk QA: Post Condition TC "Tidak ada perubahan data" tidak diasersi (S-01).
