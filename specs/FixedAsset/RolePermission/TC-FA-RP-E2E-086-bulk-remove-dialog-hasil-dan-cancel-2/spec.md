---
id: TC-FA-RP-E2E-086-bulk-remove-dialog-hasil-dan-cancel-2
title: "Bulk Remove: dialog, hasil, dan Cancel (2/2)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-RP-304
  - TC-FA-RP-1010
coverage:
  web: automated
---

# Bulk Remove: dialog, hasil, dan Cancel (2/2)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #15 (Budi Santoso), #3 (Rina Wulandari, Total Control), #43 (Group Manager Fajar Nugroho, Kevin Susanto, Lina Marlina), #19 (Tabel Role Transaksi `IT Infrastructure`), dan #18. Rina Wulandari dan Budi Santoso memegang Global Role `Manage Open API` (disiapkan lewat seed API pada langkah 16).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (penugasan `Manage Open API` Rina Wulandari dan Budi Santoso serta tingkat akses Rina Wulandari (Total Control)), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-304: Tab Total Control, Read Only, Group Manager, System, dan tabel Role Transaksi tidak memiliki bulk action

1. Klik Tab `Total Control`
2. Verifikasi tabel Tab Total Control termuat dengan sedikitnya satu baris
3. Verifikasi tidak ada kolom Checkbox dan tidak ada `Bulk Action` pada tabel Tab Total Control
4. Klik Tab `Read Only`
5. Verifikasi tabel Tab Read Only termuat dengan sedikitnya satu baris
6. Verifikasi tidak ada kolom Checkbox dan tidak ada `Bulk Action` pada tabel Tab Read Only
7. Klik Tab `Group Manager`
8. Verifikasi tabel Tab Group Manager termuat dengan sedikitnya satu baris
9. Verifikasi tidak ada kolom Checkbox dan tidak ada `Bulk Action` pada tabel Tab Group Manager
10. Klik Tab `System`
11. Verifikasi tabel Tab System termuat dengan sedikitnya satu baris
12. Verifikasi tidak ada kolom Checkbox dan tidak ada `Bulk Action` pada tabel Tab System
13. Klik Tab `Transaction Role`, klik node `IT Infrastructure` di Sidebar Group Tree
14. Verifikasi tabel Role Transaksi pada node `IT Infrastructure` termuat dengan sedikitnya satu baris
15. Verifikasi tidak ada kolom Checkbox dan tidak ada `Bulk Action` pada tabel Role Transaksi

### TC-FA-RP-1010: Cancel pada dialog Bulk Remove D-07 mempertahankan baris, tingkat akses, dan seleksi

16. Pulihkan state lewat seed API: Rina Wulandari (Total Control) dan Budi Santoso memegang `Manage Open API`
17. Klik Tab `System`, klik Role Name `Manage Open API` pada section Global Role
18. Centang baris Rina Wulandari dan Budi Santoso
19. Klik `Bulk Action` > `Remove`
20. Verifikasi dialog Title `Remove Users` memuat bullet `Rina W (Total Control)` (format anotasi `[User Name] ([Access Level])`, copy usulan)
21. Verifikasi dialog memuat kalimat `Rina W will lose their access level as a result.`
22. Klik `[Cancel]`
23. Verifikasi dialog tertutup
24. Verifikasi kedua baris tetap ada
25. Verifikasi Bulk Action Bar dan seleksi dipertahankan
26. Klik Tab `Total Control`
27. Verifikasi Rina Wulandari tetap Total Control: baris Rina Wulandari tampil di Tab Total Control
28. Verifikasi tidak ada toast

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-304, TC-FA-RP-1010).
- Langkah penghubung (S-03): membuka tab dan Detail Role; pemulihan state seed (langkah 16).
- Asersi tambahan yang tidak ada di TC: `Verifikasi` tabel termuat dengan sedikitnya satu baris pada tiap tab (langkah 2, 5, 8, 11, dan 14) sebagai anchor positif untuk asersi absence kolom dan `Bulk Action` (bagian 8b butir 2); `Verifikasi` baris Rina Wulandari tampil di Tab Total Control (langkah 27) sebagai bukti tingkat akses tidak berubah.
- Pembagian TC lintas spec: TC-FA-RP-299 dan TC-FA-RP-300 (Bulk Remove oleh Manage global user & role (Update)) ada di spec 302; TC-FA-RP-295 sampai TC-FA-RP-298 dan TC-FA-RP-301 ada di spec 085.
- Temuan untuk QA:
  - TC-FA-RP-304 menyebut Tab Total Control, Read Only, Group Manager, dan System tanpa menyebut baris pembanding; spec memakai "sedikitnya satu baris" sebagai anchor generik.
  - TC-FA-RP-1010 Expected b menyebut "Rina Wulandari tetap Total Control" tanpa surface; spec mengamatinya di Tab Total Control.
