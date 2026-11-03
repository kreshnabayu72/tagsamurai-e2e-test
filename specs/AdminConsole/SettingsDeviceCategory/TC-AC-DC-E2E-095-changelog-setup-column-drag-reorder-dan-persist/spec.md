---
id: TC-AC-DC-E2E-095-changelog-setup-column-drag-reorder-dan-persist
title: "Modal Changelog Category: Setup Column Drag Reorder Kolom dan Persist Setelah Refresh"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-199
coverage:
  web: automated
---

# Modal Changelog Category: Setup Column Drag Reorder Kolom dan Persist Setelah Refresh

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Tabel "Kolom Seret ke Atas (urut)" (parameter langkah berulang):

  | Kolom |
  |---|
  | Date |
  | Action |
  | Category |
  | Field |
  | Old Value |
  | New Value |
  | Modified By |
- Kemampuan teknis (disediakan tim FE): menghapus preferensi kolom Changelog di browser aktor; simulasi seret-lepas baris kolom di modal Setup Column.
- State global yang diubah dan dipulihkan: preferensi kolom modal Changelog di browser aktor; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE, bukan `[Reset to Default]`) dan Changelog dipulihkan ke No 17.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-199: Setup Column: drag reorder kolom lalu Save dan persist setelah refresh

1. Klik ikon Changelog pada header Sidebar Category
2. Klik ikon `⋯` pada header kolom Actions, klik "Setup Column..."
3. Untuk setiap baris tabel "Kolom Seret ke Atas (urut)" (langkah 4 sampai 5):
4. Seret kolom pada modal Setup Column ke posisi paling atas daftar
5. Verifikasi kolom yang diseret menjadi kolom pertama pada live preview
6. Verifikasi urutan live preview: Modified By, New Value, Old Value, Field, Category, Action, Date
7. Klik `[Save]`
8. Tekan F5, lalu klik ikon Changelog pada header Sidebar Category
9. Verifikasi tabel menampilkan urutan kolom Modified By, New Value, Old Value, Field, Category, Action, Date

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-199). Tidak ada TC hanya-BE di spec ini.
- Langkah berulang per baris tabel di Prerequisites memakai idiom 'Untuk setiap kolom ... (langkah X sampai Y)'; jumlah langkah dihitung dengan ekspansi (8b.7). Langkah berulang: 4 sampai 5 (7 kolom).
- Pembagian TC lintas spec: TC-AC-DC-196, 197, dan 198 ada di spec 073.
- Urutan kolom hasil seret dihapus dari preferensi kolom di hook `after` (bukan `[Reset to Default]`).
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
  - TC-AC-DC-199 menyebut konfigurasi 'tersimpan' tanpa mekanisme penyimpanan; spec mengamatinya lewat F5 dan buka ulang modal (S-13).
