---
id: TC-AUTH-SES-E2E-042-admin-force-logout-license-concurrent-user
title: "Admin Force-Logout di License > Concurrent User"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AUTH-SES-133
  - TC-AUTH-SES-134
  - TC-AUTH-SES-136
  - TC-AUTH-SES-138
  - TC-AUTH-SES-322
coverage:
  web: automated
---

# Admin Force-Logout di License > Concurrent User

## Prerequisites

- Mode: FE+BE.
- Client Q2 (Tabel Data Uji Pre-setup #12): subscription Fixed Asset dan Supply Asset Active; batas idle 15 menit. Kuota concurrent Fixed Asset dinaikkan dari 2 ke 8 di hook `before` lewat `Admin Console > License Allocation` oleh akun aktor principal Admin Console (Tabel Data Uji Pre-setup #4) `principalAdminConsole_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.AC_PRINCIPAL_PASSWORD`, supaya seluruh sesi-produk seed dan sesi-produk akun admin dapat aktif bersamaan; dipulihkan ke 2 di hook `after`.
- Akun aktor utama spec ini: Admin License `manageGlobalLicenseFixedAsset_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup #2, Global Role Manage Global License di Client Q2), kredensial `Spectra.env.FA_MGL_PASSWORD`. Login di hook `before` pada Browser License; akun ini juga memegang sesi-produk Fixed Asset Active (dibuat di `before` lewat pembukaan Fixed Asset) untuk TC-AUTH-SES-322.
- Seeding (hook `before`, lewat API oleh akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`): empat user profil BASE (Activated, Active ON, MFA dan Agreement tidak terpicu) milik Client Q2 dengan App Access Fixed Asset dan Supply Asset, password `Spectra.env.SES_PASSWORD`, email bersuffix per run:
  - TC-AUTH-SES-133: `Wulan Hidayat` (`wulanhidayat+{runId}-042@qwertysystem.net`); sesi platform web Active dan sesi-produk Fixed Asset Active di Browser A.
  - TC-AUTH-SES-134: `Bayu Utami` (`bayuutami+{runId}-042@qwertysystem.net`); sesi platform web Active dan sesi-produk Fixed Asset Active di Browser A.
  - TC-AUTH-SES-138: `Yoga Damayanti` (`yogadamayanti+{runId}-042@qwertysystem.net`); sesi web Active di Browser A (Chrome on Windows), sesi-produk Fixed Asset dan Supply Asset Active.
  - TC-AUTH-SES-136: `Joko Saputra` (`jokosaputra+{runId}-042@qwertysystem.net`); sesi platform web Active dan sesi-produk Fixed Asset Active (tanpa konteks browser yang terbuka).
  - Browser A tiap TC = konteks browser yang memuat sesi platform user TC bersangkutan (satu konteks per user, dibuat di `before` lewat login API).
- Browser Admin: akun aktor Total Control (Global Settings) dengan scope Client Q2 (Tabel Data Uji Pre-setup #26) di atas (`Spectra.env.GS_TC_PASSWORD`), membaca `Global Settings > Activity Log > Session` (TC-AUTH-SES-138).
- Hook `after` (tetap jalan walau spec gagal, tidak berasumsi seeding berhasil penuh): kembalikan jam server uji ke waktu nyata, pulihkan kuota Fixed Asset Client Q2 ke 2, akhiri semua sesi seed dan sesi-produk (termasuk sesi-produk akun admin), tutup semua konteks browser, hapus keempat user. Sesi Browser License dipulihkan atau dibuat ulang sebagai sesi default suite.
- Suite berjalan serial (`parallel: false`); state global yang diubah: kuota Fixed Asset Client Q2 serta jam server dan jam browser/perangkat (diatur bersama, hanya pada TC-AUTH-SES-136), dipulihkan di hook `after`.
- Jeda nyata: 10 detik untuk menunggu event push SSE (langkah 11 dan 20); tidak ada jeda nyata lain, pemajuan jam pada TC-AUTH-SES-136 tidak menunggu waktu nyata.
- Environment variable: `GS_TC_PASSWORD`, `AC_PRINCIPAL_PASSWORD`, `FA_MGL_PASSWORD`, `SES_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: dua sampai tiga konteks browser bersamaan (Browser License, Browser A, Browser Admin); penerimaan push SSE di web; jam server dan jam browser/perangkat dapat diatur bersama dan dipulihkan ke waktu nyata, dan sesi admin dapat disegarkan di antara dua kali pemajuan lewat sinyal aktivitas (gerak kursor di Browser License) sehingga heartbeat terkirim dan responsnya diterima (TC-AUTH-SES-136); pembacaan status sesi platform dan sesi-produk milik user uji dari sisi backend, hitungan seat, dan respons API force-logout, disediakan tim FE/BE tanpa endpoint tertentu; pengamatan penerimaan push dan dialog di sisi `Joko Saputra` (sesi tanpa konteks browser yang terbuka), disediakan tim FE/BE tanpa endpoint tertentu (TC-AUTH-SES-136); pengiriman request langsung ke `POST /v2/iam/auth/product-sessions/{id}/force-logout` (Auth - Session Management) dengan header `X-Session-ID` sesi platform akun admin (TC-AUTH-SES-322).
- Akun yang dipakai: akun admin `manageGlobalLicenseFixedAsset` pada Browser License untuk seluruh aksi force-logout; user uji pada Browser A sebagai target.

## Test Steps

### TC-AUTH-SES-322: Admin yang me-force-logout dirinya sendiri ditolak 403

1. Kirim request langsung `POST /v2/iam/auth/product-sessions/{id}/force-logout` dengan header `X-Session-ID` berisi ID sesi platform akun admin `manageGlobalLicenseFixedAsset` dan `{id}` berisi ID sesi-produk Fixed Asset Active milik akun admin itu sendiri (target: diri sendiri)
2. Verifikasi Server menolak request dengan 403
3. Verifikasi Tidak ada dialog khusus yang tampil di Browser License
4. Verifikasi Sesi admin (sesi platform dan sesi-produk Fixed Asset akun admin) tetap Active

### TC-AUTH-SES-133: Admin force-logout user di License > Concurrent User mengakhiri sesi-produk dan sesi platform target

5. Di Browser License buka `PLATFORM SETTINGS > License > Concurrent User` (Fixed Asset)
6. Pilih baris `Wulan Hidayat`
7. Klik [Force Logout] → dialog konfirmasi "Force Logout User" muncul
8. Verifikasi Dialog konfirmasi "Force Logout User" tampil sesuai `fixed-asset/license/PRD/license.md` §3.2
9. Klik [Confirm Logout]
10. Verifikasi Toast sukses tampil sesuai `fixed-asset/license/PRD/license.md` §3.2
11. Di Browser A (sesi `Wulan Hidayat`) amati tanpa interaksi selama 10 detik (event push SSE)
12. Verifikasi Sesi-produk Fixed Asset `Wulan Hidayat` berstatus Force Logged Out
13. Verifikasi Seat dilepas
14. Verifikasi Sesi platform web `Wulan Hidayat` berstatus Force Logged Out (cascade)
15. Verifikasi Dialog "Log Out" tampil di Browser A
16. Verifikasi Dialog "Log Out" di Browser A memuat Body "You have been logged out by an administrator."

### TC-AUTH-SES-134: OK pada Dialog Log Out mengarah ke Login dan user harus login ulang

17. Di Browser License muat ulang daftar License > Concurrent User dan pilih baris `Bayu Utami`
18. Klik [Force Logout] → dialog konfirmasi "Force Logout User" muncul
19. Klik [Confirm Logout]
20. Di Browser A (sesi `Bayu Utami`) amati tanpa interaksi selama 10 detik → Dialog "Log Out" muncul
21. Klik [OK]
22. Verifikasi Browser A diarahkan ke halaman Login
23. Di Browser A buka langsung URL halaman produk Fixed Asset tanpa login ulang
24. Verifikasi Halaman produk tidak dapat diakses tanpa login ulang

### TC-AUTH-SES-138: Force-logout memutus juga sesi-produk produk lain milik sesi platform yang berakhir

25. Di Browser Admin catat baseline jumlah entri `Session ended` `Yoga Damayanti` di `Global Settings > Activity Log > Session`; di Browser License muat ulang daftar License > Concurrent User (Fixed Asset) dan pilih baris `Yoga Damayanti`
26. Klik [Force Logout] → dialog konfirmasi "Force Logout User" muncul
27. Klik [Confirm Logout]
28. Verifikasi Sesi-produk Fixed Asset `Yoga Damayanti` berakhir (cascade dari sesi platform)
29. Verifikasi Sesi-produk Supply Asset `Yoga Damayanti` berakhir (cascade dari sesi platform)
30. Verifikasi Seat Fixed Asset dilepas
31. Verifikasi Seat Supply Asset dilepas
32. Di Browser Admin buka `Global Settings > Activity Log > Session`
33. Verifikasi Entri `Session ended` untuk `Yoga Damayanti` (dicari berdasarkan Note dan email) bertambah 2 dari baseline, satu per sesi-produk anak (Fixed Asset dan Supply Asset)

### TC-AUTH-SES-136: Force-logout terhadap sesi target yang sudah expired bersifat idempotent

34. Di Browser License muat ulang daftar License > Concurrent User sehingga baris `Joko Saputra` tampil (daftar tetap terbuka dan tidak dimuat ulang sesudahnya)
35. Majukan jam server dan jam browser/perangkat bersama 8 menit
36. Gerakkan kursor di Browser License (sinyal aktivitas) sehingga heartbeat sesi admin terkirim dan responsnya diterima, tanpa memuat ulang daftar
37. Majukan jam server dan jam browser/perangkat bersama 8 menit lagi (total 16 menit; sesi `Joko Saputra` tanpa aktivitas melewati batas idle 15 menit, sesi admin tetap berlaku)
38. Di Browser License klik [Force Logout] pada baris `Joko Saputra` (baris basi) → dialog konfirmasi "Force Logout User" muncul
39. Klik [Confirm Logout]
40. Verifikasi Tidak ada Dialog yang dikirim ke `Joko Saputra`
41. Verifikasi Respons force-logout OK dengan penanda "sudah berakhir"
42. Verifikasi UI admin menampilkan Dialog "Session Already Expired" (`fixed-asset/license/PRD/license.md` §6)
43. Verifikasi Status sesi `Joko Saputra` tetap Expired
44. Pulihkan jam server dan jam browser/perangkat ke waktu nyata

## Notes

- Sumber: `auth/session-management/TestCases/tc-session-management.md`. Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Aktor spec: Admin License dengan Global Role Manage Global License. TC-AUTH-SES-137 ada di spec `TC-AUTH-SES-E2E-034-sesi-produk-bersama-web-dan-mobile`.
- Penyimpangan urutan (S-05, S-10): urutan di spec ini TC-AUTH-SES-322, 133, 134, 138, 136 (urutan TC sumber 133, 134, 136, 138, 322). TC 322 (penolakan 403, tidak mengubah data) dijalankan paling awal sebelum aksi force-logout yang berhasil; TC 136 memajukan jam server uji sehingga ditaruh paling akhir.
- Langkah penghubung tanpa awalan `Verifikasi` (S-03): mengirim request force-logout langsung (langkah 1); membuka daftar License > Concurrent User, memilih baris target, mengklik [Force Logout], dan mengklik [Confirm Logout] (langkah 5 s.d. 7, 9, 17 s.d. 19, 25 s.d. 27, 34, 38, 39); mengamati Browser A tanpa interaksi untuk menunggu event push SSE (langkah 11 dan 20); mengklik [OK] pada Dialog Log Out (langkah 21); membuka URL produk Fixed Asset tanpa login ulang (langkah 23); membuka `Global Settings > Activity Log > Session` di Browser Admin (langkah 32); langkah 35 s.d. 37 memajukan jam server dan jam browser/perangkat bersama dua kali dengan sinyal aktivitas (gerak kursor, langkah 36) di antaranya supaya heartbeat sesi admin terkirim dan hanya sesi `Joko Saputra` yang kedaluwarsa; langkah 44 memulihkan jam sebelum spec selesai (hook `after` sebagai cadangan).
- Dependensi TC-AUTH-SES-134 pada TC-AUTH-SES-133 (Dialog Log Out sedang tampil): langkah force-logout dan pengamatan dialog disalin pada langkah 17 s.d. 20 (S-04). Asersi hasil force-logout itu sendiri diuji di TC-AUTH-SES-133.
- Butir b TC-AUTH-SES-136 ("Tidak ada entri log baru di `Global Settings > Activity Log > Session` dan User Log") dan butir a TC-AUTH-SES-322 ("tanpa dicatat") adalah asersi absence; tidak diasersikan di spec ini dan dirujuk ke spec absence `TC-AUTH-SES-E2E-069-absence-penolakan-force-logout-dan-aksi-admin` (S-05). Butir b TC-AUTH-SES-138 dibaca di Browser Admin (`Global Settings > Activity Log > Session`).
- Pengecualian `P-5` (b): TC-AUTH-SES-322 (request force-logout langsung yang ditolak 403, kelas a) adalah satu-satunya TC objek-uji ringan di spec ini, tanpa harness eksternal dan tanpa state berat sendiri, pada permukaan Concurrent User yang sama dengan TC lain. TC-AUTH-SES-136 memakai pengaturan jam sebagai langkah rutin untuk menunggu waktu (bagian 6), bukan objek uji, sehingga tidak butuh id pengecualian.
- Jumlah langkah (44) melewati sekitar 35 karena lima TC force-logout, masing-masing dengan user dan sesi seed sendiri sehingga bagian sesudahnya tetap bermakna walau bagian di atasnya gagal; langkah force-logout pada TC-AUTH-SES-134 disalin dari TC-AUTH-SES-133 (S-04); tiap `Verifikasi` memuat satu klausa (S-01), sehingga kemunculan Dialog "Log Out" dan Body-nya diasersikan pada dua langkah (langkah 15 dan 16).
- Temuan untuk QA: (1) TC-AUTH-SES-322 Precondition a menyebut user `Sari Wibowo` (Tabel Data Uji Dinamis #326) yang tidak dipakai di Langkah Uji maupun Expected; spec tidak men-seed user itu dan memakai sesi-produk akun admin sebagai target. (2) TC-AUTH-SES-322 tidak menyebut format request; spec memakai `POST /v2/iam/auth/product-sessions/{id}/force-logout` dari `auth/session-management/API/openapi.yaml`. (3) TC-AUTH-SES-136 Langkah 1 menjaga sesi admin dengan sinyal aktivitas (gerak kursor) sebelum setiap menunggu heartbeat, tetapi tidak menyebut jumlah pemajuan jam atau interval heartbeat; spec memajukan jam dua kali 8 menit dengan satu sinyal aktivitas di antaranya, dan interval heartbeat perlu dipastikan tim FE. (4) TC-AUTH-SES-136 butir a ("Tidak ada Dialog yang dikirim ke Joko Saputra") membutuhkan pengamatan sisi `Joko Saputra`; TC tidak menyebut konteks browsernya; spec mengamati sisi `Joko Saputra` lewat kemampuan pengamatan yang disediakan tim FE/BE (Prerequisites). (5) TC-AUTH-SES-133 butir d merujuk dialog dan toast ke `fixed-asset/license/PRD/license.md` §3.2 tanpa teksnya; spec mengasersikan kemunculannya sesuai dokumen itu. (6) TC-AUTH-SES-138 Langkah 2 membaca `Global Settings > Activity Log > Session` sebagai Total Control (Pre-setup #26), sedangkan TC-AUTH-SES-132 memakai `Activity Log > Session` milik Fixed Asset `[DEFERRED]`; spec mengikuti tiap TC. (7) TC-AUTH-SES-134 Expected b ("Mengakses halaman produk tanpa login ulang tidak mungkin") tidak punya langkah; langkah 23 membuka URL produk sebagai langkah penghubung agar asersinya dapat dijalankan (S-14). (8) TC-AUTH-SES-136 Precondition c dan Langkah 2 menulis "Browser Admin" untuk daftar `PLATFORM SETTINGS > License > Concurrent User` dan [Force Logout], sedangkan Pre-setup #1 dan #2 membedakan Browser Admin (Total Control) dari Browser License (Manage Global License); spec memakai Browser License untuk daftar License dan Force Logout (langkah 34, 38, 39) serta Browser Admin hanya untuk Activity Log.
- Baseline log (S-12): jumlah entri `Session ended` `Yoga Damayanti` dicatat di langkah 25 sebelum aksi; asersi mencari entri berdasarkan Note dan email dan mengasersi selisih jumlah. Jam baru digeser pada TC-AUTH-SES-136 (setelah bagian log) dan dipulihkan di langkah 44 serta hook `after`.
- Langkah 24 (TC-AUTH-SES-134 butir b) mengasersi hanya bahwa halaman produk tidak dapat diakses tanpa login ulang, sesuai Expected TC; tidak ada asersi tambahan tentang halaman tujuan.
