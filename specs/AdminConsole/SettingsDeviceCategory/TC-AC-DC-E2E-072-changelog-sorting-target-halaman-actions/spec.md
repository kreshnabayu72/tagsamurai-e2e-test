---
id: TC-AC-DC-E2E-072-changelog-sorting-target-halaman-actions
title: "Modal Changelog Category: Perpindahan Target Sort, Nomor Halaman, dan Kolom Actions"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-192
  - TC-AC-DC-193
  - TC-AC-DC-194
  - TC-AC-DC-195
coverage:
  web: automated
---

# Modal Changelog Category: Perpindahan Target Sort, Nomor Halaman, dan Kolom Actions

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-192: Sort Modified By berdasarkan nama lengkap bukan format singkat

1. Klik ikon Changelog pada header Sidebar Category
2. Klik header Modified By sekali
3. Verifikasi baris Budi (6 baris) tampil sebelum baris Maya (6 baris)
4. Klik header Modified By sekali lagi
5. Verifikasi baris Maya tampil sebelum baris Budi
6. Klik header Modified By sekali lagi
7. Verifikasi indikator sort Modified By hilang
8. Verifikasi urutan kembali default Date Newest First

### TC-AC-DC-193: Berpindah target sort mereset kolom lama dan tidak mereset Search atau Filter

9. Ketik Search `kit`, tekan Enter
10. Klik ikon Filter, buka dropdown Action, centang "Create", klik `[Apply]`
11. Klik header Action sekali
12. Klik header Category sekali
13. Verifikasi indikator sort Action kembali netral
14. Verifikasi indikator sort Category ascending
15. Verifikasi kata kunci "kit" tetap aktif
16. Verifikasi filter Action "Create" tetap aktif dengan 3 baris

### TC-AC-DC-194: Mengganti sort mempertahankan nomor halaman

17. Tutup modal lewat icon `[×]`, lalu klik ikon Changelog pada header Sidebar Category
18. Klik halaman 2 pada pagination
19. Klik header Category sekali
20. Verifikasi tabel tetap berada di halaman 2
21. Verifikasi halaman 2 menampilkan 2 baris terakhir menurut Category A-Z (urutan dataset baru)

### TC-AC-DC-195: Kolom Actions kosong tidak memiliki ikon sort dan berfungsi sebagai trigger Column Visibility

22. Verifikasi kolom paling kanan tidak memiliki ikon sort
23. Klik ikon `⋯` pada header kolom paling kanan
24. Verifikasi overlay Column Visibility memuat 7 kolom data tanpa kolom Actions

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-192, 193, 194, 195). Tidak ada TC hanya-BE di spec ini.
- Pembagian TC lintas spec: TC-AC-DC-190 dan 191 (sort Field, Old Value, New Value) ada di spec 071.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah dari TC): langkah 17.
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
