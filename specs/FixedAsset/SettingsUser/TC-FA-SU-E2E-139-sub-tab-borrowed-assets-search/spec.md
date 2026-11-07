---
id: TC-FA-SU-E2E-139-sub-tab-borrowed-assets-search
title: "Sub-tab Borrowed Assets: Search"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-414
  - TC-FA-SU-415
  - TC-FA-SU-416
coverage:
  web: automated
---

# Sub-tab Borrowed Assets: Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor, dan pemulihan Pre-setup bersama lewat seed API; tidak ditulis ulang di sini.
- Data Pre-setup: Client `FaUserMain` (#20) dan Responsibilities (#24). Pengguna target: Budi Santoso dengan 5 baris Borrowed Assets: `Laptop - 1`, `Laptop - 2` (Transaction ID `BRW-20260610`, PIC `Ahmad D`), `Kamera DSLR` (Brand `Canon`), `Proyektor Portable` (Asset ID `AST-01011`), dan `Kendaraan Operasional` (Model / Type `Vario 125`); nilai kolom lain tiap baris mengikuti Pre-setup #24. Kelima baris tampil pada satu halaman. Tiap kolom yang di-search, sort, atau filter memiliki sedikitnya dua nilai distinct (S-11). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Nilai Due Return Date `10/09/26` ada pada sedikitnya satu baris Borrowed Assets Pre-setup #24 (dasar TC-FA-SU-415) dan diverifikasi tampil sebelum Search (8b.15 butir b).
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan.

## Test Steps

### TC-FA-SU-415: Guard kolom non-searchable Sub-tab Borrowed Assets: Due Return Date

1. Ketik Search `Budi Santoso`, tekan Enter
2. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
3. Verifikasi nilai Due Return Date `10/09/26` tampil pada salah satu baris tabel Sub-tab Borrowed Assets sebelum Search
4. Ketik Search `10/09/26` (nilai kolom Due Return Date), tekan Enter
5. Verifikasi empty state `No results found` tampil
6. Verifikasi keyword `10/09/26` tidak mencocokkan baris melalui Search (penyaringan kolom ini hanya lewat Filter Panel)
7. Klik `(←)` pada kotak Search

### TC-FA-SU-416: Search Sub-tab Borrowed Assets terikat visibilitas kolom Name: hide lalu unhide

8. Ketik Search `Kamera`, tekan Enter
9. Verifikasi sebelum hide: keyword `Kamera` menyisakan `Kamera DSLR`
10. Klik header kolom Column Visibility (⋯)
11. Hapus centang Name pada overlay Column Visibility
12. Tutup overlay Column Visibility dengan Esc
13. Ganti isi kotak search dengan `Kamera`, tekan Enter
14. Verifikasi empty state `No results found` tampil
15. Verifikasi setelah kolom Name di-hide: keyword yang sama menyisakan tidak ada baris (kolom tersembunyi tidak dicari; kolom lain yang tampil tetap dicari)
16. Klik header kolom Column Visibility (⋯)
17. Centang kembali Name pada overlay Column Visibility
18. Tutup overlay Column Visibility dengan Esc
19. Ganti isi kotak search dengan `Kamera`, tekan Enter
20. Verifikasi setelah kolom Name di-unhide: hasil kembali `Kamera DSLR`
21. Klik `(←)` pada kotak Search

### TC-FA-SU-414: Siklus interaksi Search Sub-tab Borrowed Assets: reveal, Enter, clear, collapse

22. Klik icon Search
23. Verifikasi input Search melebar
24. Verifikasi kursor fokus pada input Search
25. Verifikasi placeholder `Search name, asset ID, or transaction ID...`
26. Hover icon Search
27. Verifikasi tooltip `Search`
28. Ketik 1 karakter dari `Kamera`
29. Verifikasi icon ✕ tampil di kanan input
30. Verifikasi tabel belum tersaring
31. Ketik sisa `Kamera`, tekan Enter
32. Verifikasi tabel tersaring menjadi `Kamera DSLR`
33. Klik ✕
34. Verifikasi input Search kosong
35. Verifikasi search bar tetap terbuka
36. Verifikasi kursor fokus pada input Search
37. Verifikasi tabel tetap menampilkan hasil search terakhir
38. Tekan Enter pada input kosong
39. Verifikasi tabel kembali ke semua baris
40. Ketik `Kamera`, tekan Enter, lalu klik `(←)`
41. Verifikasi search bar menutup
42. Verifikasi keyword dikosongkan
43. Verifikasi tabel langsung kembali ke semua baris
44. Klik icon Search, ketik `  Kamera  ` (spasi awal dan akhir), tekan Enter
45. Verifikasi hasil sama dengan `Kamera` tanpa spasi
46. Verifikasi isi input tidak berubah
47. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Langkah penghubung (S-03, R-16): sebelum Detail pengguna dibuka, kotak Search User List diisi nama persis `Budi Santoso` (nama Pre-setup) karena User List memuat 25 pengguna pada 3 halaman dan posisi baris tidak diandalkan (R-23, 8b.13); langkah itu hanya menyaring baris target dan tidak diverifikasi.
- Asersi tambahan (S-03): TC-FA-SU-416 butir b tidak menyebut empty state; `Verifikasi` empty state `No results found` ditambahkan sebagai langkah tersendiri (langkah 14) tepat sebelum asersi absence baris (langkah 15) sebagai anchor (bagian 8b butir 2).
- Asersi tambahan (S-03): langkah 3 (`Verifikasi` nilai Due Return Date `10/09/26` tampil pada salah satu baris) bukan dari Expected TC-FA-SU-415; langkah itu menjadi anchor positif sebelum Search nilai kolom non-searchable Date pada langkah 4 (bagian 8b butir 15 b).
- Alasan melewati sekitar 35 langkah (47 langkah tertulis, 47 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15): tidak ada temuan pada TC sumber spec ini.
