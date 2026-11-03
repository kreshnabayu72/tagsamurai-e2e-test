---
id: TC-FA-RP-E2E-287-resilience-kegagalan-5xx-dan-timeout-pada-remove-dan-bulk-2
title: "Resilience: kegagalan 5xx dan timeout pada Remove dan Bulk Remove (2/2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-302
  - TC-FA-RP-303
  - TC-FA-RP-333
  - TC-FA-RP-334
coverage:
  web: automated
---

# Resilience: kegagalan 5xx dan timeout pada Remove dan Bulk Remove (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Env var yang dipakai: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #15 (Budi Santoso dan Budi Setiawan memegang `Manage Open API`; Ahmad Fauzi tanpa penugasan Role Transaksi), #18, dan #19 (Putri Wulandari sebagai Staff pada `Disposal` di `IT Infrastructure`). Disiapkan lewat seeding di hook `before`.
- Kemampuan teknis: Intercept permintaan di atas backend nyata (`Spectra.intercept()`, disediakan tim FE): memaksa respons 5xx dan menunda respons hingga timeout pada permintaan yang disebut langkah; intercept dilepas segera setelah pemicu selesai (S-09) dan hook `after` melepas sisa intercept.
- State global: spec tidak mengubah state global; intercept dilepas segera dan hook `after` memulihkan data Pre-setup bila berubah.
- Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status tenant) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis kecuali dinyatakan lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-RP-302: Bulk Remove gagal 5xx, dialog tetap terbuka dan seleksi dipertahankan

1. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
2. Centang baris Budi Santoso dan Budi Setiawan
3. Klik `Bulk Action` > `Remove`
4. Blokir respons submit dengan status 5xx
5. Klik `[Remove]`
6. Verifikasi muncul toast error: `Error, failed to remove user.`
7. Verifikasi dialog tetap terbuka
8. Verifikasi seleksi dipertahankan untuk retry
9. Lepas pemblokiran respons
10. Klik `[Cancel]` pada dialog Bulk Remove
11. Klik `Unselect All`

### TC-FA-RP-303: Bulk Remove timeout jaringan, dialog tetap terbuka dan seleksi dipertahankan

12. Tunggu toast lama hilang otomatis
13. Centang baris Budi Santoso dan Budi Setiawan
14. Klik `Bulk Action` > `Remove`
15. Tunda respons hingga timeout
16. Klik `[Remove]`
17. Verifikasi muncul toast: `Connection problem. Please try again.`
18. Verifikasi dialog tetap terbuka
19. Verifikasi seleksi dipertahankan
20. Lepas penundaan respons
21. Klik `[Cancel]` pada dialog Bulk Remove

### TC-FA-RP-333: Remove Role Transaksi gagal 5xx, dialog tetap terbuka

22. Tunggu toast lama hilang otomatis
23. Klik Tab `Transaction Role`, klik node `IT Infrastructure` di Sidebar Group Tree lalu sub-tab `Disposal`
24. Klik `[⋯]` baris Putri Wulandari lalu `Remove`
25. Blokir respons submit dengan status 5xx
26. Klik `[Remove]`
27. Verifikasi muncul toast error: `Error, failed to remove Staff.` (pola `Error, failed to remove [Role Name].`)
28. Verifikasi dialog tetap terbuka
29. Verifikasi `[Remove]` aktif kembali
30. Lepas pemblokiran respons
31. Klik `[Cancel]` pada dialog Remove

### TC-FA-RP-334: Assign Role Transaksi gagal 5xx, popup tetap terbuka

32. Tunggu toast lama hilang otomatis
33. Klik `[+ Assign]` pada section Staff
34. Centang Ahmad Fauzi
35. Blokir respons submit dengan status 5xx
36. Klik `[Assign]`
37. Verifikasi muncul toast error: `Error, failed to assign Staff.`
38. Verifikasi popup tetap terbuka
39. Verifikasi seleksi Ahmad Fauzi dipertahankan
40. Lepas pemblokiran respons
41. Klik `[Cancel]` pada popup Assign

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-302, 303, 333, 334).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): "Tunggu toast lama hilang otomatis" sebelum tiap toast error yang sama diasersi lagi (R-12); `Unselect All` sesudah menutup dialog (langkah 11, S-09); menutup dialog dan popup dengan `[Cancel]` (langkah 10, 21, 31, 41); membuka tab, Detail Role, node, dan sub-tab; melepas intercept (S-09).
- Mode FE+BE dengan intercept parsial di atas backend nyata (bagian 6).
- Spec melewati sekitar 35 langkah (41 langkah). Semua blok satu kelas harness (resilience 5xx dan timeout) pada Bulk Remove, Remove Role Transaksi, dan Assign Role Transaksi. Tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; memecahnya hanya mengulang hook dan navigasi.
- Temuan untuk QA:
  - TC-FA-RP-302 dan TC-FA-RP-303 tidak menyebut cara menutup dialog atau menghapus seleksi sesudahnya; spec menutup dengan `[Cancel]` dan `Unselect All`.
  - TC-FA-RP-333 dan TC-FA-RP-334 menyebut penamaan toast berdasarkan Role Name `Staff`; spec mengasersi copy literal `Staff` sesuai TC.
