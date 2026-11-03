---
id: TC-AC-DC-E2E-065-changelog-filter-date-dan-dropdown
title: "Modal Changelog Category: Filter Date Inklusif dan Opsi Dropdown Filter"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-171
  - TC-AC-DC-172
  - TC-AC-DC-173
  - TC-AC-DC-174
coverage:
  web: automated
---

# Modal Changelog Category: Filter Date Inklusif dan Opsi Dropdown Filter

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-171: Filter Date: rentang tanggal inklusif di kedua ujung

1. Klik ikon Changelog pada header Sidebar Category
2. Klik ikon Filter, pilih rentang Date 05/09/26 sampai 10/09/26, klik `[Apply]`
3. Verifikasi tabel menampilkan 4 baris: 05/09/26 (`Gateway Kit Plus`), 08/09/26 (`Wearable` Create), 09/09/26 (`Scanner Pro`), 10/09/26 (`Scanner Max`)
4. Verifikasi baris tanggal 03/09/26 dan 12/09/26 tidak tampil

### TC-AC-DC-172: Filter Date satu hari: Start sama dengan End menampilkan entri hari itu

5. Klik ikon Filter, klik `[Clear Field]`, pilih rentang Date 08/09/26 sampai 08/09/26, klik `[Apply]`
6. Verifikasi tabel menampilkan 1 baris (Create `Wearable`, 08/09/26)

### TC-AC-DC-173: Opsi dropdown Filter berasal dari data Changelog saat ini (DISTINCT)

7. Klik ikon Filter, klik `[Clear Field]`, klik `[Apply]`
8. Klik ikon Filter, buka dropdown Action
9. Verifikasi dropdown Action berisi tepat 3 opsi: Create, Delete, Edit
10. Buka dropdown Category
11. Verifikasi dropdown Category berisi 9 opsi nama snapshot yang tercatat: Gateway Kit, Gateway Kit Plus, Kit Lama, Kit Lama Anak, Scanner, Scanner Max, Scanner Pro, Tracker Seven, Wearable (termasuk nama node yang sudah dihapus atau diganti nama)
12. Verifikasi dropdown Category tidak memuat node tanpa entri log
13. Buka dropdown Modified By
14. Verifikasi dropdown Modified By berisi 2 opsi: pelaku Budi dan pelaku Maya

### TC-AC-DC-174: Search internal dropdown Action, Category, dan Modified By mempersempit daftar opsi

15. Buka dropdown Action, ketik `ed` pada kotak pencarian dropdown
16. Verifikasi dropdown Action menampilkan 1 opsi: Edit
17. Buka dropdown Category, ketik `KIT` pada kotak pencarian dropdown
18. Verifikasi dropdown Category menampilkan 4 opsi yang mengandung "kit" (case-insensitive): Gateway Kit, Gateway Kit Plus, Kit Lama, Kit Lama Anak
19. Buka dropdown Modified By, ketik `maya` pada kotak pencarian dropdown
20. Verifikasi dropdown Modified By menampilkan 1 opsi: Maya P

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-171, 172, 173, 174). Tidak ada TC hanya-BE di spec ini.
- TC-AC-DC-171 dan 172 memilih rentang tanggal lewat date range picker; TC tidak menyebut cara interaksi picker (mengetik atau memilih di kalender), spec menulis 'pilih rentang Date' mengikuti TC.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah dari TC): langkah 7.
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
  - TC-AC-DC-173 menulis 'pelaku Budi dan pelaku Maya' tanpa label opsi; label dropdown Modified By pada TC-AC-DC-174 adalah 'Maya P' (format singkat); spec mengikuti kalimat TC.
