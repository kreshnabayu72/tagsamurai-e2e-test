---
id: TC-FA-TAG-E2E-282-pencatatan-activity-log-dan-system-log-aksi-receive-report-bagian-2
title: "Pencatatan Activity Log dan System Log Aksi Report TAG dan Decline Report"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1117
  - TC-FA-TAG-1118
  - TC-FA-TAG-1119
coverage:
  web: automated
---

# Pencatatan Activity Log dan System Log Aksi Report TAG dan Decline Report

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Staff Auditor (tidak memegang Manage asset & TAG) [SA_NOTAG] `staffAuditorTidakMemegangManageAssetTag_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_SA_NOTAG_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Akun aktor: Manage asset & TAG dengan Update di group Plant B [UP_PB] `manageAssetTagDenganUpdateDiGroupPlantB_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_UP_PB_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Dipakai pada blok TC-FA-TAG-1119 (ganti akun eksplisit).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Data (Pre-setup TC, tanpa suffix): task Existence Audit dengan item AST-0020 ('Excavator 20 Ton - 20', group Plant B) berstatus In Audit; Tag tunggal [RFID] `RF-00130` tanpa laporan terbuka (laporan terbuka Damaged dari Staff Auditor dibuat fixture sesuai kebutuhan TC).
- Akses Admin Console > Activity Log dan Global Settings > User (Detail User, tab System Log) oleh akun aktor tidak disebut TC; kemampuan membuka halaman itu dinyatakan sebagai kebutuhan akun (disediakan tim FE).
- Baseline jumlah entri Activity Log dan System Log Detail User pelaku dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama; asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan laporan Tag RF-00130 dan data aset ke keadaan awal lewat fixture backend, serta sesi ke akun default suite.
- State global yang diubah spec ini: status laporan Tag RF-00130. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1117: Report TAG menulis satu entri Activity Log

1. Buka modul Audit > Task Detail task Existence Audit, tab In Audit
2. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
3. Pilih Report Type "Damaged"
4. Isi Textarea "Note" dengan "Label retak"
5. Klik tombol [Submit]
6. Buka Admin Console > Activity Log
7. Filter entri terbaru
8. Verifikasi Activity Log memuat tepat satu entri baru untuk aksi ini dengan kolom Date terisi dan Modified By berisi nama pelaku aksi
9. Verifikasi tidak ada entri ganda untuk aksi yang sama

### TC-FA-TAG-1118: Report TAG menulis satu entri System Log pelaku

10. Pulihkan Tag RF-00130 tanpa laporan terbuka lewat fixture backend, lalu kembali ke Task Detail
11. Pilih row action "Report TAG" pada baris Excavator 20 Ton - 20
12. Pilih Report Type "Damaged"
13. Isi Textarea "Note" dengan "Label retak"
14. Klik tombol [Submit]
15. Buka Detail User pelaku aksi, tab System Log
16. Verifikasi System Log pelaku memuat tepat satu entri baru untuk aksi ini dengan kolom Date, Action, Object, Name, Field, Old Value, New Value terisi
17. Verifikasi tidak ada entri ganda untuk aksi yang sama
18. Ganti akun: logout dari akun Staff Auditor (tidak memegang Manage asset & TAG)
19. Login dengan akun Manage asset & TAG dengan Update di group Plant B [UP_PB] lalu buka Fixed Asset > TAG tab Paired; pulihkan laporan terbuka Damaged dari Staff Auditor pada Tag RF-00130 lewat fixture backend

### TC-FA-TAG-1119: Decline Report menulis satu entri Activity Log

20. Klik Asset Name "Excavator 20 Ton" pada baris group Plant B (Popup Assets)
21. Buka menu aksi baris Excavator 20 Ton - 20
22. Klik "Decline Report"
23. Isi Textarea "Reason" dengan "Tag masih terbaca"
24. Klik tombol [Submit]
25. Buka Admin Console > Activity Log
26. Filter entri terbaru
27. Verifikasi Activity Log memuat tepat satu entri baru untuk aksi ini dengan kolom Date terisi dan Modified By berisi nama pelaku aksi
28. Verifikasi tidak ada entri ganda untuk aksi yang sama

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 10, 18 dan 19 (memulihkan laporan lewat fixture dan kembali ke Task Detail, ganti akun eksplisit, S-07).
- Urutan: blok akun Staff Auditor (TC-FA-TAG-1117, 1118) mendahului blok akun UP_PB (TC-FA-TAG-1119) agar ganti akun hanya sekali.
- Asersi "tidak ada entri ganda" bukan kelas g: asersi jumlah entri terhadap baseline, didahului `Verifikasi` entri aksi yang tercatat.
- Temuan untuk QA:
  - TC-FA-TAG-1117 sampai 1119 menulis "Buka Detail User pelaku aksi" tanpa menyebut nama pelaku; spec memakai Detail User akun yang melakukan aksi pada blok itu.
  - TC-FA-TAG-1119 precondition menyebut laporan terbuka Damaged dari Staff Auditor; spec membuatnya lewat fixture backend sebelum blok akun UP_PB.
