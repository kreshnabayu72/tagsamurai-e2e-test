---
id: TC-AC-ACC-E2E-070-edit-simpan-changelog-no-op-double-save-dan-identitas-default-user-af
title: "Edit Client: Satu dan Banyak Field Tercatat di Changelog, No-Op, Double-Save, dan Identitas Default User (Active-Full)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-139
  - TC-AC-ACC-140
  - TC-AC-ACC-141
  - TC-AC-ACC-165
  - TC-AC-ACC-945
coverage:
  web: automated
---

# Edit Client: Satu dan Banyak Field Tercatat di Changelog, No-Op, Double-Save, dan Identitas Default User (Active-Full)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Active-Full (A-15) `activeFullJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_ACTIVE_FULL_PASSWORD`. Login akun Active-Full di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya. `{r6}` = 6 digit terakhir `{runId}` (dipakai agar Client Code tetap maksimal 15 karakter).
- Dataset seed (nama bersuffix): Client `PT Sejahtera Abadi {runId}-070` (replika C-01: Active, Partner CV Mitra Sejati, Group Area Jakarta, Client Code `SJA-{r6}`, Default User Activated, PIC Email awal `pic.old@example.com`) dengan Website dan Fax kosong; `PT Direct Jakarta {runId}-070` (replika C-ROL-13: Direct, Group Area Jakarta, PIC Name awal `Budi Hartono`); `PT Pilihan Master {runId}-070` (replika C-EDT-4 dengan Default User Not Yet Activated: First Name `Andre`, Last Name `Wijaya`, Email `andrewijaya+{runId}-070@qwertysystem.net`, Direct, Group Area Jakarta, tanpa subscription). Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Baseline (S-12): sebelum tiap aksi tulis dicatat jumlah baris hasil Search nama Client unik pada Changelog (N) dan, untuk TC-141, pada System Log (Settings > User > Detail akun aktor > Tab System Log), Activity Log Admin Console, serta nilai kolom Last Updated dan Modified By baris List. Asersi "baris baru" memakai selisih terhadap baseline; format Modified By `[First Name] [Last Initial]` (R-14).
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-139: Satu field tercatat satu baris

1. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Sejahtera Abadi {runId}-070`, tekan Enter
2. Catat jumlah baris hasil Search sebagai N1
3. Tutup modal Changelog
4. Ketik Search `PT Sejahtera Abadi {runId}-070`, tekan Enter
5. Buka `⋯` baris `PT Sejahtera Abadi {runId}-070` lalu klik `Edit`
6. Ubah PIC Email menjadi `pic.new@example.com`
7. Klik `[Save]`
8. Verifikasi popup tertutup
9. Verifikasi toast sukses "Success, client has been updated."
10. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Sejahtera Abadi {runId}-070`, tekan Enter
11. Verifikasi jumlah baris menjadi N1 + 1
12. Verifikasi baris teratas (Date terbaru, bertanggal hari ini): Action `Edit`, Client Name "PT Sejahtera Abadi {runId}-070", Field `PIC Email`, Old `pic.old@example.com`, New `pic.new@example.com`, Modified By nama aktor
13. Verifikasi tidak ada baris kedua dengan Action `Edit`, Field `PIC Email`, Old `pic.old@example.com`, dan New `pic.new@example.com` pada Date yang sama
14. Tutup modal Changelog

### TC-140: Beberapa field, satu baris per field

15. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Sejahtera Abadi {runId}-070`, tekan Enter
16. Catat jumlah baris hasil Search sebagai N2
17. Tutup modal Changelog
18. Buka `⋯` baris `PT Sejahtera Abadi {runId}-070` lalu klik `Edit`
19. Isi Website dengan `https://www.sejahteraabadi.co.id` dan Fax dengan `0215550123`
20. Klik `[Save]`
21. Verifikasi popup tertutup
22. Verifikasi toast sukses "Success, client has been updated."
23. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Sejahtera Abadi {runId}-070`, tekan Enter
24. Verifikasi jumlah baris menjadi N2 + 2
25. Verifikasi dua baris teratas (Date terbaru, bertanggal hari ini, urutan bebas) Action `Edit` terpisah untuk Client Name "PT Sejahtera Abadi {runId}-070": Field `Website` (Old `—`, New `https://www.sejahteraabadi.co.id`) dan Field `Fax` (Old `—`, New `0215550123`)
26. Tutup modal Changelog

### TC-141: Edit tanpa perubahan, no-op

27. Ketik Search `PT Sejahtera Abadi {runId}-070`, tekan Enter
28. Catat nilai kolom Last Updated dan Modified By baris "PT Sejahtera Abadi {runId}-070" pada List sebagai L1 dan M1
29. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Sejahtera Abadi {runId}-070`, tekan Enter, ubah ukuran halaman modal menjadi 100
30. Catat jumlah baris hasil Search sebagai N1
31. Tutup modal Changelog
32. Buka Settings > User > Detail akun aktor > Tab System Log, klik ikon Search, ketik `PT Sejahtera Abadi {runId}-070`, tekan Enter
33. Catat jumlah baris hasil Search sebagai S1
34. Buka Activity Log Admin Console (Tab User Action), saring Object "Client", klik ikon Search, ketik `PT Sejahtera Abadi {runId}-070`, tekan Enter
35. Catat jumlah baris hasil Search sebagai A1
36. Kembali ke Admin Console > Client, ketik Search `PT Sejahtera Abadi {runId}-070`, tekan Enter
37. Buka `⋯` baris `PT Sejahtera Abadi {runId}-070` lalu klik `Edit`
38. Klik `[Save]` tanpa perubahan
39. Verifikasi toast netral "No changes to save."
40. Verifikasi tidak ada toast sukses "Success, client has been updated."
41. Ketik Search `PT Sejahtera Abadi {runId}-070` pada List, tekan Enter
42. Catat nilai kolom Last Updated dan Modified By baris "PT Sejahtera Abadi {runId}-070" sebagai L2 dan M2
43. Verifikasi L2 sama dengan L1 dan M2 sama dengan M1
44. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Sejahtera Abadi {runId}-070`, tekan Enter, ubah ukuran halaman modal menjadi 100
45. Catat jumlah baris hasil Search sebagai N2
46. Verifikasi N2 sama dengan N1 (tidak ada baris Changelog baru)
47. Tutup modal Changelog
48. Buka Settings > User > Detail akun aktor > Tab System Log, klik ikon Search, ketik `PT Sejahtera Abadi {runId}-070`, tekan Enter
49. Catat jumlah baris hasil Search sebagai S2
50. Verifikasi S2 sama dengan S1 (tidak ada baris System Log baru)
51. Buka Activity Log Admin Console (Tab User Action), saring Object "Client", klik ikon Search, ketik `PT Sejahtera Abadi {runId}-070`, tekan Enter
52. Catat jumlah baris hasil Search sebagai A2
53. Verifikasi A2 sama dengan A1 (tidak ada baris Activity Log baru)

### TC-165: Double-save hanya menyimpan sekali

54. Ketik Search `PT Direct Jakarta {runId}-070`, tekan Enter
55. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Direct Jakarta {runId}-070`, tekan Enter
56. Catat jumlah baris hasil Search sebagai N4
57. Tutup modal Changelog
58. Buka `⋯` baris `PT Direct Jakarta {runId}-070` lalu klik `Edit`
59. Ubah PIC Name menjadi `Rina Kartika`
60. Klik `[Save]` dua kali dengan cepat
61. Verifikasi kontrol form ter-disable setelah klik pertama
62. Tunggu aksi selesai (popup tertutup)
63. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Direct Jakarta {runId}-070`, tekan Enter
64. Verifikasi jumlah baris menjadi N4 + 1
65. Verifikasi baris teratas (Date terbaru, bertanggal hari ini): Action `Edit`, Client Name "PT Direct Jakarta {runId}-070", Field `PIC Name`, Old `Budi Hartono`, New `Rina Kartika`
66. Verifikasi tidak ada baris kedua dengan Action `Edit`, Field `PIC Name`, Old `Budi Hartono`, dan New `Rina Kartika` pada Date yang sama
67. Tutup modal Changelog

### TC-945: Identitas Default User tercatat dengan awalan Default User

68. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Pilihan Master {runId}-070`, tekan Enter
69. Catat jumlah baris hasil Search sebagai N5
70. Tutup modal Changelog
71. Ketik Search `PT Pilihan Master {runId}-070`, tekan Enter
72. Buka `⋯` baris `PT Pilihan Master {runId}-070` lalu klik `Edit`
73. Ubah First Name menjadi `Andri`, Last Name menjadi `Wijayanto`, dan Email Default User menjadi `andre.baru+{runId}-070@qwertysystem.net`
74. Klik `[Save]`
75. Verifikasi popup tertutup
76. Verifikasi toast sukses "Success, client has been updated."
77. Klik `[Changelog]` di toolbar List, klik ikon Search di modal Changelog, ketik `PT Pilihan Master {runId}-070`, tekan Enter
78. Verifikasi jumlah baris menjadi N5 + 3 (tepat tiga baris baru; tidak ada baris baru Action `Resend Activation Email`)
79. Verifikasi tiga baris terbaru (Date hari ini, urutan bebas) Action `Edit`, Client Name "PT Pilihan Master {runId}-070", Modified By aktor: Field `Default User First Name` (Old `Andre`, New `Andri`), Field `Default User Last Name` (Old `Wijaya`, New `Wijayanto`), dan Field `Default User Email` (Old `andrewijaya+{runId}-070@qwertysystem.net`, New `andre.baru+{runId}-070@qwertysystem.net`)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Alasan di atas 35 langkah (sekitar 79 langkah): satu role, satu topik (Edit tersimpan dan tercatat), tiga Client seed milik sendiri; tiap blok berdiri sendiri. Langkah baca Changelog berpola (buka, Search nama unik, baca baris) tidak dihitung ambang (aturan blok baca-log).
- Langkah penghubung (S-03): pencatatan baseline, Search nama unik, penutupan modal Changelog; pada TC-141 pembukaan tiap surface (Changelog dengan ukuran halaman modal 100, System Log, Activity Log dengan saring Object "Client") disertai Search nama unik, penutupan modal Changelog, kembali ke Admin Console > Client dengan Search nama unik, dan pencatatan L1, M1, N1, S1, A1, L2, M2, N2, S2, A2 (langkah 27 sampai 53). Nama nilai TC-141 mengikuti TC; N1 dan N2 pada blok TC-139 dan TC-140 hanya berlaku di blok masing-masing.
- Temuan untuk QA:
  - TC-139 dan TC-140 menyebut Modified By "nama aktor"; spec mengasersi format `[First Name] [Last Initial]` (R-14) tanpa mengarang nama akun.
