---
id: TC-AC-LA-E2E-136-konfigurasi-platform-dibaca-live
title: "Konfigurasi Platform Dibaca Live: Product Price, Toggle Approval, dan Plan Berbeda"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-441
  - TC-AC-LA-475
  - TC-AC-LA-442
  - TC-AC-LA-473
coverage:
  web: automated
---

# Konfigurasi Platform Dibaca Live: Product Price, Toggle Approval, dan Plan Berbeda

## Prerequisites

- Mode: FE+BE
- Login di hook `before` spec ini sebagai Dewi Anggraini (akun pertama); halaman dibuka hook `beforeEach` suite (tab Current), yang juga menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat `suite.md`). Ganti akun ke Fajar Nugroho dilakukan eksplisit pada blok TC-AC-LA-473; hook `after` mengembalikan sesi ke akun default suite. Flag Guided Tooltip diatur hook `before` suite.
- Akun yang dipakai:

| Akun | Pre-setup | Peran | Email | Env password |
|---|---|---|---|---|
| Dewi Anggraini | #4 | Distributor PT Maju Bersama, Manage allocation Create+Read+Update | `dewiFullLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_DIST_FULL_PASSWORD` |
| Fajar Nugroho | #10 | Total Control Distributor PT Maju Bersama | `totalControlDistLic_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_LA_TC_DIST_PASSWORD` |

  Email dan `{namaCompany}` dirujuk lewat `Fixture.license-allocation-license` (fixture belum ada; disediakan tim FE).
- Data Pre-setup: Client PT Sejahtera (Pre-setup #19; FAMS Professional `SUBS-20260101-A1B2C`), Klinik Medika Jaya (Pre-setup #20; SIEM Growth `SUBS-20260301-P1Q2R`), CV Mitra Sejati (Pre-setup #22; SAMS Growth `SUBS-20260105-K2L3M`), kantong wallet Distributor PT Maju Bersama saldo $10,000.00 (Pre-setup #33), Product Price Concurrent User $365 per unit per tahun (Pre-setup #34), Require Approval for Allocation OFF (Pre-setup #39) untuk TC-AC-LA-441, 475, dan awal TC-AC-LA-442, ON (Pre-setup #38) pada seed dan akhir TC-AC-LA-442.
- Data Dinamis (seed milik spec ini, dibuat lewat seeding backend di hook `before` saat toggle ON; tidak memakai baris Pre-setup #41 bersama): `{idOld}` dan `{idWfa}`, alokasi `Waiting for Approval` Concurrent User +5 ke `SUBS-20260101-A1B2C` PT Sejahtera, requester Dewi Anggraini, Cost $150.00 di-Reserve (bentuk Pre-setup #41). Alokasi lain dikenali lewat Allocation ID hasil Submit di spec ini (`{idDone}`, `{idWait}`).
- Kemampuan teknis (disediakan tim FE/BE; TC tidak menyebut akun pelaku): fixture waktu untuk jam server dan jam browser dengan nilai absolut; fixture backend untuk mengubah harga Concurrent User di Wallet > Product Price dan memulihkannya; fixture backend untuk menyetel Require Approval for Allocation ON atau OFF (Settings > Role & Permission) dan memulihkannya; seeding alokasi dan pembersihannya; menampilkan kolom Cost lewat Setup Column (pemulihan preferensi kolom di hook `after`, disediakan tim FE).
- State global: harga Concurrent User dinaikkan dari $365 menjadi $730 per unit per tahun pada blok TC-AC-LA-441 dan dipulihkan setelah blok itu dan di hook `after`; toggle Require Approval for Allocation berganti OFF (setelah seed), ON (pada TC-AC-LA-442), lalu OFF (pada TC-AC-LA-473) dan dipulihkan di hook `after`; jam server dan jam browser diatur ke `22 Dec 2026` pada blok TC-AC-LA-441 dan dipulihkan setelah blok itu; saldo kantong #33 dipulihkan oleh pembersihan record.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### Harga Product Price berlaku untuk Submit baru (TC-AC-LA-441)

1. Atur jam server dan jam browser ke `22 Dec 2026` (nilai absolut)
2. Klik `[+ Allocation]`
3. Pilih Client `PT Sejahtera`
4. Pilih Target `SUBS-20260101-A1B2C`
5. Pilih Type `Concurrent User`
6. Isi Additional Quantity `10`
7. Catat Preview Cost dengan harga awal sebagai `{cost0}` (`$100.00`)
8. Klik `[×]`
9. Verifikasi dialog `Unsaved Changes` dengan isi `You have unsaved changes. Are you sure you want to leave?`
10. Klik `[Leave]`
11. Naikkan harga Concurrent User di Wallet > Product Price menjadi $730 per unit per tahun hingga tersimpan
12. Klik `[+ Allocation]` tanpa memuat ulang halaman List
13. Pilih Client `PT Sejahtera`
14. Pilih Target `SUBS-20260101-A1B2C`
15. Pilih Type `Concurrent User`
16. Isi Additional Quantity `10`
17. Verifikasi Preview Cost `$200.00` memakai harga baru, berbeda dari `{cost0}` tanpa memuat ulang halaman List
18. Klik `[×]`
19. Verifikasi dialog `Unsaved Changes` dengan isi `You have unsaved changes. Are you sure you want to leave?`
20. Klik `[Leave]`
21. Pastikan kolom Cost tampil: klik ikon `⋯` pada header kolom, klik `Setup Column...`, centang kolom Cost, lalu klik `[Save]`
22. Ketik Search `{idOld}`, tekan Enter
23. Verifikasi Cost record lama `{idOld}` tetap `$150.00` (snapshot)
24. Pulihkan harga Concurrent User menjadi $365 per unit per tahun dan pulihkan jam server dan jam browser ke waktu nyata
25. Klik `(←)` pada kotak Search, lalu catat baseline Allocation ID baris di halaman pertama tab Current

### Perilaku identik pada Subscription Paid dengan plan berbeda (TC-AC-LA-475)

26. Klik `[+ Allocation]`
27. Pilih Client `PT Sejahtera`
28. Pilih Target `SUBS-20260101-A1B2C` (plan Professional)
29. Pilih Type `Concurrent User`
30. Isi Additional Quantity `1`
31. Verifikasi form tidak menampilkan gating atau upsell tambahan
32. Klik `[Submit]`
33. Verifikasi baris baru tampil di tab Current (Allocation ID tidak ada pada baseline langkah 25)
34. Verifikasi alokasi diproses tanpa dialog gating atau upsell tambahan
35. Catat baseline Allocation ID baris di halaman pertama tab Current
36. Klik `[+ Allocation]`
37. Pilih Client `Klinik Medika Jaya`
38. Pilih Target `SUBS-20260301-P1Q2R` (plan Growth)
39. Pilih Type `Concurrent User`
40. Isi Additional Quantity `1`
41. Verifikasi form tidak menampilkan gating atau upsell tambahan
42. Klik `[Submit]`
43. Verifikasi baris baru tampil di tab Current (Allocation ID tidak ada pada baseline langkah 35)
44. Verifikasi alokasi diproses tanpa dialog gating atau upsell tambahan
45. Catat baseline Allocation ID baris di halaman pertama tab Current
46. Klik `[+ Allocation]`
47. Pilih Client `CV Mitra Sejati`
48. Pilih Target `SUBS-20260105-K2L3M` (plan SAMS Growth)
49. Pilih Type `Concurrent User`
50. Isi Additional Quantity `1`
51. Verifikasi form tidak menampilkan gating atau upsell tambahan
52. Klik `[Submit]`
53. Verifikasi baris baru tampil di tab Current (Allocation ID tidak ada pada baseline langkah 45)
54. Verifikasi alokasi diproses tanpa dialog gating atau upsell tambahan
55. Verifikasi alur dan UI identik pada ketiga plan (Professional, Growth, dan SAMS Growth)
56. Verifikasi satu-satunya syarat Target pada ketiga plan adalah term Paid berstatus Active atau Pending
57. Catat baseline Allocation ID baris di halaman pertama tab Current

### Pengaturan toggle approval dibaca saat Submit (TC-AC-LA-442)

58. Klik `[+ Allocation]`
59. Pilih Client `PT Sejahtera`
60. Pilih Target `SUBS-20260101-A1B2C`
61. Pilih Type `Concurrent User`
62. Isi Additional Quantity `1`
63. Klik `[Submit]`
64. Catat Allocation ID baris baru sebagai `{idDone}` (tidak ada pada baseline langkah 57)
65. Verifikasi Status `{idDone}` adalah `Completed`
66. Setel Require Approval for Allocation ON (Pre-setup #38) lewat Settings > Role & Permission
67. Tunggu aksi selesai (toggle ON tersimpan)
68. Buka Allocation > License Allocation (tab Current), lalu catat baseline Allocation ID baris di halaman pertama
69. Klik `[+ Allocation]`
70. Pilih Client `PT Sejahtera`
71. Pilih Target `SUBS-20260101-A1B2C`
72. Pilih Type `Concurrent User`
73. Isi Additional Quantity `1`
74. Klik `[Submit]`
75. Catat Allocation ID baris baru sebagai `{idWait}` (tidak ada pada baseline langkah 68)
76. Verifikasi Status `{idWait}` adalah `Waiting for Approval`
77. Verifikasi Status `{idDone}` tetap `Completed` setelah toggle diubah

### Toggle berubah saat alokasi Waiting for Approval (TC-AC-LA-473)

78. Ganti akun: Logout dari Dewi Anggraini
79. Login sebagai Fajar Nugroho (`totalControlDistLic`, password `Spectra.env.AC_LA_TC_DIST_PASSWORD`)
80. Ubah toggle Require Approval for Allocation ke OFF di Settings > Role & Permission
81. Tunggu aksi selesai (toggle OFF tersimpan)
82. Buka Allocation > License Allocation (tab Current)
83. Ketik Search `{idWfa}`, tekan Enter
84. Verifikasi Status `{idWfa}` tetap `Waiting for Approval`
85. Buka Approvals > License Allocation
86. Verifikasi alokasi `{idWfa}` tetap muncul di Approvals

## Notes

- Alasan di atas sekitar 35 langkah (86 langkah; lima langkah baseline dan tiga anchor baris baru menambah hitungan): seluruh blok satu topik (konfigurasi platform dibaca live saat aksi alokasi), satu kelas harness fungsional, masing-masing berdiri sendiri pada konfigurasi dan record sendiri. Pengisian form Allocate diulang per Client dan per Subscription pada TC-AC-LA-475 (tiga plan), dan TC-AC-LA-441 memakai dua pembukaan form yang masing-masing ditutup lewat `[×]` (S-08).
- Urutan blok berbeda dari urutan sourceTc agar toggle Require Approval for Allocation hanya berganti OFF, ON, OFF dan ganti akun hanya satu kali (S-07): TC-AC-LA-473 terakhir.
- Langkah penghubung (S-03): langkah 21 (menampilkan kolom Cost lewat `⋯` > `Setup Column...`, centang kolom Cost, `[Save]`, tanpa `Verifikasi`; kolom Cost tersembunyi secara bawaan, TC-AC-LA-1 butir b.ii), langkah 1 dan 24 (mengatur dan memulihkan jam serta harga), langkah 7 (mencatat Preview Cost awal sebagai pembanding, tanpa `Verifikasi`), langkah 11 (mengubah harga), langkah 22 dan 83 (Search baris berdasarkan Allocation ID), langkah 66 dan 80 (menyetel toggle), langkah 67 dan 81 (menunggu aksi selesai karena langkah berikutnya membuka surface lain, 8b butir 8), langkah 78 sampai 82 (ganti akun dan navigasi), langkah 25, 35, 45, 57, dan 68 (baseline Allocation ID baris di halaman pertama tab Current sebelum tiap `[Submit]`, S-12, pola spec 042; langkah 25 mengosongkan Search `{idOld}` lewat klik `(←)` pada kotak Search, sedangkan pada langkah 35, 45, dan 57 tidak ada Search aktif sehingga baseline langsung dicatat; langkah 68 membuka ulang List karena toggle baru disetel), langkah 33, 43, dan 53 (anchor positif baris baru sebelum asersi tidak ada dialog gating, 8b butir 2).
- Temuan untuk QA:
  - TC-AC-LA-475 meminta Type `Concurrent User` pada Subscription SIEM Growth Klinik Medika Jaya (Pre-setup #20), sedangkan Pre-setup #20 menyatakan "Type non-SIEM tidak tersedia" (Target Log Source) dan Pre-setup #22 (SAMS Growth) hanya memuat Target Asset Control App, Station, dan Storage. Type `Concurrent User` mungkin tidak tersedia pada dua Subscription itu; spec mengikuti TC dan mencatat kontradiksi ini.
  - TC-AC-LA-475 tidak menyebut Quantity, Target (term), dan bentuk tampilan "gating atau upsell"; spec memakai Quantity `1`, Target dari Pre-setup #19, #20, dan #22, dan asersi tidak adanya dialog atau banner tambahan.
  - TC-AC-LA-441 tidak menyebut nilai harga naik, Client, Target, Type, maupun tanggal acuan; spec memakai harga $730 per unit per tahun, Type `Concurrent User` pada PT Sejahtera, Quantity `10`, dan jam `22 Dec 2026` (Preview Cost `$100.00` menjadi `$200.00`). Pelaku perubahan harga di Wallet > Product Price tidak disebut TC (disediakan tim FE/BE).
  - TC-AC-LA-442 dan TC-AC-LA-473 tidak menyebut pelaku pengubah toggle di Settings > Role & Permission dan nilai Status awal di List; spec memakai Status `Completed` dan `Waiting for Approval` sesuai teks TC.
  - TC-AC-LA-473 butir b ("Toggle hanya memengaruhi Submit atau Edit berikutnya") adalah pernyataan cakupan; asersinya diwakili butir a.
  - TC-AC-LA-473 Precondition menyatakan toggle ON saat Submit, sedangkan spec menyetel OFF sesudah blok TC-AC-LA-442 menyetel ON; seed `{idWfa}` dibuat saat toggle ON.
  - TC-AC-LA-442 butir a menyebut Status `Completed` pada List (langkah 65 dan 77), sedangkan TC-AC-LA-7 butir g menyatakan status `Completed` tidak pernah tampil sebagai label badge; spec mengikuti teks TC-AC-LA-442.
