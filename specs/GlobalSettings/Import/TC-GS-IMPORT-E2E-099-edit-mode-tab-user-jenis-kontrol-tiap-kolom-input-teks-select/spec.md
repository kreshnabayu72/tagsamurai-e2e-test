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
5. Klik sel Division, Position, dan Shift baris #1 satu per satu sehingga daftar pilihan terbuka
6. Verifikasi sel Division, Position, dan Shift baris #1 berupa Select dengan pencarian (kolom ketik tersedia dan daftar pilihan terbuka saat diklik)
7. Tekan Esc untuk menutup daftar pilihan, lalu kosongkan sel Position dan Shift baris #1
8. Verifikasi sel Position dan Shift dapat dikosongkan
9. Verifikasi sel Access baris #1 berupa MultiSelect yang menampilkan produk terpilih sebagai chip
10. Verifikasi sel Active Period dan Join Date baris #1 berupa DatePicker dengan ikon kalender
11. Kosongkan sel Active Period dan Join Date baris #1
12. Verifikasi sel Active Period dan Join Date dapat dikosongkan
13. Verifikasi sel Emergency Phone baris #1 menampilkan pemilih Country Code diikuti input teks Number
14. Klik `[Cancel]`
15. Verifikasi sesi ditutup tanpa dialog
16. Verifikasi footer `[Import (8)]` tampil kembali

### TC-GS-IMPORT-908: Tab Brand, Measurement, Position, dan Division hanya input teks

Untuk setiap baris tabel "Tab teks saja" (langkah 17 sampai 22 diulang empat kali):

17. Buka Sub-Tab sesuai kolom Sub-Tab
18. Klik `⋯` pada baris #1, pilih `Edit`
19. Verifikasi sel sesuai kolom Sel baris #1 berupa input teks tanpa panah dropdown dan tanpa ikon kalender
20. Klik `[Cancel]`
21. Verifikasi sesi ditutup tanpa dialog
22. Verifikasi footer tampil kembali sesuai kolom Footer sebelum edit

### TC-GS-IMPORT-893: Sel Access berupa MultiSelect

23. Pilih Sub-Tab User Login
24. Klik `⋯` pada baris #1, pilih `Edit`
25. Klik sel Access baris #1
26. Verifikasi daftar pilihan memuat tepat `Global Settings` dan `Fixed Asset` menurut urutan sidebar
27. Verifikasi chip terpilih hanya `Global Settings`
28. Pilih `Fixed Asset`
29. Tekan Esc untuk menutup panel
30. Verifikasi panel tertutup
31. Verifikasi chip terpilih `Global Settings` dan `Fixed Asset`
32. Verifikasi sesi edit tetap aktif
33. Klik `[Save]`
34. Verifikasi muncul toast sukses: "Success, row has been updated."
35. Verifikasi sel Access baris #1 menampilkan `Global Settings;Fixed Asset` (bentuk kanonik urutan sidebar, pemisah `;`)
36. Verifikasi baris #1 berstatus `pending`

### TC-GS-IMPORT-895: Active Period berupa DatePicker minimal besok

37. Pulihkan draft User Login Client A ke D-05 lewat skrip pemulihan, lalu muat ulang halaman
38. Klik `⋯` pada baris #1, pilih `Edit`
39. Klik sel Active Period baris #1
40. Verifikasi tanggal hari ini dan tanggal sebelumnya tampil Disabled pada kalender
41. Coba pilih tanggal hari ini
42. Verifikasi tanggal hari ini tidak dapat dipilih
43. Pilih tanggal besok menurut zona waktu client
44. Verifikasi sel menampilkan tanggal besok dalam format `YYYY-MM-DD`
45. Klik `[Save]`
46. Verifikasi muncul toast sukses: "Success, row has been updated."
47. Verifikasi sel Active Period baris #1 menampilkan tanggal besok dalam format `YYYY-MM-DD`
48. Verifikasi baris #1 berstatus `pending`
49. Klik `⋯` pada baris #1, pilih `Edit`, lalu kosongkan sel Active Period
50. Klik `[Save]`
51. Verifikasi sel Active Period baris #1 tampil `—`
52. Verifikasi baris #1 berstatus `pending`

### TC-GS-IMPORT-897: Custom Field Date berupa DatePicker tanpa batas tanggal

53. Pulihkan draft User Login Client A ke D-05 lewat skrip pemulihan, lalu muat ulang halaman
54. Klik `⋯` pada baris #1, pilih `Edit`
55. Klik sel Join Date baris #1
56. Pilih tanggal kemarin pada kalender
57. Verifikasi tanggal kemarin dapat dipilih (tanpa batas tanggal)
58. Verifikasi sel menampilkan tanggal kemarin dalam format `YYYY-MM-DD`
59. Klik `[Save]`
60. Verifikasi muncul toast sukses: "Success, row has been updated."
61. Verifikasi sel Join Date baris #1 menampilkan tanggal kemarin dalam format `YYYY-MM-DD`
62. Verifikasi baris #1 berstatus `pending`
63. Klik `⋯` pada baris #1, pilih `Edit`, lalu kosongkan sel Join Date
64. Klik `[Save]`
65. Verifikasi sel Join Date baris #1 tampil `—`
66. Verifikasi baris #1 berstatus `pending`

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: fungsional.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan dari TC: TC-891 dan TC-908 (hanya Cancel) mendahului TC-893, 895, dan 897 yang menyimpan perubahan.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 17, 23 (pemilihan Sub-Tab); langkah 5 (membuka daftar pilihan sel Division, Position, Shift), langkah 7 (Esc menutup daftar, lalu mengosongkan sel Position, Shift) dan 11 (mengosongkan sel Active Period, Join Date); langkah 37 dan 53 memulihkan draft ke D-05 (Kontrak Fixture R2); langkah 41 mencoba memilih tanggal hari ini sebagai bagian Langkah 4 TC-895.
- Spec berisi sekitar 84 langkah dengan ekspansi (66 langkah ditambah langkah 17 sampai 22 dikali 3 pengulangan tambahan). Alasan melewati sekitar 35 langkah: semua blok satu kelas (fungsional) dan satu topik (jenis kontrol sel Edit Mode), tiap blok berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: TC-GS-IMPORT-898, 964 sampai 966 (combobox Represented By) ada di spec 101 dan 102; TC-GS-IMPORT-894 dan 896 di spec 104.
- Temuan untuk QA:
  - TC-GS-IMPORT-891 langkah 3 sampai 7 hanya "Perhatikan jenis kontrol" tanpa langkah klik sel Division, Position, Shift (daftar pilihan terbuka) dan tanpa langkah mengosongkan sel Position, Shift, Active Period, Join Date; spec menambahkan langkah 5, 7, dan 11 agar Expected b dan d teruji.
  - Sesudah pengosongan sel (langkah 7 dan 11), sesi edit memuat perubahan sehingga `[Cancel]` (langkah 14) menurut PRD §4.1 butir 3 memunculkan dialog Discard Changes, sedangkan TC-GS-IMPORT-891 Expected menyebut sesi ditutup tanpa dialog (langkah 15); belum diputuskan.
  - TC-GS-IMPORT-891 Expected a-e memuat banyak klausa dalam satu butir; spec memecahnya per kontrol (S-01). Expected b menyebut "sel Position dan Shift dapat dikosongkan" sebagai klausa; diasersi pada langkah 8 sesudah pengosongan pada langkah 7.
  - TC-GS-IMPORT-895 dan 897 menyebut "tanggal besok" dan "kemarin" tanpa menyebut zona waktu pembanding selain "zona waktu client"; batas tengah malam bergantung waktu run (S-12); jam server tidak dimanipulasi.
  - Post Condition semua TC ("Draft Client A dipulihkan ke D-05") adalah pemulihan oleh fixture dan tidak diasersi (S-01).
