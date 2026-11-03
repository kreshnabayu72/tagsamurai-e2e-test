---
id: TC-FA-GRP-E2E-057-edit-function-disposal-group-ke-none-dan-assignable-dialog-change-function
title: "Edit Function Disposal Group ke None dan ke Assignable: Screening Dialog Change Function, [Save], dan [Cancel]"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-177
  - TC-FA-GRP-178
  - TC-FA-GRP-179
  - TC-FA-GRP-180
  - TC-FA-GRP-181
  - TC-FA-GRP-182
coverage:
  web: automated
---

# Edit Function Disposal Group ke None dan ke Assignable: Screening Dialog Change Function, [Save], dan [Cancel]

## Prerequisites

- Mode: FE+BE (backend nyata; TC-FA-GRP-178 dan TC-FA-GRP-181 menyimpan perubahan Function dan membaca jumlah aset node).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data Dinamis bersuffix `{runId}-057` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script): node `FN Disposal {runId}-057` (level 1, Function Disposal Group, punya aset aktif dan histori; Pre-setup tambahan "FN Disposal") di-seed lewat API di hook `before` beserta aset dan histori yang menunjuk node itu.
- Kemampuan teknis: pembacaan jumlah aset dan histori yang menunjuk node lewat fixture BE (disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD); pemulihan Function node ke Disposal Group lewat API di langkah 11.
- Pemulihan (hook `before` dan `after`): hapus lewat API node dengan suffix `{runId}-057` beserta aset dan histori seed.
- State global: tidak ada yang diubah.

## Test Steps

1. Catat jumlah aset dan histori yang menunjuk `FN Disposal {runId}-057` lewat fixture BE sebagai baseline, lalu ketik Search `FN Disposal {runId}-057`, tekan Enter

### TC-FA-GRP-177: Disposal Group ke None, screening Dialog Change Function

2. Buka elipsis (⋯) baris `FN Disposal {runId}-057`, klik Edit, pilih Function None, lalu klik [Save]
3. Verifikasi dialog konfirmasi non-blok title `Change Function`, Body diawali bullet `FN Disposal {runId}-057` lalu `This group will no longer appear as a destination in disposal transactions. Past disposal records for this group are not affected. Are you sure you want to save it?`, tombol [Cancel] (text, contrast) dan [Save] (filled, success)

### TC-FA-GRP-179: Disposal Group ke None, [Cancel] pada dialog kembali ke form

4. Klik [Cancel] pada dialog
5. Verifikasi dialog tertutup dan Popup Edit tetap terbuka dengan pilihan None dipertahankan
6. Verifikasi belum ada perubahan tersimpan dan tidak ada toast

### TC-FA-GRP-178: Disposal Group ke None, [Save] pada dialog menyimpan

7. Klik [Save] pada Popup Edit, lalu klik [Save] pada dialog
8. Verifikasi toast sukses `Success, group has been updated.`
9. Verifikasi badge dan dot sidebar `FN Disposal {runId}-057` berubah ke `—` (tanpa dot)
10. Verifikasi aset dan histori yang menunjuk node tetap menunjuk node yang sama dan datanya tidak berubah: jumlah sama dengan baseline langkah 1
11. Pulihkan Function `FN Disposal {runId}-057` ke Disposal Group lewat API
12. Muat ulang halaman dengan F5
13. Ketik Search `FN Disposal {runId}-057`, tekan Enter

### TC-FA-GRP-180: Disposal Group ke Assignable, screening Dialog Change Function

14. Buka elipsis (⋯) baris `FN Disposal {runId}-057`, klik Edit, pilih Function Assignable, lalu klik [Save]
15. Verifikasi dialog konfirmasi non-blok title `Change Function`, Body diawali bullet `FN Disposal {runId}-057` lalu `This group will no longer appear as a destination in disposal transactions — it will become available for asset registration and transfer instead. Past disposal records for this group are not affected. Are you sure you want to save it?`, tombol [Cancel] (text, contrast) dan [Save] (filled, success)

### TC-FA-GRP-182: Disposal Group ke Assignable, [Cancel] pada dialog kembali ke form

16. Klik [Cancel] pada dialog
17. Verifikasi dialog tertutup dan Popup Edit tetap terbuka dengan pilihan Assignable dipertahankan
18. Verifikasi belum ada perubahan tersimpan dan tidak ada toast

### TC-FA-GRP-181: Disposal Group ke Assignable, [Save] pada dialog menyimpan

19. Klik [Save] pada Popup Edit, lalu klik [Save] pada dialog
20. Verifikasi toast sukses `Success, group has been updated.`
21. Verifikasi badge dan dot sidebar `FN Disposal {runId}-057` berubah ke Assignable
22. Verifikasi aset dan histori yang menunjuk node tetap menunjuk node yang sama dan datanya tidak berubah: jumlah sama dengan baseline langkah 1
23. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: screening dialog, lalu [Cancel], lalu [Save] untuk tiap transisi dalam satu pembukaan popup (TC-FA-GRP-177, 179, 178; lalu TC-FA-GRP-180, 182, 181), sesuai S-10; berbeda dari urutan nomor TC sumber. Function dipulihkan ke Disposal Group lewat API (langkah 11) sebelum transisi kedua (S-09).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 1 (Catat jumlah aset dan histori yang menunjuk `FN Disposal {runId}-057` lewat fixture BE sebagai baseline, lalu ketik Search `FN Disposal {runId}-057`, tekan Enter); langkah 11 (Pulihkan Function `FN Disposal {runId}-057` ke Disposal Group lewat API); langkah 23 (Klik `(←)` pada kotak Search). Langkah 12 (Muat ulang halaman dengan F5) dan langkah 13 (Ketik Search `FN Disposal {runId}-057`, tekan Enter) menyegarkan baris tabel yang masih menampilkan Function lama sesudah pemulihan lewat API; F5 membuang kotak Search (S-14).
- Dialog konfirmasi (judul, Body, tombol) ditulis satu `Verifikasi` karena Expected TC menyebutnya utuh dalam butir a sampai c (S-01, dialog konfirmasi satu elemen).
- Temuan untuk QA:
  - TC-FA-GRP-178 dan TC-FA-GRP-181 Post Condition "Changelog Edit Field Function ..." dan "Dropdown konsumen berubah sesuai matriks transisi (Section 7)" tidak punya langkah observasi di TC; tidak diasersi di spec ini.
  - TC-FA-GRP-178 dan TC-FA-GRP-181 Expected c "Aset/histori ... tetap menunjuk node yang sama" tidak menyebut cara membaca; spec memakai pembacaan lewat fixture BE (disediakan tim FE/BE).

