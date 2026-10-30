---
id: TC-GS-IMPORT-E2E-099-edit-mode-tab-user-jenis-kontrol-tiap-kolom-input-teks-select
title: "Edit Mode Tab User: jenis kontrol tiap kolom (input teks, Select, MultiSelect Access, DatePicker Active Period dan Join Date) dan Tab Brand, Measurement, Position, Division hanya input teks"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-891
  - TC-GS-IMPORT-893
  - TC-GS-IMPORT-895
  - TC-GS-IMPORT-897
  - TC-GS-IMPORT-908
coverage:
  web: automated
---

# Edit Mode Tab User: jenis kontrol tiap kolom (input teks, Select, MultiSelect Access, DatePicker Active Period dan Join Date) dan Tab Brand, Measurement, Position, Division hanya input teks

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`) karena draft Import dibagikan ke seluruh admin satu client dan state global dipakai bersama spec lain (lihat `suite.md`).
- Akun aktor (login sekali di hook `before`): Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), password `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > Import > Brand untuk Client A.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk akun aktor spec ini, lihat `suite.md`.
- Data Pre-setup Client A (tidak diubah): produk organisasi Global Settings dan Fixed Asset; Custom Field Active Shift (Dropdown), Shift Notes (Text Area), Overtime Hours (Numeric), Join Date (Date, Optional), Emergency Phone (Phone).
- Data Dinamis (nama literal karena asersi bergantung pada isi; pengecualian S-12), dipulihkan oleh skrip pemulihan (Kontrak Fixture R2) sebelum tiap blok: D-05 (Draft User Login 8 baris `pending`; baris #1 Access `Global Settings`), D-01 (Brand 12 baris), D-02 (Measurement 6 baris), D-03 (Position 6 baris), D-04 (Division 6 baris). Nilai tanggal dihitung saat run menurut zona waktu Client A (General Settings): "besok" = hari berikutnya, "kemarin" = hari sebelumnya, format `YYYY-MM-DD`.
- Tabel "Tab teks saja" (TC-908):

  | No | Sub-Tab | Sel baris #1 | Footer sebelum edit |
  |---|---|---|---|
  | 1 | Brand | Brand Name | `[Import (12)]` |
  | 2 | Measurement | Unit Name dan Symbol | `[Import (6)]` |
  | 3 | Position | Position Name | `[Import (6)]` |
  | 4 | Division | Division Name dan Code | `[Import (6)]` |
- Kemampuan teknis: pengamatan jenis kontrol sel (input teks, Select dengan pencarian, MultiSelect, DatePicker), skrip pemulihan draft D-01 sampai D-05 (disediakan tim FE/BE).
- State global: tidak ada yang diubah selain draft Client A dan flag Guided Tooltip (dipulihkan hook suite `after`).
- Cleanup (hook `after`, tidak berasumsi setup berhasil penuh): pulihkan draft Client A ke D-01 sampai D-05.

## Test Steps

### TC-GS-IMPORT-891: Jenis kontrol tiap kolom Tab User Login

1. Pilih Sub-Tab User Login
2. Klik `⋯` pada baris #1, pilih `Edit`
3. Verifikasi sel First Name, Last Name, Email, Employee ID, Shift Notes, dan Overtime Hours baris #1 berupa input teks tanpa panah dropdown
4. Verifikasi sel First Name, Last Name, Email, Employee ID, Shift Notes, dan Overtime Hours baris #1 tanpa ikon kalender
5. Klik sel Division baris #1
6. Verifikasi sel Division baris #1 berupa Select dengan pencarian: kolom ketik tersedia dan daftar pilihan Division terbuka
7. Tekan Esc untuk menutup daftar pilihan
8. Klik sel Position baris #1
9. Verifikasi sel Position baris #1 berupa Select dengan pencarian: kolom ketik tersedia dan daftar pilihan Position terbuka
10. Tekan Esc untuk menutup daftar pilihan
11. Klik sel Shift baris #1
12. Verifikasi sel Shift baris #1 berupa Select dengan pencarian: kolom ketik tersedia dan daftar pilihan Shift terbuka
13. Tekan Esc untuk menutup daftar pilihan, lalu kosongkan sel Position dan Shift baris #1
14. Verifikasi sel Position dan Shift dapat dikosongkan
15. Verifikasi sel Access baris #1 berupa MultiSelect yang menampilkan produk terpilih sebagai chip
16. Verifikasi sel Active Period dan Join Date baris #1 berupa DatePicker dengan ikon kalender
17. Kosongkan sel Active Period dan Join Date baris #1
18. Verifikasi sel Active Period dan Join Date dapat dikosongkan
19. Verifikasi sel Emergency Phone baris #1 menampilkan pemilih Country Code diikuti input teks Number
20. Klik `[Cancel]`
21. Verifikasi dialog Discard Changes tampil
22. Klik `[Discard]` pada dialog Discard Changes
23. Verifikasi sesi ditutup
24. Verifikasi footer `[Import (8)]` tampil kembali

### TC-GS-IMPORT-908: Tab Brand, Measurement, Position, dan Division hanya input teks

Untuk setiap baris tabel "Tab teks saja" (langkah 25 sampai 30 diulang empat kali):

25. Buka Sub-Tab sesuai kolom Sub-Tab
26. Klik `⋯` pada baris #1, pilih `Edit`
27. Verifikasi sel sesuai kolom Sel baris #1 berupa input teks tanpa panah dropdown dan tanpa ikon kalender
28. Klik `[Cancel]`
29. Verifikasi sesi ditutup tanpa dialog
30. Verifikasi footer tampil kembali sesuai kolom Footer sebelum edit

### TC-GS-IMPORT-893: Sel Access berupa MultiSelect

31. Pilih Sub-Tab User Login
32. Klik `⋯` pada baris #1, pilih `Edit`
33. Klik sel Access baris #1
34. Verifikasi daftar pilihan memuat tepat `Global Settings` dan `Fixed Asset` menurut urutan sidebar
35. Verifikasi chip terpilih hanya `Global Settings`
36. Pilih `Fixed Asset`
37. Tekan Esc untuk menutup panel
38. Verifikasi panel tertutup
39. Verifikasi chip terpilih `Global Settings` dan `Fixed Asset`
40. Verifikasi sesi edit tetap aktif
41. Klik `[Save]`
42. Verifikasi muncul toast sukses: "Success, row has been updated."
43. Verifikasi sel Access baris #1 menampilkan `Global Settings;Fixed Asset` (bentuk kanonik urutan sidebar, pemisah `;`)
44. Verifikasi baris #1 berstatus `pending`

### TC-GS-IMPORT-895: Active Period berupa DatePicker minimal besok

45. Pulihkan draft User Login Client A ke D-05 lewat skrip pemulihan, lalu muat ulang halaman
46. Klik `⋯` pada baris #1, pilih `Edit`
47. Klik sel Active Period baris #1
48. Verifikasi tanggal hari ini dan tanggal sebelumnya tampil Disabled pada kalender
49. Coba pilih tanggal hari ini
50. Verifikasi tanggal hari ini tidak dapat dipilih
51. Pilih tanggal besok menurut zona waktu client
52. Verifikasi sel menampilkan tanggal besok dalam format `YYYY-MM-DD`
53. Klik `[Save]`
54. Verifikasi muncul toast sukses: "Success, row has been updated."
55. Verifikasi sel Active Period baris #1 menampilkan tanggal besok dalam format `YYYY-MM-DD`
56. Verifikasi baris #1 berstatus `pending`
57. Klik `⋯` pada baris #1, pilih `Edit`, lalu kosongkan sel Active Period
58. Klik `[Save]`
59. Verifikasi sel Active Period baris #1 tampil `—`
60. Verifikasi baris #1 berstatus `pending`

### TC-GS-IMPORT-897: Custom Field Date berupa DatePicker tanpa batas tanggal

61. Pulihkan draft User Login Client A ke D-05 lewat skrip pemulihan, lalu muat ulang halaman
62. Klik `⋯` pada baris #1, pilih `Edit`
63. Klik sel Join Date baris #1
64. Pilih tanggal kemarin pada kalender
65. Verifikasi tanggal kemarin dapat dipilih (tanpa batas tanggal)
66. Verifikasi sel menampilkan tanggal kemarin dalam format `YYYY-MM-DD`
67. Klik `[Save]`
68. Verifikasi muncul toast sukses: "Success, row has been updated."
69. Verifikasi sel Join Date baris #1 menampilkan tanggal kemarin dalam format `YYYY-MM-DD`
70. Verifikasi baris #1 berstatus `pending`
71. Klik `⋯` pada baris #1, pilih `Edit`, lalu kosongkan sel Join Date
72. Klik `[Save]`
73. Verifikasi sel Join Date baris #1 tampil `—`
74. Verifikasi baris #1 berstatus `pending`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan dari TC: TC-891 dan TC-908 (hanya Cancel) mendahului TC-893, 895, dan 897 yang menyimpan perubahan.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 25, 31 (pemilihan Sub-Tab); langkah 5, 8, dan 11 (membuka daftar pilihan sel Division, Position, Shift), langkah 7 dan 10 (Esc menutup daftar), langkah 13 (Esc menutup daftar, lalu mengosongkan sel Position, Shift), dan 17 (mengosongkan sel Active Period, Join Date); langkah 20 dan 22 (`[Cancel]` lalu `[Discard]`); langkah 45 dan 61 memulihkan draft ke D-05 (Kontrak Fixture R2); langkah 49 mencoba memilih tanggal hari ini sebagai bagian Langkah 4 TC-895.
- Spec berisi sekitar 92 langkah dengan ekspansi (74 langkah ditambah langkah 25 sampai 30 dikali 3 pengulangan tambahan). Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional) dan satu topik (jenis kontrol sel Edit Mode), tiap blok berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-GS-IMPORT-898, 964 sampai 966 (combobox Represented By) ada di spec 101 dan 102; TC-GS-IMPORT-894 dan 896 di spec 104.
- Temuan untuk QA:
  - TC-GS-IMPORT-891 langkah 3 sampai 7 hanya "Perhatikan jenis kontrol" tanpa langkah klik sel Division, Position, Shift (daftar pilihan terbuka) dan tanpa langkah mengosongkan sel Position, Shift, Active Period, Join Date; spec menambahkan langkah 5 sampai 13 dan 17 agar Expected b dan d teruji.
  - Sesudah pengosongan sel (langkah 13 dan 17), sesi edit memuat perubahan sehingga `[Cancel]` (langkah 20) menurut PRD §4.1 butir 3 memunculkan dialog Discard Changes; spec mengikuti PRD (langkah 21 memverifikasi dialog, langkah 22 klik `[Discard]`, langkah 23 memverifikasi sesi ditutup). TC-GS-IMPORT-891 Expected f menulis "sesi ditutup tanpa dialog", bertentangan dengan PRD §4.1 butir 3 setelah sel dikosongkan; TC belum diedit.
  - TC-GS-IMPORT-891 Expected a-e memuat banyak klausa dalam satu butir; spec memecahnya per kontrol (S-01). Expected b menyebut "sel Position dan Shift dapat dikosongkan" sebagai klausa; diasersi pada langkah 14 sesudah pengosongan pada langkah 13.
  - TC-GS-IMPORT-895 dan 897 menyebut "tanggal besok" dan "kemarin" tanpa menyebut zona waktu pembanding selain "zona waktu client"; batas tengah malam bergantung waktu run (S-12); jam server tidak dimanipulasi.
  - Post Condition semua TC ("Draft Client A dipulihkan ke D-05") adalah pemulihan oleh fixture dan tidak diasersi (S-01).
