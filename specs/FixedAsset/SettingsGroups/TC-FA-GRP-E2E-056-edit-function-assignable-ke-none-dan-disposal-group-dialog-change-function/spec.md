---
id: TC-FA-GRP-E2E-056-edit-function-assignable-ke-none-dan-disposal-group-dialog-change-function
title: "Edit Function Assignable ke None dan ke Disposal Group: Screening Dialog Change Function, [Save], dan [Cancel]"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-171
  - TC-FA-GRP-172
  - TC-FA-GRP-173
  - TC-FA-GRP-174
  - TC-FA-GRP-175
  - TC-FA-GRP-176
coverage:
  web: automated
---

# Edit Function Assignable ke None dan ke Disposal Group: Screening Dialog Change Function, [Save], dan [Cancel]

## Prerequisites

- Mode: FE+BE (backend nyata; TC-FA-GRP-172 dan TC-FA-GRP-175 menyimpan perubahan Function dan membaca jumlah aset node).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Client automation Plan Professional (Pre-setup No 8) dengan jumlah group di bawah cap; pohon group Tabel A, termasuk Head Office (level 1) yang punya child Floor 2.
- Data Dinamis bersuffix `{runId}-056` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script): node `FN Assign {runId}-056` (level 1, Function Assignable, punya aset aktif dan histori; Pre-setup tambahan "FN Assign") di-seed lewat API di hook `before` beserta aset aktif dan histori yang menunjuk node itu.
- Kemampuan teknis: pembacaan jumlah aset dan histori yang menunjuk node lewat fixture BE (disediakan tim FE/BE; nama endpoint tidak disebut di TC dan PRD); pemulihan Function node ke Assignable lewat API di langkah 11.
- Pemulihan (hook `before` dan `after`): hapus lewat API node dengan suffix `{runId}-056` beserta aset dan histori seed.
- State global: tidak ada yang diubah.

## Test Steps

1. Catat jumlah aset dan histori yang menunjuk `FN Assign {runId}-056` lewat fixture BE sebagai baseline, lalu ketik Search `FN Assign {runId}-056`, tekan Enter

### TC-FA-GRP-171: Assignable ke None, screening Dialog Change Function

2. Buka elipsis (⋯) baris `FN Assign {runId}-056`, klik Edit, pilih Function None, lalu klik [Save]
3. Verifikasi dialog konfirmasi non-blok title `Change Function`, Body diawali bullet `FN Assign {runId}-056` lalu `This group will no longer appear as a destination when registering or transferring assets. Assets already in this group are not affected — they stay here as is. Are you sure you want to save it?`, tombol [Cancel] (text, contrast) dan [Save] (filled, success)

### TC-FA-GRP-173: Assignable ke None, [Cancel] pada dialog kembali ke form

4. Klik [Cancel] pada dialog
5. Verifikasi dialog tertutup dan Popup Edit tetap terbuka dengan pilihan None dipertahankan
6. Verifikasi belum ada perubahan tersimpan dan tidak ada toast

### TC-FA-GRP-172: Assignable ke None, [Save] pada dialog menyimpan

7. Klik [Save] pada Popup Edit, lalu klik [Save] pada dialog
8. Verifikasi toast sukses `Success, group has been updated.`
9. Verifikasi badge dan dot sidebar `FN Assign {runId}-056` berubah ke `—` (tanpa dot)
10. Verifikasi aset dan histori yang menunjuk node tetap menunjuk node yang sama dan datanya tidak berubah: jumlah sama dengan baseline langkah 1
11. Pulihkan Function `FN Assign {runId}-056` ke Assignable lewat API
12. Muat ulang halaman dengan F5
13. Ketik Search `FN Assign {runId}-056`, tekan Enter

### TC-FA-GRP-174: Assignable ke Disposal Group, screening Dialog Change Function

14. Buka elipsis (⋯) baris `FN Assign {runId}-056`, klik Edit, pilih Function Disposal Group, lalu klik [Save]
15. Verifikasi dialog konfirmasi non-blok title `Change Function`, Body diawali bullet `FN Assign {runId}-056` lalu `This group will no longer appear as a destination when registering or transferring assets — it will become a disposal destination instead. Assets already in this group are not affected — they stay here as is. Are you sure you want to save it?`, tombol [Cancel] (text, contrast) dan [Save] (filled, success)

### TC-FA-GRP-176: Assignable ke Disposal Group, [Cancel] pada dialog kembali ke form

16. Klik [Cancel] pada dialog
17. Verifikasi dialog tertutup dan Popup Edit tetap terbuka dengan pilihan Disposal Group dipertahankan
18. Verifikasi belum ada perubahan tersimpan dan tidak ada toast

### TC-FA-GRP-175: Assignable ke Disposal Group, [Save] pada dialog menyimpan

19. Klik [Save] pada Popup Edit, lalu klik [Save] pada dialog
20. Verifikasi toast sukses `Success, group has been updated.`
21. Verifikasi badge dan dot sidebar `FN Assign {runId}-056` berubah ke Disposal Group
22. Verifikasi aset dan histori yang menunjuk node tetap menunjuk node yang sama dan datanya tidak berubah: jumlah sama dengan baseline langkah 1
23. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Urutan TC: screening dialog, lalu [Cancel], lalu [Save] untuk tiap transisi dalam satu pembukaan popup (TC-FA-GRP-171, 173, 172; lalu TC-FA-GRP-174, 176, 175), sesuai S-10; berbeda dari urutan nomor TC sumber. Function dipulihkan ke Assignable lewat API (langkah 11) sebelum transisi kedua (S-09).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 1 (Catat jumlah aset dan histori yang menunjuk `FN Assign {runId}-056` lewat fixture BE sebagai baseline, lalu ketik Search `FN Assign {runId}-056`, tekan Enter); langkah 11 (Pulihkan Function `FN Assign {runId}-056` ke Assignable lewat API); langkah 23 (Klik `(←)` pada kotak Search). Langkah 12 (Muat ulang halaman dengan F5) dan langkah 13 (Ketik Search `FN Assign {runId}-056`, tekan Enter) menyegarkan baris tabel yang masih menampilkan Function lama sesudah pemulihan lewat API; F5 membuang kotak Search (S-14).
- Dialog konfirmasi (judul, Body, tombol) ditulis satu `Verifikasi` karena Expected TC menyebutnya utuh dalam butir a sampai c (S-01, dialog konfirmasi satu elemen).
- Temuan untuk QA:
  - TC-FA-GRP-172 dan TC-FA-GRP-175 Post Condition "Changelog Edit Field Function ..." dan "Dropdown konsumen berubah sesuai matriks transisi (Section 7)" tidak punya langkah observasi di TC; tidak diasersi di spec ini.
  - TC-FA-GRP-172 dan TC-FA-GRP-175 Expected c "Aset/histori ... tetap menunjuk node yang sama" tidak menyebut cara membaca; spec memakai pembacaan lewat fixture BE (disediakan tim FE/BE).
  - TC-FA-GRP-171 Expected b menyebut "bullet FN Assign"; spec memakai nama node bersuffix.

