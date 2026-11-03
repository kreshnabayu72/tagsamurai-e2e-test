---
id: TC-AC-DC-E2E-074-changelog-setup-column-pin-dan-reset
title: "Modal Changelog Category: Setup Column Batas Pin Ketiga dan Reset to Default"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-201
  - TC-AC-DC-202
coverage:
  web: automated
---

# Modal Changelog Category: Setup Column Batas Pin Ketiga dan Reset to Default

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE): menghapus preferensi kolom Changelog di browser aktor; simulasi seret-lepas baris kolom di modal Setup Column.
- State global yang diubah dan dipulihkan: preferensi kolom modal Changelog di browser aktor; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE, bukan `[Reset to Default]`) dan Changelog dipulihkan ke No 17.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-201: Setup Column: pin ke-4 dinonaktifkan dengan tooltip batas

1. Klik ikon Changelog pada header Sidebar Category
2. Klik ikon `⋯` pada header kolom Actions, klik "Setup Column..."
3. Klik icon Pin pada kolom Date, Action, dan Category
4. Hover icon Pin pada kolom Field
5. Verifikasi icon Pin kolom Field disabled
6. Verifikasi tooltip icon Pin kolom Field berisi "Maximum 3 columns can be pinned at once. Unpin another column first."
7. Klik icon Pin pada kolom Category untuk unpin
8. Verifikasi icon Pin kolom Field aktif kembali

### TC-AC-DC-202: Setup Column: Reset to Default mengembalikan konfigurasi bawaan setelah Save

9. Klik icon close `[×]` pada modal Setup Column tanpa Save
10. Klik ikon `⋯` pada header kolom Actions, klik "Setup Column..."
11. Uncheck kolom Field dan seret kolom Modified By ke atas daftar, klik `[Save]`
12. Klik ikon `⋯` pada header kolom Actions, klik "Setup Column..."
13. Klik `[Reset to Default]`
14. Verifikasi preview setelah Reset menampilkan 7 kolom
15. Verifikasi urutan preview: Date, Action, Category, Field, Old Value, New Value, Modified By
16. Klik `[Save]`
17. Tekan F5, lalu klik ikon Changelog pada header Sidebar Category
18. Verifikasi tabel memakai konfigurasi default setelah Save
19. Verifikasi konfigurasi default tetap berlaku setelah refresh

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-201, 202). Tidak ada TC hanya-BE di spec ini.
- Pembagian TC lintas spec: TC-AC-DC-200 (pin kolom dan persist) ada di spec 096.
- Pin yang diatur TC-AC-DC-201 tidak disimpan (modal ditutup tanpa Save); konfigurasi TC-AC-DC-202 dihapus dari preferensi kolom di hook `after`.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah dari TC): langkah 9.
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
  - TC-AC-DC-202 menyebut 'Reset to Default' tanpa menyatakan apakah preferensi tersimpan dihapus; spec mengasersi tampilan dan persist setelah F5.
