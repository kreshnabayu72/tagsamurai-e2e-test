---
id: TC-FA-LBL-E2E-021-color-picker-create-validasi-kode-hex-tidak-valid-v04-bagian-1
title: "Color Picker Create: Validasi Kode Hex Tidak Valid (V-04) (bagian 1/2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-LBL-54
  - TC-FA-LBL-55
  - TC-FA-LBL-56
coverage:
  web: automated
---

# Color Picker Create: Validasi Kode Hex Tidak Valid (V-04) (bagian 1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson), `Fixture.assetLabeling.akun.totalControl`, `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec. Fixture `fixtures/asset-labeling.json` (`Fixture.assetLabeling.*`) memuat identitas akun tanpa rahasia; fixture ini belum ada dan disediakan tim FE.
- Env var `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak mengubah state global kecuali dinyatakan di bawah.
- Spec ini tidak membuat atau menyimpan label (semua submit diblokir validasi); tidak ada cleanup data.

## Test Steps

1. Klik `[+ Label]`

### TC-FA-LBL-54: Kode hex kurang dari 6 digit ditolak real-time dengan V-04

2. Isi Label Name `Hex Check 54`
3. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
4. Kosongkan kolom Hex lalu ketik `#12345`
5. Verifikasi inline error `Invalid color format` tampil di dalam overlay
6. Verifikasi Swatch Trigger dan Live Preview tetap berlatar `#3B82F6` (warna valid terakhir)
7. Verifikasi `[Submit]` berstatus disabled walau Label Name terisi

### TC-FA-LBL-55: Kode hex lebih dari 6 digit ditolak real-time dengan V-04

8. Tekan Esc untuk menutup overlay
9. Ganti isi Label Name dengan `Hex Check 55`
10. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
11. Kosongkan kolom Hex lalu ketik `#3B82F6` (warna valid sebagai pembersih error)
12. Kosongkan kolom Hex lalu ketik `#1234567`
13. Verifikasi inline error `Invalid color format` tampil di dalam overlay
14. Verifikasi Swatch Trigger dan Live Preview tetap berlatar `#3B82F6` (warna valid terakhir)
15. Verifikasi `[Submit]` berstatus disabled walau Label Name terisi

### TC-FA-LBL-56: Kode hex berisi karakter non-heksadesimal ditolak real-time dengan V-04

16. Tekan Esc untuk menutup overlay
17. Ganti isi Label Name dengan `Hex Check 56`
18. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
19. Kosongkan kolom Hex lalu ketik `#3B82F6` (warna valid sebagai pembersih error)
20. Kosongkan kolom Hex lalu ketik `#GGGGGG`
21. Verifikasi inline error `Invalid color format` tampil di dalam overlay
22. Verifikasi Swatch Trigger dan Live Preview tetap berlatar `#3B82F6` (warna valid terakhir)
23. Verifikasi `[Submit]` berstatus disabled walau Label Name terisi
24. Tekan Esc untuk menutup overlay
25. Klik icon `[✕]`
26. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` dan `[Leave]` tampil
27. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Satu pembukaan modal dipakai TC-FA-LBL-54, 55, dan 56 (prinsip 6). Label Name diisi sebelum overlay dibuka (urutan TC); karena modal dipakai bersama, sebelum TC-FA-LBL-55 dan 56 overlay ditutup dengan Esc, Label Name diganti isinya, lalu overlay dibuka lagi. Error `Invalid color format` identik antar-TC, jadi sesudah overlay dibuka lagi kolom Hex diisi `#3B82F6` sebagai pembersih sebelum kode tidak valid diketik (R-12; aksi tanpa `Verifikasi`, S-03).
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 8 dan 16 (menutup overlay dengan Esc supaya Label Name bisa diisi sebelum overlay dibuka lagi), pembersih `#3B82F6` pada langkah 11 dan 19, serta langkah 24, 25, dan 27 (menutup overlay dan modal; form dirty karena Label Name terisi, jadi ditutup lewat dialog `Unsaved Changes` dengan `[Leave]`, S-08).
- Label Name hanya diketik dan tidak pernah disimpan, jadi `Hex Check 54`, `Hex Check 55`, dan `Hex Check 56` tidak memakai suffix.
