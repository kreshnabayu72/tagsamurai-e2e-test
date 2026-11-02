---
id: TC-FA-GRP-E2E-023-role-matrix-gating-checkbox-bulk-aktor-d-parsial-dan-tanpa-d
title: "Role Matrix Gating Checkbox: Disabled pada Node Tanpa D, Kolom Checkbox Hidden Tanpa D, dan Baris Disabled Tidak Ikut Select All"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-62
  - TC-FA-GRP-63
  - TC-FA-GRP-1123
coverage:
  web: automated
---

# Role Matrix Gating Checkbox: Disabled pada Node Tanpa D, Kolom Checkbox Hidden Tanpa D, dan Baris Disabled Tidak Ikut Select All

## Prerequisites

- Mode: FE+BE.
- Role yang diuji (spec ditulis per blok role karena langkah tiap role berbeda):

| Role | Akun (Pre-setup) | Password | Blok langkah |
|---|---|---|---|
| Manage Group D parsial level 1 (R+D di Head Office, R saja di Branch Office) (TC-FA-GRP-62, 1123) | No 24 (email perlu data dari tim FE/QA) | `Spectra.env.FA_MGDP_PASSWORD` | langkah 1 sampai 12 |
| Manage Group R+U scope Region West (TC-FA-GRP-63) | No 6 `manageGroupUpdate_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MGRU_PASSWORD` | langkah 13 sampai 16 |

- Login di hook `before` spec ini sebagai Manage Group D parsial; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip `fa-settings-groups` untuk kedua akun disetel `seen` di hook `before` spec ini dan dipulihkan di hook `after` (kemampuan disediakan tim FE/BE); hook suite hanya menyetel akun aktor default suite.
- Data Pre-setup (hanya dibaca, tidak diubah): pohon group baku Tabel A (Pre-setup No 9) dengan Head Office (checkbox enabled bagi aktor D parsial) dan Branch Office (checkbox disabled bagi aktor D parsial). Spec ini tidak menjalankan Delete; seleksi dibersihkan pada langkah 12.
- Kemampuan teknis: fixture BE dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### Role Manage Group D parsial (TC-FA-GRP-62)

1. Verifikasi checkbox baris Head Office enabled
2. Verifikasi checkbox baris Branch Office tetap tampil namun disabled (abu-abu)
3. Hover checkbox baris Branch Office
4. Verifikasi tooltip `You don't have permission to do this.` tampil

### Role Manage Group D parsial (TC-FA-GRP-1123)

5. Klik checkbox header
6. Verifikasi hanya baris dengan checkbox enabled yang tercentang, termasuk Head Office
7. Verifikasi Branch Office tetap unchecked dan disabled
8. Verifikasi counter seleksi hanya menghitung baris dengan checkbox enabled
9. Verifikasi checkbox header berstatus checked karena seluruh baris enabled di halaman aktif tercentang (baris Disabled tidak dihitung)
10. Klik Select All ([N] records)
11. Verifikasi [N] pada Select All tidak menyertakan baris Disabled dan Branch Office tidak ikut terpilih
12. Hapus seleksi dengan Unselect All

### Role Manage Group R+U (TC-FA-GRP-63)

13. Logout dari akun Manage Group D parsial
14. Login sebagai Manage Group R+U dengan `Spectra.env.FA_MGRU_PASSWORD`
15. Buka Fixed Asset > Settings > Groups
16. Verifikasi tabel menampilkan baris group (anchor permukaan) dan kolom Checkbox tidak dirender sama sekali, termasuk checkbox header

## Notes

- Spec 16 langkah, di bawah batas sekitar 35 langkah.
- Langkah penghubung (S-03): langkah 12 (Unselect All sebelum ganti akun, S-09), langkah 13 sampai 15 (ganti akun eksplisit dan membuka layar), langkah 16 memuat anchor positif absence kolom Checkbox (8b butir 2; tidak ada di Expected TC).
- Urutan TC dalam spec: 62, 1123, 63.
- Temuan untuk QA:
  - Email akun Manage Group R+U pada Pre-setup No 6 ditulis dengan elipsis; spec melengkapinya dengan pola `{namaCompany}@qwertysystem.net`.
  - TC-FA-GRP-1123 tidak menyebut nilai [N] atau counter; spec membandingkan dengan jumlah baris enabled.
