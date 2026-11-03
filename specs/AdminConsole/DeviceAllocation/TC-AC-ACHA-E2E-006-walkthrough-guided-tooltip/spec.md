---
id: TC-AC-ACHA-E2E-006-walkthrough-guided-tooltip
title: "Walkthrough Guided Tooltip Halaman Device Allocation"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHA-37
  - TC-AC-ACHA-38
  - TC-AC-ACHA-39
  - TC-AC-ACHA-40
  - TC-AC-ACHA-41
  - TC-AC-ACHA-42
  - TC-AC-ACHA-43
coverage:
  web: automated
---

# Walkthrough Guided Tooltip Halaman Device Allocation

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal PT ABC (Pre-setup #21) `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD` (TC-37 sampai TC-41). Akun kedua: Read Only Distributor PT Global Distribusi (Pre-setup #34, alias RO_DIST) `readOnlyDistributor_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_RO_DIST_PASSWORD` (TC-42). Akun ketiga: Total Control Distributor PT Global Distribusi (Pre-setup #27) `totalControlDistributor_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_DA_TC_DIST_PASSWORD` (TC-43, akun kedua yang belum pernah membuka halaman ini; TC tidak menyebut akunnya).
- Login akun aktor pertama di hook `before` spec ini; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal PT ABC, `AC_TC_PASSWORD`). Ganti akun di tengah spec memakai langkah logout dan login eksplisit.
- Hook suite (dinyatakan sekali di `suite.md`): sesi API aktor, fixture API Pre-setup #20 (disediakan tim FE/BE; endpoint tidak dikarang di spec ini), dan pemulihan preferensi kolom Setup Column. Pengecualian atas hook suite untuk flag Guided Tooltip (bagian 4): spec ini menguji flag itu sendiri sehingga flag `guided_tooltip_seen_ac-device-allocation` tidak bergantung pada hook suite `before`; spec mengatur flag per TC (belum diset atau sudah diset) lewat kemampuan fixture mengatur dan membaca flag per akun (disediakan tim FE/BE; endpoint tidak dikarang di spec ini). Hook suite `after` memulihkan flag semua akun aktor menjadi true. Suite berjalan serial (`parallel: false`).
- Data Pre-setup (hanya dibaca): Seed 30 alokasi (Pre-setup #48); `page_key` walkthrough `ac-device-allocation`. Walkthrough dibuka dengan memuat ulang halaman (F5) setelah flag diatur.
- General Settings Pre-setup #1 tidak diubah. State global: flag Guided Tooltip diubah dan dipulihkan hook `after`; suite berjalan serial.
- Tabel Step walkthrough aktor dengan tombol `[+ Allocation]` (TC-37; langkah 6 sampai 9 mengulang Step 1 sampai Step 4):

| Step | Spotlight | Title | Description |
|---|---|---|---|
| 1 | Stock Balance Summary Panel | `Allocated quota` | `Monitor the total allocated device quota per Category.` |
| 2 | tombol `[+ Allocation]` | `Allocate Device` | `Click this button to create a new device allocation for a client.` |
| 3 | kolom Allocation ID | `Allocation ID` | `Click an allocation ID anytime to view its allocation log and approval history.` |
| 4 | kolom Status | `Allocation Status` | `Track the processing status of each allocation here.` |
| 5 | kolom Actions | `Allocation Actions` | `Use the action menu to manage a specific allocation.` |

- Tabel Step walkthrough aktor tanpa tombol `[+ Allocation]` (TC-42; langkah 67 sampai 69 mengulang Step 1 sampai Step 3 dari 4):

| Step | Spotlight | Title |
|---|---|---|
| 1 of 4 | Stock Balance Summary Panel | `Allocated quota` |
| 2 of 4 | kolom Allocation ID | `Allocation ID` |
| 3 of 4 | kolom Status | `Allocation Status` |
| 4 of 4 | kolom Actions | `Allocation Actions` |

- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`. Env var `AC_DA_RO_DIST_PASSWORD` dan `AC_DA_TC_DIST_PASSWORD` belum terdaftar: didaftarkan tim FE di `spectra.config.ts` dan `.env.example` pada tahap script. Password tidak ditulis di spec atau fixture.

## Test Steps

### TC-AC-ACHA-37: Walkthrough first-visit lima step

1. Atur flag `guided_tooltip_seen_ac-device-allocation` akun Principal menjadi belum diset lewat fixture
2. Muat ulang halaman Allocation > Device Allocation (F5) sebagai kunjungan pertama
3. Verifikasi walkthrough tampil otomatis pada `Step 1 of 5`
4. Verifikasi `[Back]` Hidden pada Step 1
5. Untuk setiap baris tabel "Step walkthrough aktor dengan tombol [+ Allocation]" Step 1 sampai Step 4 lakukan langkah 6 sampai 9
6. Verifikasi spotlight pada elemen kolom "Spotlight" dengan indikator `Step N of 5`
7. Verifikasi Title step sesuai kolom "Title"
8. Verifikasi Description step sesuai kolom "Description"
9. Klik `[Next]`
10. Verifikasi `Step 5 of 5` dengan spotlight pada kolom Actions
11. Verifikasi Title Step 5 `Allocation Actions`
12. Verifikasi Description Step 5 `Use the action menu to manage a specific allocation.`
13. Verifikasi `[Next]` berubah menjadi `[Done]` pada Step 5
14. Klik `[Done]`
15. Verifikasi walkthrough tertutup
16. Verifikasi flag seen diset untuk akun ini (dibaca lewat fixture)

### TC-AC-ACHA-38: Trigger auto hanya sekali dan replay manual tidak mereset flag

17. Atur flag `guided_tooltip_seen_ac-device-allocation` akun Principal menjadi sudah diset lewat fixture
18. Muat ulang halaman Allocation > Device Allocation
19. Verifikasi Table Tools `Search`, `Filter`, `Download` tampil
20. Verifikasi tidak ada walkthrough otomatis
21. Klik tombol `[?]` di sebelah kanan Breadcrumb
22. Verifikasi walkthrough dimulai dari Step 1
23. Verifikasi flag seen tetap diset (replay manual tidak mereset flag)
24. Klik `[Skip]`
25. Verifikasi walkthrough tertutup
26. Muat ulang halaman Allocation > Device Allocation
27. Verifikasi Table Tools `Search`, `Filter`, `Download` tampil
28. Verifikasi tidak ada walkthrough otomatis

### TC-AC-ACHA-39: Klik overlay menutup walkthrough dan mengeset flag seen

29. Atur flag akun Principal menjadi belum diset lewat fixture
30. Muat ulang halaman Allocation > Device Allocation
31. Verifikasi walkthrough muncul
32. Klik overlay gelap di luar spotlight
33. Verifikasi walkthrough tertutup (setara `[Skip]`)
34. Verifikasi flag seen diset
35. Muat ulang halaman Allocation > Device Allocation
36. Verifikasi Table Tools `Search`, `Filter`, `Download` tampil
37. Verifikasi tidak ada walkthrough otomatis

### TC-AC-ACHA-40: Keluar tanpa menyelesaikan tidak mengeset flag seen

38. Atur flag akun Principal menjadi belum diset lewat fixture
39. Muat ulang halaman Allocation > Device Allocation
40. Verifikasi walkthrough muncul pada Step 1
41. Navigasi ke menu Dashboard lewat sidebar
42. Verifikasi halaman Dashboard terbuka
43. Verifikasi walkthrough tertutup
44. Verifikasi flag seen belum diset
45. Buka Allocation > Device Allocation lewat sidebar
46. Verifikasi walkthrough muncul lagi otomatis dari Step 1

### TC-AC-ACHA-41: Interaksi keyboard walkthrough

47. Atur flag akun Principal menjadi belum diset lewat fixture
48. Muat ulang halaman Allocation > Device Allocation
49. Verifikasi walkthrough muncul
50. Verifikasi tooltip box menerima keyboard focus saat aktif
51. Tekan `Enter`
52. Verifikasi walkthrough maju ke `Step 2 of 5`
53. Tekan `→`
54. Verifikasi walkthrough maju ke `Step 3 of 5`
55. Tekan `←`
56. Verifikasi walkthrough kembali ke `Step 2 of 5`
57. Tekan `Esc`
58. Verifikasi walkthrough tertutup
59. Verifikasi flag seen diset

### Ganti akun ke Read Only Distributor

60. Logout dari akun Total Control Principal
61. Login sebagai Read Only Distributor (`readOnlyDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_RO_DIST_PASSWORD`)

### TC-AC-ACHA-42: Walkthrough aktor tanpa tombol Allocation melewati Step 2

62. Atur flag akun Read Only menjadi belum diset lewat fixture
63. Buka Allocation > Device Allocation lewat sidebar sebagai kunjungan pertama
64. Verifikasi walkthrough tampil pada `Step 1 of 4`
65. Verifikasi `[Back]` Hidden di step pertama
66. Untuk setiap baris tabel "Step walkthrough aktor tanpa tombol [+ Allocation]" Step 1 sampai Step 3 dari 4 lakukan langkah 67 sampai 69
67. Verifikasi indikator step dan spotlight pada elemen sesuai tabel
68. Verifikasi Title step sesuai kolom "Title"
69. Klik `[Next]`
70. Verifikasi `Step 4 of 4` dengan spotlight pada kolom Actions dan Title `Allocation Actions`
71. Verifikasi `[Next]` berubah menjadi `[Done]` di step terakhir
72. Verifikasi walkthrough tidak memuat step dengan Title `Allocate Device` (Step 2 dilewati dan nomor step dihitung ulang)
73. Klik `[Done]`
74. Verifikasi walkthrough tertutup
75. Verifikasi flag seen diset untuk akun Read Only

### Ganti akun ke Total Control Distributor

76. Logout dari akun Read Only Distributor
77. Login sebagai Total Control Distributor (`totalControlDistributor_automated_qaTeam1@qwertysystem.net`, password dari `Spectra.env.AC_DA_TC_DIST_PASSWORD`)

### TC-AC-ACHA-43: Flag seen bersifat per akun

78. Atur flag akun Principal menjadi sudah diset lewat fixture
79. Verifikasi flag seen untuk akun Principal sudah diset (dibaca lewat fixture)
80. Atur flag akun Total Control Distributor menjadi belum diset lewat fixture
81. Buka Allocation > Device Allocation lewat sidebar
82. Verifikasi walkthrough muncul otomatis untuk akun ini
83. Klik `[Skip]`

## Notes

- Mode: FE+BE. Sumber: `admin-console/device-allocation/TestCases/tc-device-allocation.md`. Spec walkthrough; flag diatur per TC (pengecualian hook suite bagian 4).
- Langkah penghubung (S-03): langkah pengaturan flag lewat fixture, muat ulang halaman untuk memulai kunjungan pertama, langkah ganti akun (subjudul "Ganti akun ..."), dan `[Skip]` terakhir pada TC-43 (menutup walkthrough agar sesi tidak berakhir dengan overlay terbuka). Langkah navigasi ke Dashboard pada TC-40 adalah pilihan spec atas klausa "atau" di Langkah Uji (viewport tidak diubah).
- Anchor (S-02, bagian 8b butir 2): `Verifikasi` Table Tools `Search`, `Filter`, `Download` tampil (langkah 19, 27, 36) membuktikan halaman termuat sebelum asersi "tidak ada walkthrough otomatis" (langkah 20, 28, 37); `Verifikasi` walkthrough tampil pada Step 1 (langkah 3 dan 64) mendahului asersi `[Back]` Hidden (langkah 4 dan 65); langkah 42 (halaman Dashboard terbuka) mendahului asersi walkthrough tertutup (langkah 43). Pembacaan flag seen lewat fixture (langkah 16, 23, 34, 44, 59, 75, 79) adalah observasi state, bukan klaim pada langkah aksi.
- Tidak ada ketergantungan antar TC: TC-38 dan TC-43 mengatur flag akun Principal menjadi sudah diset lewat fixture (langkah 17 dan 78) sehingga berdiri sendiri.
- Langkah berulang (bagian 8b butir 7): langkah 6 sampai 9 diulang empat kali (Step 1 sampai Step 4), langkah 67 sampai 69 tiga kali; parameter ada di tabel Prerequisites.
- Ukuran spec (di atas sekitar 35 langkah): satu topik (Guided Tooltip) dengan tiap Expected menjadi `Verifikasi` sendiri; tiap blok TC mengatur flag sendiri sehingga bagian sesudahnya tetap bermakna walau blok sebelumnya gagal.
- Temuan untuk QA:
  - TC-43 tidak menyebut akun kedua dan Langkah Uji 1 hanya "login sebagai akun kedua"; spec memakai Total Control Distributor (Pre-setup #27) dengan flag diatur belum diset, dan membaca flag akun Principal sebagai pembanding.
  - TC-40 Langkah Uji 2 menyebut dua jalan ("ubah ukuran viewport sehingga walkthrough tertutup, atau navigasi ke menu lain"); spec memilih navigasi ke Dashboard agar deterministik.
  - TC-37 Expected a sampai e tidak menyebut batas teks Description dipotong atau tidak; spec mengasersi teks persis.
  - Pembacaan dan pengaturan flag seen per akun tidak punya kontrak di TC, PRD, atau LLD (`foundation/functions/guided-tooltip.md §16.1` hanya menyebut perilaku); disediakan tim FE/BE (S-11, S-13).
  - Post Condition TC-37 sampai TC-43 bernilai `-`.
