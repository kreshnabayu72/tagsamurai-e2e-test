---
id: TC-AUTH-SES-E2E-057-pencatatan-akun-akses-force-logout-dan-password
title: "Pencatatan Sesi karena App Access Dicabut, Admin Force-Logout, Change Password, Deactivate, dan Delete Account"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-194
  - TC-AUTH-SES-205
  - TC-AUTH-SES-206
  - TC-AUTH-SES-207
  - TC-AUTH-SES-208
  - TC-AUTH-SES-266
coverage:
  web: automated
  mobile: automated
---

# Pencatatan Sesi karena App Access Dicabut, Admin Force-Logout, Change Password, Deactivate, dan Delete Account

## Prerequisites

- Mode: FE+BE.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`; scope Client Alpha Logistik: Tabel Data Uji Pre-setup #1, scope Client Q2 untuk user milik Client Q2: Tabel Data Uji Pre-setup #26): enam user profil BASE (Tabel Data Uji Pre-setup #5 dan #12: Activated, Active ON, MFA dan Agreement tidak terpicu), password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-194: `Bayu Anggraini` (`bayuanggraini+{runId}-057@qwertysystem.net`), Client Alpha Logistik; sesi web Active di Browser A (Chrome on Windows) dengan sesi-produk Fixed Asset dan Supply Asset Active (App Access keduanya)
  - TC-AUTH-SES-205: `Nadia Ramadhan` (`nadiaramadhan+{runId}-057@qwertysystem.net`), Client Q2 dengan App Access Fixed Asset dan Supply Asset; sesi platform web Active dan sesi-produk Fixed Asset Active di Browser A
  - TC-AUTH-SES-266: `Irfan Damayanti` (`irfandamayanti+{runId}-057@qwertysystem.net`), Client Q2 dengan App Access Fixed Asset dan Supply Asset; sesi platform web Active dan sesi-produk Fixed Asset Active di Browser A
  - TC-AUTH-SES-208: `Budi Firmansyah` (`budifirmansyah+{runId}-057@qwertysystem.net`), Client Alpha Logistik; sesi web Active di Browser A dan sesi mobile Active di perangkat Android uji A (Tabel Data Uji Pre-setup #10; cara menyiapkan: Pre-setup #28) dengan sesi-produk Fixed Asset anak yang Active
  - TC-AUTH-SES-207: `Tari Hidayat` (`tarihidayat+{runId}-057@qwertysystem.net`), Client Alpha Logistik; sesi web Active di Browser A
  - TC-AUTH-SES-206: `Irfan Wulandari` (`irfanwulandari+{runId}-057@qwertysystem.net`), Client Alpha Logistik; sesi web Active di Browser A
- Konteks dan akun (dibuka di hook `before`, login pertama tiap konteks ada di hook):
  - Browser Admin: akun aktor Total Control (Global Settings) di atas dengan scope Client Alpha Logistik (Tabel Data Uji Pre-setup #1) dan scope Client Q2 (Tabel Data Uji Pre-setup #26; `Nadia Ramadhan` dan `Irfan Damayanti` milik Client Q2), dipakai mencabut App Access, menghapus dan menonaktifkan user, serta membaca `Global Settings > Activity Log > Session`, `Activity Log > Session` milik Fixed Asset, dan `Global Settings > User > Detail > User Log`.
  - Browser License: akun aktor `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #2 dan #33: Global Role Manage Global License, scope Client Alpha Logistik dan Client Q2), kredensial `Spectra.env.FA_MGL_PASSWORD`, dipakai di `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset).
  - Browser A (memuat sesi web seed milik user TC yang sedang berjalan) dan perangkat Android uji A (sesi mobile).
- Password: password lama user uji `Spectra.env.SES_PASSWORD`; password baru hasil Change Password `Spectra.env.SES_PASSWORD_NEW`.
- Hook `after`: akhiri semua sesi seed (web, mobile, sesi-produk), tutup konteks Browser A, Browser License, dan Browser Admin, hapus user yang masih ada (user `Irfan Wulandari` sudah terhapus oleh TC-AUTH-SES-206; pembersihan tidak gagal bila user tidak ditemukan). Pembersihan tidak berasumsi seeding berhasil penuh.
- Environment variable: `GS_TC_PASSWORD`, `FA_MGL_PASSWORD`, `SES_PASSWORD`, `SES_PASSWORD_NEW`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`); state global yang diubah: seat Fixed Asset Client Q2 (kuota 2) diisi sesi-produk seed (`Nadia Ramadhan` dan `Irfan Damayanti`, masing-masing 1 seat), dipulihkan di hook `after`; perangkat fisik Android uji A dipakai bersama (sesi mobile `Budi Firmansyah`).
- Kemampuan teknis: konteks browser bersamaan (Browser A, Browser Admin, Browser License); driver otomasi Android (aplikasi native) pada perangkat A; alamat IP uji yang berbeda antara Browser A (user) dan Browser Admin/Browser License (admin) supaya asersi "IP Address dari sesi yang di-invalidate, bukan IP admin" dapat dibuktikan; pembacaan stempel waktu entri log untuk membedakan entri baru dari entri seeding.
- Akun yang dipakai: user uji masing-masing TC di Browser A dan perangkat A; akun aktor di Browser Admin dan Browser License.
- Jeda nyata 10 detik pada TC-AUTH-SES-205 dan 266 menunggu push SSE ke Browser A; tidak ada jeda nyata lain.

## Test Steps

### TC-AUTH-SES-194: Pencatatan App Access dicabut

1. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Bayu Anggraini`
2. Di Browser Admin buka `Global Settings > User`, cari `Bayu Anggraini`, buka Detail, dan cabut App Access Fixed Asset
3. Di Browser A (sesi web Active `Bayu Anggraini`) amati halaman Portal — Product Hub dan buka card Supply Asset
4. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset) dan periksa daftar sesi aktif serta hitungan seat
5. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset dan cari entri untuk `Bayu Anggraini` yang dibuat sesudah langkah 2 dimulai
6. Verifikasi Entri baru tampil di `Activity Log > Session` milik Fixed Asset: Activity `Session`, Status `—`, Note `Session ended`
7. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Activity Log > Session` milik Fixed Asset
8. Verifikasi Entri itu memiliki kolom Date, User, IP Address, dan Device / Browser yang terisi
9. Buka `Global Settings > User > Detail > User Log` milik `Bayu Anggraini` dan cari entri yang dibuat sesudah langkah 2 dimulai
10. Verifikasi Entri baru tampil di `Global Settings > User > Detail > User Log`: Activity `Session`, Status `—`, Note `Session ended (Fixed Asset)`
11. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > User > Detail > User Log`
12. Verifikasi Entri itu memiliki kolom Date, IP Address, dan Device / Browser yang terisi (User Log tidak memiliki kolom User)

### TC-AUTH-SES-205: Pencatatan admin force-logout

13. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Nadia Ramadhan`
14. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset), pilih `Nadia Ramadhan`, lalu klik [Force Logout] dan [Confirm Logout] pada dialog konfirmasi "Force Logout User"
15. Di Browser A (sesi web Active `Nadia Ramadhan`) amati tanpa interaksi selama 10 detik (event push SSE)
16. Di Browser Admin buka `Activity Log > Session` milik Fixed Asset dan cari entri untuk `Nadia Ramadhan` yang dibuat sesudah langkah 14 dimulai
17. Verifikasi Entri baru tampil di `Activity Log > Session` milik Fixed Asset (row sesi-produk): Activity `Session`, Status `—`, Note `Logged out by admin`
18. Verifikasi IP Address entri berasal dari sesi yang di-invalidate (IP Browser A), bukan IP admin
19. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Activity Log > Session` milik Fixed Asset
20. Verifikasi Entri itu memiliki kolom Date, User, IP Address, dan Device / Browser yang terisi
21. Buka `Global Settings > User > Detail > User Log` milik `Nadia Ramadhan` dan cari entri sesi-produk yang dibuat sesudah langkah 14 dimulai
22. Verifikasi Entri baru tampil di `Global Settings > User > Detail > User Log`: Activity `Session`, Status `—`, Note `Logged out by admin (Fixed Asset)`
23. Verifikasi IP Address entri di User Log berasal dari sesi yang di-invalidate, bukan IP admin
24. Verifikasi Satu event menghasilkan satu entri sesi-produk (tidak ganda) di `Global Settings > User > Detail > User Log`
25. Verifikasi Entri itu memiliki kolom Date, IP Address, dan Device / Browser yang terisi (User Log tidak memiliki kolom User)

### TC-AUTH-SES-266: Pencatatan sesi platform yang berakhir karena admin force-logout

26. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Irfan Damayanti`
27. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset), pilih `Irfan Damayanti`, lalu klik [Force Logout] dan [Confirm Logout] pada dialog konfirmasi "Force Logout User"
28. Di Browser A (sesi web Active `Irfan Damayanti`) amati tanpa interaksi selama 10 detik (event push SSE)
29. Di Browser Admin buka `Global Settings > Activity Log > Session` dan cari entri untuk `Irfan Damayanti` yang dibuat sesudah langkah 27 dimulai
30. Verifikasi Entri baru tampil di `Global Settings > Activity Log > Session`: Activity `Logout`, Status `—`, Note `Logged out by admin`
31. Verifikasi IP Address entri di `Global Settings > Activity Log > Session` berasal dari sesi yang di-invalidate, bukan IP admin
32. Buka `Global Settings > User > Detail > User Log` milik `Irfan Damayanti` dan cari entri yang dibuat sesudah langkah 27 dimulai
33. Verifikasi Entri baru tampil di `Global Settings > User > Detail > User Log`: Activity `Logout`, Status `—`, Note `Logged out by admin`
34. Verifikasi IP Address entri di User Log berasal dari sesi yang di-invalidate, bukan IP admin
35. Buka `Activity Log > Session` milik Fixed Asset dan cari entri `Irfan Damayanti` yang dibuat sesudah langkah 27 dimulai
36. Verifikasi Entri sesi platform (Activity `Logout`) di `Global Settings > Activity Log > Session` terpisah dari entri sesi-produk (Activity `Session`) di `Activity Log > Session` milik Fixed Asset: dua row, bukan satu

### TC-AUTH-SES-208: Pencatatan Change Password meng-invalidate sesi lain

37. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Budi Firmansyah`
38. Di Browser A (sesi web Active `Budi Firmansyah`, Chrome on Windows) buka `Global Settings > My Profile > Change Password` → modal Change Password tampil
39. Ketik `Spectra.env.SES_PASSWORD` pada field Current Password
40. Ketik `Spectra.env.SES_PASSWORD_NEW` pada field New Password
41. Ketik `Spectra.env.SES_PASSWORD_NEW` pada field Confirm New Password
42. Klik [Save] → password berhasil diubah
43. Di Browser A klik menu lain
44. Tutup aplikasi sebelumnya di perangkat Android uji A dan buka aplikasi dengan memuat sesi mobile seed milik `Budi Firmansyah`
45. Di perangkat Android uji A (aplikasi memuat sesi mobile Active `Budi Firmansyah`) ketuk layar → Dialog muncul
46. Di Browser Admin buka `Global Settings > Activity Log > Session` dan cari entri untuk `Budi Firmansyah` yang dibuat sesudah langkah 38 dimulai
47. Verifikasi Entri baru tampil di `Global Settings > Activity Log > Session`: Activity `Logout`, Status `—`, Note `Logged out (password changed)`
48. Verifikasi Tepat satu entri `Logged out (password changed)` per sesi platform yang berakhir (sesi mobile)
49. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > Activity Log > Session`
50. Verifikasi Entri itu memiliki kolom Date, User, IP Address, dan Device / Browser yang terisi
51. Buka `Global Settings > User > Detail > User Log` milik `Budi Firmansyah` dan cari entri yang dibuat sesudah langkah 38 dimulai
52. Verifikasi Entri baru tampil di `Global Settings > User > Detail > User Log`: Activity `Logout`, Status `—`, Note `Logged out (password changed)`
53. Verifikasi Tampil `Session ended` per sesi-produk anak dari sesi mobile yang berakhir (`Session ended (Fixed Asset)`)
54. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > User > Detail > User Log`
55. Verifikasi Entri itu memiliki kolom Date, IP Address, dan Device / Browser yang terisi (User Log tidak memiliki kolom User)

### TC-AUTH-SES-207: Pencatatan deactivate account

56. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Tari Hidayat`
57. Di Browser Admin buka `Global Settings > User`, cari `Tari Hidayat`, dan matikan Toggle Active
58. Di Browser A (sesi web Active `Tari Hidayat`) amati layar
59. Di Browser A klik [OK] pada dialog yang tampil
60. Di Browser Admin buka `Global Settings > Activity Log > Session` dan cari entri untuk `Tari Hidayat` yang dibuat sesudah langkah 57 dimulai
61. Verifikasi Entri baru tampil di `Global Settings > Activity Log > Session`: Activity `Logout`, Status `—`, Note `Account deactivated`
62. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > Activity Log > Session`
63. Verifikasi Entri itu memiliki kolom Date, User, IP Address, dan Device / Browser yang terisi
64. Buka `Global Settings > User > Detail > User Log` milik `Tari Hidayat` dan cari entri yang dibuat sesudah langkah 57 dimulai
65. Verifikasi Entri baru tampil di `Global Settings > User > Detail > User Log`: Activity `Logout`, Status `—`, Note `Account deactivated`
66. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > User > Detail > User Log`
67. Verifikasi Entri itu memiliki kolom Date, IP Address, dan Device / Browser yang terisi (User Log tidak memiliki kolom User)

### TC-AUTH-SES-206: Pencatatan delete account

68. Tutup konteks Browser A sebelumnya dan buka konteks baru Browser A dengan memuat sesi web seed milik `Irfan Wulandari`
69. Di Browser Admin buka `Global Settings > User`, cari `Irfan Wulandari`, dan hapus user sampai konfirmasi selesai
70. Di Browser A (sesi web Active `Irfan Wulandari`) amati layar
71. Di Browser Admin buka `Global Settings > Activity Log > Session` dan cari entri untuk `Irfan Wulandari` yang dibuat sesudah langkah 69 dimulai
72. Verifikasi Entri baru tampil di `Global Settings > Activity Log > Session`: Activity `Logout`, Status `—`, Note `Account deleted`
73. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di `Global Settings > Activity Log > Session`
74. Verifikasi Entri itu memiliki kolom Date, User, IP Address, dan Device / Browser yang terisi
75. Buka User Log milik `Irfan Wulandari` dan cari entri yang dibuat sesudah langkah 69 dimulai
76. Verifikasi Entri baru tampil di User Log: Activity `Logout`, Status `—`, Note `Account deleted`
77. Verifikasi Satu event menghasilkan satu entri (tidak ganda) di User Log
78. Verifikasi Entri itu memiliki kolom Date, IP Address, dan Device / Browser yang terisi (User Log tidak memiliki kolom User)

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Kelas harness: pencatatan (Status/Note spesifik) dibaca lewat akun aktor di Browser Admin; asersi absence ada di spec `TC-AUTH-SES-E2E-060-absence-pencatatan-sesi`. Seluruh TC batch ini memerlukan beberapa konteks bersamaan (multi-konteks) sesuai rencana yang disetujui.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini 194, 205, 266, 208, 207, 206 (urutan TC sumber 194, 205, 206, 207, 208, 266). TC-AUTH-SES-206 (hapus akun) ditaruh paling akhir karena aksi merusak data; 207 (nonaktifkan) sebelum 206. Tiap TC memakai user sendiri, jadi urutan tidak membuat TC saling bergantung.
- Pembagian TC lintas spec (prinsip 10): TC-AUTH-SES-182 (alur Change Password) diuji di spec `TC-AUTH-SES-E2E-055-change-dan-reset-password-meng-invalidate-sesi`; spec ini menyalin langkahnya (langkah 38–45) sebagai dependensi TC-AUTH-SES-208 dan mengasersi pencatatannya (LOG-20). Asersi hasil dependensi (dialog, status sesi, seat, halaman Login) diuji di spec pemilik TC dependensi (TC-AUTH-SES-72, 88, 90, 133, 182).
- Langkah dependensi disalin (S-04): TC-AUTH-SES-194 dari TC-AUTH-SES-72 (langkah 2–4, termasuk pembacaan Concurrent User); TC-AUTH-SES-205 dan 266 dari TC-AUTH-SES-133 (langkah 14–15 dan 27–28); TC-AUTH-SES-206 dari TC-AUTH-SES-88 (langkah 69–70); TC-AUTH-SES-207 dari TC-AUTH-SES-90 (langkah 57–59); TC-AUTH-SES-208 dari TC-AUTH-SES-182 (langkah 38–45).
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): perpindahan antar konteks dan perangkat; mengamati Browser A tanpa interaksi 10 detik agar event push SSE tiba. Entri "baru" dibedakan dari entri seeding lewat stempel waktu: hanya entri yang dibuat sesudah langkah pembuka TC itu yang dihitung.
- Temuan untuk QA:
  - TC-AUTH-SES-206 Expected butir a menyebut entri juga di User Log milik `Irfan Wulandari`, tetapi user sudah terhapus sehingga halaman `Global Settings > User > Detail > User Log`-nya mungkin tidak dapat dibuka; Langkah Uji hanya membuka `Global Settings > Activity Log > Session`. Spec mengikuti Expected (langkah 75–78) tanpa menetapkan jalur akses User Log user terhapus.
  - TC-AUTH-SES-205 dan 266 menulis user `Nadia Ramadhan`/`Irfan Damayanti` milik Client Alpha, sedangkan dependensi TC-AUTH-SES-133 memakai user Client Q2 dan akun Manage Global License di Client Q2; spec memakai Client Q2 untuk kedua user, membutuhkan akun Manage Global License yang berlaku di Client Alpha dan Client Q2 (TC-AUTH-SES-72 memakai akun yang sama untuk Client Alpha; Pre-setup #33), dan akun Total Control dengan scope Client Q2 (Pre-setup #26) di samping scope Client Alpha (Pre-setup #1) karena TC memakai Pre-setup #1 untuk semua user.
  - TC-AUTH-SES-208 Expected menyebut `Session ended` per sesi-produk anak tetapi precondition tidak menyebut sesi-produk; spec men-seed sesi-produk Fixed Asset anak pada sesi mobile `Budi Firmansyah`. Expected tidak menyebut surface mana yang memuat `Session ended`; spec mengasersinya di User Log (suffix produk).
  - TC-AUTH-SES-266 Expected butir b menyebut dua row (platform dan sesi-produk) tanpa menyebut pembacaan di `Activity Log > Session` milik Fixed Asset di Langkah Uji; spec menambah langkah 35 (S-14).
  - TC-AUTH-SES-194, 205 membaca `Activity Log > Session` milik Fixed Asset dengan akun Total Control Global Settings; akses akun itu ke Activity Log produk (forward-dependency PRD §12 #3) tidak dinyatakan di TC.
  - Kolom "User" pada Expected butir b TC batch ini tidak ada di surface User Log (PRD §8 surface #3); spec mengasersi kolom User hanya di surface yang memilikinya. PRD §9.8 LOG-18/19/20 menulis Status `Failed`, sedangkan TC dan PRD §8 menulis `—`; spec mengikuti TC.
  - TC-AUTH-SES-207 dan 206 tidak menyebut teks dialog di Browser A; asersi dialog diuji di spec pemilik TC-AUTH-SES-88 dan 90.
- Langkah penghubung ganti akun (S-03, S-07): tiap TC membuka konteks baru Browser A dengan sesi web seed milik user TC itu (dan memuat sesi mobile seed di perangkat Android uji A pada TC-AUTH-SES-208), tanpa awalan `Verifikasi`.
