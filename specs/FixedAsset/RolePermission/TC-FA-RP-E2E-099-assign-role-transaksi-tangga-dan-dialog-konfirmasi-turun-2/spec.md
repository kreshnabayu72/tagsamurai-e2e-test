---
id: TC-FA-RP-E2E-099-assign-role-transaksi-tangga-dan-dialog-konfirmasi-turun-2
title: "Assign Role Transaksi: tangga dan dialog konfirmasi turun tangga (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-324
  - TC-FA-RP-325
  - TC-FA-RP-1117
coverage:
  web: automated
---

# Assign Role Transaksi: tangga dan dialog konfirmasi turun tangga (2/2)

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Total Control Siti Rahmawati (Pre-setup #2), `totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #18, #19 (Nadia Putri Asset Admin, Putri Wulandari Staff pada `IT Infrastructure` sub-tab Disposal) dan Nadia Putri sebagai Asset Admin pada `IT Infrastructure` sub-tab `Damaged` (precondition TC-FA-RP-324, disiapkan lewat seed API di hook `before`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): pulihkan data Pre-setup yang diubah spec ini ke kondisi Tabel Data Uji Pre-setup TC (penugasan Role Transaksi pada `IT Infrastructure` sub-tab `Disposal` dan `Damaged` (Nadia Putri tidak lagi Approver)), mengikuti catatan "Pemulihan fixture destruktif" di TC; pemulihan dijamin fixture backend yang disediakan tim FE/BE (lihat suite.md).

## Test Steps

### TC-FA-RP-324: Jenis transaksi tanpa Staff bertangga dua tingkat: turun dari Asset Admin ke Monitoring & Report memicu dialog

1. Klik Tab `Transaction Role`, klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Damaged`
2. Klik `[+ Assign]` pada section Monitoring & Report
3. Centang Nadia Putri, lalu klik `[Assign]`
4. Verifikasi dialog `Change Transaction Role` tampil dengan bullet `• Nadia P (currently Asset Admin)`, teks `This will change their role for Damaged to Monitoring & Report in IT Infrastructure.`, dan penutup `Are you sure you want to change it?`; tombol `[Cancel]` dan `[Change]`
5. Verifikasi section Asset Admin, Monitoring & Report, dan Approver tampil serta section Staff tidak ada pada sub-tab `Damaged`
6. Klik `[Cancel]`

### TC-FA-RP-325: Approver berada di luar tangga dan dapat dipegang bersamaan dengan role tangga

7. Klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
8. Klik `[+ Assign]` pada section Approver
9. Centang Nadia Putri (Asset Admin), lalu klik `[Assign]`
10. Verifikasi muncul toast sukses: `Success, Approver has been assigned.`
11. Verifikasi Nadia Putri tampil di section Approver
12. Verifikasi Nadia Putri tetap di section Asset Admin

### TC-FA-RP-1117: Turun tangga >=2 user: dialog gabungan mendaftar semua user turun tangga dan pertanyaan penutup bentuk jamak

13. Klik `[+ Assign]` pada section Monitoring & Report
14. Centang Nadia Putri (Asset Admin) dan Putri Wulandari (Staff)
15. Klik `[Assign]`
16. Verifikasi dialog severity warning: Title `Change Transaction Roles`; Body memuat bullet `• Nadia P (currently Asset Admin)` dan `• Putri W (currently Staff)`, lalu `This will change their role for Disposal to Monitoring & Report in IT Infrastructure.`, ditutup `Are you sure you want to change them?`; tombol `[Cancel]` dan `[Change]`
17. Verifikasi hanya satu dialog yang tampil untuk kedua user
18. Klik `[Cancel]`

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-324, TC-FA-RP-325, TC-FA-RP-1117).
- Langkah penghubung (S-03): membuka Tab Transaction Role, node, dan sub-tab; menutup dialog dengan `[Cancel]` (langkah 6 dan 18) agar blok berikutnya tidak berjalan di atas dialog terbuka (S-09).
- Asersi tambahan yang tidak ada di TC: section lain tampil pada sub-tab `Damaged` (langkah 5) sebagai anchor positif untuk asersi absence section Staff (bagian 8b butir 2); TC-FA-RP-324 Expected b menyatakan section Staff tidak ada.
- Temuan untuk QA:
  - TC-FA-RP-325 tidak menyebut apakah Nadia Putri sebelumnya Approver; spec mengasumsikan bukan Approver sebelum Assign.
  - Copy dialog bertanda `copy usulan, PRD 12 #1` (keputusan NC-02) diasersi literal sesuai TC; bergantung pada persetujuan PM.
