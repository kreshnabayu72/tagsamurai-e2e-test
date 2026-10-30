---
id: TC-GS-ACTLOG-E2E-045-independensi-dan-retensi-state-antar-tab-refresh-dan-klik-ulang-menu
title: "Independensi dan Retensi State Antar Tab, Refresh, dan Klik Ulang Menu"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-17
  - TC-GS-ACTLOG-117
  - TC-GS-ACTLOG-121
  - TC-GS-ACTLOG-126
coverage:
  web: automated
---

# Independensi dan Retensi State Antar Tab, Refresh, dan Klik Ulang Menu

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (seed BE bersuffix `{runId}-045`, disediakan tim FE/BE; log bersifat append-only sehingga tidak dihapus dan spec tidak mengubahnya). N total diturunkan dari seeding:
  - Tab Session dan Tab User Action masing-masing memuat lebih dari 60 baris (TC-GS-ACTLOG-121) dan lebih dari 30 baris (TC-GS-ACTLOG-126).
  - Tab Session memuat lebih dari 25 baris User `Budi Anwar {runId}-045` dengan Activity `Login`, sehingga Search `Budi` dengan Filter Activity `Login` memberi halaman 2 pada page size 25 (TC-GS-ACTLOG-121).
  - Tab User Action memuat baris Name `Acme Corp {runId}-045` dengan Action `Edit`, sehingga Search `Acme` dengan Filter Action `Edit` memberi hasil.
  - Kata Search `John`, `Budi`, dan `Acme` ditulis literal sesuai TC karena asersi berupa state Search, Filter, dan Sort, bukan isi baris tertentu.
- Kemampuan teknis (disediakan tim FE/BE): seed BE volume baris log Session dan User Action sesuai syarat di atas; volume tersebut tidak dapat dihasilkan lewat aksi nyata modul sumber dalam satu run. Memuat ulang halaman dengan F5.
- Konfigurasi Setup Column tiap tab pada keadaan default saat spec dimulai (TC-GS-ACTLOG-117).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- State global yang diubah: konfigurasi Setup Column kedua tab pada TC-GS-ACTLOG-117 (dikembalikan lewat [Reset to Default] dan [Save] di langkah pemulihan akhir; hook `after` memulihkan dengan cara yang sama sebagai cadangan). Spec tidak membuat atau mengubah data backend. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ACTLOG-17: Search dan Filter tab Session tidak memengaruhi tab User Action

1. Buka Global Settings > Activity Log > Tab "Session", ketik Search `John`, tekan Enter
2. Klik icon Filter, pilih Activity `Login`, klik [Apply]
3. Klik tab "User Action"
4. Verifikasi kotak Search Tab User Action kosong dengan placeholder `"Search user action log..."`
5. Klik icon Filter di Tab User Action
6. Verifikasi field Filter Panel Tab User Action kosong dengan placeholder `"Select date"`
7. Verifikasi field Filter Panel Tab User Action kosong dengan placeholder `"All actions"`
8. Verifikasi field Filter Panel Tab User Action kosong dengan placeholder `"All objects"`
9. Verifikasi field Filter Panel Tab User Action kosong dengan placeholder `"All fields"`
10. Verifikasi field Filter Panel Tab User Action kosong dengan placeholder `"All users"`
11. Verifikasi tabel Tab User Action menampilkan baris tanpa saringan, bukan hasil `John` atau `Login` dari Tab Session

### Pemulihan state antar TC

12. Tutup Filter Panel tanpa [Apply], lalu klik menu Activity Log di sidebar sehingga kedua tab kembali ke default

### TC-GS-ACTLOG-126: State dipertahankan per tab saat pindah tab lalu kembali

13. Pada Tab "Session" ketik Search `Budi`, tekan Enter; klik icon Filter, pilih Activity `Login`, klik [Apply]; klik header kolom Activity satu kali sehingga sort Activity `(↑)` aktif; ubah page size menjadi `25`
14. Klik tab "User Action"
15. Verifikasi Search Tab User Action kosong
16. Verifikasi Filter Tab User Action kosong
17. Verifikasi sort Tab User Action default (Date terbaru di atas)
18. Verifikasi page size Tab User Action default (10 baris)
19. Pada Tab User Action ketik Search `Acme`, tekan Enter; klik icon Filter, pilih Action `Edit`, klik [Apply]; klik header kolom Action satu kali sehingga sort Action `(↑)` aktif
20. Klik tab "Session"
21. Verifikasi Search `Budi` tetap terisi di Tab Session
22. Verifikasi Filter Activity `Login` tetap aktif di Tab Session
23. Verifikasi sort Activity `(↑)` tetap aktif di Tab Session
24. Verifikasi page size 25 tetap aktif di Tab Session
25. Klik tab "User Action"
26. Verifikasi Search `Acme` tetap terisi di Tab User Action
27. Verifikasi Filter Action `Edit` tetap aktif di Tab User Action
28. Verifikasi sort Action `(↑)` tetap aktif di Tab User Action

### Pemulihan state antar TC

29. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default

### TC-GS-ACTLOG-121: State bertahan setelah refresh; klik ulang menu sidebar mengembalikan ke default

30. Pada Tab Session ketik Search `Budi`, tekan Enter; klik icon Filter, pilih Activity `Login`, klik [Apply]; klik header kolom Activity satu kali sehingga sort Activity `(↑)` aktif; ubah page size menjadi `25`; buka halaman 2
31. Tekan F5 untuk memuat ulang halaman
32. Verifikasi Search `Budi` tetap terisi di Tab Session
33. Verifikasi Filter Activity `Login` tetap aktif di Tab Session
34. Verifikasi sort Activity `(↑)` tetap aktif di Tab Session
35. Verifikasi page size 25 tetap aktif di Tab Session
36. Verifikasi halaman 2 tetap aktif di Tab Session
37. Klik menu Activity Log di sidebar
38. Verifikasi Search Tab Session kosong
39. Verifikasi Filter Tab Session kosong
40. Verifikasi sort Tab Session kembali default (Date terbaru di atas)
41. Verifikasi page size Tab Session kembali default (10 baris)
42. Klik tab "User Action", ketik Search `Acme`, tekan Enter; klik icon Filter, pilih Action `Edit`, klik [Apply]; klik header kolom Action satu kali sehingga sort Action `(↑)` aktif; ubah page size menjadi `25`
43. Tekan F5 untuk memuat ulang halaman
44. Verifikasi Search `Acme` tetap terisi di Tab User Action
45. Verifikasi Filter Action `Edit` tetap aktif di Tab User Action
46. Verifikasi sort Action `(↑)` tetap aktif di Tab User Action
47. Verifikasi page size 25 tetap aktif di Tab User Action
48. Klik menu Activity Log di sidebar, lalu klik tab "User Action"
49. Verifikasi Search Tab User Action kosong
50. Verifikasi Filter Tab User Action kosong
51. Verifikasi sort Tab User Action kembali default (Date terbaru di atas)
52. Verifikasi page size Tab User Action kembali default (10 baris)

### TC-GS-ACTLOG-117: Konfigurasi Setup Column tab Session dan tab User Action independen

53. Klik tab "Session", sembunyikan kolom Note lewat Popup Setup Column, klik [Save]
54. Tunggu aksi selesai: Popup Setup Column tertutup
55. Klik tab "User Action"
56. Verifikasi kolom `Date`, `Action`, `Object`, `Name`, `Field`, `Old Value`, `New Value`, dan `Modified By` tampil di Tab User Action
57. Sembunyikan kolom Field lewat Popup Setup Column, klik [Save]
58. Tunggu aksi selesai: Popup Setup Column tertutup
59. Klik tab "Session"
60. Verifikasi kolom Note tetap tersembunyi di Tab Session
61. Verifikasi kolom Session lain tampil di Tab Session
62. Tekan F5 untuk memuat ulang halaman
63. Verifikasi Tab Session menyembunyikan kolom Note saja setelah F5
64. Klik tab "User Action"
65. Verifikasi Tab User Action menyembunyikan kolom Field saja setelah F5

### Pemulihan state akhir

66. Pada Tab User Action buka Popup Setup Column, klik [Reset to Default], klik [Save], lalu tunggu aksi selesai: Popup Setup Column tertutup; klik tab "Session" dan lakukan hal yang sama

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Urutan TC: TC-GS-ACTLOG-17, 126, 121, 117. TC-GS-ACTLOG-126 ditempatkan tepat setelah TC-GS-ACTLOG-17 karena dependensinya (TC-GS-ACTLOG-17); TC-GS-ACTLOG-117 ditempatkan paling akhir karena menyimpan konfigurasi kolom, dan state itu dipulihkan di langkah 66.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah pemulihan 12, 29, dan 66; langkah 5 membuka Filter Panel Tab User Action untuk mengamati field (Expected a TC-17); langkah 54 dan 58 (menunggu [Save] Setup Column selesai sebelum pindah tab, 8b.8); langkah 48 (klik menu sidebar lalu pindah ke Tab User Action).
- Spec di atas smell 35 langkah (66 langkah nominal, tanpa perulangan). Alasan: keempat blok berada pada satu topik dan satu dataset (state per tab Activity Log), tiap blok dimulai dari state default hasil klik ulang menu atau konfigurasi default, dan berdiri sendiri; jumlah langkah terutama berasal dari `Verifikasi` yang dipecah per klausa state (Search, Filter, sort, page size, halaman) dan per field placeholder untuk dua tab (S-01).
- Langkah 30 membuka halaman 2 tanpa syarat karena data seed memastikan halaman 2 tersedia (Prerequisites).
- Sort kolom non-Date dicapai dengan satu klik pada header kolom (`(↑)`); default sort adalah Date terbaru di atas dan default page size 10 baris.
- Temuan untuk QA:
  - TC-121 langkah 1 menulis "buka halaman 2 (jika tersedia)"; spec menetapkan seed yang membuat halaman 2 selalu tersedia, sehingga langkah tidak bersyarat.
  - TC-117 menyebut "Popup Setup Column" dengan [Save]; spec tidak menyebut [Cancel] dan mengikuti label [Reset to Default] dan [Save].
  - TC-117 Expected a berbunyi "setelah langkah 1" padahal pengamatan terjadi pada langkah 2 TC; spec mengasersi kolom Tab User Action setelah berpindah tab dan sebelum menyembunyikan kolom Field.
  - TC-126 Expected a berbunyi "setelah langkah 1" padahal pengamatan terjadi pada langkah 2 TC; spec mengasersi pada langkah pindah tab.
  - Post Condition semua TC bernilai `-`; tidak diasersi.
