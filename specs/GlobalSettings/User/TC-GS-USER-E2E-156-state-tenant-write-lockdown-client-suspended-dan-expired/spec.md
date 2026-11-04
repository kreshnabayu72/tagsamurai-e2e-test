---
id: TC-GS-USER-E2E-156-state-tenant-write-lockdown-client-suspended-dan-expired
title: "State Tenant: Write-Lockdown Client Suspended dan Expired"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-USER-984
  - TC-GS-USER-1021
  - TC-GS-USER-1022
  - TC-GS-USER-1023
  - TC-GS-USER-1024
  - TC-GS-USER-1025
  - TC-GS-USER-1026
coverage:
  web: automated
---

# State Tenant: Write-Lockdown Client Suspended dan Expired

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`); berlaku untuk akun Total Control kedua Client uji di bawah (flag disetel untuk akun aktor yang dipakai spec).
- Akun yang diuji (spec memakai dua akun dan berganti akun secara eksplisit). Kedua akun adalah Total Control dari Client yang statusnya sudah Suspended atau Expired; akun dan Client ini tidak ada di Tabel Data Uji Pre-setup dan disediakan tim FE:

  | Urutan | Role | Email | Environment variable password |
  |---|---|---|---|
  | 1 | Total Control Client Suspended (disediakan tim FE) | akun disediakan tim FE | `GS_CLIENTSUSP_TC_PASSWORD` |
  | 2 | Total Control Client Expired (disediakan tim FE) | akun disediakan tim FE | `GS_CLIENTEXP_TC_PASSWORD` |

  Login akun 1 di hook `before` lalu membuka Global Settings > User > User List (sub-tab Login User); hook `after` mengembalikan sesi ke akun default suite (Total Control Client A, `Spectra.env.GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Env var: `GS_CLIENTSUSP_TC_PASSWORD`, `GS_CLIENTEXP_TC_PASSWORD`, `GS_TC_PASSWORD`.
- Kemampuan teknis: klien HTTP yang mengirim request Edit user langsung ke server dengan token sesi akun yang sedang login, tanpa lewat UI (endpoint dan cara menangkap token disediakan tim FE; TC dan PRD tidak menyebutnya).
- Data: Client Suspended dan Client Expired adalah Client tetap yang disiapkan tim FE. Karena aksi tulis ditolak pada kedua Client, spec tidak men-seed data di dalamnya dan hanya membaca; masing-masing Client memuat salinan data Pre-setup (Tabel Data Uji Pre-setup No. 10 sampai 22, disediakan tim FE): Login User `Dewi Lestari` (Activated, Active, Custom Field `Blood Type` bernilai `A`) beserta sedikitnya satu entri Changelog. Spec tidak mengubah data Client mana pun dan tidak mengubah status Client, sehingga tidak ada state global yang diubah dan tidak ada cleanup selain mengembalikan sesi.
- TC-GS-USER-984, 1021, 1022, 1023, 1024, 1025: Client berstatus Suspended. TC-GS-USER-1026: Client berstatus Expired. Semuanya login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User).

## Test Steps

### Client Suspended: kontrol tulis Disabled (TC-GS-USER-1021, 1022, 1023, 1024)

1. Klik icon Search, ketik `Dewi Lestari`, tekan Enter
2. Hover `[+ User]`
3. Verifikasi `[+ User]` tampil
4. Verifikasi `[+ User]` disabled
5. Verifikasi tooltip `"You don't have permission to edit."` tampil pada `[+ User]`
6. Hover switch Active baris `Dewi Lestari`
7. Verifikasi switch Active baris `Dewi Lestari` tampil
8. Verifikasi switch Active baris `Dewi Lestari` disabled
9. Verifikasi tooltip `"You don't have permission to edit."` tampil pada switch Active baris `Dewi Lestari`
10. Klik `⋯` pada baris `Dewi Lestari`
11. Verifikasi opsi `Edit` dan `Delete` di overlay (⋯) tampil
12. Verifikasi opsi `Edit` dan `Delete` di overlay (⋯) disabled
13. Hover opsi `Edit`
14. Verifikasi tooltip `"You don't have permission to edit."` tampil pada opsi `Edit`
15. Hover opsi `Delete`
16. Verifikasi tooltip `"You don't have permission to edit."` tampil pada opsi `Delete`
17. Tekan Esc untuk menutup overlay (⋯)
18. Klik Name `Dewi Lestari`
19. Verifikasi icon inline edit Custom Field `Blood Type` di Detail tampil
20. Verifikasi icon inline edit Custom Field `Blood Type` di Detail disabled
21. Hover icon inline edit Custom Field `Blood Type`
22. Verifikasi tooltip `"You don't have permission to edit."` tampil pada icon inline edit Custom Field `Blood Type`

### Client Suspended: aksi tulis tidak diproses dan data tetap terbaca (TC-GS-USER-984)

23. Kembali ke User List dengan klik Back
24. Verifikasi baris `Dewi Lestari` tampil di tabel User List
25. Klik `[+ User]`
26. Verifikasi Popup Create User tidak terbuka
27. Klik switch Active baris `Dewi Lestari`
28. Verifikasi tidak ada dialog konfirmasi Deactivate yang tampil
29. Verifikasi switch Active baris `Dewi Lestari` tetap ON
30. Klik `⋯` pada baris `Dewi Lestari`, lalu klik opsi `Edit`
31. Verifikasi Popup Edit User tidak terbuka
32. Klik opsi `Delete`
33. Verifikasi tidak ada dialog `Delete User` yang tampil
34. Tekan Esc untuk menutup overlay (⋯)
35. Verifikasi baris `Dewi Lestari` tampil di tabel User List
36. Klik Name `Dewi Lestari`
37. Verifikasi Detail `Dewi Lestari` tampil
38. Klik Tab `Changelog`
39. Verifikasi Tab Changelog memuat sedikitnya satu baris log
40. Kembali ke User List dengan klik Back

### Client Suspended: request langsung ditolak (TC-GS-USER-1025)

41. Catat Last Update baris `Dewi Lestari` sebagai `{lu}`
42. Tangkap token sesi Total Control Client Suspended, lalu kirim request Edit user `Dewi Lestari` langsung ke server tanpa lewat UI
43. Verifikasi server menolak dengan `403`
44. Muat ulang halaman User List
45. Klik icon Search, ketik `Dewi Lestari`, tekan Enter
46. Verifikasi Last Update baris `Dewi Lestari` sama dengan `{lu}` (data tidak berubah)

### Client Expired: kontrol tulis sama dengan Suspended (TC-GS-USER-1026)

47. Ganti akun: logout, lalu login sebagai Total Control Client Expired (akun disediakan tim FE) dengan `Spectra.env.GS_CLIENTEXP_TC_PASSWORD`, lalu buka Global Settings > User > User List
48. Klik icon Search, ketik `Dewi Lestari`, tekan Enter
49. Verifikasi `[+ User]` dan switch Active baris `Dewi Lestari` tampil
50. Verifikasi `[+ User]` dan switch Active baris `Dewi Lestari` disabled
51. Hover `[+ User]`
52. Verifikasi tooltip `"You don't have permission to edit."` tampil pada `[+ User]`
53. Hover switch Active baris `Dewi Lestari`
54. Verifikasi tooltip `"You don't have permission to edit."` tampil pada switch Active baris `Dewi Lestari`

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`. Kelas state tenant (prinsip 13h): write-lockdown Client Suspended dan Expired pada akun Total Control Client yang statusnya sudah ditetapkan; TC-GS-USER-1025 (request langsung ke server) adalah penolakan server atas write-lockdown tenant dan diasersi sebagai bagian kelas ini.
- Subjudul `###` memetakan langkah ke id TC granular.
- Urutan TC sumber diubah: TC-GS-USER-1021, 1022, 1023, 1024 (screening tooltip, tanpa aksi) lebih dulu, lalu TC-GS-USER-984 (klik pada kontrol Disabled), TC-GS-USER-1025 (request langsung), dan TC-GS-USER-1026 (akun Client Expired) paling akhir karena membutuhkan ganti akun eksplisit (langkah 47); state tooltip diasersi tepat sesudah hover (bagian 8b butir 5).
- Spec melewati sekitar 35 langkah (54 langkah). Alasan: tujuh TC semuanya satu kelas (13h) dan satu layar, tiap TC mengasersi tampil, disabled, dan tooltip sebagai klausa terpisah pada beberapa kontrol (`[+ User]`, switch Active, opsi Edit dan Delete, icon inline edit; S-01), dan blok tiap kontrol berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 45, 48 (Search); langkah 10, 13, 15, 17, 18, 21, 30, 32, 34 (membuka dan menutup overlay, Detail, dan hover); langkah 2, 6, 51, 53 (hover untuk tooltip); langkah 23, 40 (Back ke User List); langkah 25, 27, 36, 38 (klik pada kontrol yang diuji TC-GS-USER-984); langkah 41 (mencatat Last Update sebagai pembanding langkah 46); langkah 44 (memuat ulang); langkah 47 (ganti akun). Langkah 24 (`Verifikasi` baris `Dewi Lestari` tampil di User List sesudah Back) adalah anchor positif bagi `Verifikasi` aksi tidak diproses pada langkah 26, 28, 29, 31, dan 33 (bagian 8b butir 2); langkah 35 mengonfirmasi baris tetap tampil sesudah semua aksi.
- Asersi tambahan di luar Expected TC: langkah 26, 28, 29, 31, 33 membuktikan "tidak ada aksi tulis yang berhasil diproses" pada Expected a TC-GS-USER-984 dengan mengamati bahwa form atau dialog tidak muncul dan status tidak berubah; langkah 46 adalah state data untuk Expected c TC-GS-USER-1025.
- Pembagian TC: aksi tulis lewat UI saat Client Suspended atau Expired (Create, Edit, Delete, Toggle Active) tidak diuji dengan memicu server karena kontrolnya Disabled; penolakan server diasersi hanya lewat TC-GS-USER-1025.
- Tidak ada TC yang terbelah lintas spec.
- Temuan untuk QA:
  - TC-GS-USER-984, 1021 sampai 1026: precondition "Client berstatus suspended" atau "expired" tidak menyebut Client, akun, dan cara menyiapkan data di Client yang terkunci; disediakan tim FE sebagai Client tetap dengan salinan data Pre-setup (S-13).
  - TC-GS-USER-984: Langkah Uji "coba klik" kontrol Disabled tidak menyebut hasil terlihat selain "tidak ada aksi tulis yang berhasil diproses"; spec mengasersi form atau dialog tidak muncul dan status tidak berubah. Expected b ("Data tetap dapat dibaca (List, Detail, log)") tidak menyebut log mana; spec memakai Tab Changelog pada Detail dan mengasumsikan Dewi punya sedikitnya satu entri Changelog.
  - TC-GS-USER-1025: Expected b (toast error `"Changes can't be saved while this workspace is suspended or expired."`) adalah perilaku FE untuk request langsung; tidak diasersi di spec ini (bagian 8b butir 1). TC juga tidak menyebut payload Edit; spec mengirim request Edit untuk Dewi dan membandingkan Last Update.
  - TC-GS-USER-1026: Langkah Uji menyebut "Hover `[+ User]` dan switch Active" tanpa menyebut baris; spec memakai baris `Dewi Lestari`. TC tidak menyebut perilaku opsi overlay, icon inline edit, dan request langsung pada Client Expired; spec hanya mengasersi dua kontrol yang disebut.
  - TC-GS-USER-1021 sampai 1024, 1026: tooltip `"You don't have permission to edit."` tertulis dengan tanda kutip ganda; tidak jelas apakah tanda kutip bagian dari teks tooltip atau pembatas.
