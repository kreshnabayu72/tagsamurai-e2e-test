---
id: TC-FA-LBL-E2E-022-color-picker-create-validasi-kode-hex-tidak-valid-v04-bagian-2
title: "Color Picker Create: Validasi Kode Hex Tidak Valid (V-04) (bagian 2/2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-57
  - TC-FA-LBL-58
coverage:
  web: automated
---

# Color Picker Create: Validasi Kode Hex Tidak Valid (V-04) (bagian 2/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec. Fixture `fixtures/asset-labeling.json` (`Fixture.assetLabeling.*`) memuat identitas akun tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Env var `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak mengubah state global kecuali dinyatakan di bawah.
- Spec ini tidak membuat atau menyimpan label (semua submit diblokir validasi); tidak ada cleanup data.

## Test Steps

1. Klik `[+ Label]`

### TC-FA-LBL-57: Kode hex 6 digit tanpa awalan # ditolak real-time dengan V-04

2. Isi Label Name `Hex Check 57`
3. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
4. Kosongkan kolom Hex lalu ketik `3B82F6`
5. Verifikasi inline error `Invalid color format` tampil di dalam overlay
6. Verifikasi Swatch Trigger dan Live Preview tetap berlatar `#3B82F6` (warna valid terakhir)
7. Verifikasi `[Submit]` berstatus disabled walau Label Name terisi

### TC-FA-LBL-58: Setelah kode hex tidak valid, mengetik kode valid menghapus error dan mengaktifkan Submit

8. Kosongkan kolom Hex lalu ketik `#3B82F6` (warna valid sebagai pembersih error)
9. Kosongkan kolom Hex lalu ketik `#12345`
10. Ganti isi Label Name dengan `Hex Recover 58`
11. Ketik ulang kolom Hex menjadi `#10B981`
12. Verifikasi inline error `Invalid color format` hilang
13. Verifikasi Live Preview berlatar `#10B981`
14. Verifikasi `[Submit]` berstatus enabled
15. Tekan Esc untuk menutup overlay
16. Klik icon `[✕]`
17. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` dan `[Leave]` tampil
18. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Satu pembukaan modal dan satu pembukaan overlay dipakai TC-FA-LBL-57 dan 58 (prinsip 6); Label Name TC-FA-LBL-57 diisi sebelum overlay dibuka (urutan TC), sedangkan pada TC-FA-LBL-58 Label Name diganti isinya saat overlay terbuka sesuai Langkah TC-FA-LBL-58. Error `Invalid color format` identik antar-TC, jadi sebelum TC-FA-LBL-58 kolom Hex diisi `#3B82F6` sebagai pembersih (R-12; aksi tanpa `Verifikasi`, S-03).
- Langkah penghubung (tanpa awalan Verifikasi, S-03): pembersih `#3B82F6` sebelum TC-FA-LBL-58, serta langkah 15 dan 18 (menutup overlay dan modal; form dirty, jadi ditutup lewat dialog `Unsaved Changes` dengan `[Leave]`, S-08).
- Label Name hanya diketik dan tidak pernah disimpan, jadi `Hex Check 57` dan `Hex Recover 58` tidak memakai suffix.
