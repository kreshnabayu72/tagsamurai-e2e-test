---
id: TC-FA-GRP-E2E-307-delete-leaf-yang-hanya-tercakup-baris-pola-gm-ancestor-dialog-normal-bukan-d-15
title: "Delete Leaf yang Hanya Tercakup Baris Pola GM Ancestor: Dialog Normal (Bukan D-15), Leaf Terhapus, Penugasan GM di Ancestor Tetap"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-GRP-1304
coverage:
  web: automated
---

# Delete Leaf yang Hanya Tercakup Baris Pola GM Ancestor: Dialog Normal (Bukan D-15), Leaf Terhapus, Penugasan GM di Ancestor Tetap

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup No 1 `totalControlGroups_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip, sesi API aktor, fixture BE, pemulihan state global): lihat `suite.md`. Suite berjalan serial (`parallel: false`).
- Akun user yang diamati (hanya dibaca lewat Settings > Role & Permission, tidak login): gmPatternLeaf Pre-setup No 34 `gmPatternLeaf_automated_{namaCompany}@qwertysystem.net` (tier Group Manager hanya di ancestor, tanpa Group Role lain). Nilai email nyata belum ditetapkan tim FE/QA (lihat Temuan untuk QA).
- Data Dinamis (Pre-setup tambahan No 24, tanpa aset aktif, di-seed lewat sesi API aktor di hook `before`, sisa dihapus di hook `after`): `Del GM Pat Root {runId}-307` (level 1, Function None) > `Del GM Pat Leaf {runId}-307`. Penugasan Group Manager gmPatternLeaf di-seed lewat API hanya di `Del GM Pat Root {runId}-307`, dan baris pola GM terbentuk di `Del GM Pat Leaf {runId}-307` dari penugasan ancestor itu; tidak ada Group Role eksplisit maupun penugasan GM lain di `Del GM Pat Leaf {runId}-307`, dan tidak ada user lain ter-assign. Mekanisme seeding disediakan tim FE/BE tanpa endpoint karangan (S-13); penugasan dilepas dan sisa node (`Del GM Pat Root {runId}-307`) dihapus di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE tanpa endpoint karangan): membaca tab Group Manager dan tab Group Role per user dan per node di Settings > Role & Permission dengan sidebar Group Tree.

## Test Steps

1. Baca tab Group Role user gmPatternLeaf pada `Del GM Pat Leaf {runId}-307` lewat kemampuan baca modul Role & Permission
2. Verifikasi `Del GM Pat Leaf {runId}-307` memuat baris pola GM gmPatternLeaf (precondition terpenuhi)
3. Baca tab Group Manager user gmPatternLeaf lewat kemampuan baca modul Role & Permission
4. Verifikasi penugasan Group Manager gmPatternLeaf tercatat pada `Del GM Pat Root {runId}-307`
5. Ketik Search `Del GM Pat Leaf {runId}-307`, tekan Enter
6. Buka elipsis `Del GM Pat Leaf {runId}-307`, pilih Delete
7. Verifikasi dialog dengan title "Delete Group", bullet `Del GM Pat Leaf {runId}-307`, isi "Are you sure you want to delete it? This action cannot be undone." (bukan varian warning D-15; baris pola GM gmPatternLeaf dari penugasan ancestor bukan assignment eksplisit dan tidak dihitung kondisi 5)
8. Klik [Delete]
9. Verifikasi toast sukses `Success, group has been deleted.`
10. Verifikasi Groups List menampilkan empty state "No results found" untuk Search `Del GM Pat Leaf {runId}-307`
11. Ganti isi kotak search dengan `Del GM Pat Root {runId}-307`, tekan Enter
12. Verifikasi Groups List memuat baris `Del GM Pat Root {runId}-307` (Del GM Pat Root tetap ada)
13. Klik `(←)` pada kotak Search
14. Baca tab Group Manager user gmPatternLeaf lewat kemampuan baca modul Role & Permission
15. Verifikasi penugasan Group Manager gmPatternLeaf tetap tercatat pada `Del GM Pat Root {runId}-307`

## Notes

- Spec memiliki 15 langkah. Langkah penghubung (S-03): langkah 1, 3, 14 (observasi lewat kemampuan baca), langkah 5 dan 11 (Search untuk menemukan baris target, R-16; client memiliki lebih dari 10 node level 1 sehingga posisi baris di halaman 1 tidak diandalkan), dan langkah 13 (menutup Search). Aksi hapus diletakkan sesudah pembacaan precondition (S-10).
- Keputusan product owner 2026-11-05 (NC-12 butir 2): guard Delete kondisi 5 hanya menghitung assignment eksplisit; baris pola GM turunan penugasan ancestor tidak dihitung, sehingga dialog normal. Konfirmasi PM masih diminta.
- Temuan untuk QA:
  - Email Pre-setup No 34 (gmPatternLeaf) belum punya nilai nyata (TC: perlu data tim FE/QA); mekanisme seeding penugasan Group Manager dan terbentuknya baris pola GM di leaf tidak ditegaskan di TC.
