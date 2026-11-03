---
id: TC-FA-FAAL-E2E-052-sse-tab-user-action-search-filter-role-dan-isolasi
title: "SSE Tab User Action: Search/Filter Aktif, Default User, Empty State, Opsi Object Baru, dan Isolasi Client"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-131
  - TC-FA-FAAL-263
  - TC-FA-FAAL-278
  - TC-FA-FAAL-280
  - TC-FA-FAAL-281
  - TC-FA-FAAL-288
coverage:
  web: automated
---

# SSE Tab User Action: Search/Filter Aktif, Default User, Empty State, Opsi Object Baru, dan Isolasi Client

## Prerequisites

- Mode: FE+BE (backend nyata; pembaruan real-time lewat SSE tanpa intercept).
- Akun aktor sesi A: Total Control (Admin Alpha, Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Tab Session terbuka, langkah 1 membuka Tab User Action). Langkah 39 (TC-FA-FAAL-278) memakai Default User (Pre-setup #3) `defaultUserFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_DU_PASSWORD`; langkah 47 (TC-FA-FAAL-288) memakai Total Control client baru (Pre-setup #29). Keduanya ganti akun eksplisit; hook `after` mengembalikan sesi ke akun default suite.
- Pelaku kedua: Admin Beta (Total Control lain, Pre-setup #16) lewat sesi API aktor sesuai `suite.md` untuk TC-FA-FAAL-280, 281 dan 288; Admin Alpha lewat sesi API untuk TC-FA-FAAL-278; Total Control client B (Pre-setup #15, client lain untuk isolasi) lewat sesi API untuk TC-FA-FAAL-263; satu aktor yang melakukan aksi Borrow yang tercatat untuk TC-FA-FAAL-131. Semua pelaku hanya memicu perubahan state dan tidak membuka sesi UI. Email dan password Admin Beta, akun client B, akun client baru (#29), dan pemicu aksi Borrow tidak tertulis di Pre-setup TC dan disediakan tim FE (lihat Temuan untuk QA). Kemampuan mengubah nama group dan melakukan aksi Borrow lewat API disediakan tim FE/BE tanpa endpoint karangan.
- Data Pre-setup: Data Log Tab User Action UA-01 sampai UA-15 (#12); group `Gedung G` (#18) dan `Gedung H` (#19); client B (#15) dengan log berbeda dari client A; client baru tanpa riwayat sesi dan tanpa log aksi dengan satu group `Gedung J` (#29, seed BE tanpa baris log); kondisi belum ada baris Object `Borrow` di Tab User Action client A (TC-FA-FAAL-131 butir d). Identitas data dirujuk lewat `fixtures/activity-log.json` (belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Uji dari TC sumber: nama baru `Gedung G1`, `Gedung H1`, `Gedung J1`; Filter Object `Groups`; Search `Gedung` dan `Citra`.
- Total entri (Z): dibaca dari teks `Showing X–Y of Z entries` sebelum aksi pelaku kedua. Log client A bersifat permanen dan spec lain menambah baris, sehingga asersi memakai selisih terhadap Z yang dicatat, bukan angka absolut (S-12, bagian 8b butir 10). Client baru (#29) tanpa log adalah pengecualian: baris pertama membuat `Showing 1–1 of 1 entries`.
- State yang diubah dan pemulihannya: nama group `Gedung G` dan `Gedung H` (client A) serta `Gedung J` (client #29) diubah lalu dipulihkan ke nama awal lewat fixture BE yang tidak menambah baris log (kemampuan disediakan tim FE/BE; Last Updated group berubah); client baru (#29) dikembalikan ke keadaan tanpa baris log oleh fixture BE sebelum spec. Baris log client A hasil perubahan bersifat permanen dan tidak dihapus. Perubahan lain yang dilakukan pelaku client B dan aksi Borrow juga tercatat permanen; kondisi tanpa Object `Borrow` dipulihkan oleh fixture BE sebelum spec (kemampuan disediakan tim FE/BE).
- Jendela asersi absence SSE: lima detik tanpa memuat ulang halaman, pilihan spec ini (bagian 6).
- Suite berjalan serial (`parallel: false`).
- Hook suite (flag Guided Tooltip, seed dan pemulihan lewat API, sesi API aktor) mengikuti `suite.md`.
- Env var: `FA_TC_PASSWORD`, `FA_DU_PASSWORD`, didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.

## Test Steps

### TC-FA-FAAL-131: Opsi Object baru muncul saat modul pertama kali mencatat aktivitas

1. Di sesi A klik tab User Action
2. Buka Filter Panel dan dropdown Object
3. Verifikasi opsi lain pada dropdown Object tampil (mis. `Groups`)
4. Verifikasi opsi `Borrow` tidak ada
5. Pelaku kedua melakukan satu aksi Borrow yang tercatat di Activity Log hingga aksi tersimpan
6. Tanpa memuat ulang halaman, tutup dropdown Object lalu buka kembali
7. Verifikasi opsi `Borrow` muncul tanpa muat ulang halaman
8. Tutup dropdown Object dan Filter Panel tanpa Apply

### TC-FA-FAAL-263: Log client lain tidak terlihat dan tidak dikirim lewat SSE

9. Catat Z Tab User Action client A dan baris paling atas tabel
10. Klik tab Session
11. Catat Z Tab Session client A
12. Pelaku kedua (Total Control client B, sesi API) mengubah satu group milik client B hingga perubahan tersimpan
13. Tunggu 5 detik tanpa memuat ulang halaman
14. Verifikasi sedikitnya satu baris client A tampil di Tab Session
15. Verifikasi tidak ada baris milik client B di Tab Session client A
16. Klik tab User Action
17. Verifikasi sedikitnya satu baris client A tampil di Tab User Action
18. Verifikasi tidak ada baris milik client B di Tab User Action client A
19. Verifikasi baris paling atas Tab User Action sama dengan yang dicatat pada langkah 9 (aksi client B tidak menambah baris di client A)
20. Verifikasi Z Tab User Action tidak berubah dari nilai yang dicatat

### TC-FA-FAAL-280: Baris baru yang cocok dengan Search dan Filter aktif disisipkan

21. Di sesi A terapkan Filter Object `Groups`
22. Ketik Search `Gedung`, tekan Enter
23. Catat teks `Showing 1–Y0 of Z0 entries` sebagai baseline
24. Verifikasi hasil memuat baris UA-02, UA-13, UA-14, dan UA-15
25. Pelaku kedua (Admin Beta, sesi API) mengubah nama group `Gedung G` menjadi `Gedung G1` hingga perubahan tersimpan
26. Verifikasi baris `Edit` | `Groups` | `Gedung G1` disisipkan in-place di baris pertama tanpa muat ulang
27. Verifikasi tidak ada dialog maupun toast
28. Verifikasi teks pagination menjadi `Showing 1–Y1 of Z1 entries` dengan Z1 = Z0 + 1 dan Y1 = Y0 + 1
29. Pulihkan nama group `Gedung G1` menjadi `Gedung G` lewat fixture BE

### TC-FA-FAAL-281: Baris baru yang tidak cocok dengan Search aktif diabaikan

30. Klik `(←)` pada kotak Search, lalu bersihkan Filter lewat Clear Field
31. Ketik Search `Citra`, tekan Enter
32. Catat teks `Showing 1–Y0 of Z0 entries` sebagai baseline
33. Verifikasi hasil memuat baris UA-07, UA-10, dan UA-12
34. Pelaku kedua (Admin Beta, sesi API) mengubah nama group `Gedung H` menjadi `Gedung H1` hingga perubahan tersimpan
35. Tunggu 5 detik tanpa memuat ulang halaman
36. Verifikasi baris `Edit` | `Groups` | `Gedung H1` tidak disisipkan
37. Verifikasi teks pagination tetap `Showing 1–Y0 of Z0 entries`, sama dengan baseline langkah 32
38. Pulihkan nama group `Gedung H1` menjadi `Gedung H` lewat fixture BE

### TC-FA-FAAL-278: Default User menerima baris baru lewat SSE

39. Ganti akun: logout, lalu login sebagai Default User (Pre-setup #3) dengan `Spectra.env.FA_DU_PASSWORD`
40. Buka Fixed Asset > Reports & Logs > Activity Log, lalu klik tab User Action tanpa Search, Filter, maupun Sort
41. Catat teks `Showing 1–10 of Z0 entries` sebagai baseline
42. Pelaku kedua (Admin Alpha, sesi API) mengubah nama group `Gedung G` menjadi `Gedung G1` hingga perubahan tersimpan
43. Verifikasi baris `Edit` | `Groups` | `Gedung G1` muncul otomatis di baris paling atas tanpa muat ulang
44. Verifikasi tidak ada dialog maupun toast
45. Verifikasi teks pagination menjadi `Showing 1–10 of Z1 entries` dengan Z1 = Z0 + 1
46. Pulihkan nama group `Gedung G1` menjadi `Gedung G` lewat fixture BE

### TC-FA-FAAL-288: Baris pertama lewat SSE menggantikan empty state

47. Ganti akun: logout, lalu login sebagai Total Control (Admin Alpha) client baru (Pre-setup #29)
48. Buka Fixed Asset > Reports & Logs > Activity Log, lalu klik tab User Action
49. Verifikasi empty state tampil dengan Illustration, Title `No activity yet`, dan Description `Fixed Asset user actions and changes will appear here.`
50. Pelaku kedua (Admin Beta, sesi API) mengubah nama group `Gedung J` menjadi `Gedung J1` hingga perubahan tersimpan
51. Verifikasi empty state diganti tabel satu baris dengan Action `Edit`, Object `Groups`, dan Name `Gedung J1` tanpa muat ulang
52. Verifikasi tidak ada dialog maupun toast
53. Verifikasi teks pagination `Showing 1–1 of 1 entries`
54. Pulihkan nama group `Gedung J1` menjadi `Gedung J` dan keadaan client baru tanpa baris log lewat fixture BE

## Notes

- Mode: FE+BE, kelas c (multi-konteks): sesi A mengamati pembaruan SSE akibat aksi pelaku lain. Pelaku kedua memakai sesi API, bukan konteks UI kedua, sehingga tidak butuh butir `P-2` (keputusan 2026-10-30).
- Alasan melewati sekitar 35 langkah (54 langkah): seluruh blok satu kelas harness (SSE multi-konteks pada Tab User Action) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna. Blok TC-FA-FAAL-278 dan 288 membutuhkan ganti akun sehingga ditaruh di akhir agar ganti akun hanya dua kali.
- Urutan TC berbeda dari nomor TC sumber (S-10): TC-FA-FAAL-131 dan 263 dijalankan lebih dulu sebagai akun default (tanpa ganti akun), lalu TC-FA-FAAL-280 dan 281 yang berbagi Search dan Filter, dan TC-FA-FAAL-278 serta 288 terakhir karena ganti akun.
- Asersi tambahan atas TC (S-03): selisih Z (+1) pada langkah 28 dan 45 serta kesamaan baris teratas pada langkah 19 adalah baseline S-12 agar baris dari run sebelumnya tidak dianggap baris baru. Langkah 24 dan 33 memastikan hasil Search dan Filter memuat baris seed sebelum aksi (anchor).
- Urutan asersi absence (langkah 35 sampai 37, 13 sampai 15 dan 17 sampai 20): jendela lima detik ditulis sebagai langkah penghubung tanpa `Verifikasi` (bagian 6); langkah 33 dan 14 serta 17 menjadi anchor positif baris pembanding sebelum asersi absence.
- Langkah penghubung (S-03, S-09): langkah 1 (pindah tab), 8 (menutup panel), 10 dan 16 (pindah tab), 29, 38, 46, 54 (memulihkan nama group dan keadaan client), 30 (membersihkan Search dan Filter), 39 dan 47 (ganti akun eksplisit), 40 dan 48 (membuka layar karena hook `beforeEach` membuka layar di akun dan client default).
- Temuan untuk QA:
  - TC-FA-FAAL-131 butir d menyatakan "Belum ada baris Object `Borrow`" tetapi tidak menyebut aksi Borrow dan aktornya (producer Tab User Action yang tidak punya baris Activity Log tidak diberi TC, NC-14); spec menulis pemicu sebagai kemampuan disediakan tim FE/BE. Karena log permanen, kondisi "belum ada Borrow" hanya berlaku sekali per client; tim FE/BE perlu client atau fixture yang memulihkannya setiap run. Klausa "tanpa perubahan skema" tidak teramati dari UI dan tidak diasersi.
  - TC-FA-FAAL-263 tidak menyebut akun, group, atau nama baris client B maupun data Tab Session client B; spec memakai satu group milik client B yang disediakan tim FE dan mengasersi tidak ada baris milik client B tanpa menyebut nama baris.
  - TC-FA-FAAL-263 butir b ("tidak menambah baris di client A dan Z tidak berubah") dikerjakan dengan dua `Verifikasi` (langkah 19 dan 20) karena dua klausa.
  - TC-FA-FAAL-278 butir 2 mengasumsikan Admin Alpha sebagai sesi B pada client yang sama dengan Default User; spec memakai sesi API Admin Alpha.
  - TC-FA-FAAL-288 tidak menyebut akun Total Control client baru (#29) dan Admin Beta pada client itu; akun disediakan tim FE. Client #29 hanya "tanpa log" pada run pertama; fixture harus mengembalikannya setiap run.
