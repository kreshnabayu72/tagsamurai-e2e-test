---
id: TC-GS-USER-E2E-081-modal-changelog-user-sort-3-state-pagination-dan-kombinasi
title: "Modal Changelog User: Sort 3-State Semua Kolom, Pagination, dan Kombinasi Search, Filter, Sort, serta Pagination"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-491
  - TC-GS-USER-492
  - TC-GS-USER-493
  - TC-GS-USER-508
  - TC-GS-USER-509
coverage:
  web: automated
---

# Modal Changelog User: Sort 3-State Semua Kolom, Pagination, dan Kombinasi Search, Filter, Sort, serta Pagination

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control (Siti Nurhaliza), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 2); kredensial `Spectra.env.GS_TC_PASSWORD`. Akun ini adalah akun default suite: login di hook `before`, hook `after` mengembalikan sesi ke akun ini. Nama singkat di kolom Modified By: `Siti N` (tooltip `Siti Nurhaliza`). Halaman awal: Global Settings > User > User List (sub-tab Login User). Password tidak ditulis di spec atau fixture.
- Akun aksi lewat API (tidak login UI): Manage user and role, Full CRUD (Fajar Nugroho), `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 4); kredensial `Spectra.env.GS_FULLCRUD_PASSWORD`. Dipakai hanya untuk memicu entri Changelog dengan Modified By kedua `Fajar N` (nama singkat dibentuk seperti `Siti N`; TC tidak menyebutnya), sehingga kolom Modified By punya sedikitnya dua nilai distinct (S-11). Tidak ada sesi UI kedua.
- Env var: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Seeding minimal (S-11; lewat API di hook `before`; kemampuan seeding user dan perubahan user lewat API disediakan tim FE/BE; endpoint tidak disebut di TC dan PRD. Tiap user seed diberi Position `Staff` (Tabel Data Uji Pre-setup No. 22), Division `Finance` (No. 23), dan Access `Fixed Asset` (No. 26), email `<nama>+{runId}-081@qwertysystem.net`. Kuota user plan cukup untuk user seed milik spec ini (disediakan tim FE). Tiap panggilan menunggu respons sebelumnya. Hook menunggu sampai menit berganti (maksimum 60 detik; konvensi bagian 6) setelah entri inti (3) dan sebelum entri inti (4), sehingga entri (1) sampai (3) dan entri (4) sampai (7) berada di menit berbeda; asersi urutan Date dibatasi pada pasangan entri beda menit, urutan antar entri se-menit tidak diasersi. Employee ID numerik diturunkan dari `{runId}` (hanya digit timestamp) dan memuat nomor spec (S-12): `{runId}0811` dan `{runId}0812`):
  - Inti (7 entri, berurutan): (1) Create `Alfa {runId}-081 Inti` oleh Siti Nurhaliza dengan Employee ID `{runId}0811`; (2) Create `Beta {runId}-081 Inti` oleh Fajar Nugroho; (3) Create `Gamma {runId}-081 Inti` oleh Siti Nurhaliza; (4) Edit Position `Alfa` dari `Staff` menjadi `Supervisor` oleh Siti Nurhaliza; (5) Edit Employee ID `Alfa` dari `{runId}0811` menjadi `{runId}0812` oleh Siti Nurhaliza; (6) Deactivate `Beta` oleh Siti Nurhaliza; (7) Delete `Gamma` oleh Siti Nurhaliza.
  - Nilai pada tujuh entri inti: Action `Create` (3), `Edit` (2), `Deactivate`, `Delete`; User Name `Alfa`, `Beta`, `Gamma` (3, 2, 2 entri); Field `Name` (4), `Position`, `Employee ID`, `Status (Global)`; Old Value `—` (3, entri Create), `Staff`, `{runId}0811`, `Active`, `Gamma {runId}-081 Inti`; New Value `Alfa {runId}-081 Inti`, `Beta {runId}-081 Inti`, `Gamma {runId}-081 Inti`, `Supervisor`, `{runId}0812`, `Inactive`, `—` (entri Delete); Modified By `Siti N` (6) dan `Fajar N` (1). Search `{runId}-081 Inti` hanya mengembalikan tujuh entri ini.
  - Pembantu (20 entri): Create `Halaman 01 {runId}-081` sampai `Halaman 20 {runId}-081` oleh Siti Nurhaliza, dibuat sesudah entri inti. Bersama entri inti, Search `{runId}-081` mengembalikan 27 entri (lebih dari 25) untuk TC-GS-USER-508 (precondition data uji dua puluh satu baris atau lebih) dan TC-GS-USER-509; pada TC-GS-USER-509 Filter Action `Create` menyisakan 23 entri (3 inti dan 20 pembantu), lebih dari 10 dan kurang dari 25.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Alfa`, `Beta`, dan 20 user pembantu bila masih ada; kembalikan sesi ke akun default suite. Entri Changelog tidak bisa dihapus.
- Kemampuan teknis: klik header kolom sort; ubah page size; ketik nomor halaman pada input Pagination; membaca urutan nilai kolom pada baris yang tampil.
- Precondition TC-GS-USER-491 sampai 493, 508, 509: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User); riwayat Changelog terisi.
- Suite serial (`parallel: false`). Changelog bersifat append-only dan dipakai bersama spec lain: asersi memakai pola baris (nilai bersuffix `{runId}-081`), bukan jumlah baris total, kecuali dinyatakan lain. Spec ini tidak mengubah atau menghapus data Pre-setup (S-06).
- State global yang diubah: tidak ada (Sort dan Pagination hanya state tampilan modal).

## Test Steps

### TC-GS-USER-491: Sort 3-state kolom Date
1. Klik icon Changelog di Table Tools
2. Klik icon Search, ketik `{runId}-081 Inti`, tekan Enter
3. Verifikasi tabel memuat tujuh baris entri inti
4. Klik header Date
5. Verifikasi Date Oldest First: baris Create `Alfa` di atas baris Edit `Alfa` (Field Position), baris Create `Beta` di atas baris Deactivate `Beta`, dan baris Create `Gamma` di atas baris Delete `Gamma` (pasangan entri beda menit)
6. Klik header Date
7. Verifikasi Date Newest First: baris Edit `Alfa` (Field Position) di atas baris Create `Alfa`, baris Deactivate `Beta` di atas baris Create `Beta`, dan baris Delete `Gamma` di atas baris Create `Gamma` (pasangan entri beda menit)
8. Klik header Date
9. Verifikasi Date kembali ke default sort tabel: baris Delete `Gamma {runId}-081 Inti` di atas baris Create `Alfa {runId}-081 Inti` (Newest First)
### TC-GS-USER-492: Sort 3-state kolom kelas teks
10. Klik header Action
11. Verifikasi Action ascending: urutan `Create`, `Create`, `Create`, `Deactivate`, `Delete`, `Edit`, `Edit`
12. Klik header Action
13. Verifikasi Action descending: urutan `Edit`, `Edit`, `Delete`, `Deactivate`, `Create`, `Create`, `Create`
14. Klik header Action
15. Verifikasi Action kembali ke default sort tabel: baris Delete `Gamma {runId}-081 Inti` di atas baris Create `Alfa {runId}-081 Inti` (Newest First)
16. Klik header User Name
17. Verifikasi User Name ascending: urutan `Alfa` (3 baris), `Beta` (2 baris), `Gamma` (2 baris)
18. Klik header User Name
19. Verifikasi User Name descending: urutan `Gamma` (2 baris), `Beta` (2 baris), `Alfa` (3 baris)
20. Klik header User Name
21. Verifikasi User Name kembali ke default sort tabel: baris Delete `Gamma {runId}-081 Inti` di atas baris Create `Alfa {runId}-081 Inti` (Newest First)
22. Klik header Field
23. Verifikasi Field ascending: urutan `Employee ID`, `Name` (4 baris), `Position`, `Status (Global)`
24. Klik header Field
25. Verifikasi Field descending: urutan `Status (Global)`, `Position`, `Name` (4 baris), `Employee ID`
26. Klik header Field
27. Verifikasi Field kembali ke default sort tabel: baris Delete `Gamma {runId}-081 Inti` di atas baris Create `Alfa {runId}-081 Inti` (Newest First)
28. Klik header Modified By
29. Verifikasi Modified By ascending: urutan `Fajar N`, lalu `Siti N` (6 baris)
30. Klik header Modified By
31. Verifikasi Modified By descending: urutan `Siti N` (6 baris), lalu `Fajar N`
32. Klik header Modified By
33. Verifikasi Modified By kembali ke default sort tabel: baris Delete `Gamma {runId}-081 Inti` di atas baris Create `Alfa {runId}-081 Inti` (Newest First)
### TC-GS-USER-493: Sort 3-state kolom nilai campuran
34. Klik header Old Value
35. Verifikasi Old Value ascending: numerik lebih dulu, lalu teks A-Z, kosong di akhir (urutan `{runId}0811`, `Active`, `Gamma {runId}-081 Inti`, `Staff`, lalu `—` tiga baris)
36. Klik header Old Value
37. Verifikasi Old Value descending: kebalikan klik 1 (urutan `—` tiga baris, lalu `Staff`, `Gamma {runId}-081 Inti`, `Active`, `{runId}0811`)
38. Klik header Old Value
39. Verifikasi Old Value kembali ke default sort tabel: baris Delete `Gamma {runId}-081 Inti` di atas baris Create `Alfa {runId}-081 Inti` (Newest First)
40. Klik header New Value
41. Verifikasi New Value ascending: numerik lebih dulu, lalu teks A-Z, kosong di akhir (urutan `{runId}0812`, `Alfa {runId}-081 Inti`, `Beta {runId}-081 Inti`, `Gamma {runId}-081 Inti`, `Inactive`, `Supervisor`, lalu `—`)
42. Klik header New Value
43. Verifikasi New Value descending: kebalikan klik 1 (urutan `—`, `Supervisor`, `Inactive`, `Gamma {runId}-081 Inti`, `Beta {runId}-081 Inti`, `Alfa {runId}-081 Inti`, `{runId}0812`)
44. Klik header New Value
45. Verifikasi New Value kembali ke default sort tabel: baris Delete `Gamma {runId}-081 Inti` di atas baris Create `Alfa {runId}-081 Inti` (Newest First)
### TC-GS-USER-508: Pagination ubah page size dan input nomor halaman
46. Klik `[✕]` untuk menutup Modal Changelog
47. Klik icon Changelog di Table Tools
48. Klik icon Search, ketik `{runId}-081`, tekan Enter
49. Verifikasi halaman 1 memuat 10 baris (page size default)
50. Ubah page size ke 25
51. Verifikasi page size 25: halaman 1 memuat 25 baris (maksimal 25 baris)
52. Ubah page size kembali ke 10
53. Ketik nomor halaman `2` pada input nomor halaman, tekan Enter
54. Verifikasi input 2 + Enter: langsung berada di halaman 2
55. Klik next
56. Verifikasi next berpindah ke halaman 3
57. Klik prev
58. Verifikasi prev berpindah kembali ke halaman 2
### TC-GS-USER-509: Kombinasi Search, Filter, Sort, dan Pagination
59. Klik `[✕]` untuk menutup Modal Changelog
60. Klik icon Changelog di Table Tools
61. Klik icon Search, ketik `{runId}-081`, tekan Enter
62. Klik icon Filter, pilih opsi `Create` pada Action, klik `[Apply]`
63. Klik header User Name
64. Ubah page size ke 25
65. Verifikasi Search tetap berlaku (input Search berisi `{runId}-081`)
66. Verifikasi sedikitnya satu baris tampil di tabel
67. Verifikasi Filter tetap berlaku (semua baris tampil bernilai Action `Create`)
68. Verifikasi Sort tetap berlaku (User Name ascending, baris pertama `Alfa {runId}-081 Inti`)
69. Verifikasi Pagination berlaku (halaman 1 memuat lebih dari 10 baris dan paling banyak 25 baris)

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec mengikuti TC sumber (491, 492, 493, 508, 509). Pagination (508) dan kombinasi (509) sesudah ketiga TC Sort karena memakai Search yang lebih luas (`{runId}-081`) dan mengubah page size; tiap TC 508 dan 509 membuka modal baru supaya state TC sebelumnya tidak terbawa (S-09).
- Langkah penghubung (aksi tanpa `Verifikasi`, S-03 dan S-09): `Klik icon Search, ketik {runId}-081 Inti` pada TC-GS-USER-491 (membatasi baris yang diamati pada tujuh entri inti sehingga urutan tiap kolom diasersi tepat, S-11; Search tetap aktif sampai TC-GS-USER-493 selesai), serta `Klik [✕]` lalu `Klik icon Changelog` di awal TC-GS-USER-508 dan 509. `Verifikasi` tabel memuat tujuh baris pada TC-GS-USER-491 dan halaman 1 memuat 10 baris pada TC-GS-USER-508 adalah pembanding (S-03).
- Asersi urutan memakai nilai bersuffix `{runId}-081` dan baris tie (nilai sama) dibaca sebagai nilai yang tampil, bukan urutan antar-baris bernilai sama. Urutan Date dan Newest First diasersi hanya pada pasangan entri beda menit (Prerequisites; konvensi bagian 6): entri inti (1) sampai (3) dan (4) sampai (7) dipisahkan penantian pergantian menit, sehingga urutan antar entri se-menit tidak diasersi. Klik 3 "kembali ke default sort tabel" diasersi lewat pasangan Newest First (baris Delete `Gamma` di atas baris Create `Alfa`, beda menit) yang berbeda dari urutan klik 1 dan 2 untuk kolom selain Date.
- `Verifikasi sedikitnya satu baris tampil di tabel` sebelum asersi Filter pada TC-GS-USER-509 adalah pembanding sebelum asersi universal (S-03, bagian 8b butir 2).
- Urutan descending Old Value dan New Value mengikuti prd-conventions.md §9.7 (descending = kebalikan penuh; nilai kosong di awal pada descending).
- Pembagian TC Modal Changelog User: screening dan Search ada di spec 078, Filter Panel ada di spec 079, kombinasi Search+Filter ada di spec 080, Setup Column ada di spec 082, Download ada di spec 083.
- Spec melewati sekitar 35 langkah (69 langkah) karena TC-GS-USER-492 dan 493 menguji enam kolom dengan tiga klik dan tiga `Verifikasi` per kolom (S-01); semua blok satu layar (Sort dan Pagination Modal Changelog User), satu akun aktor, dan satu dataset seed, serta tiap kolom mengembalikan sort ke default pada klik ketiga sehingga kolom berikutnya mulai dari default.
- Temuan untuk QA: (1) TC-GS-USER-492 c mengharapkan nilai kosong Field di akhir pada A-Z dan tetap di akhir pada Z-A; PRD user.md §8.2 menyatakan Create dan Delete selalu Field `Name` sehingga tidak ada entri Field kosong, dan prd-conventions.md §9.7 menempatkan nilai kosong di awal pada descending. Klausa "nilai kosong di akhir" tidak dapat diseed dan tidak diasersi; selisih descending untuk QA dan pemilik PRD. (2) TC-GS-USER-493 menyebut "klik 2 kebalikannya" tanpa posisi nilai kosong; spec memakai §9.7 (kosong di awal pada descending). (3) TC-GS-USER-493 membutuhkan nilai numerik pada Old Value dan New Value; spec memakai Employee ID numerik (`{runId}0811` dan `{runId}0812`). Nama Field `Employee ID` pada Changelog dan penerimaan Employee ID berisi angka saja tidak disebut di TC, PRD, atau LLD; ketersediaannya disediakan tim FE/BE. (4) TC-GS-USER-491 sampai 493: klik 3 kembali ke default Newest First menghasilkan urutan baris yang sama dengan klik 2 untuk kolom Date; TC tidak menyebut cara membedakannya selain urutan. (5) TC-GS-USER-508 "ketik nomor halaman 2" dan "next lalu prev" mensyaratkan tabel berisi 25 baris (Data Uji: fixture BE, Pre-setup No. 29); spec memakai 27 entri seed milik spec dan mengasersi 25 baris pada page size 25 (TC hanya menyebut maksimal 25). (6) TC-GS-USER-509 langkah 3 menyebut filter pada Action (1 opsi) tanpa nilai; spec memakai `Create`.
