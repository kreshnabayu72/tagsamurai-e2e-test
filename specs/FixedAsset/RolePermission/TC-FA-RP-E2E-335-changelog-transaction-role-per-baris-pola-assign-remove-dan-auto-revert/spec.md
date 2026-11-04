---
id: TC-FA-RP-E2E-335-changelog-transaction-role-per-baris-pola-assign-remove-dan-auto-revert
title: "Changelog Transaction Role per baris pola: Assign, Remove, dan Auto-Revert Total Control"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-1163
coverage:
  web: automated
---

# Changelog Transaction Role per baris pola: Assign, Remove, dan Auto-Revert Total Control

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Rahmawati, Pre-setup #2) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control).
- Hook suite (flag Guided Tooltip, pemulihan Pre-setup bersama, sesi API aktor) berlaku seperti di `suite.md` bagian "Hook suite"; spec ini tidak mengubahnya.
- Data Pre-setup (identitas dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` yang belum ada dan disediakan tim FE): #15 (Ahmad Fauzi, pengguna Standard tanpa tingkat akses; target Assign Total Control), #18 (pohon group: `IT Infrastructure`), #24 (`Company Changelog`, dirujuk TC; lihat Temuan untuk QA). Ahmad Fauzi di-seed ke state #15 lewat seeding API di hook `before` (kemampuan disediakan tim FE/BE, tanpa endpoint karangan).
- Data Dinamis: tidak ada data yang dibuat spec.
- Kemampuan teknis: membaca jumlah entri berdasarkan kombinasi kolom pada Changelog Transaction Role sub-tab `Disposal`, Changelog Tab Total Control, System Log aktor (Settings > User > Detail Siti Rahmawati > Tab System Log), dan Activity Log FAMS lewat kemampuan baca yang disediakan tim FE/BE (langkah 1 dan 19). Entri yang diasersi adalah selisih jumlah terhadap baseline, bukan baris teratas dan bukan total absolut (S-12).
- State yang diubah dan pemulihannya: Assign Total Control mengubah Ahmad Fauzi menjadi Total Control dengan baris pola Group Role dan Transaction Role; Remove baris Approver di `IT Infrastructure` sub-tab `Disposal` (D-04) melepas tier Total Control dan baris pola Transaction Role Ahmad Fauzi. Changelog, System Log, dan Activity Log bertambah entri (audit trail permanen, tidak dipulihkan). Hook `after` memulihkan Ahmad Fauzi ke state Pre-setup #15 lewat fixture backend yang disediakan tim FE/BE (TC: "dipulihkan ke state Pre-setup #15 oleh automation baseline").
- Env var yang dipakai: `FA_TC_PASSWORD`. Nama dan arti tercantum di `suite.md` bagian "Env password akun aktor". Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-1163: Log Transaction Role per baris pola untuk Assign, Remove, dan Auto-Revert Total Control

1. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Assign` dengan New Value `Ahmad Fauzi` untuk Field `Asset Admin — IT Infrastructure` dan untuk Field `Approver — IT Infrastructure` pada Changelog Transaction Role sub-tab `Disposal`; jumlah entri Action `Assign`, Object `Transaction Role`, New Value `Ahmad Fauzi` untuk kedua Field itu pada System Log aktor Siti Rahmawati dan pada Activity Log FAMS
2. Klik `[+ Assign]` di Tab `Total Control`
3. Ketik Search `Ahmad Fauzi`, tekan Enter pada popup Assign
4. Centang Ahmad Fauzi lalu klik `[Assign]`
5. Tunggu aksi selesai: popup Assign tertutup
6. Klik Tab `Transaction Role`
7. Klik node `IT Infrastructure` lalu sub-tab `Disposal`
8. Klik ikon Changelog pada Table Tools
9. Verifikasi Changelog Transaction Role memuat satu entri baru (jumlah entri kombinasi ini bertambah tepat satu terhadap baseline): Action `Assign`, Field `Asset Admin — IT Infrastructure`, Old Value `—`, New Value `Ahmad Fauzi`
10. Verifikasi Changelog Transaction Role memuat satu entri baru (jumlah entri kombinasi ini bertambah tepat satu terhadap baseline): Action `Assign`, Field `Approver — IT Infrastructure`, Old Value `—`, New Value `Ahmad Fauzi`
11. Verifikasi entri Field `Asset Admin — IT Infrastructure` dan entri Field `Approver — IT Infrastructure` tampil sebagai dua baris terpisah, bukan satu entri ringkasan
12. Tutup modal Changelog
13. Buka Settings > User > Detail Siti Rahmawati > Tab System Log
14. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru (jumlah entri kombinasi ini bertambah tepat satu terhadap baseline): Action `Assign`, Object `Transaction Role`, Field `Asset Admin — IT Infrastructure`, Old Value `—`, New Value `Ahmad Fauzi`
15. Verifikasi System Log aktor Siti Rahmawati memuat satu entri baru (jumlah entri kombinasi ini bertambah tepat satu terhadap baseline): Action `Assign`, Object `Transaction Role`, Field `Approver — IT Infrastructure`, Old Value `—`, New Value `Ahmad Fauzi`
16. Buka Activity Log FAMS (menu Activity Log)
17. Verifikasi Activity Log memuat satu entri baru (jumlah entri kombinasi ini bertambah tepat satu terhadap baseline): Action `Assign`, Object `Transaction Role`, Field `Asset Admin — IT Infrastructure`, Old Value `—`, New Value `Ahmad Fauzi`, Modified By `Siti R`
18. Verifikasi Activity Log memuat satu entri baru (jumlah entri kombinasi ini bertambah tepat satu terhadap baseline): Action `Assign`, Object `Transaction Role`, Field `Approver — IT Infrastructure`, Old Value `—`, New Value `Ahmad Fauzi`, Modified By `Siti R`
19. Catat baseline (aksi tanpa `Verifikasi`; baca lewat kemampuan baca yang disediakan tim FE/BE): jumlah entri Action `Remove`, Field `Approver — IT Infrastructure`, Old Value `Ahmad Fauzi` pada Changelog Transaction Role sub-tab `Disposal`; jumlah entri Action `Auto-Revert`, User Name `Ahmad Fauzi`, Field `Access Level` pada Changelog Tab `Total Control`
20. Buka Fixed Asset > Settings > Role & Permission, klik Tab `Transaction Role`, lalu klik node `IT Infrastructure` dan sub-tab `Disposal`
21. Klik `[⋯]` baris Ahmad Fauzi di section Approver lalu `Remove`
22. Klik `[Remove]` pada dialog konfirmasi `D-04`
23. Tunggu aksi selesai: dialog tertutup
24. Klik ikon Changelog pada Table Tools
25. Verifikasi Changelog Transaction Role memuat satu entri baru (jumlah entri kombinasi ini bertambah tepat satu terhadap baseline langkah 19): Action `Remove`, Field `Approver — IT Infrastructure`, Old Value `Ahmad Fauzi`, New Value `—`
26. Tutup modal Changelog
27. Klik Tab `Total Control`
28. Klik ikon Changelog di toolbar Tab `Total Control`
29. Verifikasi Changelog Tab Total Control memuat satu entri baru (jumlah entri kombinasi ini bertambah tepat satu terhadap baseline langkah 19): Action `Auto-Revert`, User Name `Ahmad Fauzi`, Field `Access Level`
30. Verifikasi entri `Auto-Revert` langkah 29 bernilai Modified By `Siti R` (aktor), bukan `System`
31. Tutup modal Changelog

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 31 langkah.
- Langkah penghubung (S-03, bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 1 dan 19 (pencatatan baseline, S-12), langkah 3 (Search kandidat di popup Assign, supaya Ahmad Fauzi pasti tampil pada Table User Picker berpaginasi; R-22), langkah 5 dan 23 (tunggu aksi selesai sebelum berpindah surface, bagian 8b butir 8), langkah 6, 7, 8, 12, 24, 26, 27, 28, dan 31 (membuka dan menutup Tab, node, sub-tab, dan modal Changelog), langkah 20 (kembali ke modul asal sesudah Settings > User dan Activity Log, S-14). Akun aktor pertama sudah login di hook `before` (S-07).
- Search tidak dipakai untuk menemukan baris Ahmad Fauzi pada langkah 21: section Approver `IT Infrastructure` sub-tab `Disposal` memuat empat baris header Pre-setup #19 ditambah baris pola, tidak melebihi satu halaman. Tab `Total Control` pada langkah 27 tidak mengasersi baris tertentu.
- Entri yang diasersi dikenali lewat kombinasi Action, Object, Field, dan nilai serta selisih jumlahnya terhadap baseline yang dicatat sebelum aksi pemicu; posisi baris dan total entri tidak diasersi (S-12, S-14). Baseline langkah 1 mendahului Assign; baseline langkah 19 mendahului Remove.
- Klausa Expected "bukan satu entri ringkasan" diasersi secara positif pada langkah 11 (dua entri terpisah per Field), bukan sebagai absence.
- Langkah 22: dialog konfirmasi `D-04` hanya dikonfirmasi; TC tidak memuat teks dialog sehingga tidak diasersi di spec ini (teks dialog diasersi di spec 324).
- Pembagian TC lintas spec: TC-FA-RP-1164 (notifikasi auto-revert varian Role Transaksi) ada di spec 336. Spec 322, 324, dan 342 merujuk TC-FA-RP-1163 dan TC-FA-RP-1164 sebagai tempat pembuktian log dan notifikasi.
- Nomor cadangan 349 dan 350 tidak dipakai.
- Temuan untuk QA:
  - TC-FA-RP-1163 langkah 2 tidak menyebut node untuk Changelog sub-tab `Disposal`; spec memakai `IT Infrastructure` karena Field entri yang diharapkan memuat `IT Infrastructure`.
  - TC-FA-RP-1163 merujuk Pre-setup #24 (`Company Changelog`, client terpisah dengan Total Control sendiri) bersama #15 dan #18; Pre-setup #15 dan #18 milik Company Alpha. Spec memakai akun Siti Rahmawati (`FA_TC_PASSWORD`) dan asersi relatif terhadap baseline; bila TC dimaksudkan berjalan di `Company Changelog`, akun dan password (`FA_CHANGELOG_TC_PASSWORD`) berubah.
  - Expected a menyebut "satu entri `Assign` per baris pola" dengan contoh (`mis.`) Asset Admin dan Approver di `IT Infrastructure`; spec hanya mengasersi dua contoh itu, bukan seluruh baris pola pada setiap node dan sub-tab.
  - Expected a menulis "(Modified By aktor)" setelah System Log dan Activity Log; spec mengasersi Modified By hanya pada Activity Log (kolom Modified By pada System Log aktor tidak dipastikan di TC).
  - Expected b tidak menyebut Old Value dan New Value entri `Auto-Revert` serta Modified By entri `Remove`; spec tidak mengasersinya.
  - Expected b tidak menyebut kolom User Name entri `Auto-Revert`; spec memakai `Ahmad Fauzi` untuk mengenali entri pada Changelog Tab Total Control.
  - TC menyebut "Ahmad Fauzi dipulihkan ke state Pre-setup #15 oleh automation baseline" tanpa langkah observasi; tidak diasersi. Sesudah Remove, baris pola Group Role menjadi baris reguler (D-04), sehingga pemulihan ke #15 perlu fixture backend.
  - Pernyataan Pre-setup bersama di `suite.md` belum menyebut Pre-setup #24.
