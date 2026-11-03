---
id: TC-FA-FAAL-E2E-076-absence-log-tab-session-kedaluwarsa-force-logout-event-platform-dan-aksi-gagal
title: "Absence Log: Session ended Kedaluwarsa, Force Logout, Event Platform, dan Aksi Edit Gagal"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAL-211
  - TC-FA-FAAL-218
  - TC-FA-FAAL-219
  - TC-FA-FAAL-255
coverage:
  web: automated
---

# Absence Log: Session ended Kedaluwarsa, Force Logout, Event Platform, dan Aksi Edit Gagal

## Prerequisites

- Mode: FE+BE.
- Akun observer dan aktor: Total Control (Pre-setup #1, Admin Alpha), `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Reports & Logs > Activity Log, tab Session). Pengecualian: langkah 28 sampai 34 membuka Activity Log > User Action dan Edit Group di Settings > Groups.
- Pelaku (Pre-setup #16), email dari `Fixture.activity-log.<kunci>.email` (fixture belum ada, disediakan tim FE), password lewat env var di butir "Env var" `suite.md` (R-07):
  - John Doe: App Access Fixed Asset dan seat subscription tersedia; password `Spectra.env.FA_JOHNDOE_PASSWORD`.
  - Mike Tan: password `Spectra.env.FA_MIKETAN_PASSWORD`.
  - Kedua env var terdaftar di butir "Env var" `suite.md`. Password tidak ditulis di spec atau fixture.
- Group `Gedung B` ada (disediakan tim FE/BE) untuk TC-FA-FAAL-255; nama baru uji `Gedung B1`.
- Kemampuan teknis disediakan tim BE/FE:
  - Sesi API aktor (butir "Sesi API aktor" di `suite.md`) untuk John Doe, Mike Tan, dan Admin Alpha (Force Logout di License > Concurrent User lewat sesi API aktor).
  - Manipulasi jam (butir "Manipulasi jam" di `suite.md`): jam server dan jam browser diatur bersama. Acuan T0 dibaca dari waktu terbit sesi-produk lewat API seeding; jam server diset absolut ke T0 + Session Idle Timeout + margin 5 menit. Nilai Session Idle Timeout tidak tertulis di TC (lihat Temuan untuk QA).
  - Intercept jaringan untuk memaksa respons Edit Group gagal (500) di atas backend nyata.
- Baseline (S-12): total baris Tab Session dan Tab User Action dibaca dari teks pagination `Showing x–y of N entries` sebelum aksi pemicu dan sebelum jam digeser; asersi sesudah jam digeser memakai selisih total, bukan posisi teratas.
- State yang diubah dan pemulihannya: jam server dan jam browser dipulihkan pada langkah 6 dan 12 serta di hook `after`; sesi-produk John Doe dan Mike Tan ditutup di hook `after`; intercept dilepas pada langkah 30.
- Flag Guided Tooltip halaman Activity Log: hook suite `before` men-set true dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`). Berlaku untuk akun observer.
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-FAAL-211: Session ended tercatat saat sesi platform kedaluwarsa

1. Pelaku John Doe (sesi API aktor) login dengan password dan membuka produk Fixed Asset hingga Session started tersimpan
2. Catat total baris Tab Session dari teks pagination (N0)
3. Majukan jam server melewati batas Session Idle Timeout sesi John Doe (T0 + Session Idle Timeout + 5 menit) dan jam browser, lalu John Doe (sesi API aktor) mengirim satu request dari sesi tersebut hingga Session ended tersimpan
4. Verifikasi tanpa memuat ulang halaman: total baris Tab Session N0 + 1, yaitu hanya satu baris baru
5. Verifikasi tanpa memuat ulang halaman: baris baru muncul otomatis di baris paling atas Tab Session: User `John D`, Activity `Session`, Status `—`, Note `Session ended`
6. Pulihkan jam server dan jam browser ke waktu nyata
7. Verifikasi tidak ada baris dengan Note `Logged out by admin` untuk sesi-produk yang sama

### TC-FA-FAAL-218: Force-logout tidak menambah baris Session ended untuk sesi-produk yang sama

8. Pelaku Mike Tan (sesi API aktor) login dengan password dan membuka produk Fixed Asset hingga Session started tersimpan
9. Catat total baris Tab Session dari teks pagination (N0)
10. Admin Total Control (sesi API aktor, Admin Alpha) melakukan Force Logout sesi Mike Tan dari License > Concurrent User hingga Logged out by admin tersimpan
11. Majukan jam server melewati batas sesi platform Mike Tan (T0 + Session Idle Timeout + 5 menit) dan jam browser, lalu Mike Tan (sesi API aktor) mengirim satu request hingga sesi platform dinyatakan berakhir
12. Pulihkan jam server dan jam browser ke waktu nyata
13. Muat ulang halaman (F5)
14. Klik icon Filter, pilih Note `Logged out by admin`, klik `[Apply]`, lalu ketik Search email Mike Tan (`Fixture.activity-log.<kunci>.email`), tekan Enter
15. Verifikasi baris Mike Tan: User `Mike T`, Activity `Session`, Status `—`, Note `Logged out by admin`
16. Klik menu `Activity Log` pada sidebar Reports & Logs (mereset Search, Filter, dan Sort)
17. Verifikasi tidak ada baris baru dengan Note `Session ended` untuk sesi-produk yang sama
18. Verifikasi total baris Tab Session N0 + 1, yaitu hanya satu baris baru pada langkah 15

### TC-FA-FAAL-219: Event platform tidak muncul di Tab Session Fixed Asset

19. Catat total baris Tab Session dari teks pagination (N0)
20. Pelaku John Doe (sesi API aktor) login dengan password, membuka produk Fixed Asset, dan melakukan Logout dari platform hingga Session started dan Session ended tersimpan
21. Verifikasi baris `Session started` dan `Session ended` John D untuk sesi langkah 20 ada
22. Verifikasi total baris Tab Session N0 + 2 dari langkah 19
23. Verifikasi tidak ada baris dengan Note `Login with password`, `Logged out`, maupun `Session expired`
24. Verifikasi total baris Tab Session N0 + 2, yaitu hanya dua baris pada langkah 21
25. Klik icon Filter dan buka dropdown Note
26. Verifikasi dropdown Note hanya memuat `Concurrent limit reached`, `Logged out by admin`, `Session ended`, `Session started`

### TC-FA-FAAL-255: Aksi modul lain yang gagal tidak meninggalkan baris

27. Klik menu `Activity Log` pada sidebar Reports & Logs (mereset Search, Filter, dan Sort)
28. Buka Activity Log > User Action
29. Catat total baris Tab User Action dari teks pagination (NU)
30. Aktifkan intercept jaringan yang memaksa respons Edit Group gagal (500), buka Edit Group `Gedung B` di Settings > Groups, ganti nama dengan `Gedung B1`, klik simpan, lalu lepas intercept
31. Klik `✕` pada form Edit Group
32. Verifikasi dialog `Unsaved Changes` tampil
33. Klik `[Leave]`
34. Buka Activity Log > User Action
35. Verifikasi total baris Tab User Action sama dengan NU

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- P-5 butir a: pemicu time-travel (langkah 3 dan 11), Force Logout (langkah 10), dan kegagalan 500 lewat intercept (langkah 30) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji; tiap TC punya pelaku dan baseline sendiri.
- TC-FA-FAAL-211 dan TC-FA-FAAL-218 butir a punya asersi presence; keduanya berada di spec ini karena menyatu dengan butir absence yang sama (S-05, TC terbelah antara presence dan absence).
- Urutan langkah TC-FA-FAAL-211: selisih total (langkah 4) dibaca lebih dulu, lalu baris Session ended di baris paling atas (langkah 5), keduanya sebelum jam dipulihkan (langkah 6) karena baris yang dibuat saat jam digeser bercap waktu masa depan; langkah 7 tidak memakai posisi teratas (S-12). Langkah 13 (F5) pada TC-FA-FAAL-218 memuat ulang Tab Session sesudah jam dipulihkan; baris Mike Tan ditemukan lewat Filter Note dan Search email (langkah 14, R-16), bukan posisi teratas, karena baris bercap waktu masa depan dari langkah 3 berada di atas; langkah 18 memakai selisih total.
- Anchor absence: langkah 5 untuk langkah 7; langkah 15 untuk langkah 17; langkah 21 untuk langkah 23.
- Langkah penghubung (S-03): langkah 1, 8 (sesi-produk aktif sebagai precondition TC), langkah 6, 12 (pemulihan jam), langkah 13, 16, 27, 28, 34 (memuat ulang, mereset, dan membuka Tab User Action), langkah 31 sampai 33 (menutup form dirty, S-08).
- Langkah 22 memakai selisih total tanpa Search karena Search `John` pada Tab Session bisa mencocokkan baris John lain dan baris Session ended bercap masa depan dari langkah 3 berada di atas; posisi teratas tidak dipakai.
- Temuan untuk QA:
  - TC-FA-FAAL-211 dan 218 tidak menyebut nilai Session Idle Timeout atau durasi sesi platform; spec menulis T0 + Session Idle Timeout + 5 menit dan nilainya disediakan tim BE/FE.
  - TC-FA-FAAL-218 langkah 2 menulis "Tunggu hingga sesi platform Mike Tan berakhir"; spec memakai manipulasi jam (R-10).
  - TC-FA-FAAL-219 Expected butir b tidak punya cara memeriksa Note yang tidak ada di banyak halaman selain total; spec memakai total N0 + 2.
  - Langkah 14 mengasumsikan Search Tab Session dapat mencocokkan email user; TC dan PRD yang dibaca tidak menyebut kolom yang dicari Search, sehingga perlu konfirmasi QA.
  - TC-FA-FAAL-255 langkah 1 menyebut "simpan perubahan nama" tanpa menyebut menu; spec memakai Settings > Groups. TC tidak menyebut efek form setelah respons 500; spec menutup form lewat `✕` dan `[Leave]`.
  - Email dan password John Doe dan Mike Tan tidak tertulis di Pre-setup TC; email disediakan tim FE dan env var password mengikuti `suite.md`.
