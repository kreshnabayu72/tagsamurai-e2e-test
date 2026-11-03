---
id: TC-FA-TAG-E2E-286-pencatatan-changelog-report-decline-cancel-bagian-3
title: "Pencatatan Changelog Cancel Report, Asset Detail, Scope Group, dan Entri Lama Tidak Berubah"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1129
  - TC-FA-TAG-1130
  - TC-FA-TAG-1131
  - TC-FA-TAG-1132
coverage:
  web: automated
---

# Pencatatan Changelog Cancel Report, Asset Detail, Scope Group, dan Entri Lama Tidak Berubah

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG] `staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Akun aktor: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Dipakai untuk membaca Changelog dan menjalankan Decline Report (ganti akun eksplisit).
- Akun aktor: Manage asset & TAG (Read) dengan assign group Plant A [MR_APA] `manageAssetTagReadDenganAssignGroupPlantA_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_MR_APA_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Dipakai pada blok TC-FA-TAG-1131 (ganti akun eksplisit).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE, lihat `suite.md`); langkah pemicunya tidak memuat asersi di sesi itu.
- Data (Pre-setup TC, tanpa suffix): task Existence Audit dengan item AST-0020 ('Excavator 20 Ton - 20', group Plant B) dan Tag tunggal `RF-00130` dengan laporan terbuka Damaged dari Staff Auditor (blok TC-FA-TAG-1129); entri Changelog Report TAG untuk AST-0020 (Plant B) dan aset AST-0501 (Plant A) (blok TC-FA-TAG-1131).
- Baseline jumlah entri Changelog Paired TAG dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama; asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan laporan Tag RF-00130 dan data aset ke keadaan awal lewat fixture backend, serta sesi ke akun default suite.
- State global yang diubah spec ini: status laporan Tag RF-00130. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1129: aksi Cancel Report

1. Buka modul Audit > Task Detail task Existence Audit
2. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 20
3. Isi Textarea "Reason" dengan "Tag ternyata terbaca"
4. Klik tombol [Cancel Report]

### TC-FA-TAG-1130: aksi Report TAG Damaged

5. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
6. Pilih Report Type "Damaged"
7. Isi Textarea "Note" dengan "Label retak"
8. Klik tombol [Submit]
9. Ganti akun: logout dari akun Staff Auditor (tidak memegang Manage asset & TAG)
10. Login dengan akun Total Control [TC] lalu buka Fixed Asset > TAG tab Paired

### TC-FA-TAG-1129: pembacaan Changelog Cancel Report

11. Klik tombol "Changelog"
12. Verifikasi satu entri baru dengan Action "Cancel Report", Name "Excavator 20 Ton - 20", Field "Report Status", Old Value "Open", New Value "Canceled", dan Modified By pelaku Cancel Report
13. Tutup Modal Changelog

### TC-FA-TAG-1130: Changelog Asset Detail

14. Buka Asset > Asset Detail aset AST-0020
15. Klik "Changelog"
16. Verifikasi Modal Changelog Asset Detail memuat entri Action "Report TAG", Field "Report Type", Old Value "—", New Value "Damaged"

### TC-FA-TAG-1132: entri Changelog lama tidak berubah setelah laporan dibuka lagi

17. Pulihkan laporan terbuka Damaged dari Staff Auditor pada Tag RF-00130 lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired
18. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)
19. Buka menu aksi baris Excavator 20 Ton - 20
20. Klik "Decline Report"
21. Isi Textarea "Reason" dengan "Tag masih terbaca"
22. Klik tombol [Submit]
23. Pelaku kedua (Staff Auditor) lewat sesi API melaporkan RF-00130 sebagai "Missing" dengan Note "Hilang lagi" hingga laporan tersimpan
24. Klik tombol "Changelog" pada halaman Tag
25. Verifikasi entri "Decline Report" (Open menjadi Declined) tetap tampil apa adanya
26. Verifikasi entri baru "Report TAG" dengan New Value "Missing" muncul sebagai entri terpisah; tidak ada entri lama yang ditimpa

### TC-FA-TAG-1131: Changelog Report TAG sesuai scope group

27. Ganti akun: logout dari akun Total Control
28. Login dengan akun Manage asset & TAG (Read) dengan assign group Plant A [MR_APA] lalu buka Fixed Asset > TAG tab Paired
29. Klik tombol "Changelog"
30. Verifikasi entri aset AST-0501 (Plant A) tampil
31. Verifikasi entri aset AST-0020 (Plant B) tidak tampil

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 9, 10, 13, 17, 27 dan 28 (ganti akun eksplisit, S-07; menutup modal dan menyiapkan laporan terbuka lewat fixture antar TC, S-09).
- Urutan (S-10): aksi Staff Auditor TC-FA-TAG-1129 dan 1130 dijalankan berturut-turut sebelum ganti akun; pembacaan Changelog TC-FA-TAG-1129 dan 1130 menyusul oleh Total Control, lalu TC-FA-TAG-1132, lalu TC-FA-TAG-1131 (akun MR_APA) di akhir.
- Pelaku kedua pada TC-FA-TAG-1132 memakai sesi API karena hanya memicu laporan baru dan tidak diasersi di sesinya (R-20).
- Absence TC-FA-TAG-1131 (entri AST-0020 tidak tampil): didahului `Verifikasi` entri AST-0501 sebagai anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-TAG-1131 menyebut akun "Manage asset & TAG (Read) dengan assign group Plant A" [MR_APA] yang membaca Changelog Paired TAG; spec mengikuti TC.
  - TC-FA-TAG-1132 langkah TC ke-7 ("Login sbg Staff Auditor lalu laporkan") adalah pemicu; spec memakai pelaku kedua lewat sesi API tanpa asersi di sesinya.
