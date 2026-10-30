---
id: TC-GS-UCF-E2E-015-create-screening-aksesibilitas-dan-info-popover-data-type
title: "Popup Create Custom Field: Screening, Aksesibilitas, Info Popover, dan Perilaku Data Type"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UCF-44
  - TC-GS-UCF-45
  - TC-GS-UCF-404
  - TC-GS-UCF-46
  - TC-GS-UCF-47
  - TC-GS-UCF-48
  - TC-GS-UCF-49
  - TC-GS-UCF-50
  - TC-GS-UCF-51
coverage:
  web: automated
---

# Popup Create Custom Field: Screening, Aksesibilitas, Info Popover, dan Perilaku Data Type

## Prerequisites

- Mode: FE+BE (backend nyata). Spec ini tidak membuat data dan tidak mengirim Create ke server.
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`; environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_<page_key>` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Layar awal: Global Settings > User > tab Custom Field, dibuka di hook `beforeEach`.
- Data Pre-setup: tidak ada yang dibaca. Tidak ada data dinamis dan tidak ada cleanup.
- Kemampuan teknis: pembacaan atribut ARIA (`aria-required`, `aria-describedby`) pada elemen input; penekanan Tab berulang dan Esc; klik di luar popover.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-UCF-44: Screening Popup Create Custom Field pada state awal

1. Klik [+ Custom Field]
2. Verifikasi header popup menampilkan judul `New Custom Field`
3. Verifikasi header popup menampilkan icon close `[✕]`
4. Verifikasi field `Field Name *` kosong dengan placeholder `Enter field name`
5. Verifikasi field `Data Type *` kosong dengan placeholder `Select data type`
6. Verifikasi icon `[ℹ]` tampil di samping label Data Type
7. Verifikasi field `Dropdown Values` tidak tampil
8. Verifikasi field `Decimal Places` tidak tampil
9. Verifikasi field `Placeholder` kosong dengan placeholder `Enter placeholder`
10. Verifikasi helper Placeholder `Optional guide text for user profile input. If empty, default placeholder will be applied.`
11. Verifikasi switch `Required Field` berada pada posisi No
12. Verifikasi tidak ada switch Active
13. Verifikasi footer baris 1: checkbox `Stay on this form after submitting` tidak tercentang
14. Verifikasi footer baris 1: checkbox `Stay on this form after submitting` rata kanan
15. Verifikasi footer baris 2 (rata kanan): `[Clear Field]` (text, primary) dan `[Submit]` (filled, success)
16. Verifikasi tidak ada `[Cancel]` di footer

### TC-GS-UCF-404: Accessibility Popup Create: aria-required dan aria-describedby

17. Verifikasi input `Field Name *` memiliki `aria-required="true"`
18. Verifikasi input `Data Type *` memiliki `aria-required="true"`
19. Klik [Submit] tanpa mengisi apa pun
20. Verifikasi pesan `Field name must not be empty` tampil di bawah Field Name
21. Verifikasi pesan `Data type must not be empty` tampil di bawah Data Type
22. Verifikasi input Field Name memiliki `aria-describedby` yang merujuk elemen pesan `Field name must not be empty`
23. Verifikasi input Data Type memiliki `aria-describedby` yang merujuk elemen pesan `Data type must not be empty`

### TC-GS-UCF-46: Info popover Data Type menampilkan deskripsi enam tipe dan dapat ditutup

24. Klik icon `[ℹ]` di samping label Data Type
25. Verifikasi popover memuat deskripsi Text: `A field that is suitable for short entries, such as brief descriptions or any information filled in free-form, with a maximum limit of 120 characters.`
26. Verifikasi popover memuat deskripsi Text Area: `A larger text field that is ideal for more extensive descriptions, notes, or detailed information, with a maximum limit of 360 characters.`
27. Verifikasi popover memuat deskripsi Dropdown: `Creates a list of predefined options, allowing users to select one option from the list. Useful for fields with a limited set of choices.`
28. Verifikasi popover memuat deskripsi Date: `Allows users to select a specific date from a calendar interface. Suitable for date-related information such as joining date, birth date, and more.`
29. Verifikasi popover memuat deskripsi Numeric: `A field used for storing numerical values, ideal for quantities, measurements, or any numeric data. It supports a leading '-' for negative numbers and a decimal point for precision.`
30. Verifikasi popover memuat deskripsi Phone: `Used specifically for storing phone numbers. Helps maintain consistency and ensures a standardized format for phone entries.`
31. Klik di luar popover
32. Verifikasi popover tertutup
33. Klik icon `[ℹ]` di samping label Data Type lagi
34. Tekan Esc
35. Verifikasi popover tertutup
36. Verifikasi popup Create tetap terbuka

### TC-GS-UCF-47: Dropdown Data Type menampilkan enam opsi berurutan

37. Klik field Data Type
38. Verifikasi daftar opsi berurutan: `Text`, `Text Area`, `Dropdown`, `Date`, `Numeric`, `Phone`
39. Verifikasi tidak ada opsi lain

### TC-GS-UCF-48: Memilih Data Type Dropdown menampilkan input Dropdown Values yang wajib

40. Pilih Data Type `Dropdown`
41. Verifikasi field `Dropdown Values` muncul (wajib)
42. Verifikasi helper `Press enter to add new value or click the badge to edit` tampil di bawah input Dropdown Values
43. Verifikasi field `Decimal Places` tidak tampil
44. Verifikasi input Dropdown Values menampilkan placeholder `Enter value`

### TC-GS-UCF-49: Memilih Data Type Numeric menampilkan pilihan Decimal Places 0, 1, 2

45. Pilih Data Type `Numeric`
46. Buka pilihan Decimal Places
47. Verifikasi field `Decimal Places` muncul dengan pilihan `0`, `1`, `2`
48. Verifikasi nilai awal Decimal Places `0`
49. Verifikasi field `Dropdown Values` tidak tampil

### TC-GS-UCF-50: Data Type Text, Text Area, Date, atau Phone tidak menampilkan field tambahan

50. Pilih Data Type `Text`
51. Verifikasi form hanya berisi Field Name, Data Type, Placeholder, dan Required Field
52. Verifikasi `Dropdown Values` dan `Decimal Places` tidak tampil
53. Ganti Data Type ke `Text Area`
54. Verifikasi form hanya berisi Field Name, Data Type, Placeholder, dan Required Field
55. Verifikasi `Dropdown Values` dan `Decimal Places` tidak tampil
56. Ganti Data Type ke `Date`
57. Verifikasi form hanya berisi Field Name, Data Type, Placeholder, dan Required Field
58. Verifikasi `Dropdown Values` dan `Decimal Places` tidak tampil
59. Ganti Data Type ke `Phone`
60. Verifikasi form hanya berisi Field Name, Data Type, Placeholder, dan Required Field
61. Verifikasi `Dropdown Values` dan `Decimal Places` tidak tampil

### TC-GS-UCF-51: Mengganti Data Type di dalam form sebelum Submit mengosongkan Dropdown Values dan Decimal Places

62. Pilih Data Type `Dropdown`
63. Ketik value `Alpha`, tekan Enter, lalu ketik value `Beta`, tekan Enter
64. Ganti Data Type ke `Text`
65. Ganti kembali Data Type ke `Dropdown`
66. Verifikasi Dropdown Values kosong (`Alpha` dan `Beta` tidak kembali)
67. Ganti Data Type ke `Numeric`, pilih Decimal Places `2`
68. Ganti Data Type ke `Text`
69. Ganti kembali Data Type ke `Numeric`
70. Verifikasi Decimal Places kembali `0`

### Tutup form dirty lalu buka form bersih untuk TC-GS-UCF-45

71. Klik `[✕]`
72. Verifikasi dialog `Unsaved Changes` tampil
73. Klik [Leave]

### TC-GS-UCF-45: Accessibility Popup Create: focus trap dan Esc pada form kosong

74. Klik [+ Custom Field]
75. Tekan Tab berulang melewati elemen terakhir popup
76. Verifikasi fokus keyboard berputar di dalam popup
77. Tekan Esc
78. Verifikasi popup tertutup
79. Verifikasi dialog `Unsaved Changes` tidak muncul

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 44, 404, 46, 47, 48, 49, 50, 51, lalu 45 (urutan sumber 44, 45, 404, 46, ...). Alasan: TC-GS-UCF-45 mengasersi Esc pada form kosong sehingga butuh form bersih, sedangkan TC-GS-UCF-46 sampai 51 mengubah form menjadi dirty; TC-GS-UCF-45 ditaruh di akhir pada pembukaan form baru (prinsip 6). TC-GS-UCF-404 memakai state awal form dan submit kosong yang tidak membuat form dirty, sehingga ditaruh tepat sesudah screening.
- Dua kali [+ Custom Field] dibuka untuk dua kejadian menutup form: ✕ + [Leave] (langkah 71 sampai 73, penghubung) dan Esc pada form kosong (TC-GS-UCF-45).
- Langkah penghubung (aksi tanpa asersi TC): langkah 31 (klik di luar popover; hasilnya diverifikasi di langkah 32), langkah 33 dan 37 (membuka popover dan dropdown), langkah 45 sampai 46 dan 53, 56, 59, 62 sampai 65, 67 sampai 69 (mengganti Data Type sebagai bagian dari langkah TC), serta langkah 71 sampai 73 (menutup form dirty; `Verifikasi` dialog `Unsaved Changes` mengikuti S-08).
- Spec melewati sekitar 35 langkah (smell, bagian 3 prinsip 13 konvensi) karena satu topik (screening dan perilaku field popup Create) dengan satu akun dan satu pembukaan form, dan setiap Expected bermajemuk dipecah satu `Verifikasi` per klausa (S-01), termasuk enam deskripsi popover dan empat tipe tanpa field tambahan. Bagian sesudah satu blok tetap bermakna bila blok sebelumnya gagal karena tiap blok mengasersi elemen berbeda.
- Temuan untuk QA: tidak ada. Judul popup, placeholder, dan teks popover memakai nilai TC (keputusan NC-27 sudah tercermin di PRD).
