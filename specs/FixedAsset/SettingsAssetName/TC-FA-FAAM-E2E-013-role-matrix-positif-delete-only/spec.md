---
id: TC-FA-FAAM-E2E-013-role-matrix-positif-delete-only
title: "Role Matrix Positif Delete-Only: Dialog Blok In-Use, Delete, dan Bulk Delete"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-54
  - TC-FA-FAAM-55
  - TC-FA-FAAM-57
coverage:
  web: automated
---

# Role Matrix Positif Delete-Only: Dialog Blok In-Use, Delete, dan Bulk Delete

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji (Pre-setup #6):

| Role | Akun (Pre-setup) | Env password |
|---|---|---|
| Delete-Only | `deleteOnly_automated_{namaCompany}@qwertysystem.net` (#6) | `Spectra.env.FA_DO_PASSWORD` |

- Login akun Delete-Only di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `Spectra.env.FA_TC_PASSWORD`). Password tidak ditulis di spec atau fixture. Nama env baru didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya.
- Data Pre-setup (hanya dibaca, dirujuk lewat fixture baru `Fixture.faAssetName.catalog`): `Dell Latitude` (#10, Total Asset 42) hanya dibuka sampai dialog blok in-use.
- Data Dinamis (suffix `{runId}-013`, seed API di hook `before`, Total Asset 0; dihapus oleh spec, hook `after` membersihkan sisa bila spec gagal): `Delete Role Item {runId}-013` (salinan fixture #13b), `Bulk Role A {runId}-013` dan `Bulk Role B {runId}-013` (salinan fixture #13c).
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAM-57: Pemegang Delete-Only menekan Delete pada Asset Name in-use dan mendapat dialog blok

1. Ketik Search `Dell Latitude`, tekan Enter
2. Klik `⋯` baris `Dell Latitude` lalu `Delete`
3. Verifikasi dialog `Cannot Delete Asset Name` memuat bullet `Dell Latitude`, teks `This asset name is used by 42 assets and cannot be deleted.`, dan tombol `[OK]`
4. Klik `[OK]`

### TC-FA-FAAM-54: Pemegang Delete-Only menghapus Asset Name tanpa aset sampai sukses

5. Ganti isi kotak search dengan `Delete Role Item {runId}-013`, tekan Enter
6. Klik `⋯` baris `Delete Role Item {runId}-013` lalu `Delete`
7. Verifikasi dialog `Delete Asset Name` memuat bullet `Delete Role Item {runId}-013`
8. Klik `[Delete]` pada dialog konfirmasi
9. Verifikasi toast `Success, asset name has been deleted.`
10. Verifikasi baris `Delete Role Item {runId}-013` hilang dari List

### TC-FA-FAAM-55: Pemegang Delete-Only menjalankan Bulk Delete sampai sukses

11. Ganti isi kotak search dengan `{runId}-013`, tekan Enter
12. Centang baris `Bulk Role A {runId}-013` dan `Bulk Role B {runId}-013`
13. Klik `Bulk Action` lalu `Delete`
14. Verifikasi dialog `Delete Asset Names` memuat bullet `Bulk Role A {runId}-013` dan `Bulk Role B {runId}-013`
15. Klik `[Delete]` pada dialog
16. Verifikasi toast `Success, asset name has been deleted.`
17. Verifikasi baris `Bulk Role A {runId}-013` dan `Bulk Role B {runId}-013` hilang dari List

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC di spec: 57, 54, 55 (dialog blok sebelum aksi sukses, aksi menghapus data di akhir, S-10).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03): langkah 1, 5, 11 (Search untuk menemukan baris target, R-16; Search `{runId}-013` pada langkah 11 hanya mencocokkan kedua salinan Bulk Role karena salinan lain sudah dihapus pada langkah 8), langkah 4 (menutup dialog blok).
- Langkah 10 dan 17 (absence baris) memakai toast sukses pada langkah 9 dan 16 sebagai anchor (bagian 8b butir 2).
- Langkah 7 dan 14 mengasersi judul dan bullet dialog konfirmasi sebagai satu elemen; tombol `[Delete]` dikliknya pada langkah berikutnya.
- Temuan untuk QA:
  - TC-54 dan TC-55 memakai `Delete Role Item`, `Bulk Role A`, dan `Bulk Role B` (Pre-setup #13b dan #13c) sebagai target Delete tanpa salinan per TC di Tabel Data Uji Dinamis; spec memakai salinan seed API bersuffix `{runId}-013` supaya fixture bersama tidak terhapus (S-06).
  - TC-55 Expected b memakai toast `Success, asset name has been deleted.` (bentuk tunggal) untuk Bulk Delete dua nama; spec mengikuti teks TC.
