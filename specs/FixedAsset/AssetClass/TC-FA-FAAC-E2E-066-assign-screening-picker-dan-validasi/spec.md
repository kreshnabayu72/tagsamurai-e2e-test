---
id: TC-FA-FAAC-E2E-066-assign-screening-picker-dan-validasi
title: "Screening Dialog Assign Asset Names, Filter Picker, Search Kosong, dan Validasi Tanpa Pilihan"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAC-149
  - TC-FA-FAAC-150
  - TC-FA-FAAC-155
  - TC-FA-FAAC-168
  - TC-FA-FAAC-169
coverage:
  web: automated
---

# Screening Dialog Assign Asset Names, Filter Picker, Search Kosong, dan Validasi Tanpa Pilihan

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`; password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Flag Guided Tooltip diatur hook suite.
- Data milik spec (seed di hook `before` lewat API, dihapus di hook `after`; kode literal, lihat Notes): Asset Class Active tanpa Asset Name ter-assign, Class Code `ANCHOR-066`, Class Name `Anchor Class {runId}-066` (disebut "anchor").
- Data Pre-setup bernama literal (seed idempotent, dipulihkan oleh fixture BE di hook `before` dan `after`): Asset Name tanpa Asset Class: Forklift 3T (6 aset aktif; Machinery > Warehouse; Label Warehouse, Insured), Forklift 5T (2 aset aktif; Machinery > Warehouse; Label Warehouse), Laptop Standard (120 aset aktif; IT > Devices; IT, Portable), Pallet Jack Electric (0 aset aktif), Meeting Table (0 aset aktif); Asset Name 'Delivery Van' (9 aset aktif) ter-assign ke 'Vehicles' (VEHICLES) dan 'Office Chair' (0 aset aktif) ter-assign ke 'Office Equipment (New)' (OFFICE-NEW). Nilai mengacu ke `Fixture.fixed-asset-asset-class.<kunci>` (fixture belum ada, disediakan tim FE). Data uji Search: "zzzz".
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): seed dan pemulihan lewat fixture BE; fixture BE yang meng-assign seluruh Asset Name company ke Asset Class lain (blok TC-168) dan memulihkannya di hook `after`.
- State global: keanggotaan Asset Name tanpa Asset Class berubah pada blok TC-168; dipulihkan di hook `after`.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Klik link Class Code `ANCHOR-066`, lalu klik tab "Asset Names"

### TC-FA-FAAC-149: Screening Dialog Assign Asset Names pada Asset Class Active mode Edit

2. Klik tombol "+ Assign Asset Names"
3. Verifikasi dialog ukuran LG berjudul "Assign Asset Names to Anchor Class {runId}-066"
4. Verifikasi dialog memiliki tombol [✕]
5. Verifikasi dialog tanpa ikon severity
6. Verifikasi toolbar dialog: checkbox "Without asset class only" tercentang di sisi kiri, Search dengan placeholder "Search asset name...", dan tombol Filter
7. Verifikasi kolom tabel picker: Asset Name, Category, Label, Current Class, Assets
8. Verifikasi baris terurut Asset Name A-Z (kelima Asset Name seed tampil berurutan relatif)
9. Verifikasi seluruh baris menampilkan "—" pada Current Class (hanya berisi Asset Name tanpa Asset Class)
10. Verifikasi Asset Name yang sudah berada di Asset Class ini tidak ditampilkan
11. Verifikasi checkbox baris belum ada yang tercentang
12. Verifikasi ringkasan menampilkan "0 to assign" tanpa bagian "to move"
13. Verifikasi Effective From dan pratinjau dampak Hidden
14. Verifikasi footer berisi [Cancel] dan [Assign]
15. Verifikasi [Assign] Enabled

### TC-FA-FAAC-150: Picker Assign: menonaktifkan checkbox Without asset class only

16. Hilangkan centang checkbox "Without asset class only"
17. Verifikasi daftar picker menambahkan Asset Name di Asset Class lain dengan badge Current Class berisi "[Class Name]": "Delivery Van" berbadge "Vehicles" dan "Office Chair" berbadge "Office Equipment (New)"
18. Verifikasi Asset Name tanpa Asset Class menampilkan "—" pada Current Class
19. Arahkan kursor ke badge Current Class baris Delivery Van
20. Verifikasi hover badge menampilkan nama lengkap "VEHICLES – Vehicles"
21. Verifikasi Asset Name yang sudah berada di Asset Class ini tetap tidak tampil
22. Centang kembali checkbox "Without asset class only"

### TC-FA-FAAC-169: Search picker Assign tanpa hasil menampilkan EmptyState No results found

23. Ketik Search "zzzz" pada Search "Search asset name...", tekan Enter
24. Verifikasi EmptyState tampil: Illustration, Title "No results found", Description "Try adjusting your search or filter."
25. Klik `(←)` pada kotak Search

### TC-FA-FAAC-155: Klik Assign tanpa memilih Asset Name

26. Klik [Assign] tanpa mencentang baris apa pun
27. Verifikasi submit dicegah: dialog tetap terbuka
28. Verifikasi [Assign] tetap Enabled
29. Verifikasi teks error inline berwarna danger tampil rata kanan tepat di atas tombol footer: "You must pick an item" (bukan toast, bukan Alert)
30. Verifikasi tidak ada toast
31. Klik [Cancel]

### TC-FA-FAAC-168: Picker Assign tanpa kandidat menampilkan EmptyState All asset names have an asset class

32. Assign seluruh Asset Name company yang tanpa Asset Class ke Asset Class lain lewat fixture BE
33. Klik tombol "+ Assign Asset Names"
34. Verifikasi EmptyState tampil: Illustration, Title "All asset names have an asset class", Description "Turn off the filter to move asset names from other asset classes."
35. Klik [Cancel]

## Notes

- Sumber: `fixed-asset/asset-class/TestCases/tc-asset-class.md`. Urutan TC dalam spec: 149, 150, 169, 155, 168 (TC-168 memerlukan semua Asset Name sudah ber-Asset Class sehingga diletakkan terakhir).
- Pengecualian nama literal (S-06, S-12; pengecualian beralasan yang disetujui user): Asset Name seed Pre-setup dipakai apa adanya; blok ini hanya membaca picker dan tidak meng-assign, kecuali langkah 32 oleh fixture BE yang dipulihkan di hook `after`.
- Class Code `ANCHOR-066` ditulis literal tanpa suffix `{runId}-<NNN>` karena Class Code dibatasi 15 karakter sehingga suffix itu tidak muat (S-12, nama literal; pola spec 047 dan 048); hook `before` menghapus sisa run sebelumnya dan hook `after` menghapus kode itu (cleanup tidak berasumsi setup berhasil penuh).
- Langkah penghubung (S-03): langkah 1 (membuka Detail anchor), 22 dan 25 (pemulihan state picker), 31 dan 35 (menutup dialog), 32 (mengubah state seed untuk TC-168).
- Langkah 5 dan 9 menjadi anchor bagi asersi lain pada dialog yang sama (bagian 8b butir 2).
- Temuan untuk QA: TC-168 menyebut "seed Pre-setup" bahwa semua Asset Name company sudah ter-assign, sedangkan TC-149 sampai TC-155 mensyaratkan Asset Name tanpa Asset Class pada company yang sama; spec memakai fixture BE untuk berpindah antar keadaan (disediakan tim FE/BE).
