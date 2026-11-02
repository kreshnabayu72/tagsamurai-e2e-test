---
id: TC-FA-GRP-E2E-087-bulk-delete-parent-dan-descendant-tidak-sama-sama-terpilih-dan-satu-group-identik-single
title: "Bulk Delete: Parent dan Descendant Tidak Sama-Sama Terpilih (Cascade) dan Satu Group Terpilih Identik dengan Delete Single"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-268
  - TC-FA-GRP-981
coverage:
  web: automated
---

# Bulk Delete: Parent dan Descendant Tidak Sama-Sama Terpilih (Cascade) dan Satu Group Terpilih Identik dengan Delete Single

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Total Control (Pre-setup No 1: `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`); halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite. Hook suite (flag Guided Tooltip, sesi API aktor, klien HTTP, fixture BE) mengikuti `suite.md`; hook `after` mengembalikan sesi ke akun default suite. Suite berjalan serial (`parallel: false`).
- Nama data Dinamis di Test Steps ditulis tanpa suffix; nilai sebenarnya `<nama> {runId}-NNN` (NNN = nomor spec ini) dan sama di seeding, asersi teks, dan cleanup. Nilai mengacu `Fixture.fixedAssetSettingsGroups.<kunci>` (berkas `fixtures/fixedAssetSettingsGroups.json` belum ada; ditambahkan tim FE).
- Data Dinamis (di-seed lewat API di `before`, kosong tanpa aset): `Bulk Parent` dengan child `Bulk Child` (TC-268) dan `Bulk E13` dengan child `Bulk E13 Child` (TC-981).
- Kemampuan teknis (disediakan tim FE/BE): tidak ada selain fixture seeding. Baseline entri Changelog nol karena entri dicari lewat Search nama group bersuffix unik (S-12).
- Cleanup di `after`: hapus sisa data milik spec lewat API.

## Test Steps

### TC-FA-GRP-268: Parent dan descendant tidak pernah sama-sama terpilih

1. Centang `Bulk Parent`
2. Klik node `Bulk Parent` di sidebar (tabel menampilkan `Bulk Child`)
3. Verifikasi tidak ada baris tercentang dan bar bulk action hilang (seleksi direset)
4. Verifikasi tabel node `Bulk Parent` hanya menampilkan `Bulk Child`
5. Klik `All Groups` di sidebar (kembali ke node induk)
6. Centang `Bulk Parent` saja
7. Buka Bulk Action, pilih `Delete`
8. Klik [Delete]
9. Verifikasi toast sukses "Success, group has been deleted."
10. Verifikasi `Bulk Parent` dan `Bulk Child` terhapus dari tabel dan sidebar tanpa error
11. Buka Modal Changelog: Group, lalu ketik Search `Bulk Parent`, tekan Enter
12. Verifikasi tepat satu entri Action `Delete` untuk `Bulk Parent`
13. Ganti isi kotak search dengan `Bulk Child`, tekan Enter
14. Verifikasi tepat satu entri Action `Delete` untuk `Bulk Child` (tidak dobel)
15. Klik `(←)` pada kotak Search, lalu tutup Modal Changelog: Group

### TC-FA-GRP-981: Satu group terpilih identik dengan Delete single

16. Centang hanya `Bulk E13`
17. Buka Bulk Action, pilih `Delete`
18. Verifikasi dialog single dengan title "Delete Group" dan satu bullet `Bulk E13`
19. Klik [Delete]
20. Verifikasi toast sukses "Success, group has been deleted."
21. Verifikasi `Bulk E13` dan `Bulk E13 Child` terhapus dari tabel dan sidebar
22. Buka Modal Changelog: Group, lalu ketik Search `Bulk E13`, tekan Enter
23. Verifikasi entri Action `Delete` untuk `Bulk E13` dan `Bulk E13 Child` tampil (satu entri per node)
24. Verifikasi tidak ada entri Action `Bulk Delete`
25. Klik `(←)` pada kotak Search, lalu tutup Modal Changelog: Group

## Notes

- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 5, 11, 13, 15, 22, 25: menutup modal atau dialog, membuka layar, ganti akun, dan memulihkan state.
- Search di Modal Changelog untuk menemukan entri target adalah langkah penghubung (R-16). Asersi absence entri `Bulk Delete` didahului anchor positif pada langkah 23 (entri `Delete` tampil di surface yang sama, 8b butir 2).
- Temuan untuk QA:
  - TC-268 Expected b menyebut "tanpa error" tanpa elemen error tertentu; spec memakai toast sukses sebagai bukti tidak ada error.
  - TC-981 Expected a menyebut dialog row-action single; spec mengasersi title dan bullet dialog.
