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
- Suite berjalan serial (`parallel: false`): hierarki dan alokasi grup dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data: Pre-setup #14 (sesi aktif PT Sejahtera): 18 sesi, seat 25, Online Users 18/25; sesi Budi Santoso (Chrome on Windows) tidak aktif lebih dari 2 jam (Last Activity 07:05); Dewi Lestari Last Activity 09:36.
- Data: Fixture BE penyetel untuk TC-FA-LIC-174: Dewi Lestari memiliki sesi Windows/Edge dan sesi Android/Mobile App.
- Data: Akun login Budi Santoso (Pre-setup #14) dipakai sesi API untuk mengakhiri sesinya sendiri pada TC-FA-LIC-175; email dan password akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA), disediakan tim FE.
- Pemulihan sesi aktif Pre-setup #14 (18 sesi, seat 25) dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: entri `Changelog: Concurrent User`, System Log aktor, dan Activity Log bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: Kemampuan membaca jumlah entri `Changelog: Concurrent User`, System Log aktor, dan Activity Log sebagai baseline (disediakan tim FE/BE; audit trail permanen sehingga asersi memakai selisih jumlah entri, S-12).
- Kemampuan teknis: jeda waktu nyata 5 detik pada langkah `Tunggu 5 detik` (langkah 42) untuk memastikan toast Success yang hilang otomatis setelah 4 detik (TC-FA-LIC-171 butir d) sudah lewat; durasi 5 detik dipilih spec karena TC hanya menyebut 4 detik, jam tidak digeser, dan jeda di bawah 30 detik memakai waktu nyata.

## Test Steps

### TC-FA-LIC-169: Screening dialog Force Logout User

1. Klik tab `Concurrent User`
2. Klik `[Force Logout]` pada baris Budi Santoso
3. Verifikasi dialog dengan ikon warning dan Title `Force Logout User`
4. Verifikasi Body: bullet `Budi Santoso`, teks `This will immediately terminate the user's active session and release one concurrent seat. The user will be required to log in again.`, dan `Are you sure you want to log out this user?`
5. Verifikasi Footer: `[Cancel]` (text, contrast) dan `[Confirm Logout]` (filled, primary)

### TC-FA-LIC-170: Cancel, Esc, dan backdrop tidak mengubah apa pun

6. Klik `[Cancel]`
7. Verifikasi dialog tertutup
8. Klik `[Force Logout]` pada baris Budi Santoso
9. Tekan Esc
10. Verifikasi dialog tertutup
11. Klik `[Force Logout]` pada baris Budi Santoso
12. Klik backdrop
13. Verifikasi dialog tidak tertutup
14. Klik `[Cancel]`
15. Verifikasi baris Budi Santoso tetap ada
16. Verifikasi Online Users tetap `18/25`
17. Verifikasi tidak ada toast

### TC-FA-LIC-175: Force Logout atas sesi yang sudah berakhir

18. Klik `[Force Logout]` pada baris Budi Santoso
19. Akhiri sesi Budi Santoso (logout sendiri) lewat sesi API hingga sesi berakhir tersimpan
20. Klik `[Confirm Logout]`
21. Verifikasi dialog blok `Session Already Expired` dengan teks `This session is no longer active.` dan tombol `[OK]`
22. Verifikasi tidak ada toast sukses `Success, user session has been terminated.`
23. Klik `[OK]`
24. Verifikasi daftar sesi di-refresh tanpa baris Budi Santoso

### TC-FA-LIC-172: Force Logout tersedia untuk sesi idle tanpa syarat idle

25. Jalankan fixture BE pemulih Pre-setup #14 hingga tersimpan
26. Muat ulang halaman License, lalu klik tab `Concurrent User`
27. Verifikasi tombol `[Force Logout]` tersedia pada baris Budi Santoso (Last Activity 07:05) dan baris Dewi Lestari (Last Activity 09:36)
28. Klik `[Force Logout]` pada baris Budi Santoso
29. Klik `[Confirm Logout]`
30. Verifikasi toast sukses `Success, user session has been terminated.` untuk Budi Santoso
31. Klik `[Force Logout]` pada baris Dewi Lestari
32. Klik `[Confirm Logout]`
33. Verifikasi toast sukses `Success, user session has been terminated.` untuk Dewi Lestari

### TC-FA-LIC-171: Force Logout sukses

34. Jalankan fixture BE pemulih Pre-setup #14 hingga tersimpan
35. Muat ulang halaman License, lalu klik tab `Concurrent User`
36. Klik `[Force Logout]` pada baris Budi Santoso
37. Klik `[Confirm Logout]`
38. Verifikasi toast sukses `Success, user session has been terminated.`
39. Verifikasi baris Budi Santoso hilang (fade-out) dari daftar
40. Verifikasi Metric Summary Bar menjadi `Online Users: 17/25`
41. Verifikasi toast Success tampil di kanan bawah layar (bottom-right)
42. Tunggu 5 detik
43. Verifikasi toast hilang otomatis setelah 4 detik

### TC-FA-LIC-178: Double-click Confirm Logout hanya memproses satu request

44. Jalankan fixture BE pemulih Pre-setup #14 hingga tersimpan
45. Muat ulang halaman License, lalu klik tab `Concurrent User`
46. Catat jumlah entri `Changelog: Concurrent User`, System Log aktor, dan Activity Log Fixed Asset sebagai baseline
47. Klik `[Force Logout]` pada baris Budi Santoso
48. Klik `[Confirm Logout]` dua kali cepat
49. Verifikasi satu toast sukses
50. Verifikasi Online Users berkurang tepat satu
51. Periksa `Changelog: Concurrent User` (ikon Changelog pada toolbar), System Log aktor, dan Activity Log Fixed Asset
52. Verifikasi tepat satu entri baru di `Changelog: Concurrent User`, satu di System Log aktor, dan satu di Activity Log dibanding baseline
53. Tutup modal `Changelog: Concurrent User`

### TC-FA-LIC-174: Force Logout hanya mengakhiri sesi yang dipilih

54. Jalankan fixture BE pemulih Pre-setup #14 dan penyetel Dewi Lestari dengan dua sesi (Windows/Edge dan Android/Mobile App) hingga tersimpan
55. Muat ulang halaman License, lalu klik tab `Concurrent User`
56. Verifikasi baris Dewi Lestari Windows/Edge dan Android/Mobile App tampil
57. Klik `[Force Logout]` pada baris Dewi Lestari sesi Windows/Edge
58. Klik `[Confirm Logout]`
59. Verifikasi baris Android/Mobile App Dewi Lestari tetap ada
60. Verifikasi baris Windows/Edge Dewi Lestari hilang

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): fixture BE pemulih dan penyetel, muat ulang halaman, dan klik tab menyiapkan state tiap blok setelah sesi Budi Santoso atau Dewi Lestari diakhiri; `Periksa ...` membuka surface log; `Tutup modal` menutup modal Changelog; `Akhiri sesi ... lewat sesi API` adalah pemicu pelaku kedua (R-20).
- Langkah penghubung `Tunggu 5 detik` (langkah 42, aksi tanpa `Verifikasi`) menunggu timer toast 4 detik berlalu sebelum `Verifikasi` toast hilang otomatis pada langkah 43.
- Urutan TC: TC-FA-LIC-169 dan TC-FA-LIC-170 (tanpa mutasi) lebih dulu, lalu TC-FA-LIC-175, TC-FA-LIC-172, TC-FA-LIC-171, TC-FA-LIC-178, dan TC-FA-LIC-174 yang masing-masing mengakhiri sesi dan dipulihkan fixture (S-10).
- TC-FA-LIC-175: klausa `tanpa log` pada judul TC dirujuk ke spec absence log (kelas g, S-05); spec ini mengasersi dialog blok, tidak ada toast sukses, dan daftar sesi.
- Temuan untuk QA:
  - TC-FA-LIC-175: Automation `Manual Only — (d) dua sesi paralel`; spec memakai sesi API Budi Santoso untuk mengakhiri sesinya dan satu sesi UI aktor. Email dan password Budi Santoso tidak tertulis di Pre-setup #14 (disediakan tim FE).
  - TC-FA-LIC-172: klausa `tanpa pengecekan idle` diasersi lewat keberhasilan Force Logout atas sesi dengan Last Activity berbeda (07:05 dan 09:36); TC tidak menyebut cara mengamati pengecekan idle.
  - TC-FA-LIC-174: precondition tidak menyebut Pre-setup untuk dua sesi Dewi Lestari; disediakan fixture penyetel tim FE/BE.
- Alasan di atas sekitar 35 langkah (60 langkah): semua blok satu topik (Force Logout pada Tab Concurrent User) dan berdiri sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah tambahan hanya pemulihan fixture sesi dan muat ulang.
