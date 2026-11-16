---
id: TC-FA-TDC-E2E-032-suspended-aksi-single-activate-deactivate-delete-ditolak-toast-baku
title: "Entitas Suspended: Aksi Single Activate, Deactivate, dan Delete Ditolak dengan Toast Baku"
layer: ui-e2e
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-874
  - TC-FA-TDC-875
  - TC-FA-TDC-876
sourceRules: ["E-FATDC-62", "T-12", "R-04", "L-04", "R-05", "R-06", "L-05"]
smoke: []
dependsOn: []
trace:
  "E-FATDC-62": [4, 7, 8, 13, 16, 17, 22, 25, 26]
  "T-12": [4, 13, 22]
  "R-04": 7
  "L-04": [8, 17]
  "R-05": 16
  "R-06": 25
  "L-05": 26
anchor: [5, 6, 14, 15, 23, 24]
coverage:
  web: automated
---

# Entitas Suspended: Aksi Single Activate, Deactivate, dan Delete Ditolak dengan Toast Baku

## Prerequisites

- Mode: FE+BE.
- Aktor: Total Control pada company uji khusus automation berstatus Suspended. Akun, email, dan company tidak tertulis di TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan tim FE).
- Login di hook `before` spec ini sebagai Total Control pada company Suspended; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data uji (di-seed fixture BE di hook `before`, dipulihkan di hook `after`; kunci di `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada dan disediakan tim FE): 7 class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) ditambah NB-OLD (Inactive, Used By 0); NB-4 Active dengan Used By 0 dan tanpa Last Posted Tax Year. Tabel memuat 8 baris pada satu halaman.
- Status entitas Suspended dibentuk fixture BE dan tidak diubah spec ini; kemampuan itu disediakan tim FE/BE.
- Kemampuan baca jumlah entri log (Changelog, System Log, dan Activity Log) per class lewat fixture BE, disediakan tim FE/BE; baseline dibaca tepat sebelum aksi tiap TC (8b.10, S-12).
- State global: tidak ada yang diubah bila penolakan berfungsi; hook `after` memulihkan dataset class dan sesi.
- Rujukan suite: `suite.md` (hook `before`, `beforeEach`, `after`; seed dan pemulihan lewat API).

## Test Steps

### TC-FA-TDC-874: Activate ditolak

1. Catat baseline jumlah entri Changelog, System Log, dan Activity Log untuk NB-OLD
2. Klik toggle `Active` baris NB-OLD
3. Klik `[Activate]` pada dialog
4. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tampil
5. Verifikasi toast tampil di kanan bawah
6. Verifikasi halaman tetap berada di tab Tax Depreciation Class tanpa pengalihan
7. Verifikasi status NB-OLD tetap Inactive
8. Verifikasi jumlah entri Changelog, System Log, dan Activity Log untuk NB-OLD sama dengan baseline
9. Tutup toast error

### TC-FA-TDC-875: Deactivate ditolak

10. Catat baseline jumlah entri Changelog, System Log, dan Activity Log untuk NB-4
11. Klik toggle `Active` baris NB-4
12. Klik `[Deactivate]` pada dialog
13. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tampil
14. Verifikasi toast tampil di kanan bawah
15. Verifikasi halaman tetap berada di tab Tax Depreciation Class tanpa pengalihan
16. Verifikasi status NB-4 tetap Active
17. Verifikasi jumlah entri Changelog, System Log, dan Activity Log untuk NB-4 sama dengan baseline
18. Tutup toast error

### TC-FA-TDC-876: Delete ditolak

19. Catat baseline jumlah entri Changelog, System Log, dan Activity Log untuk NB-4
20. Klik tombol ⋯ baris NB-4 lalu `Delete`
21. Klik `[Delete]` pada dialog
22. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tampil
23. Verifikasi toast tampil di kanan bawah
24. Verifikasi halaman tetap berada di tab Tax Depreciation Class tanpa pengalihan
25. Verifikasi class NB-4 tetap ada di tabel
26. Verifikasi jumlah entri Changelog, System Log, dan Activity Log untuk NB-4 sama dengan baseline

## Notes

- Langkah penghubung (S-03): langkah 9 dan 18 menutup toast error sebelum toast identik diasersi lagi (R-12). Baris target ditemukan tanpa Search karena tabel memuat 8 baris pada satu halaman (dinyatakan di Prerequisites).
- S-05 dan prinsip 13g (pengecualian kelas h): asersi "tidak ada entri log baru" (langkah 8, 17, dan 26) ditulis di spec ini sebagai `Verifikasi` selisih jumlah entri terhadap baseline per surface log (Changelog, System Log, Activity Log); toast error pada langkah 4, 13, dan 22 adalah anchor positif bahwa server sudah merespons (8b.2).
- Langkah 6, 15, dan 24: TC tidak menyebut cara mengamati "tanpa pengalihan"; spec mengamati bahwa tab Tax Depreciation Class tetap tampil.
- Temuan untuk QA:
  - TC tidak menyebut akun, email, dan company Total Control untuk status Suspended.
  - TC-FA-TDC-874 sampai 876 menyebut "entri log baru" tanpa menyebut surface log; spec memakai tiga surface log modul (Changelog, System Log, Activity Log).
  - TC memakai class seed literal (NB-OLD, NB-4) sebagai target aksi tulis yang ditolak; spec memakai dataset company khusus automation yang dipulihkan fixture karena modul ini tidak memiliki butir Lampiran A untuk nama literal.
