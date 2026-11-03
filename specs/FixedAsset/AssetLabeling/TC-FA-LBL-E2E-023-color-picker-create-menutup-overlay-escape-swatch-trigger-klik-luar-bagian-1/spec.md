---
id: TC-FA-LBL-E2E-023-color-picker-create-menutup-overlay-escape-swatch-trigger-klik-luar-bagian-1
title: "Color Picker Create: Menutup Overlay (Escape, Swatch Trigger, Klik Luar) (bagian 1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-59
  - TC-FA-LBL-60
  - TC-FA-LBL-61
  - TC-FA-LBL-62
coverage:
  web: automated
---

# Color Picker Create: Menutup Overlay (Escape, Swatch Trigger, Klik Luar) (bagian 1/2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson), password dari `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak mengubah state global kecuali dinyatakan di bawah.
- Palet Preset (Pre-setup #33): swatch baris 1 kolom 1 bernilai `#EF4444`.
- Spec ini tidak membuat atau menyimpan label; tidak ada cleanup data.

## Test Steps

1. Klik `[+ Label]`
2. Klik Swatch Trigger Color untuk membuka Color Picker Overlay

### TC-FA-LBL-59: Color Picker Overlay tetap terbuka setelah memilih swatch, mengklik kanvas, atau mengetik hex

3. Klik swatch baris 1 kolom 1
4. Verifikasi overlay tetap terbuka
5. Verifikasi warna terpilih langsung tampil di Swatch Trigger dan Live Preview
6. Klik satu titik kanvas
7. Verifikasi overlay tetap terbuka
8. Verifikasi warna terpilih langsung tampil di Swatch Trigger dan Live Preview
9. Kosongkan kolom Hex lalu ketik `#10B981`
10. Verifikasi overlay tetap terbuka
11. Verifikasi warna terpilih langsung tampil di Swatch Trigger dan Live Preview

### TC-FA-LBL-60: Tombol Escape menutup overlay tanpa menutup modal Create Label dan warna dipertahankan

12. Klik swatch baris 1 kolom 1
13. Kosongkan kolom Hex lalu ketik `#10B981`
14. Tekan Escape
15. Verifikasi overlay tertutup
16. Verifikasi modal Create Label tetap terbuka
17. Verifikasi Swatch Trigger dan Live Preview tetap berlatar `#10B981`

### TC-FA-LBL-61: Klik Swatch Trigger saat overlay terbuka menutup overlay dengan warna terakhir dipertahankan

18. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
19. Klik swatch baris 1 kolom 1
20. Klik Swatch Trigger lagi
21. Verifikasi overlay tertutup
22. Verifikasi modal tetap terbuka
23. Verifikasi warna swatch yang dipilih (`#EF4444`) dipertahankan di Swatch Trigger dan Live Preview

### TC-FA-LBL-62: Klik di luar overlay menutup overlay tanpa menutup modal Create Label

24. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
25. Klik titik kanvas lalu klik area kosong di dalam modal di luar overlay
26. Verifikasi overlay tertutup
27. Verifikasi modal Create Label tetap terbuka
28. Verifikasi warna dari titik kanvas dipertahankan di Swatch Trigger dan Live Preview
29. Klik icon `[✕]`
30. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?`, tombol `[Cancel]` dan `[Leave]` tampil
31. Klik `[Leave]`

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Satu pembukaan modal dipakai TC-FA-LBL-59 sampai 62 (prinsip 6); overlay dibuka ulang di awal TC-FA-LBL-61 dan 62 sesudah TC di atasnya menutupnya.
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 12 (TC-FA-LBL-59 berakhir di `#10B981`, sama dengan data TC-FA-LBL-60; swatch baris 1 kolom 1 dipilih dulu supaya warna `#10B981` pada TC-FA-LBL-60 benar-benar berubah) dan langkah 31 (menutup modal; form dirty karena warna berubah, jadi ditutup lewat dialog `Unsaved Changes` dengan `[Leave]`, S-08).
- Langkah 3 TC-FA-LBL-62 (klik titik kanvas lalu klik area kosong di dalam modal) ditulis satu langkah sesuai kalimat TC.
- TC-FA-LBL-512 (menutup overlay saat Hex tidak valid) ada di spec 024.
