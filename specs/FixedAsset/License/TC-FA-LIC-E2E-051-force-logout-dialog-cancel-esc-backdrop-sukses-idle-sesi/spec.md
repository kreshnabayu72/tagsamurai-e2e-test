---
id: TC-FA-LIC-E2E-051-force-logout-dialog-cancel-esc-backdrop-sukses-idle-sesi
title: "Force Logout: Dialog, Cancel, Esc, Backdrop, Sukses, Sesi Idle, dan Sesi Berakhir"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-169
  - TC-FA-LIC-170
  - TC-FA-LIC-171
  - TC-FA-LIC-172
  - TC-FA-LIC-174
  - TC-FA-LIC-175
  - TC-FA-LIC-178
coverage:
  web: automated
---

# Force Logout: Dialog, Cancel, Esc, Backdrop, Sukses, Sesi Idle, dan Sesi Berakhir

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): spec ini mengubah sesi aktif Pre-setup #14 (sesi Budi Santoso dan Dewi Lestari diakhiri); hook `after` memulihkannya lewat fixture BE pemulih. Spec ini tidak mengubah hierarki atau alokasi grup.
- Data: Pre-setup #14 (sesi aktif PT Sejahtera): 18 sesi, seat 25, Online Users 18/25; sesi Budi Santoso (Chrome on Windows) tidak aktif lebih dari 2 jam (Last Activity 07:05); Dewi Lestari Last Activity 09:36.
- Data: Fixture BE penyetel untuk TC-FA-LIC-174: Dewi Lestari memiliki sesi Windows/Edge dan sesi Android/Mobile App.
- Data: Akun login Budi Santoso (Pre-setup #14) dipakai sesi API untuk mengakhiri sesinya sendiri pada TC-FA-LIC-175; email dan password akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA), disediakan tim FE.
- Pemulihan sesi aktif Pre-setup #14 (18 sesi, seat 25) dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: entri `Changelog: Concurrent User`, System Log aktor, dan Activity Log bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: Kemampuan membaca jumlah entri `Changelog: Concurrent User`, System Log aktor, dan Activity Log sebagai baseline (disediakan tim FE/BE; audit trail permanen sehingga asersi memakai selisih jumlah entri, S-12).
- Jalur menu: Changelog lewat License > Concurrent User > ikon Changelog pada toolbar; System Log aktor lewat Global Settings > User > Detail Rudi Hartono > Tab System Log; Activity Log lewat Fixed Asset > Reports & Logs > Activity Log.
- Kemampuan teknis (disediakan tim FE): mengirim tombol `Esc` ke browser (langkah 10).
- Kemampuan teknis: jeda waktu nyata 5 detik pada langkah `Tunggu 5 detik` (langkah 49) untuk memastikan toast Success yang hilang otomatis setelah 4 detik (TC-FA-LIC-171 butir d) sudah lewat; durasi 5 detik dipilih spec karena TC hanya menyebut 4 detik, jam tidak digeser, dan jeda di bawah 30 detik memakai waktu nyata.

## Test Steps

### TC-FA-LIC-169: Screening dialog Force Logout User

1. Klik tab `Concurrent User`
2. Ketik Search `Budi Santoso`, tekan Enter
3. Klik `[Force Logout]` pada baris Budi Santoso
4. Verifikasi dialog dengan ikon warning dan Title `Force Logout User`
5. Verifikasi Body: bullet `Budi Santoso`, teks `This will immediately terminate the user's active session and release one concurrent seat. The user will be required to log in again.`, dan `Are you sure you want to log out this user?`
6. Verifikasi Footer: `[Cancel]` (text, contrast) dan `[Confirm Logout]` (filled, primary)

### TC-FA-LIC-170: Cancel, Esc, dan backdrop tidak mengubah apa pun

7. Klik `[Cancel]`
8. Verifikasi dialog tertutup
9. Klik `[Force Logout]` pada baris Budi Santoso
10. Tekan Esc
11. Verifikasi dialog tertutup
12. Klik `[Force Logout]` pada baris Budi Santoso
13. Klik backdrop
14. Verifikasi dialog tidak tertutup
15. Klik `[Cancel]`
16. Verifikasi baris Budi Santoso tetap ada
17. Verifikasi Online Users tetap `18/25`
18. Verifikasi tidak ada toast

### TC-FA-LIC-175: Force Logout atas sesi yang sudah berakhir

19. Klik `[Force Logout]` pada baris Budi Santoso
20. Akhiri sesi Budi Santoso (logout sendiri) lewat sesi API hingga sesi berakhir tersimpan
21. Klik `[Confirm Logout]`
22. Verifikasi dialog blok `Session Already Expired` dengan teks `This session is no longer active.` dan tombol `[OK]`
23. Verifikasi tidak ada toast sukses `Success, user session has been terminated.`
24. Klik `[OK]`
25. Verifikasi daftar sesi di-refresh tanpa baris Budi Santoso

### TC-FA-LIC-172: Force Logout tersedia untuk sesi idle tanpa syarat idle

26. Jalankan fixture BE pemulih Pre-setup #14 hingga tersimpan
27. Muat ulang halaman License, lalu klik tab `Concurrent User`
28. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter
29. Verifikasi tombol `[Force Logout]` tersedia pada baris Budi Santoso (Last Activity 07:05)
30. Ganti isi kotak search dengan `Dewi Lestari`, tekan Enter
31. Verifikasi tombol `[Force Logout]` tersedia pada baris Dewi Lestari (Last Activity 09:36)
32. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter
33. Klik `[Force Logout]` pada baris Budi Santoso
34. Klik `[Confirm Logout]`
35. Verifikasi toast sukses `Success, user session has been terminated.` untuk Budi Santoso
36. Ganti isi kotak search dengan `Dewi Lestari`, tekan Enter
37. Klik `[Force Logout]` pada baris Dewi Lestari
38. Klik `[Confirm Logout]`
39. Verifikasi toast sukses `Success, user session has been terminated.` untuk Dewi Lestari

### TC-FA-LIC-171: Force Logout sukses

40. Jalankan fixture BE pemulih Pre-setup #14 hingga tersimpan
41. Muat ulang halaman License, lalu klik tab `Concurrent User`
42. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter
43. Klik `[Force Logout]` pada baris Budi Santoso
44. Klik `[Confirm Logout]`
45. Verifikasi toast sukses `Success, user session has been terminated.`
46. Verifikasi baris Budi Santoso hilang (fade-out) dari daftar
47. Verifikasi Metric Summary Bar menjadi `Online Users: 17/25`
48. Verifikasi toast Success tampil di kanan bawah layar (bottom-right)
49. Tunggu 5 detik
50. Verifikasi toast hilang otomatis setelah 4 detik

### TC-FA-LIC-178: Double-click Confirm Logout hanya memproses satu request

51. Jalankan fixture BE pemulih Pre-setup #14 hingga tersimpan
52. Muat ulang halaman License, lalu klik tab `Concurrent User`
53. Catat jumlah entri `Changelog: Concurrent User`, System Log aktor, dan Activity Log Fixed Asset sebagai baseline
54. Ganti isi kotak search dengan `Budi Santoso`, tekan Enter
55. Klik `[Force Logout]` pada baris Budi Santoso
56. Klik `[Confirm Logout]` dua kali cepat
57. Verifikasi satu toast sukses
58. Verifikasi Online Users berkurang tepat satu
59. Klik ikon Changelog pada toolbar
60. Verifikasi tepat satu entri baru di `Changelog: Concurrent User` dibanding baseline
61. Tutup modal `Changelog: Concurrent User`
62. Buka Global Settings > User, ketik Search `Rudi Hartono`, tekan Enter
63. Klik Name `Rudi Hartono`, buka Tab System Log
64. Verifikasi tepat satu entri baru di System Log aktor dibanding baseline
65. Buka Fixed Asset > Reports & Logs > Activity Log
66. Verifikasi tepat satu entri baru di Activity Log Fixed Asset dibanding baseline

### TC-FA-LIC-174: Force Logout hanya mengakhiri sesi yang dipilih

67. Jalankan fixture BE pemulih Pre-setup #14 dan penyetel Dewi Lestari dengan dua sesi (Windows/Edge dan Android/Mobile App) hingga tersimpan
68. Buka Fixed Asset > License, klik tab `Concurrent User`
69. Ganti isi kotak search dengan `Dewi Lestari`, tekan Enter
70. Verifikasi baris Dewi Lestari Windows/Edge dan Android/Mobile App tampil
71. Klik `[Force Logout]` pada baris Dewi Lestari sesi Windows/Edge
72. Klik `[Confirm Logout]`
73. Verifikasi baris Android/Mobile App Dewi Lestari tetap ada
74. Verifikasi baris Windows/Edge Dewi Lestari hilang

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): fixture BE pemulih dan penyetel, muat ulang halaman, pembukaan ulang Fixed Asset > License (langkah 68), dan klik tab menyiapkan state tiap blok setelah sesi Budi Santoso atau Dewi Lestari diakhiri; langkah 59, 62 sampai 63, dan 65 membuka satu surface log per kali (Changelog, System Log aktor, Activity Log) dan langkah 61 menutup modal Changelog sebelum surface berikutnya (S-14); `Akhiri sesi ... lewat sesi API` adalah pemicu pelaku kedua (R-20).
- Langkah 69 memakai "ganti isi kotak search" karena retensi Search lintas navigasi menu tidak diatur bagian 8b butir 9; idiom ini aman baik kotak kosong maupun terisi.
- Baris Budi Santoso dan Dewi Lestari di tabel Active Sessions (18 sesi, lebih dari satu halaman) dibuka lewat Search sebagai langkah penghubung (R-16, bagian 8b butir 13): langkah 2, 28, 30, 32, 36, 42, 54, dan 69, serta langkah 62 dan 63 untuk baris aktor di Global Settings > User. Search bertahan selama dialog dibuka dan ditutup pada langkah 3 sampai 25 dan sesudah muat ulang halaman (8b.9): langkah 28, 42, dan 54 memakai "ganti isi kotak search" karena kotak masih berisi pencarian blok sebelumnya.
- Langkah penghubung `Tunggu 5 detik` (langkah 49, aksi tanpa `Verifikasi`) menunggu timer toast 4 detik berlalu sebelum `Verifikasi` toast hilang otomatis pada langkah 50.
- Urutan TC: TC-FA-LIC-169 dan TC-FA-LIC-170 (tanpa mutasi) lebih dulu, lalu TC-FA-LIC-175, TC-FA-LIC-172, TC-FA-LIC-171, TC-FA-LIC-178, dan TC-FA-LIC-174 yang masing-masing mengakhiri sesi dan dipulihkan fixture (S-10).
- TC-FA-LIC-175: klausa `tanpa log` pada judul TC dirujuk ke spec absence log (kelas g, S-05); spec ini mengasersi dialog blok, tidak ada toast sukses, dan daftar sesi.
- Temuan untuk QA:
  - TC-FA-LIC-175: Automation `Manual Only — (d) dua sesi paralel`; spec memakai sesi API Budi Santoso untuk mengakhiri sesinya dan satu sesi UI aktor. Email dan password Budi Santoso tidak tertulis di Pre-setup #14 (disediakan tim FE).
  - TC-FA-LIC-172: klausa `tanpa pengecekan idle` diasersi lewat keberhasilan Force Logout atas sesi dengan Last Activity berbeda (07:05 dan 09:36); TC tidak menyebut cara mengamati pengecekan idle.
  - TC-FA-LIC-174: precondition tidak menyebut Pre-setup untuk dua sesi Dewi Lestari; disediakan fixture penyetel tim FE/BE.
- Alasan di atas sekitar 35 langkah (74 langkah): semua blok satu topik (Force Logout pada Tab Concurrent User) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya pemulihan fixture sesi dan muat ulang.
