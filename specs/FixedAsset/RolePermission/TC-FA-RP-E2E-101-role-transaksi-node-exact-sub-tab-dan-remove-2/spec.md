---
id: TC-FA-RP-E2E-101-role-transaksi-node-exact-sub-tab-dan-remove-2
title: "Role Transaksi: node exact, sub-tab, dan Remove (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-330
  - TC-FA-RP-331
  - TC-FA-RP-332
  - TC-FA-RP-335
coverage:
  web: automated
---

# Role Transaksi: node exact, sub-tab, dan Remove (2/2)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_TC_PASSWORD`, `FA_TC2_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Sesi API aktor: login API untuk pelaku kedua dan pembacaan state lewat fixture BE mengikuti pernyataan di suite.md.
- Pelaku kedua (Sesi 2) pada TC-FA-RP-335: Total Control kedua Rina Wulandari (Pre-setup #3), `totalControlSecond_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC2_PASSWORD`, lewat sesi API (hanya memicu penghapusan group `Dock 1`, bukan konteks UI kedua).
- Data Pre-setup: #18 (group `Dock 1` dihapus Sesi 2), #19 (Oscar Pratama Monitoring & Report, Putri Wulandari Staff, Pandu Wijaya Approver pada `IT Infrastructure` sub-tab Disposal; Require Approval OFF pada node ini sebagai precondition TC-FA-RP-332), dan pool #15 (Ahmad Fauzi).
- Kemampuan teknis: pembacaan state data lewat fixture BE (disediakan tim FE/BE).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (penugasan Role Transaksi `IT Infrastructure` sub-tab `Disposal` (Pre-setup #19), group `Dock 1` (dipulihkan sesuai catatan "Pemulihan fixture destruktif" di TC), dan Ahmad Fauzi tanpa role), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-330: Confirm Remove Monitoring & Report: baris dihapus dan toast sukses

1. Klik Tab `Transaction Role`, klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
2. Klik `[⋯]` baris Oscar Pratama lalu `Remove`
3. Klik `[Remove]`
4. Verifikasi muncul toast sukses: `Success, Monitoring & Report has been removed.`
5. Verifikasi baris Oscar Pratama hilang dari section Monitoring & Report

### TC-FA-RP-331: Confirm Remove Staff: baris dihapus dan toast sukses

6. Klik `[⋯]` baris Putri Wulandari lalu `Remove`
7. Klik `[Remove]`
8. Verifikasi muncul toast sukses: `Success, Staff has been removed.`
9. Verifikasi baris Putri Wulandari hilang dari section Staff

### TC-FA-RP-332: Confirm Remove Approver: baris dihapus dan toast sukses

10. Klik `[⋯]` baris Pandu Wijaya lalu `Remove`
11. Klik `[Remove]`
12. Verifikasi muncul toast sukses: `Success, Approver has been removed.`
13. Verifikasi baris Pandu Wijaya hilang dari section Approver

### TC-FA-RP-335: Assign Role Transaksi pada node yang dihapus sesi lain: toast netral dan tree di-refresh

14. Klik node `Dock 1` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
15. Klik `[+ Assign]` pada section Approver, lalu centang Ahmad Fauzi
16. Sesi 2 (sesi API Total Control Rina Wulandari) menghapus group `Dock 1` hingga penghapusan tersimpan
17. Tunggu aksi selesai: Sesi 2 selesai sebelum berpindah ke Sesi 1
18. Di Sesi 1, klik `[Assign]`
19. Verifikasi muncul toast netral: `This group is no longer available.`
20. Verifikasi Sidebar Group Tree di-refresh: node `Dock 1` tidak ada
21. Verifikasi tidak ada perubahan tersimpan: Ahmad Fauzi tidak tercatat sebagai Approver (dibaca lewat fixture BE)

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-330, TC-FA-RP-331, TC-FA-RP-332, TC-FA-RP-335).
- Langkah penghubung (S-03): membuka Tab Transaction Role, node, dan sub-tab; "Tunggu aksi selesai" pada langkah 18 karena aktor berpindah sesi sesudah aksi tanpa asersi (bagian 8b butir 8). Blok TC-FA-RP-335 diletakkan terakhir karena menghapus group `Dock 1` (S-10).
- Asersi tambahan yang tidak ada di TC: tidak ada.
- Temuan untuk QA:
  - Post Condition TC-FA-RP-330, TC-FA-RP-331, dan TC-FA-RP-332 (log `Remove` tercatat, lihat Section 5) tidak memuat langkah observasi dan tidak diasersi (S-01).
  - TC-FA-RP-335 menyebut "Dua sesi" tanpa akun sesi kedua dan tanpa cara menghapus group; spec memakai Total Control kedua Pre-setup #3 lewat sesi API dan menulisnya sebagai kemampuan yang disediakan tim FE/BE (S-13).
  - Expected b TC-FA-RP-335 menyebut "tidak ada perubahan tersimpan" tanpa langkah observasi; spec membacanya lewat fixture BE.
