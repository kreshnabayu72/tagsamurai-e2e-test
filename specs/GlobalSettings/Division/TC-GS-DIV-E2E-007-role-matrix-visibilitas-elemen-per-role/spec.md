---
id: TC-GS-DIV-E2E-007-role-matrix-visibilitas-elemen-per-role
title: "Role Matrix: Visibilitas Elemen Tab Division per Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-18
  - TC-GS-DIV-19
  - TC-GS-DIV-20
  - TC-GS-DIV-21
  - TC-GS-DIV-22
  - TC-GS-DIV-23
  - TC-GS-DIV-24
coverage:
  web: automated
---

# Role Matrix: Visibilitas Elemen Tab Division per Role

## Prerequisites

- Mode: FE+BE.
- Langkah per role sama strukturnya (buka Global Settings > User, buka Tab Division bila tersedia, periksa Table Tools, row action baris `Compliance`, kolom Checkbox, dan Bulk Action Bar); yang berbeda akun login dan hasil Show/Hidden (tabel Role yang diuji), sehingga sebagian langkah berbeda per role (mis. menu `⋯` dibuka hanya pada role yang punya Edit atau Delete). Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables`.

Role yang diuji (Tabel Data Uji Pre-setup):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-DIV-23 | Total Control | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-DIV-24 | Read Only | Maya Putri | `readOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` |
| TC-GS-DIV-19 | System Role: Read saja | Tono Hartono | `readCapability_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_READ_PASSWORD` |
| TC-GS-DIV-20 | System Role: Create dan Read | Rina Marlina | `createOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_CREATE_PASSWORD` |
| TC-GS-DIV-21 | System Role: Update dan Read | Agus Wijaya | `updateOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_UPDATE_PASSWORD` |
| TC-GS-DIV-22 | System Role: Delete dan Read | Dewi Lestari | `deleteOnly_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_DELETE_PASSWORD` |
| TC-GS-DIV-18 | Tanpa Capability | Fajar Nugroho | `noCapability_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_NOCAP_PASSWORD` |

- Data Pre-setup Division (6 Division, data environment tetap), termasuk baris `Compliance` yang selalu berada di halaman 1 (urutan A-Z) baik dengan maupun tanpa Population D-02. Spec tidak membuat, mengubah, atau menghapus data; aksi Create, Edit, dan Delete tidak dijalankan, hanya visibilitasnya yang diperiksa (menu row action dibuka lalu ditutup, baris dicentang lalu dicentang ulang).
- Login Total Control (role pertama) dilakukan di hook `before`; role berikutnya memakai langkah ganti akun eksplisit (logout lalu login) sebagai langkah pembuka tiap blok role berikutnya (bagian 3a konvensi). Karena spec berakhir di akun Tanpa Capability, hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).
- Guided Tooltip: hook `before` mencatat nilai awal flag `guided_tooltip_seen_gs-division` untuk keenam akun yang dapat membuka Tab Division, lalu menyetelnya ke true supaya walkthrough otomatis tidak menutupi layar; hook `after` memulihkan nilai awal tiap akun. Kemampuan membaca dan menyetel flag disediakan tim FE/BE (nama endpoint tidak disebut di TC dan PRD).
- State global yang diubah: hanya flag Guided Tooltip (dipulihkan seperti di atas). Capability tiap akun adalah data Pre-setup dan tidak diubah di spec ini.

## Test Steps

### TC-GS-DIV-23: Total Control melihat seluruh elemen

1. Buka Global Settings > User
2. Verifikasi Tab `Division` tampil
3. Klik Tab Division
4. Verifikasi Toolbar Search, Filter, Download, dan Changelog tampil
5. Verifikasi Tombol `[+ Division]` tampil
6. Klik `⋯` pada baris `Compliance`
7. Verifikasi row action `Edit` tampil
8. Verifikasi row action `Delete` tampil
9. Tutup row action menu dengan Esc
10. Verifikasi Checkbox baris tabel tampil
11. Centang baris `Compliance`
12. Verifikasi Bulk Action Bar `[Delete]` tampil saat satu baris dicentang
13. Hapus centang baris `Compliance`

### TC-GS-DIV-24: Read Only (Access Level) hanya dapat melihat

14. Logout, lalu login sebagai Read Only
15. Buka Global Settings > User
16. Verifikasi Tab `Division` tampil
17. Klik Tab Division
18. Verifikasi Toolbar Search, Filter, Download, dan Changelog tampil
19. Verifikasi Tombol `[+ Division]` Hidden
20. Verifikasi row action `Edit` dan `Delete` Hidden pada baris `Compliance`
21. Verifikasi Checkbox baris tabel Hidden
22. Verifikasi Bulk Action Bar `[Delete]` Hidden

### TC-GS-DIV-19: Aktor dengan capability Read saja

23. Logout, lalu login sebagai System Role: Read saja
24. Buka Global Settings > User
25. Verifikasi Tab `Division` tampil
26. Klik Tab Division
27. Verifikasi Toolbar Search, Filter, Download, dan Changelog tampil
28. Verifikasi Tombol `[+ Division]` Hidden
29. Verifikasi row action `Edit` dan `Delete` Hidden pada baris `Compliance` (menu baris tidak tampil)
30. Verifikasi Checkbox baris tabel Hidden
31. Verifikasi Bulk Action Bar `[Delete]` Hidden

### TC-GS-DIV-20: Aktor dengan capability Create dan Read

32. Logout, lalu login sebagai System Role: Create dan Read
33. Buka Global Settings > User
34. Verifikasi Tab `Division` tampil
35. Klik Tab Division
36. Verifikasi Toolbar Search, Filter, Download, dan Changelog tampil
37. Verifikasi Tombol `[+ Division]` tampil
38. Verifikasi row action `Edit` dan `Delete` Hidden pada baris `Compliance`
39. Verifikasi Checkbox baris tabel Hidden
40. Verifikasi Bulk Action Bar `[Delete]` Hidden

### TC-GS-DIV-21: Aktor dengan capability Update dan Read

41. Logout, lalu login sebagai System Role: Update dan Read
42. Buka Global Settings > User
43. Verifikasi Tab `Division` tampil
44. Klik Tab Division
45. Verifikasi Toolbar Search, Filter, Download, dan Changelog tampil
46. Verifikasi Tombol `[+ Division]` Hidden
47. Klik `⋯` pada baris `Compliance`
48. Verifikasi row action `Edit` tampil (menu baris hanya memuat Edit)
49. Verifikasi row action `Delete` Hidden
50. Tutup row action menu dengan Esc
51. Verifikasi Checkbox baris tabel Hidden
52. Verifikasi Bulk Action Bar `[Delete]` Hidden

### TC-GS-DIV-22: Aktor dengan capability Delete dan Read

53. Logout, lalu login sebagai System Role: Delete dan Read
54. Buka Global Settings > User
55. Verifikasi Tab `Division` tampil
56. Klik Tab Division
57. Verifikasi Toolbar Search, Filter, Download, dan Changelog tampil
58. Verifikasi Tombol `[+ Division]` Hidden
59. Klik `⋯` pada baris `Compliance`
60. Verifikasi row action `Delete` tampil (menu baris hanya memuat Delete)
61. Verifikasi row action `Edit` Hidden
62. Tutup row action menu dengan Esc
63. Verifikasi Checkbox baris tabel tampil
64. Centang baris `Compliance`
65. Verifikasi Bulk Action Bar `[Delete]` tampil saat satu baris dicentang
66. Hapus centang baris `Compliance`

### TC-GS-DIV-18: Aktor tanpa capability Manage user and role tidak melihat Tab Division

67. Logout, lalu login sebagai Tanpa Capability
68. Buka Global Settings > User
69. Verifikasi Tab `User List` tampil
70. Verifikasi Tab `Division` Hidden
71. Verifikasi Tombol `[+ Division]`, row action `Edit` dan `Delete`, Checkbox baris tabel, Bulk Action Bar `[Delete]`, serta Toolbar Search, Filter, Download, dan Changelog Hidden

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec Role Matrix (bagian 3a konvensi) berupa matriks visibilitas elemen per role yang memuat polaritas tampil dan Hidden dengan struktur alur sama per role; `caseType` Positive mengikuti alur dominan (bagian 8). Spec melewati sekitar 35 langkah (71 langkah) karena tujuh role dijalankan berurutan dalam satu kelas harness (role matrix), bukan karena beberapa kelas harness; tiap blok role berdiri sendiri (login ulang di awal blok) sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah "Buka Global Settings > User" di awal tiap blok role dipertahankan karena merupakan Langkah Uji TC sumber (langkah 1 TC-GS-DIV-18 sampai TC-GS-DIV-24) dan dijalankan sesudah ganti akun.
- Urutan TC sumber diubah: Total Control (TC-GS-DIV-23) dijalankan pertama karena akun hook `before`, TC-GS-DIV-18 (Tanpa Capability) terakhir karena Tab Division tidak tersedia sehingga tidak ada elemen yang dapat dibuka.
- TC-GS-DIV-18 langkah 2 sampai 4 ("Buka Tab Division (bila tampil)", "Centang 1 baris (bila checkbox tampil)") bersyarat; spec menulisnya deterministik: Tab Division Hidden (langkah 70), sehingga tidak ada tab yang diklik dan tidak ada baris yang dicentang; elemen turunan Division diverifikasi Hidden sebagai satu daftar (langkah 71).
- Pada role tanpa Edit dan Delete (TC-GS-DIV-24, TC-GS-DIV-19, TC-GS-DIV-20), menu baris `⋯` tidak tampil (TC-GS-DIV-19 Expected e; PRD §4.8), sehingga spec tidak mengklik `⋯` dan memverifikasi `Edit` dan `Delete` Hidden pada baris `Compliance`. Pada role yang punya salah satunya (TC-GS-DIV-21, TC-GS-DIV-22, Total Control), menu dibuka lalu ditutup dengan Esc. Pada role tanpa Checkbox, Bulk Action Bar diverifikasi Hidden tanpa mencentang baris karena tidak ada checkbox yang dapat dicentang.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): menutup row action menu dengan Esc (langkah 9, 50, 62), menghapus centang baris (langkah 13 dan 66), serta logout lalu login ke role berikutnya (langkah 14, 23, 32, 41, 53, 67).
- Pengecekan Bulk Action Bar (langkah 11 sampai 13 dan 64 sampai 66) menambah satu centang baris karena Expected Result TC menyatakan "`[Delete]` tampil saat >=1 baris dicentang"; tidak ada aksi Delete yang dijalankan.
- Langkah 69 (Tab `User List` tampil) menjadi anchor positif bahwa halaman User sudah dimuat sebelum asersi Hidden pada langkah 70 dan 71.
- Kombinasi role yang tidak punya TC sumber tidak ditambahkan. Akses langsung URL oleh aktor tanpa capability diuji di spec `TC-GS-DIV-E2E-008-role-matrix-negatif-direct-url-tanpa-capability`.
- Temuan untuk QA:
  - TC-GS-DIV-18 sampai TC-GS-DIV-24 tidak menyebut baris yang dipakai untuk memeriksa row action; spec memakai `Compliance` (Pre-setup, halaman 1).
  - TC-GS-DIV-18 langkah 3 dan 4 bersifat bersyarat ("bila tampil"); Expected a sampai f dirumuskan dari sisi Tab Division yang Hidden, sehingga elemen turunan tidak dapat diamati secara individual.
