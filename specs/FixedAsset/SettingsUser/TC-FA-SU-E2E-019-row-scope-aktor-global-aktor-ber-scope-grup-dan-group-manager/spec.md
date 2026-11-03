---
id: TC-FA-SU-E2E-019-row-scope-aktor-global-aktor-ber-scope-grup-dan-group-manager
title: "Row Scope Aktor Global, Aktor Ber-scope Grup, dan Group Manager"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-58
  - TC-FA-SU-59
  - TC-FA-SU-60
  - TC-FA-SU-69
coverage:
  web: automated
---

# Row Scope Aktor Global, Aktor Ber-scope Grup, dan Group Manager

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Lina Marlina, Pre-setup #1, akun default suite); halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke Total Control. Hook suite (login default, `beforeEach`, `after`, sesi API aktor, Principal Automation, password lewat env) dirujuk dari `suite.md` dan tidak diulang di sini.
- Role yang diuji (satu blok per aktor karena ganti akun menuntut Step eksplisit):

| Aktor | Pre-setup | Nama | Email | Env password |
|---|---|---|---|---|
| Total Control | #1 | Lina Marlina | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| Manage global user & role (Update) | #4 | Qori Akbar | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_MURG_UPD_PASSWORD` |
| Manage user & role Group (Update) | #6 | Sinta Dewi | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_MURGR_UPD_PASSWORD` |
| Group Manager (IT Infrastructure dan Accounts Payable) | #9 | Oscar Pranata | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_GM_PASSWORD` |
| Manage user & role Group (Update pada Finance & Accounting, Read pada Branch Surabaya) | #8 | Umar Faruq | Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA) | `Spectra.env.FA_MURGPART_PASSWORD` |

- Nama env `FA_MURG_UPD_PASSWORD`, `FA_MURGR_UPD_PASSWORD`, `FA_GM_PASSWORD`, dan `FA_MURGPART_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; satu nama satu arti. Password tidak ditulis di spec atau fixture.
- Data Pre-setup (hanya dibaca): Client `FaUserMain` dengan 25 pengguna (#20; halaman 1: 10, halaman 2: 10, halaman 3: 5), pohon grup (#21), tier dan penugasan (#23). Scope Finance & Accounting (aktor Sinta Dewi): 12 pengguna yaitu Ahmad Dahlan, Budi Santoso, Citra Lestari, Gita Permata, Lina Marlina, Nanda Pratama, Oscar Pranata, Putri Anggraeni, Sinta Dewi, Teguh Prakoso, Umar Faruq, dan Wawan Setiawan. Scope IT Infrastructure (aktor Oscar Pranata): 8 pengguna yaitu Ahmad Dahlan, Citra Lestari, Indra Wijaya, Lina Marlina, Oscar Pranata, Putri Anggraeni, Qori Akbar, dan Wawan Setiawan.
- Tabel "Pengguna di luar scope Sinta Dewi" (langkah 21 sampai 23): Indra Wijaya, Eka Wulandari, Rudi Hartono, Rina Susanti, Qori Akbar, Doni Prasetyo.
- Tabel "Pengguna di luar scope Oscar Pranata" (langkah 32 sampai 34): Eka Wulandari, Budi Santoso.
- Data Dinamis: tidak ada.
- Kemampuan teknis: login dan logout bergantian antar akun pada satu sesi browser; hover elemen; Download CSV dengan pembacaan isi berkas (nilai sel) disediakan tim FE.
- State global: tidak ada yang diubah; data Pre-setup tidak diubah.

## Test Steps

### TC-FA-SU-58: Row scope Manage global user & role dan Total Control, seluruh pengguna organisasi

1. Verifikasi halaman 1 User List berisi 10 baris
2. Klik halaman 2 pada Pagination
3. Verifikasi halaman 2 berisi 10 baris
4. Klik halaman 3 pada Pagination
5. Verifikasi halaman 3 berisi 5 baris, sehingga daftar memuat seluruh 25 pengguna organisasi tanpa batasan grup
6. Ketik Search `Rudi Hartono`, tekan Enter
7. Verifikasi baris Rudi Hartono (hanya Global Role) tampil
8. Ganti isi kotak search dengan `Doni Prasetyo`, tekan Enter
9. Verifikasi baris Doni Prasetyo (tanpa grup) tampil
10. Klik `(←)` pada kotak Search
11. Ganti akun: logout lalu login sebagai Manage global user & role (Update) (Qori Akbar)
12. Buka Settings > User dari sidebar

Ulangi langkah 1 sampai 10 untuk Manage global user & role (Update) (Qori Akbar).

### TC-FA-SU-59: Row scope Manage user & role Group, grup tumpang tindih termasuk turunan

13. Ganti akun: logout lalu login sebagai Manage user & role Group (Update) (Sinta Dewi)
14. Buka Settings > User dari sidebar
15. Verifikasi halaman 1 User List berisi 10 baris yang seluruhnya termasuk 12 nama scope Finance & Accounting
16. Klik halaman 2 pada Pagination
17. Verifikasi halaman 2 berisi 2 baris sisanya sehingga halaman 1 dan 2 memuat tepat 12 nama scope Finance & Accounting
18. Ketik Search `Putri Anggraeni`, tekan Enter
19. Verifikasi baris Putri Anggraeni (Group Role pada Accounts Payable, turunan Finance & Accounting) tampil
20. Klik `(←)` pada kotak Search

Untuk setiap nama pada tabel "Pengguna di luar scope Sinta Dewi", jalankan langkah 21 sampai 23.

21. Ketik Search nama pengguna pada baris tabel, tekan Enter
22. Verifikasi empty state `No results found`
23. Klik `(←)` pada kotak Search
24. Klik icon Download
25. Pilih format CSV
26. Verifikasi berkas CSV terunduh
27. Verifikasi isi berkas CSV memuat baris Budi Santoso
28. Verifikasi isi berkas CSV tidak memuat Indra Wijaya, Eka Wulandari, Rudi Hartono, Rina Susanti, Qori Akbar, dan Doni Prasetyo

### TC-FA-SU-60: Row scope Group Manager, pengguna Group Role atau Group Manager pada grup aktor

29. Ganti akun: logout lalu login sebagai Group Manager (Oscar Pranata)
30. Buka Settings > User dari sidebar
31. Verifikasi tabel User List memuat tepat 8 pengguna scope IT Infrastructure (Ahmad Dahlan, Citra Lestari, Indra Wijaya, Lina Marlina, Oscar Pranata, Putri Anggraeni, Qori Akbar, Wawan Setiawan) pada satu halaman

Untuk setiap nama pada tabel "Pengguna di luar scope Oscar Pranata", jalankan langkah 32 sampai 34.

32. Ketik Search nama pengguna pada baris tabel, tekan Enter
33. Verifikasi empty state `No results found`
34. Klik `(←)` pada kotak Search

### TC-FA-SU-69: Manage user & role Group dengan Update hanya pada sebagian grup, union per grup

35. Ganti akun: logout lalu login sebagai Manage user & role Group (Update pada Finance & Accounting, Read pada Branch Surabaya) (Umar Faruq)
36. Buka Settings > User dari sidebar
37. Ketik Search `Budi Santoso`, tekan Enter
38. Verifikasi sakelar Active baris Budi Santoso Enabled
39. Buka Detail Budi Santoso lalu Tab Role (Sub-tab Group Role)
40. Verifikasi `[Assign Group]` Enabled
41. Buka Sub-tab Transaction Role
42. Verifikasi `[+ Assign]` dan `Remove` Enabled
43. Buka Settings > User dari sidebar
44. Ketik Search `Eka Wulandari`, tekan Enter
45. Hover sakelar Active baris Eka Wulandari
46. Verifikasi sakelar Active Disabled dengan tooltip `You don't have permission to edit.`
47. Verifikasi Table Tools User List tampil
48. Buka row action menu `⋯` baris Eka Wulandari
49. Verifikasi row action `Resend Activation Email` dan `Resend Confirmation Email` Hidden
50. Tutup row action menu dengan menekan Esc
51. Buka Detail Eka Wulandari lalu Tab Role (Sub-tab Group Role)
52. Verifikasi baris Group Role Eka Wulandari pada Branch Surabaya tampil
53. Verifikasi `[Assign Group]` Hidden
54. Buka Sub-tab Transaction Role
55. Verifikasi Sub-tab Transaction Role tampil
56. Verifikasi `[+ Assign]` dan `Remove` Hidden

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Role Matrix (bagian 3a) ditulis per blok role: langkah tiap aktor berbeda dan ganti akun menuntut Step eksplisit (akun pertama login di hook `before`). Judul tanpa kata Positif atau Negatif.
- Spec melewati sekitar 35 langkah (56 langkah nominal, 84 langkah dengan ekspansi). Alasan: seluruh blok satu kelas (fungsional, hanya membaca data scope), keempat TC berdiri sendiri (kegagalan satu blok tidak membuat blok lain kehilangan makna), dan tiap blok menuntut ganti akun eksplisit. Langkah yang diulang: langkah 1 sampai 10 diulang untuk Qori Akbar (+10), langkah 21 sampai 23 untuk enam nama (+15), langkah 32 sampai 34 untuk dua nama (+3); parameter ada di tabel `## Prerequisites`.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): Search untuk menemukan baris atau memeriksa nama pada langkah 6, 8, 10, 18, 20, 21, 23, 32, 34, 37, 44 (R-16); menutup row action menu pada langkah 50; membuka ulang Settings > User pada langkah 43.
- Empty state `No results found` pada langkah 22 dan 33 adalah anchor positif yang sah untuk absence hasil Search (bagian 8b butir 2). Langkah 47 adalah anchor permukaan untuk asersi Hidden langkah 49; langkah 52 adalah anchor positif untuk Hidden langkah 53; langkah 55 untuk langkah 56.
- Langkah 26 sampai 28 (Download CSV, TC-FA-SU-59 langkah 4): kemampuan membaca isi berkas disediakan tim FE; langkah 27 adalah anchor positif untuk asersi absence langkah 28.
- Temuan untuk QA:
  - TC-FA-SU-58: Data Uji menyebut aktor Total Control dan Manage global user & role (Update), tetapi precondition hanya Manage global user & role; spec menjalankan keduanya (Total Control di hook `before`, Qori Akbar sesudah ganti akun).
  - TC-FA-SU-59 Expected b menyebut "tabel, filter, maupun hasil Download", tetapi langkah TC hanya Search dan Download; asersi filter tidak ditulis karena tidak ada langkah dan tidak ada nama filter yang disebut. Data Uji memuat empat pengguna di luar scope, sedangkan Expected b menyebut enam (menambah Rina Susanti dan Qori Akbar); spec memakai enam.
  - TC-FA-SU-59 tidak menyebut format Download dan teks menu pilihan format; spec memakai CSV sesuai langkah TC dan mengasumsikan pilihan `CSV` pada menu Download.
  - TC-FA-SU-60: judul menyebut "grup aktor dan ancestor", tetapi Expected tidak menyebut ancestor; tidak diasersi. Expected a memuat nama-nama pengguna dengan "serta pengguna tier" tanpa menyebut nama; spec memakai Ahmad Dahlan, Citra Lestari, dan Lina Marlina (Pre-setup #23).
  - TC-FA-SU-69 Expected b menyebut "aksi tulis paksa ditolak server dengan toast" tanpa langkah, endpoint, atau kode status; perilaku FE atas permintaan langsung tidak diasersi (bagian 8b butir 1) dan endpoint tidak dikarang. TC-FA-SU-69 Expected c ("Dimensi Create dan Delete aktor tidak memengaruhi aksi modul ini") tidak punya langkah observasi sehingga tidak diasersi. TC-FA-SU-69 Expected b tidak menyebut status Eka Wulandari; asersi Hidden Resend pada baris Eka Wulandari yang berstatus aktif tidak membuktikan Resend tersembunyi karena aturan scope (Resend memang tidak tampil untuk status aktif); QA perlu menambah target Pending pada Branch Surabaya.
  - TC-FA-SU-69 Expected a menyebut "kontrol tulis" tanpa daftar; spec mengasersi sakelar Active, `[Assign Group]`, `[+ Assign]`, dan `Remove`.
  - Email akun #4, #6, #8, dan #9 tidak tertulis di Pre-setup TC; password tidak diberi nama env di TC.
