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
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman dibuka di langkah pertama (hook suite `beforeEach` dikecualikan, lihat `suite.md`). Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Pelaku kedua memakai sesi API (token tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE, lihat `suite.md`); langkah pemicunya tidak memuat asersi di sesi itu.
- Data (Pre-setup TC, tanpa suffix): task Existence Audit dengan item AST-0020 ('Excavator 20 Ton - 20', group Plant B) dan Tag tunggal `RF-00130` dengan laporan terbuka Damaged dari Staff Auditor (blok TC-FA-TAG-1129); entri Changelog Report TAG untuk AST-0020 (Plant B) dan aset AST-0501 (Plant A) (blok TC-FA-TAG-1131).
- Baseline jumlah entri Changelog Paired TAG dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama; asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14). Baseline jumlah entri Changelog Asset Detail aset AST-0020 (Action `Report TAG`) dibaca pada langkah 6, sebelum pemicu langkah 10 (butir A-18).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 10, 27); entri Changelog `Decline Report` per Tag (langkah 25); entri Changelog `Cancel Report` per Tag (langkah 4). Jumlah entri Changelog dibaca sebagai baseline lewat kemampuan baca; log itu permanen dan tidak dipulihkan fixture, dan asersi entri baru memakai selisih terhadap baseline: butir A-18.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan laporan Tag RF-00130 dan data aset ke keadaan awal lewat fixture backend, serta sesi ke akun default suite.
- State global yang diubah spec ini: status laporan Tag RF-00130. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1129: aksi Cancel Report

1. Buka modul Audit > Task Detail task Existence Audit
2. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 20
3. Isi Textarea "Reason" dengan "Tag ternyata terbaca"
4. Klik tombol [Cancel Report]
5. Tunggu aksi selesai (dialog "Cancel Report" tertutup dan tombol aktif kembali)

### TC-FA-TAG-1130: aksi Report TAG Damaged

6. Catat jumlah entri Changelog Asset Detail aset AST-0020 dengan Action `Report TAG` sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)
7. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
8. Pilih Report Type "Damaged"
9. Isi Textarea "Note" dengan "Label retak"
10. Klik tombol [Submit]
11. Tunggu aksi selesai (dialog "Report TAG" tertutup dan tombol aktif kembali)
12. Ganti akun: logout dari akun Staff Auditor (tidak memegang Manage asset & TAG)
13. Login dengan akun Total Control [TC] lalu buka Fixed Asset > TAG tab Paired

### TC-FA-TAG-1129: pembacaan Changelog Cancel Report

14. Klik tombol "Changelog"
15. Verifikasi satu entri baru dengan Action "Cancel Report", Name "Excavator 20 Ton - 20", Field "Report Status", Old Value "Open", New Value "Canceled", dan Modified By pelaku Cancel Report
16. Tutup Modal Changelog

### TC-FA-TAG-1130: Changelog Asset Detail

17. Buka Asset > Asset Detail aset AST-0020
18. Klik "Changelog"
19. Verifikasi Modal Changelog Asset Detail memuat satu entri baru (selisih jumlah entri Action "Report TAG" terhadap baseline langkah 6) dengan Action "Report TAG", Field "Report Type", Old Value "—", New Value "Damaged"

### TC-FA-TAG-1132: entri Changelog lama tidak berubah setelah laporan dibuka lagi

20. Pulihkan laporan terbuka Damaged dari Staff Auditor pada Tag RF-00130 lewat fixture backend, lalu buka Fixed Asset > TAG tab Paired
21. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)
22. Buka menu aksi baris Excavator 20 Ton - 20
23. Klik "Decline Report"
24. Isi Textarea "Reason" dengan "Tag masih terbaca"
25. Klik tombol [Submit]
26. Tunggu aksi selesai (dialog "Decline Report" tertutup dan tombol aktif kembali)
27. Pelaku kedua (Staff Auditor) lewat sesi API melaporkan RF-00130 sebagai "Missing" dengan Note "Hilang lagi" hingga laporan tersimpan
28. Klik tombol "Changelog" pada halaman Tag
29. Verifikasi entri "Decline Report" (Open menjadi Declined) tetap tampil apa adanya
30. Verifikasi entri baru "Report TAG" dengan New Value "Missing" muncul sebagai entri terpisah; tidak ada entri lama yang ditimpa

### TC-FA-TAG-1131: Changelog Report TAG sesuai scope group

31. Ganti akun: logout dari akun Total Control
32. Login dengan akun Manage asset & TAG (Read) dengan assign group Plant A [MR_APA] lalu buka Fixed Asset > TAG tab Paired
33. Klik tombol "Changelog"
34. Verifikasi entri aset AST-0501 (Plant A) tampil
35. Verifikasi entri aset AST-0020 (Plant B) tidak tampil

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 5, 6, 11, 12, 13, 16, 20, 26, 31 dan 32 (ganti akun eksplisit, S-07; menutup modal dan menyiapkan laporan terbuka lewat fixture antar TC, S-09). Langkah 5, 11 dan 26 adalah "Tunggu aksi selesai" (bagian 8b butir 8) karena sesudahnya terjadi pindah surface, ganti akun atau permintaan langsung (fixture atau sesi API). Langkah 6 adalah Catat jumlah baseline (butir A-18).
- Urutan (S-10): aksi Staff Auditor TC-FA-TAG-1129 dan 1130 dijalankan berturut-turut sebelum ganti akun; pembacaan Changelog TC-FA-TAG-1129 dan 1130 menyusul oleh Total Control, lalu TC-FA-TAG-1132, lalu TC-FA-TAG-1131 (akun MR_APA) di akhir.
- Pelaku kedua pada TC-FA-TAG-1132 memakai sesi API karena hanya memicu laporan baru dan tidak diasersi di sesinya (R-20).
- Absence TC-FA-TAG-1131 (entri AST-0020 tidak tampil): didahului `Verifikasi` entri AST-0501 sebagai anchor positif (bagian 8b butir 2).
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Report TAG` per Tag (langkah 10, 27); entri Changelog `Decline Report` per Tag (langkah 25); entri Changelog `Cancel Report` per Tag (langkah 4).
- Temuan untuk QA:
  - TC-FA-TAG-1131 menyebut akun "Manage asset & TAG (Read) dengan assign group Plant A" [MR_APA] yang membaca Changelog Paired TAG; spec mengikuti TC.
  - TC-FA-TAG-1132 langkah TC ke-7 ("Login sbg Staff Auditor lalu laporkan") adalah pemicu; spec memakai pelaku kedua lewat sesi API tanpa asersi di sesinya.
