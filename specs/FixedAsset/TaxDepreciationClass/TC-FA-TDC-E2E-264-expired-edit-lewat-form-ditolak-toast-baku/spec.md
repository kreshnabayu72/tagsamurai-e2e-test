---
id: TC-FA-TDC-E2E-264-expired-edit-lewat-form-ditolak-toast-baku
title: "Entitas Expired: Edit lewat Form Ditolak dengan Toast Baku"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-102
coverage:
  web: automated
---

# Entitas Expired: Edit lewat Form Ditolak dengan Toast Baku

## Prerequisites

- Mode: FE+BE.
- Aktor: Total Control pada company uji khusus automation berstatus Expired. Akun, email, dan company tidak tertulis di TC (lihat Temuan untuk QA); disediakan tim FE. Password lewat `Spectra.env.FA_TC_PASSWORD` (nama env belum terdaftar di `executionConfig.environmentVariables` dan `.env.example`; didaftarkan tim FE).
- Login di hook `before` spec ini sebagai Total Control pada company Expired; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Data uji (di-seed fixture BE di hook `before`, dipulihkan di hook `after`; kunci di `Fixture.fixedAssetTaxDepreciationClass`, fixture belum ada dan disediakan tim FE): 7 class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) belum diubah. Tabel memuat 7 baris pada satu halaman. Class Name baru NB-2: `Bukan bangunan – Kelompok 2 Revisi`.
- Status entitas Expired dibentuk fixture BE dan tidak diubah spec ini; kemampuan itu disediakan tim FE/BE.
- Kemampuan baca jumlah entri log (Changelog, System Log, dan Activity Log) per class lewat fixture BE, disediakan tim FE/BE; baseline dibaca tepat sebelum aksi (8b.10, S-12).
- Kemampuan browser: dialog `beforeunload` ditangani hook suite `beforeEach` (jaring pengaman form dirty).
- State global: tidak ada yang diubah bila penolakan berfungsi; hook `after` memulihkan dataset class dan sesi.
- Rujukan suite: `suite.md` (hook `before`, `beforeEach`, `after`; seed dan pemulihan lewat API).

## Test Steps

### TC-FA-TDC-102: Edit lewat form ditolak

1. Catat baseline jumlah entri Changelog, System Log, dan Activity Log untuk NB-2
2. Klik Class Code NB-2
3. Catat Class Name NB-2 yang tersimpan pada field Drawer
4. Ubah Class Name menjadi `Bukan bangunan – Kelompok 2 Revisi`
5. Klik `[Save]`
6. Verifikasi muncul toast error: `Changes can't be saved while this workspace is suspended or expired.`
7. Kembalikan Class Name ke nilai tersimpan yang dicatat pada langkah 3
8. Tutup Drawer dengan `[×]`
9. Verifikasi Class Name NB-2 pada tabel tidak berubah
10. Verifikasi jumlah entri Changelog, System Log, dan Activity Log untuk NB-2 sama dengan baseline

## Notes

- Langkah penghubung (S-03): langkah 3 mencatat nilai tersimpan; langkah 7 mengembalikan field Drawer yang dirty ke nilai tersimpan sebelum Drawer ditutup (S-09) sehingga `[×]` pada langkah 8 tidak memicu dialog `Unsaved Changes`. Baris target ditemukan tanpa Search karena tabel memuat 7 baris pada satu halaman (dinyatakan di Prerequisites).
- S-05 dan prinsip 13g (pengecualian kelas h): Expected TC-FA-TDC-102 adalah toast baku kelas h, bukan ketiadaan log saja; asersi "tidak ada entri log baru" (langkah 10) ditulis di spec ini sebagai `Verifikasi` selisih jumlah entri terhadap baseline per surface log (Changelog, System Log, Activity Log). Toast error langkah 6 adalah anchor positif bahwa server sudah merespons (8b.2). `Verifikasi` log ditaruh sesudah langkah 9 karena Class Name tabel baru teramati setelah Drawer ditutup (8b.5).
- Pembagian TC lintas spec: penolakan Activate, Deactivate, Delete, dan Bulk Delete pada entitas Expired ada di spec 034.
- Temuan untuk QA:
  - TC tidak menyebut akun, email, dan company Total Control untuk status Expired.
  - TC-FA-TDC-102 menyebut "entri log baru" tanpa menyebut surface log; spec memakai tiga surface log modul.
  - TC-FA-TDC-102 tidak menyebut Class Name awal NB-2 dan keadaan Drawer setelah penolakan; spec mencatat nilai tersimpan dari field Drawer dan mengasumsikan Drawer tetap terbuka dengan input dipertahankan.
  - TC memakai class seed literal (NB-2) sebagai target aksi tulis yang ditolak; spec memakai dataset company khusus automation yang dipulihkan fixture karena modul ini tidak memiliki butir Lampiran A untuk nama literal.
