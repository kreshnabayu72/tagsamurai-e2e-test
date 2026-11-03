---
id: TC-AC-DC-E2E-096-changelog-setup-column-pin-kolom-dan-persist
title: "Modal Changelog Category: Setup Column Pin Kolom Membekukan Kolom dan Persist Setelah Refresh"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-200
coverage:
  web: automated
---

# Modal Changelog Category: Setup Column Pin Kolom Membekukan Kolom dan Persist Setelah Refresh

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Tabel "Kolom Pin" (parameter langkah berulang):

  | Kolom |
  |---|
  | Date |
  | Action |
  | Category |
  | Field |
  | Old Value |
  | New Value |
  | Modified By |
- Kemampuan teknis (disediakan tim FE): menghapus preferensi kolom Changelog di browser aktor; scroll horizontal tabel Changelog.
- State global yang diubah dan dipulihkan: preferensi kolom modal Changelog di browser aktor; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE, bukan `[Reset to Default]`) dan Changelog dipulihkan ke No 17.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-200: Setup Column: pin kolom membekukan kolom saat tabel di-scroll horizontal

1. Klik ikon Changelog pada header Sidebar Category
2. Klik ikon `⋯` pada header kolom Actions, klik "Setup Column..."
3. Untuk setiap baris tabel "Kolom Pin" (langkah 4 sampai 7):
4. Klik icon Pin kolom pada modal Setup Column
5. Verifikasi icon Pin kolom aktif
6. Klik icon Pin kolom sekali lagi
7. Verifikasi icon Pin kolom non-aktif
8. Klik icon Pin pada kolom Date dan Action
9. Klik `[Save]`
10. Scroll tabel secara horizontal
11. Verifikasi kolom Date dan Action tetap di kiri (beku) saat tabel di-scroll horizontal
12. Tekan F5, lalu klik ikon Changelog pada header Sidebar Category
13. Verifikasi pin kolom Date tetap berlaku setelah refresh
14. Verifikasi pin kolom Action tetap berlaku setelah refresh

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-200). Tidak ada TC hanya-BE di spec ini.
- Langkah berulang per baris tabel di Prerequisites memakai idiom 'Untuk setiap kolom ... (langkah X sampai Y)'; jumlah langkah dihitung dengan ekspansi (8b.7). Langkah berulang: 4 sampai 7 (7 kolom).
- Alasan melewati sekitar 35 langkah: satu TC, satu kelas harness (fungsional), dan langkah ulang per kolom (7 kolom x 4 langkah) ditentukan TC; tidak ada blok lain yang dapat dipisah.
- Pembagian TC lintas spec: TC-AC-DC-201 dan 202 ada di spec 074.
- Pin Date dan Action dihapus dari preferensi kolom di hook `after`.
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
