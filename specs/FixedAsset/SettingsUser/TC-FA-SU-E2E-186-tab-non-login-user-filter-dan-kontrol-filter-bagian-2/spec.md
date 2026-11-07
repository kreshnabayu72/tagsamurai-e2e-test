---
id: TC-FA-SU-E2E-186-tab-non-login-user-filter-dan-kontrol-filter-bagian-2
title: "Tab Non-Login User: Filter dan Kontrol Filter (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-555
  - TC-FA-SU-556
coverage:
  web: automated
---

# Tab Non-Login User: Filter dan Kontrol Filter (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` (#20) dan Non-Login User (#26): pengguna target Budi Santoso dengan 5 Non-Login User (`Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`; `Printer Lantai 5` Inactive). Asersi Search, Sort, dan Filter memakai sedikitnya dua nilai distinct pada kolom yang diuji (S-11); kolom tanpa nilai distinct dicatat di Temuan untuk QA.
- Data Dinamis: tidak ada.
- Nama pengguna dan nilai Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Spec tidak mengubah data backend; perubahan tampilan (Search, Filter, Sort, Column Visibility) dipulihkan oleh langkah penghubung spec.
- Urutan default (Name ascending): `Gudang Cabang Bekasi`, `Kendaraan Operasional B 1234 XY`, `Mesin Fotokopi Lt.3`, `Printer Lantai 5`, `Ruang Meeting Anggrek`.

## Test Steps

1. Ketik Search `Budi Santoso`, tekan Enter, lalu buka Detail Budi Santoso > Tab Non-Login User

### TC-FA-SU-555: Kombinasi Search dan Filter dua arah

2. Ketik Search `Printer`, tekan Enter
3. Verifikasi keyword `Printer` menyisakan `Printer Lantai 5`
4. Klik icon Filter
5. Buka dropdown Division lalu centang `Facility`
6. Klik `[Apply]`
7. Verifikasi irisan Search `Printer` dan Filter Division `Facility` menyisakan tidak ada baris (0 baris)
8. Verifikasi keyword Search `Printer` tidak dikosongkan oleh Apply Filter
9. Klik `[Clear Field]` pada field Division
10. Klik `[Apply]`
11. Klik `←` pada kotak Search
12. Buka dropdown Division lalu centang `Facility`
13. Klik `[Apply]`
14. Verifikasi Filter Division `Facility` menyisakan `Ruang Meeting Anggrek`
15. Ketik Search `Printer`, tekan Enter
16. Verifikasi Filter Division `Facility` lalu Search `Printer` menghasilkan tidak ada baris, identik dengan urutan sebaliknya
17. Verifikasi chip Filter Division `Facility` tidak di-reset oleh Search
18. Verifikasi tabel berada di halaman 1

### TC-FA-SU-556: Pelepasan kontrol Clear Field, Clear Search, ganti kolom sort, dan recovery empty state

19. Klik `[Clear Field]` pada field Division
20. Klik `[Apply]`
21. Klik `←` pada kotak Search
22. Ketik Search `Printer`, tekan Enter
23. Buka dropdown Division lalu centang `Facility`
24. Klik `[Apply]`
25. Klik header Name satu kali
26. Klik `[Clear Field]` pada field Division
27. Klik `[Apply]`
28. Verifikasi Search `Printer` tetap berlaku setelah Clear Field (hasil `Printer Lantai 5`)
29. Verifikasi Sort Name ascending (↑) tetap berlaku setelah Clear Field
30. Buka dropdown Division lalu centang `Facility`
31. Klik `[Apply]`
32. Klik `←` pada kotak Search
33. Verifikasi Filter Division `Facility` tetap berlaku setelah Search dikosongkan (hasil `Ruang Meeting Anggrek`)
34. Verifikasi Sort Name ascending (↑) tetap berlaku setelah Search dikosongkan
35. Ketik Search `Printer`, tekan Enter
36. Klik header Email satu kali
37. Verifikasi sort berpindah ke kolom Email (indikator pada Email, bukan Name)
38. Verifikasi Search `Printer` dan Filter Division `Facility` tidak di-reset oleh pergantian kolom sort
39. Verifikasi kombinasi Search `Printer` dan Filter Division `Facility` menampilkan empty state `No results found` dengan deskripsi `Try adjusting your search or filter.`
40. Klik `←` pada kotak Search
41. Verifikasi baris yang cocok langsung pulih: `Ruang Meeting Anggrek`

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`): Search nama `Budi Santoso` (Enter) lalu membuka Detail Budi Santoso, karena User List memuat lebih dari satu halaman (R-16, 8b butir 13); `[Clear Field]`, `[Apply]`, dan `←` pada Search di awal TC-FA-SU-556 mengosongkan kontrol sisa TC-FA-SU-555 (S-09).
- Langkah `Verifikasi keyword Printer menyisakan Printer Lantai 5` dan `Verifikasi Filter Division Facility menyisakan Ruang Meeting Anggrek` ditambahkan sebagai anchor positif absence 0 baris (8b butir 2, S-03).
- TC-FA-SU-557 ada di spec 193.
- Jumlah langkah: 41 tertulis, 41 dengan ekspansi iterasi.
- Spec melewati sekitar 35 langkah bila ekspansi dihitung (41 langkah). Seluruh blok berada pada satu surface (satu tab, satu dataset), satu kelas fungsional, tanpa mengubah data backend, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-FA-SU-555 dan TC-FA-SU-556: kombinasi Search `Printer` dan Filter Division `Facility` menghasilkan 0 baris, sehingga asersi "Search dan Sort tetap berlaku" tidak dapat dibedakan dari urutan baris; spec mengasersi indikator sort dan kontrol yang tidak di-reset. Langkah Verifikasi `Printer Lantai 5` sebelum Filter ditambahkan sebagai anchor positif atas absence 0 baris (8b butir 2).
  - TC-FA-SU-556 langkah 6 menyebut "keyword yang tidak ada hasilnya" tanpa nilai; spec memakai kombinasi Search `Printer` dengan Filter Division `Facility` yang menghasilkan 0 baris.
