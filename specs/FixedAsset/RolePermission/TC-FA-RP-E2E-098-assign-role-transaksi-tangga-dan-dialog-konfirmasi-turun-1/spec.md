---
id: TC-FA-RP-E2E-098-assign-role-transaksi-tangga-dan-dialog-konfirmasi-turun-1
title: "Assign Role Transaksi: tangga dan dialog konfirmasi turun tangga (1/2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-320
  - TC-FA-RP-321
  - TC-FA-RP-322
  - TC-FA-RP-323
coverage:
  web: automated
---

# Assign Role Transaksi: tangga dan dialog konfirmasi turun tangga (1/2)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #18, #19 (Nadia Putri Asset Admin, Oscar Pratama Monitoring & Report, Putri Wulandari Staff, Pandu Wijaya Approver pada `IT Infrastructure` sub-tab Disposal) dan pool #15 (Ahmad Fauzi tanpa role). Pemulihan state seed antar blok lewat seed API (langkah 8).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (penugasan Role Transaksi pada `IT Infrastructure` sub-tab `Disposal` (Pre-setup #19) dan Ahmad Fauzi tanpa role), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-320: Naik tangga: Assign Asset Admin ke pemegang Monitoring & Report menggantikan role lama tanpa konfirmasi

1. Klik Tab `Transaction Role`, klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
2. Klik `[+ Assign]` pada section Asset Admin
3. Centang Oscar Pratama, lalu klik `[Assign]`
4. Verifikasi tidak ada dialog konfirmasi
5. Verifikasi muncul toast sukses: `Success, Asset Admin has been assigned.`
6. Verifikasi Oscar Pratama tampil di section Asset Admin
7. Verifikasi Oscar Pratama tidak lagi di section Monitoring & Report

### TC-FA-RP-321: Naik tangga: Assign Staff ke pemegang Monitoring & Report menggantikan role lama tanpa konfirmasi

8. Pulihkan state lewat seed API: Oscar Pratama kembali Monitoring & Report, lalu muat ulang halaman dan buka kembali node `IT Infrastructure` sub-tab `Disposal`
9. Klik `[+ Assign]` pada section Staff
10. Centang Oscar Pratama, lalu klik `[Assign]`
11. Verifikasi tidak ada dialog konfirmasi
12. Verifikasi muncul toast sukses: `Success, Staff has been assigned.`
13. Verifikasi Oscar Pratama tampil di section Staff
14. Verifikasi Oscar Pratama tidak lagi di section Monitoring & Report

### TC-FA-RP-322: Turun tangga: dialog hanya mendaftar user yang turun tangga, menyebut role lama, dan Cancel membatalkan seluruh submit

15. Klik `[+ Assign]` pada section Monitoring & Report
16. Centang Nadia Putri (Asset Admin) dan Ahmad Fauzi (belum punya role)
17. Klik `[Assign]`
18. Verifikasi dialog severity warning: Title `Change Transaction Role`; Body diawali bullet `• Nadia P (currently Asset Admin)`, lalu `This will change their role for Disposal to Monitoring & Report in IT Infrastructure.`, ditutup `Are you sure you want to change it?`; tombol `[Cancel]` dan `[Change]`
19. Verifikasi Ahmad Fauzi tidak didaftar pada dialog karena tidak turun tangga
20. Klik `[Cancel]`
21. Amati toast serta section Asset Admin dan Monitoring & Report pada sub-tab `Disposal` `IT Infrastructure`
22. Verifikasi tidak ada toast
23. Verifikasi Nadia Putri tetap tampil di section Asset Admin
24. Verifikasi Ahmad Fauzi tidak ditugaskan: Ahmad Fauzi tidak ada di section Monitoring & Report

### TC-FA-RP-323: Turun tangga: Confirm menyimpan seluruh penugasan dalam satu transaksi

25. Klik `[+ Assign]` pada section Monitoring & Report
26. Centang Nadia Putri (Asset Admin) dan Ahmad Fauzi
27. Klik `[Assign]`, lalu klik `[Change]` pada dialog
28. Verifikasi muncul toast sukses: `Success, Monitoring & Report has been assigned.`
29. Verifikasi Nadia Putri tampil di section Monitoring & Report
30. Verifikasi Nadia Putri tidak lagi di section Asset Admin
31. Verifikasi Ahmad Fauzi tampil di section Monitoring & Report

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-320, TC-FA-RP-321, TC-FA-RP-322, TC-FA-RP-323).
- Langkah penghubung (S-03): membuka Tab Transaction Role, node, dan sub-tab; pemulihan state seed (langkah 8); langkah 21 (mengamati toast dan section sesudah Cancel pada TC-FA-RP-322) langsung diikuti `Verifikasi`.
- Asersi absence Oscar Pratama di Monitoring & Report (langkah 7 dan 14) didahului toast sukses server dan baris Oscar Pratama yang tampil di section tujuan sebagai anchor positif (bagian 8b butir 2).
- Asersi tambahan yang tidak ada di TC: `Verifikasi` Nadia Putri tetap tampil di section Asset Admin (sebelum asersi Ahmad Fauzi tidak ditugaskan) sebagai pembanding positif pada sub-tab yang sama (bagian 8b butir 2); Expected b TC-FA-RP-322 menyebut keduanya sebagai bagian dari satu butir.
- Temuan untuk QA:
  - TC-FA-RP-322 dan TC-FA-RP-323 memakai Ahmad Fauzi "belum punya role" dari pool #15 tanpa menyebut bahwa TC-FA-RP-323 berjalan setelah Cancel pada TC-FA-RP-322; spec menjalankan keduanya berurutan dengan state yang sama (tidak ada penugasan tersimpan setelah Cancel).
  - Copy dialog bertanda `copy usulan, PRD 12 #1` (keputusan NC-02) diasersi literal sesuai TC; bergantung pada persetujuan PM.
