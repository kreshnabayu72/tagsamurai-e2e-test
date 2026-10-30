---
id: TC-GS-UCF-E2E-026-form-user-phone-country-code-dan-validasi-number
title: "Form User: Field Phone (Country Code Default, Validasi Number 4 sampai 15 Digit, Required, dan Penyimpanan Kode Negara)"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-GS-UCF-180
  - TC-GS-UCF-497
  - TC-GS-UCF-390
  - TC-GS-UCF-181
  - TC-GS-UCF-182
  - TC-GS-UCF-183
  - TC-GS-UCF-184
  - TC-GS-UCF-369
  - TC-GS-UCF-492
  - TC-GS-UCF-493
  - TC-GS-UCF-494
coverage:
  web: automated
---

# Form User: Field Phone (Country Code Default, Validasi Number 4 sampai 15 Digit, Required, dan Penyimpanan Kode Negara)

## Prerequisites

- Mode: FE+BE (backend nyata). Cakupan lintas modul: field Custom Field Phone pada form Create User, form Edit User, dan Detail User (modul User).
- Akun aktor: Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`; environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Flag Guided Tooltip `guided_tooltip_seen_<page_key>` disetel true oleh hook suite `before` untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Layar awal: Global Settings > User > User List sub-tab Login User, dibuka di hook `beforeEach`.
- Data Pre-setup (di-seed lewat API di hook `before`, idempotent, fixture `Fixture.customFieldUser.*`; hanya dibaca): 14 Custom Field aktif Client A (D-01): 6 Pre-setup (`Cost Center` Dropdown `Finance`, `Operations`, `Marketing`, Required Yes; `Employee Grade`; `Job Description`; `Bonus`; `Office Phone` Phone Required Yes; `Joining Date` [Inactive]) dan 8 Population (`Blood Type`, `Shirt Size`, `Emergency Phone` Phone tidak Required, `Birth Date`, `Tax ID` Text Required Yes, `Work Notes`, `Annual Target`, `badge number`).
- Kondisi D-158 (precondition TC): Custom Field Required Yes yang Active di Client A hanya `Cost Center`, `Office Phone`, dan `Tax ID`; dijamin oleh butir hook suite "D-158" di `suite.md` (hook `before` suite menonaktifkan atau menghapus Required Yes Active lainnya lewat API, hook `after` memulihkan); spec ini tidak mengubah status field.
- Field wajib Create User (fixture form, tabel Data Uji Pre-setup TC): First Name `Probe`, Last Name `Custom`, Email `probeCustom<nomor TC>_automated_qaTeam1+{runId}-026@qwertysystem.net` (`{runId}` terdiri atas digit), Division = Division Client A mana pun (fixture modul Division, disediakan tim FE), Access = opsi pertama yang tersedia untuk Client A; field User opsional dikosongkan.
- Data dinamis (user dibuat lewat UI): `User Phone Opt` (D-79, Email `probeCustom184...`, Emergency Phone kosong), user Email `probeCustom369...` (Office Phone `+65 81234567`), `User Phone Plus1` (D-225, Email `probeCustom492...`, `+1 5551234567`), `User Phone Plus971` (D-226, Email `probeCustom493...`, `+971 501234567`). Nilai yang hanya diketik: `123`, `1234`, `812345678901234`, `8123456789012345`, `12ab`, `1`, dan Country Code `🇮🇩 +62`, `🇸🇬 +65`.
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua user Client A dengan Email yang memuat `{runId}-026`.
- Kemampuan teknis: pengubahan Country Code lewat dropdown yang searchable; penekanan Backspace dan Delete pada dropdown Country Code; membuka Detail User (section Custom Fields) dan Edit User dari modul User berdasarkan Email; pembacaan teks nilai Phone di Detail User; menutup popup Create User dirty lewat `[✕]` dan `[Leave]`.
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### Sesi form 1: Country Code dan validasi Number (tanpa membuat user)

1. Klik [+ User] pada tab User List sub-tab Login User

#### TC-GS-UCF-180 (bagian kondisi awal): Country Code terisi default dan tidak dapat dikosongkan, Number mulai kosong

2. Verifikasi Country Code Office Phone menampilkan `🇮🇩 +62` terpilih
3. Verifikasi Number Office Phone kosong dan tidak Disabled
4. Buka dropdown Country Code, tekan Backspace dan Delete
5. Verifikasi nilai Country Code tetap `🇮🇩 +62` setelah Backspace dan Delete
6. Verifikasi tidak ada kontrol hapus pada addon Country Code

#### TC-GS-UCF-497: Number Phone 1 digit menampilkan error `Min. 4 characters` langsung saat diketik

7. Ketik `1` pada Number Office Phone (tanpa mengubah Country Code)
8. Verifikasi Country Code menampilkan `🇮🇩 +62`
9. Verifikasi error inline `Min. 4 characters` langsung muncul setelah digit pertama diketik

#### TC-GS-UCF-390: Number Phone tanpa memilih Country Code: 15 digit diterima, 16 digit ditolak, kurang dari 4 digit ditolak real-time

10. Kosongkan Number, lalu isi Number `812345678901234` (15 digit)
11. Verifikasi Country Code menampilkan `🇮🇩 +62`
12. Verifikasi tidak ada error pada Number (15 digit)
13. Tambahkan digit `5` (16 digit)
14. Verifikasi error inline `Max. 15 characters` langsung muncul
15. Kosongkan Number, lalu ketik `123`
16. Verifikasi error inline `Min. 4 characters` langsung muncul setelah digit ketiga diketik

#### TC-GS-UCF-180 (bagian dropdown searchable): Country Code dapat dicari dan dipilih

17. Kosongkan Number, buka dropdown Country Code, lalu ketik `65` pada pencarian dropdown
18. Verifikasi hasil pencarian `65` memuat `🇸🇬 +65`
19. Pilih `🇸🇬 +65`
20. Verifikasi Country Code menampilkan `🇸🇬 +65`
21. Verifikasi kontrol Country Code menyatu dengan input Number sebagai addon kiri

#### TC-GS-UCF-181: Number Phone 4 sampai 15 digit setelah Country Code diterima dan kurang dari 4 ditolak

22. Pilih Country Code `🇮🇩 +62`
23. Isi Number `123` (3 digit)
24. Verifikasi error inline `Min. 4 characters` langsung muncul setelah digit ketiga diketik
25. Ganti Number dengan `1234`
26. Verifikasi tidak ada error pada Number (4 digit)
27. Ganti Number dengan `812345678901234` (15 digit)
28. Verifikasi tidak ada error pada Number (Country Code tidak dihitung; nilai gabungan `+62812345678901234` valid)

#### TC-GS-UCF-182: Number Phone 16 digit ditolak dan karakter non-angka diblok diam

29. Pilih `🇮🇩 +62`, isi Number `8123456789012345` (16 digit)
30. Verifikasi error inline `Max. 15 characters`
31. Kosongkan Number, ketik `12ab`
32. Verifikasi hanya `12` yang masuk ke Number
33. Verifikasi huruf tidak masuk tanpa pesan
34. Verifikasi error inline `Min. 4 characters` tampil untuk `12` (Number terisi 1 digit atau lebih dan kurang dari 4)
35. Klik `[✕]`
36. Verifikasi dialog `Unsaved Changes` tampil
37. Klik [Leave]

### Sesi form 2: Required dan Phone tidak Required

38. Klik [+ User] pada tab User List sub-tab Login User

#### TC-GS-UCF-183: Phone Required: Number kosong ditolak walau Country Code terisi

39. Isi Field wajib Create User (Email `probeCustom183_automated_qaTeam1+{runId}-026@qwertysystem.net`), Cost Center `Finance`, dan Tax ID `TX-001`; biarkan Office Phone pada kondisi awal (Country Code default, Number kosong)
40. Klik [Submit]
41. Verifikasi error inline `Office phone must not be empty` (kondisi awal)
42. Ganti Country Code Office Phone menjadi `🇸🇬 +65` tanpa mengisi Number
43. Klik [Submit]
44. Verifikasi error inline `Office phone must not be empty` (Country Code diganti tanpa Number)
45. Verifikasi User tidak tersimpan pada kedua langkah: popup Create User tetap terbuka tanpa toast sukses

#### TC-GS-UCF-184: Phone tidak Required: Number kosong valid walau Country Code terisi atau diganti

46. Ganti Email dengan `probeCustom184_automated_qaTeam1+{runId}-026@qwertysystem.net`, lalu ganti Country Code Office Phone menjadi `🇮🇩 +62` dengan Number `81234567890`
47. Ganti Country Code Emergency Phone menjadi `🇸🇬 +65` tanpa mengisi Number
48. Klik [Submit]
49. Verifikasi User tersimpan tanpa error inline pada Emergency Phone
50. Buka Global Settings > User > Detail User dengan Email `probeCustom184_automated_qaTeam1+{runId}-026@qwertysystem.net`, section Custom Fields
51. Verifikasi Emergency Phone tidak memiliki nilai (kode negara saja bukan nilai)

### TC-GS-UCF-369: Mengganti Country Code Phone menyimpan gabungan kode baru dan Number

52. Klik [+ User] pada tab User List sub-tab Login User
53. Isi Field wajib Create User (Email `probeCustom369_automated_qaTeam1+{runId}-026@qwertysystem.net`), Cost Center `Finance`, dan Tax ID `TX-001`
54. Ganti Country Code Office Phone menjadi `🇸🇬 +65` dan isi Number `81234567`
55. Klik [Submit]
56. Verifikasi User tersimpan tanpa error
57. Buka Global Settings > User > Detail User dengan Email `probeCustom369_automated_qaTeam1+{runId}-026@qwertysystem.net`, section Custom Fields
58. Verifikasi Office Phone pada Detail User tampil `+65 81234567` (kode negara dan Number dipisah satu spasi)

### TC-GS-UCF-492: Phone dengan Country Code 1 digit `+1` disimpan dan ditampilkan terpisah dari Number

59. Klik [+ User] pada tab User List sub-tab Login User
60. Isi Field wajib Create User (Email `probeCustom492_automated_qaTeam1+{runId}-026@qwertysystem.net`), Cost Center `Finance`, dan Tax ID `TX-001`
61. Buka dropdown Country Code Office Phone, ketik `1` pada pencarian, pilih opsi dengan kode tepat `+1`
62. Isi Number Office Phone `5551234567`
63. Verifikasi Country Code Office Phone menampilkan `+1`
64. Verifikasi tidak ada error inline pada Office Phone
65. Klik [Submit]
66. Verifikasi User tersimpan tanpa error
67. Buka Global Settings > User > Detail User dengan Email `probeCustom492_automated_qaTeam1+{runId}-026@qwertysystem.net`, section Custom Fields
68. Verifikasi Office Phone pada Detail User tampil `+1 5551234567` (kode 1 digit dan Number dipisah satu spasi)

### TC-GS-UCF-493: Phone dengan Country Code 3 digit `+971` disimpan dan ditampilkan terpisah dari Number

69. Klik [+ User] pada tab User List sub-tab Login User
70. Isi Field wajib Create User (Email `probeCustom493_automated_qaTeam1+{runId}-026@qwertysystem.net`), Cost Center `Finance`, dan Tax ID `TX-001`
71. Buka dropdown Country Code Office Phone, ketik `971` pada pencarian, pilih `🇦🇪 +971`
72. Isi Number Office Phone `501234567`
73. Verifikasi Country Code Office Phone menampilkan `🇦🇪 +971`
74. Verifikasi tidak ada error inline pada Office Phone
75. Klik [Submit]
76. Verifikasi User tersimpan tanpa error
77. Buka Global Settings > User > Detail User dengan Email `probeCustom493_automated_qaTeam1+{runId}-026@qwertysystem.net`, section Custom Fields
78. Verifikasi Office Phone pada Detail User tampil `+971 501234567` (kode 3 digit dan Number dipisah satu spasi)

### TC-GS-UCF-494: Edit User menampilkan Country Code Phone tersimpan pada field yang sudah bernilai

79. Ketik Search `probeCustom493_automated_qaTeam1+{runId}-026@qwertysystem.net` pada User List, tekan Enter
80. Klik `⋯` pada baris user dengan Email tersebut > Edit
81. Verifikasi popup Edit User terbuka pre-filled
82. Verifikasi Country Code Office Phone menampilkan `🇦🇪 +971` (bukan default `🇮🇩 +62`)
83. Verifikasi Number Office Phone menampilkan `501234567`
84. Klik `[✕]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/custom-field-user/TestCases/tc-custom-field-user.md`.
- Subjudul memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: 180 (terbelah), 497, 390, 181, 182 (sesi form 1, tanpa data), 183, 184 (sesi form 2), 369, 492, 493, 494. Urutan sumber (180 sampai 184, 369, 390, 497, 492, 493, 494) berubah demi satu sesi form 1: TC-GS-UCF-497 dan 390 mengasersi Country Code default `🇮🇩 +62` sehingga dijalankan sebelum TC-GS-UCF-180 mengganti Country Code ke `🇸🇬 +65`; karena itu TC-GS-UCF-180 terbelah menjadi bagian kondisi awal (langkah 2 sampai 6) dan bagian dropdown searchable (langkah 17 sampai 21). TC-GS-UCF-183 dan 184 digabung dalam satu sesi form (TC-GS-UCF-184 dimulai dengan mengisi Office Phone dan mengganti Email setelah TC-GS-UCF-183 yang diblokir; langkah 46), memangkas satu pembukaan form. Jumlah pembukaan form: 5 pembukaan form Create User (langkah 1, 38, 52, 59, 69) ditambah satu Edit User (langkah 80); kejadian menutup form: langkah 35 sampai 37 (Leave) dan Submit sukses pada sesi 2 sampai 5; langkah 84 menutup Edit User bersih.
- TC-GS-UCF-494 bergantung pada user TC-GS-UCF-493 (Dependensi di TC); user itu dibuat dalam spec yang sama (langkah 69 sampai 78).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4 (membuka dropdown dan menekan Backspace/Delete sebagai bagian TC), langkah 10, 15, 17, 22, 29, 31 (mengosongkan atau mengisi Number sebagai bagian TC), langkah 35 sampai 37 (menutup form dirty; `Verifikasi` dialog `Unsaved Changes` mengikuti S-08), langkah 50, 57, 67, 77 (membuka Detail User), langkah 79 dan 80 (Search dan membuka Edit), langkah 84 (menutup Edit User bersih tanpa perubahan).
- Spec melewati sekitar 35 langkah (smell, bagian 3 prinsip 13 konvensi): 11 TC satu topik (field Phone pada form User) dengan satu akun dan satu dataset seeding; setiap Expected bermajemuk dipecah satu `Verifikasi` per klausa (S-01). Sesi form 1 tidak membuat data; sesi 2 sampai 5 membuat satu user masing-masing sehingga satu kegagalan tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - TC-GS-UCF-182 Expected b menulis error `Min. 4 characters` untuk `12` sementara NC-05 membahas pesan numerik; spec mengikuti TC.
  - TC-GS-UCF-183 menyebut Office Phone "kondisi awal" tanpa memilih Country Code; Country Code default `🇮🇩 +62` bukan nilai (PRD §4.2).
  - Tidak ada toast Create User yang tertulis di TC modul ini; "User tersimpan" diasersi lewat Detail User yang dapat dibuka dan tidak ada error inline. Pada TC-GS-UCF-184, "User tersimpan tanpa error" (langkah 49) hanya mengasersi tidak adanya error inline pada Emergency Phone sesuai Expected.
  - Cara membuka Detail User berdasarkan Email tidak ditulis di TC; mengikuti alur modul User (disediakan tim FE).
