---
id: TC-FA-LBL-E2E-031-create-dari-tombol-plus-pada-tab-asset-name
title: "Create dari Tombol [+] pada Tab Asset Name"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-100
  - TC-FA-LBL-502
coverage:
  web: automated
---

# Create dari Tombol [+] pada Tab Asset Name

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson), password dari `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak mengubah state global kecuali dinyatakan di bawah.
- Suffix nama bersuffix spec ini: `{runId}-031` (`{runId}` hanya digit).
- Data Pre-setup #14: popup Create/Edit Asset Name tersedia (Asset Name `Warehouse Item`, `Laptop Dell`, dan lainnya); spec memakai popup Create Asset Name tanpa menyimpannya.
- Data Pre-setup #12: label `High Priority` sudah ada di katalog Company Alpha; hanya dibaca untuk TC-FA-LBL-502.
- Label yang dibuat: `Plus Label 100 {runId}-031`.
- Label yang dibuat spec ini (nama bersuffix `{runId}-031`) dihapus di hook `after` lewat sesi API aktor.
- Kemampuan teknis (disediakan tim FE/BE, suite.md): sesi API aktor dan fixture BE untuk membaca state katalog (jumlah label bernama `High Priority`) dan menghapus label.

## Test Steps

### TC-FA-LBL-100: Create Label dari tombol [➕] pada tab Asset Name memakai modal yang sama dan label tidak otomatis terpilih

1. Klik tab `Asset Name`
2. Klik `[+ Asset Name]` untuk membuka popup Create Asset Name
3. Klik tombol `[➕]` pada field Default Label
4. Verifikasi modal `Create Label` terbuka dengan struktur, validasi, dan tombol yang sama seperti dari `[+ Label]` (Title, Label Name, Color, Live Preview, checkbox Stay, `[Clear Field]`, `[Submit]`)

### TC-FA-LBL-502: Create Label dari tombol [➕]: validasi nama duplikat dan nama kosong dieksekusi di modal yang sama

5. Hover `[Submit]` dengan Label Name dibiarkan kosong
6. Verifikasi `[Submit]` berstatus disabled dengan tooltip `Enter a label name to continue.`
7. Ketik `High Priority` di Label Name dan tunggu lebih dari 500 ms
8. Verifikasi inline error `Label name already exists` tampil
9. Verifikasi `[Submit]` berstatus disabled
10. Verifikasi tepat satu label `High Priority` di katalog (lewat fixture BE), tidak ada label ganda

### TC-FA-LBL-100: lanjutan: Create Label dari tombol [➕] dan label tidak otomatis terpilih

11. Ganti isi Label Name dengan `Plus Label 100 {runId}-031`
12. Klik `[Submit]`
13. Verifikasi toast `Success, label has been created.`
14. Buka dropdown Default Label
15. Verifikasi `Plus Label 100 {runId}-031` muncul sebagai opsi di dropdown Default Label
16. Verifikasi `Plus Label 100 {runId}-031` tidak otomatis terpilih (field Default Label tidak terisi)
17. Tekan Esc untuk menutup dropdown
18. Klik icon `[✕]` pada popup Create Asset Name

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: pembukaan modal dan Expected a TC-FA-LBL-100, lalu TC-FA-LBL-502 (validasi diblokir), lalu submit sukses TC-FA-LBL-100 (S-10); satu pembukaan modal [➕] dipakai kedua TC (prinsip 6).
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 1 (pindah ke tab Asset Name; layar awal hook adalah tab Labels), langkah 17 (menutup dropdown), dan langkah 18 (menutup popup Create Asset Name; form tidak diubah sehingga tidak ada dialog `Unsaved Changes`).
- Temuan untuk QA:
  - TC-FA-LBL-100 Post Condition "entri Create tercatat sama seperti jalur `[+ Label]`" tidak punya langkah observasi di TC dan tidak diasersi di spec ini.
  - TC-FA-LBL-502 berlabel FE Test "Need API" tetapi Expected tidak memuat respons API; spec memeriksa jumlah label lewat fixture BE.
