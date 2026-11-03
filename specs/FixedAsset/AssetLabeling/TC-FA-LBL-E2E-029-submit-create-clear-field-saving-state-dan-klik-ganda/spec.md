---
id: TC-FA-LBL-E2E-029-submit-create-clear-field-saving-state-dan-klik-ganda
title: "Submit Create: Clear Field, Saving State, dan Klik Ganda"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LBL-83
  - TC-FA-LBL-91
  - TC-FA-LBL-90
coverage:
  web: automated
---

# Submit Create: Clear Field, Saving State, dan Klik Ganda

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson), password dari `Spectra.env.FA_LBL_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Tidak ada ganti akun di tengah spec.
- Env var `FA_LBL_TC_PASSWORD` terdaftar di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Hook suite (flag Guided Tooltip `seen`, pembukaan tab Labels, pemulihan state global) mengikuti `suite.md`; spec ini tidak mengubah state global kecuali dinyatakan di bawah.
- Suffix nama bersuffix spec ini: `{runId}-029` (`{runId}` hanya digit).
- Data Pre-setup #12: label `High Priority` sudah ada di katalog Company Alpha; hanya dibaca untuk memunculkan error duplikat pada TC-FA-LBL-83.
- Label yang dibuat: `Saving State 91 {runId}-029` dan `Double Click 90 {runId}-029`.
- Intercept (`Spectra.intercept()`): menahan respons Create (TC-FA-LBL-91) untuk mengamati saving state; dilepas segera sesudah pengamatan.
- Label yang dibuat spec ini (nama bersuffix `{runId}-029`) dihapus di hook `after` lewat sesi API aktor.
- Kemampuan teknis (disediakan tim FE/BE, suite.md): sesi API aktor dan fixture BE untuk membaca state katalog, entri Create di Changelog, dan menghapus label.

## Test Steps

1. Klik `[+ Label]`

### TC-FA-LBL-83: Tombol Clear Field mengosongkan nama, mengembalikan warna default, dan mempertahankan Stay

2. Centang `Stay on this form after submitting`
3. Ketik `High Priority` dan tunggu error duplikat
4. Verifikasi inline error `Label name already exists` tampil
5. Klik Swatch Trigger Color untuk membuka Color Picker Overlay
6. Kosongkan kolom Hex lalu ketik `#10B981`
7. Klik `[Clear Field]`
8. Verifikasi Label Name kosong
9. Verifikasi Color kembali `#3B82F6` pada Swatch Trigger
10. Verifikasi Live Preview kembali berlatar `#3B82F6`
11. Verifikasi inline error duplikat hilang dan status validasi kembali pristine
12. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
13. Verifikasi tidak ada dialog konfirmasi
14. Verifikasi modal tetap terbuka
15. Verifikasi fokus berada di Label Name
16. Hapus centang `Stay on this form after submitting`

### TC-FA-LBL-91: Saving state Submit: tombol loading, kontrol lain terkunci selama request

17. Isi Label Name `Saving State 91 {runId}-029`
18. Tahan respons Create (delay jaringan)
19. Klik `[Submit]`
20. Verifikasi `[Submit]` menampilkan spinner dan berstatus disabled
21. Verifikasi `[Clear Field]`, icon `[✕]`, dan input form berstatus disabled sampai respons diterima
22. Lepas tahanan respons Create lalu tunggu modal tertutup

### TC-FA-LBL-90: Klik ganda cepat pada Submit hanya memproses satu request

23. Klik `[+ Label]`
24. Isi Label Name `Double Click 90 {runId}-029`
25. Klik `[Submit]` dua kali dengan cepat
26. Verifikasi `[Submit]` berstatus disabled dengan loading setelah klik pertama
27. Verifikasi hanya satu label `Double Click 90 {runId}-029` di katalog (lewat fixture BE)
28. Verifikasi tepat satu entri Create tercatat untuk `Double Click 90 {runId}-029` (lewat fixture BE; baseline nol karena nama unik)

## Notes

- Sumber: `fixed-asset/settings-asset-labeling/TestCases/tc-settings-asset-labeling.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 83, 91, 90. TC-FA-LBL-83 (tanpa menyimpan) lebih dulu supaya modal yang sama dipakai; checkbox Stay dihapus centangnya pada langkah 16 sebelum TC-FA-LBL-91 supaya Submit menutup modal.
- Langkah penghubung (tanpa awalan Verifikasi, S-03): langkah 16 (menghapus centang Stay) dan langkah 22 (melepas intercept dan menunggu modal tertutup, S-09).
- Asersi tambahan di luar Expected TC (S-03): langkah 4 memastikan error duplikat sudah tampil sebagai anchor positif bagi asersi "error duplikat hilang" sesudah `[Clear Field]` (bagian 8b butir 2).
- Pada langkah 3 TC-FA-LBL-83 "Klik Swatch Trigger lalu ketik hex" overlay masih terbuka ketika `[Clear Field]` diklik; TC tidak menentukan keadaan overlay sesudahnya dan spec tidak mengasersinya.
- Temuan untuk QA:
  - TC-FA-LBL-83 Expected a "status validasi kembali pristine" tidak punya definisi teramati; spec menggabungkannya dengan hilangnya error duplikat dalam satu `Verifikasi`.
  - TC-FA-LBL-90 Expected menyebut "satu entri Create tercatat" tanpa permukaan log; spec membacanya lewat fixture BE dengan nama bersuffix unik (baseline nol).
  - TC-FA-LBL-84 ada di spec 030 dan TC-FA-LBL-86 ada di spec 160.
