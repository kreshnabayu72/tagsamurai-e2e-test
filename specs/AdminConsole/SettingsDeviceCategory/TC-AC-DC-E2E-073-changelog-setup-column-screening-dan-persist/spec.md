---
id: TC-AC-DC-E2E-073-changelog-setup-column-screening-dan-persist
title: "Modal Changelog Category: Screening Overlay Column Visibility dan Setup Column, Hide, dan Persist"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-196
  - TC-AC-DC-197
  - TC-AC-DC-198
coverage:
  web: automated
---

# Modal Changelog Category: Screening Overlay Column Visibility dan Setup Column, Hide, dan Persist

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Tabel "Kolom Uncheck" (parameter langkah berulang):

  | Kolom |
  |---|
  | Date |
  | Action |
  | Category |
  | Field |
  | Old Value |
  | New Value |
- Kemampuan teknis (disediakan tim FE): menghapus preferensi kolom Changelog di browser aktor (cache per tabel).
- State global yang diubah dan dipulihkan: preferensi kolom modal Changelog di browser aktor; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE, bukan `[Reset to Default]`) dan Changelog dipulihkan ke No 17.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-196: Screening overlay Column Visibility: daftar kolom, default, dan akses Setup Column

1. Klik ikon Changelog pada header Sidebar Category
2. Klik ikon `⋯` pada header kolom Actions
3. Verifikasi overlay menempel pada trigger tanpa backdrop blocking
4. Verifikasi overlay memuat daftar 7 kolom: Date, Action, Category, Field, Old Value, New Value, Modified By
5. Verifikasi setiap kolom tercentang
6. Verifikasi checkbox setiap kolom enabled (Hideable)
7. Verifikasi setiap baris kolom memiliki drag handle untuk reorder
8. Verifikasi item "Setup Column..." berada di bagian bawah overlay

### TC-AC-DC-197: Screening modal Setup Column dan live preview

9. Klik "Setup Column..."
10. Verifikasi judul modal "Setup Column"
11. Verifikasi deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns."
12. Verifikasi icon close `[×]` tampil
13. Verifikasi daftar 7 kolom tercentang (Hideable)
14. Verifikasi setiap baris kolom memiliki drag handle
15. Verifikasi setiap baris kolom memiliki icon Pin
16. Verifikasi live preview: tabel di balik modal merefleksikan urutan header dan data sel yang sama
17. Verifikasi tombol `[Reset to Default]` (text) dan `[Save]` (filled) rata kanan di footer
18. Verifikasi tidak ada tombol `[Cancel]`

### TC-AC-DC-198: Setup Column: uncheck dan check kolom data pada modal lalu Save dan persist setelah refresh

19. Untuk setiap baris tabel "Kolom Uncheck" (langkah 20 sampai 21):
20. Uncheck kolom pada modal Setup Column
21. Verifikasi kolom yang di-uncheck langsung hilang pada live preview
22. Klik `[Save]`
23. Verifikasi tabel hanya menampilkan kolom Modified By
24. Tekan F5, lalu klik ikon Changelog pada header Sidebar Category
25. Verifikasi konfigurasi kolom tetap sama setelah refresh: tabel hanya menampilkan kolom Modified By
26. Klik ikon `⋯` pada header kolom Actions, klik "Setup Column..."
27. Centang kembali keenam kolom pada tabel "Kolom Uncheck", klik `[Save]`
28. Verifikasi tabel menampilkan kembali ketujuh kolom

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-196, 197, 198). Tidak ada TC hanya-BE di spec ini.
- Langkah berulang per baris tabel di Prerequisites memakai idiom 'Untuk setiap kolom ... (langkah X sampai Y)'; jumlah langkah dihitung dengan ekspansi (8b.7). Langkah berulang: 20 sampai 21 (6 kolom).
- Alasan melewati sekitar 35 langkah: seluruh blok satu kelas harness (fungsional, satu permukaan Setup Column modal Changelog) dan tiap TC membuka Setup Column dari keadaan konfigurasi tersimpan yang dipulihkan lebih dulu, sehingga kegagalan satu TC tidak membuat TC lain kehilangan makna; langkah ulang per kolom ditentukan TC.
- Pembagian TC lintas spec: TC-AC-DC-199 (drag reorder dan persist) ada di spec 095.
- Konfigurasi kolom TC-AC-DC-198 dikembalikan ke tujuh kolom pada akhir TC itu; sisa preferensi kolom dihapus di hook `after` (bukan `[Reset to Default]`).
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
  - TC-AC-DC-198 menyebut konfigurasi 'tersimpan di cache browser' tanpa mekanisme penyimpanan; spec mengamatinya lewat F5 dan buka ulang modal (S-13: tidak mengarang endpoint).
