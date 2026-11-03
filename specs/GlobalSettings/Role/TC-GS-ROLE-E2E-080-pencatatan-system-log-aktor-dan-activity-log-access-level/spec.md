---
id: TC-GS-ROLE-E2E-080-pencatatan-system-log-aktor-dan-activity-log-access-level
title: "Pencatatan System Log Aktor dan Activity Log untuk Assign, Remove, dan Auto-Revert Access Level"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-221
  - TC-GS-ROLE-289
coverage:
  web: automated
---

# Pencatatan System Log Aktor dan Activity Log untuk Assign, Remove, dan Auto-Revert Access Level

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Ahmad Fauzi (Total Control, Modified By `Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar). Akun ini akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Layar awal dibuka di hook `beforeEach`: Global Settings > Role & Permission > Tab Total Control.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup yang dipakai (bernama literal sesuai TC; state awal dipulihkan di hook `after`):

| User | Pre-setup | State awal (Given di hook `before`) | Aksi pemicu di spec ini | TC |
|---|---|---|---|---|
| Sari Wulandari | #11 kandidat (Active) | Tanpa access level dan tanpa baris role | Assign Total Control, lalu Remove Total Control | TC-GS-ROLE-221 |
| Maya Anggraini | #11 kandidat (Inactive) | Di-assign Total Control oleh Ahmad Fauzi lewat sesi API (setara TC-GS-ROLE-59, hanya Maya Anggraini; dipakai sebagai precondition TC, tidak diasersi) | Auto-Revert Total Control lewat Update Manage TAG dikosongkan | TC-GS-ROLE-221 |
| Rahmat Hidayat | #11 kandidat (Active) | Tanpa access level, punya baris Manage files (Read dan Delete checked) | Assign Read Only, lalu Remove Read Only | TC-GS-ROLE-289 |
| Wawan Setiawan | #11 kandidat (Active) | Di-assign Read Only oleh Ahmad Fauzi lewat sesi API (Given TC-GS-ROLE-107 precondition c; dipakai sebagai precondition TC, tidak diasersi) | Auto-Revert Read Only lewat Create Manage hardware dicentang | TC-GS-ROLE-289 |

- Data Dinamis bersuffix tidak ada: entri log dikenali lewat baseline jumlah entri (S-12). User Pre-setup bernama literal, sehingga entri log run sebelumnya tetap ada. Jumlah entri adalah total hasil Filter Name pada Tab System Log Detail Ahmad Fauzi (`S-SW`, `S-MA`, `S-RH`, `S-WS`) dan total hasil Search nama user pada Activity Log (`A-SW`, `A-MA`, `A-RH`, `A-WS`), dicatat pada langkah 1 sampai 17 (sebelum aksi pemicu pertama yang diasersi); asersi "entry baru" memakai selisih terhadap baseline itu. Alasan beda cara: Search Tab System Log Detail User berplaceholder "Search action, field, or value..." (`user.md` §4.1.6 dan wireframe Tab System Log) sehingga tidak diandalkan untuk nama user, sedangkan kolom Name punya Filter Panel multi-select (placeholder "All users"); Activity Log Tab User Action menandai kolom Name `Searchable ✅` (`activity-log.md` §4.1.2), sehingga Search nama user tetap dipakai di sana. Kemampuan membaca total hasil Filter dan Search pada kedua surface disediakan tim FE.
- Kemampuan teknis: aksi pemicu dijalankan lewat sesi API atas nama Ahmad Fauzi (agar Modified By tercatat `Ahmad F`): Assign dan Remove access level, serta Edit CRUD pada baris role beserta konfirmasi `[Remove]` auto-revert. Aksi ini adalah dependensi TC sumber (TC-GS-ROLE-58, 86, 106, 80, 88, 107) yang dijalankan lewat seeding API (S-04). Mekanisme dan endpoint disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD).
- Pemulihan (hook `after`, tidak berasumsi seeding atau aksi berhasil penuh), lewat sesi API Ahmad Fauzi: Sari Wulandari, Maya Anggraini, dan Wawan Setiawan dikembalikan ke tanpa access level dan tanpa baris role; Rahmat Hidayat dikembalikan ke tanpa access level dengan baris Manage files (Read dan Delete checked). Efek pada Pre-setup: Modified By dan Last Updated keempat user berubah; entri log bersifat immutable dan tidak dihapus.
- Format tanggal mengikuti General Settings aktif. Tidak ada manipulasi jam. Date baris Activity Log dibandingkan dengan Date baris System Log aksi yang sama (S-12).
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`) karena spec mengubah access level dan baris role user Pre-setup bersama; tidak ada state global lain yang diubah.

## Test Steps

### Baseline jumlah entri (sebelum aksi pemicu TC-GS-ROLE-221 dan TC-GS-ROLE-289)

1. Buka Global Settings > User > Ahmad Fauzi > Tab System Log
2. Buka Filter Panel dan klik `[Clear Field]`
3. Pilih Name `Sari Wulandari` di Filter Panel
4. Klik `[Apply]`, catat total hasil sebagai `S-SW`
5. Buka Filter Panel dan klik `[Clear Field]`
6. Pilih Name `Maya Anggraini` di Filter Panel
7. Klik `[Apply]`, catat total hasil sebagai `S-MA`
8. Buka Filter Panel dan klik `[Clear Field]`
9. Pilih Name `Rahmat Hidayat` di Filter Panel
10. Klik `[Apply]`, catat total hasil sebagai `S-RH`
11. Buka Filter Panel dan klik `[Clear Field]`
12. Pilih Name `Wawan Setiawan` di Filter Panel
13. Klik `[Apply]`, catat total hasil sebagai `S-WS`
14. Buka Global Settings > Activity Log, ketik Search `Sari Wulandari`, tekan Enter, catat total hasil sebagai `A-SW`
15. Ganti isi kotak search dengan `Maya Anggraini`, tekan Enter, catat total hasil sebagai `A-MA`
16. Ganti isi kotak search dengan `Rahmat Hidayat`, tekan Enter, catat total hasil sebagai `A-RH`
17. Ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter, catat total hasil sebagai `A-WS`

### TC-GS-ROLE-221: System Log aktor dan Activity Log untuk Assign, Remove, dan Auto-Revert Total Control

18. Aksi pemicu (sesi API Ahmad Fauzi): Assign Total Control ke Sari Wulandari (setara TC-GS-ROLE-58 langkah 1 sampai 3)
19. Aksi pemicu (sesi API Ahmad Fauzi): Remove Total Control dari Sari Wulandari (setara TC-GS-ROLE-86 langkah 1 sampai 2)
20. Aksi pemicu (sesi API Ahmad Fauzi): hapus centang Update baris Manage TAG milik Maya Anggraini dan konfirmasi `[Remove]` (setara TC-GS-ROLE-106 langkah 1 sampai 2)
21. Buka Global Settings > User > Ahmad Fauzi > Tab System Log
22. Buka Filter Panel dan klik `[Clear Field]`
23. Pilih Name `Sari Wulandari` di Filter Panel
24. Klik `[Apply]`
25. Verifikasi total hasil Filter sama dengan `S-SW` + 2 (entry Assign dan entry Remove baru)
26. Verifikasi entry terbaru dengan Action `Remove` dan Name `Sari Wulandari` pada System Log: Action `Remove`, Object `Total Control`, Name `Sari Wulandari`, Old Value `Total Control`, New Value `—`; catat Date entry sebagai `D-SW-REMOVE`
27. Verifikasi entry terbaru dengan Action `Assign` dan Name `Sari Wulandari` pada System Log: Action `Assign`, Object `Total Control`, Name `Sari Wulandari`, Field `Access Level`, Old Value `—`, New Value `Total Control`; catat Date entry sebagai `D-SW-ASSIGN`
28. Buka Filter Panel dan klik `[Clear Field]`
29. Pilih Name `Maya Anggraini` di Filter Panel
30. Klik `[Apply]`
31. Verifikasi total hasil Filter sama dengan `S-MA` + 1 (tepat 1 entry baru)
32. Verifikasi entry baru pada System Log (dikenali lewat kombinasi Action, Field, dan Name, bukan posisi baris; selisih +1 pada langkah 31): Action `Auto-Revert`, Object `Total Control`, Name `Maya Anggraini`, Old Value `Total Control`, New Value `—`; catat Date entry sebagai `D-MA`
33. Buka Global Settings > Activity Log, ketik Search `Sari Wulandari`, tekan Enter
34. Verifikasi total hasil Search sama dengan `A-SW` + 2 (baris Assign dan baris Remove baru)
35. Verifikasi baris terbaru dengan Action `Remove` dan Name `Sari Wulandari` pada Activity Log: Action `Remove`, Object `Total Control`, Name `Sari Wulandari`, Old Value `Total Control`, New Value `—`, Modified By `Ahmad F`, Date sama dengan `D-SW-REMOVE`
36. Verifikasi baris terbaru dengan Action `Assign` dan Name `Sari Wulandari` pada Activity Log: Action `Assign`, Object `Total Control`, Name `Sari Wulandari`, Field `Access Level`, Old Value `—`, New Value `Total Control`, Modified By `Ahmad F`, Date sama dengan `D-SW-ASSIGN`
37. Ganti isi kotak search dengan `Maya Anggraini`, tekan Enter
38. Verifikasi total hasil Search sama dengan `A-MA` + 1 (tepat 1 baris baru)
39. Verifikasi baris baru pada Activity Log (dikenali lewat kombinasi Action, Field, dan Name, bukan posisi baris; selisih +1 pada langkah 38): Action `Auto-Revert`, Object `Total Control`, Name `Maya Anggraini`, Old Value `Total Control`, New Value `—`, Modified By `Ahmad F`, Date sama dengan `D-MA`

### TC-GS-ROLE-289: System Log aktor dan Activity Log untuk Assign, Remove, dan Auto-Revert Read Only

40. Aksi pemicu (sesi API Ahmad Fauzi): Assign Read Only ke Rahmat Hidayat (setara TC-GS-ROLE-80 langkah 1 sampai 3)
41. Aksi pemicu (sesi API Ahmad Fauzi): Remove Read Only dari Rahmat Hidayat (setara TC-GS-ROLE-88 langkah 1 sampai 3)
42. Aksi pemicu (sesi API Ahmad Fauzi): centang Create baris Wawan Setiawan di Detail "Manage hardware" dan konfirmasi `[Remove]` (setara TC-GS-ROLE-107 langkah 1 sampai 3)
43. Buka Global Settings > User > Ahmad Fauzi > Tab System Log
44. Buka Filter Panel dan klik `[Clear Field]`
45. Pilih Name `Rahmat Hidayat` di Filter Panel
46. Klik `[Apply]`
47. Verifikasi total hasil Filter sama dengan `S-RH` + 2 (entry Assign dan entry Remove baru)
48. Verifikasi entry terbaru dengan Action `Remove` dan Name `Rahmat Hidayat` pada System Log: Action `Remove`, Object `Read Only`, Name `Rahmat Hidayat`, Field `Access Level`, Old Value `Read Only`, New Value `—`; catat Date entry sebagai `D-RH-REMOVE`
49. Verifikasi entry terbaru dengan Action `Assign` dan Name `Rahmat Hidayat` pada System Log: Action `Assign`, Object `Read Only`, Name `Rahmat Hidayat`, Field `Access Level`, Old Value `—`, New Value `Read Only`; catat Date entry sebagai `D-RH-ASSIGN`
50. Buka Filter Panel dan klik `[Clear Field]`
51. Pilih Name `Wawan Setiawan` di Filter Panel
52. Klik `[Apply]`
53. Verifikasi total hasil Filter sama dengan `S-WS` + 1 (tepat 1 entry baru)
54. Verifikasi entry baru pada System Log (dikenali lewat kombinasi Action, Field, dan Name, bukan posisi baris; selisih +1 pada langkah 53): Action `Auto-Revert`, Object `Read Only`, Name `Wawan Setiawan`, Field `Access Level`, Old Value `Read Only`, New Value `—`; catat Date entry sebagai `D-WS`
55. Buka Global Settings > Activity Log, ketik Search `Rahmat Hidayat`, tekan Enter
56. Verifikasi total hasil Search sama dengan `A-RH` + 2 (baris Assign dan baris Remove baru)
57. Verifikasi baris terbaru dengan Action `Remove` dan Name `Rahmat Hidayat` pada Activity Log: Action `Remove`, Object `Read Only`, Name `Rahmat Hidayat`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Ahmad F`, Date sama dengan `D-RH-REMOVE`
58. Verifikasi baris terbaru dengan Action `Assign` dan Name `Rahmat Hidayat` pada Activity Log: Action `Assign`, Object `Read Only`, Name `Rahmat Hidayat`, Field `Access Level`, Old Value `—`, New Value `Read Only`, Modified By `Ahmad F`, Date sama dengan `D-RH-ASSIGN`
59. Ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter
60. Verifikasi total hasil Search sama dengan `A-WS` + 1 (tepat 1 baris baru)
61. Verifikasi baris baru pada Activity Log (dikenali lewat kombinasi Action, Field, dan Name, bukan posisi baris; selisih +1 pada langkah 60): Action `Auto-Revert`, Object `Read Only`, Name `Wawan Setiawan`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Ahmad F`, Date sama dengan `D-WS`

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 61 langkah nominal. Alasan di atas sekitar 35 langkah: seluruh spec satu kelas (pencatatan System Log aktor dan Activity Log), dan sebagian besar langkah adalah blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) serta baseline, yang tidak dihitung ke ambang (bagian 3 konvensi). Dua TC sumber adalah varian tier yang sama (Total Control dan Read Only) pada surface log yang sama; tiap blok berdiri sendiri dengan baseline sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber (221, 289) dipertahankan. Dependensi TC-GS-ROLE-58, 86, 106, 80, 88, dan 107 dijalankan lewat aksi pemicu sesi API (langkah 18 sampai 20 dan 40 sampai 42); Given Maya Anggraini ber-Total Control (setara TC-GS-ROLE-59) dan Wawan Setiawan ber-Read Only terjadi di hook `before` sebelum baseline dicatat, sehingga entry Assign keduanya tidak termasuk entri baru yang diasersi. Semua aksi pemicu satu TC dijalankan sebelum surface log dibuka, supaya satu pembukaan System Log dan satu pembukaan Activity Log membaca seluruh entri TC itu.
- "Entry baru" pada entri tunggal dikenali lewat kombinasi kolom Action, Field, dan Name serta selisih terhadap baseline (+1), bukan lewat posisi baris. Entri berpasangan yang dibuat berurutan dalam hitungan detik tidak diidentifikasi lewat posisi baris karena kolom Date berketelitian menit (S-12, S-14); tiap entri dikenali lewat kombinasi kolom Action, Field, dan Name pada hasil Filter Name (Tab System Log Detail User) atau Search nama user (Activity Log), tanpa bergantung posisi baris. Pada Tab System Log, Filter Name dipilih sebagai pengganti Search nama karena placeholder Search tab itu tidak mencantumkan kolom Name (`user.md` §4.1.6); tabel kolom di PRD yang sama menandai Name `Searchable ✅`, sehingga ketidakselarasan itu dicatat sebagai temuan dan Filter dipilih karena terdokumentasi tegas. Date baris Activity Log dibandingkan dengan Date baris System Log aksi yang sama (S-12) karena Expected "baris yang sama".
- Langkah penghubung (aksi tanpa `Verifikasi`): berpindah ke System Log atau Activity Log, membuka Filter Panel dan `[Clear Field]`, memilih Name, `[Apply]`, serta mengganti isi kotak search (langkah 1 sampai 17, 21 sampai 24, 28 sampai 30, 33, 37, 43 sampai 46, 50 sampai 52, 55, 59); aksi pemicu API (langkah 18 sampai 20 dan 40 sampai 42). `[Clear Field]` di awal tiap pemakaian Filter Panel menjamin Filter Name sebelumnya tidak terbawa dan tidak mengandalkan persistensi Filter antar pembukaan Detail User; Filter Name terakhir di Tab System Log dibiarkan hingga navigasi berikutnya (hook `beforeEach` suite).
- Temuan untuk QA:
  - TC-GS-ROLE-221 Expected b dan c tidak menyebut kolom Field untuk entry Remove dan Auto-Revert Total Control (Expected a menyebut Field "Access Level" untuk Assign); spec mengikuti TC dan tidak mengasersi Field pada langkah 26, 32, 35, dan 39.
  - TC-GS-ROLE-221 Expected d dan TC-GS-ROLE-289 Expected d ("baris yang sama + Modified By") tidak menyebut Date; spec membandingkan Date dengan baris System Log aksi yang sama, dengan dasar frasa "baris yang sama".
  - TC-GS-ROLE-221 dan TC-GS-ROLE-289 tidak mendefinisikan cara menghitung entri pada System Log dan Activity Log dan memakai user Pre-setup bernama literal yang entrinya menumpuk lintas run; spec memakai total hasil Filter Name (System Log) dan Search nama user (Activity Log) dengan baseline sebagai kemampuan yang disediakan tim FE.
