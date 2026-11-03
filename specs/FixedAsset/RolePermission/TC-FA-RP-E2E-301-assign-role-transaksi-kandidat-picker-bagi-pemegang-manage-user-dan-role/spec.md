---
id: TC-FA-RP-E2E-301-assign-role-transaksi-kandidat-picker-bagi-pemegang-manage-user-dan-role
title: "Assign Role Transaksi: kandidat picker bagi pemegang Manage user & role"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-RP-318
coverage:
  web: automated
---

# Assign Role Transaksi: kandidat picker bagi pemegang Manage user & role

## Prerequisites

- Mode: FE+BE.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Halaman: Fixed Asset > Settings > Role & Permission pada tab awal Total Control dibuka hook `beforeEach` suite (lihat suite.md).
- Akun aktor: Manage global user & role (Update) Hendra Wijaya (Pre-setup #6), `murGlobal_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_MUR_GLOBAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Environment variable: `FA_MUR_GLOBAL_PASSWORD`. Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example` (lihat suite.md).
- Data Pre-setup: #18, #19 (Seed Role Transaksi `IT Infrastructure` sub-tab Disposal), #3 (Rina Wulandari, Total Control), #12 (Maya Anggraeni, Read Only), dan pool #15 (Ahmad Fauzi). Tidak ada data yang diubah spec ini (hanya membaca picker).

## Test Steps

### TC-FA-RP-318: Picker Role Transaksi bagi pemegang Manage user & role: kandidat Total Control dan Read Only disaring

1. Klik node `IT Infrastructure` di Sidebar Group Tree pada Tab Transaction Role, lalu klik sub-tab `Disposal`
2. Klik `[+ Assign]` pada section Asset Admin
3. Ketik Search `Ahmad Fauzi`, tekan Enter
4. Verifikasi Ahmad Fauzi ada di daftar picker
5. Ganti isi kotak search dengan `Rina Wulandari`, tekan Enter
6. Verifikasi empty state `No results found` tampil sehingga Rina Wulandari tidak ada di daftar picker
7. Ganti isi kotak search dengan `Maya Anggraeni`, tekan Enter
8. Verifikasi empty state `No results found` tampil sehingga Maya Anggraeni tidak ada di daftar picker
9. Tutup popup Assign

## Notes

- Sumber TC: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md` (TC-FA-RP-318).
- Langkah penghubung (S-03): membuka node dan sub-tab; menutup popup Assign.
- Urutan pencarian dibalik terhadap TC (Ahmad Fauzi lebih dulu sebagai anchor positif pada picker yang sama sebelum asersi absence, bagian 8b butir 2); hasil pencarian Rina Wulandari dan Maya Anggraeni berupa empty state `No results found` yang menjadi anchor sah.
- Pembagian TC lintas spec: TC-FA-RP-317 ada di spec 096; TC-FA-RP-1123 dan TC-FA-RP-1124 ada di spec 097.
- Temuan untuk QA:
  - TC-FA-RP-318 tidak menyebut apakah aktor pemegang Manage global user & role dikecualikan dari picker; hanya tiga kandidat yang diasersi sesuai TC.
