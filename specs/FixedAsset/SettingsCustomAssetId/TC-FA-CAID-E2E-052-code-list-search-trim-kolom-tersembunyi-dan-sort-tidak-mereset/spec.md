---
id: TC-FA-CAID-E2E-052-code-list-search-trim-kolom-tersembunyi-dan-sort-tidak-mereset
title: "Modal View Code List: Search Trim, Visibilitas Kolom, dan Sort Tidak Mereset Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CAID-125
  - TC-FA-CAID-126
  - TC-FA-CAID-131
coverage:
  web: automated
---

# Modal View Code List: Search Trim, Visibilitas Kolom, dan Sort Tidak Mereset Search

## Prerequisites

- Mode: FE+BE (isi Code List dibaca dari backend nyata).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Akun aktor: Total Control Company Alpha (Pre-setup No 1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`.
- Hook suite (`suite.md`): flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-asset-id` disetel `seen`; konfigurasi Company Alpha baseline B1 (Pre-setup No 10) dan aset A1 sampai A5 (Pre-setup No 11) dipulihkan lewat seed API sesi aktor; layar awal Fixed Asset > Settings > Asset Master > Custom Asset ID dibuka di `beforeEach`. Suite berjalan serial (`parallel: false`).
- Nilai data dirujuk lewat `Fixture.customAssetId.<kunci>` (berkas `fixtures/customAssetId.json` belum ada; prasyarat tahap script yang disediakan tim FE/BE).
- Master data Code List Company Alpha (Pre-setup No 28): Groups `Head Office` (HO), `Head Office > Floor 1` (F1), `Head Office > Floor 2` (F2), `Jakarta Office` (JKT), `Surabaya Branch` (SBY, Excess), `Warehouse` (WH); Categories `IT Equipment` (ITE), `IT Equipment > Laptop` (LAP), `Old Equipment` (OLD, Locked), `Printer` (PRN); Asset Names `Dell, Latitude 14"` (DL14), `LaserJet Pro` (LJP), `ThinkPad T490` (T490); Divisions `Finance` (FIN), `Human Resources` (HR), `Operations` (OPS); Accounts Active `Computer Equipment` (1210) dan `Office Furniture` (1220). Di-seed di hook `before` lewat sesi API aktor (kemampuan disediakan tim FE). Spec hanya membaca.
- Data Dinamis: tidak ada. State global: visibilitas kolom `Code` Modal View Code List diubah pada TC-FA-CAID-126 lalu ditampilkan kembali di spec; hook `after` spec ini menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE.

## Test Steps

### TC-FA-CAID-125: Query Search di-trim saat Enter

1. Klik tautan `[View Code List]`
2. Ketik Search `  floor  ` (spasi di awal dan akhir), tekan Enter
3. Verifikasi query dengan spasi tepi menemukan `Head Office > Floor 1` dan `Head Office > Floor 2`
4. Verifikasi isi input di layar tidak berubah (tetap `  floor  ` dengan spasi di awal dan akhir)
5. Ganti isi kotak search dengan `head  office` (dua spasi di tengah), tekan Enter
6. Verifikasi tabel menampilkan Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
7. Verifikasi query dengan dua spasi di tengah tidak dipecah (spasi di tengah dipertahankan)
8. Klik `(←)` pada kotak Search

### TC-FA-CAID-131: Mengubah sort tidak mereset Search

9. Ketik Search `floor`, tekan Enter
10. Klik header `Group Name` dua kali
11. Verifikasi kotak Search tetap berisi `floor`
12. Verifikasi tabel menampilkan `Head Office > Floor 2` lalu `Head Office > Floor 1` (Descending)
13. Klik header `Group Name` sekali lagi (sort kembali default)
14. Klik `(←)` pada kotak Search

### TC-FA-CAID-126: Search terikat visibilitas kolom

15. Klik header kolom Actions (⋯)
16. Hilangkan centang `Code`
17. Tekan `Esc` (menutup overlay Column Visibility)
18. Ketik Search `jkt`, tekan Enter
19. Verifikasi saat kolom `Code` disembunyikan, pencarian `jkt` tidak menemukan baris: tampil Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`
20. Klik header kolom Actions (⋯)
21. Centang `Code`
22. Tekan `Esc` (menutup overlay Column Visibility)
23. Ganti isi kotak search dengan `jkt`, tekan Enter
24. Verifikasi setelah kolom `Code` ditampilkan kembali, pencarian `jkt` menemukan `Jakarta Office / JKT`

## Notes

- Sumber: `fixed-asset/settings-custom-asset-id/TestCases/tc-settings-custom-asset-id.md`. 24 langkah.
- Urutan TC di dalam spec: TC-FA-CAID-125, 131, lalu 126. TC-FA-CAID-126 mengubah visibilitas kolom `Code` sehingga ditaruh paling akhir.
- Langkah penghubung (tanpa `Verifikasi`): langkah 8 dan 14 (klik `(←)` mengosongkan Search antar TC, S-09), langkah 13 (klik ketiga mengembalikan sort ke default), serta langkah 17 dan 22 (`Esc` menutup overlay Column Visibility sebelum Search; Esc menutup overlay paling atas lebih dulu, TC-FA-CAID-161).
- Pada TC-FA-CAID-125 dan 126 empty state `No results found` menjadi anchor bahwa Search sudah diproses; pencarian yang menemukan baris pada langkah sesudahnya membuktikan tabel sudah termuat.
- Pembagian TC lintas spec: TC-FA-CAID-121 dan 124 ada di spec 051; TC-FA-CAID-122 dan 123 ada di spec 064.
- Temuan untuk QA:
  - TC-FA-CAID-126 langkah kedua menyebut header kolom Actions (⋯) dan checkbox `Code` di overlay tanpa menyebut cara menutup overlay sebelum Search; spec memakai `Esc`.
  - TC-FA-CAID-131 tidak menyebut cara mengembalikan sort; spec memakai klik ketiga pada header `Group Name`.
