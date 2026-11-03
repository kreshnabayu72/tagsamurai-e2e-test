---
id: TC-FA-RP-E2E-290-resilience-download-gagal
title: "Resilience: Download gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-523
  - TC-FA-RP-571
  - TC-FA-RP-591
  - TC-FA-RP-665
  - TC-FA-RP-751
  - TC-FA-RP-764
coverage:
  web: automated
---

# Resilience: Download gagal

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Env var yang dipakai: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #36 (Tab Total Control terisi), #37 (Tab Read Only terisi), #38 (Tab Group Manager terisi), #39 (Detail Role `Manage files` terisi), #42 (Changelog Tab Total Control), dan #18. Disiapkan lewat seeding di hook `before`; spec tidak mengubah data tersebut.
- Kemampuan teknis: Intercept permintaan di atas backend nyata (`Spectra.intercept()`, disediakan tim FE): memaksa respons 5xx dan menunda respons hingga timeout pada permintaan yang disebut langkah; intercept dilepas segera setelah pemicu selesai (S-09) dan hook `after` melepas sisa intercept. Permintaan yang di-intercept adalah permintaan ekspor (download) dengan respons 5xx.
- State global: spec tidak mengubah state global; intercept dilepas segera setelah toast diasersi dan hook `after` melepas sisa intercept.
- Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group, status tenant) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup yang diubah dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis kecuali dinyatakan lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-RP-523: Download Tab Total Control gagal, toast error dengan nama berkas tanpa extension

1. Klik Tab `Total Control`
2. Blokir respons download dengan status 5xx
3. Klik ikon Download lalu `Download as CSV`
4. Verifikasi muncul toast error: `Error, failed to download Role-Permission-Total-Control.`
5. Lepas pemblokiran respons download

### TC-FA-RP-571: Download Tab Group Manager gagal, toast error dengan nama berkas tanpa extension

6. Tunggu toast lama hilang otomatis
7. Klik Tab `Group Manager`
8. Blokir respons download dengan status 5xx
9. Klik ikon Download lalu `Download as CSV`
10. Verifikasi muncul toast error: `Error, failed to download Role-Permission-Group-Manager.`
11. Lepas pemblokiran respons download

### TC-FA-RP-591: Download Tab System gagal, toast error

12. Tunggu toast lama hilang otomatis
13. Klik Tab `System`
14. Blokir respons download dengan status 5xx
15. Klik ikon Download lalu `Download as CSV`
16. Verifikasi muncul toast error: `Error, failed to download Role-Permission-System.`
17. Lepas pemblokiran respons download

### TC-FA-RP-665: Download Detail Role gagal, toast error dengan nama berkas tanpa extension

18. Tunggu toast lama hilang otomatis
19. Klik Role Name `Manage files` pada section Group Role
20. Klik `All Groups` di Sidebar Group Tree
21. Blokir respons download dengan status 5xx
22. Klik ikon Download lalu `Download as CSV`
23. Verifikasi muncul toast error: `Error, failed to download Role-Permission-Manage-Files.`
24. Lepas pemblokiran respons download

### TC-FA-RP-751: Download Modal Changelog gagal, toast error dengan nama berkas tanpa extension

25. Tunggu toast lama hilang otomatis
26. Klik Tab `Total Control`
27. Klik ikon Changelog pada toolbar
28. Blokir respons download dengan status 5xx
29. Klik ikon Download lalu `Download as CSV`
30. Verifikasi muncul toast error: `Error, failed to download Changelog-Role-Permission-Total-Control.`
31. Lepas pemblokiran respons download
32. Tutup modal Changelog

### TC-FA-RP-764: Download Changelog gagal: toast error dengan nama berkas dan pola toast PRD `[File Name]`

33. Tunggu toast lama hilang otomatis
34. Klik Tab `Total Control`
35. Klik ikon Changelog pada toolbar
36. Blokir respons download dengan status 5xx
37. Klik ikon Download lalu `Download as CSV`
38. Verifikasi muncul toast error: `Error, failed to download Changelog-Role-Permission-Total-Control.` (pola `Error, failed to download [File Name].`)
39. Lepas pemblokiran respons download

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-523, 571, 591, 665, 751, 764).
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): "Tunggu toast lama hilang otomatis" sebelum tiap toast error yang sama diasersi lagi (R-12); membuka tab, Detail Role, Sidebar Group Tree, dan modal Changelog; menutup modal Changelog; melepas intercept (S-09).
- Mode FE+BE dengan intercept parsial di atas backend nyata (bagian 6): hanya permintaan ekspor yang dipaksa gagal dan toast diasersi; spec tidak mengasersi berkas terunduh.
- Kelas b (resilience) memuat enam TC Download gagal pada enam permukaan; Download berhasil ada di spec Download masing-masing permukaan.
- Spec melewati sekitar 35 langkah (39 langkah). Semua blok satu kelas harness (resilience, Download gagal) dengan langkah yang sama di tiap permukaan. Tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna; memecahnya hanya mengulang hook dan navigasi.
- Temuan untuk QA:
  - TC-FA-RP-751 dan TC-FA-RP-764 mengasersi toast yang sama (`Error, failed to download Changelog-Role-Permission-Total-Control.`) pada permukaan yang sama (Modal Changelog Tab Total Control); spec menjalankan keduanya terpisah dengan toast lama dibuang di antaranya.
  - Expected b TC-FA-RP-764 memuat contoh varian Tab System (`Error, failed to download Changelog-Role-Permission-System.`) tanpa langkah untuk varian itu; spec hanya mengasersi toast Tab Total Control dan menyebut pola toast.
  - TC-FA-RP-751 dan TC-FA-RP-764 menyebut Precondition Pre-setup #24 (`Company Changelog`); spec tetap memakai tenant akun default karena kegagalan Download tidak bergantung pada tenant.
