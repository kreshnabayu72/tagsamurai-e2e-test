---
id: TC-FA-FAAM-E2E-062-edit-validasi-code
title: "Edit: Validasi Code (Batas 15, Karakter Tidak Valid, Duplikat, Kapitalisasi Sendiri)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAM-190
  - TC-FA-FAAM-191
  - TC-FA-FAAM-192
  - TC-FA-FAAM-193
  - TC-FA-FAAM-194
coverage:
  web: automated
---

# Edit: Validasi Code (Batas 15, Karakter Tidak Valid, Duplikat, Kapitalisasi Sendiri)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #13d: Asset Name `Edit Target Item` (Code `ETI`, Category `IT Equipment`, TAG Type `QR`, Brand `Dell` model `5420`, UoM `Unit`, Total Asset 0), dirujuk lewat fixture baru `Fixture.faAssetName.editTargetItem`; dipakai TC-190, 192, 193, 194 hanya untuk dibuka dan ditolak validasi, tidak disimpan sehingga Last Updated tidak berubah (S-06). Pre-setup #10 `Dell Latitude` (Code `DLAT`) hanya dirujuk sebagai Code yang sudah ada untuk TC-193 dan tidak diubah.
- Data Dinamis (salinan seed fixture #13d, Dinamis #21): `Edit Target Item 191 {runId}-062` (Code `ETI191`) untuk TC-191. Code 15 karakter valid yang diketik TC-191: `ETI191-01234567`.
- Kemampuan teknis (disediakan tim FE/BE): seed API per TC untuk salinan fixture bernama bersuffix `{runId}-062` (Code salinan mengikuti pola TC dan tetap di bawah batas 15 karakter) dan sesi API aktor; salinan dihapus lewat id hasil seed di hook `after`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-190: Code 16 karakter menampilkan error real-time saat Edit

1. Ketik Search `Edit Target Item`, tekan Enter
2. Klik `⋯` baris `Edit Target Item` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
3. Ketik Code 16 karakter `ABCDEFGHIJKLMNOP`
4. Verifikasi error inline `Max. 15 characters`

### TC-FA-FAAM-192: Code berisi karakter tidak valid menampilkan error saat Edit

5. Ganti isi field Code dengan `AB CD#`
6. Verifikasi error inline `Code contains invalid characters`

### TC-FA-FAAM-193: Code milik Asset Name lain menampilkan error duplikat saat Edit

7. Ganti isi field Code dengan `dlat` lalu tunggu lebih dari 500 ms
8. Verifikasi error inline `Code already exists`

### TC-FA-FAAM-194: Code milik sendiri dengan kapitalisasi beda tidak dianggap duplikat

9. Ganti isi field Code dengan `eti` lalu tunggu lebih dari 500 ms
10. Verifikasi field Code menampilkan `ETI`
11. Verifikasi tidak ada error `Code already exists`
12. Klik `[✕]` pada modal Edit

### TC-FA-FAAM-191: Code tepat 15 karakter diterima saat Edit

13. Ganti isi kotak search dengan `Edit Target Item 191 {runId}-062`, tekan Enter
14. Klik `⋯` baris `Edit Target Item 191 {runId}-062` lalu `Edit` sehingga `Popup Edit Asset Name` terbuka
15. Ubah Code menjadi 15 karakter valid `ETI191-01234567`
16. Verifikasi field Code berisi 15 karakter
17. Verifikasi tidak ada error inline pada field Code
18. Klik `[Save]`
19. Verifikasi toast `Success, asset name has been updated.` tampil

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1 dan 13 untuk menemukan baris target (R-16); penutupan modal pada langkah 12 tanpa dialog karena Code sudah sama dengan nilai tersimpan (`ETI`).
- Urutan TC: validasi yang diblokir lebih dulu (TC-FA-FAAM-190, 192, 193, 194) pada satu pembukaan popup, lalu aksi sukses TC-FA-FAAM-191 pada salinan (S-10).
- Pada TC-FA-FAAM-194 spec menambahkan jeda lebih dari 500 ms (seperti TC-FA-FAAM-193) agar pemeriksaan duplikat sempat berjalan sebelum asersi ketiadaan error; Verifikasi field Code menampilkan `ETI` menjadi anchor bagi asersi ketiadaan error (bagian 8b butir 2). Anchor yang sama (Verifikasi field Code berisi 15 karakter) dipakai pada TC-FA-FAAM-191.
- Keunikan nilai Code yang diketik (batas 15 karakter tidak menyisakan ruang untuk suffix `{runId}-<NNN>`): nilai Code mengikuti TC, nomor TC membuatnya berbeda antar spec, seed salinan idempotent, cleanup hanya menghapus yang dibuat spec ini, dan suite berjalan serial (S-12).
- Temuan untuk QA:
  - TC-FA-FAAM-191 menyebut "Code 15 karakter valid" tanpa nilainya; spec memilih `ETI191-01234567` (diputuskan penulis).
  - TC-FA-FAAM-190 menyebut "Code 16 karakter" tanpa nilainya; spec memilih `ABCDEFGHIJKLMNOP` (diputuskan penulis).
