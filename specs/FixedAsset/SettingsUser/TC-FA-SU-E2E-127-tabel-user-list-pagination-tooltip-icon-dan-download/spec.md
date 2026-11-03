---
id: TC-FA-SU-E2E-127-tabel-user-list-pagination-tooltip-icon-dan-download
title: "Tabel User List: Pagination, Tooltip Icon, dan Download"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-359
  - TC-FA-SU-360
  - TC-FA-SU-364
coverage:
  web: automated
---

# Tabel User List: Pagination, Tooltip Icon, dan Download

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20, plan Enterprise, 25 pengguna). Nama pengguna dan nilai Pre-setup dirujuk lewat `Fixture.fa-settings-user.<kunci>` (berkas `fixtures/fa-settings-user.json` belum ada dan disediakan tim FE).
- Spec ini hanya membaca data Pre-setup dan tidak mengubahnya; suite berjalan serial (`parallel: false`).
- Nomor halaman tidak valid: `0`, `-1`, `999`, `abc` (Expected b TC-FA-SU-359 menyebut 0, negatif, melebihi halaman terakhir, dan bukan angka).
- Tabel `Input Nomor Halaman`:

| Input |
|---|
| 0 |
| -1 |
| 999 |
| abc |

- Tabel `Tooltip Table Tools dan Header Actions`:

| Elemen | Tooltip |
|---|---|
| icon Search | `Search` |
| icon Filter | `Filter` |
| icon Download | `Download` |
| icon Changelog | `Changelog` |
| header kolom Actions (⋯) | `Column Visibility` |

- Kemampuan baca isi berkas unduhan CSV dan XLSX (nama berkas, header kolom, jumlah dan isi baris, encoding, nama sheet) disediakan tim FE.

## Test Steps

### TC-FA-SU-359: Pagination

1. Klik dropdown page size
2. Verifikasi pilihan page size 10, 25, 50, 100 tanpa opsi All
3. Tutup dropdown page size dengan Esc
4. Verifikasi default 10 baris per halaman
5. Pindah ke halaman 2
6. Pindah ke halaman terakhir
7. Untuk setiap baris tabel `Input Nomor Halaman` di Prerequisites (langkah 8 sampai 9):
8. Isi nomor halaman <Input>, tekan Enter
9. Verifikasi tabel tetap di halaman terakhir
10. Isi nomor halaman 2, tekan Enter
11. Verifikasi halaman 2 terbuka
12. Klik header `Name` satu kali
13. Verifikasi tabel tetap di nomor halaman sekarang (halaman 2) setelah sort diganti
14. Klik header `Name` dua kali lagi hingga sort netral
15. Ketik Search `Budi`, tekan Enter
16. Verifikasi tabel kembali ke halaman 1 setelah Search
17. Klik `(←)` pada kotak Search, pindah ke halaman 2
18. Klik ikon Filter, buka dropdown Status, centang `Active`, klik `[Apply]`
19. Verifikasi tabel kembali ke halaman 1 setelah Filter
20. Klik `[Clear Field]` lalu `[Apply]` pada panel Filter, pindah ke halaman 2
21. Ganti page size ke 25
22. Verifikasi tabel kembali ke halaman 1 setelah page size diganti
23. Ganti page size ke 10

### TC-FA-SU-360: Download CSV dan XLSX

24. Hover icon Download
25. Verifikasi tooltip `Download` tampil
26. Klik icon Download
27. Verifikasi overlay `Download as CSV` dan `Download as XLSX` tampil
28. Pilih `Download as CSV`
29. Verifikasi tidak ada toast sukses
30. Verifikasi berkas `User.csv` terunduh
31. Klik icon Download, pilih `Download as XLSX`
32. Verifikasi tidak ada toast sukses
33. Verifikasi berkas `User.xlsx` terunduh
34. Verifikasi berkas CSV berencoding UTF-8 dengan BOM dan nilai ber-koma, tanda kutip, atau baris baru dibungkus tanda kutip ganda
35. Verifikasi berkas XLSX memuat satu sheet bernama `Sheet1`

### TC-FA-SU-364: Tooltip icon Table Tools dan header Actions

36. Untuk setiap baris tabel `Tooltip Table Tools dan Header Actions` di Prerequisites (langkah 37 sampai 38):
37. Hover <Elemen>
38. Verifikasi tooltip <Tooltip> tampil

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, tanpa awalan `Verifikasi`): langkah 3 (menutup dropdown), 14 (mengembalikan sort netral), 17, 20 (membersihkan Search dan Filter lalu pindah ke halaman 2 agar kembali ke halaman 1 dapat diasersi, S-14), dan 23 (memulihkan page size).
- Langkah yang diulang: langkah 8 sampai 9 (empat nomor halaman tidak valid) dan langkah 37 sampai 38 (lima elemen tooltip), parameter pada tabel Prerequisites.
- Asersi terakhir TC-FA-SU-360 (encoding BOM, kutipan ganda, nama sheet) berkaitan dengan isi berkas (kelas f, bagian 3 prinsip 13); TC-FA-SU-360 tetap di spec ini karena Expected-nya satu TC dengan nama berkas dan ketiadaan toast.
- Temuan untuk QA (S-15): (1) TC-FA-SU-359 Expected c menyebut "mengganti sort tetap di nomor halaman sekarang" tetapi langkah 5 TC meminta pindah ke halaman 2 lalu mengganti sort; spec mengikuti Expected. (2) TC-FA-SU-359 langkah 3 hanya menyebut nomor halaman 0, 999, `abc`, sedangkan Expected b menambah nomor negatif; spec memakai keempatnya.
- Alasan di atas sekitar 35 langkah (ekspansi perulangan dihitung): seluruh blok berkelas fungsional yang sama pada halaman, akun, dan dataset Pre-setup #20 yang sama tanpa mengubah data; langkah berulang per kolom atau field berpola identik (langkah 8 sampai 9, langkah 37 sampai 38) dan kegagalan satu iterasi tidak membuat iterasi lain kehilangan makna; bagian 3 konvensi menetapkan Setup Column, Bulk Action Bar, dan Search, Filter, Sort tetap satu spec selama dataset dan harness sama, sedangkan pemecahan hanya menambah login, hook, dan pembukaan halaman. Tiga TC ringan satu surface dan dataset yang sama; pemecahan hanya menambah login, hook, dan pembukaan halaman.
