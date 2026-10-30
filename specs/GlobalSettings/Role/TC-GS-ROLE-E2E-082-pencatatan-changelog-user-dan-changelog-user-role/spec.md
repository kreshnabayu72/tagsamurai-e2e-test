---
id: TC-GS-ROLE-E2E-082-pencatatan-changelog-user-dan-changelog-user-role
title: "Pencatatan Changelog: User dan Changelog: User > Role"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ROLE-223
  - TC-GS-ROLE-290
coverage:
  web: automated
---

# Pencatatan Changelog: User dan Changelog: User > Role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Ahmad Fauzi (Total Control, Modified By `Ahmad F`), `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #1). Login di hook `before` spec ini; kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar). Akun ini akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Layar awal dibuka di hook `beforeEach`: Global Settings > Role & Permission > Tab Total Control.
- Environment variable: `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup yang dipakai (bernama literal sesuai TC; state awal dipulihkan di hook `after`):

| User | Pre-setup | State awal (Given di hook `before`) | Aksi pemicu di spec ini | TC |
|---|---|---|---|---|
| Sari Wulandari | #11 kandidat (Active) | Tanpa access level dan tanpa baris role | Assign Total Control, lalu Remove Total Control | TC-GS-ROLE-223 |
| Maya Anggraini | #11 kandidat (Inactive) | Di-assign Total Control oleh Ahmad Fauzi lewat sesi API (setara TC-GS-ROLE-59, hanya Maya Anggraini; dipakai sebagai precondition TC, tidak diasersi) | Update Manage TAG dikosongkan, memicu Edit dan Auto-Revert | TC-GS-ROLE-223, TC-GS-ROLE-290 |
| Wawan Setiawan | #11 kandidat (Active) | Tanpa access level dan tanpa baris role | Assign baris Manage TAG | TC-GS-ROLE-290 |
| Doni Pratama | #10 (Staff, IT) | Manage TAG: Read checked, Update unchecked | Remove baris Manage TAG | TC-GS-ROLE-290 |

- Data Dinamis bersuffix tidak ada: entri log dikenali lewat baseline jumlah entri (S-12). User Pre-setup bernama literal, sehingga entri log run sebelumnya tetap ada. Jumlah entri adalah total entri pada tab Changelog: User atau Changelog: User > Role milik user itu (seluruh halaman), dicatat pada langkah 1 sampai 5 (sebelum aksi pemicu pertama yang diasersi) sebagai `B-SW-U`, `B-MA-R`, `B-MA-U`, `B-WS-R`, dan `B-DP-R`; asersi "entry baru" memakai selisih terhadap baseline itu. Kemampuan membaca total entri pada kedua tab disediakan tim FE.
- Kemampuan teknis: aksi pemicu dijalankan lewat sesi API atas nama Ahmad Fauzi (agar Modified By tercatat `Ahmad F`): Assign dan Remove access level, Edit CRUD satu baris role beserta konfirmasi `[Remove]` auto-revert, Assign Role, dan Remove baris role. Aksi ini adalah dependensi TC sumber (TC-GS-ROLE-58, 86, 106, 94, 112) yang dijalankan lewat seeding API (S-04). Mekanisme dan endpoint disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD).
- Pemulihan (hook `after`, tidak berasumsi seeding atau aksi berhasil penuh), lewat sesi API Ahmad Fauzi: Sari Wulandari, Maya Anggraini, dan Wawan Setiawan dikembalikan ke tanpa access level dan tanpa baris role; baris Manage TAG milik Doni Pratama ditambahkan kembali dengan Read checked dan Update unchecked. Efek pada Pre-setup: Modified By dan Last Updated keempat user berubah; entri log bersifat immutable dan tidak dihapus.
- Format tanggal mengikuti General Settings aktif. Tidak ada manipulasi jam.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Suite berjalan serial (`parallel: false`) karena spec mengubah access level dan baris role user Pre-setup bersama; tidak ada state global lain yang diubah.

## Test Steps

### Baseline jumlah entri (sebelum aksi pemicu TC-GS-ROLE-223 dan TC-GS-ROLE-290)

1. Buka Global Settings > User > Sari Wulandari > Changelog: User, catat total entri sebagai `B-SW-U`
2. Buka Global Settings > User > Maya Anggraini > Changelog: User > Role, catat total entri sebagai `B-MA-R`
3. Buka Global Settings > User > Maya Anggraini > Changelog: User, catat total entri sebagai `B-MA-U`
4. Buka Global Settings > User > Wawan Setiawan > Changelog: User > Role, catat total entri sebagai `B-WS-R`
5. Buka Global Settings > User > Doni Pratama > Changelog: User > Role, catat total entri sebagai `B-DP-R`

### TC-GS-ROLE-223: Changelog: User mencatat aksi access level dan role; Changelog: User > Role hanya aksi per-role

6. Aksi pemicu (sesi API Ahmad Fauzi): Assign Total Control ke Sari Wulandari (setara TC-GS-ROLE-58 langkah 1 sampai 3)
7. Aksi pemicu (sesi API Ahmad Fauzi): Remove Total Control dari Sari Wulandari (setara TC-GS-ROLE-86 langkah 1 sampai 2)
8. Aksi pemicu (sesi API Ahmad Fauzi): hapus centang Update baris Manage TAG milik Maya Anggraini dan konfirmasi `[Remove]` (setara TC-GS-ROLE-106 langkah 1 sampai 2)
9. Buka Global Settings > User > Sari Wulandari > Changelog: User
10. Verifikasi total entri sama dengan `B-SW-U` + 2 (entry Assign dan entry Remove baru)
11. Verifikasi entry Remove Access Level (teratas): Action `Remove`, Field `Access Level`
12. Verifikasi entry Assign Access Level (kedua): Action `Assign`, Field `Access Level`
13. Buka Global Settings > User > Maya Anggraini > Changelog: User > Role
14. Verifikasi total entri sama dengan `B-MA-R` + 1 (tepat 1 entry baru)
15. Verifikasi entry baru (teratas): Action `Edit`, Manage TAG, Field `Update`
16. Verifikasi tidak ada entry baru Action `Auto-Revert` pada Changelog: User > Role Maya Anggraini; satu-satunya entry baru adalah Edit pada langkah 15

### TC-GS-ROLE-290: Changelog: User > Role mencatat Assign dan Remove baris role; Changelog: User mencatat Auto-Revert

17. Aksi pemicu (sesi API Ahmad Fauzi): Assign baris Manage TAG ke Wawan Setiawan (setara TC-GS-ROLE-94 langkah 1 sampai 3, hanya Wawan Setiawan)
18. Aksi pemicu (sesi API Ahmad Fauzi): Remove baris Doni Pratama dari Detail "Manage TAG" (setara TC-GS-ROLE-112 langkah 1 sampai 2)
19. Buka Global Settings > User > Wawan Setiawan > Changelog: User > Role
20. Verifikasi total entri sama dengan `B-WS-R` + 1 (tepat 1 entry baru)
21. Verifikasi entry baru (teratas): Action `Assign`, Manage TAG, Field `Access`, Old Value `—`, New Value `Assigned`
22. Buka Global Settings > User > Doni Pratama > Changelog: User > Role
23. Verifikasi total entri sama dengan `B-DP-R` + 1 (tepat 1 entry baru)
24. Verifikasi entry baru (teratas): Action `Remove`, Manage TAG, Field `Access`, Old Value `Assigned`, New Value `—`
25. Buka Global Settings > User > Maya Anggraini > Changelog: User
26. Verifikasi total entri lebih besar daripada `B-MA-U` (entry baru dari langkah 8 tercatat)
27. Verifikasi entry baru Auto-Revert tampil: Action `Auto-Revert`, Field `Access Level`, Old Value `Total Control`, New Value `—`

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec memuat 27 langkah. Urutan TC sumber (223, 290) dipertahankan. Dependensi TC-GS-ROLE-58, 86, 106, 94, dan 112 dijalankan lewat aksi pemicu sesi API (langkah 6 sampai 8, 17, 18). Aksi pemicu Maya Anggraini (langkah 8) dipakai bersama oleh TC-GS-ROLE-223 Expected b dan c (Changelog: User > Role) dan TC-GS-ROLE-290 Expected c (Changelog: User); Given Maya Anggraini ber-Total Control terjadi di hook `before` sebelum baseline dicatat. Nina Kartika tidak di-assign karena tidak diasersi di spec ini (seeding minimal, S-11).
- TC-GS-ROLE-223 Expected c ("tidak memuat entry Auto-Revert") ditulis sebagai asersi jumlah terhadap baseline (langkah 14 dan 16), bukan asersi absence kelas g: aksi pemicu nyata ada di spec ini (langkah 8) dan anchor positifnya adalah entry Edit pada langkah 15 di tab yang sama. Asersi absence untuk Assign Total Control ada di spec `TC-GS-ROLE-E2E-083-absence-log-assign-total-control-tidak-menulis-changelog-user-role` (TC-GS-ROLE-224), yang tidak dimuat di spec ini.
- "Entry baru (teratas)" dan "(kedua)" berarti urutan pada tab (urutan default Newest First); jumlah entri baru diyakinkan lewat selisih terhadap baseline.
- Langkah penghubung (aksi tanpa `Verifikasi`): membuka tab Changelog: User atau Changelog: User > Role milik user (langkah 1 sampai 5, 9, 13, 19, 22, 25); aksi pemicu API (langkah 6 sampai 8, 17, 18).
- Temuan untuk QA:
  - TC-GS-ROLE-223 Expected a menyebut "Changelog: User Sari Wulandari memuat entry Assign dan Remove Access Level" tanpa jumlah entri; spec mengasersi selisih +2 terhadap baseline karena Sari Wulandari tidak punya aksi lain pada langkah 6 dan 7.
  - TC-GS-ROLE-223 Expected b menyebut "entry Edit Manage TAG Update" tanpa format kolom Changelog: User > Role; spec menulis `Manage TAG` dan Field `Update` mengikuti pola Changelog Detail dan perlu dikonfirmasi.
  - TC-GS-ROLE-223 judul menyatakan Changelog: User juga mencatat aksi role, tetapi TC-GS-ROLE-290 Expected c hanya menyebut Auto-Revert di Changelog: User Maya Anggraini; karena belum jelas apakah Edit Manage TAG juga masuk Changelog: User, spec mengasersi total Maya Anggraini lebih besar daripada baseline (langkah 26) dan bukan selisih tepat.
  - TC-GS-ROLE-290 Expected a dan b tidak menyebut Role — User atau User Name; spec memakai Manage TAG dan Field `Access` sesuai TC.
  - TC-GS-ROLE-223 dan TC-GS-ROLE-290 tidak mendefinisikan cara menghitung entri pada tab Changelog: User dan memakai user Pre-setup bernama literal yang entrinya menumpuk lintas run; spec memakai total entri dengan baseline sebagai kemampuan yang disediakan tim FE.
