---
id: TC-FA-RP-E2E-286-resilience-kegagalan-5xx-dan-timeout-pada-remove-dan-bulk-1
title: "Resilience: kegagalan 5xx dan timeout pada Remove dan Bulk Remove (1/2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-207
  - TC-FA-RP-213
  - TC-FA-RP-239
  - TC-FA-RP-284
  - TC-FA-RP-285
coverage:
  web: automated
---

# Resilience: kegagalan 5xx dan timeout pada Remove dan Bulk Remove (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Env var yang dipakai: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #15 (Ahmad Fauzi berstatus Total Control pada TC-FA-RP-207 dan Read Only pada TC-FA-RP-213), #39 (Detail Role Global Role `Manage Open API` terisi: Budi Santoso memegang `Manage Open API`; TC-FA-RP-284 dan 285), #43 (Kevin Susanto Group Manager di `Data Center`), dan #18. Disiapkan lewat seeding di hook `before` dan langkah 10.
- Kemampuan teknis: Intercept permintaan di atas backend nyata (`Spectra.intercept()`, disediakan tim FE): memaksa respons 5xx dan menunda respons hingga timeout pada permintaan yang disebut langkah; intercept dilepas segera setelah pemicu selesai (S-09) dan hook `after` melepas sisa intercept.
- State global: spec mengubah tingkat akses Ahmad Fauzi (Remove sukses pada retry TC-FA-RP-207 dan TC-FA-RP-213); dipulihkan pada langkah 10 dan di hook `after`.
- Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status tenant) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis kecuali dinyatakan lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-RP-207: Remove Total Control gagal 5xx, dialog tetap terbuka dan Remove aktif kembali

1. Klik `[⋯]` baris Ahmad Fauzi lalu `Remove`
2. Blokir respons submit dengan status 5xx
3. Klik `[Remove]`
4. Verifikasi muncul toast error: `Error, failed to remove Total Control.`
5. Verifikasi dialog tetap terbuka
6. Verifikasi `[Remove]` aktif kembali
7. Lepas pemblokiran respons
8. Klik `[Remove]` lagi
9. Verifikasi muncul toast sukses: `Success, Total Control has been removed.`
10. Pulihkan state lewat seed API: Ahmad Fauzi berstatus Read Only, lalu muat ulang halaman

### TC-FA-RP-213: Remove Read Only gagal 5xx, dialog tetap terbuka dan Remove aktif kembali

11. Tunggu toast lama hilang otomatis
12. Klik Tab `Read Only`
13. Klik `[⋯]` baris Ahmad Fauzi lalu `Remove`
14. Blokir respons submit dengan status 5xx
15. Klik `[Remove]`
16. Verifikasi muncul toast error: `Error, failed to remove Read Only.`
17. Verifikasi dialog tetap terbuka
18. Verifikasi `[Remove]` aktif kembali
19. Lepas pemblokiran respons
20. Klik `[Remove]` lagi
21. Verifikasi muncul toast sukses: `Success, Read Only has been removed.`

### TC-FA-RP-239: Remove Group Manager gagal 5xx, dialog tetap terbuka

22. Tunggu toast lama hilang otomatis
23. Klik Tab `Group Manager`
24. Klik `[⋯]` baris Kevin Susanto di `Data Center` lalu `Remove`
25. Blokir respons submit dengan status 5xx
26. Klik `[Remove]`
27. Verifikasi muncul toast error: `Error, failed to remove Group Manager.`
28. Verifikasi dialog tetap terbuka
29. Verifikasi `[Remove]` aktif kembali
30. Lepas pemblokiran respons
31. Klik `[Cancel]` pada dialog Remove

### TC-FA-RP-284: Remove baris peran gagal 5xx, dialog tetap terbuka

32. Tunggu toast lama hilang otomatis
33. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
34. Klik `[⋯]` baris Budi Santoso lalu `Remove`
35. Blokir respons submit dengan status 5xx
36. Klik `[Remove]`
37. Verifikasi muncul toast error: `Error, failed to remove user.`
38. Verifikasi dialog tetap terbuka
39. Verifikasi `[Remove]` aktif kembali
40. Lepas pemblokiran respons
41. Klik `[Cancel]` pada dialog Remove

### TC-FA-RP-285: Remove baris peran timeout jaringan, dialog tetap terbuka

42. Tunggu toast lama hilang otomatis
43. Klik `[⋯]` baris Budi Santoso lalu `Remove`
44. Tunda respons hingga timeout
45. Klik `[Remove]`
46. Verifikasi muncul toast: `Connection problem. Please try again.`
47. Verifikasi dialog tetap terbuka untuk retry
48. Lepas penundaan respons
49. Klik `[Cancel]` pada dialog Remove

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-207, 213, 239, 284, 285).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): pemulihan state seed (langkah 10); "Tunggu toast lama hilang otomatis" sebelum tiap toast error yang sama diasersi lagi (R-12); menutup dialog dengan `[Cancel]` (langkah 31, 41, 49, S-09); membuka tab dan Detail Role; melepas intercept (S-09).
- Mode FE+BE dengan intercept parsial di atas backend nyata (bagian 6): TC-FA-RP-207 dan TC-FA-RP-213 mengasersi retry yang berhasil di server.
- Spec melewati sekitar 35 langkah (49 langkah). Semua blok satu kelas harness (resilience 5xx dan timeout) pada kelompok Remove yang sama. Tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; memecahnya hanya mengulang hook dan navigasi.
- Temuan untuk QA:
  - TC-FA-RP-239 dan TC-FA-RP-285 tidak menyebut cara menutup dialog atau langkah sesudahnya; spec melepas intercept dan menutup dialog dengan `[Cancel]`.
  - TC-FA-RP-285 tidak menyebut apakah dialog Remove masih memuat target setelah timeout; spec hanya mengasersi dialog tetap terbuka.
