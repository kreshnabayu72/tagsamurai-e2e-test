---
id: TC-GS-USER-E2E-017-role-matrix-target-default-user-inline-edit-resend-dan-tab-role
title: "Role Matrix: Target Default User untuk Inline Edit Custom Field, Tab Role, dan Resend Confirmation Email oleh Total Control dan Full CRUD"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-USER-82
  - TC-GS-USER-1001
  - TC-GS-USER-1046
  - TC-GS-USER-1047
coverage:
  web: automated
---

# Role Matrix: Target Default User untuk Inline Edit Custom Field, Tab Role, dan Resend Confirmation Email oleh Total Control dan Full CRUD

## Prerequisites

- Mode: FE+BE.
- Hook suite: flag Guided Tooltip `gs-user` = seen (lihat `suite.md`).
- Role yang diuji (tiap role memakai akunnya sendiri; langkah ganti akun ditulis eksplisit di Test Steps):

| Role | Akun (Tabel Data Uji Pre-setup) | Nama user | Env var password | Aksi terhadap target Default User Hendra Gunawan |
|---|---|---|---|---|
| Total Control | `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (No. 2) | Siti Nurhaliza | `Spectra.env.GS_TC_PASSWORD` | Inline edit Custom Field (TC-GS-USER-82), Tab Role (TC-GS-USER-1001), Resend Confirmation Email (TC-GS-USER-1046) |
| Manage user and role (Full CRUD) | `manageUserFullCrud_automated_{namaCompany}@qwertysystem.net` (No. 4) | Fajar Nugroho | `Spectra.env.GS_FULLCRUD_PASSWORD` | Opsi Resend Hidden dan request langsung ditolak 403 (TC-GS-USER-1047) |

- Login akun Total Control (aktor pertama spec, sekaligus akun default suite) dilakukan di hook `before`; Full CRUD memakai langkah ganti akun eksplisit. Karena spec berakhir di akun Full CRUD, hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Env var: `GS_TC_PASSWORD`, `GS_FULLCRUD_PASSWORD` (didaftarkan di `executionConfig.environmentVariables`).
- Data Pre-setup (hanya dibaca kecuali Default User): Hendra Gunawan (No. 1, Default User, MFA Enrolled), Custom Field `Blood Type` (Dropdown A/B/O/AB, No. 24). Nilai `Blood Type` Hendra Gunawan bernilai `A` sebelum spec berjalan (TC-GS-USER-82; Tabel Pre-setup tidak menyebut nilai ini, disediakan tim FE/BE).
- Data Dinamis: pending email change pada Default User (TC-GS-USER-1046 precondition d dan TC-GS-USER-1047 precondition d): email baru `hendragunawan+{runId}-017@qwertysystem.net` dipasang di hook `before` oleh sesi Total Control lewat API, status masih pending konfirmasi. Mekanisme pemasangan tidak disebut di TC dan PRD; disediakan tim FE/BE (nama endpoint ditentukan tim FE di tahap script).
- Efek pada data Pre-setup Default User (S-06): TC-GS-USER-82 mengubah `Blood Type` Hendra Gunawan `A` → `B`; hook `after` memulihkan menjadi `A` lewat API dan membatalkan pending email change `hendragunawan+{runId}-017@qwertysystem.net`. Last Updated dan Modified By Hendra Gunawan tidak ikut pulih (berubah menjadi waktu dan aktor perubahan terakhir dari spec ini).
- Pemulihan data Pre-setup yang ditulis spec ini (`Blood Type` dan pending email Default User) merujuk fixture pemulihan di `suite.md` ("Pemulihan data Pre-setup yang ditulis spec").
- Kemampuan teknis (disediakan tim FE/BE): memajukan jam server dan jam browser bersama (cooldown Resend 60 detik pada TC-GS-USER-1046; countdown UI berjalan di jam browser); klien HTTP untuk request langsung Resend Confirmation Email ke Default User dengan sesi Full CRUD pada TC-GS-USER-1047 (nama endpoint ditentukan tim FE di tahap script).
- State global yang diubah: jam server dan jam browser (dimajukan di langkah 19, dipulihkan di langkah 29; hook `after` memulihkan sebagai cadangan), `Blood Type` dan pending email Default User (dipulihkan di hook `after`). Suite berjalan serial (`parallel: false`) dan spec ini berjalan sesudah spec yang mengasersi Default User seed yang belum diedit (lihat `suite.md`).

## Test Steps

### TC-GS-USER-82: Inline edit Custom Field target Default User oleh Total Control sukses

1. Klik icon Search, ketik `Hendra Gunawan`, tekan Enter
2. Klik Name `Hendra Gunawan` untuk membuka Detail (Default User)
3. Hover baris Custom Field `Blood Type`
4. Klik icon Edit2Line
5. Pilih `B`
6. Klik `[✓ Save]`
7. Verifikasi toast sukses `Success, Blood Type has been updated.`
8. Verifikasi baris kembali Display `Blood Type: B`

### TC-GS-USER-1001: Tab Role target Default User, keenam switch ON dan Disabled dengan tooltip Default User

9. Klik Tab `Role`
10. Verifikasi keenam switch Active Tab Role ON
11. Hover switch Active Tab Role
12. Verifikasi switch Active Tab Role tampil namun disabled
13. Verifikasi tooltip switch Active Tab Role "Default User cannot be modified."
14. Hover checkbox Tab Role
15. Verifikasi checkbox Tab Role tampil namun disabled
16. Verifikasi tooltip checkbox Tab Role "Default User cannot be modified."

### TC-GS-USER-1046: Resend Confirmation Email untuk target Default User oleh Total Control

17. Klik menu User di sidebar Global Settings
18. Klik icon Search, ketik `Hendra Gunawan`, tekan Enter
19. Majukan jam server dan jam browser bersama 120 detik sehingga cooldown resend email pending Hendra Gunawan sudah lewat
20. Klik (⋯) baris `Hendra Gunawan`
21. Verifikasi opsi `Resend Confirmation Email` tampil dan enabled pada baris Default User
22. Klik `Resend Confirmation Email`
23. Verifikasi toast sukses `Success, confirmation email has been sent to Hendra Gunawan.`
24. Klik (⋯) baris `Hendra Gunawan`
25. Verifikasi opsi `Resend Confirmation Email` masuk cooldown
26. Hover opsi `Resend Confirmation Email`
27. Verifikasi tooltip countdown tampil pada opsi `Resend Confirmation Email`
28. Tekan Esc untuk menutup overlay baris
29. Pulihkan jam server dan jam browser ke waktu semula

### TC-GS-USER-1047: Resend Email untuk target Default User Hidden bagi capability holder

30. Logout, login sebagai Manage user and role (Full CRUD), lalu buka Global Settings > User > User List (sub-tab Login User)
31. Klik icon Search, ketik `Hendra Gunawan`, tekan Enter
32. Klik (⋯) baris `Hendra Gunawan`
33. Verifikasi overlay baris `Hendra Gunawan` memuat opsi `Detail`
34. Verifikasi opsi `Resend Confirmation Email` tidak tampil (Hidden)
35. Tekan Esc untuk menutup overlay baris
36. Kirim request langsung Resend Confirmation Email ke Default User `Hendra Gunawan` dengan sesi Full CRUD lewat klien HTTP
37. Verifikasi respons server berstatus 403

## Notes

- Mode: FE+BE. Sumber: `global-settings/user/TestCases/tc-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Spec melewati sekitar 35 langkah (37 langkah) karena keempat TC berada di satu kelas harness (Role Matrix target Default User) pada layar List dan Detail, memakai dua akun dengan satu kali ganti akun, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC sumber dipertahankan. TC-GS-USER-1001 memakai Detail Hendra Gunawan yang sudah terbuka dari TC-GS-USER-82 (langkah 1 TC-GS-USER-1001 "Klik Name `Hendra Gunawan`" dipenuhi oleh langkah 2). Mail-catcher tidak dipakai: TC-GS-USER-1046 tidak mengharapkan asersi isi atau jumlah email.
- Langkah buka layar User List untuk akun awal tidak ditulis di Test Steps: dibuka oleh `beforeEach` suite (`suite.md`). Langkah penghubung (aksi tanpa `Verifikasi`): langkah 1, 18, 31 (Search nama target), 17 (kembali ke User List), 19 dan 29 (memajukan dan memulihkan jam; jam dipulihkan sebelum ganti akun), 24 (membuka ulang overlay baris untuk mengamati cooldown), 28 dan 35 (menutup overlay), 30 (ganti akun beserta pembukaan User List, karena `beforeEach` tidak dijalankan ulang).
- Anchor absence (bagian 8b butir 2): langkah 33 (opsi `Detail` tampil di overlay yang sama) mendahului langkah 34; asersi ini tidak ada di TC dan ditambahkan hanya sebagai anchor.
- P-5: TC-GS-USER-1047 Expected b (request langsung ke server) adalah objek uji ringan kelas a (defense-in-depth) tanpa harness eksternal dan tanpa state berat; satu-satunya TC kelas a di spec ini, berada di spec Role Matrix permukaan yang sama (opsi Resend Default User). Sesuai bagian 8b butir 1, hanya respons server yang diasersi (langkah 37); perilaku FE untuk respons yang sama tidak diasersi.
- Pembagian TC lintas spec: Resend Confirmation Email pada akun sendiri (TC-GS-USER-1029) diverifikasi di spec 018.
- Temuan untuk QA:
  - TC-GS-USER-1046 dan TC-GS-USER-1047 precondition d ("Email Default User sudah diubah dan masih pending konfirmasi") tanpa cara memasangnya; spec memasang pending email lewat kemampuan yang disediakan tim FE/BE.
  - TC-GS-USER-1046 tidak menyebut cooldown resend sudah lewat sebagai precondition, padahal email pending baru dipasang dan Expected a mensyaratkan opsi enabled; spec memajukan jam server dan jam browser bersama. TC-GS-USER-1046 Expected c ("tooltip countdown") tidak menyebut teks tooltip; spec mengasersi tooltip countdown tampil tanpa teks.
  - TC-GS-USER-1047 Expected b ("Request langsung Resend ke Default User ditolak 403") tidak menyebut endpoint atau state data yang dicek sesudahnya; spec hanya mengasersi status 403.
  - TC-GS-USER-82 tidak menyebut nilai awal `Blood Type` Hendra Gunawan (Data Uji `A` → `B`); Tabel Pre-setup hanya menyebut `Blood Type A` untuk Dewi Lestari.
