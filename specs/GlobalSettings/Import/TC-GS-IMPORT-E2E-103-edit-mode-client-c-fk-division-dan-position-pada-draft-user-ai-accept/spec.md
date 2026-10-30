---
id: TC-GS-IMPORT-E2E-103-edit-mode-client-c-fk-division-dan-position-pada-draft-user-ai-accept
title: "Edit Mode Client C: FK Division dan Position pada draft User, AI Accept dan Dismiss pada sel, tombol Create Missing Disabled, Division Use duplicate"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-205
  - TC-GS-IMPORT-659
  - TC-GS-IMPORT-665
  - TC-GS-IMPORT-835
  - TC-GS-IMPORT-899
  - TC-GS-IMPORT-907
coverage:
  web: automated
---

# Edit Mode Client C: FK Division dan Position pada draft User, AI Accept dan Dismiss pada sel, tombol Create Missing Disabled, Division Use duplicate

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global (mode mock AI) dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client C (Rudi Hartanto) `totalControl_automated_qaTeam3@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > User Login untuk Client C.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Layanan AI: mock tetap mode normal (D-40, tabel D-41 dan D-42), default tanpa penggantian mode; disediakan tim FE/BE. Hook `after` memastikan mode kembali normal.
- Data Pre-setup Client C (tidak diubah): Division `Engineering` dan `Gudang`, Position `Senior Developer`; `Logistik` bukan Division; User Login `dewi.anggraini.c@example.com`.
- Data Dinamis: D-30 (Draft User Login Client C 7 baris dari `user-login-fk.csv`, Access `Global Settings` pada semua baris), dibuat ulang lewat skrip fixture sebelum tiap blok: #1 Ahmad Fauzi `pending` (Division `Engineering`, Position `Senior Developer`); #2 Citra Lestari Division `Gudng` (error FK); #3 Budi Setiawan Position `Seniur Developer` (error FK); #4 Dewi Anggraini Email `dewi.anggraini.c@example.com` (`duplicate`); #5 Eko Prasetyo Division `Gudng` dan Position `Seniur Developer`; #6 Last Name `Wibowo`, First Name 121 karakter (error non-FK); #7 Last Name `Hartono`, First Name 121 karakter (nilai sumber First Name pertama tabel D-41), Division `Gudng` (error, dua badge saran AI). Nilai ubahan: Last Name `Nugroho`, Division `Gudx`, `Gud`, `Gudang`, `Logistik`. Nilai saran AI: Division `Did you mean 'Gudang'?`; First Name `AI suggestion: 'Muhammad Abdurrahman Nurrahman'?`.
- Tabel "Tombol Create Missing di Callout" (TC-665): varian 1 baris pesan "Division not found" dengan tombol `[Create Missing Divisions]`; varian 2 baris pesan "Position not found" dengan tombol `[Create Missing Positions]`.
- Tabel "Accept AI lalu Cancel" (TC-835): varian 1 sel Division, badge "Did you mean 'Gudang'?", nilai hasil Accept `Gudang`; varian 2 sel First Name, badge "AI suggestion: 'Muhammad Abdurrahman Nurrahman'?", nilai hasil Accept `Muhammad Abdurrahman Nurrahman`.
- Kemampuan teknis: pengamatan badge saran AI, mock AI, skrip seed D-30 (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain draft Client C dan flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): buang draft User Login Client C, kembalikan mode mock AI ke normal, lepas kunci sesi edit.

## Test Steps

### TC-GS-IMPORT-665: Tombol Create Missing pada Callout Disabled selama Edit Mode

1. Buat ulang draft D-30 Client C lewat skrip fixture, lalu muat ulang halaman
2. Klik `⋯` pada baris #1, pilih `Edit`
Untuk setiap baris tabel "Tombol Create Missing di Callout" (langkah 3 sampai 7 diulang dua kali):
3. Arahkan kursor ke tombol Create Missing pada baris pesan varian di Error Summary Callout
4. Verifikasi tombol Create Missing varian tampil Disabled
5. Verifikasi tooltip pada tombol: "Finish or cancel the current edit first."
6. Klik tombol Create Missing pada baris pesan varian
7. Verifikasi tidak ada dialog maupun toast, dan footer tetap `[Cancel]` dan `[Save]`
8. Klik `[Cancel]`

### TC-GS-IMPORT-659: AI Dismiss pada badge First Name

9. Buat ulang draft D-30 Client C lewat skrip fixture, lalu muat ulang halaman
10. Klik `⋯` pada baris #7, pilih `Edit`
11. Ubah sel Last Name baris #7 menjadi `Nugroho`
12. Klik `[Dismiss]` pada badge `AI suggestion: 'Muhammad Abdurrahman Nurrahman'?` di sel First Name baris #7
13. Verifikasi badge `AI suggestion: 'Muhammad Abdurrahman Nurrahman'?` pada sel First Name hilang
14. Verifikasi sel First Name tetap input berisi 121 karakter semula
15. Verifikasi sel Last Name tetap `Nugroho`
16. Verifikasi sel Division tetap input `Gudng`
17. Verifikasi badge saran `Did you mean 'Gudang'?` pada sel Division tetap tampil
18. Verifikasi footer tetap `[Cancel]` dan `[Save]`
19. Klik `[Cancel]`, lalu klik `[Discard]` pada dialog Discard Changes

### TC-GS-IMPORT-205 dan TC-GS-IMPORT-835 varian 1: AI Accept pada sel Division, lalu Cancel dan Discard

20. Buat ulang draft D-30 Client C lewat skrip fixture, lalu muat ulang halaman
21. Klik `⋯` pada baris #7, pilih `Edit`
22. Ubah sel Last Name baris #7 menjadi `Nugroho`
23. Klik `[Accept]` pada badge `Did you mean 'Gudang'?` di sel Division baris #7
24. Verifikasi sel Division baris #7 menampilkan nilai terpilih `Gudang` pada Select tanpa border `danger`
25. Verifikasi badge saran pada sel Division hilang
26. Verifikasi sel Last Name baris #7 tetap menampilkan input `Nugroho`
27. Verifikasi sel First Name baris #7 tetap berisi 121 karakter semula dengan border `danger` dan pesan "Max. 120 characters"
28. Verifikasi footer tetap `[Cancel]` dan `[Save]`
29. Klik `[Cancel]`
30. Verifikasi dialog dengan Title "Discard Changes" dan Body "Unsaved edits will be lost." tampil dengan tombol `[Keep Editing]` dan `[Discard]`
31. Klik `[Discard]` pada dialog
32. Verifikasi sesi berakhir: footer `[Import (1)]` tampil kembali dan `[Cancel]` serta `[Save]` tidak tampil
33. Verifikasi sel Division baris #7 menampilkan `Gudang` tanpa border `danger`
34. Verifikasi sel Last Name baris #7 menampilkan `Hartono`
35. Verifikasi baris #7 berstatus `error`

### TC-GS-IMPORT-835 varian 2: AI Accept pada sel First Name, lalu Cancel dan Discard

36. Buat ulang draft D-30 Client C lewat skrip fixture, lalu muat ulang halaman
37. Klik `⋯` pada baris #7, pilih `Edit`
38. Ubah sel Last Name baris #7 menjadi `Nugroho`
39. Klik `[Accept]` pada badge `AI suggestion: 'Muhammad Abdurrahman Nurrahman'?` di sel First Name baris #7
40. Verifikasi sel First Name baris #7 menampilkan input berisi `Muhammad Abdurrahman Nurrahman`
41. Verifikasi badge saran pada sel First Name hilang
42. Klik `[Cancel]`
43. Verifikasi dialog dengan Title "Discard Changes" dan Body "Unsaved edits will be lost." tampil dengan tombol `[Keep Editing]` dan `[Discard]`
44. Klik `[Discard]` pada dialog
45. Verifikasi sesi berakhir: footer `[Import (1)]` tampil kembali dan `[Cancel]` serta `[Save]` tidak tampil
46. Verifikasi sel First Name baris #7 menampilkan `Muhammad Abdurrahman Nurrahman` tanpa border `danger`
47. Verifikasi sel Last Name baris #7 menampilkan `Hartono`
48. Verifikasi baris #7 berstatus `error`

### TC-GS-IMPORT-899: Division berupa Select pencarian

49. Buat ulang draft D-30 Client C lewat skrip fixture, lalu muat ulang halaman
50. Klik `⋯` pada baris #2, pilih `Edit`
51. Verifikasi sel Division menampilkan `Gudng` sebagai nilai terpilih berstatus Invalid (ikon dan teks deskriptif) dan tidak dikosongkan
52. Klik sel Division dan ketik `Gudx`
53. Verifikasi daftar pilihan hanya memuat satu pilihan `Use "Gudx"`
54. Hapus teks lalu ketik `Gud`
55. Verifikasi daftar pilihan memuat `Gudang`
56. Pilih `Gudang`
57. Klik `[Save]`
58. Verifikasi muncul toast sukses: "Success, row has been updated."
59. Verifikasi baris #2 berstatus `pending`
60. Verifikasi baris #2 Division `Gudang`

### TC-GS-IMPORT-907: Use Division pada baris duplicate

61. Tunggu toast lama hilang otomatis; buat ulang draft D-30 Client C lewat skrip fixture, lalu muat ulang halaman
62. Klik `⋯` pada baris #4, pilih `Edit`
63. Ketik `Logistik` pada sel Division, lalu pilih `Use "Logistik"`
64. Klik `[Save]`
65. Verifikasi muncul toast sukses: "Success, row has been updated."
66. Verifikasi baris #4 tetap berstatus `duplicate` dengan sorotan peringatan
67. Verifikasi sel Division baris #4 tanpa border `danger`
68. Verifikasi Error Summary Callout tetap memuat "Division not found" dengan badge "3 rows"

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional (mock AI mode normal adalah default, bukan objek uji).
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penggabungan: TC-205 dan TC-835 varian 1 berbagi satu sesi (Accept pada sel Division lalu Cancel dan Discard); Expected TC-205 a-d pada langkah 24 sampai 28, Expected TC-835 a-f pada langkah 24, 25, 30, 32 sampai 35. TC-665 diletakkan pertama (screening) dan TC-899 serta TC-907 terakhir karena menyimpan perubahan (prinsip 2 dan 5 bagian 3).
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 9, 20, 36, 49, 61 membuat ulang D-30 (Kontrak Fixture R2: "dibuat ulang per TC"); langkah 8, 19, 29 menutup sesi (Cancel atau Cancel lalu Discard).
- Spec berisi 68 langkah. Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional) dan satu topik (Edit Mode FK pada Client C), tiap blok membuat ulang draft dan berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-GS-IMPORT-894, 896, 904 sampai 906 ada di spec 104.
- Temuan untuk QA:
  - TC-GS-IMPORT-835 Expected c menyebut footer `[Import (1)]` setelah sesi berakhir; angka 1 sama dengan jumlah baris `pending` D-30 (baris #1) dan bukan jumlah total baris. Diikuti apa adanya.
  - TC-GS-IMPORT-835 Langkah 4 memakai "badge varian" yang dipecah menjadi dua varian; varian 2 menyisakan baris #7 berstatus `error` karena Division `Gudng` belum diperbaiki.
  - Post Condition TC-835 ("Draft Client C kembali ke D-30 kecuali sel varian berisi nilai hasil Accept") adalah pemulihan oleh fixture; tidak diasersi (S-01).
