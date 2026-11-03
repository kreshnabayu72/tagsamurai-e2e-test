---
id: TC-FA-RP-E2E-284-resilience-kegagalan-5xx-dan-timeout-pada-assign-serta-edit-1
title: "Resilience: kegagalan 5xx dan timeout pada Assign serta Edit (1/2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-201
  - TC-FA-RP-202
  - TC-FA-RP-203
  - TC-FA-RP-204
  - TC-FA-RP-230
coverage:
  web: automated
---

# Resilience: kegagalan 5xx dan timeout pada Assign serta Edit (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Env var yang dipakai: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #15 (Ahmad Fauzi dan Budi Santoso tanpa tingkat akses sebagai kandidat Assign) dan #18 (group `Helpdesk`). Disiapkan lewat seeding di hook `before` dan langkah 12 dan 36.
- Kemampuan teknis: Intercept permintaan di atas backend nyata (`Spectra.intercept()`, disediakan tim FE): memaksa respons 5xx dan menunda respons hingga timeout pada permintaan yang disebut langkah; intercept dilepas segera setelah pemicu selesai (S-09) dan hook `after` melepas sisa intercept.
- State global: spec mengubah tingkat akses Ahmad Fauzi (Total Control dan Read Only pada retry sukses); dipulihkan pada langkah 12 dan 36 serta di hook `after`.
- Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status tenant) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis kecuali dinyatakan lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-RP-201: Assign Total Control gagal 5xx, popup tetap terbuka dengan seleksi dipertahankan

1. Klik `[+ Assign]` di Tab Total Control
2. Centang Ahmad Fauzi
3. Blokir respons submit dengan status 5xx
4. Klik `[Assign]`
5. Verifikasi muncul toast error: `Error, failed to assign Total Control.`
6. Verifikasi popup tetap terbuka
7. Verifikasi Ahmad Fauzi tetap tercentang
8. Verifikasi `[Assign]` aktif kembali
9. Lepas pemblokiran respons
10. Klik `[Assign]` lagi
11. Verifikasi muncul toast sukses: `Success, Total Control has been assigned.`
12. Pulihkan state lewat seed API: Ahmad Fauzi tanpa tingkat akses

### TC-FA-RP-202: Assign Total Control timeout jaringan, popup tetap terbuka dan toast koneksi

13. Tunggu toast lama hilang otomatis
14. Klik `[+ Assign]` di Tab Total Control
15. Centang Ahmad Fauzi
16. Tunda respons submit hingga timeout
17. Klik `[Assign]`
18. Verifikasi muncul toast: `Connection problem. Please try again.`
19. Verifikasi popup tetap terbuka
20. Verifikasi seleksi Ahmad Fauzi dipertahankan untuk retry
21. Lepas penundaan respons
22. Klik `[Cancel]` pada popup Assign

### TC-FA-RP-203: Assign Read Only gagal 5xx, popup tetap terbuka dengan seleksi dipertahankan

23. Tunggu toast lama hilang otomatis
24. Klik Tab `Read Only`
25. Klik `[+ Assign]` di Tab Read Only
26. Centang Ahmad Fauzi
27. Blokir respons submit dengan status 5xx
28. Klik `[Assign]`
29. Verifikasi muncul toast error: `Error, failed to assign Read Only.`
30. Verifikasi popup tetap terbuka
31. Verifikasi Ahmad Fauzi tetap tercentang
32. Verifikasi `[Assign]` aktif kembali
33. Lepas pemblokiran respons
34. Klik `[Assign]` lagi
35. Verifikasi muncul toast sukses: `Success, Read Only has been assigned.`
36. Pulihkan state lewat seed API: Ahmad Fauzi tanpa tingkat akses

### TC-FA-RP-204: Assign Read Only timeout jaringan, popup tetap terbuka dan toast koneksi

37. Tunggu toast lama hilang otomatis
38. Klik `[+ Assign]` di Tab Read Only
39. Centang Ahmad Fauzi
40. Tunda respons submit hingga timeout
41. Klik `[Assign]`
42. Verifikasi muncul toast: `Connection problem. Please try again.`
43. Verifikasi popup tetap terbuka
44. Verifikasi seleksi Ahmad Fauzi dipertahankan untuk retry
45. Lepas penundaan respons
46. Klik `[Cancel]` pada popup Assign

### TC-FA-RP-230: Assign Group Manager gagal 5xx, popup tetap terbuka dengan seleksi dipertahankan

47. Tunggu toast lama hilang otomatis
48. Klik Tab `Group Manager`
49. Klik `[+ Assign]`
50. Pilih group `Helpdesk`
51. Centang Budi Santoso
52. Blokir respons submit dengan status 5xx
53. Klik `[Assign]`
54. Verifikasi muncul toast error: `Error, failed to assign Group Manager.`
55. Verifikasi popup tetap terbuka
56. Verifikasi Budi Santoso tetap tercentang
57. Verifikasi field Group tetap `Helpdesk`
58. Lepas pemblokiran respons
59. Klik `[Cancel]` pada popup Assign

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-201, 202, 203, 204, 230).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): pemulihan state seed (langkah 12 dan 36); "Tunggu toast lama hilang otomatis" sebelum tiap toast error yang sama diasersi lagi (R-12); menutup popup dengan `[Cancel]` (langkah 22, 46, 59, S-09); membuka tab dan memilih group; melepas intercept (S-09).
- Mode FE+BE dengan intercept parsial di atas backend nyata (bagian 6): spec mengasersi toast dan state popup serta langkah retry yang berhasil di server.
- Spec melewati sekitar 35 langkah (59 langkah). Semua blok satu kelas harness (resilience 5xx dan timeout) pada kelompok Assign yang sama. Tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; memecahnya hanya mengulang hook dan navigasi.
- Temuan untuk QA:
  - TC-FA-RP-202 dan TC-FA-RP-204 tidak menyebut cara menutup popup atau langkah sesudah timeout; spec melepas penundaan lalu menutup popup dengan `[Cancel]`.
  - TC-FA-RP-201 dan TC-FA-RP-203 menyebut `[Assign]` aktif kembali tanpa menyebut spinner; spec hanya mengasersi state `[Assign]` aktif.
