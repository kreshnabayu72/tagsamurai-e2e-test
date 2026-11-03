---
id: TC-FA-RP-E2E-157-tab-read-only-search-filter-sort-download-setup-column-dan-2
title: "Tab Read Only: Search, Filter, Sort, Download, Setup Column, dan menu baris (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-535
  - TC-FA-RP-536
  - TC-FA-RP-537
  - TC-FA-RP-538
coverage:
  web: automated
---

# Tab Read Only: Search, Filter, Sort, Download, Setup Column, dan menu baris (2/2)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #37 (Tab Read Only empat baris) dan #36 (Tab Total Control sembilan baris; baris Rina Wulandari dipakai TC-FA-RP-538). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE): membaca berkas unduhan (nama berkas, kolom, jumlah baris).
- State yang diubah: konfigurasi kolom Setup Column Tab Read Only (kolom Division disembunyikan); hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).

## Test Steps

### Download Tab Read Only (TC-FA-RP-535)

1. Klik Tab `Read Only`
2. Klik ikon Download lalu `Download as CSV`
3. Verifikasi tidak ada toast sukses
4. Verifikasi berkas `Role-Permission-Read-Only.csv` terunduh berisi empat baris Read Only
5. Klik ikon Download lalu `Download as XLSX`
6. Verifikasi tidak ada toast sukses
7. Verifikasi berkas `Role-Permission-Read-Only.xlsx` terunduh

### Setup Column memakai kolom yang sama dengan Tab Total Control (TC-FA-RP-536)

8. Klik header `(⋯)` kolom Column Visibility, lalu klik `Setup Column...`
9. Verifikasi kolom bawaan tercentang: `Name`, `Position`, `Division`, `Status`, `Modified By`, `Last Updated`
10. Verifikasi kolom curated tidak tercentang: `Email`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Cost Center`, `Joined Date`, `Badge No`
11. Klik `(X)` untuk menutup popup

### Konfigurasi kolom terpisah dari Tab Total Control (TC-FA-RP-537)

12. Klik header `(⋯)` kolom Column Visibility, klik `Setup Column...`, hapus centang kolom `Division`, lalu klik `[Save]`
13. Klik Tab `Total Control`
14. Verifikasi Tab Total Control tetap menampilkan kolom Division (cache per tabel)

### Menu baris hanya memuat Remove (TC-FA-RP-538)

15. Klik Tab `Read Only`
16. Klik `[⋯]` pada baris Maya Anggraeni
17. Verifikasi menu hanya memuat `Remove` (ikon DeleteBin6Line, severity danger)
18. Verifikasi tidak ada Detail, Edit, atau aksi lain pada menu baris Maya Anggraeni
19. Tutup menu dengan Esc
20. Klik Tab `Total Control`
21. Klik `[⋯]` pada baris Rina Wulandari
22. Verifikasi menu hanya memuat `Remove` (ikon DeleteBin6Line, severity danger)
23. Verifikasi tidak ada Detail, Edit, atau aksi lain pada menu baris Rina Wulandari
24. Tutup menu dengan Esc

## Notes

- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab (langkah 1, 13, 15, 20); menutup popup Setup Column dengan `(X)` (langkah 11); membuka menu baris dan menutupnya dengan Esc (langkah 16, 19, 21, 24).
- Asersi "tidak ada toast sukses" (langkah 3 dan 6) diletakkan segera setelah pemicu dan sebelum asersi artefak; klik format menjadi anchor positif yang buktinya menyusul pada `Verifikasi` berkas terunduh (bagian 8b butir 11).
- Asersi berkas terbatas pada nama berkas, jumlah baris, dan nama kolom; isi sel tidak diasersi (kelas fungsional, prinsip 13f).
- Temuan untuk QA:
  - Precondition TC-FA-RP-535 sampai TC-FA-RP-538 menyebut Pre-setup #36 yang hanya dipakai pada langkah 20 sampai 24.
  - TC-FA-RP-537 Expected hanya menyebut Tab Total Control tetap menampilkan kolom Division; TC tidak menyebut bahwa Tab Read Only tidak menampilkannya, sehingga spec tidak mengasersinya.
  - TC-FA-RP-535 Expected b tidak menyebut jumlah baris berkas XLSX; spec mengasersi hanya nama berkas XLSX.
  - TC-FA-RP-538 Expected menyebut ikon `DeleteBin6Line` dan severity danger tanpa cara membacanya (atribut ikon atau kelas gaya); spec mengikuti teks TC.
