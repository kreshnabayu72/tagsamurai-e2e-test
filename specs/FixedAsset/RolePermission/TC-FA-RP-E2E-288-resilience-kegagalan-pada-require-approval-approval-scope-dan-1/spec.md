---
id: TC-FA-RP-E2E-288-resilience-kegagalan-pada-require-approval-approval-scope-dan-1
title: "Resilience: kegagalan pada Require Approval, Approval Scope, dan Auto-Revert (1/2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-351
  - TC-FA-RP-352
  - TC-FA-RP-353
  - TC-FA-RP-358
coverage:
  web: automated
---

# Resilience: kegagalan pada Require Approval, Approval Scope, dan Auto-Revert (1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Env var yang dipakai: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #18, #19 (Approver Pandu Wijaya pada `Disposal` di `IT Infrastructure`; Require Approval Off di semua node), dan #20 (sub-tab `Transfer` pada `IT Infrastructure` dengan Require Approval On, aturan OR, Approval Scope `Both`). Disiapkan lewat seeding di hook `before` dan langkah 10 dan 17.
- Kemampuan teknis: Intercept permintaan di atas backend nyata (`Spectra.intercept()`, disediakan tim FE): memaksa respons 5xx dan menunda respons hingga timeout pada permintaan yang disebut langkah; intercept dilepas segera setelah pemicu selesai (S-09) dan hook `after` melepas sisa intercept.
- State global: spec tidak mengubah state global; nilai Require Approval dan aturan pada `IT Infrastructure` dipulihkan ke Pre-setup #19 dan #20 di hook `after`.
- Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status tenant) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis kecuali dinyatakan lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-RP-351: Toggle gagal 5xx, toggle kembali ke posisi awal

1. Klik Tab `Transaction Role`, klik node `IT Infrastructure` di Sidebar Group Tree lalu sub-tab `Disposal`
2. Tahan respons update permission dan siapkan status 5xx saat dilepas
3. Aktifkan toggle
4. Verifikasi toggle sempat berubah (ON) selama proses
5. Verifikasi toggle Disabled selama proses
6. Lepas tahanan respons dengan status 5xx
7. Verifikasi muncul toast error: `Error, failed to update permissions.`
8. Verifikasi toggle kembali OFF
9. Lepas intercept permintaan update permission

### TC-FA-RP-352: Radio gagal 5xx, radio kembali ke nilai asal

10. Pulihkan state lewat seed API: toggle `Require Approval for Disposal` ON dengan radio `Any approver (OR)` pada `IT Infrastructure`, lalu muat ulang halaman, klik Tab `Transaction Role`, klik node `IT Infrastructure` lalu sub-tab `Disposal`
11. Tunggu toast lama hilang otomatis
12. Blokir respons update aturan dengan status 5xx
13. Pilih radio `All approvers (AND)`
14. Verifikasi muncul toast error: `Error, failed to update approval rule.`
15. Verifikasi radio kembali ke `Any approver (OR)`
16. Lepas pemblokiran respons

### TC-FA-RP-353: Toggle timeout jaringan, toggle kembali dan toast koneksi

17. Pulihkan state lewat seed API: toggle `Require Approval for Disposal` OFF pada `IT Infrastructure`, lalu muat ulang halaman, klik Tab `Transaction Role`, klik node `IT Infrastructure` lalu sub-tab `Disposal`
18. Tunggu toast lama hilang otomatis
19. Tunda respons update permission hingga timeout
20. Aktifkan toggle
21. Verifikasi muncul toast: `Connection problem. Please try again.`
22. Verifikasi toggle kembali OFF
23. Lepas penundaan respons

### TC-FA-RP-358: Approval Scope gagal 5xx, kembali ke nilai awal

24. Tunggu toast lama hilang otomatis
25. Klik node `IT Infrastructure` lalu sub-tab `Transfer`
26. Blokir respons update aturan dengan status 5xx
27. Pilih opsi `Origin only`
28. Verifikasi muncul toast error: `Error, failed to update approval rule.`
29. Verifikasi RadioGroup Approval Scope kembali ke `Both`
30. Lepas pemblokiran respons

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-351, 352, 353, 358).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): pemulihan state seed dan memuat ulang halaman (langkah 10 dan 17); "Tunggu toast lama hilang otomatis" sebelum tiap toast error yang sama diasersi lagi (R-12); membuka tab, node, dan sub-tab; melepas intercept (S-09).
- Langkah penahanan respons pada TC-FA-RP-351 (Tahan respons lalu 5xx saat dilepas) menggantikan "Blokir respons" supaya Expected a (toggle sempat berubah dan Disabled selama proses) teramati sebelum Expected b dan c (bagian 8b butir 5).
- Mode FE+BE dengan intercept parsial di atas backend nyata (bagian 6).
- Temuan untuk QA:
  - TC-FA-RP-352 mensyaratkan toggle ON dengan radio OR pada `IT Infrastructure` sub-tab `Disposal`, sedangkan Pre-setup #19 menyatakan Require Approval Off di semua node; spec menyiapkan kondisi itu lewat seeding.
  - TC-FA-RP-358 menyebut nilai awal Approval Scope `Both` tanpa menyebut efek ke Require Approval sub-tab `Transfer`; spec memakai Pre-setup #20.
