---
id: TC-FA-SU-E2E-280-tab-user-log-sub-tab-assignment-filter-dan-kontrol-filter
title: "Tab User Log sub-tab Assignment: Filter dan Kontrol Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-851
  - TC-FA-SU-852
  - TC-FA-SU-853
  - TC-FA-SU-854
coverage:
  web: automated
---

# Tab User Log sub-tab Assignment: Filter dan Kontrol Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen` dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20) dan User Log (#30). Pengguna target: Budi Santoso. Nama pengguna dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Seed Tab User Log sub-tab Assignment Budi Santoso (Pre-setup #30, 5 baris; urutan default Date descending). Label baris = `Activity|Transaction ID`; alias dipakai langkah:
  - A-1: `Unassigned|ASG-20260618-0089`, Date `30/06/26`, PIC `Eka W` (keyword `Wulandari`)
  - A-2: `Handed over|ASG-20260625-0102`, Name `Lemari`, PIC `Ahmad D`
  - A-3: `Handed over|ASG-20260618-0089`, PIC `Eka W` (keyword `Wulandari`)
  - A-4: `Handed over|ASG-20260512-0067`, PIC `Ahmad D`, Date di dalam rentang 05/05/26 sampai 12/05/26
  - A-5: `Handed over|ASG-20260505-0045`, PIC `Ahmad D`, Date di dalam rentang 05/05/26 sampai 12/05/26
- Kemampuan seed API (disediakan tim BE/FE): menyediakan ulang seed User Log #30 (Catatan TC: fixture yang diubah disediakan ulang lewat seed API) di hook `before` dan `after`. Spec ini hanya membaca surface User Log dan tidak menambah entri pada Budi Santoso.

## Test Steps

### TC-FA-SU-851: Filter kelas enum: Activity

1. Ketik Search `Budi Santoso`, tekan Enter, buka Detail pengguna Budi Santoso lalu klik tab User Log, sub-tab Assignment
2. Klik icon Filter
3. Buka dropdown Activity
4. Verifikasi opsi dropdown Activity = DISTINCT data tabel (`Handed over`, `Unassigned`)
5. Centang `Handed over`
6. Verifikasi chip `Handed over` tampil di dalam field Activity
7. Klik `[Apply]`
8. Verifikasi memilih `Handed over` menyisakan A-2, A-3, A-4, A-5 (4 baris)
9. Klik `[Clear Field]` lalu `[Apply]`

### TC-FA-SU-852: Filter kelas fk: PIC

10. Buka dropdown PIC
11. Verifikasi opsi dropdown PIC = DISTINCT data tabel (`Ahmad D`, `Eka W`)
12. Centang `Ahmad D`
13. Verifikasi chip `Ahmad D` tampil di dalam field PIC
14. Klik `[Apply]`
15. Verifikasi memilih `Ahmad D` menyisakan A-2, A-4, A-5 (3 baris)
16. Klik `[Clear Field]` lalu `[Apply]`

### TC-FA-SU-853: Kombinasi Search dan Filter dua arah

17. Ketik Search `Unassigned`, tekan Enter
18. Verifikasi Search `Unassigned` menyisakan A-1 (anchor sebelum asersi irisan)
19. Buka dropdown Activity, centang `Handed over`
20. Klik `[Apply]`
21. Verifikasi menerapkan Filter tidak mengosongkan keyword Search
22. Verifikasi Search `Unassigned` lalu Filter Activity `Handed over`: hasil irisan tidak ada baris (0 baris)
23. Klik `[Clear Field]` lalu `[Apply]`
24. Klik icon ← pada kotak Search
25. Buka dropdown Activity, centang `Handed over`
26. Klik `[Apply]`
27. Verifikasi Filter Activity `Handed over` menyisakan A-2, A-3, A-4, A-5 (anchor sebelum asersi irisan)
28. Ketik Search `Unassigned`, tekan Enter
29. Verifikasi Filter Activity `Handed over` lalu Search `Unassigned`: hasil identik tidak ada baris
30. Verifikasi menjalankan Search tidak mereset Filter
31. Verifikasi tabel kembali ke halaman 1 saat kriteria berubah
32. Klik icon ← pada kotak Search
33. Klik `[Clear Field]` lalu `[Apply]`

### TC-FA-SU-854: Pelepasan kontrol: Clear Field, Clear Search, ganti kolom sort, dan recovery empty state

34. Ketik Search `Unassigned`, tekan Enter
35. Buka dropdown Activity, centang `Handed over`
36. Klik `[Apply]`
37. Klik header Date satu kali
38. Klik `[Clear Field]` lalu `[Apply]`
39. Verifikasi Clear Field pada Filter: Search `Unassigned` dan Sort Date tetap berlaku
40. Buka dropdown Activity, centang `Handed over`
41. Klik `[Apply]`
42. Klik icon ← pada kotak Search
43. Verifikasi setelah Search dikosongkan, Filter Activity `Handed over` dan Sort Date tetap berlaku
44. Klik header PIC satu kali
45. Verifikasi Ganti kolom sort: sort pindah ke kolom PIC tanpa mereset Filter Activity `Handed over`
46. Ketik Search `zzzz` (tanpa hasil), tekan Enter
47. Verifikasi kombinasi 0 baris menampilkan `No results found` dengan deskripsi `Try adjusting your search or filter.`
48. Klik icon ← pada kotak Search
49. Verifikasi melepas Search langsung memulihkan baris yang cocok dengan Filter Activity `Handed over`
50. Klik `[Clear Field]` lalu `[Apply]`
51. Klik header PIC dua kali lagi hingga netral
52. Klik icon Filter untuk menutup panel

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): pengosongan Search, penutupan overlay, pemulihan Filter dan sort, serta penghapusan preferensi kolom; semuanya hanya mengembalikan state sebelum TC berikutnya (S-09).
- Langkah penghubung pencarian baris (S-03, R-16, bagian 8b butir 13): langkah 1 mencari pengguna lewat Search nama persis `Budi Santoso` (nama Pre-setup) sebelum membuka Detail, karena User List dapat memuat lebih dari satu halaman (25 pengguna, 3 halaman) sehingga spec tidak mengandalkan posisi baris di halaman.
- Panel Filter tetap terbuka sesudah `[Apply]` dan baru tertutup bila icon Filter diklik (keputusan produk); karena itu `[Clear Field]` + `[Apply]` dijalankan tanpa mengklik icon Filter lagi. Langkah 52 (`Klik icon Filter untuk menutup panel`) adalah langkah penghubung yang menutup panel sebelum blok berikutnya (S-03, S-09).
- Spec ini berjumlah 52 langkah (dihitung dengan ekspansi langkah berulang) dan tetap di atas sekitar 35 langkah. Alasan: seluruh TC di dalamnya satu kelas (fungsional) pada satu surface yang sama, berdiri sendiri, dan kegagalan satu blok TC tidak membuat blok lain kehilangan makna; ukuran berasal dari klausa Expected yang wajib punya `Verifikasi` sendiri (S-01), bukan dari langkah tambahan.
- Asersi irisan 0 baris pada TC-FA-SU-853 didahului `Verifikasi` hasil tunggal (Search saja dan Filter saja) sebagai anchor positif (bagian 8b butir 2); keduanya asersi tambahan di luar Expected TC dan dicatat di sini sesuai S-03.
- Temuan untuk QA (S-15): (1) TC mengasersi isi dan urutan baris seed tanpa Filter pembatas pada surface User Log yang dapat bertambah entri; spec mengikuti TC dan mengandalkan seed #30 yang disediakan ulang di hook `before` dan `after` (S-12, S-14). (2) TC-FA-SU-853: Expected a dan b (irisan 0 baris) tidak punya anchor positif di TC; spec menambah `Verifikasi` hasil tunggal sebagai anchor (lihat Notes). TC-FA-SU-854: Expected c menyebut sort pindah tanpa mereset Search dan Filter, tetapi Langkah Uji 4 sudah mengosongkan Search sebelum langkah 5; spec hanya mengasersi Filter yang masih aktif. TC-FA-SU-851 dan 852 menyebut chip di dalam field; spec memverifikasi chip pada panel yang masih terbuka sebelum `[Apply]`; panel tetap terbuka sesudah `[Apply]` (keputusan produk).
