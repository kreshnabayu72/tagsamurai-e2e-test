---
id: TC-FA-TDC-E2E-034-expired-aksi-activate-deactivate-delete-dan-bulk-delete-ditolak-toast-baku
title: "Entitas Expired: Aksi Activate, Deactivate, Delete, dan Bulk Delete Ditolak dengan Toast Baku"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-880
  - TC-FA-TDC-881
  - TC-FA-TDC-882
  - TC-FA-TDC-883
coverage:
  web: automated
---

# Entitas Expired: Aksi Activate, Deactivate, Delete, dan Bulk Delete Ditolak dengan Toast Baku

## Prerequisites

- Mode: FE+BE.
- Aktor: Total Control pada company uji khusus automation berstatus Expired. Akun, email, dan company tidak tertulis di TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`; nilainya disediakan tim FE).
- Login di hook `before` spec ini sebagai Total Control pada company Expired; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data uji (di-seed fixture BE di hook `before`, dipulihkan di hook `after`; kunci di `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada dan disediakan tim FE): 7 class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) ditambah NB-OLD (Inactive, Used By 0); NB-3 dan NB-4 Active dengan Used By 0 dan tanpa Last Posted Tax Year. Tabel memuat 8 baris pada satu halaman.
- Status entitas Expired dibentuk fixture BE dan tidak diubah spec ini; kemampuan itu disediakan tim FE/BE.
- Kemampuan baca jumlah entri log (Changelog, System Log, dan Activity Log) per class lewat fixture BE, disediakan tim FE/BE; baseline dibaca tepat sebelum aksi tiap TC (8b.10, S-12).
- State global: tidak ada yang diubah bila penolakan berfungsi; hook `after` memulihkan dataset class dan sesi.
- Rujukan suite: `suite.md` (hook `before`, `beforeEach`, `after`; seed dan pemulihan lewat API).

## Test Steps

### TC-FA-TDC-880: Activate ditolak

1. Catat baseline jumlah entri Changelog, System Log, dan Activity Log untuk NB-OLD
2. Klik toggle `Active` baris NB-OLD
3. Klik `[Activate]` pada dialog
4. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tampil
5. Verifikasi toast tampil di kanan bawah
6. Verifikasi halaman tetap berada di tab Tax Depreciation Class tanpa pengalihan
7. Verifikasi status NB-OLD tetap Inactive
8. Verifikasi jumlah entri Changelog, System Log, dan Activity Log untuk NB-OLD sama dengan baseline
9. Tutup toast error

### TC-FA-TDC-881: Deactivate ditolak

10. Catat baseline jumlah entri Changelog, System Log, dan Activity Log untuk NB-4
11. Klik toggle `Active` baris NB-4
12. Klik `[Deactivate]` pada dialog
13. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tampil
14. Verifikasi toast tampil di kanan bawah
15. Verifikasi halaman tetap berada di tab Tax Depreciation Class tanpa pengalihan
16. Verifikasi status NB-4 tetap Active
17. Verifikasi jumlah entri Changelog, System Log, dan Activity Log untuk NB-4 sama dengan baseline
18. Tutup toast error

### TC-FA-TDC-882: Delete ditolak

19. Catat baseline jumlah entri Changelog, System Log, dan Activity Log untuk NB-4
20. Klik tombol ⋯ baris NB-4 lalu `Delete`
21. Klik `[Delete]` pada dialog
22. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tampil
23. Verifikasi toast tampil di kanan bawah
24. Verifikasi halaman tetap berada di tab Tax Depreciation Class tanpa pengalihan
25. Verifikasi class NB-4 tetap ada di tabel
26. Verifikasi jumlah entri Changelog, System Log, dan Activity Log untuk NB-4 sama dengan baseline
27. Tutup toast error

### TC-FA-TDC-883: Bulk Delete ditolak

28. Catat baseline jumlah entri Changelog, System Log, dan Activity Log untuk NB-3 dan NB-4
29. Centang baris NB-3 dan NB-4, klik `Delete`
30. Klik `[Delete]` pada dialog
31. Verifikasi toast error "Changes can't be saved while this workspace is suspended or expired." tampil
32. Verifikasi toast tampil di kanan bawah
33. Verifikasi halaman tetap berada di tab Tax Depreciation Class tanpa pengalihan
34. Verifikasi class NB-3 dan NB-4 tetap ada di tabel
35. Verifikasi jumlah entri Changelog, System Log, dan Activity Log untuk NB-3 dan NB-4 sama dengan baseline
36. Tutup toast error
37. Klik `Unselect All` pada Bulk Action Bar

## Notes

- Langkah penghubung (S-03): langkah 9, 18, 27, dan 36 menutup toast error sebelum toast identik diasersi lagi (R-12); langkah 37 membersihkan seleksi (S-09). Baris target ditemukan tanpa Search karena tabel memuat 8 baris pada satu halaman (dinyatakan di Prerequisites).
- S-05 dan prinsip 13g (pengecualian kelas h): asersi "tidak ada entri log baru" (langkah 8, 17, 26, dan 35) ditulis di spec ini sebagai `Verifikasi` selisih jumlah entri terhadap baseline per surface log (Changelog, System Log, Activity Log); toast error adalah anchor positif bahwa server sudah merespons (8b.2).
- Langkah 6, 15, 24, dan 33: TC tidak menyebut cara mengamati "tanpa pengalihan"; spec mengamati bahwa tab Tax Depreciation Class tetap tampil.
- Pembagian TC lintas spec: TC-FA-TDC-102 (edit lewat form ditolak dengan toast baku kelas h, S-05) ada di spec 264.
- Alasan spec melewati sekitar 35 langkah (37 langkah): satu topik (penolakan toast baku atas aksi tulis single dan bulk pada entitas Expired) pada dataset 8 baris yang sama dan satu kelas harness (h). Tiap blok memiliki baseline sendiri; satu-satunya langkah yang menyambung blok adalah penutupan toast error (langkah 9, 18, 27) dan pembersihan seleksi (langkah 37). Selisih dua langkah dari ambang tidak cukup untuk memecah blok single dan bulk yang berbagi dataset dan hook.
- Temuan untuk QA:
  - TC tidak menyebut akun, email, dan company Total Control untuk status Expired.
  - TC-FA-TDC-880 sampai 883 menyebut "entri log baru" tanpa menyebut surface log; spec memakai tiga surface log modul.
  - TC tidak menyebut label tombol pembatalan seleksi pada Bulk Action Bar; spec memakai `Unselect All` (S-09).
  - TC memakai class seed literal (NB-OLD, NB-3, NB-4) sebagai target aksi tulis yang ditolak; spec memakai dataset company khusus automation yang dipulihkan fixture karena modul ini tidak memiliki butir Lampiran A untuk nama literal.
