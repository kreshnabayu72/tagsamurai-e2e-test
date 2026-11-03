---
id: TC-FA-FAAL-E2E-030-filter-panel-draft-badge-dan-keyboard-kedua-tab
title: "Filter Panel Kedua Tab: Draft, Badge, Independen dari Kolom, dan Keyboard"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-98
  - TC-FA-FAAL-99
  - TC-FA-FAAL-100
  - TC-FA-FAAL-286
coverage:
  web: automated
---

# Filter Panel Kedua Tab: Draft, Badge, Independen dari Kolom, dan Keyboard

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Admin Alpha, Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.FA_TC_PASSWORD` (didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log, Tab Session). Tidak ada ganti akun di tengah spec.
- Data Pre-setup #11 (Tab Session SS-01 sampai SS-11) dan #12 (Tab User Action UA-01 sampai UA-15), hanya dibaca dan tidak diubah. Baris yang dipakai: Tab Session SS-03, SS-05 (Position `—`), SS-09, SS-11 (Division `Finance`); Tab User Action UA-01 dan UA-07 (Action `Assign`), UA-04, UA-05, UA-06, UA-10 (Field `Status`). Identitas baris dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE); nama dan nilai ditulis seperti di TC.
- Nilai Data Uji TC: Position `Staff`; Division `Finance` dan `Marketing`; Action `Delete` dan `Assign`; Field `Status` (ditulis seperti di TC).
- Kemampuan teknis: navigasi keyboard (`Tab` dan `Enter`) pada Filter Panel.
- Posisi dan isi baris pada asersi bergantung pada Tab Session dan Tab User Action client uji yang hanya memuat baris seed #11 dan #12 saat spec berjalan; jaminan itu disediakan tim FE/BE (lihat Temuan untuk QA). Total entri tidak diasersi sebagai angka absolut.
- State yang diubah spec: Filter kedua tab dan visibilitas kolom Division (Tab Session) serta Field (Tab User Action). Filter dibersihkan oleh langkah penghubung dan di-reset pembukaan layar hook `beforeEach` suite sebelum spec berikutnya; visibilitas kolom dipulihkan oleh langkah 34 dan 42, dan hook `after` memulihkannya dengan menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Flag Guided Tooltip halaman Activity Log di-set true oleh hook suite `before` untuk akun aktor (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-99: Badge titik Filter dan nilai kosong tidak punya opsi filter

1. Verifikasi icon Filter tanpa badge titik
2. Klik icon Filter, pilih Position `Staff`, klik `[Apply]`
3. Klik icon Filter untuk menutup panel
4. Verifikasi badge titik tampil pada icon Filter walau panel tertutup
5. Verifikasi sedikitnya satu baris tampil pada tabel
6. Verifikasi SS-05 (Position `—`) tidak tampil
7. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
8. Verifikasi badge titik pada icon Filter hilang
9. Verifikasi SS-05 tampil kembali

### TC-FA-FAAL-98: Menutup Filter Panel tanpa Apply membuang draft di kedua tab

10. Klik icon Filter untuk menutup panel
11. Klik icon Filter, pilih Division `Finance`, klik `[Apply]`
12. Pilih juga Division `Marketing` tanpa `[Apply]`
13. Klik icon Filter untuk menutup panel
14. Klik icon Filter untuk membuka kembali panel
15. Verifikasi panel Filter Tab Session menampilkan hanya `Finance` (nilai ter-Apply terakhir)
16. Verifikasi tabel Tab Session tetap menampilkan baris dengan Division `Finance`
17. Klik icon Filter untuk menutup panel
18. Klik tab User Action
19. Catat baris yang tampil pada tabel Tab User Action (baseline)
20. Klik icon Filter, pilih Action `Delete` tanpa `[Apply]`
21. Klik di luar panel
22. Klik icon Filter untuk membuka kembali panel
23. Verifikasi panel Filter Tab User Action kosong tanpa `Delete`
24. Verifikasi tabel Tab User Action tidak berubah dari baseline langkah 19
25. Klik di luar panel
26. Klik tab Session
27. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### TC-FA-FAAL-100: Filter independen dari visibilitas kolom di kedua tab

28. Klik icon Filter untuk menutup panel
29. Klik header Actions (⋯), hilangkan centang kolom `Division` pada overlay Column Visibility
30. Klik icon Filter
31. Verifikasi field Division tetap ada di Filter Panel Tab Session
32. Pilih Division `Finance`, klik `[Apply]`
33. Verifikasi tabel Tab Session menampilkan hanya SS-03, SS-05, SS-09, dan SS-11
34. Klik header Actions (⋯), centang kembali kolom `Division` pada overlay Column Visibility
35. Verifikasi filter Division `Finance` tetap ter-Apply setelah kolom ditampilkan kembali
36. Klik tab User Action
37. Klik header Actions (⋯), hilangkan centang kolom `Field` pada overlay Column Visibility
38. Klik icon Filter
39. Verifikasi field Field tetap ada di Filter Panel Tab User Action
40. Pilih Field `Status`, klik `[Apply]`
41. Verifikasi tabel Tab User Action menampilkan hanya UA-04, UA-05, UA-06, dan UA-10
42. Klik header Actions (⋯), centang kembali kolom `Field` pada overlay Column Visibility
43. Verifikasi filter Field `Status` tetap ter-Apply setelah kolom ditampilkan kembali
44. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
45. Klik tab Session
46. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`
47. Klik icon Filter untuk menutup panel

### TC-FA-FAAL-286: Tombol Clear Field dan Apply Filter Panel dapat dijangkau dengan keyboard di kedua tab

48. Klik icon Filter, pilih Division `Finance` dengan mouse tanpa klik `[Apply]`
49. Tekan `Tab` berulang sampai fokus mencapai `[Clear Field]`, lalu `[Apply]`
50. Verifikasi `[Clear Field]` lalu `[Apply]` menerima fokus lewat `Tab` setelah field Filter pada Tab Session
51. Tekan `Enter` pada `[Apply]`
52. Verifikasi tabel Tab Session menampilkan hanya SS-03, SS-05, SS-09, dan SS-11
53. Klik tab User Action
54. Klik icon Filter, pilih Action `Assign` dengan mouse
55. Tekan `Tab` berulang sampai fokus mencapai `[Clear Field]`, lalu `[Apply]`, kemudian tekan `Enter`
56. Verifikasi `[Clear Field]` lalu `[Apply]` menerima fokus lewat `Tab` setelah field Filter pada Tab User Action
57. Verifikasi tabel Tab User Action menampilkan hanya UA-01 dan UA-07

## Notes

- Alasan di atas 35 langkah (57 langkah): keempat TC memakai Filter Panel kedua tab pada dataset #11 dan #12 yang sama, satu kelas fungsional, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; 10 dari 57 langkah adalah langkah penghubung yang membersihkan state antar-TC (S-09).
- Urutan TC: TC-FA-FAAL-99, 98, 100, 286. TC-FA-FAAL-99 dijalankan lebih dulu karena mensyaratkan icon Filter tanpa badge titik dan Filter bersih; TC-FA-FAAL-98 dan 100 meninggalkan Filter Tab Session yang dibersihkan langkah penghubung sebelum TC berikutnya (S-09, S-10).
- Langkah penghubung (S-03): langkah 10, 25, 26, 27, 28, 44, 45, 46, 47 (membersihkan Filter dan menutup panel antar-TC); langkah 19 (mencatat baris Tab User Action sebagai baseline asersi langkah 24). Langkah 10, 28, dan 47 menutup Filter Panel dengan klik icon Filter karena TC-FA-FAAL-98 langkah 2 menyiratkan panel tetap terbuka sesudah `[Apply]` dan klik icon Filter berikutnya akan menutupnya.
- Langkah 5 adalah anchor positif untuk asersi langkah 6 (butir 8b.2); langkah 33, 41, 52, dan 57 menyebut daftar baris seed sekaligus sebagai pembanding positif asersi "hanya".
- Langkah 24 dan baseline langkah 19: TC-FA-FAAL-98 menulis "tabel tidak berubah" tanpa menyebut cara membandingkan; spec membandingkan dengan baris yang dicatat sebelum aksi (S-12).
- Temuan untuk QA:
  - TC-FA-FAAL-98, 99, 100, 286 mengasumsikan Tab Session dan Tab User Action hanya berisi seed #11 dan #12, padahal Activity Log adalah audit trail permanen yang tumbuh; spec mengikuti TC dan menuliskan jaminan data di Prerequisites sebagai kebutuhan tim FE/BE.
  - TC tidak menyatakan apakah Filter Panel tetap terbuka atau menutup sesudah `[Apply]`; spec memakai pembacaan "tetap terbuka" (TC-FA-FAAL-98 langkah 2 dan TC-FA-FAAL-99 langkah 2) dan menutupnya dengan klik icon Filter pada langkah penghubung.
  - TC-FA-FAAL-98 langkah 4 tidak menyebut membuka Filter Panel Tab User Action sebelum memilih Action `Delete`; spec membukanya eksplisit (langkah 20).
  - TC-FA-FAAL-99 pada judul menyebut "nilai kosong tidak punya opsi filter" tetapi Expected hanya memuat badge titik dan tampil/hilangnya SS-05; spec hanya mengasersi Expected.
  - TC-FA-FAAL-286 tidak menyebut jumlah penekanan `Tab` sampai `[Clear Field]`; spec menulisnya "berulang sampai fokus mencapai" sesuai TC.
