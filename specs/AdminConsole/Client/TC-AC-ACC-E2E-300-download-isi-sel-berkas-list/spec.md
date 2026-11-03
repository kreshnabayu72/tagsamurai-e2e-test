---
id: TC-AC-ACC-E2E-300-download-isi-sel-berkas-list
title: "Download Client List: Isi Sel Berkas CSV (Baris Sub-tab Aktif, Filter, Managed By, Group, Status Produk, Nilai Kosong, Last Updated)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-699
  - TC-AC-ACC-413
  - TC-AC-ACC-702
  - TC-AC-ACC-703
  - TC-AC-ACC-704
  - TC-AC-ACC-706
  - TC-AC-ACC-705
coverage:
  web: automated
---

# Download Client List: Isi Sel Berkas CSV (Baris Sub-tab Aktif, Filter, Managed By, Group, Status Produk, Nilai Kosong, Last Updated)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (A-01), password dari `Spectra.env.AC_TC_PASSWORD`. Login akun ini dilakukan di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, `AC_TC_PASSWORD`). Tidak ada ganti akun di tengah spec.
- Data Pre-setup: Tabel A (C-01 sampai C-14) tersedia sebagai fixture residen yang hanya dibaca; spec ini tidak mengubahnya.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Flag Guided Tooltip halaman List dan Detail diset true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan sekali di `suite.md`).
- Kemampuan teknis: mengamati berkas yang terunduh di browser (nama berkas) dan membaca isinya (CSV/XLSX) di sisi test runner; disediakan tim FE. Tidak butuh intercept atau jam server.
- Pemulihan preferensi Setup Column: hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`); kemampuan ini disediakan tim FE.
- Fixture residen: C-W3LST-3 `PT Tiga Mitra Uji` (Anchor CV Mitra Sejati, relasi CV Mitra Mandiri dan CV Mitra Lestari; tanpa subscription) dan C-14 `PT Uji Halaman 30`; C-09 `PT Baru Daftar` tanpa Company Email dan Industry. Isi sel berkas diasersi di spec ini (kelas f); nama berkas dan header di spec 299.
- Tidak butuh intercept atau jam server.

## Test Steps

### Baris berkas mengikuti sub-tab Active tanpa Search dan Filter (TC-AC-ACC-699)

1. Catat angka badge sub-tab Active (Search dan Filter tidak aktif, ukuran halaman 10)
2. Klik ikon Download lalu klik `Download as CSV`
3. Buka berkas `Clients.csv`
4. Verifikasi jumlah baris data berkas (di luar baris header) sama dengan angka badge sub-tab Active
5. Verifikasi jumlah baris data berkas lebih banyak dari 10 baris halaman
6. Verifikasi berkas memuat `PT Sejahtera Abadi` dan `PT Uji Halaman 30` (berada di halaman tabel yang berbeda)
7. Verifikasi berkas tidak memuat `PT Wahana Nusantara` (Suspended) dan `PT Karya Abadi` (Archived)

### Download mengikuti filter dan scope (TC-AC-ACC-413)

8. Klik Filter, pilih FAMS `Active`, lalu klik [Apply]
9. Klik ikon Download lalu klik `Download as CSV`, lalu buka berkas `Clients.csv`
10. Verifikasi berkas hanya memuat baris sub-tab Active hasil filter dalam scope aktor: `PT Sejahtera Abadi` ada
11. Verifikasi berkas tidak memuat `PT Teknologi Maju` (FAMS Grace) dan `PT Cahaya Baru` (FAMS Waiting for Approval)
12. Verifikasi kolom berkas sesuai spesifikasi: baris header memuat Company Name, Client Code, PIC Name, Managed By, Group, FAMS, SAMS, SIEM, Modified By, dan Last Updated
13. Klik Filter, klik [Clear Field], lalu klik [Apply]

### Sel Managed By dan Group (TC-AC-ACC-702 dan TC-AC-ACC-703)

14. Klik ikon Download lalu klik `Download as CSV`, lalu buka berkas `Clients.csv`
15. Verifikasi sel Managed By `PT Teknologi Maju`: `CV Mitra Sejati, CV Mitra Lestari` (tanpa teks `+1 more`)
16. Verifikasi sel Managed By `PT Tiga Mitra Uji`: `CV Mitra Sejati, CV Mitra Lestari, CV Mitra Mandiri` (tanpa teks `+2 more`)
17. Verifikasi sel Managed By `PT Baru Daftar`: `Direct`
18. Verifikasi sel Group `PT Sejahtera Abadi`: `Regional Barat > Area Jakarta`
19. Verifikasi sel Group `PT Baru Daftar`: `Regional Barat > Area Jakarta > Cabang Menteng`

### Sel FAMS, SAMS, SIEM dan Last Updated (TC-AC-ACC-704 dan TC-AC-ACC-706)

20. Catat teks sel Last Updated baris `PT Sejahtera Abadi` di tabel
21. Verifikasi sel FAMS, SAMS, SIEM `PT Sejahtera Abadi` pada berkas: `Active`, `Active`, `Active`
22. Verifikasi sel FAMS, SAMS, SIEM `PT Teknologi Maju` pada berkas: `Grace`, `No Subscription`, `No Subscription`
23. Verifikasi sel FAMS `PT Cahaya Baru` pada berkas: `Waiting for Approval`
24. Verifikasi sel FAMS `PT Mulai Esok` pada berkas: `Pending`
25. Verifikasi nilai sel Last Updated `PT Sejahtera Abadi` pada berkas sama dengan teks sel yang tampil di tabel (format tanggal-waktu General Settings)

### Nilai kosong ditulis tanda hubung (TC-AC-ACC-705)

26. Klik header kolom Actions `(⋯)` lalu centang Company Email dan Industry
27. Klik ikon Download lalu klik `Download as CSV`, lalu buka berkas `Clients.csv`
28. Verifikasi sel Company Email `PT Baru Daftar` berisi `-` (tanda hubung tunggal)
29. Verifikasi sel Industry `PT Baru Daftar` berisi `-` (tanda hubung tunggal)
30. Klik header kolom Actions `(⋯)` lalu hapus centang Company Email dan Industry (kembali ke default Hidden)

## Notes

- Kelas f (binary buffer): spec ini memuat asersi isi sel berkas; satu berkas CSV yang sama dibuka untuk TC-AC-ACC-702, 703, 704, dan 706 (satu unduhan, Download as CSV pada langkah awal blok TC-AC-ACC-702). Berkas TC-AC-ACC-699 dan TC-AC-ACC-413 diunduh terpisah karena memakai Search/Filter berbeda.
- Urutan TC disusun ulang (S-10): TC-AC-ACC-705 paling akhir karena mengubah visibilitas kolom (Company Email, Industry) lalu memulihkannya; TC-AC-ACC-704 dan TC-AC-ACC-706 berbagi unduhan yang sama dengan TC-AC-ACC-702/703 (tanpa langkah baru).
- Spec melewati sekitar 35 langkah; alasan: semua blok satu kelas harness dan dataset (isi berkas List) dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA
  - TC-AC-ACC-413: Data Uji kosong dan Langkah `Terapkan filter` tidak menyebut nilai; spec memakai FAMS `Active`. Expected `kolom sesuai spesifikasi` tanpa daftar; spec memakai 10 kolom default.
  - TC-AC-ACC-699: Expected `Jumlah baris ... lebih banyak dari 10 baris halaman` bergantung C-14 (30 baris) yang tidak disebut Precondition.
  - TC-AC-ACC-704: Data Uji baris `PT Cahaya Baru` dan `PT Mulai Esok` hanya menyebut FAMS; kolom SAMS/SIEM keduanya tidak diasersi.
