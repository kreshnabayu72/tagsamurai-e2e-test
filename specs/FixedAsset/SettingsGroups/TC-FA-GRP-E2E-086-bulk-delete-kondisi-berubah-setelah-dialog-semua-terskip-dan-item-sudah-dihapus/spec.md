---
id: TC-FA-GRP-E2E-086-bulk-delete-kondisi-berubah-setelah-dialog-semua-terskip-dan-item-sudah-dihapus
title: "Bulk Delete: Kondisi Berubah Setelah Dialog (Re-Evaluasi per Group), Seluruh Item Terskip, dan Item Sudah Dihapus User Lain"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-264
  - TC-FA-GRP-265
  - TC-FA-GRP-266
coverage:
  web: automated
---

# Bulk Delete: Kondisi Berubah Setelah Dialog (Re-Evaluasi per Group), Seluruh Item Terskip, dan Item Sudah Dihapus User Lain

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control (Pre-setup No 1: `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`, kosong tanpa aset): `Bulk E7` dan `Bulk E8` (TC-264), `Bulk E9` dan `Bulk E10` (TC-265), `Bulk E11` dan `Bulk E12` (TC-266).
- Pelaku kedua ("user lain") memicu perubahan state lewat sesi API: mendaftarkan atau menambah aset ke group (kemampuan membuat aset disediakan tim FE/BE) dan menghapus `Bulk E12`; bukan konteks UI kedua (suite.md).
- Cleanup di `after`: lepas aset seed lewat fixture BE, lalu hapus sisa group milik spec lewat API.

## Test Steps

### TC-FA-GRP-264: Kondisi berubah setelah dialog, re-evaluasi per group

1. Centang `Bulk E7` dan `Bulk E8`
2. Buka Bulk Action, pilih `Delete` (dialog homogen terbuka)
3. User lain (sesi API) mendaftarkan aset ke `Bulk E8` hingga pendaftaran tersimpan
4. Klik [Delete]
5. Verifikasi toast "Success, group has been deleted. Some items were skipped."
6. Verifikasi `Bulk E7` terhapus (hilang dari tabel)
7. Verifikasi `Bulk E8` masuk hitungan skip (tetap ada di tabel)

### TC-FA-GRP-265: Seluruh item terskip saat commit

8. Centang `Bulk E9` dan `Bulk E10`
9. Buka Bulk Action, pilih `Delete`
10. User lain (sesi API) menambah aset ke `Bulk E9` dan `Bulk E10` hingga penambahan tersimpan
11. Klik [Delete]
12. Verifikasi tidak ada toast sukses
13. Verifikasi dialog dengan title "Cannot Delete Groups", bullet `Bulk E9` dan `Bulk E10`, isi "These groups could not be deleted because their status changed. Please review and try again."
14. Verifikasi dialog hanya memuat tombol [OK]
15. Klik [OK]
16. Verifikasi `Bulk E9` dan `Bulk E10` tetap ada di tabel (tidak ada yang terhapus)

### TC-FA-GRP-266: Item sudah dihapus user lain masuk hitungan skip

17. Centang `Bulk E11` dan `Bulk E12`
18. Buka Bulk Action, pilih `Delete`
19. User lain (sesi API) menghapus `Bulk E12` hingga penghapusan tersimpan
20. Klik [Delete]
21. Verifikasi toast "Success, group has been deleted. Some items were skipped." (`Bulk E12` dihitung skip)
22. Verifikasi `Bulk E11` terhapus (hilang dari tabel)

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 3, 10, 19: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Setiap pemicu pelaku kedua ditulis "... hingga ... tersimpan" (R-20). Langkah 12 (absence toast sukses) diletakkan segera setelah pemicu [Delete]; anchor positif menyusul pada dialog "Cannot Delete Groups" di langkah berikutnya (8b butir 11).
- Hilangnya `Bulk E7` dan `Bulk E11` sebagai asersi absence didahului toast ringkasan (langkah 5 dan 21) sebagai anchor respons server (8b butir 2); urutan langkah mengikuti urutan state, bukan urutan butir Expected (8b butir 5).
- Temuan untuk QA:
  - TC-264 Expected tidak menyebut dialog homogen; dialog hanya dibuka sebagai langkah, tidak diasersi.
  - TC-266 Precondition tidak ada; spec memakai dua group kosong `Bulk E11` dan `Bulk E12` dari Langkah 2.
