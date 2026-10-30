---
id: TC-GS-ROLE-E2E-041-auto-revert-saat-edit-crud-dialog-cancel-dan-konfirmasi
title: "Auto-Revert saat Edit CRUD: Dialog, Cancel, dan Konfirmasi"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-104
  - TC-GS-ROLE-105
  - TC-GS-ROLE-106
  - TC-GS-ROLE-107
coverage:
  web: automated
---

# Auto-Revert saat Edit CRUD: Dialog, Cancel, dan Konfirmasi

## Prerequisites

- Mode: FE+BE.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role` mengikuti pernyataan hook suite di `suite.md`.
- Akun aktor hook `before`: Ahmad Fauzi (Total Control, Pre-setup #1), email `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login dilakukan di hook `before`; hook `beforeEach` membuka Global Settings > Role & Permission > Tab System. Spec memakai satu akun; tidak ada ganti akun.
- Data Given (disiapkan di hook `before` lewat seeding API, kemampuan disediakan tim FE/BE; dipakai sebagai precondition TC):
  - Maya Anggraini (Pre-setup #11, Inactive) di-assign Total Control dengan keenam role CRUD penuh (kondisi hasil TC-GS-ROLE-59, Tabel Data Uji Dinamis #2). Target TC-GS-ROLE-104, 105, dan 106.
  - Wawan Setiawan (Pre-setup #11) di-assign Read Only sehingga punya baris `Manage hardware`. Target TC-GS-ROLE-107.
- Data yang diubah spec: Maya Anggraini kehilangan access level Total Control (TC-GS-ROLE-106) dan Wawan Setiawan kehilangan Read Only (TC-GS-ROLE-107); Create baris `Manage hardware` Wawan Setiawan menjadi checked. Hook `after` memulihkan Maya Anggraini dan Wawan Setiawan ke kondisi kandidat Pre-setup #11 (tanpa access level, tanpa baris role) lewat seeding API.
- Kemampuan teknis: memuat ulang halaman; hover pada komponen user di dialog; baseline entry Changelog dibaca dari Modal Changelog.
- State global: tidak ada yang diubah (suite berjalan serial, `suite.md`).

## Test Steps

### TC-GS-ROLE-104: Screening dialog auto-revert saat mengedit role user Total Control

1. Klik Role Name `Manage TAG`
2. Hapus centang Update baris Maya Anggraini
3. Verifikasi title dialog "Remove Access"
4. Verifikasi body dialog memuat komponen user (ikon user generik dan "Maya A")
5. Arahkan kursor ke komponen user "Maya A"
6. Verifikasi tooltip menampilkan nama lengkap "Maya Anggraini"
7. Verifikasi body dialog memuat teks "Editing this permission will remove Total Control access from this user. Are you sure you want to remove it?"
8. Verifikasi tombol `[Cancel]` (contrast) dan `[Remove]` (danger) tampil
9. Verifikasi tidak ada toast
10. Klik `[Cancel]`
11. Muat ulang halaman
12. Verifikasi Update baris Maya Anggraini checked (perubahan belum tersimpan)

### TC-GS-ROLE-105: Cancel dialog auto-revert

13. Klik `Changelog`
14. Catat jumlah entry untuk Maya Anggraini di Modal Changelog `Manage TAG` (K105)
15. Tutup Modal Changelog dengan `✕`
16. Hapus centang Update baris Maya Anggraini
17. Klik `[Cancel]`
18. Verifikasi tidak ada toast
19. Verifikasi checkbox Update baris Maya Anggraini kembali checked
20. Buka Tab Total Control
21. Ketik Search `Maya`, tekan Enter
22. Verifikasi baris Maya Anggraini tampil di Tab Total Control
23. Klik `(←)` pada kotak Search
24. Buka Tab System
25. Klik Role Name `Manage TAG`
26. Klik `Changelog`
27. Verifikasi Modal Changelog `Manage TAG` tampil
28. Verifikasi jumlah entry untuk Maya Anggraini sama dengan K105 (tidak ada entry baru)
29. Tutup Modal Changelog dengan `✕`

### TC-GS-ROLE-106: Konfirmasi auto-revert user Total Control

30. Hapus centang Update baris Maya Anggraini
31. Klik `[Remove]`
32. Verifikasi toast sukses "Success, permissions have been updated. Maya Anggraini is no longer Total Control."
33. Buka Tab Total Control
34. Ketik Search `Maya`, tekan Enter
35. Verifikasi "No results found"
36. Klik `(←)` pada kotak Search
37. Buka Tab System
38. Klik Role Name `Manage TAG`
39. Verifikasi Read baris Maya Anggraini checked
40. Verifikasi Update baris Maya Anggraini unchecked
41. Klik segmen `System` pada breadcrumb untuk membuka Tab System
42. Klik Role Name `Manage user and role`
43. Verifikasi Create, Read, Update, dan Delete baris Maya Anggraini tetap checked
44. Klik segmen `System` pada breadcrumb untuk membuka Tab System
45. Klik Role Name `Import data`
46. Verifikasi Create dan Read baris Maya Anggraini tetap checked

### TC-GS-ROLE-107: Konfirmasi auto-revert user Read Only

47. Klik segmen `System` pada breadcrumb untuk membuka Tab System
48. Klik Role Name `Manage hardware`
49. Centang Create baris Wawan Setiawan
50. Verifikasi body dialog memuat komponen user (ikon user generik dan "Wawan S")
51. Arahkan kursor ke komponen user "Wawan S"
52. Verifikasi tooltip menampilkan nama lengkap "Wawan Setiawan"
53. Verifikasi body dialog memuat teks "Editing this permission will remove Read Only access from this user. Are you sure you want to remove it?"
54. Klik `[Remove]`
55. Verifikasi toast sukses "Success, permissions have been updated. Wawan Setiawan is no longer Read Only."
56. Buka Tab Read Only
57. Ketik Search `Wawan`, tekan Enter
58. Verifikasi "No results found"
59. Klik `(←)` pada kotak Search
60. Buka Tab System
61. Klik Role Name `Manage hardware`
62. Verifikasi Create baris Wawan Setiawan checked

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC sumber.
- Spec melewati sekitar 35 langkah (62 langkah) karena empat TC berada di satu kelas harness (fungsional, Auto-Revert pada Detail dengan akun aktor yang sama) dan memakai dataset yang sama (Maya Anggraini pada TC-GS-ROLE-104, 105, dan 106). Urutan 104, 105, lalu 106 menjaga Maya Anggraini tetap Total Control sampai konfirmasi di TC-GS-ROLE-106; memisahkan ketiganya menggandakan seeding Maya Anggraini. TC-GS-ROLE-107 memakai Wawan Setiawan dan blok awalnya berdiri sendiri (dimulai dari Tab System), sehingga kegagalan blok sebelumnya tidak membuat blok ini kehilangan makna.
- Langkah penghubung (tanpa awalan `Verifikasi`): menutup dialog dengan `[Cancel]` dan memuat ulang halaman (langkah 10 dan 11), mencatat baseline Changelog (langkah 13 sampai 15), menutup Modal Changelog (langkah 29), serta membuka tab dan Detail yang dibutuhkan langkah berikutnya (langkah 20, 24, 25, 33, 37, 38, 41, 42, 44, 45, 47, 48, 56, 60, 61).
- Langkah 10 dan 11 serta langkah 12 diperlukan karena TC-GS-ROLE-104 Expected d ("belum ada perubahan tersimpan") hanya dapat diamati sesudah dialog ditutup; spec membatalkan dialog lalu memuat ulang halaman untuk membuktikan Update tetap checked.
- Absence di Tab Total Control dan Tab Read Only memakai Search yang menghasilkan "No results found" sebagai anchor positif (langkah 35 dan 58). Langkah 22 (baris Maya Anggraini tampil) adalah anchor positif untuk Search yang berhasil menemukan baris.
- Asersi "tidak ada entry baru" di Changelog (langkah 28) memakai baseline jumlah entry yang dicatat sebelum aksi (langkah 14) dan didahului langkah 27 sebagai anchor bahwa modal sudah termuat.
- Langkah 9 dan 18 (tidak ada toast) diletakkan segera sesudah pemicu (butir 11 bagian 8b).
- Temuan untuk QA:
  - TC-GS-ROLE-106 Post Condition (access level Maya Anggraini kosong, role lain tidak direset; log Edit dan Auto-Revert; notifikasi ke Maya Anggraini) tidak punya langkah observasi di TC. Bagian "role lain tidak direset" diamati lewat Expected d; bagian lain tidak diasersi.
  - TC-GS-ROLE-104 Expected d dan TC-GS-ROLE-105 Expected d tidak menyebut cara membaca entry Changelog atau menyaring per user; spec menghitung entry yang menyebut Maya Anggraini.
  - TC-GS-ROLE-105 Expected d tidak menyebut jumlah awal entry; spec memakai baseline sebelum aksi.
  - TC-GS-ROLE-107 precondition c menyebut Wawan Setiawan di-assign Read Only lewat UI; spec menyiapkannya lewat seeding API (S-04).
