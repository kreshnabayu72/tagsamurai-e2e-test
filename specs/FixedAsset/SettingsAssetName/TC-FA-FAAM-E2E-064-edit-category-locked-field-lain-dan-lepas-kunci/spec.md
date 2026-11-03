---
id: TC-FA-FAAM-E2E-064-edit-category-locked-field-lain-dan-lepas-kunci
title: "Edit Category Locked: Field Lain Tidak Memeriksa Ulang dan Category Leaf Baru Melepas Kunci"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-199
  - TC-FA-FAAM-200
coverage:
  web: automated
---

# Edit Category Locked: Field Lain Tidak Memeriksa Ulang dan Category Leaf Baru Melepas Kunci

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (seed API per TC, sesi API aktor, cleanup `after`) mengikuti `suite.md`; suite berjalan serial (`parallel: false`).
- Data Pre-setup #12: Asset Name `MacBook Pro` (Code `MBP`, Category internal `Electronics` sehingga Category Locked dengan badge `Needs Update`, TAG Type `QR`+`BLE`, Brand `Apple`, UoM `Unit`, Total Asset 15), dirujuk lewat fixture baru `Fixture.faAssetName.macBookPro`. Fixture ini tidak dapat digandakan; TC-199 mengubah Code dan TC-200 mengubah Category sehingga kunci terlepas. Pemulihan ke keadaan Pre-setup #12 dijamin fixture seed reset yang disediakan tim FE/BE dan dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar-TC. Efek yang tersisa: Last Updated baris dan entri audit trail Changelog, System Log, dan Activity Log bertambah. Suite berjalan serial (S-06, pengecualian 2026-10-30).
- Pohon kategori Pre-setup #22: leaf `Laptop` (di bawah `Electronics`) dipilih TC-200.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-199: Edit field lain pada Asset Name ber-Category Locked tidak memeriksa ulang Category

1. Ketik Search `MacBook Pro`, tekan Enter
2. Klik `⋯` baris `MacBook Pro` lalu `Edit`
3. Ubah Code menjadi `MBP2`
4. Klik `[Save]`
5. Verifikasi toast `Success, asset name has been updated.` tampil
6. Verifikasi Category baris `MacBook Pro` tetap `Electronics`
7. Verifikasi badge `Needs Update` tetap tampil pada baris `MacBook Pro`
8. Pulihkan `MacBook Pro` ke keadaan Pre-setup #12 lewat seed reset

### TC-FA-FAAM-200: Memilih Category leaf lain melepas status Category Locked

9. Ganti isi kotak search dengan `MacBook Pro`, tekan Enter
10. Klik `⋯` baris `MacBook Pro` lalu `Edit`
11. Klik `[Select Category]`, pilih leaf `Laptop` lewat Tree Picker, klik `[Select]`
12. Klik `[Save]`
13. Verifikasi dialog `Change Category` tampil (D-11)
14. Klik `[Save]` pada dialog Change Category
15. Verifikasi badge `Needs Update` hilang dari baris `MacBook Pro`
16. Verifikasi Category baris `MacBook Pro` menjadi `Laptop`
17. Pulihkan `MacBook Pro` ke keadaan Pre-setup #12 lewat seed reset

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search pada langkah 1 dan 9 untuk menemukan baris target (R-16); pemulihan fixture pada langkah 8 (antar-TC, sesuai Post Condition TC-FA-FAAM-199) dan 17 (akhir spec, sesuai Post Condition TC-FA-FAAM-200).
- Langkah Uji TC-FA-FAAM-199 "Pada baris `MacBook Pro` ubah Code menjadi `MBP2`" dijalankan sebagai perubahan Code pada form Edit baris `MacBook Pro`.
- Temuan untuk QA:
  - TC-FA-FAAM-200 Expected menyebut dialog `Change Category` tampil (D-11) tanpa teksnya; spec hanya mengasersi dialog tampil dengan judul itu.
  - Pernyataan pemulihan fixture `MacBook Pro` dan `Dell Latitude` oleh seed reset belum tercantum di `suite.md` (S-06, pengecualian 2026-10-30 mensyaratkannya); pemilik suite perlu menambahkannya.
