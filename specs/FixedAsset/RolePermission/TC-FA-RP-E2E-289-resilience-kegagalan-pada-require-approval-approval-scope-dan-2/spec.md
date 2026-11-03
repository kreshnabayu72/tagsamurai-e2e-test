---
id: TC-FA-RP-E2E-289-resilience-kegagalan-pada-require-approval-approval-scope-dan-2
title: "Resilience: kegagalan pada Require Approval, Approval Scope, dan Auto-Revert (2/2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-373
  - TC-FA-RP-391
  - TC-FA-RP-392
coverage:
  web: automated
---

# Resilience: kegagalan pada Require Approval, Approval Scope, dan Auto-Revert (2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Env var yang dipakai: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #3 (Rina Wulandari, Total Control; baris `Manage accounting` dan `Manage Open API` CRUD penuh), #18, dan #21 (pemegang Update Manage asset & TAG pada `IT Infrastructure: Budi Santoso`; toggle persetujuan registrasi Off). Disiapkan lewat seeding di hook `before`.
- Kemampuan teknis: Intercept permintaan di atas backend nyata (`Spectra.intercept()`, disediakan tim FE): memaksa respons 5xx dan menunda respons hingga timeout pada permintaan yang disebut langkah; intercept dilepas segera setelah pemicu selesai (S-09) dan hook `after` melepas sisa intercept. Kemampuan baca state lewat fixture BE (disediakan tim FE/BE, tanpa endpoint karangan): status tingkat akses, baris peran, nilai Require Approval, dan aturan persetujuan dibaca untuk Expected "tidak ada perubahan data" atau nilai akhir.
- State global: spec tidak mengubah state global; intercept dilepas segera dan hook `after` memulihkan data Pre-setup bila berubah.
- Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status tenant) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis kecuali dinyatakan lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-RP-373: Toggle registrasi gagal 5xx, kembali ke posisi awal

1. Klik Tab `System`, klik Role Name `Manage asset & TAG` pada section Group Role, klik node `IT Infrastructure`
2. Blokir respons update permission dengan status 5xx
3. Aktifkan toggle persetujuan registrasi
4. Verifikasi muncul toast error: `Error, failed to update permissions.`
5. Verifikasi toggle kembali OFF
6. Lepas pemblokiran respons

### TC-FA-RP-391: Confirm auto-revert gagal 5xx, dialog tetap terbuka dan cell menampilkan nilai baru sampai Cancel

7. Tunggu toast lama hilang otomatis
8. Klik Tab `System`, klik Role Name `Manage accounting` pada section Global Role
9. Hapus centang Delete pada baris Rina Wulandari
10. Blokir respons submit dengan status 5xx
11. Klik `[Remove]` pada dialog
12. Verifikasi muncul toast error: `Error, failed to update permissions.`
13. Verifikasi dialog tetap terbuka
14. Verifikasi `[Remove]` aktif kembali
15. Verifikasi cell Delete menampilkan nilai baru yang dipilih (tidak tercentang)
16. Lepas pemblokiran respons
17. Klik `[Cancel]`
18. Verifikasi cell Delete baris Rina Wulandari kembali ke nilai tersimpan (tercentang)
19. Verifikasi lewat kemampuan baca Rina Wulandari tetap Total Control

### TC-FA-RP-392: Confirm Remove baris target Total Control gagal 5xx, baris dan tingkat akses tidak berubah

20. Tunggu toast lama hilang otomatis
21. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
22. Klik `[⋯]` baris Rina Wulandari lalu `Remove`
23. Blokir respons submit dengan status 5xx
24. Klik `[Remove]`
25. Verifikasi muncul toast error: `Error, failed to remove user.`
26. Verifikasi dialog tetap terbuka
27. Verifikasi lewat kemampuan baca baris Rina Wulandari pada `Manage Open API` dan tingkat akses Total Control tidak berubah
28. Lepas pemblokiran respons
29. Klik `[Cancel]` pada dialog Remove

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-373, 391, 392).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): "Tunggu toast lama hilang otomatis" sebelum tiap toast error yang sama diasersi lagi (R-12); membuka tab, Detail Role, dan node; menutup dialog dengan `[Cancel]` (langkah 29); melepas intercept (S-09).
- Mode FE+BE dengan intercept parsial di atas backend nyata dan asersi state server (bagian 6).
- Temuan untuk QA:
  - TC-FA-RP-373 menyebut "aktifkan toggle" tanpa menyebut nama toggle; spec memakai toggle persetujuan registrasi pada node `IT Infrastructure` Detail Role `Manage asset & TAG` (Pre-setup #21).
  - TC-FA-RP-391 menulis dialog auto-revert dengan tombol `[Remove]` dan `[Cancel]` tanpa menyebut teks dialog; spec tidak mengasersi teks dialog selain keberadaannya.
