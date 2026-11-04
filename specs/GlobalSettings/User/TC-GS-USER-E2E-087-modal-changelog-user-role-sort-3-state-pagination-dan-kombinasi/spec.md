---
id: TC-GS-USER-E2E-087-modal-changelog-user-role-sort-3-state-pagination-dan-kombinasi
title: "Modal Changelog Role: Sort 3-state, Pagination, dan kombinasi Search+Filter+Sort+Pagination"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-USER-532
  - TC-GS-USER-533
  - TC-GS-USER-534
  - TC-GS-USER-549
  - TC-GS-USER-550
coverage:
  web: automated
---

# Modal Changelog Role: Sort 3-state, Pagination, dan kombinasi Search+Filter+Sort+Pagination

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Akun aktor: Total Control Siti Nurhaliza (`Siti N`), `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 2), akun default suite. Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > User List (sub-tab Login User).
- Pelaku seeding lewat sesi API (tidak login UI): Manage user and role (Full CRUD) Fajar Nugroho (`Fajar N`), `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup baris 4), `Spectra.env.GS_FULLCRUD_PASSWORD`. Fajar menjadi nilai Modified By kedua selain `Siti N`.
- Environment variable: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup: tidak dipakai. TC menyebut `Ahmad Fauzi` (Tabel Data Uji Pre-setup baris 13); aksi tulis Role memakai user seed milik spec (S-06), jadi Pre-setup tidak diubah.
- Data Dinamis: user seed `Ahmad Fauzi {runId}-087`, email `ahmadfauzi+{runId}-087@qwertysystem.net`, Access `Global Settings`, bukan tier, field wajib lain diisi seadanya oleh seeding.
- Seeding minimal (S-11; lewat API di hook `before`, urutan sebagai berikut; setara TC-GS-USER-902, 903, 904, 1052). TC-GS-USER-549 mensyaratkan sedikitnya 21 baris; seeding membuat 26 entri agar page size 25 terisi penuh dan halaman 3 pada page size 10 ada. Hook menunggu sampai menit berganti (maksimum 60 detik; konvensi bagian 6) setelah entri 6 dan sebelum entri 7, sehingga entri 1 sampai 6 dan entri 7 sampai 26 berada di menit berbeda; asersi urutan Date dibatasi pada pasangan entri beda menit, urutan antar entri se-menit tidak diasersi:
  - 1. Siti N: Assign `Manage TAG` -> `Assign | Manage TAG | Access | — | Assigned | Siti N`.
  - 2. Siti N: centang Update `Manage TAG` -> `Edit | Manage TAG | Update | Inactive | Active | Siti N`.
  - 3. Fajar N: Assign `Manage files` -> `Assign | Manage files | Access | — | Assigned | Fajar N`.
  - 4. Siti N: Remove `Manage files` -> `Remove | Manage files | Access | Assigned | — | Siti N`.
  - 5. Siti N: centang Read `Manage hardware` -> `Assign | Manage hardware | Access | — | Assigned | Siti N`.
  - 6. Fajar N: centang Update `Manage hardware` -> `Edit | Manage hardware | Update | Inactive | Active | Fajar N`.
  - 7 sampai 25. Siti N: 19 kali mengubah centang bergantian Create, Update, dan Delete pada `Manage TAG` (tiap perubahan satu baris `Edit | Manage TAG | <Create/Update/Delete> | Inactive/Active | Active/Inactive | Siti N`).
  - 26. Siti N: Remove `Manage hardware` -> `Remove | Manage hardware | Access | Assigned | — | Siti N` (entri terbaru, baris unik).
  - Nilai distinct (S-11): Action 3 (`Assign`, `Edit`, `Remove`), Role 3 (`Manage TAG`, `Manage files`, `Manage hardware`), Field 4 (`Access`, `Create`, `Delete`, `Update`), Old Value 4 (`—`, `Inactive`, `Active`, `Assigned`), New Value 4 (`Assigned`, `Active`, `Inactive`, `—`), Modified By 2 (`Siti N`, `Fajar N`).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus user seed lewat API. Entri Changelog tidak bisa dihapus.
- Kemampuan teknis: klik header kolom sort; membaca arah sort dan urutan baris; mengubah page size dan mengetik nomor halaman di input pagination; membaca state icon Filter.
- Precondition TC-GS-USER-532, 533, 534, 549, 550: login sebagai Total Control dan berada di Global Settings > User > User List (sub-tab Login User); data pre-setup User tersedia; riwayat Changelog Role user seed terisi (26 entri).
- Suite serial (`parallel: false`), lihat `suite.md`.
- State global yang dipulihkan: tidak ada (sort, filter, dan page size hanya state tampilan modal).

## Test Steps

### TC-GS-USER-532: Sort 3-state kolom kelas tanggal

1. Ketik Search `Ahmad Fauzi {runId}-087`, tekan Enter
2. Klik Name `Ahmad Fauzi {runId}-087` di User List
3. Klik Tab `Role`
4. Klik icon Changelog di toolbar Tab Role
5. Ubah page size ke 100
6. Klik header Date
7. Verifikasi Date Oldest First: baris `Assign | Manage TAG | Access | — | Assigned | Siti N` (entri 1) di atas baris `Remove | Manage hardware | Access | Assigned | — | Siti N` (entri 26), pasangan entri beda menit
8. Klik header Date
9. Verifikasi Date Newest First: baris `Remove | Manage hardware | Access | Assigned | — | Siti N` (entri 26) di atas baris `Assign | Manage TAG | Access | — | Assigned | Siti N` (entri 1), pasangan entri beda menit
10. Klik header Date
11. Verifikasi kembali ke default sort tabel (Date terbaru di atas)

### TC-GS-USER-533: Sort 3-state kolom kelas teks A-Z

12. Klik header Action
13. Verifikasi Action A-Z (baris pertama Action `Assign`, baris terakhir Action `Remove`)
14. Klik header Action
15. Verifikasi Action Z-A (baris pertama Action `Remove`, baris terakhir Action `Assign`)
16. Klik header Action
17. Verifikasi Action kembali ke default sort tabel (Date terbaru di atas)
18. Klik header Role
19. Verifikasi Role A-Z case-insensitive (baris pertama Role `Manage files`, baris terakhir Role `Manage TAG`)
20. Klik header Role
21. Verifikasi Role Z-A case-insensitive (baris pertama Role `Manage TAG`, baris terakhir Role `Manage files`)
22. Klik header Role
23. Verifikasi Role kembali ke default sort tabel (Date terbaru di atas)
24. Klik header Field
25. Verifikasi Field A-Z (baris pertama Field `Access`, baris terakhir Field `Update`)
26. Klik header Field
27. Verifikasi Field Z-A (baris pertama Field `Update`, baris terakhir Field `Access`)
28. Klik header Field
29. Verifikasi Field kembali ke default sort tabel (Date terbaru di atas)
30. Klik header Modified By
31. Verifikasi Modified By A-Z (baris pertama Modified By `Fajar N`, baris terakhir Modified By `Siti N`)
32. Klik header Modified By
33. Verifikasi Modified By Z-A (baris pertama Modified By `Siti N`, baris terakhir Modified By `Fajar N`)
34. Klik header Modified By
35. Verifikasi Modified By kembali ke default sort tabel (Date terbaru di atas)

### TC-GS-USER-534: Sort 3-state kolom kelas nilai campuran

36. Klik header Old Value
37. Verifikasi Old Value klik 1: nilai teks A-Z dengan kosong di akhir (baris pertama Old Value `Active`, baris terakhir Old Value `—`)
38. Klik header Old Value
39. Verifikasi Old Value klik 2: kebalikan klik 1 (baris pertama Old Value `—`, baris terakhir Old Value `Active`)
40. Klik header Old Value
41. Verifikasi Old Value klik 3: kembali ke default sort tabel (Date terbaru di atas)
42. Klik header New Value
43. Verifikasi New Value klik 1: nilai teks A-Z dengan kosong di akhir (baris pertama New Value `Active`, baris terakhir New Value `—`)
44. Klik header New Value
45. Verifikasi New Value klik 2: kebalikan klik 1 (baris pertama New Value `—`, baris terakhir New Value `Active`)
46. Klik header New Value
47. Verifikasi New Value klik 3: kembali ke default sort tabel (Date terbaru di atas)

### TC-GS-USER-549: Pagination ubah page size dan input nomor halaman

48. Ubah page size ke 25
49. Verifikasi tabel menampilkan 25 baris
50. Ubah page size kembali ke 10
51. Ketik nomor halaman `2` di input pagination, tekan Enter
52. Verifikasi tampil halaman 2
53. Klik tombol next
54. Verifikasi tampil halaman 3
55. Klik tombol prev
56. Verifikasi tampil halaman 2

### TC-GS-USER-550: Kombinasi Search, Filter, Sort, dan Pagination

57. Klik icon Search, ketik `edit`, tekan Enter
58. Klik icon Filter, pilih opsi Modified By `Siti N`, klik `[Apply]`
59. Klik header Date
60. Verifikasi halaman 1 menampilkan 10 baris
61. Ubah page size ke 25
62. Verifikasi Search berlaku (isi Search tetap `edit`, semua baris Action `Edit`)
63. Verifikasi Filter berlaku (semua baris Modified By `Siti N`)
64. Verifikasi Sort berlaku (Date Oldest First, baris pertama `Edit | Manage TAG | Update | Inactive | Active | Siti N`)
65. Verifikasi page size 25 berlaku (halaman 1 menampilkan lebih dari 10 baris)

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Modal Changelog Role dibuka sekali di langkah 2 sampai 4 untuk semua TC.
- Urutan TC dalam spec mengikuti TC sumber (532, 533, 534, 549, 550). Penyimpangan dari tabel slice tidak ada.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1 (Search nama baris persis sebelum Klik Name, karena User List bisa lebih dari satu halaman; akhiran runId saja tidak cukup), langkah 5 (page size 100 agar seluruh 26 baris berada pada satu halaman selama TC-GS-USER-532, 533, dan 534; TC tidak menyebut page size untuk Sort), dan langkah 50 (kembali ke page size 10, tertulis "Kembali 10" di TC-GS-USER-549). Tiap klik ketiga mengembalikan sort ke default, sehingga TC berikutnya mulai dari default.
- "Kembali ke default sort tabel" diasersi sebagai urutan Date terbaru di atas, sama dengan kondisi awal tabel; kondisi awal itu tidak diasersi sendiri di spec ini.
- Asersi baris pertama dan terakhir memakai pola baris dan nilai distinct dari seeding (26 entri milik user seed), jadi entri dari run atau spec lain tidak memengaruhi hasil. Sort Role diasersi case-insensitive (Expected e TC-GS-USER-533): `Manage files` dan `Manage hardware` sebelum `Manage TAG`, sedangkan urutan sensitif huruf besar-kecil menaruh `Manage TAG` lebih dulu.
- Urutan Date (langkah 7 dan 9) dan baris pertama pada TC-GS-USER-550 (langkah 64) hanya memakai pasangan entri beda menit: entri 1 sampai 6 dan entri 7 sampai 26 dipisahkan penantian pergantian menit (Prerequisites); pada langkah 64 hanya entri 2 dari kelompok pertama yang lolos Search `edit` dan Filter `Siti N`, sehingga baris pertama pada Oldest First tidak bergantung pada urutan entri se-menit.
- `Verifikasi halaman 1 menampilkan 10 baris` (langkah 60) adalah pembanding tambahan atas page size default sebelum diubah ke 25 (S-03).
- Spec melewati sekitar 35 langkah (65 langkah) karena TC-GS-USER-533 menguji empat kolom dan TC-GS-USER-534 dua kolom, masing-masing tiga klik dan tiga `Verifikasi` (S-01). Semua blok satu kelas harness (tabel Modal Changelog Role: Sort, Pagination, kombinasi), satu akun, satu dataset, dan tiap blok berdiri sendiri karena sort dikembalikan ke default pada klik ketiga dan modal dibuka sekali.
- TC terbagi lintas spec: Search dan Filter berdiri sendiri ada di spec 084 dan 085; kombinasi Search dan Filter tanpa Sort di spec 086.
- Temuan untuk QA: (1) TC-GS-USER-534 Expected "numerik dulu lalu teks" tidak berlaku untuk data Changelog Role, karena Old Value dan New Value hanya bernilai teks (`Inactive`, `Active`, `Assigned`) atau `—`; spec mengasersi teks A-Z dengan kosong di akhir. (2) TC-GS-USER-534 klik 2 "kebalikannya" tidak menyebut posisi nilai kosong; spec membaca kebalikan klik 1 (kosong di awal). (3) TC-GS-USER-550 "terapkan filter bila tersedia" ambigu; spec selalu menerapkan Filter (Modified By `Siti N`) dan tidak memakai langkah bersyarat. (4) TC-GS-USER-549 menyebut `Volume Test User` dan Data Uji tabel berisi 25 baris (fixture BE, Pre-setup No. 29); spec memakai user seed milik spec dengan 26 entri supaya page size 25 terisi penuh dan halaman 3 ada. (5) TC-GS-USER-532 sampai 550 menyebut `Ahmad Fauzi` tanpa suffix; spec memakai user seed bersuffix. (6) TC-GS-USER-533 klik 3 "kembali ke default sort tabel" tidak menyebut apakah icon sort Date ikut kembali; spec hanya mengasersi urutan baris.
