---
id: TC-GS-USER-E2E-099-tab-system-log-detail-sort-3-state-pagination-dan-kombinasi
title: "Tab System Log Detail: Sort 3-State (Date, Kolom Teks, Old/New Value), Pagination, dan Kombinasi Search, Filter, Sort, Pagination"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-612
  - TC-GS-USER-613
  - TC-GS-USER-614
  - TC-GS-USER-629
  - TC-GS-USER-630
coverage:
  web: automated
---

# Tab System Log Detail: Sort 3-State (Date, Kolom Teks, Old/New Value), Pagination, dan Kombinasi Search, Filter, Sort, Pagination

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor UI: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2; kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `USER_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (Tabel Data Uji Pre-setup No. 23 dan 26): hanya dibaca (Division dan Access dipakai sebagai nilai field user seed). Spec tidak mengubah atau menghapus data Pre-setup.
- Data Dinamis, di-seed lewat API di hook `before` (kemampuan seeding user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD). System Log memuat aksi yang dilakukan user sebagai aktor (PRD user.md §8.3). Tiap user diberi Division `Finance` dan Access `Fixed Asset`:
  - Pemilik log `Aktor Log {runId}-099`, email `aktorlog+{runId}-099@qwertysystem.net`, tier Total Control, status Activated, password `Spectra.env.USER_PASSWORD`. Aktivasi akun seed dan sesi API Aktor Log disediakan tim FE/BE (TC, PRD, dan LLD tidak menyebut mekanismenya). Seluruh aksi seed di bawah dijalankan lewat sesi API Aktor Log.
  - Target aksi `Target Alfa {runId}-099` (email `targetalfa+{runId}-099@qwertysystem.net`, Position `Staff`, Employee ID `{empId1}`) dan `Target Beta {runId}-099` (email `targetbeta+{runId}-099@qwertysystem.net`). Employee ID diturunkan dari `{runId}` (digit timestamp, sehingga numerik murni dan unik per run): `{empId1}` = `{runId}991` dan `{empId2}` = `{runId}992`; keduanya dibutuhkan bernilai numerik untuk asersi urutan numerik pada Old Value dan New Value.
  - Aksi seed oleh Aktor Log, berurutan, dengan jeda antar-aksi yang cukup agar urutan Date deterministik (resolusi tampilan Date tidak disebut TC maupun PRD; jeda disediakan tim FE/BE): (1) Create `Target Alfa` (Field `Name`, Old Value `—`); (2) Create `Target Beta`; (3) Edit Position `Target Alfa` dari `Staff` menjadi `Supervisor`; (4) Edit Employee ID `Target Alfa` dari `{empId1}` menjadi `{empId2}`; (5) 18 kali Edit Position `Target Alfa` bergantian `Supervisor` ke `Staff` dan `Staff` ke `Supervisor` (berakhir `Supervisor`); (6) Deactivate `Target Alfa` (Field `Status (Global)`, `Active` menjadi `Inactive`); (7) Activate `Target Alfa` (`Inactive` menjadi `Active`); (8) Delete `Target Beta` (Field `Name`, New Value `—`); (9) Assign Total Control ke `Target Alfa` (Object `Total Control`, Field `Access Level`, New Value `Total Control`). Entri ke-9 menjadi entri terbaru dan entri ke-1 menjadi entri tertua.
  - Hasil: 26 entri (TC-GS-USER-629 menyebut tabel berisi 25 baris (fixture BE, Pre-setup No. 29); 26 baris membuat halaman 1 berisi tepat 25 baris pada page size 25 dan halaman 3 berisi 6 baris pada page size 10). Kolom Action memuat `Activate`, `Assign`, `Create`, `Deactivate`, `Delete`, `Edit`; kolom Object memuat `Total Control` dan `User`; kolom Name memuat `Target Alfa` dan `Target Beta`; kolom Field memuat `Access Level`, `Employee ID`, `Name`, `Position`, `Status (Global)`; kolom Old Value memuat numerik (`{empId1}`), teks, dan `—`; kolom New Value memuat numerik (`{empId2}`), teks, dan `—` (sedikitnya dua nilai distinct per kolom, S-11). Search `alfa` mencocokkan 24 entri (semua kecuali Create dan Delete `Target Beta`); Filter Action `Edit` mencocokkan 20 entri (19 Edit Position dan 1 Edit Employee ID).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Target Alfa` (cabut tier Total Control lebih dulu bila diperlukan), `Target Beta` bila masih ada, dan `Aktor Log`; hapus sisa user bersuffix `-099` dari run lama. Entri log tidak bisa dihapus.
- Kemampuan teknis: klik header kolom sort; mengubah page size (10, 25, 100); mengetik nomor halaman di input Pagination.
- State global yang diubah: tidak ada (sort, filter, dan page size hanya state tampilan tab). Suite berjalan serial (`parallel: false`).
- Precondition TC-GS-USER-612, 613, 614, 629, 630: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User). TC-GS-USER-629: tabel berisi 25 baris atau lebih.

## Test Steps

### Pembukaan tab

1. Klik icon Search di User List, ketik `Aktor Log {runId}-099`, tekan Enter
2. Klik Name `Aktor Log {runId}-099`
3. Klik Tab `System Log`
4. Ubah page size ke 100

### TC-GS-USER-612: Sort 3-state kolom kelas tanggal

5. Klik header Date
6. Verifikasi Date Oldest First (baris pertama Action `Create`)
7. Klik header Date
8. Verifikasi Date Newest First (baris pertama Action `Assign`)
9. Klik header Date
10. Verifikasi Date kembali ke default sort tabel Newest First (baris pertama Action `Assign`)

### TC-GS-USER-613: Sort 3-state kolom kelas teks A-Z

11. Klik header Action
12. Verifikasi Action ascending A-Z (baris pertama Action `Activate`, baris terakhir Action `Edit`)
13. Klik header Action
14. Verifikasi Action descending Z-A (baris pertama Action `Edit`, baris terakhir Action `Activate`)
15. Klik header Action
16. Verifikasi Action kembali ke default sort tabel Newest First (baris pertama Action `Assign`)
17. Klik header Object
18. Verifikasi Object ascending A-Z (baris pertama Object `Total Control`, baris terakhir Object `User`)
19. Klik header Object
20. Verifikasi Object descending Z-A (baris pertama Object `User`, baris terakhir Object `Total Control`)
21. Klik header Object
22. Verifikasi Object kembali ke default sort tabel Newest First (baris pertama Action `Assign`)
23. Klik header Name
24. Verifikasi Name ascending A-Z (baris pertama Name `Target Alfa {runId}-099`, baris terakhir Name `Target Beta {runId}-099`)
25. Klik header Name
26. Verifikasi Name descending Z-A (baris pertama Name `Target Beta {runId}-099`, baris terakhir Name `Target Alfa {runId}-099`)
27. Klik header Name
28. Verifikasi Name kembali ke default sort tabel Newest First (baris pertama Action `Assign`)
29. Klik header Field
30. Verifikasi Field ascending A-Z (baris pertama Field `Access Level`, baris terakhir Field `Status (Global)`)
31. Klik header Field
32. Verifikasi Field descending Z-A (baris pertama Field `Status (Global)`, baris terakhir Field `Access Level`)
33. Klik header Field
34. Verifikasi Field kembali ke default sort tabel Newest First (baris pertama Action `Assign`)

### TC-GS-USER-614: Sort 3-state kolom kelas nilai campuran

35. Klik header Old Value
36. Verifikasi Old Value klik 1: baris pertama Old Value `{empId1}` (numerik lebih dulu)
37. Verifikasi Old Value klik 1: baris kedua Old Value `Active` (teks sesudah numerik)
38. Verifikasi Old Value klik 1: baris terakhir Old Value `—` (kosong di akhir)
39. Klik header Old Value
40. Verifikasi Old Value klik 2: baris pertama Old Value `—` (kosong di awal)
41. Verifikasi Old Value klik 2: baris Old Value `Target Beta {runId}-099` (teks) berada sebelum baris Old Value `{empId1}` (numerik)
42. Verifikasi Old Value klik 2: baris terakhir Old Value `{empId1}` (numerik di akhir)
43. Klik header Old Value
44. Verifikasi Old Value kembali ke default sort tabel Newest First (baris pertama Action `Assign`)
45. Klik header New Value
46. Verifikasi New Value klik 1: baris pertama New Value `{empId2}` (numerik lebih dulu)
47. Verifikasi New Value klik 1: baris kedua New Value `Active` (teks sesudah numerik)
48. Verifikasi New Value klik 1: baris terakhir New Value `—` (kosong di akhir)
49. Klik header New Value
50. Verifikasi New Value klik 2: baris pertama New Value `—` (kosong di awal)
51. Verifikasi New Value klik 2: baris New Value `Total Control` (teks) berada sebelum baris New Value `{empId2}` (numerik)
52. Verifikasi New Value klik 2: baris terakhir New Value `{empId2}` (numerik di akhir)
53. Klik header New Value
54. Verifikasi New Value kembali ke default sort tabel Newest First (baris pertama Action `Assign`)

### TC-GS-USER-629: Pagination ubah page size dan input nomor halaman

55. Ubah page size ke 25
56. Verifikasi halaman 1 memuat 25 baris (maksimal 25 baris)
57. Ubah page size ke 10
58. Ketik nomor halaman `2` di input nomor halaman, tekan Enter
59. Verifikasi langsung berada di halaman 2
60. Klik next
61. Verifikasi berpindah ke halaman 3
62. Klik prev
63. Verifikasi berpindah kembali ke halaman 2

### TC-GS-USER-630: Kombinasi Search, Filter, Sort, dan Pagination berjalan bersamaan

64. Klik icon Search, ketik `alfa`, tekan Enter
65. Klik icon Filter, pilih Action `Edit`, klik `[Apply]`
66. Klik header Field
67. Ubah page size ke 25
68. Verifikasi Search tetap berlaku (input Search berisi `alfa`)
69. Verifikasi sedikitnya satu baris tampil di tabel
70. Verifikasi semua baris bernilai Action `Edit` (Filter tetap berlaku)
71. Verifikasi Sort tetap berlaku (Field ascending A-Z, baris pertama Field `Employee ID`)
72. Verifikasi Pagination tetap berlaku (halaman 1 memuat 20 baris pada page size 25)

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pemilik log: TC sumber memakai `Siti Nurhaliza` sebagai pemilik System Log; isi log user itu bergantung pada aksi spec lain. Spec memakai user milik spec (`Aktor Log`) dengan aksi seed yang diketahui (S-06, S-11).
- Urutan TC dalam spec mengikuti `sourceTc` (612, 613, 614, 629, 630). TC-GS-USER-630 di akhir karena memasang Search, Filter, dan Sort yang tidak dilepas; state tampilan tab tidak tersimpan.
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-14): langkah 1 sampai 3 (membuka User Detail; Name dicari di User List) dan langkah 4 (page size 100 agar seluruh 26 baris tampil pada satu halaman dan baris terakhir dapat diamati pada TC-GS-USER-612 sampai 614). TC-GS-USER-629 mengubah page size ke 25 dan kembali ke 10 sesuai langkah TC (langkah 55 dan 57).
- Sort 3-state: klik 3 pada tiap kolom mengembalikan sort ke default tabel Newest First, yang sama dengan klik 2 pada kolom Date; kedua kondisi dibedakan oleh langkah klik yang bernomor, bukan oleh urutan baris. Asersi sort memakai nilai baris pertama dan baris terakhir yang tidak bergantung pada urutan antar-entri bernilai sama.
- Spec melewati sekitar 35 langkah (72 langkah) karena TC-GS-USER-613 dan 614 menguji enam kolom, masing-masing tiga klik dan tiga `Verifikasi` (S-01). Semua blok satu kelas (Sort, Pagination, dan kombinasi pada Tab System Log), satu akun, satu dataset, dan tiap blok berdiri sendiri karena sort dikembalikan ke default pada klik ketiga.
- Anchor positif (bagian 8b butir 2): langkah 69 (`Verifikasi sedikitnya satu baris tampil di tabel`) mendahului asersi "semua baris" Action `Edit` pada langkah 70.
- Pembagian TC lintas spec: Search saja di spec 096; Filter saja di spec 097; kombinasi Search dan Filter dengan Clear di spec 098.
- Temuan untuk QA: (1) TC-GS-USER-612 dan 613 "default sort tabel" dibaca sebagai Date Newest First (PRD user.md §4.1.6). (2) TC-GS-USER-629 Data Uji menyebut tabel berisi 25 baris (fixture BE) pada `Siti Nurhaliza` tanpa cara menyiapkan; spec menyiapkan 26 entri lewat aksi seed pada user milik spec (S-06). (3) TC-GS-USER-630 langkah 4 "Terapkan filter bila tersedia" bersyarat; spec menerapkan Filter Action `Edit` tanpa syarat karena Filter Panel tersedia. (4) TC-GS-USER-614 menyebut nilai numerik tanpa contoh; spec memakai Employee ID `{empId1}` menjadi `{empId2}` sebagai satu-satunya nilai numerik. (5) Resolusi tampilan Date tidak disebut TC maupun PRD; urutan antar-entri yang dibuat dalam menit yang sama bergantung pada jeda seeding.
