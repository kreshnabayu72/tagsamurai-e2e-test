---
id: TC-AC-DC-E2E-075-changelog-setup-column-tutup-guard-dan-isolasi
title: "Modal Changelog Category: Setup Column Tutup Tanpa Save, Guard Satu Kolom, dan Isolasi Antar Tabel"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-203
  - TC-AC-DC-204
  - TC-AC-DC-205
coverage:
  web: automated
---

# Modal Changelog Category: Setup Column Tutup Tanpa Save, Guard Satu Kolom, dan Isolasi Antar Tabel

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE): menghapus preferensi kolom Changelog dan tabel Device Name di browser aktor; membaca daftar kolom dan status centang Setup Column tabel Device Name sebagai baseline.
- State global yang diubah dan dipulihkan: preferensi kolom modal Changelog di browser aktor; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE, bukan `[Reset to Default]`) dan Changelog dipulihkan ke No 17.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-203: Setup Column: tutup lewat icon X atau Esc membuang perubahan preview

1. Klik ikon Changelog pada header Sidebar Category
2. Klik ikon `⋯` pada header kolom Actions, klik "Setup Column..."
3. Uncheck kolom Field
4. Klik icon close `[×]` pada modal Setup Column tanpa Save
5. Verifikasi tabel menampilkan kolom Field setelah penutupan lewat icon close
6. Klik ikon `⋯` pada header kolom Actions, klik "Setup Column..."
7. Uncheck kolom Field, tekan Esc
8. Verifikasi tabel menampilkan kolom Field setelah penutupan lewat Esc
9. Tekan F5, lalu klik ikon Changelog pada header Sidebar Category
10. Verifikasi konfigurasi tersimpan terakhir tidak berubah: tabel menampilkan ketujuh kolom

### TC-AC-DC-204: Guard satu kolom tersisa: checkbox kolom terakhir tidak dapat di-uncheck

11. Klik ikon `⋯` pada header kolom Actions, klik "Setup Column..."
12. Uncheck kolom Action, Category, Field, Old Value, New Value, dan Modified By hingga hanya Date yang tercentang
13. Hover checkbox kolom Date
14. Verifikasi checkbox kolom Date disabled (tidak bisa di-uncheck)
15. Verifikasi tooltip checkbox kolom Date berisi "At least one column must remain visible."
16. Centang kembali kolom Action
17. Verifikasi semua checkbox kolom aktif
18. Klik icon close `[×]` pada modal Setup Column tanpa Save

### TC-AC-DC-205: Konfigurasi kolom Changelog Category tidak memengaruhi tabel lain

19. Tutup modal Changelog lalu catat baseline daftar kolom dan status centang Setup Column tabel Device Name
20. Klik ikon Changelog pada header Sidebar Category
21. Klik ikon `⋯` pada header kolom Actions, klik "Setup Column..."
22. Uncheck kolom Field, klik `[Save]`
23. Tutup modal Changelog lalu buka Setup Column pada tabel Device Name
24. Verifikasi daftar kolom dan status centang Setup Column tabel Device Name sama dengan baseline (konfigurasi tabel Device Name tidak berubah)
25. Tutup modal Setup Column tabel Device Name, klik ikon Changelog pada header Sidebar Category
26. Klik ikon `⋯` pada header kolom Actions, klik "Setup Column..."
27. Verifikasi kolom Field pada Changelog tetap tersembunyi

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-203, 204, 205). Tidak ada TC hanya-BE di spec ini.
- Konfigurasi kolom Field yang disembunyikan pada TC-AC-DC-205 dihapus dari preferensi browser di hook `after`.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah dari TC): langkah 18, 19, 25.
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
  - TC-AC-DC-203 butir b ('konfigurasi tersimpan terakhir di cache tidak berubah') tidak menyebut cara mengamati cache; spec mengamatinya lewat F5 dan buka ulang modal.
  - TC-AC-DC-205 tidak menyebut keadaan awal Setup Column tabel Device Name; spec mencatat baseline sebelum aksi dan membandingkannya sesudah (S-14).
  - TC-AC-DC-205 membuka Setup Column tabel Device Name tanpa menyebut triggernya; spec mengikuti kalimat TC.
