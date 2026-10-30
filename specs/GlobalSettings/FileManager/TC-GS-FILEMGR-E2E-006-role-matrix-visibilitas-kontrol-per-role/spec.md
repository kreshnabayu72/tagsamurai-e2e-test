---
id: TC-GS-FILEMGR-E2E-006-role-matrix-visibilitas-kontrol-per-role
title: "Role Matrix: Visibilitas Kontrol Tabel Utama, Recycle Bin, dan Kartu Storage per Role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-FILEMGR-43
  - TC-GS-FILEMGR-44
  - TC-GS-FILEMGR-45
  - TC-GS-FILEMGR-46
  - TC-GS-FILEMGR-280
coverage:
  web: automated
---

# Role Matrix: Visibilitas Kontrol Tabel Utama, Recycle Bin, dan Kartu Storage per Role

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Total Control) dilakukan di hook `before`; ganti akun ke role berikutnya ditulis sebagai langkah eksplisit di awal tiap blok. Spec berakhir di akun Manage files: Delete; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

Role yang diuji (Tabel Data Uji Pre-setup A1; domain `{namaCompany}`):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-FILEMGR-43 | Total Control | Sinta Maharani | `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-FILEMGR-44 | Read Only | Rina Pratiwi | `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` |
| TC-GS-FILEMGR-45 | Manage files: Read | Doni Saputra | `manageFilesRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_FILES_READ_PASSWORD` |
| TC-GS-FILEMGR-46 | Manage files: Delete | Agus Wibowo | `manageFilesDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_FILES_DELETE_PASSWORD` |

TC-GS-FILEMGR-280 (kartu Storage Usage tampil untuk keempat role) dijalankan sebagai bagian blok tiap role.

- Langkah tiap role berbeda (Hidden vs tampil per elemen), sehingga spec ditulis per blok role, bukan perulangan (bagian 3a konvensi).
- Data Pre-setup (data environment tetap, hanya dibaca): Tabel A2 (33 file aktif, termasuk `budi-avatar.jpg` dengan file fisik), Tabel A3 (16 file di Recycle Bin, termasuk `old-avatar.png`), dan skenario S1 Tabel A5 (Total Used `4.8 GB`, Storage Quota `50.0 GB`, ProgressBar `9%`, `Fixed Asset 3.2 GB`, `Admin Console 1.4 GB`, `Global Settings 204.8 MB`, `Last updated 14/09/26 02:00`). Spec tidak membuat, mengubah, atau menghapus data; aksi Delete, Permanently Delete, dan Download tidak dijalankan, hanya visibilitasnya yang diperiksa.
- Guided Tooltip: flag `guided_tooltip_seen_gs-file-manager` disetel true untuk keempat akun oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: fixture BE untuk Tabel A2, A3, dan S1 (mekanisme seeding tidak disebut di TC, PRD, atau LLD; disediakan tim FE/BE); membaca jumlah tab browser dan URL tab baru.
- State global: tidak ada yang diubah. Capability tiap akun adalah data Pre-setup. Suite berjalan serial (`parallel: false`).

## Test Steps

### Total Control (TC-GS-FILEMGR-43 dan bagian kartu TC-GS-FILEMGR-280)

1. Buka Global Settings > File Manager dari sidebar sebagai Total Control
2. Amati toolbar, kolom Checkbox, dan header Actions tabel utama
3. Verifikasi toolbar tampil `Search | Filter | Download | Changelog | Recycle Bin`
4. Verifikasi kolom Checkbox tampil
5. Verifikasi header Actions (⋯) tampil
6. Klik ikon (⋯) baris `budi-avatar.jpg`
7. Verifikasi overlay baris memuat `Download` dan `Delete`
8. Tutup overlay dengan menekan Esc
9. Centang satu baris
10. Verifikasi Bulk Action Bar tampil dengan aksi Delete
11. Hapus centang baris itu
12. Buka modal Recycle Bin
13. Verifikasi kolom Checkbox tampil di Recycle Bin
14. Klik ikon (⋯) baris `old-avatar.png`
15. Verifikasi overlay baris memuat `Permanently Delete`
16. Tutup overlay dengan menekan Esc, lalu tutup modal Recycle Bin dengan `✕` di header
17. Verifikasi kartu Storage Usage tampil (Show)
18. Verifikasi isi kartu identik dengan skenario S1: Total Used `4.8 GB`, Storage Quota `50.0 GB`, ProgressBar `9%`, `Fixed Asset 3.2 GB`, `Admin Console 1.4 GB`, `Global Settings 204.8 MB`, dan `Last updated 14/09/26 02:00`
19. Verifikasi tidak ada kontrol tulis di kartu Storage Usage

### Read Only (TC-GS-FILEMGR-44 dan bagian kartu TC-GS-FILEMGR-280)

20. Ganti akun: logout, lalu login sebagai Read Only
21. Buka Global Settings > File Manager dari sidebar
22. Amati toolbar, kolom Checkbox, dan header Actions tabel utama
23. Verifikasi toolbar tampil `Search | Filter | Download | Changelog | Recycle Bin`
24. Verifikasi kolom Checkbox tidak tampil (Hidden) sehingga Bulk Action Bar tidak tersedia
25. Verifikasi header Actions (⋯) tampil
26. Klik ikon (⋯) baris `budi-avatar.jpg`
27. Verifikasi overlay baris hanya memuat `Download` (opsi `Delete` Hidden)
28. Tutup overlay dengan menekan Esc
29. Klik teks `budi-avatar.jpg` di kolom File Name
30. Verifikasi satu tab browser baru terbuka menampilkan `budi-avatar.jpg`
31. Tutup tab baru dan kembali ke tab asal
32. Buka modal Recycle Bin
33. Verifikasi kolom Checkbox Hidden di Recycle Bin
34. Verifikasi sel Actions baris `old-avatar.png` kosong (tanpa `Permanently Delete`)
35. Verifikasi header Actions (⋯) tetap tampil di Recycle Bin
36. Tutup modal Recycle Bin dengan `✕` di header
37. Verifikasi kartu Storage Usage tampil (Show)
38. Verifikasi isi kartu identik dengan skenario S1 (Total Used `4.8 GB`, Storage Quota `50.0 GB`, ProgressBar `9%`, `Fixed Asset 3.2 GB`, `Admin Console 1.4 GB`, `Global Settings 204.8 MB`, `Last updated 14/09/26 02:00`)
39. Verifikasi tidak ada kontrol tulis di kartu Storage Usage

### Manage files: Read (TC-GS-FILEMGR-45 dan bagian kartu TC-GS-FILEMGR-280)

40. Ganti akun: logout, lalu login sebagai Manage files: Read
41. Buka Global Settings > File Manager dari sidebar
42. Amati toolbar, kolom Checkbox, dan header Actions tabel utama
43. Verifikasi toolbar tampil `Search | Filter | Download | Changelog | Recycle Bin`
44. Verifikasi kolom Checkbox Hidden sehingga Bulk Action Bar tidak tersedia
45. Klik ikon (⋯) baris `budi-avatar.jpg`
46. Verifikasi overlay baris hanya memuat `Download`
47. Tutup overlay dengan menekan Esc
48. Klik teks `budi-avatar.jpg` di kolom File Name
49. Verifikasi satu tab browser baru terbuka menampilkan `budi-avatar.jpg`
50. Tutup tab baru dan kembali ke tab asal
51. Buka modal Recycle Bin
52. Verifikasi kolom Checkbox Hidden di Recycle Bin
53. Verifikasi sel Actions baris `old-avatar.png` kosong (tanpa `Permanently Delete`)
54. Verifikasi header Actions (⋯) tetap tampil di Recycle Bin
55. Tutup modal Recycle Bin dengan `✕` di header
56. Verifikasi kartu Storage Usage tampil (Show)
57. Verifikasi isi kartu identik dengan skenario S1 (Total Used `4.8 GB`, Storage Quota `50.0 GB`, ProgressBar `9%`, `Fixed Asset 3.2 GB`, `Admin Console 1.4 GB`, `Global Settings 204.8 MB`, `Last updated 14/09/26 02:00`)
58. Verifikasi tidak ada kontrol tulis di kartu Storage Usage

### Manage files: Delete (TC-GS-FILEMGR-46 dan bagian kartu TC-GS-FILEMGR-280)

59. Ganti akun: logout, lalu login sebagai Manage files: Delete
60. Buka Global Settings > File Manager dari sidebar
61. Amati toolbar, kolom Checkbox, dan header Actions tabel utama
62. Verifikasi toolbar tampil `Search | Filter | Download | Changelog | Recycle Bin`
63. Verifikasi daftar tabel terbaca (baris `budi-avatar.jpg` tampil)
64. Verifikasi kolom Checkbox tampil
65. Klik ikon (⋯) baris `budi-avatar.jpg`
66. Verifikasi overlay baris memuat `Download` dan `Delete`
67. Tutup overlay dengan menekan Esc
68. Klik teks `budi-avatar.jpg` di kolom File Name
69. Verifikasi satu tab browser baru terbuka menampilkan `budi-avatar.jpg`
70. Tutup tab baru dan kembali ke tab asal
71. Centang satu baris
72. Verifikasi Bulk Action Bar tampil dengan aksi Delete
73. Hapus centang baris itu
74. Buka modal Recycle Bin
75. Verifikasi kolom Checkbox tampil di Recycle Bin
76. Klik ikon (⋯) baris `old-avatar.png`
77. Verifikasi overlay baris memuat `Permanently Delete`
78. Tutup overlay dengan menekan Esc, lalu tutup modal Recycle Bin dengan `✕` di header
79. Verifikasi kartu Storage Usage tampil (Show)
80. Verifikasi isi kartu identik dengan skenario S1 (Total Used `4.8 GB`, Storage Quota `50.0 GB`, ProgressBar `9%`, `Fixed Asset 3.2 GB`, `Admin Console 1.4 GB`, `Global Settings 204.8 MB`, `Last updated 14/09/26 02:00`)
81. Verifikasi tidak ada kontrol tulis di kartu Storage Usage

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Urutan blok role mengikuti TC-43 sampai TC-46; TC-280 (kartu untuk keempat role) dikerjakan di tiap blok (langkah 17 sampai 19, 37 sampai 39, 56 sampai 58, 79 sampai 81).
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 8, 16, 28, 31, 36, 47, 50, 55, 67, 70, 73, 78 (menutup overlay/modal/tab, menghapus centang), langkah 20, 40, dan 59 (ganti akun), langkah 21, 41, dan 60 (membuka File Manager di akun baru). Langkah 11 (hapus centang) adalah pemulihan state (S-09).
- Alasan spec di atas sekitar 35 langkah (S-10, bagian 3a): spec Role Matrix dengan empat blok role yang tiap bloknya berdiri sendiri lewat Step ganti akun eksplisit; kegagalan keras satu blok role tidak membuat blok role berikutnya kehilangan makna karena tiap blok membuka File Manager dari sidebar sebagai akun barunya. Langkah berbeda per role (elemen Hidden berbeda), sehingga perulangan identik tidak dipakai.
- Asersi `Hidden` memakai anchor permukaan (bagian 8b butir 2): toolbar dan baris tabel yang sudah tampil pada blok yang sama.
- Langkah 27, 46: "hanya memuat `Download`" ditulis satu `Verifikasi` (daftar utuh dalam satu overlay). Langkah 24 dan 44: Hidden kolom Checkbox diperlakukan sebagai kesimpulan tunggal bersama Bulk Action Bar tidak tersedia (S-03).
- Langkah 63 mencakup klausa "daftar tabel terbaca" pada Expected TC-46 butir a; klausa "grant Delete mengimplikasikan Read" tidak diasersi terpisah karena merupakan penjelasan.
- Temuan untuk QA:
  - TC-44, TC-45, dan TC-46 menulis "File Preview terbuka dari klik File Name" dan "tutup modal preview", sedangkan PRD File Preview dan TC-GS-FILEMGR-48 menyatakan web tidak punya modal/dialog preview (file dibuka di tab browser baru). Spec memakai perilaku tab baru (langkah 29 sampai 31, 48 sampai 50, 68 sampai 70); teks TC perlu diselaraskan.
  - TC-280 Expected a menyebut isi kartu "identik dengan TC-GS-FILEMGR-268"; spec menuliskan isi S1 secara eksplisit dari Expected TC-268.
  - TC-44 dan TC-45 Expected b menyatakan Bulk Action Bar "tidak tersedia" tanpa langkah yang memicunya (tidak ada checkbox untuk dicentang); spec memeriksa kolom Checkbox Hidden saja.
  - Mekanisme seeding Tabel A2, A3, dan S1 ("fixture BE") tidak disebut di TC, PRD, atau LLD; disediakan tim FE/BE (S-13).
