---
id: TC-FA-FAAM-E2E-103-popup-detail-tautan-lintas-modul-dan-group-scope
title: "Popup Detail: Tautan Lintas Modul, Hidden Tanpa Akses, dan Daftar Client-Wide pada Group Scope Terbatas"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-308
  - TC-FA-FAAM-309
  - TC-FA-FAAM-310
coverage:
  web: automated
---

# Popup Detail: Tautan Lintas Modul, Hidden Tanpa Akses, dan Daftar Client-Wide pada Group Scope Terbatas

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor berurutan (login akun pertama di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite; akun kedua dan ketiga lewat langkah `Ganti akun` eksplisit; hook `after` mengembalikan sesi ke akun default suite, Total Control `Spectra.env.FA_TC_PASSWORD`):
  - Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (TC-FA-FAAM-308).
  - Permission Read (Pre-setup #3) `permissionRead_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_PR_PASSWORD`; aktor tidak memiliki akses modul asset dan custom fields (TC-FA-FAAM-309).
  - Permission Read dengan Group scope terbatas di modul asset (Pre-setup #26b). Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); akun disediakan tim FE, password `Spectra.env.FA_PRG_PASSWORD` (TC-FA-FAAM-310).
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; suite berjalan serial (`parallel: false`). Spec ini tidak memakai seed API per TC.
- Data Pre-setup yang hanya dibaca: Pre-setup #10 `Dell Latitude` (Total Asset 42), custom field Pre-setup #27, dan 42 aset Pre-setup #26 di Group `Head Office`, `Finance`, dan `Warehouse`; fixture `Fixture.faAssetName.dellLatitude`. Tidak ada data yang diubah.
- Kemampuan teknis: tidak ada tambahan di luar `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-308: Tautan lintas modul mengikuti aturan same-tab

1. Ketik Search `Dell Latitude`, tekan Enter
2. Klik nama `Dell Latitude`
3. Klik tab `Linked Custom Fields (3)`
4. Klik tautan `Open in Custom Fields ↗`
5. Verifikasi navigasi ke Custom Fields terjadi di tab yang sama
6. Buka Fixed Asset > Settings > Asset Master > Asset Name

### TC-FA-FAAM-309: Tautan lintas modul Hidden bagi pemegang tanpa akses modul tujuan

7. Ganti akun: logout, lalu login sebagai Permission Read `permissionRead_automated_{namaCompany}@qwertysystem.net`
8. Buka Fixed Asset > Settings > Asset Master > Asset Name
9. Ketik Search `Dell Latitude`, tekan Enter
10. Klik nama `Dell Latitude`
11. Klik tab `Linked Custom Fields (3)`
12. Verifikasi tabel Linked Custom Fields dengan kolom `Field Name`, `Data Type`, `Global Value` tampil
13. Verifikasi tautan `Open in Custom Fields ↗` Hidden
14. Klik icon `[✕]`

### TC-FA-FAAM-310: Daftar aset dan jumlah di Detail client-wide tanpa pembatasan Group scope

15. Ganti akun: logout, lalu login sebagai Permission Read dengan Group scope terbatas di modul asset (Pre-setup #26b)
16. Buka Fixed Asset > Settings > Asset Master > Asset Name
17. Ketik Search `Dell Latitude`, tekan Enter
18. Klik nama `Dell Latitude`
19. Verifikasi label tab `Total Assets (42)` memuat jumlah seluruh aset client
20. Klik tab `Total Assets (42)`
21. Verifikasi daftar aset memuat aset dari semua Group (`Head Office`, `Finance`, dan `Warehouse`)
22. Klik icon `[✕]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (R-16, langkah 1, 9, 17), kembali ke halaman Asset Name (langkah 6), membuka halaman Asset Name sesudah login akun baru (langkah 8, 16), dan `[✕]` menutup popup (langkah 14, 22).
- TC-FA-FAAM-308 Expected b ("pemegang tanpa akses modul tujuan melihat tautan Hidden") diasersi pada langkah 13 milik TC-FA-FAAM-309 karena TC-FA-FAAM-308 hanya memiliki aktor Total Control.
- Asersi Hidden pada langkah 13 memakai tabel yang sudah diasersi (langkah 12) sebagai anchor (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-FAAM-310 memakai aktor Permission Read dengan Group scope terbatas (Pre-setup #26b) yang belum punya baris akun lengkap (email) di Tabel Pre-setup.
  - TC-FA-FAAM-309 Precondition c menyebut aktor "tidak memiliki akses modul asset dan custom fields" tanpa menyebut apakah akun Pre-setup #3 memenuhinya; spec memakai Permission Read Pre-setup #3.
  - TC-FA-FAAM-310 Expected tidak menyebut jumlah baris per Group; spec mengasersi jumlah pada label tab (42) dan kehadiran ketiga Group pada daftar.
  - TC-FA-FAAM-308 Expected a ("tab yang sama") tidak menyebut cara teramati; spec memeriksa bahwa halaman Custom Fields terbuka tanpa tab baru.
