---
id: TC-FA-TAG-E2E-283-pencatatan-activity-log-dan-system-log-aksi-receive-report-bagian-3
title: "Pencatatan Activity Log dan System Log Aksi Decline Report dan Cancel Report"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1120
  - TC-FA-TAG-1121
  - TC-FA-TAG-1122
coverage:
  web: automated
---

# Pencatatan Activity Log dan System Log Aksi Decline Report dan Cancel Report

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Manage asset & TAG dengan Update di group Plant B [UP_PB] `manageAssetTagDenganUpdateDiGroupPlantB_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_UP_PB_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Akun aktor: Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG] `staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Dipakai pada blok TC-FA-TAG-1121 dan 1122 (ganti akun eksplisit).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Data (Pre-setup TC, tanpa suffix): aset AST-0020 ('Excavator 20 Ton - 20', group Plant B) dengan Tag tunggal `RF-00130` dan laporan terbuka Damaged dari Staff Auditor; task Existence Audit dengan item AST-0020.
- Akses Admin Console > Activity Log dan Global Settings > User (Detail User, tab System Log) oleh akun aktor tidak disebut TC; kemampuan membuka halaman itu dinyatakan sebagai kebutuhan akun (disediakan tim FE).
- Baseline jumlah entri Activity Log dan System Log Detail User pelaku dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama dan dibaca ulang pada langkah 12 dan 23 sesudah pemulihan fixture (butir A-18); asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: entri Changelog `Decline Report` per Tag (langkah 5); entri Changelog `Cancel Report` per Tag (langkah 16, 26); entri Activity Log (Admin Console) (langkah 16); entri System Log pelaku (langkah 5, 26).
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan laporan Tag RF-00130 dan data aset ke keadaan awal lewat fixture backend, serta sesi ke akun default suite.
- State global yang diubah spec ini: status laporan Tag RF-00130. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1120: Decline Report menulis satu entri System Log pelaku

1. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)
2. Buka menu aksi baris Excavator 20 Ton - 20
3. Klik "Decline Report"
4. Isi Textarea "Reason" dengan "Tag masih terbaca"
5. Klik tombol [Submit]
6. Tunggu aksi selesai (dialog "Decline Report" tertutup dan tombol aktif kembali)
7. Buka Detail User pelaku aksi, tab System Log
8. Verifikasi System Log pelaku memuat satu entri baru untuk aksi ini (selisih jumlah entri terhadap baseline hook `before`) dengan kolom Date, Action, Object, Name, Field, Old Value, New Value terisi
9. Verifikasi tidak ada entri ganda untuk aksi yang sama
10. Ganti akun: logout dari akun Manage asset & TAG dengan Update di group Plant B
11. Login dengan akun Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG]; pulihkan laporan terbuka Damaged dari Staff Auditor pada Tag RF-00130 lewat fixture backend
12. Catat jumlah entri Activity Log (Admin Console) sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)

### TC-FA-TAG-1121: Cancel Report menulis satu entri Activity Log

13. Buka modul Audit > Task Detail task Existence Audit
14. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 20
15. Isi Textarea "Reason" dengan "Tag ternyata terbaca"
16. Klik tombol [Cancel Report]
17. Tunggu aksi selesai (dialog "Cancel Report" tertutup dan tombol aktif kembali)
18. Buka Admin Console > Activity Log
19. Filter entri terbaru
20. Verifikasi Activity Log memuat satu entri baru untuk aksi ini (selisih jumlah entri terhadap baseline langkah 12) dengan kolom Date terisi dan Modified By berisi nama pelaku aksi
21. Verifikasi tidak ada entri ganda untuk aksi yang sama

### TC-FA-TAG-1122: Cancel Report menulis satu entri System Log pelaku

22. Pulihkan laporan terbuka Damaged dari Staff Auditor pada Tag RF-00130 lewat fixture backend, lalu kembali ke Task Detail
23. Catat jumlah entri System Log Detail User pelaku (akun Staff Auditor) sebagai baseline (dibaca lewat kemampuan baca, disediakan tim FE/BE)
24. Pilih row action "Cancel Report TAG" pada baris Excavator 20 Ton - 20
25. Isi Textarea "Reason" dengan "Tag ternyata terbaca"
26. Klik tombol [Cancel Report]
27. Tunggu aksi selesai (dialog "Cancel Report" tertutup dan tombol aktif kembali)
28. Buka Detail User pelaku aksi, tab System Log
29. Verifikasi System Log pelaku memuat satu entri baru untuk aksi ini (selisih jumlah entri terhadap baseline langkah 23) dengan kolom Date, Action, Object, Name, Field, Old Value, New Value terisi
30. Verifikasi tidak ada entri ganda untuk aksi yang sama

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 6, 10, 11, 12, 17, 22, 23 dan 27 (ganti akun eksplisit, S-07; memulihkan laporan terbuka lewat fixture antar TC, S-09). Langkah 6, 17 dan 27 adalah "Tunggu aksi selesai" (bagian 8b butir 8) karena sesudahnya terjadi pindah surface. Langkah 12 dan 23 adalah Catat jumlah baseline (butir A-18).
- Urutan: blok akun UP_PB (TC-FA-TAG-1120) mendahului blok akun Staff Auditor (TC-FA-TAG-1121, 1122) agar ganti akun hanya sekali.
- Asersi "tidak ada entri ganda" bukan kelas g: asersi jumlah entri terhadap baseline, didahului `Verifikasi` entri aksi yang tercatat.
- A-15: nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Decline Report` per Tag (langkah 5); entri Changelog `Cancel Report` per Tag (langkah 16, 26); entri Activity Log (Admin Console) (langkah 16); entri System Log pelaku (langkah 5, 26).
- Temuan untuk QA:
  - TC-FA-TAG-1120 sampai 1122 menulis "Buka Detail User pelaku aksi" tanpa menyebut nama pelaku; spec memakai Detail User akun yang melakukan aksi pada blok itu.
