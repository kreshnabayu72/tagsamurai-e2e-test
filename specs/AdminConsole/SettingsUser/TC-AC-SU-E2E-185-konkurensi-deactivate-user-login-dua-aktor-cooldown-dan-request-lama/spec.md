---
id: TC-AC-SU-E2E-185-konkurensi-deactivate-user-login-dua-aktor-cooldown-dan-request-lama
title: "Konkurensi Deactivate User Sedang Login, Dua Aktor Mengubah Status, Resend Saat Cooldown Aktor Lain, dan Switch Role Request Lama"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-94
  - TC-AC-SU-104
  - TC-AC-SU-150
  - TC-AC-SU-577
coverage:
  web: automated
---

# Konkurensi Deactivate User Sedang Login, Dua Aktor Mengubah Status, Resend Saat Cooldown Aktor Lain, dan Switch Role Request Lama

## Prerequisites

- Mode: FE+BE.
- Akun aktor UI utama (aktor A): Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun UI utama ke Default User dilakukan eksplisit pada langkah 25 dan 26 (TC-94 mensyaratkan aktor Default User); hook `after` memulihkan sesi ke Default User.
- Aktor kedua (aktor B): pada TC-104, aktor B adalah sesi UI kedua (konteks browser kedua; layar B dan hasil di kedua layar diasersi), Default User `defaultUserAdminConsole_automated_{namaCompany}@qwertysystem.net` dengan `Spectra.env.AC_DU_PASSWORD`, login pada langkah 1 dan ditutup bersama sesi loginnya sesudah blok. Pada TC-150, aktor B memicu Resend lewat sesi API Default User (login API password; token tidak dihitung sebagai sesi web; kemampuan disediakan tim BE/FE). Pada TC-94, user target Jane Smith adalah sesi UI kedua (konteks browser kedua, objek asersi), password dari `Spectra.env.AC_SU_SEEDED_PASSWORD` (nama env baru, didaftarkan pemilik repo). Pada TC-577, aktor yang sama membuka dua tab browser (tab 1 dan tab 2).
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. Satu user per blok TC:

| Kode | Name | Email | State awal |
|---|---|---|---|
| U1 | `John Doe {runId}-185A` | `johndoe+{runId}-185a@qwertysystem.net` | Activated, Active (TC-104) |
| U2 | `Mike Tan {runId}-185B` | `miketan+{runId}-185b@qwertysystem.net` | Pending Activation, di luar cooldown Resend (TC-150) |
| U3 | `Mike Tan {runId}-185C` | `miketan+{runId}-185c@qwertysystem.net` | Activated, tanpa tier, "Manage group" OFF saat tab 1 dimuat (TC-577) |
| U4 | `Jane Smith {runId}-185D` | `janesmith+{runId}-185d@qwertysystem.net` | Activated, Active, dua Group Role aktif, dapat login ke Admin Console, memiliki satu notifikasi in-app lama sebagai anchor (TC-94) |

- Kemampuan teknis: Fixture BE (seeding user, role, dan satu notifikasi lama untuk U4); konteks browser kedua; sesi API aktor B; jam server dan jam browser sinkron (cooldown Resend 60 detik pada TC-150 dijaga dalam jendela 60 detik dengan membekukan kedua jam pada T + 10 detik, dipulihkan di hook `after`). Tanpa intercept. Jendela tunggu 5 detik tanpa memuat ulang halaman sebelum asersi absence notifikasi (TC-94) adalah pilihan spec (bukan nilai TC atau PRD).
- State global yang diubah spec: jam server dan jam browser (TC-150); suite berjalan serial (`parallel: false`).
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-104: Dua aktor mengubah status user yang sama
1. Buka konteks kedua (jendela privat), login sebagai Default User (aktor B)
2. Buka Settings > User lewat sidebar di sesi aktor B
3. Ketik Search `John Doe {runId}-185A`, tekan Enter di sesi aktor B
4. Di sesi aktor A: ketik Search `John Doe {runId}-185A`, tekan Enter sehingga baris U1 tampil Active
5. Di sesi aktor A: klik switch Active baris U1, lalu klik `[Deactivate]`, lalu tunggu aksi selesai
6. Di sesi aktor B (tanpa memuat ulang): klik switch Active baris U1, lalu konfirmasi dialog yang tampil, lalu tunggu aksi selesai
7. Muat ulang kedua layar
8. Verifikasi tidak ada dialog konflik di kedua aktor
9. Verifikasi status akhir U1 di kedua layar sama dengan hasil aksi yang dikirim terakhir (aksi aktor B, Inactive)
### TC-AC-SU-150: Resend ditolak server karena cooldown dari admin lain
10. Tutup konteks kedua dan hapus sesi loginnya, lalu di sesi aktor A ganti isi kotak search dengan `Mike Tan {runId}-185B`, tekan Enter sehingga baris U2 tampil dengan Resend Activation Email enabled
11. Aktor B mengirim Resend Activation Email untuk U2 lewat sesi API hingga pengiriman tersimpan
12. Catat T dari waktu terbit Resend aktor B lewat API seeding
13. Bekukan jam server dan jam browser pada T + 10 detik
14. Di sesi aktor A (tanpa memuat ulang): buka row action (⋯) baris U2, lalu klik Resend Activation Email
15. Verifikasi tidak ada toast error
16. Verifikasi tombol langsung di-refresh ke state cooldown dengan countdown sisa waktu
17. Pulihkan jam server dan jam browser
### TC-AC-SU-577: Switch role request lama
18. Ganti isi kotak search dengan `Mike Tan {runId}-185C`, tekan Enter, klik Name baris U3, klik Tab Role, lalu sub-tab Global Role sehingga switch "Manage group" tampil OFF (tab 1)
19. Buka tab 2 pada jendela yang sama, buka Detail U3, klik Tab Role, sub-tab Global Role, aktifkan switch "Manage group" (OFF ke ON), lalu tunggu aksi selesai
20. Kembali ke tab 1 (tanpa memuat ulang) dan klik switch "Manage group" dari OFF ke ON
21. Verifikasi toast sukses `"Success, role has been updated."`
22. Verifikasi tab 1 di-refresh ke state server dengan switch "Manage group" ON
23. Tutup tab 2, klik menu Settings > User di sidebar, klik icon Changelog di toolbar, lalu ketik Search `Mike Tan {runId}-185C` pada Popup Changelog: User, tekan Enter
24. Verifikasi Popup Changelog: User hanya memuat 1 baris Assign untuk U3 (dari tab 2)
### TC-AC-SU-94: Deactivate user yang sedang login
25. Tutup popup, lakukan Logout dari akun Total Control
26. Login sebagai Default User (aktor)
27. Buka Settings > User lewat sidebar di sesi aktor
28. Buka konteks kedua (jendela privat), login sebagai U4 (`janesmith+{runId}-185d@qwertysystem.net`), lalu buka Settings > User di sesi U4
29. Di sesi aktor: ketik Search `Jane Smith {runId}-185D`, tekan Enter, klik switch Active baris U4, lalu klik `[Deactivate]`
30. Verifikasi toast sukses `"Success, user has been deactivated."` di sesi aktor
31. Verifikasi halaman Settings > User di sesi aktor tidak menampilkan dialog atau aksi pemutusan sesi
32. Di sesi U4 (tanpa memuat ulang), amati layar
33. Verifikasi layar sesi U4 tidak menampilkan dialog atau aksi pemutusan sesi apa pun
34. Klik lonceng notifikasi navbar di sesi U4
35. Verifikasi notifikasi lama milik U4 yang sudah ada tampil di daftar
36. Tunggu 5 detik tanpa memuat ulang halaman
37. Verifikasi daftar notifikasi U4 tidak memuat notifikasi baru untuk event Deactivate

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): Search baris target (R-16), pembukaan dan penutupan konteks kedua, pembukaan tab 2, pembekuan dan pemulihan jam (TC-150), ganti akun eksplisit pada langkah 25 dan 26, pembukaan Settings > User lewat sidebar sesudah login di konteks kedua dan sesudah login Default User (langkah 2, 27, dan 28), dan jendela tunggu 5 detik pada langkah 36 (bagian 6, pilihan spec).
- Urutan: TC-104, TC-150, TC-577, lalu TC-94 karena TC-94 menggantikan akun UI utama ke Default User sehingga ditaruh terakhir (S-10).
- Empat blok kelas c berpola sama (dua sesi, aksi yang berpotongan, asersi hasil); kegagalan satu blok tidak membuat blok lain kehilangan makna, sehingga 37 langkah (di atas smell 35 langkah) dipertahankan.
- Temuan untuk QA:
  - TC-94, TC-104, TC-150, dan TC-577 tidak menyatakan apakah aktor atau sesi kedua memakai sesi UI atau API; spec memakai sesi UI kedua hanya bila hasilnya diasersi (TC-104 layar B, TC-94 layar target) dan sesi API untuk pemicu (TC-150).
  - TC-94 mensyaratkan aktor Default User dan Jane Smith login di browser lain tanpa password/akun; spec memakai user seeding dengan env baru `AC_SU_SEEDED_PASSWORD`. Butir c TC-94 menyebut notifikasi lama sebagai anchor tanpa asal notifikasinya; spec men-seed satu notifikasi lama untuk U4 (kemampuan disediakan tim FE/BE), mengasersi notifikasi itu tampil (langkah 35), lalu mengasersi tidak ada notifikasi baru untuk event Deactivate.
  - Post Condition TC-94 (status Inactive; Role dan 2 Group Role tetap tersimpan), TC-104, dan TC-150 ("Hanya 1 email terkirim") tidak punya langkah observasi di TC dan tidak diasersi.
  - TC-577 menyatakan precondition "Mike Tan 'Manage group' sudah aktif" sekaligus tab 1 menampilkan OFF; spec men-seed OFF saat tab 1 dimuat lalu tab 2 mengaktifkannya. TC-577 butir c ("Hanya 1 baris Assign") tidak menyebut baseline; user bernama unik sehingga baseline entri nol.
  - TC memakai nama literal (`John Doe`, `Mike Tan`, `Jane Smith`); spec memakai nama bersuffix (S-12).
