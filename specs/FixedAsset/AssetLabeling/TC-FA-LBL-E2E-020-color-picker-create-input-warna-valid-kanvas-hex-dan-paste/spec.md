---
id: TC-FA-LBL-E2E-020-color-picker-create-input-warna-valid-kanvas-hex-dan-paste
title: "Color Picker Create: Input Warna Valid (Kanvas, Hex, dan Paste)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-50
  - TC-FA-LBL-51
  - TC-FA-LBL-52
  - TC-FA-LBL-53
coverage:
  web: automated
---

# Color Picker Create: Input Warna Valid (Kanvas, Hex, dan Paste)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson), password dari `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak mengubah state global kecuali dinyatakan di bawah.
- Spec ini tidak membuat atau menyimpan label; tidak ada cleanup data. Kemampuan teknis: menempel teks dari clipboard ke kolom Hex (TC-FA-LBL-53).

## Test Steps

1. Klik `[+ Label]`
2. Klik Swatch Trigger Color untuk membuka Color Picker Overlay

### TC-FA-LBL-50: Klik titik pada kanvas warna kustom memperbarui kolom Hex dan Live Preview

3. Klik titik di area kanvas spektrum
4. Verifikasi kolom Hex menampilkan kode `#RRGGBB` kapital dari titik yang diklik
5. Verifikasi Swatch Trigger dan Live Preview berlatar warna yang sama dengan kolom Hex
6. Verifikasi overlay tetap terbuka

### TC-FA-LBL-51: Mengetik kode hex huruf kapital valid memperbarui warna terpilih secara instan

7. Kosongkan kolom Hex lalu ketik `#1E3A8A`
8. Verifikasi Swatch Trigger dan Live Preview langsung berlatar `#1E3A8A`
9. Verifikasi kolom Hex menampilkan `#1E3A8A`
10. Verifikasi tidak ada inline error di dalam overlay

### TC-FA-LBL-53: Menempel kode hex valid di kolom Hex memperbarui warna terpilih

11. Kosongkan kolom Hex lalu tempel `#10B981` dari clipboard
12. Verifikasi Swatch Trigger dan Live Preview berlatar `#10B981`
13. Verifikasi kolom Hex menampilkan `#10B981`

### TC-FA-LBL-52: Mengetik kode hex huruf kecil valid ditampilkan huruf kapital di kolom Hex

14. Kosongkan kolom Hex lalu ketik `#1e3a8a`
15. Verifikasi kolom Hex menampilkan `#1E3A8A` dalam huruf kapital
16. Verifikasi Swatch Trigger dan Live Preview berlatar `#1E3A8A`
17. Verifikasi tidak ada inline error `Invalid color format`
18. Tekan Esc untuk menutup overlay
19. Klik icon `[✕]`
20. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` dan `[Leave]` tampil
21. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 50, 51, 53, 52. TC-FA-LBL-51 dan TC-FA-LBL-52 sama-sama mengakhiri warna di `#1E3A8A`; TC-FA-LBL-53 (`#10B981`) disisipkan di antaranya supaya warna pada TC-FA-LBL-52 benar-benar berubah dari warna yang berlaku.
- Satu pembukaan modal dan satu pembukaan overlay dipakai seluruh TC; kolom Hex dikosongkan di antara kasus (prinsip 6).
- Klik tiap swatch preset (TC-FA-LBL-49) ada di spec 159.
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 18 dan 21 (menutup overlay dan modal; form dirty karena warna berubah, jadi ditutup lewat dialog `Unsaved Changes` dengan `[Leave]`, S-08).
