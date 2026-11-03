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
- Spec tidak mengubah data backend; tidak ada seeding atau cleanup selain pemulihan konfigurasi tampilan yang tidak disimpan.

## Test Steps

### TC-FA-SU-415: Guard kolom non-searchable Sub-tab Borrowed Assets: Due Return Date

1. Buka Detail Budi Santoso > Tab Responsibilities > Sub-tab Borrowed Assets
2. Ketik Search `10/09/26` (nilai kolom Due Return Date), tekan Enter
3. Verifikasi empty state `No results found` tampil
4. Verifikasi keyword `10/09/26` tidak mencocokkan baris melalui Search (penyaringan kolom ini hanya lewat Filter Panel)
5. Klik `(←)` pada kotak Search

### TC-FA-SU-416: Search Sub-tab Borrowed Assets terikat visibilitas kolom Name: hide lalu unhide

6. Ketik Search `Kamera`, tekan Enter
7. Verifikasi sebelum hide: keyword `Kamera` menyisakan `Kamera DSLR`
8. Klik header kolom Column Visibility (⋯)
9. Hapus centang Name pada overlay Column Visibility
10. Tutup overlay Column Visibility dengan Esc
11. Ganti isi kotak search dengan `Kamera`, tekan Enter
12. Verifikasi setelah kolom Name di-hide: keyword yang sama menyisakan tidak ada baris (kolom tersembunyi tidak dicari; kolom lain yang tampil tetap dicari), dengan empty state `No results found` tampil sebagai anchor
13. Klik header kolom Column Visibility (⋯)
14. Centang kembali Name pada overlay Column Visibility
15. Tutup overlay Column Visibility dengan Esc
16. Ganti isi kotak search dengan `Kamera`, tekan Enter
17. Verifikasi setelah kolom Name di-unhide: hasil kembali `Kamera DSLR`
18. Klik `(←)` pada kotak Search

### TC-FA-SU-414: Siklus interaksi Search Sub-tab Borrowed Assets: reveal, Enter, clear, collapse

19. Klik icon Search
20. Verifikasi input Search melebar
21. Verifikasi kursor fokus pada input Search
22. Verifikasi placeholder `Search name, asset ID, or transaction ID...`
23. Hover icon Search
24. Verifikasi tooltip `Search`
25. Ketik 1 karakter dari `Kamera`
26. Verifikasi icon ✕ tampil di kanan input
27. Verifikasi tabel belum tersaring
28. Ketik sisa `Kamera`, tekan Enter
29. Verifikasi tabel tersaring menjadi `Kamera DSLR`
30. Klik ✕
31. Verifikasi input Search kosong
32. Verifikasi search bar tetap terbuka
33. Verifikasi kursor fokus pada input Search
34. Verifikasi tabel tetap menampilkan hasil search terakhir
35. Tekan Enter pada input kosong
36. Verifikasi tabel kembali ke semua baris
37. Ketik `Kamera`, tekan Enter, lalu klik `(←)`
38. Verifikasi search bar menutup
39. Verifikasi keyword dikosongkan
40. Verifikasi tabel langsung kembali ke semua baris
41. Klik icon Search, ketik `  Kamera  ` (spasi awal dan akhir), tekan Enter
42. Verifikasi hasil sama dengan `Kamera` tanpa spasi
43. Verifikasi isi input tidak berubah
44. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular; urutan blok mengikuti prinsip bagian 3 (screening dan baca di awal, perubahan konfigurasi tersimpan di akhir).
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): menutup overlay Column Visibility, dropdown, dan panel Filter; menutup kotak Search lewat `(←)` atau `✕` + Enter; `[Clear Field]` dan `[Apply]` pemulih, serta mengembalikan sort ke netral dan visibilitas kolom ke semula, supaya blok berikutnya tidak mewarisi state.
- Asersi tambahan (S-03): TC-FA-SU-416 butir b tidak menyebut empty state; `Verifikasi` empty state `No results found` ditambahkan pada langkah yang sama sebagai anchor absence baris (bagian 8b butir 2).
- Alasan melewati sekitar 35 langkah (44 langkah tertulis, 44 dengan ekspansi langkah berulang): seluruh blok berkelas fungsional (kontrol tabel pada satu sub-tab, satu dataset Pre-setup yang hanya dibaca), tiap blok berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna, dan Detail pengguna dibuka sekali.
- Temuan untuk QA (S-15): tidak ada temuan pada TC sumber spec ini.
