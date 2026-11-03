---
id: TC-FA-RP-E2E-062-remove-total-control-2
title: "Remove Total Control (2/3)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-217
  - TC-FA-RP-1086
  - TC-FA-RP-1127
  - TC-FA-RP-1129
coverage:
  web: automated
---

# Remove Total Control (2/3)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2, Siti Rahmawati), email `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Hook `after` mengembalikan sesi ke akun default suite (Total Control, `FA_TC_PASSWORD`).
- Data Pre-setup: #1 (Admin Utama Default User), #15 (Ahmad Fauzi di-seed berstatus Total Control dengan Global Role `Manage accounting` CRUD penuh dan seluruh Global Role selaras sesuai TC), #24 (Company Changelog), #36 (Tab Total Control terisi), #3 (Rina Wulandari Total Control kedua; satu-satunya Total Control selain Default User pada TC-FA-RP-217, di-seed lewat seeding API).
- Navigasi lintas modul: Settings > User > Detail User > Tab Role sub-tab Global Role (halaman Global Settings, TC-FA-RP-1086 dan 1127).
- Flag Guided Tooltip, halaman awal, sesi API aktor, dan pemulihan Pre-setup bersama: lihat `suite.md` bagian "Hook suite".
- Data Pre-setup dirujuk lewat fixture `fixtures/fixedAssetRolePermission.json` (belum ada; disediakan tim FE). Email data pengguna berformat `[namalengkaptanpaspasi]@qwertysystem.net`.
- Seeding dan pemulihan: kondisi Precondition tiap TC (tingkat akses, penugasan, group) dibuat lewat seeding API (kemampuan disediakan tim FE/BE, tanpa endpoint karangan) di hook `before` dan sebagai langkah penghubung antar blok TC; Pre-setup dipulihkan ke Tabel Data Uji Pre-setup TC di hook `after` (Catatan TC "Pemulihan fixture destruktif"). Spec tidak membuat data Dinamis. Suite berjalan serial (`parallel: false`).
- Env var yang dipakai: `FA_TC_PASSWORD`. Didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (nama dan arti tercantum di `suite.md` bagian "Env password akun aktor" kecuali dinyatakan lain di atas). Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-FA-RP-217: Remove Total Control tanpa pengecekan jumlah, termasuk saat tidak ada Total Control lain selain Default User

1. Klik `[⋯]` baris Rina Wulandari lalu `Remove`
2. Klik `[Remove]`
3. Verifikasi muncul toast sukses: `Success, Total Control has been removed.`
4. Verifikasi Tab Total Control masih memuat baris Admin Utama (Default User) sehingga tidak pernah kosong
5. Pulihkan Rina Wulandari dan Total Control Pre-setup #36 lewat seeding API

### TC-FA-RP-1086: Remove Total Control mereset total Global Role: switch ON setelahnya hanya memulihkan baseline Read, bukan nilai C/U/D sebelum Total Control

6. Tetapkan Ahmad Fauzi sebagai Total Control dengan Global Role `Manage accounting` CRUD penuh lewat seeding API
7. Klik Tab `Read Only` lalu klik Tab `Total Control`
8. Klik `[⋯]` baris Ahmad Fauzi lalu `Remove`, klik `[Remove]`
9. Tunggu aksi selesai: dialog tertutup
10. Buka Settings > User > Detail Ahmad Fauzi > Tab Role sub-tab Global Role
11. Verifikasi switch `Manage accounting` OFF
12. Verifikasi checkbox Create, Read, Update, dan Delete `Manage accounting` tidak tercentang (kondisi tanpa role)
13. Nyalakan switch `Manage accounting`
14. Verifikasi switch `Manage accounting` menyala
15. Verifikasi tidak ada dialog tambahan
16. Buka Fixed Asset > Settings > Role & Permission > System lalu Detail Role `Manage accounting`
17. Verifikasi baris Ahmad Fauzi tampil dengan Read aktif dan terkunci
18. Verifikasi Create, Update, dan Delete tidak aktif (nilai CRUD penuh sebelum pencabutan tidak dipulihkan)

### TC-FA-RP-1127: Confirm Remove Total Control mereset total Global Role: user tidak tampil di Detail Role mana pun dan kolom Users Tab System berkurang satu

19. Tetapkan ulang Ahmad Fauzi sebagai Total Control dengan seluruh Global Role selaras (CRUD penuh sesuai kolom berlaku) lewat seeding API
20. Buka Tab System lalu catat kolom Users baris `Manage Open API` dan `Manage accounting` sebagai baseline
21. Buka Tab Total Control, klik `[⋯]` baris Ahmad Fauzi lalu `Remove`, klik `[Remove]`
22. Verifikasi toast sukses `Success, Total Control has been removed.`
23. Buka Tab System dan amati kolom Users baris yang sama
24. Verifikasi kolom Users baris `Manage Open API` dan `Manage accounting` masing-masing berkurang 1 dari baseline
25. Buka Detail Role `Manage Open API` lalu ketik Search `Ahmad Fauzi`, tekan Enter
26. Verifikasi baris Ahmad Fauzi tidak tampil di Detail Role `Manage Open API` (empty state hasil Search)
27. Klik `(←)` pada kotak Search
28. Buka Detail Role `Manage accounting` lalu ketik Search `Ahmad Fauzi`, tekan Enter
29. Verifikasi baris Ahmad Fauzi tidak tampil di Detail Role `Manage accounting` (empty state hasil Search)
30. Buka Settings > User > Detail Ahmad Fauzi > Tab Role sub-tab Global Role
31. Verifikasi seluruh switch Global Role OFF
32. Verifikasi seluruh checkbox Create, Read, Update, dan Delete tidak tercentang

### TC-FA-RP-1129: Setelah Remove Total Control, user kembali eligible di popup Assign User ke Role dan penugasan baru dimulai dari baseline Read

33. Tetapkan ulang Ahmad Fauzi sebagai Total Control dengan seluruh Global Role selaras lewat seeding API
34. Buka Fixed Asset > Settings > Role & Permission > System lalu Detail Role `Manage Open API`
35. Klik `[+ Assign]`
36. Ketik Search `Ahmad Fauzi`, tekan Enter
37. Verifikasi Ahmad Fauzi tidak ada di daftar (Total Control dikecualikan; empty state hasil Search)
38. Tutup popup lewat `✕`
39. Buka Tab Total Control, klik `[⋯]` baris Ahmad Fauzi lalu `Remove`, klik `[Remove]`
40. Buka Detail Role `Manage Open API` lalu klik `[+ Assign]`
41. Ketik Search `Ahmad Fauzi`, tekan Enter
42. Verifikasi Ahmad Fauzi ada di daftar (tidak ada penugasan tersisa, termasuk inactive-retained)
43. Centang Ahmad Fauzi lalu klik `[Assign]`
44. Verifikasi baris Ahmad Fauzi tampil di Detail Role `Manage Open API` dengan Read aktif dan terkunci
45. Verifikasi Create, Update, dan Delete tidak aktif

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec ini memuat 45 langkah.
- Langkah penghubung (S-03): langkah 7, 9, 27, 38. Akun aktor pertama sudah login di hook `before` (S-07).
- Langkah seeding atau pemulihan lewat seeding API (S-04, S-09): langkah 5–6, 19, 33; tidak ada `Verifikasi`.
- Langkah Search pada TC-FA-RP-1127 mengikuti TC ("cari Ahmad Fauzi"); absence memakai empty state hasil Search sebagai anchor positif (butir 8b.2).
- Asersi `Verifikasi` kolom Users memakai baseline yang dicatat pada langkah pertama TC-FA-RP-1127 (S-12); nilai absolut tidak diasersi.
- Temuan untuk QA:
  - TC-FA-RP-217 precondition d menyebut "satu-satunya Total Control selain Default User adalah Rina Wulandari", sedangkan aktor (Siti Rahmawati) sendiri Total Control dan Pre-setup #36 memuat Total Control lain. Spec mengikuti TC: Total Control selain Default User dan aktor hanya Rina Wulandari (seeding API).
  - TC-FA-RP-1129 Expected c menyebut "Create, Update, dan Delete tidak aktif" pada `Manage Open API`, sedangkan TC-FA-RP-242 menyatakan kolom yang tidak berlaku (Create dan Delete) berupa `—`, bukan checkbox. Spec mengikuti teks TC.
  - TC-FA-RP-1086 dan 1127 membuka Settings > User > Detail User (Global Settings); TC tidak menyebut jalur navigasi selain breadcrumb.
  - TC-FA-RP-1127 baseline Users `Manage Open API` dan `Manage accounting` dicatat sebagai langkah TC; spec mengasersi selisih 1 terhadap baseline.
- Ukuran spec (45 langkah, di atas smell sekitar 35 langkah): semua blok berkelas fungsional, memakai permukaan dan dataset Pre-setup yang sama, dan tiap blok TC menyiapkan state sendiri lewat seeding sehingga kegagalan satu blok tidak menghilangkan makna blok lain; langkah membengkak karena tiap klausa Expected menjadi satu `Verifikasi` (S-01). Tidak dipecah lagi (konvensi bagian 3, batas ukuran).
