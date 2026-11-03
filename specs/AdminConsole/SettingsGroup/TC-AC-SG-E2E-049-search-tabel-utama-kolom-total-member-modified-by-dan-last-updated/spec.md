---
id: TC-AC-SG-E2E-049-search-tabel-utama-kolom-total-member-modified-by-dan-last-updated
title: "Search Tabel Utama: Kolom Total Member, Modified By, dan Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-177
  - TC-AC-SG-178
  - TC-AC-SG-179
coverage:
  web: automated
---

# Search Tabel Utama: Kolom Total Member, Modified By, dan Last Updated

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1, nama tampil `Budi Santoso`) `totalControlGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): `Pohon Uji Utama` entitas Principal (Pre-setup #16, #17, #19, #20), node `All Groups` terpilih, 14 group, page size bawaan 10 baris, urutan bawaan Group A-Z. Nilai yang dipakai: `Branch 2` Total Member 3; `Warehouse Jakarta` Total User 3; `Branch 3` dan `Room 301` bernama mengandung `3`; `Branch 1` dan `Branch 2` Modified By `Admin B`; `Region A` memiliki nilai Last Updated.
- Kelima kolom data (Group, Total User, Total Member, Modified By, Last Updated) tampil secara default; preferensi kolom di browser bersih.
- Kemampuan teknis: Fixture BE untuk baseline `Pohon Uji Utama`, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini hanya membaca data dan tidak mengubah state global.

## Test Steps

### TC-AC-SG-177: Search tabel utama by kolom Total Member: substring, case-insensitive, dan tanpa hasil

1. Ketik Search `3`, tekan Enter
2. Verifikasi tabel menampilkan `Branch 2` (Total Member 3), `Warehouse Jakarta` (Total User 3), `Branch 3` dan `Room 301` (nama Group)
3. Ganti isi kotak search dengan versi huruf kapital dari `3` (yaitu `3`), tekan Enter
4. Verifikasi hasil identik dengan langkah 2: `Branch 2`, `Warehouse Jakarta`, `Branch 3`, dan `Room 301`
5. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
6. Verifikasi empty state dengan Title `No results found` dan Description `Try adjusting your search or filter.`

### TC-AC-SG-178: Search tabel utama by kolom Modified By: substring, case-insensitive, dan tanpa hasil

7. Ganti isi kotak search dengan `admin b`, tekan Enter
8. Verifikasi tabel menampilkan baris dengan Modified By `Admin B` (`Branch 1` dan `Branch 2`)
9. Ganti isi kotak search dengan `ADMIN B`, tekan Enter
10. Verifikasi hasil identik dengan langkah 8: `Branch 1` dan `Branch 2`
11. Ganti isi kotak search dengan `zzzxxx`, tekan Enter
12. Verifikasi empty state dengan Title `No results found` dan Description `Try adjusting your search or filter.`

### TC-AC-SG-179: Search tidak mencocokkan kolom Last Updated (tanggal eksklusif ke Filter)

13. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
14. Salin teks Last Updated baris `Region A` yang tampil
15. Ketik Search dengan menempel teks yang disalin pada langkah 14, tekan Enter
16. Verifikasi empty state `No results found` (tidak ada baris yang cocok)
17. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 13 (mereset tabel dari hasil kosong supaya baris `Region A` tampil, R-16/S-14) dan langkah 17 (menutup Search, S-09). Antar blok TC kotak search tidak ditutup: isinya diganti, sehingga tiap blok tidak bergantung pada blok sebelumnya.
- Langkah "Pastikan kolom Total Member tampil" dan "Pastikan kolom Modified By tampil" (TC-177, TC-178) dipenuhi oleh Prerequisites (semua kolom tampil secara default) dan tidak ditulis sebagai langkah terpisah.
- Temuan untuk QA:
  - TC-AC-SG-177: kata kunci `3` tidak memiliki varian huruf kapital sehingga Expected b tidak bermakna; langkah 3 menulis kata kunci yang sama.
  - TC-AC-SG-179: Expected hanya menyebut empty state `No results found`; kalimat "penyaringan tanggal hanya lewat Filter Panel" bersifat penjelasan dan tidak diasersi.
