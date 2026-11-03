---
id: TC-FA-CAID-E2E-096-registrasi-hapus-draft-dan-counter-setelah-save
title: "Registrasi Aset: Increment Tidak Dipakai Ulang Setelah Hapus Draft dan Counter Setelah Save"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-265
  - TC-FA-CAID-266
coverage:
  web: automated
---

# Registrasi Aset: Increment Tidak Dipakai Ulang Setelah Hapus Draft dan Counter Setelah Save

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Company Register (Pre-setup No 24; pola `totalControl_automated_{namaCompany}@qwertysystem.net`, email tidak tertulis di Pre-setup TC, disediakan tim FE), password `Spectra.env.FA_REGISTER_TC_PASSWORD` (nama usulan; didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun kedua (ganti akun eksplisit untuk TC-FA-CAID-266): Total Control Company Alpha `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson, Pre-setup No 1), password `Spectra.env.FA_TC_PASSWORD`; akun ini sekaligus akun default suite.
- Layar awal: hook `beforeEach` suite membuka tab Custom Asset ID; spec ini berawal di Fixed Asset > Assets > Registration, jadi langkah pertama membuka halaman itu.
- Data Pre-setup: Company Register (No 24): hook `before` men-seed konfigurasi B1 tanpa aset; master data Division `Human Resources`, Asset Name `ThinkPad T490` (`T490`), Group `Jakarta Office` (`JKT`), Category `Laptop` (`LAP`), Brand `Lenovo`. Company Alpha baseline B1 (No 10) dan aset A1 sampai A5 (No 11) dipulihkan hook `beforeEach` suite.
- Data Dinamis: aset Draft hasil registrasi (Dinamis No 7, aset keempat setelah hapus Draft); dibersihkan oleh seed reset Company.
- Kemampuan teknis: sesi API aktor dan seed API (suite.md).
- State global: aset dan konfigurasi Company Register serta Company Alpha diubah (Separator `- (Dash)`); hook `after` memulihkan Company Register ke B1 tanpa aset, Company Alpha ke baseline B1 dan aset A1 sampai A5, dan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CAID-265: Nomor Increment aset yang dihapus tidak dipakai ulang

1. Buka Fixed Asset > Assets > Registration
2. Klik `[+ Quick Register]`, pilih Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`, lalu klik `[Save as Draft]`; ulangi sampai tiga aset Draft terdaftar
3. Pilih `[Delete Draft]` pada aset ber-Asset ID `JKT/LAP/T490/0000/2`
4. Konfirmasi pada dialog `Delete Draft Asset`
5. Verifikasi toast sukses `Success, draft asset has been deleted.` tampil
6. Verifikasi baris `JKT/LAP/T490/0000/2` hilang
7. Klik `[+ Quick Register]`, pilih Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`, lalu klik `[Save as Draft]` sekali lagi
8. Verifikasi aset baru terbit `JKT/LAP/T490/0000/4`
9. Verifikasi nomor 2 tidak dipakai ulang: tidak ada aset ber-Asset ID `JKT/LAP/T490/0000/2`

### TC-FA-CAID-266: Save yang me-recompute aset tidak mengubah counter: registrasi berikutnya melanjutkan nomor

10. Logout dari akun Total Control Company Register
11. Login sebagai Total Control Company Alpha (password dari `Spectra.env.FA_TC_PASSWORD`)
12. Buka Fixed Asset > Settings > Asset Master > Custom Asset ID
13. Pilih Separator `- (Dash)` lalu klik `[Save]`
14. Verifikasi toast sukses `Success, Custom Asset ID configuration has been updated.` tampil
15. Buka Fixed Asset > Assets > Registration, klik `[+ Quick Register]`, pilih Asset Name `ThinkPad T490`, Brand `Lenovo`, Model/Type `T490`, Group `Jakarta Office`, Condition `Normal`, lalu klik `[Save as Draft]`
16. Verifikasi aset baru terbit `JKT-LAP-T490-0000-6` (melanjutkan setelah Increment 5 milik A5)
17. Buka Fixed Asset > Assets > All Assets
18. Verifikasi A1 sampai A3 tetap berakhiran 1, 2, 3

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Pembagian TC lintas spec: TC-FA-CAID-261, 263, dan 264 ada di spec 084 (`TC-FA-CAID-E2E-084-registrasi-approval-fallback-dan-counter`).
- Langkah penghubung: langkah 1 (buka halaman), 3 dan 4 (aksi hapus Draft yang hasilnya diasersi pada langkah 5), 10 dan 11 (ganti akun eksplisit ke Company Alpha, S-07), 12, 17 (buka halaman).
- Temuan untuk QA:
  - Email akun Total Control Company Register tidak tertulis di Pre-setup TC.
  - Asersi A1 sampai A3 pada TC-FA-CAID-266 hanya memeriksa akhiran Increment; nilai lengkap Asset ID mengikuti Separator `- (Dash)`.
  - Post Condition tidak diasersi karena tidak punya langkah observasi.
