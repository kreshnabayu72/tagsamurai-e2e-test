---
id: TC-GS-POS-E2E-005-role-matrix-visibilitas-tab-dan-kontrol
title: Role Matrix: visibilitas tab dan kontrol per capability
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-POS-54
  - TC-GS-POS-55
  - TC-GS-POS-56
  - TC-GS-POS-57
  - TC-GS-POS-58
  - TC-GS-POS-59
coverage:
  web: automated
---

# Role Matrix: visibilitas tab dan kontrol per capability

## Prerequisites

- Spec ini dijalankan untuk setiap role pada tabel "Role yang diuji". Langkahnya identik, hanya akun
  login yang berbeda. Kredensial setiap akun diambil lewat `Spectra.env`, tidak ditulis di spec ini.
- Environment run adalah environment terisolasi khusus otomasi yang disiapkan tim FE, bukan
  environment yang dipakai tester manual bersamaan, karena kapabilitas tiap akun dimutasi di
  environment itu.
- Modul Position murni binary Show/Hidden dan tidak punya elemen berstate Disabled
  (PRD `position.md` §4.8). Karena itu tidak ada satu pun langkah di spec ini yang mengharapkan
  elemen tampil tapi nonaktif. Kalau ada elemen yang muncul dalam keadaan nonaktif, itu temuan bug.
- `Fixture.globalSettingsPosition.positions.population` berisi cukup banyak Position agar setiap
  role punya baris untuk diperiksa pada langkah pemeriksaan row action.
- `Fixture.globalSettingsPosition.captions.rowActions.edit` dan `.delete` adalah label opsi pada
  menu row action.

Role yang diuji:

| Role | Akun | Hak yang dimiliki |
|---|---|---|
| Total Control | `Fixture.globalSettingsPosition.actors.totalControl` | `access_level` Total Control, akses penuh tanpa capability terpisah |
| Read Only | `Fixture.globalSettingsPosition.actors.readOnly` | `access_level` Read Only, tanpa capability Manage user and role |
| Capability Read-Only | `Fixture.globalSettingsPosition.actors.capabilityReadOnly` | Capability Manage user and role dengan hak Read saja |
| Create-Only | `Fixture.globalSettingsPosition.actors.createOnly` | Capability Create saja, Update dan Delete tidak dimiliki |
| Update-Only | `Fixture.globalSettingsPosition.actors.updateOnly` | Capability Update saja, Create dan Delete tidak dimiliki |
| Delete-Only | `Fixture.globalSettingsPosition.actors.deleteOnly` | Capability Delete saja, Create dan Update tidak dimiliki |

## Test Steps

Lakukan seluruh subbagian berikut untuk setiap role pada tabel "Role yang diuji", dengan login ulang
sebagai akun yang sesuai di awal tiap subbagian.

### Total Control: seluruh kontrol tampil dan aktif

1. Login sebagai Role Total Control, lalu buka tab `Position`
2. Verifikasi tab `Position` tampil pada sub-tab bar
3. Verifikasi seluruh baris data Position dapat dibaca
4. Verifikasi tombol `[+ Position]` tampil dan dapat diklik
5. Verifikasi kolom Checkbox seleksi baris tampil di header tabel
6. Verifikasi kolom Checkbox seleksi baris tampil di setiap baris body tabel
7. Verifikasi ikon Elipsis `(⋯)` pada setiap baris data tampil
8. Klik ikon Elipsis `(⋯)` pada salah satu baris
9. Verifikasi opsi `Edit` tampil pada menu row action
10. Verifikasi opsi `Delete` tampil pada menu row action
11. Tutup menu row action
12. Verifikasi header Column Visibility `(⋯)` tampil pada header tabel
13. Verifikasi tombol `Search` tampil
14. Verifikasi tombol `Filter` tampil
15. Verifikasi tombol `Download` tampil
16. Verifikasi tombol `Changelog` tampil
17. Verifikasi kontrol Pagination tampil

### Read Only: hanya baca, seluruh aksi tulis hidden

18. Login sebagai Role Read Only, lalu buka tab `Position`
19. Verifikasi tab `Position` tetap tampil
20. Verifikasi seluruh baris data Position tetap dapat dibaca
21. Verifikasi tombol `[+ Position]` tidak tampil di toolbar
22. Verifikasi tidak ada kolom Checkbox seleksi di header tabel
23. Verifikasi tidak ada kolom Checkbox seleksi di body tabel
24. Verifikasi tidak ada ikon Elipsis `(⋯)` pada setiap baris data
25. Verifikasi header Column Visibility `(⋯)` tetap tampil
26. Verifikasi tombol `Search`, `Filter`, `Download`, dan `Changelog` tetap tampil
27. Verifikasi kontrol Pagination tetap tampil
28. Verifikasi tabel tidak punya Bulk Action Bar yang muncul tanpa dicentang

### Capability Read-Only: sama seperti Read Only

29. Login sebagai Role Capability Read-Only, lalu buka tab `Position`
30. Verifikasi tab `Position` tetap tampil
31. Verifikasi seluruh baris data Position dapat dibaca
32. Verifikasi tombol `[+ Position]` tidak tampil
33. Verifikasi tidak ada kolom Checkbox seleksi di header maupun body tabel
34. Verifikasi tidak ada ikon Elipsis `(⋯)` pada setiap baris data
35. Verifikasi header Column Visibility `(⋯)` tetap tampil
36. Verifikasi tombol `Search`, `Filter`, `Download`, dan `Changelog` tetap tampil
37. Verifikasi kontrol Pagination tetap tampil

### Create-Only: hanya Create yang tampil

38. Login sebagai Role Create-Only, lalu buka tab `Position`
39. Verifikasi tab `Position` tetap tampil
40. Verifikasi seluruh baris data Position dapat dibaca
41. Verifikasi tombol `[+ Position]` tampil dan dapat diklik
42. Verifikasi tidak ada kolom Checkbox seleksi di header tabel
43. Verifikasi tidak ada kolom Checkbox seleksi di body tabel
44. Verifikasi tidak ada Bulk Action Bar
45. Verifikasi tidak ada ikon Elipsis `(⋯)` pada setiap baris data, karena role ini tidak memiliki
    hak Update maupun Delete
46. Verifikasi header Column Visibility `(⋯)` tetap tampil
47. Verifikasi tombol `Search`, `Filter`, `Download`, dan `Changelog` tetap tampil
48. Verifikasi kontrol Pagination tetap tampil

### Update-Only: hanya Edit yang tampil

49. Login sebagai Role Update-Only, lalu buka tab `Position`
50. Verifikasi tab `Position` tetap tampil
51. Verifikasi seluruh baris data Position dapat dibaca
52. Verifikasi tombol `[+ Position]` tidak tampil
53. Verifikasi tidak ada kolom Checkbox seleksi di header maupun body tabel
54. Verifikasi ikon Elipsis `(⋯)` tampil pada setiap baris data
55. Klik ikon Elipsis `(⋯)` pada salah satu baris
56. Verifikasi opsi `Edit` tampil pada menu row action
57. Verifikasi opsi `Delete` tidak tampil pada menu row action
58. Tutup menu row action
59. Verifikasi header Column Visibility `(⋯)` tetap tampil
60. Verifikasi tombol `Search`, `Filter`, `Download`, dan `Changelog` tetap tampil
61. Verifikasi kontrol Pagination tetap tampil

### Delete-Only: hanya Delete dan Bulk Delete yang tampil

62. Login sebagai Role Delete-Only, lalu buka tab `Position`
63. Verifikasi tab `Position` tetap tampil
64. Verifikasi seluruh baris data Position dapat dibaca
65. Verifikasi tombol `[+ Position]` tidak tampil
66. Verifikasi kolom Checkbox seleksi tampil di header tabel
67. Verifikasi kolom Checkbox seleksi tampil di setiap baris body tabel
68. Centang satu baris Position yang tidak direferensikan user
69. Verifikasi Bulk Action Bar muncul
70. Verifikasi tombol `[Delete]` pada Bulk Action Bar tampil dan dapat diklik
71. Verifikasi Bulk Action Bar tidak muncul kembali setelahcheckbox dilepas
72. Verifikasi ikon Elipsis `(⋯)` tampil pada setiap baris data
73. Klik ikon Elipsis `(⋯)` pada salah satu baris
74. Verifikasi opsi `Delete` tampil pada menu row action
75. Verifikasi opsi `Edit` tidak tampil pada menu row action
76. Tutup menu row action
77. Verifikasi header Column Visibility `(⋯)` tetap tampil
78. Verifikasi tombol `Search`, `Filter`, `Download`, dan `Changelog` tetap tampil
79. Verifikasi kontrol Pagination tetap tampil

### Tidak ada kontrol mutasi yang bisa dijangkau tanpa capability

80. Susunlah daftar seluruh kontrol mutasi yang terlihat selama subbagian tiap role pada tabel
81. Verifikasi tidak ada satu pun kontrol mutasi yang terlihat bagi role yang tidak memiliki
    capability-nya, berdasarkan matriks pada §4.8
82. Verifikasi setiap kontrol mutasi yang terlihat hanya bisa menyelesaikan aksi sampai toast sukses
    bagi role yang memiliki capability-nya, dibuktikan terpisah di spec 006 dan spec 007

## Notes

- Spec ini sengaja berhenti pada tingkat "tombolnya tampil". Membuktikan bahwa aksi benar-benar
  berhasil bagi tiap capability ada di spec 006 dan spec 007. Menggabungkannya di sini akan
  menguji dua hal berbeda dalam satu spec: gate visibilitas dan kelengkapan alur mutasi.
- Enam actor dipakai berulang dalam satu spec karena langkahnya identik dan hanya berbeda pada akun
  login. Cara skrip menjalankan banyak role, apakah perulangan di dalam satu `it()` atau beberapa
  kali run, diputuskan di tahap script.
- Bagian akhir spec sengaja berupa pemeriksaan silang, bukan pengulangan. Gunanya memastikan matriks
  §4.8 tidak ada baris yang hanya terisi separuh. Contohnya, tombol Delete tampil bagi role Create-Only
  karena capability-nya keliru dipetakan.
- Tidak ada satu pun langkah yang memeriksa state Disabled. PRD §4.8 menyatakan modul ini binary
  Show/Hidden, dan catatan pada tabel itu secara khusus menolak tooltip permission Disabled. Kalau
  nanti tim FE menambahkan elemen Disabled, spec ini perlu diperluas, bukan ditunda sekarang.
- Role Read Only dan Capability Read-Only menghasilkan matriks UI yang identik. Keduanya tetap
  diuji terpisah karenabeda mereka ada di lapisan server dan scope data, bukan di UI, dan
  menyatukannya menghilangkan pembuktian bahwa dua sumber hak yang berbeda itu memang menghasilkan
  dua role berbeda.
- Pembuktian bahwa actor non-Total-Control dapat melakukan mutasi sungguhan ada di spec 006 dan
  spec 007.
  Tanpa itu, spec ini hanya membuktikan tombolnya terlihat, yang persis kelemahan yang disebut
  TC-GS-POS-57, 58, dan 59.
