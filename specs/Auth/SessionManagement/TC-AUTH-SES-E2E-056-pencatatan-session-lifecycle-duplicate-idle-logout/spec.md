---
id: TC-AUTH-SES-E2E-056-pencatatan-session-lifecycle-duplicate-idle-logout
title: "Pencatatan Session Lifecycle: Duplicate Login, Idle Expired Web dan Mobile, Sesi Mobile Digantikan, dan Manual Logout"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-189
  - TC-AUTH-SES-191
  - TC-AUTH-SES-192
  - TC-AUTH-SES-193
  - TC-AUTH-SES-197
coverage:
  web: automated
  mobile: automated
---

# Pencatatan Session Lifecycle: Duplicate Login, Idle Expired Web dan Mobile, Sesi Mobile Digantikan, dan Manual Logout

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): lima user profil BASE milik Client Alpha Logistik (Tabel Data Uji Pre-setup #5 dan #11: batas idle 15 menit; subscription Fixed Asset dan Supply Asset Active, kuota 5; user Activated, Active ON; MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-189: `Lestari Puspita` (`lestaripuspita+{runId}-056@qwertysystem.net`); sesi web Active di Browser A (Chrome on Windows); Browser B (Firefox on macOS) belum login
  - TC-AUTH-SES-193: `Wulan Rahayu` (`wulanrahayu+{runId}-056@qwertysystem.net`); sesi mobile Active di perangkat Android uji A (Tabel Data Uji Pre-setup #10; cara menyiapkan: Pre-setup #28) dengan sesi-produk Fixed Asset anak yang Active
  - TC-AUTH-SES-197: `Citra Maulana` (`citramaulana+{runId}-056@qwertysystem.net`); sesi web Active di Browser A (Chrome on Windows)
  - TC-AUTH-SES-191: `Putri Firmansyah` (`putrifirmansyah+{runId}-056@qwertysystem.net`); sesi web Active di Browser A pada Portal — Product Hub
  - TC-AUTH-SES-192: `Eko Damayanti` (`ekodamayanti+{runId}-056@qwertysystem.net`); tanpa sesi aktif (sesi mobile dibuat oleh langkah login di TC)
- Konteks dan akun (dibuka di hook `before`, login pertama tiap konteks ada di hook): Browser Admin dengan akun aktor Total Control (Global Settings) di atas, dipakai membaca `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log`; Browser A dan Browser B untuk sesi web user uji (Browser A memuat sesi web seed milik user TC yang sedang berjalan); perangkat Android uji A untuk sesi mobile.
- Suite berjalan serial (`parallel: false`); state global yang diubah: jam server dan jam browser/perangkat, diatur bersama (digeser oleh TC-AUTH-SES-193, 191, dan 192), dipulihkan di hook `after` dan dikembalikan ke waktu normal di langkah TC sebelum akun aktor membuka Activity Log atau User Log. Karena pergeseran kumulatif melewati batas idle 15 menit, akun aktor di Browser Admin login ulang di langkah penghubung pada TC-AUTH-SES-191 dan 192.
- Jeda nyata 10 detik pada TC-AUTH-SES-189 menunggu push SSE ke Browser A; tidak ada jeda nyata lain.
- Pergeseran jam TC-AUTH-SES-193 bernilai tetap 90 detik (lebih dari batas 60 detik tanpa heartbeat pada precondition TC-AUTH-SES-70). Nilai pembanding Date entri `Session expired` pada TC-AUTH-SES-193 adalah waktu login menurut jam server yang dimajukan (dicatat di langkah 28), dengan toleransi 5 detik; waktu app-kill (langkah 26) lebih awal sekitar 90 detik sehingga berada di luar toleransi.
- Hook `after`: akhiri semua sesi seed (web, mobile, sesi-produk), tutup konteks Browser A, Browser B, dan Browser Admin, hapus kelima user. Pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua konteks browser bersamaan dengan user agent yang dapat ditetapkan (Chrome on Windows, Firefox on macOS) serta Browser Admin sebagai konteks ketiga; driver otomasi Android (aplikasi native) termasuk menghapus aplikasi dari recent apps (app-kill) dan mencatat waktunya; pengatur waktu (Tabel Data Uji Pre-setup #18) yang memajukan dan memulihkan jam server dan jam browser/perangkat bersama serta menampilkan pembacaan jam server yang dimajukan; pembacaan stempel waktu entri log untuk membedakan entri baru dari entri seeding; reCAPTCHA mode uji di environment untuk login web (halaman Login with Password).
- Akun yang dipakai: user uji masing-masing TC di Browser A, Browser B, dan perangkat Android uji A; akun aktor di Browser Admin.

## Test Steps

### TC-AUTH-SES-189: Pencatatan Duplicate Login: device lama ter-logout

1. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Lestari Puspita`
2. Di Browser B (Firefox on macOS) buka `Auth > Login with Password` → halaman Login with Password tampil
3. Ketik email `lestaripuspita+{runId}-056@qwertysystem.net` dan password `Spectra.env.SES_PASSWORD`, lalu klik [Log in] → Dialog Duplicate Login Attempt muncul
4. Klik [Confirm] pada Dialog Duplicate Login Attempt → Browser B masuk Portal — Product Hub
5. Pindah ke Browser A dan amati tanpa interaksi selama 10 detik (event push SSE)
6. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Lestari Puspita` yang dibuat sesudah langkah 2 dimulai
7. Verifikasi Entri baru tampil di `Global Settings > Activity Log > Session`: Activity `Logout`, Status `—`, Note `Logged out (new device login)`
8. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > Activity Log > Session`
9. Verifikasi Entri itu memiliki kolom Date, User, IP Address, dan Device / Browser yang terisi
10. Buka `Global Settings > User > Detail > User Log` milik `Lestari Puspita` dan cari entri yang dibuat sesudah langkah 2 dimulai
11. Verifikasi Entri baru tampil di `Global Settings > User > Detail > User Log`: Activity `Logout`, Status `—`, Note `Logged out (new device login)`
12. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > User > Detail > User Log`
13. Verifikasi Entri itu memiliki kolom Date, IP Address, dan Device / Browser yang terisi (User Log tidak memiliki kolom User)

### TC-AUTH-SES-197: Pencatatan Manual Logout

14. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Citra Maulana`
15. Di Browser A (Chrome on Windows, sesi web Active `Citra Maulana`) klik menu Profile di navbar lalu pilih Log Out → Browser A diarahkan ke halaman Login with Password
16. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Citra Maulana` yang dibuat sesudah langkah 15 dimulai
17. Verifikasi Entri baru tampil di `Global Settings > Activity Log > Session`: Activity `Logout`, Status `—`, Note `Logged out`
18. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > Activity Log > Session`
19. Verifikasi Entri itu memiliki kolom Date, User, IP Address, dan Device / Browser yang terisi
20. Buka `Global Settings > User > Detail > User Log` milik `Citra Maulana` dan cari entri yang dibuat sesudah langkah 15 dimulai
21. Verifikasi Entri baru tampil di `Global Settings > User > Detail > User Log`: Activity `Logout`, Status `—`, Note `Logged out`
22. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > User > Detail > User Log`
23. Verifikasi Entri itu memiliki kolom Date, IP Address, dan Device / Browser yang terisi (User Log tidak memiliki kolom User)

### TC-AUTH-SES-193: Pencatatan sesi mobile yang digantikan login baru dari perangkat yang sama

24. Di Browser Admin buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Wulan Rahayu`, lalu catat jumlah entri Note `Session expired` sebagai baseline
25. Tutup aplikasi sebelumnya di perangkat Android uji A dan buka aplikasi dengan memuat sesi mobile seed milik `Wulan Rahayu`
26. Di perangkat Android uji A hapus aplikasi mobile dari recent apps (app-kill) saat sesi mobile `Wulan Rahayu` masih berstatus Active, lalu catat waktunya
27. Majukan jam server dan jam browser/perangkat bersama 90 detik tanpa heartbeat dari perangkat A
28. Buka aplikasi mobile di perangkat Android uji A dan login sebagai `wulanrahayu+{runId}-056@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD` → Portal — Product Hub tampil, lalu catat waktu login menurut jam server yang dimajukan
29. Kembalikan jam server dan jam browser/perangkat uji ke waktu normal
30. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Wulan Rahayu` (`wulanrahayu+{runId}-056@qwertysystem.net`) dengan Note `Session expired`
31. Verifikasi Entri baru tampil di `Global Settings > Activity Log > Session`: Activity `Logout`, Status `—`, Note `Session expired` (jumlah entri Note `Session expired` bertambah 1 dibanding baseline)
32. Verifikasi Entri ditulis saat penggantian sesi: Date entri sama dengan waktu login yang dicatat pada langkah 28 (menurut jam server yang dimajukan) dengan toleransi 5 detik, dan berbeda sekitar 90 detik dari waktu app-kill pada langkah 26
33. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > Activity Log > Session`
34. Verifikasi Entri itu memiliki kolom Date, User, IP Address, dan Device / Browser yang terisi
35. Buka `Global Settings > User > Detail > User Log` milik `Wulan Rahayu` dan cari entri dengan Note `Session expired`
36. Verifikasi Entri baru tampil di `Global Settings > User > Detail > User Log`: Activity `Logout`, Status `—`, Note `Session expired` (jumlah entri Note `Session expired` bertambah 1 dibanding baseline)
37. Verifikasi Entri di User Log ditulis saat penggantian sesi: Date entri sama dengan waktu login yang dicatat pada langkah 28 (menurut jam server yang dimajukan) dengan toleransi 5 detik, dan berbeda sekitar 90 detik dari waktu app-kill pada langkah 26
38. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > User > Detail > User Log`
39. Verifikasi Entri itu memiliki kolom Date, IP Address, dan Device / Browser yang terisi (User Log tidak memiliki kolom User)

### TC-AUTH-SES-191: Pencatatan idle web expired

40. Di Browser Admin buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Putri Firmansyah`, lalu catat jumlah entri Note `Session expired` sebagai baseline
41. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Putri Firmansyah`
42. Di Browser A (sesi web Active `Putri Firmansyah` di Portal — Product Hub; batas idle 15 menit) biarkan tanpa aktivitas dan majukan jam server dan jam browser/perangkat bersama 10 menit → amati Toast
43. Majukan jam server dan jam browser/perangkat bersama 6 menit lagi (idle 16 menit) → Dialog Session Expired muncul
44. Coba klik tombol atau menu di halaman di belakang dialog
45. Kembalikan jam server dan jam browser/perangkat uji ke waktu normal
46. Di Browser Admin login ulang dengan akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dan password `Spectra.env.GS_TC_PASSWORD`, lalu klik [Log in] (sesi aktor melewati batas idle karena jam digeser)
47. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Putri Firmansyah` (`putrifirmansyah+{runId}-056@qwertysystem.net`) dengan Note `Session expired`
48. Verifikasi Entri baru tampil di `Global Settings > Activity Log > Session`: Activity `Logout`, Status `—`, Note `Session expired` (jumlah entri Note `Session expired` bertambah 1 dibanding baseline)
49. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > Activity Log > Session`
50. Verifikasi Entri itu memiliki kolom Date, User, IP Address, dan Device / Browser yang terisi
51. Buka `Global Settings > User > Detail > User Log` milik `Putri Firmansyah` dan cari entri dengan Note `Session expired`
52. Verifikasi Entri baru tampil di `Global Settings > User > Detail > User Log`: Activity `Logout`, Status `—`, Note `Session expired` (jumlah entri Note `Session expired` bertambah 1 dibanding baseline)
53. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > User > Detail > User Log`
54. Verifikasi Entri itu memiliki kolom Date, IP Address, dan Device / Browser yang terisi (User Log tidak memiliki kolom User)

### TC-AUTH-SES-192: Pencatatan idle mobile expired

55. Di Browser Admin buka `Global Settings > Activity Log > Session` dan `Global Settings > User > Detail > User Log` milik `Eko Damayanti`, lalu catat jumlah entri Note `Session expired` sebagai baseline
56. Tutup aplikasi sebelumnya di perangkat Android uji A dan hapus data aplikasinya agar login berikutnya bukan lanjutan sesi user sebelumnya
57. Buka aplikasi mobile di perangkat Android uji A, login sebagai `ekodamayanti+{runId}-056@qwertysystem.net` dengan password `Spectra.env.SES_PASSWORD`, dan masuk Portal — Product Hub
58. Biarkan app di foreground tanpa sentuhan dan majukan jam server dan jam browser/perangkat bersama 16 menit
59. Ketuk layar → Dialog Session Expired muncul
60. Ketuk [OK] → app diarahkan ke halaman Login
61. Kembalikan jam server dan jam browser/perangkat uji ke waktu normal
62. Di Browser Admin login ulang dengan akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` dan password `Spectra.env.GS_TC_PASSWORD`, lalu klik [Log in] (sesi aktor melewati batas idle karena jam digeser)
63. Pindah ke Browser Admin, buka `Global Settings > Activity Log > Session`, dan cari entri untuk `Eko Damayanti` (`ekodamayanti+{runId}-056@qwertysystem.net`) dengan Note `Session expired`
64. Verifikasi Entri baru tampil di `Global Settings > Activity Log > Session`: Activity `Logout`, Status `—`, Note `Session expired` (jumlah entri Note `Session expired` bertambah 1 dibanding baseline)
65. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > Activity Log > Session`
66. Verifikasi Entri itu memiliki kolom Date, User, IP Address, dan Device / Browser yang terisi
67. Buka `Global Settings > User > Detail > User Log` milik `Eko Damayanti` dan cari entri dengan Note `Session expired`
68. Verifikasi Entri baru tampil di `Global Settings > User > Detail > User Log`: Activity `Logout`, Status `—`, Note `Session expired` (jumlah entri Note `Session expired` bertambah 1 dibanding baseline)
69. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > User > Detail > User Log`
70. Verifikasi Entri itu memiliki kolom Date, IP Address, dan Device / Browser yang terisi (User Log tidak memiliki kolom User)

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness: pencatatan (Status/Note spesifik) dibaca lewat akun aktor di Browser Admin; asersi absence ada di spec `TC-AUTH-SES-E2E-060-absence-pencatatan-sesi`. Pergeseran jam pada TC-AUTH-SES-191 dan 192 adalah langkah rutin pemicu state yang dibaca di log (konvensi bagian 6, bukan pemisah kelas d), dan Browser B pada TC-AUTH-SES-189 hanya pemicu state (`P-2`); TC-AUTH-SES-191 dan 192 yang menggeser jam server ditaruh paling akhir.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini 189, 197, 193, 191, 192 (urutan TC sumber 189, 191, 192, 193, 197). TC yang menggeser jam server (191, 192) ditaruh di akhir supaya pergeseran 16 menit tidak meng-expire sesi seed TC lain. Tiap TC memakai user sendiri, jadi urutan tidak membuat TC saling bergantung.
- Langkah dependensi disalin (S-04): TC-AUTH-SES-189 dari TC-AUTH-SES-26 (langkah 2–5, termasuk amati Browser A 10 detik); TC-AUTH-SES-197 dari TC-AUTH-SES-140 (langkah 15); TC-AUTH-SES-193 dari TC-AUTH-SES-70 (langkah 26–28, dengan app-kill dan tunggu 60 detik dari precondition TC-AUTH-SES-70); TC-AUTH-SES-191 dari TC-AUTH-SES-46 (langkah 42–44; Toast Idle Warning pada TC-AUTH-SES-44 tidak diasersi di sini); TC-AUTH-SES-192 dari TC-AUTH-SES-63 (langkah 57–60). Asersi hasil dependensi (dialog, status sesi, halaman Login) diuji di spec pemilik TC dependensi masing-masing.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): perpindahan antar Browser A, B, Admin dan perangkat A; app-kill dan memajukan jam 90 detik (langkah 26–27); mencatat waktu login menurut jam server yang dimajukan (langkah 28); mengembalikan jam server ke waktu normal (langkah 29, 45, dan 61; hook `after` sebagai cadangan, S-09). Entri "baru" dibedakan dari entri seeding lewat stempel waktu: hanya entri yang dibuat sesudah langkah pembuka TC itu yang dihitung.
- Temuan untuk QA:
  - Kolom "User" pada Expected butir b di semua TC batch ini tidak ada di surface `Global Settings > User > Detail > User Log` (PRD §8 surface #3 hanya memuat Date, Activity, Status, Note, IP Address, Device / Browser); spec mengasersi kolom User hanya di `Global Settings > Activity Log > Session`.
  - PRD §9.8 LOG-01, 03, 04, 05, 09 menulis Status `Failed`/`Success`, sedangkan TC dan PRD §8 menulis Status `—` untuk Activity `Logout`; spec mengikuti TC.
  - TC-AUTH-SES-192 (dependensi TC-AUTH-SES-63) menulis precondition "sesi mobile aktif" tetapi Langkah Uji TC-AUTH-SES-63 login dari awal; spec tidak men-seed sesi mobile untuk `Eko Damayanti` dan login di langkah 57.
  - TC-AUTH-SES-193 menyebut "ditulis saat penggantian, bukan saat app dibunuh" tanpa cara membedakannya di UI; spec membandingkan Date entri dengan waktu login yang dicatat (langkah 28, toleransi 5 detik) dan waktu app-kill (langkah 26).
  - TC-AUTH-SES-189, 191, 192, 193, 197 menulis akun pembaca log tanpa menyebut klien tempat akun aktor berada; spec mengasumsikan akun aktor dapat membaca log user Client Alpha Logistik.
  - TC sumber menulis "login" tanpa menyebut tombol maupun widget reCAPTCHA pada halaman Login with Password; spec memakai tombol [Log in] sesuai label web TC lain dan mengandalkan reCAPTCHA mode uji di environment (Prerequisites).
- Baseline entri log dan jam (S-09, S-12): TC-AUTH-SES-193, 191, dan 192 mencatat jumlah entri Note `Session expired` milik user TC di Activity Log > Session dan User Log sebagai aksi tanpa `Verifikasi` sebelum aksi, dan asersi entri baru berarti jumlah bertambah 1 dibanding baseline itu. Jam server dan jam browser/perangkat dimajukan bersama dan dikembalikan sebelum akun aktor membuka log. Login ulang akun aktor di Browser Admin (TC-AUTH-SES-191 dan 192) dan langkah penghubung ganti akun di Browser A dan perangkat Android uji A adalah aksi tanpa `Verifikasi` (S-03, S-07).
