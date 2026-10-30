---
id: TC-GS-IMPORT-E2E-168-isi-dan-styling-berkas-template-custom-field-active-di-akhir-katalog
title: "Isi dan styling berkas template: Custom Field Active di akhir, katalog saat diunduh, styling Sheet 1 dan Sheet 2, Custom Field Required"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-IMPORT-447
  - TC-GS-IMPORT-448
  - TC-GS-IMPORT-449
  - TC-GS-IMPORT-450
  - TC-GS-IMPORT-451
  - TC-GS-IMPORT-452
  - TC-GS-IMPORT-762
coverage:
  web: automated
---

# Isi dan styling berkas template: Custom Field Active di akhir, katalog saat diunduh, styling Sheet 1 dan Sheet 2, Custom Field Required

## Prerequisites

- Mode: FE+BE (backend nyata).
- Suite serial (`parallel: false`): spec menambah dan menghapus Custom Field Client A (state global yang dibaca lintas spec); lihat `suite.md`.
- Akun (login aktor pertama di hook `before`; ganti akun eksplisit di tengah spec, hook `after` mengembalikan sesi ke akun default suite):
  - Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (Pre-setup), `Spectra.env.GS_TC_PASSWORD`: aktor pertama.
  - Total Control Client G (Putri Ananda) `totalControl_automated_qaTeam10@qwertysystem.net` (Pre-setup), `Spectra.env.GS_CLIENTG_TC_PASSWORD`: ganti akun eksplisit pada TC-762.
  - Pelaku kedua (pemicu): Admin kedua Client A (Nadia Pratama) `totalControlSecond_automated_qaTeam1@qwertysystem.net` (Pre-setup), `Spectra.env.GS_TC2_PASSWORD`, memakai sesi API untuk menambah dan menghapus Custom Field `Locker Number` pada TC-449; tidak ada sesi UI kedua karena hasil di sesi itu tidak diasersi (P-2).
  - Password tidak ditulis di spec atau fixture. Layar awal Global Settings > Import dibuka hook `beforeEach`.
- Guided Tooltip: hook suite `before` men-set flag `guided_tooltip_seen_gs-import` true untuk kedua akun UI spec ini dan hook `after` memulihkannya, lihat `suite.md`.
- Kemampuan teknis (disediakan tim FE/BE):
  - Pembaca berkas XLSX pada buffer unduhan (nama berkas, nama sheet, isi sel) dan pembaca gaya sel (fill, bold, tinggi baris, lebar kolom, freeze pane, format sel, wrap, rata vertikal, proteksi sheet, password proteksi, status terkunci sel, izin memilih sel terkunci, warna tab, autofilter, data validation) serta penghitung rasio kontras warna teks terhadap fill.
  - Sesi API Admin kedua Client A untuk menambah dan menghapus Custom Field (mekanisme lewat fixture).
- Data Pre-setup Client A (hanya dibaca kecuali Custom Field `Locker Number` milik spec ini): Custom Field Active `Emergency Phone` (Phone), `Join Date` (Date), `Overtime Hours` (Numeric 2 desimal), `Shift` (Dropdown: Pagi, Siang, Malam), `Shift Notes` (Text Area), seluruhnya Optional; `Old Badge` nonaktif. Client G: satu-satunya Custom Field Active `Badge Code` (Text, Required).
- Data Dinamis (milik spec ini): Custom Field `Locker Number` (Text, Optional) ditambahkan pada TC-449 dan dihapus kembali di langkah 74 dan hook `after`. Nama literal tanpa suffix per run karena asersi urutan A-Z antar-Custom Field (pengecualian S-12 butir (ii)); hook `before` membersihkan sisa `Locker Number` dari run sebelumnya lewat API.
- Satu unduhan dipakai bersama untuk beberapa TC bila TC sumber mengunduh berkas yang sama pada Sub-Tab yang sama (TC-447 dan TC-451 pada User Login).
- Pemulihan (hook `after`, tidak berasumsi seeding berhasil penuh): hapus Custom Field `Locker Number` Client A bila masih ada dan kembalikan sesi ke akun default suite.

## Test Steps

### TC-GS-IMPORT-447 dan TC-GS-IMPORT-451: Tab User Login (Custom Field di akhir dan styling Sheet 1)

1. Pilih Sub-Tab User Login
2. Klik `[Download Template]` di Tab User Login
3. Buka berkas XLSX yang terunduh pada pembaca buffer
4. Baca header Sheet 1
5. Verifikasi header memuat kolom Emergency Phone, Join Date, Overtime Hours, Shift, dan Shift Notes setelah kolom "Active Period"
6. Verifikasi header tidak memuat kolom Old Badge
7. Buka Sheet 2 `Field Limit` dan baca baris Custom Field Active di akhir tabel
8. Verifikasi Sheet 2 memuat lima baris tambahan setelah baris "Active Period" untuk kelima Custom Field Active
9. Verifikasi Sheet 2 tidak memuat baris Old Badge
10. Verifikasi baris "Shift": Data Type "Dropdown", Description "Custom field.", Constraint "Optional. Must match one of the configured options (case-insensitive): Pagi; Siang; Malam.", Example "Pagi"
11. Verifikasi baris "Shift Notes": Data Type "Text Area", Description "Custom field.", Constraint "Optional. Max 360 characters.", Example "Handles inbound shipments and stock counts."
12. Verifikasi baris "Overtime Hours": Data Type "Numeric", Description "Custom field.", Constraint "Optional. Valid number, max 15 digits, at most 2 decimal places. A leading - is allowed.", Example "1250.50"
13. Verifikasi baris "Emergency Phone": Data Type "Phone", Description "Custom field.", Constraint "Optional. Format +[Country Code][Number]; one space between the country code and the number is tolerated and ignored when parsing. Country code must be a supported code; number 4–15 digits after the country code.", Example "+62812345678901234"
14. Verifikasi baris "Join Date": Data Type "Date", Description "Custom field.", Constraint "Optional. Must be a valid date.", Example tanggal pada bulan berikutnya dari hari uji dalam format YYYY-MM-DD
15. Buka Sheet 1 dan periksa gaya Sheet 1
16. Periksa properti format sel Employee ID, Active Period, dan Emergency Phone pada baris 5
17. Verifikasi freeze pane hanya baris 1
18. Verifikasi lebar kolom auto-fit minimum 12 dan maksimum 40 karakter
19. Verifikasi kolom First Name, Last Name, Email, Division, Position, Employee ID, Access, Active Period, Emergency Phone, Join Date, Overtime Hours, Shift, dan Shift Notes berformat Text
20. Verifikasi sel Employee ID, Active Period, dan Emergency Phone pada baris 5 berformat Text
21. Verifikasi teks panjang tidak di-wrap
22. Verifikasi baris 2 sampai 4 berteks muted
23. Verifikasi baris 5 ke bawah kosong tanpa styling
24. Verifikasi Sheet 1 tanpa proteksi sheet, autofilter, maupun data validation
25. Verifikasi Sheet 1 aktif dan terpilih saat dibuka dengan warna tab default

### TC-GS-IMPORT-448: Tab User Non Login (Custom Field di akhir, tanpa kolom Access)

26. Pilih Sub-Tab User Non Login
27. Klik `[Download Template]` di Tab User Non Login
28. Buka berkas XLSX yang terunduh pada pembaca buffer
29. Baca header Sheet 1
30. Verifikasi header Sheet 1: First Name; Last Name; Email; Division; Position; Employee ID; Represented By; Active Period, diikuti kolom Emergency Phone, Join Date, Overtime Hours, Shift, dan Shift Notes
31. Verifikasi header tidak memuat kolom Access
32. Buka Sheet 2 `Field Limit`
33. Verifikasi baris "Represented By": Data Type "Email", Description "The Login User who represents this user.", Constraint "Required. Must be the email of an active User Login account.", Example "ahmad.fauzi@example.com"
34. Verifikasi Sheet 2 memuat lima baris Custom Field Active (Emergency Phone, Join Date, Overtime Hours, Shift, Shift Notes) setelah baris `Active Period`
35. Verifikasi masing-masing dari kelima baris Custom Field Active memiliki Description "Custom field."
36. Verifikasi Constraint masing-masing dari kelima baris Custom Field Active diawali "Optional."
37. Verifikasi Sheet 2 tidak memuat baris "Access"

### TC-GS-IMPORT-450: Styling header Sheet 1 Tab Division

38. Pilih Sub-Tab Division
39. Klik `[Download Template]` di Tab Division
40. Buka berkas XLSX yang terunduh pada pembaca buffer
41. Periksa gaya header Sheet 1 (baris 1)
42. Verifikasi baris 1 bold
43. Verifikasi baris 1 bertinggi tetap
44. Verifikasi header `Division Name` (Required) berfill warna utama platform dengan teks terang
45. Verifikasi header `Code` (Optional) berfill netral muda dengan teks gelap
46. Verifikasi fill header `Division Name` dan header `Code` berbeda
47. Verifikasi rasio kontras teks terhadap fill >= 4.5:1 pada kedua header
48. Verifikasi teks header `Division Name` dan `Code` persis nama Target Attribute
49. Verifikasi header tidak diberi tanda `*`

### TC-GS-IMPORT-452: Styling Sheet 2 Field Limit Tab Measurement

50. Pilih Sub-Tab Measurement
51. Klik `[Download Template]` di Tab Measurement
52. Buka berkas XLSX yang terunduh pada pembaca buffer
53. Periksa gaya Sheet 2 `Field Limit`
54. Periksa properti proteksi Sheet 2: status proteksi sheet, password, status terkunci sel Constraint baris 2, dan izin memilih sel terkunci
55. Verifikasi baris 1 Sheet 2 bold dengan fill warna utama platform dan teks terang
56. Verifikasi freeze pane baris 1 dan kolom A
57. Verifikasi lebar kolom: Column 24, Data Type 14, Description 40, Constraint 60, Example 30
58. Verifikasi wrap text pada Description, Constraint, dan Example
59. Verifikasi rata atas vertikal
60. Verifikasi tinggi baris menyesuaikan isi yang di-wrap
61. Verifikasi format sel Text
62. Verifikasi proteksi Sheet 2 aktif tanpa password
63. Verifikasi sel Constraint baris 2 berstatus terkunci
64. Verifikasi proteksi Sheet 2 mengizinkan memilih sel terkunci (isi sel dapat disalin)
65. Verifikasi warna tab Sheet 2 netral dan berbeda dari Sheet 1

### TC-GS-IMPORT-449: Template mengikuti katalog Custom Field saat diunduh

66. Buka Global Settings > Import dan pilih Sub-Tab User Login (halaman dimuat sebelum Custom Field ditambahkan)
67. Tambahkan Custom Field `Locker Number` (tipe Text, Optional) di Client A atas nama Admin kedua Client A lewat sesi API hingga tersimpan
68. Klik `[Download Template]` di Tab User Login tanpa memuat ulang halaman Import
69. Buka berkas XLSX yang terunduh pada pembaca buffer
70. Baca header Sheet 1 dan baris Sheet 2
71. Verifikasi header Sheet 1 memuat kolom `Locker Number` di antara kolom `Join Date` dan `Overtime Hours` (urutan Field Name A-Z)
72. Buka Sheet 2 `Field Limit`
73. Verifikasi baris "Locker Number": Data Type "Text", Description "Custom field.", Constraint "Optional. Max 120 characters.", Example "Warehouse crew"
74. Hapus Custom Field `Locker Number` Client A lewat sesi API (pemulihan Kontrak Fixture R2)

### TC-GS-IMPORT-762: Header Custom Field Required berfill Required (Client G)

75. Ganti akun: logout, lalu login sebagai Total Control Client G (Putri Ananda)
76. Buka Global Settings > Import, pilih Sub-Tab User Login
77. Klik `[Download Template]` di Tab User Login
78. Buka berkas XLSX yang terunduh pada pembaca buffer
79. Bandingkan fill header `Badge Code`, `First Name`, dan `Position` pada Sheet 1
80. Verifikasi header `Badge Code` memiliki fill yang sama dengan header kolom Required `First Name` (warna utama platform, teks terang)
81. Verifikasi fill header `Badge Code` berbeda dari fill header kolom Optional `Position` (netral muda, teks gelap)
82. Buka Sheet 2 `Field Limit` dan baca baris `Badge Code`
83. Verifikasi baris "Badge Code": Data Type "Text", Description "Custom field.", Constraint "Required. Max 120 characters.", Example "Warehouse crew"

## Notes

- Mode: FE+BE. Sumber: `global-settings/import/TestCases/tc-import.md`. Kelas harness: binary buffer (f); objek uji adalah isi dan gaya berkas XLSX hasil unduhan. Admin kedua hanya memicu perubahan katalog Custom Field lewat sesi API (P-2).
- Alasan melewati sekitar 35 langkah (83 langkah nominal): enam blok homogen (satu unduhan per blok, kecuali TC-447 dan TC-451 yang berbagi satu unduhan), semua satu kelas binary buffer dan berdiri sendiri tanpa data bersama; sebagian besar langkah adalah `Verifikasi` per properti gaya atau per baris Field Limit (satu per klausa). Blok yang mengubah katalog Custom Field (TC-449) diletakkan sebelum ganti akun ke Client G dan dipulihkan pada langkah 74; bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal.
- Subjudul `###` memetakan langkah ke id TC granular. Pembagian unduhan: TC-GS-IMPORT-447 (Sheet 2 baris Custom Field) dan TC-GS-IMPORT-451 (gaya Sheet 1) memakai satu unduhan Tab User Login karena TC sumber mengunduh berkas yang sama.
- Langkah penghubung (tanpa `Verifikasi`): pemilihan Sub-Tab, klik `[Download Template]`, pembukaan berkas pada pembaca buffer, pembukaan Sheet 1 dan Sheet 2, pembacaan header dan properti gaya (langkah 4, 7, 15, 16, 29, 41, 53, 54, 70, 79, 82), penambahan dan penghapusan Custom Field `Locker Number` (langkah 67 dan 74), dan ganti akun (langkah 75). Asersi absence kolom atau baris (langkah 6, 9, 31, 37) didahului Verifikasi kolom atau baris lain pada sheet yang sama sebagai pembanding.
- Temuan untuk QA:
  - TC-GS-IMPORT-449 langkah 1 dan 2 dilakukan oleh Admin kedua Client A (sesi UI kedua di Langkah TC); spec memakai sesi API (P-2) karena hasil di sesi itu tidak diasersi. Menunggu konfirmasi QA.
  - TC-GS-IMPORT-450, 451, 452 mengasersi gaya (warna utama platform, fill netral muda, teks muted, rasio kontras) tanpa nilai warna konkret di Expected; nilai warna acuan diambil dari desain/PRD §4.1 Styling XLSX Template oleh tim FE.
  - TC-GS-IMPORT-451 Expected h menyebut "warna tab default" dan TC-GS-IMPORT-452 Expected g "warna tab netral" tanpa nilai; asersi mengikuti kata TC.
  - TC-GS-IMPORT-447 dan 762 menyebut Example Join Date atau Badge Code tanpa nilai spesifik (Join Date: tanggal bulan berikutnya); spec menghitung dari tanggal hari uji.
  - Post Condition TC-GS-IMPORT-449 ("Custom Field `Locker Number` dihapus kembali") dikerjakan langkah 74 dan hook `after`; Post Condition TC lain "-".
