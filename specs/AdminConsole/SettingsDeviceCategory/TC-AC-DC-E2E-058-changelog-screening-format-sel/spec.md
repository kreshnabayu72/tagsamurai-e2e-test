---
id: TC-AC-DC-E2E-058-changelog-screening-format-sel
title: "Modal Changelog Category: Screening, Tooltip Toolbar, dan Format Sel"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DC-146
  - TC-AC-DC-148
  - TC-AC-DC-149
  - TC-AC-DC-147
coverage:
  web: automated
---

# Modal Changelog Category: Screening, Tooltip Toolbar, dan Format Sel

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Principal `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1, nama tampil `Budi Santoso`, Modified By `Budi S`; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Settings > Device > Device Name dibuka hook `beforeEach` suite.
- Data Pre-setup (hanya dibaca): Pohon Uji Kategori (No 14), Riwayat Changelog Uji (No 17: dua belas entri, Field `Category`, pelaku `Budi S` dan `Maya P`), dan General Settings entitas uji (No 19: Date Format `dd/MM/yy`, Time Format 24 jam, Timezone Asia/Jakarta). Nilai persis dibaca dari tabel Pre-setup TC dan tidak ditulis ulang di luar langkah.
- Pemulihan Changelog: kemampuan fixture BE (disediakan tim FE/BE; TC, PRD, dan LLD tidak mendefinisikan mekanismenya) memulihkan Riwayat Changelog entitas uji ke Pre-setup No 17 di hook `before` dan `after`. Jumlah total entri (12) dan pembagian halaman pada asersi bersumber dari No 17.
- Sesi API aktor dan fixture BE pemulihan pohon Category: lihat `suite.md`.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-AC-DC-146: Screening modal Changelog: Category dari atas ke bawah

1. Klik ikon Changelog pada header Sidebar Category
2. Verifikasi header modal menampilkan judul "Changelog: Category" dan icon close `[×]`
3. Verifikasi Table Tools menampilkan Search | Filter | Download dengan Search di ujung kiri
4. Verifikasi tidak ada tombol aksi tambah pada Table Tools
5. Verifikasi kolom tabel berurutan: Date (sortable) | Action (sortable) | Category (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Column Visibility (⋯) (unsortable, klik header membuka overlay Column Visibility, body kosong tanpa row action)
6. Verifikasi tabel read-only: tidak ada row action, tidak ada checkbox, dan tidak ada Bulk Action
7. Verifikasi halaman 1 menampilkan 10 baris data dengan urutan default Date Newest First
8. Verifikasi footer menampilkan Pagination default 10 data per halaman

### TC-AC-DC-148: Tooltip ikon toolbar modal Changelog dan tooltip Column Visibility

9. Hover ikon Search pada toolbar modal
10. Verifikasi tooltip ikon Search berisi "Search"
11. Hover ikon Filter pada toolbar modal
12. Verifikasi tooltip ikon Filter berisi "Filter"
13. Hover ikon Download pada toolbar modal
14. Verifikasi tooltip ikon Download berisi "Download"
15. Hover ikon `⋯` pada header kolom Actions
16. Verifikasi tooltip ikon `⋯` pada header kolom Actions berisi "Column Visibility"

### TC-AC-DC-149: Format sel Changelog: Date, Action, Category, dan Modified By dengan tooltip nama lengkap

17. Verifikasi kolom Date baris pertama (Delete `Kit Lama Anak` oleh Maya Putri) menampilkan tanggal "18/09/26" sesuai Date Format `dd/MM/yy` General Settings
18. Verifikasi kolom Date baris pertama menampilkan jam "16:05" sesuai Time Format 24 jam General Settings
19. Verifikasi kolom Action baris pertama menampilkan teks biasa "Delete" (bukan badge berwarna)
20. Verifikasi kolom Action baris Edit `Scanner Max` menampilkan teks biasa "Edit" (bukan badge berwarna)
21. Verifikasi kolom Category baris Edit `Scanner Max` menampilkan nama snapshot sesudah perubahan "Scanner Max"
22. Verifikasi kolom Modified By baris pertama menampilkan teks biasa "Maya P"
23. Hover sel Modified By pada baris pertama
24. Verifikasi tooltip sel Modified By baris pertama berisi nama lengkap "Maya Putri"

### TC-AC-DC-147: Modal Changelog ditutup lewat icon close atau Esc dan tidak lewat klik backdrop

25. Klik area backdrop di luar modal
26. Verifikasi modal Changelog tetap terbuka (klik backdrop diabaikan)
27. Tekan Esc
28. Verifikasi modal Changelog tertutup
29. Verifikasi halaman Device Name kembali dengan tree Sidebar Category utuh
30. Klik ikon Changelog pada header Sidebar Category
31. Klik icon close `[×]` pada modal
32. Verifikasi modal Changelog tertutup
33. Verifikasi halaman Device Name kembali dengan tree Sidebar Category utuh

## Notes

- Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md` (TC-AC-DC-146, 147, 148, 149). Tidak ada TC hanya-BE di spec ini.
- Urutan TC di spec: 146, 148, 149, lalu 147 (menutup modal di akhir, S-10); tooltip diasersi tepat setelah hover (8b.5).
- Semua data Pre-setup hanya dibaca; spec tidak melakukan aksi tulis.
- Temuan untuk QA:
  - Asersi spec ini bergantung pada isi persis Riwayat Changelog Pre-setup #17 (dua belas entri, termasuk angka total 12 dan pembagian halaman), sedangkan S-12 melarang angka total absolut pada audit trail permanen dan Lampiran A belum punya butir untuk modul ini. Spec mengikuti TC dan mengandalkan kemampuan fixture BE yang memulihkan Changelog entitas uji ke #17 sebelum dan sesudah spec. Perlu keputusan pengecualian Lampiran A (setara A-5) atau entitas uji khusus Changelog.
  - TC-AC-DC-149 Expected a menyebut baris pertama Delete `Kit Lama Anak` dan baris Edit `Scanner Max` tanpa menyebut posisi baris Edit; spec mencarinya di halaman 1 (urutan default Date Newest First).
