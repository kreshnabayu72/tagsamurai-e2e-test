---
id: TC-FA-TDC-E2E-033-suspended-aksi-bulk-activate-deactivate-delete-ditolak-toast-baku
title: "Entitas Suspended: Aksi Bulk Activate, Deactivate, dan Delete Ditolak dengan Toast Baku"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-877
  - TC-FA-TDC-878
  - TC-FA-TDC-879
coverage:
  web: automated
---

# Entitas Suspended: Aksi Bulk Activate, Deactivate, dan Delete Ditolak dengan Toast Baku

## Prerequisites

- Mode: FE+BE.
- Aktor: Total Control pada company uji khusus automation berstatus Suspended. Akun, email, dan company tidak tertulis di TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan tim FE).
- Login di hook `before` spec ini sebagai Total Control pada company Suspended; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data uji (di-seed fixture BE di hook `before`, dipulihkan di hook `after`; kunci di `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada dan disediakan tim FE): 7 class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) ditambah NB-OLD dan NB-OLD2 (keduanya Inactive, Used By 0); NB-3 dan NB-4 Active dengan Used By 0 dan tanpa Last Posted Tax Year. Tabel memuat 9 baris pada satu halaman.
- Status entitas Suspended dibentuk fixture BE dan tidak diubah spec ini; kemampuan itu disediakan tim FE/BE.
- Kemampuan baca jumlah entri log (Changelog, System Log, dan Activity Log) per class lewat fixture BE, disediakan tim FE/BE; baseline dibaca tepat sebelum aksi tiap TC (8b.10, S-12).
- State global: tidak ada yang diubah bila penolakan berfungsi; hook `after` memulihkan dataset class dan sesi.
- Rujukan suite: `suite.md` (hook `before`, `beforeEach`, `after`; seed dan pemulihan lewat API).

## Test Steps

### TC-FA-TDC-877: Bulk Activate ditolak

1. Catat baseline jumlah entri Changelog, System Log, dan Activity Log untuk NB-OLD dan NB-OLD2
2. Centang baris NB-OLD dan NB-OLD2, klik `Activate`
3. Klik `[Activate]` pada dialog
4. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tampil
5. Verifikasi toast tampil di kanan bawah
6. Verifikasi halaman tetap berada di tab Tax Depreciation Class tanpa pengalihan
7. Verifikasi status NB-OLD dan NB-OLD2 tetap Inactive
8. Verifikasi jumlah entri Changelog, System Log, dan Activity Log untuk NB-OLD dan NB-OLD2 sama dengan baseline
9. Tutup toast error
10. Klik `Unselect All` pada Bulk Action Bar

### TC-FA-TDC-878: Bulk Deactivate ditolak

11. Catat baseline jumlah entri Changelog, System Log, dan Activity Log untuk NB-3 dan NB-4
12. Centang baris NB-3 dan NB-4, klik `Deactivate`
13. Klik `[Deactivate]` pada dialog
14. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tampil
15. Verifikasi toast tampil di kanan bawah
16. Verifikasi halaman tetap berada di tab Tax Depreciation Class tanpa pengalihan
17. Verifikasi status NB-3 dan NB-4 tetap Active
18. Verifikasi jumlah entri Changelog, System Log, dan Activity Log untuk NB-3 dan NB-4 sama dengan baseline
19. Tutup toast error
20. Klik `Unselect All` pada Bulk Action Bar

### TC-FA-TDC-879: Bulk Delete ditolak

21. Catat baseline jumlah entri Changelog, System Log, dan Activity Log untuk NB-3 dan NB-4
22. Centang baris NB-3 dan NB-4, klik `Delete`
23. Klik `[Delete]` pada dialog
24. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tampil
25. Verifikasi toast tampil di kanan bawah
26. Verifikasi halaman tetap berada di tab Tax Depreciation Class tanpa pengalihan
27. Verifikasi class NB-3 dan NB-4 tetap ada di tabel
28. Verifikasi jumlah entri Changelog, System Log, dan Activity Log untuk NB-3 dan NB-4 sama dengan baseline
29. Klik `Unselect All` pada Bulk Action Bar

## Notes

- Langkah penghubung (S-03, S-09): langkah 9 dan 19 menutup toast error sebelum toast identik diasersi lagi (R-12); langkah 10, 20, dan 29 membersihkan seleksi sebelum TC berikutnya. Baris target dipilih tanpa Search karena tabel memuat 9 baris pada satu halaman (dinyatakan di Prerequisites).
- S-05 dan prinsip 13g (pengecualian kelas h): asersi "tidak ada entri log baru" (langkah 8, 18, dan 28) ditulis di spec ini sebagai `Verifikasi` selisih jumlah entri terhadap baseline per surface log (Changelog, System Log, Activity Log); toast error pada langkah 4, 14, dan 24 adalah anchor positif bahwa server sudah merespons (8b.2).
- Langkah 6, 16, dan 26: TC tidak menyebut cara mengamati "tanpa pengalihan"; spec mengamati bahwa tab Tax Depreciation Class tetap tampil.
- Temuan untuk QA:
  - TC tidak menyebut akun, email, dan company Total Control untuk status Suspended.
  - TC-FA-TDC-877 sampai 879 menyebut "entri log baru" tanpa menyebut surface log; spec memakai tiga surface log modul.
  - TC tidak menyebut label tombol pembatalan seleksi pada Bulk Action Bar; spec memakai `Unselect All` (S-09).
  - TC memakai class seed literal (NB-OLD, NB-OLD2, NB-3, NB-4) sebagai target aksi tulis yang ditolak; spec memakai dataset company khusus automation yang dipulihkan fixture karena modul ini tidak memiliki butir Lampiran A untuk nama literal.
