---
id: TC-AC-ACC-E2E-266-pencatatan-log-create-edit-change-partner-di-tiga-surface
title: "Pencatatan Log Create, Edit, Change Partner, Perubahan Group, dan Satu Baris per Field di Changelog Client, System Log, dan Activity Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-418
  - TC-AC-ACC-419
  - TC-AC-ACC-420
  - TC-AC-ACC-430
  - TC-AC-ACC-913
  - TC-AC-ACC-914
coverage:
  web: automated
---

# Pencatatan Log Create, Edit, Change Partner, Perubahan Group, dan Satu Baris per Field di Changelog Client, System Log, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) A-01 `totalControlPrincipal_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`. Nama tampil A-01 tidak tertulis di Pre-setup TC (disediakan tim FE); kolom Modified By diasersi berformat `[First Name] [Last Initial]` dan hover menampilkan nama lengkap (R-14). Login di hook `before` spec ini; halaman List Client dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Tiga surface pembaca log: Changelog: Client (ikon Changelog di toolbar List; kolom Date, Action, Client Name, Field, Old Value, New Value, Modified By), System Log akun aktor (Settings > User > Detail akun aktor > Tab System Log; kolom Date, Action, Object, Name, Field, Old Value, New Value, tanpa Modified By), Activity Log Admin Console (Tab User Action, disaring Object `Client`; kolom sama dengan System Log ditambah Modified By).
- Data Dinamis milik spec (bersuffix `{runId}-266`, dihapus di hook `after`): Client baru TC-AC-ACC-418 "PT Log Satu {runId}-266" (Client Code kosong, PIC Name "Maya Anggraini", PIC Email `maya.anggraini+{runId}-266@qwertysystem.net`, Address "Jl. Gatot Subroto No. 5", Country/State/City Indonesia/DKI Jakarta/Jakarta Selatan, Postal Code 12930, Default User "Hendra Wijaya" dengan email `hendrawijaya+{runId}-266@qwertysystem.net` dan Division "Operations"); nama Client unik sehingga baseline baris log bernilai nol.
- Data Pre-setup dan fixture yang diubah lalu dipulihkan (Post Condition TC): C-12 "PT Timur Perkasa" (Fax kosong; TC-AC-ACC-419); C-13 "PT Ganti Mitra" (hanya Partner CV Mitra Sejati; TC-AC-ACC-420); Tabel A3 C-ROL-13 "PT Direct Jakarta" (PIC Name awal "Budi Hartono", Website dan Fax kosong; TC-AC-ACC-430); C-AST-13 "PT Riwayat Nama Uji" (Client Direct, Group Cabang Menteng; TC-AC-ACC-913 dan 914). Pemulihan dilakukan sebagai langkah dan dijamin lewat reset data uji (fixture BE disediakan tim FE/BE).
- Baseline (S-12): jumlah baris log pada tiap surface dicatat dengan Search nama Client dan Action sebelum aksi, ukuran halaman 100; asersi "baris baru" memakai selisih terhadap baseline. Jam server dan jam browser sinkron; kolom Date tidak diasersi (Expected TC tidak menyebutnya).
- Parameter blok TC-AC-ACC-419, 420, 913 (langkah 25 sampai 36):

| TC | Client (Search) | Aksi | Action | Field | Old Value | New Value |
|---|---|---|---|---|---|---|
| TC-AC-ACC-419 | PT Timur Perkasa | Buka ⋯ baris, klik Edit, isi Fax `021-5550101`, klik [Save] | `Edit` | `Fax` | `—` | `021-5550101` |
| TC-AC-ACC-420 | PT Ganti Mitra | Buka ⋯ baris, klik Change Partner, klik [+ Add Partner] dan pilih "CV Mitra Lestari", klik [Confirm] | `Change Partner` | `Partner` | `CV Mitra Sejati` | sel memuat `CV Mitra Sejati` dan `CV Mitra Lestari` |
| TC-AC-ACC-913 | PT Riwayat Nama Uji | Buka ⋯ baris, klik Edit, pilih Group "Area Jakarta" pada tree Select Group, klik [Save] | `Edit` | `Group` | `Cabang Menteng` | `Area Jakarta` |

- State global: log baru ditambahkan pada audit trail permanen; suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman List diatur hook suite.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.

## Test Steps

### TC-AC-ACC-418: Log Create tercatat di tiga surface

1. Klik `[+ New Client]`
2. Isi Company Name "PT Log Satu {runId}-266", PIC Name "Maya Anggraini", PIC Email `maya.anggraini+{runId}-266@qwertysystem.net`, Address "Jl. Gatot Subroto No. 5", Country/State/City Indonesia/DKI Jakarta/Jakarta Selatan, Postal Code 12930, Default User "Hendra Wijaya" dengan email `hendrawijaya+{runId}-266@qwertysystem.net` dan Division "Operations"; kosongkan Client Code dan Partner
3. Pilih Group "Cabang Menteng" pada tree Select Group
4. Klik `[Submit]`
5. Klik ikon Changelog di toolbar List, ketik Search "PT Log Satu {runId}-266" di modal, tekan Enter, dan ubah ukuran halaman menjadi 100
6. Verifikasi Changelog: Client memuat tepat 1 baris dengan Action `Create`, Client Name "PT Log Satu {runId}-266", Field `Company Name`, Old Value `—`, New Value "PT Log Satu {runId}-266"
7. Verifikasi Modified By baris itu adalah nama aktor A-01
8. Tutup modal, lalu buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100, ketik Search "PT Log Satu {runId}-266", tekan Enter
9. Verifikasi System Log memuat baris Action `Create`, Object `Client`, Name "PT Log Satu {runId}-266", Field `Company Name`, Old Value `—`, New Value "PT Log Satu {runId}-266"
10. Verifikasi System Log tidak memiliki kolom Modified By
11. Buka Activity Log Admin Console (Tab User Action), saring Object `Client`, ubah ukuran halaman menjadi 100, ketik Search "PT Log Satu {runId}-266", tekan Enter
12. Verifikasi Activity Log memuat baris Action `Create`, Object `Client`, Name "PT Log Satu {runId}-266", Field `Company Name`, Old Value `—`, New Value "PT Log Satu {runId}-266"
13. Verifikasi Modified By baris Activity Log itu adalah nama aktor A-01
14. Hapus Client "PT Log Satu {runId}-266" dari sub-tab Active (Client tanpa riwayat subscription; pemulihan Post Condition)

### TC-AC-ACC-430: Satu baris log per field yang berubah dalam satu aksi

15. Klik ikon Changelog di toolbar List, ketik Search "PT Direct Jakarta" di modal, tekan Enter, ubah ukuran halaman menjadi 100, hitung baris Action `Edit` dengan Field `Website`, `Fax`, atau `PIC Name` (N0), lalu tutup modal
16. Ketik Search "PT Direct Jakarta", tekan Enter, buka ⋯ baris "PT Direct Jakarta", lalu klik Edit
17. Ubah Website menjadi `https://www.direct-jakarta.co.id`, Fax menjadi `0215550188`, dan PIC Name menjadi "Rina Kartika", lalu klik [Save]
18. Klik ikon Changelog di toolbar List, ketik Search "PT Direct Jakarta" di modal, tekan Enter, ubah ukuran halaman menjadi 100, lalu hitung baris Action `Edit` dengan Field `Website`, `Fax`, atau `PIC Name` (N1)
19. Verifikasi N1 = N0 + 3, berupa Action `Edit` terpisah untuk "PT Direct Jakarta"
20. Verifikasi salah satu dari tiga baris baru itu: Field `Website`, Old Value `—`, New Value `https://www.direct-jakarta.co.id`
21. Verifikasi salah satu dari tiga baris baru itu: Field `Fax`, Old Value `—`, New Value `0215550188`
22. Verifikasi salah satu dari tiga baris baru itu: Field `PIC Name`, Old Value `Budi Hartono`, New Value `Rina Kartika`

23. Klik menu Client di sidebar, ketik Search "PT Direct Jakarta", tekan Enter, buka ⋯ baris "PT Direct Jakarta", lalu klik Edit
24. Kosongkan Website dan Fax, ubah PIC Name menjadi "Budi Hartono", lalu klik [Save] (pemulihan Post Condition TC-AC-ACC-430)

### Parameter blok: TC-AC-ACC-419, TC-AC-ACC-420, TC-AC-ACC-913

25. Untuk setiap baris tabel "Parameter blok TC-AC-ACC-419, 420, 913" (langkah 25 sampai 36): tutup modal Changelog sebelumnya, klik menu Client di sidebar, lalu klik ikon Changelog di toolbar List
26. Ketik Search nama Client sesuai kolom "Client" di modal, tekan Enter, ubah ukuran halaman menjadi 100, dan catat jumlah baris Action sesuai kolom "Action" (C0)
27. Tutup modal, buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100, ketik Search nama Client, tekan Enter, dan catat jumlah baris Action sesuai kolom "Action" (S0)
28. Buka Activity Log Admin Console (Tab User Action), saring Object `Client`, ubah ukuran halaman menjadi 100, ketik Search nama Client, tekan Enter, dan catat jumlah baris Action sesuai kolom "Action" (V0)
29. Klik menu Client di sidebar, ketik Search nama Client, tekan Enter, lalu lakukan aksi sesuai kolom "Aksi"
30. Klik ikon Changelog di toolbar List, ketik Search nama Client di modal, tekan Enter, dan ubah ukuran halaman menjadi 100
31. Verifikasi Changelog: Client memuat tepat 1 baris baru (jumlah = C0 + 1) dengan Action, Field, Old Value, dan New Value sesuai tabel, Client Name sesuai kolom "Client", dan Modified By nama aktor A-01
32. Tutup modal, buka Settings > User > Detail akun aktor > Tab System Log, ubah ukuran halaman menjadi 100, ketik Search nama Client, tekan Enter
33. Verifikasi System Log memuat baris baru (jumlah = S0 + 1) dengan Action, Object `Client`, Name sesuai kolom "Client", Field, Old Value, dan New Value sesuai tabel
34. Buka Activity Log Admin Console (Tab User Action), saring Object `Client`, ubah ukuran halaman menjadi 100, ketik Search nama Client, tekan Enter
35. Verifikasi Activity Log memuat baris baru (jumlah = V0 + 1) dengan Action, Object `Client`, Name sesuai kolom "Client", Field, Old Value, dan New Value sesuai tabel, serta Modified By nama aktor A-01
36. Pulihkan Client ke keadaan awal lewat Edit atau Change Partner (Fax dikosongkan kembali untuk TC-AC-ACC-419, "CV Mitra Lestari" di-Remove untuk TC-AC-ACC-420, Group dikembalikan ke "Cabang Menteng" untuk TC-AC-ACC-913)

### TC-AC-ACC-914: Entri Changelog lama tidak berubah setelah Company Name diubah dua kali

37. Klik ikon Changelog di toolbar List, ketik Search "PT Riwayat Nama" di modal, tekan Enter, ubah ukuran halaman menjadi 100, catat jumlah baris Action `Edit` dengan Field `Company Name` (N0), lalu tutup modal
38. Klik menu Client di sidebar, ketik Search "PT Riwayat Nama Uji", tekan Enter, buka ⋯ baris, klik Edit, ubah Company Name menjadi "PT Riwayat Nama Dua", lalu klik [Save]
39. Ketik Search "PT Riwayat Nama Dua", tekan Enter, buka ⋯ baris, klik Edit, ubah Company Name menjadi "PT Riwayat Nama Tiga", lalu klik [Save]
40. Klik ikon Changelog di toolbar List, ketik Search "PT Riwayat Nama" di modal, tekan Enter, dan ubah ukuran halaman menjadi 100
41. Verifikasi Changelog: Client memuat jumlah baris Action `Edit` dengan Field `Company Name` = N0 + 2 (dari kedua aksi)
42. Verifikasi baris rename pertama: Old Value `PT Riwayat Nama Uji`, New Value `PT Riwayat Nama Dua`
43. Verifikasi baris rename kedua: Old Value `PT Riwayat Nama Dua`, New Value `PT Riwayat Nama Tiga`
44. Tutup modal, lalu kembalikan Company Name "PT Riwayat Nama Tiga" ke "PT Riwayat Nama Uji" lewat Edit

## Notes

- Sumber: `admin-console/client/TestCases/tc-client.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03, R-16, S-12): langkah 5, 8, 11, 15, 18, 25 sampai 28, 30, 32, 34, 37, 40 (Search nama Client, ukuran halaman 100, dan baseline jumlah baris log agar "baris baru" teruji dengan selisih pada audit trail permanen, S-14); langkah 14, 23, 24, 36, dan 44 (pemulihan Post Condition TC); klik menu Client di sidebar (mengembalikan ke List dan mereset Search).
- TC-AC-ACC-418 memakai nama Client dan email bersuffix `{runId}-266` (S-12); TC menulis "PT Log Satu" literal. TC-AC-ACC-430 dan 914 kini memuat langkah baseline sendiri: spec mencatat N0 (jumlah baris Action `Edit` dengan Field `Website`, `Fax`, atau `PIC Name`, Search "PT Direct Jakarta") pada langkah 15 dan mengasersi N1 = N0 + 3 pada langkah 19 (urutan ketiga baris tidak ditentukan); untuk TC-AC-ACC-914 N0 (Action `Edit`, Field `Company Name`, Search "PT Riwayat Nama") dicatat pada langkah 37 dan N1 = N0 + 2 diasersi pada langkah 41 (S-12).
- Urutan TC di spec: TC-AC-ACC-418 lebih dulu (membuat data), diikuti TC-AC-ACC-430 (Edit), blok TC-AC-ACC-419/420/913 (tabel), dan TC-AC-ACC-914 setelah TC-AC-ACC-913 pada Client C-AST-13 yang sama; tiap TC memulihkan datanya sendiri.
- Spec ini melewati sekitar 35 langkah setelah ekspansi (blok langkah 25 sampai 36 diulang 3 kali = 36 langkah). Alasan: semua blok satu topik aksi tulis Client dengan akun yang sama dan pola baca tiga surface yang identik; tiap blok memakai Client sendiri dan memulihkan datanya sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Pembagian TC lintas spec: log Suspend/Unsuspend/Bulk di spec 267; log aksi sistem (Auto-Archive, Auto-Reactivate, Send Activation Email) di spec 268; log Resend dan toggle BYO di spec 269; log Asset Control di spec 270; log Delete di spec 271; asersi "tidak ada baris log" di spec 272; snapshot Modified By di spec 273.
- Temuan untuk QA:
  - TC-AC-ACC-418 menulis Division Default User "Operations" dan Client Code "kosong" tanpa menyebut field Default User lain yang wajib; spec mengikuti Data Uji.
  - TC-AC-ACC-419, 420, 913 tidak menyebut baseline; spec menambahkannya (S-12).
  - Nama tampil A-01 untuk asersi Modified By tidak tertulis di Pre-setup TC.
