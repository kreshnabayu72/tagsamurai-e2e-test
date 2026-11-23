---
id: TC-FA-FAFM-UI-092-guided-tooltip-empat-langkah
title: "Guided Tooltip: empat langkah, navigasi, dan replay"
layer: ui-client
priority: Medium
caseType: Positive
status: ready-for-automation
sourceRules: ["§4.7#r2", "§4.7#r3", "§4.7#r4", "§4.7#r5", "§4.7#r6", "EB-TBL-10"]
smoke: []
dependsOn: []
trace:
  "§4.7#r2": [3, 11, 17, 22]
  "§4.7#r3": [4, 5, 6]
  "§4.7#r4": [12, 13, 14]
  "§4.7#r5": [18, 19, 20]
  "§4.7#r6": [23, 24, 25]
  "EB-TBL-10": [2, 7, 8, 15, 26, 27, 29, 30, 31, 36, 37, 40, 41, 42, 45, 46, 49, 51, 53, 54, 56, 57, 59, 60, 61, 62, 63, 66, 67, 68]
coverage:
  web: automated
---

# Guided Tooltip: empat langkah, navigasi, dan replay

## Prerequisites
- Aktor: Total Control.
- Layar awal: Settings > File Manager.
- Komponen: Guided Tooltip File Manager
- Data:
  - DU-092-1: Akun yang belum pernah membuka halaman File Manager, dengan flag `guided_tooltip_seen_fams-file-manager` belum diset.
  - DU-092-2: Akun yang sudah pernah menyelesaikan atau melewati tur, dengan flag `guided_tooltip_seen_fams-file-manager` bernilai `true`.
    - Indikator langkah yang diharapkan `Step 1 of 4` sampai `Step 4 of 4`, dari format `Step [N] of [Total]` dengan 4 langkah dan `page_key` `fams-file-manager`.
  - DU-092-3: Lebar jendela browser setelah diubah `800` piksel.
- Kondisi:
  - K1: halaman dibuka oleh akun DU-092-1 (kunjungan pertama), sehingga tur Guided Tooltip aktif dari langkah 1.
  - K2: halaman dibuka oleh akun DU-092-2, sehingga tur tidak aktif sampai tombol `[?]` diklik.

## Test Steps

### Tur muncul otomatis di kunjungan pertama dengan langkah 1
1. Tampilkan Guided Tooltip File Manager dengan kondisi K1
2. Verifikasi Guided Tooltip tampil otomatis tanpa klik apa pun
3. Verifikasi indikator langkah `Step 1 of 4` tampil
4. Verifikasi judul tooltip `Storage Usage` tampil
5. Verifikasi deskripsi `See how much storage Fixed Asset uses and how close your organization is to its quota.` tampil
6. Verifikasi spotlight menyorot Storage Usage card
7. Verifikasi tombol `[Skip]` dan `[Next]` tampil
8. Verifikasi tombol `[Back]` tidak tampil pada langkah 1

### Next berpindah dari langkah 2 sampai langkah 4 dan Done menutup tur
9. Tampilkan Guided Tooltip File Manager dengan kondisi K1
10. Klik `[Next]`
11. Verifikasi indikator langkah `Step 2 of 4` tampil
12. Verifikasi judul `File categories` tampil
13. Verifikasi deskripsi `Each tab lists the photos and documents uploaded to your assets by category.` tampil
14. Verifikasi spotlight menyorot Category tabs
15. Verifikasi tombol `[Back]` tampil pada langkah 2
16. Klik `[Next]`
17. Verifikasi indikator langkah `Step 3 of 4` tampil
18. Verifikasi judul `Disposed & Unmanaged Assets` tampil
19. Verifikasi deskripsi `Review the storage used by disposed and unmanaged assets. Their data can only be deleted from the Asset menu.` tampil
20. Verifikasi spotlight menyorot tab Disposed & Unmanaged Assets
21. Klik `[Next]`
22. Verifikasi indikator langkah `Step 4 of 4` tampil
23. Verifikasi judul `Recycle Bin` tampil
24. Verifikasi deskripsi `Access deleted files before they are permanently removed.` tampil
25. Verifikasi spotlight menyorot tombol Recycle Bin pada header Storage Usage card
26. Verifikasi tombol `[Done]` tampil pada langkah 4
27. Verifikasi tombol `[Next]` tidak tampil pada langkah 4
28. Klik `[Done]`
29. Verifikasi permintaan menyimpan flag `guided_tooltip_seen_fams-file-manager` bernilai `true` terkirim
30. Verifikasi Storage Usage card tampil pada halaman
31. Verifikasi Guided Tooltip tidak tampil setelah Done

### Back kembali ke langkah sebelumnya
32. Tampilkan Guided Tooltip File Manager dengan kondisi K1
33. Klik `[Next]`
34. Klik `[Next]`
35. Klik `[Back]`
36. Verifikasi indikator langkah `Step 2 of 4` tampil setelah Back
37. Verifikasi judul `File categories` tampil setelah Back

### Skip menutup tur dan menyimpan flag
38. Tampilkan Guided Tooltip File Manager dengan kondisi K1
39. Klik `[Skip]`
40. Verifikasi permintaan menyimpan flag `guided_tooltip_seen_fams-file-manager` bernilai `true` terkirim
41. Verifikasi Storage Usage card tampil pada halaman
42. Verifikasi Guided Tooltip tidak tampil setelah Skip

### Klik overlay menutup tur seperti Skip
43. Tampilkan Guided Tooltip File Manager dengan kondisi K1
44. Klik overlay gelap di luar spotlight
45. Verifikasi Storage Usage card tampil pada halaman
46. Verifikasi Guided Tooltip tidak tampil setelah klik overlay

### Tombol keyboard memindah langkah dan Esc menutup tur
47. Tampilkan Guided Tooltip File Manager dengan kondisi K1
48. Tekan `→`
49. Verifikasi indikator langkah `Step 2 of 4` tampil setelah `→`
50. Tekan `←`
51. Verifikasi indikator langkah `Step 1 of 4` tampil setelah `←`
52. Tekan `Esc`
53. Verifikasi Storage Usage card tampil pada halaman
54. Verifikasi Guided Tooltip tidak tampil setelah `Esc`

### Tur tidak muncul otomatis bila flag sudah diset dan [?] memutarnya ulang tanpa mereset flag
55. Tampilkan Guided Tooltip File Manager dengan kondisi K2
56. Verifikasi Storage Usage card tampil pada halaman
57. Verifikasi Guided Tooltip tidak tampil otomatis
58. Klik tombol bantuan `[?]`
59. Verifikasi Guided Tooltip tampil
60. Verifikasi indikator langkah `Step 1 of 4` tampil pada replay
61. Verifikasi judul tooltip `Storage Usage` tampil pada replay
62. Verifikasi flag `guided_tooltip_seen_fams-file-manager` masih bernilai `true` selama replay
63. Verifikasi tidak ada permintaan yang menghapus atau menyetel ulang flag `guided_tooltip_seen_fams-file-manager`

### Menutup tur lewat ubah ukuran jendela tidak menyimpan flag
64. Tampilkan Guided Tooltip File Manager dengan kondisi K1
65. Ubah lebar jendela browser menjadi `800` piksel
66. Verifikasi Storage Usage card tampil pada halaman
67. Verifikasi Guided Tooltip tidak tampil setelah ukuran jendela diubah
68. Verifikasi tidak ada permintaan menyimpan flag `guided_tooltip_seen_fams-file-manager`
