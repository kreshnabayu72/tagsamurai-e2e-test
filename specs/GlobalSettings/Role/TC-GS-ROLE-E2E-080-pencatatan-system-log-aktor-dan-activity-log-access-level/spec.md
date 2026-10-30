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

- Data Dinamis bersuffix tidak ada: entri log dikenali lewat baseline jumlah entri (S-12). User Pre-setup bernama literal, sehingga entri log run sebelumnya tetap ada. Jumlah entri adalah total hasil Search nama user pada System Log Ahmad Fauzi (`S-SW`, `S-MA`, `S-RH`, `S-WS`) dan pada Activity Log (`A-SW`, `A-MA`, `A-RH`, `A-WS`), dicatat pada langkah 1 sampai 8 (sebelum aksi pemicu pertama yang diasersi); asersi "entry baru" memakai selisih terhadap baseline itu. Kemampuan membaca total hasil Search pada System Log dan Activity Log disediakan tim FE.
- Kemampuan teknis: aksi pemicu dijalankan lewat sesi API atas nama Ahmad Fauzi (agar Modified By tercatat `Ahmad F`): Assign dan Remove access level, serta Edit CRUD pada baris role beserta konfirmasi `[Remove]` auto-revert. Aksi ini adalah dependensi TC sumber (TC-GS-ROLE-58, 86, 106, 80, 88, 107) yang dijalankan lewat seeding API (S-04). Mekanisme dan endpoint disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD).
- Pemulihan (hook `after`, tidak berasumsi seeding atau aksi berhasil penuh), lewat sesi API Ahmad Fauzi: Sari Wulandari, Maya Anggraini, dan Wawan Setiawan dikembalikan ke tanpa access level dan tanpa baris role; Rahmat Hidayat dikembalikan ke tanpa access level dengan baris Manage files (Read dan Delete checked). Efek pada Pre-setup: Modified By dan Last Updated keempat user berubah; entri log bersifat immutable dan tidak dihapus.
- Format tanggal mengikuti General Settings aktif. Tidak ada manipulasi jam. Date baris Activity Log dibandingkan dengan Date baris System Log aksi yang sama (S-12).
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`) karena spec mengubah access level dan baris role user Pre-setup bersama; tidak ada state global lain yang diubah.

## Test Steps

### Baseline jumlah entri (sebelum aksi pemicu TC-GS-ROLE-221 dan TC-GS-ROLE-289)

1. Buka Global Settings > User > Ahmad Fauzi > Tab System Log, ketik Search `Sari Wulandari`, tekan Enter, catat total hasil sebagai `S-SW`
2. Ganti isi kotak search dengan `Maya Anggraini`, tekan Enter, catat total hasil sebagai `S-MA`
3. Ganti isi kotak search dengan `Rahmat Hidayat`, tekan Enter, catat total hasil sebagai `S-RH`
4. Ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter, catat total hasil sebagai `S-WS`
5. Buka Global Settings > Activity Log, ketik Search `Sari Wulandari`, tekan Enter, catat total hasil sebagai `A-SW`
6. Ganti isi kotak search dengan `Maya Anggraini`, tekan Enter, catat total hasil sebagai `A-MA`
7. Ganti isi kotak search dengan `Rahmat Hidayat`, tekan Enter, catat total hasil sebagai `A-RH`
8. Ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter, catat total hasil sebagai `A-WS`

### TC-GS-ROLE-221: System Log aktor dan Activity Log untuk Assign, Remove, dan Auto-Revert Total Control

9. Aksi pemicu (sesi API Ahmad Fauzi): Assign Total Control ke Sari Wulandari (setara TC-GS-ROLE-58 langkah 1 sampai 3)
10. Aksi pemicu (sesi API Ahmad Fauzi): Remove Total Control dari Sari Wulandari (setara TC-GS-ROLE-86 langkah 1 sampai 2)
11. Aksi pemicu (sesi API Ahmad Fauzi): hapus centang Update baris Manage TAG milik Maya Anggraini dan konfirmasi `[Remove]` (setara TC-GS-ROLE-106 langkah 1 sampai 2)
12. Buka Global Settings > User > Ahmad Fauzi > Tab System Log, ketik Search `Sari Wulandari`, tekan Enter
13. Verifikasi total hasil Search sama dengan `S-SW` + 2 (entry Assign dan entry Remove baru)
14. Verifikasi entry Remove (teratas) pada System Log: Action `Remove`, Object `Total Control`, Name `Sari Wulandari`, Old Value `Total Control`, New Value `—`; catat Date entry sebagai `D-SW-REMOVE`
15. Verifikasi entry Assign (kedua) pada System Log: Action `Assign`, Object `Total Control`, Name `Sari Wulandari`, Field `Access Level`, Old Value `—`, New Value `Total Control`; catat Date entry sebagai `D-SW-ASSIGN`
16. Ganti isi kotak search dengan `Maya Anggraini`, tekan Enter
17. Verifikasi total hasil Search sama dengan `S-MA` + 1 (tepat 1 entry baru)
18. Verifikasi entry baru (teratas) pada System Log: Action `Auto-Revert`, Object `Total Control`, Name `Maya Anggraini`, Old Value `Total Control`, New Value `—`; catat Date entry sebagai `D-MA`
19. Buka Global Settings > Activity Log, ketik Search `Sari Wulandari`, tekan Enter
20. Verifikasi total hasil Search sama dengan `A-SW` + 2 (baris Assign dan baris Remove baru)
21. Verifikasi baris Remove (teratas) pada Activity Log: Action `Remove`, Object `Total Control`, Name `Sari Wulandari`, Old Value `Total Control`, New Value `—`, Modified By `Ahmad F`, Date sama dengan `D-SW-REMOVE`
22. Verifikasi baris Assign (kedua) pada Activity Log: Action `Assign`, Object `Total Control`, Name `Sari Wulandari`, Field `Access Level`, Old Value `—`, New Value `Total Control`, Modified By `Ahmad F`, Date sama dengan `D-SW-ASSIGN`
23. Ganti isi kotak search dengan `Maya Anggraini`, tekan Enter
24. Verifikasi total hasil Search sama dengan `A-MA` + 1 (tepat 1 baris baru)
25. Verifikasi baris baru (teratas) pada Activity Log: Action `Auto-Revert`, Object `Total Control`, Name `Maya Anggraini`, Old Value `Total Control`, New Value `—`, Modified By `Ahmad F`, Date sama dengan `D-MA`

### TC-GS-ROLE-289: System Log aktor dan Activity Log untuk Assign, Remove, dan Auto-Revert Read Only

26. Aksi pemicu (sesi API Ahmad Fauzi): Assign Read Only ke Rahmat Hidayat (setara TC-GS-ROLE-80 langkah 1 sampai 3)
27. Aksi pemicu (sesi API Ahmad Fauzi): Remove Read Only dari Rahmat Hidayat (setara TC-GS-ROLE-88 langkah 1 sampai 3)
28. Aksi pemicu (sesi API Ahmad Fauzi): centang Create baris Wawan Setiawan di Detail "Manage hardware" dan konfirmasi `[Remove]` (setara TC-GS-ROLE-107 langkah 1 sampai 3)
29. Buka Global Settings > User > Ahmad Fauzi > Tab System Log, ketik Search `Rahmat Hidayat`, tekan Enter
30. Verifikasi total hasil Search sama dengan `S-RH` + 2 (entry Assign dan entry Remove baru)
31. Verifikasi entry Remove (teratas) pada System Log: Action `Remove`, Object `Read Only`, Name `Rahmat Hidayat`, Field `Access Level`, Old Value `Read Only`, New Value `—`; catat Date entry sebagai `D-RH-REMOVE`
32. Verifikasi entry Assign (kedua) pada System Log: Action `Assign`, Object `Read Only`, Name `Rahmat Hidayat`, Field `Access Level`, Old Value `—`, New Value `Read Only`; catat Date entry sebagai `D-RH-ASSIGN`
33. Ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter
34. Verifikasi total hasil Search sama dengan `S-WS` + 1 (tepat 1 entry baru)
35. Verifikasi entry baru (teratas) pada System Log: Action `Auto-Revert`, Object `Read Only`, Name `Wawan Setiawan`, Field `Access Level`, Old Value `Read Only`, New Value `—`; catat Date entry sebagai `D-WS`
36. Buka Global Settings > Activity Log, ketik Search `Rahmat Hidayat`, tekan Enter
37. Verifikasi total hasil Search sama dengan `A-RH` + 2 (baris Assign dan baris Remove baru)
38. Verifikasi baris Remove (teratas) pada Activity Log: Action `Remove`, Object `Read Only`, Name `Rahmat Hidayat`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Ahmad F`, Date sama dengan `D-RH-REMOVE`
39. Verifikasi baris Assign (kedua) pada Activity Log: Action `Assign`, Object `Read Only`, Name `Rahmat Hidayat`, Field `Access Level`, Old Value `—`, New Value `Read Only`, Modified By `Ahmad F`, Date sama dengan `D-RH-ASSIGN`
40. Ganti isi kotak search dengan `Wawan Setiawan`, tekan Enter
41. Verifikasi total hasil Search sama dengan `A-WS` + 1 (tepat 1 baris baru)
42. Verifikasi baris baru (teratas) pada Activity Log: Action `Auto-Revert`, Object `Read Only`, Name `Wawan Setiawan`, Field `Access Level`, Old Value `Read Only`, New Value `—`, Modified By `Ahmad F`, Date sama dengan `D-WS`

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 42 langkah nominal. Alasan di atas sekitar 35 langkah: seluruh spec satu kelas (pencatatan System Log aktor dan Activity Log), dan sebagian besar langkah adalah blok baca-log berpola (buka surface, cari entri, lalu `Verifikasi` kolom log) serta baseline, yang tidak dihitung ke ambang (bagian 3 konvensi). Dua TC sumber adalah varian tier yang sama (Total Control dan Read Only) pada surface log yang sama; tiap blok berdiri sendiri dengan baseline sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber (221, 289) dipertahankan. Dependensi TC-GS-ROLE-58, 86, 106, 80, 88, dan 107 dijalankan lewat aksi pemicu sesi API (langkah 9 sampai 11 dan 26 sampai 28); Given Maya Anggraini ber-Total Control (setara TC-GS-ROLE-59) dan Wawan Setiawan ber-Read Only terjadi di hook `before` sebelum baseline dicatat, sehingga entry Assign keduanya tidak termasuk entri baru yang diasersi. Semua aksi pemicu satu TC dijalankan sebelum surface log dibuka, supaya satu pembukaan System Log dan satu pembukaan Activity Log membaca seluruh entri TC itu.
- "Entry baru (teratas)" dan "(kedua)" berarti urutan pada hasil Search (urutan default Newest First); jumlah entri baru diyakinkan lewat selisih terhadap baseline. Date baris Activity Log dibandingkan dengan Date baris System Log aksi yang sama (S-12) karena Expected "baris yang sama".
- Langkah penghubung (aksi tanpa `Verifikasi`): berpindah ke System Log atau Activity Log dan mengganti isi kotak search (langkah 1 sampai 8, 12, 16, 19, 23, 29, 33, 36, 40); aksi pemicu API (langkah 9 sampai 11 dan 26 sampai 28).
- Temuan untuk QA:
  - TC-GS-ROLE-221 Expected b dan c tidak menyebut kolom Field untuk entry Remove dan Auto-Revert Total Control (Expected a menyebut Field "Access Level" untuk Assign); spec mengikuti TC dan tidak mengasersi Field pada langkah 14 dan 18.
  - TC-GS-ROLE-221 Expected d dan TC-GS-ROLE-289 Expected d ("baris yang sama + Modified By") tidak menyebut Date; spec membandingkan Date dengan baris System Log aksi yang sama, dengan dasar frasa "baris yang sama".
  - TC-GS-ROLE-221 dan TC-GS-ROLE-289 tidak mendefinisikan cara menghitung entri pada System Log dan Activity Log dan memakai user Pre-setup bernama literal yang entrinya menumpuk lintas run; spec memakai total hasil Search dengan baseline sebagai kemampuan yang disediakan tim FE.
