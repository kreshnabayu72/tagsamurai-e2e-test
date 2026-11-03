---
id: TC-FA-FAAM-E2E-005-truncation-badge-teks-panjang-dan-needs-update
title: "Teks Panjang Tanpa Potongan, Truncation Badge 25 Karakter, dan Badge Needs Update"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-23
  - TC-FA-FAAM-24
  - TC-FA-FAAM-25
  - TC-FA-FAAM-28
coverage:
  web: automated
---

# Teks Panjang Tanpa Potongan, Truncation Badge 25 Karakter, dan Badge Needs Update

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; spec ini tidak memakai seed API per TC dan tidak memakai sesi API aktor.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru; nama Asset Name #14d, #14e, #14f tidak tertulis di TC):
  - Asset Name 120 karakter dengan Code 15 karakter (#14d): `Fixture.faAssetName.longNameItem`.
  - Asset Name ber-Category, Brand, dan model masing-masing 25 karakter (#14e): `Fixture.faAssetName.badge25Item`.
  - Asset Name ber-Category, Brand, dan model masing-masing 26 karakter (#14f): `Fixture.faAssetName.badge26Item`.
  - `MacBook Pro` (#12): Category internal `Electronics` sehingga Category Locked.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-23: Asset Name dan Code sangat panjang tampil utuh tanpa potongan dan tanpa tooltip

1. Ketik Search nama Asset Name 120 karakter (`Fixture.faAssetName.longNameItem`), tekan Enter
2. Verifikasi Asset Name pada baris tersebut tampil utuh dengan wrap natural
3. Verifikasi Asset Name pada baris tersebut tidak memuat `..`
4. Verifikasi Code pada baris tersebut tampil utuh
5. Hover nama Asset Name pada baris tersebut
6. Verifikasi tidak ada tooltip muncul saat hover nama
7. Hover Code pada baris tersebut
8. Verifikasi tidak ada tooltip muncul saat hover Code

### TC-FA-FAAM-24: Badge Category, Brand, dan Model/Type sampai 25 karakter tampil nama penuh

9. Ganti isi kotak search dengan nama Asset Name 25 karakter (`Fixture.faAssetName.badge25Item`), tekan Enter
10. Verifikasi badge Category pada baris tersebut tampil nama penuh tanpa `..`
11. Verifikasi badge Brand pada baris tersebut tampil nama penuh tanpa `..`
12. Verifikasi badge Model/Type pada baris tersebut tampil nama penuh tanpa `..`

### TC-FA-FAAM-25: Badge lebih dari 25 karakter terpotong 12 + .. + 12 dan hover menampilkan nilai penuh

13. Ganti isi kotak search dengan nama Asset Name 26 karakter (`Fixture.faAssetName.badge26Item`), tekan Enter
14. Verifikasi badge Category, Brand, dan Model/Type pada baris tersebut masing-masing menampilkan 12 karakter pertama, `..`, lalu 12 karakter terakhir
15. Hover badge Category
16. Verifikasi tooltip badge Category menampilkan hierarki `[Parent] > [Child]`
17. Hover badge Brand
18. Verifikasi tooltip badge Brand menampilkan nama penuh
19. Hover badge Model/Type
20. Verifikasi tooltip badge Model/Type menampilkan nama penuh

### TC-FA-FAAM-28: Asset Name ber-Category Locked menampilkan badge Needs Update dengan tooltip dan teks tidak di-dim

21. Ganti isi kotak search dengan `MacBook Pro`, tekan Enter
22. Verifikasi sel Category baris `MacBook Pro` menampilkan badge `Electronics`
23. Verifikasi sel Category baris `MacBook Pro` menampilkan badge peringatan `Needs Update` (severity warning)
24. Hover badge `Needs Update`
25. Verifikasi tooltip `Category is no longer selectable. Update the category before this template can be used for new asset registration.`
26. Verifikasi teks nama `MacBook Pro` tidak di-dim

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 23, 24, 25, 28 (semua pembacaan; tidak ada aksi yang mengubah data).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 9, 13, 21 (Search untuk menemukan baris target, R-16). Langkah "Perhatikan ..." pada Langkah uji TC dilebur ke langkah `Verifikasi` karena tidak mengubah state.
- Langkah 6 dan 8 (absence tooltip) memakai langkah hover sebagai anchor (8b butir 2) dan baris yang baru diasersi tampil.
- Temuan untuk QA:
  - TC-23, 24, 25 mengacu ke fixture #14d, #14e, #14f tanpa nama Asset Name; spec memakai kunci fixture baru yang disediakan tim FE/BE.
  - TC-25 b mengharapkan hover Category menampilkan hierarki `[Parent] > [Child]`, sedangkan Pre-setup #14f hanya menyebut Category 26 karakter tanpa menyatakan bahwa kategori itu bersarang (punya parent); spec mengasersi hierarki sesuai Expected.
  - TC-25 a menyebut 12 karakter pertama dan terakhir tanpa nilai literal; spec tidak menulis string literal dan mengasersi pola pemotongan.
