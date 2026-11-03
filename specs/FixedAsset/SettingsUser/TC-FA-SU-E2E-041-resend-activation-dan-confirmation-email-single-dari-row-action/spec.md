---
id: TC-FA-SU-E2E-041-resend-activation-dan-confirmation-email-single-dari-row-action
title: "Resend Activation dan Confirmation Email Single dari Row Action"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-135
  - TC-FA-SU-136
coverage:
  web: automated
---

# Resend Activation dan Confirmation Email Single dari Row Action

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Hook suite: lihat `suite.md` (flag Guided Tooltip `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (Client `FaUserMain`, #20; layanan #37): Hana Kusuma `hana.kusuma@corp.id` (Pending Activation) dan Indra Wijaya `indra.wijaya@corp.id` (Pending Email Confirmation dengan email baru pending; alamat email baru pending disediakan tim FE). Fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE.
- Kondisi awal: cooldown Resend Hana dan Indra belum berjalan (60 detik sejak pengiriman terakhir telah lewat); dipastikan hook `before` lewat seed API.
- Baseline log: hook `before` mencatat jumlah entri `Resend Activation Email` milik Hana dan `Resend Confirmation Email` milik Indra pada Tab Changelog target, Tab System Log aktor, dan Activity Log (kemampuan baca jumlah entri disediakan tim FE/BE; bagian 8b butir 10). Asersi memakai selisih terhadap baseline.
- Entri log muncul eventual (NC-03): pemeriksaan surface log memuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- Jam: jam server dan jam browser dibekukan bersama supaya tooltip cooldown bernilai tepat 60 detik, dan dilepas sebelum surface log dibuka (S-09). Hook `after` memulihkan jam. Entri log yang dibuat saat jam dibekukan dicari lewat Note, email, dan selisih jumlah, bukan posisi teratas (S-12).
- Kemampuan teknis (disediakan tim FE/BE): seed API untuk mereset cooldown dan status; jalur navigasi ke Tab System Log aktor dan Activity Log (tidak disebut TC).
- State global dan pemulihan: jam (dipulihkan hook `after`); cooldown Resend Hana dan Indra berjalan sesudah spec dan dipulihkan lewat seed API di hook `after`; dua entri log Resend bertambah permanen (audit trail). Suite berjalan serial (`parallel: false`).

## Test Steps

1. Bekukan jam server dan jam browser bersamaan

### TC-FA-SU-135: Resend Activation Email dari row action pengguna Pending Activation

2. Ketik Search `Hana`, tekan Enter di User List
3. Klik ⋯ pada baris Hana Kusuma
4. Verifikasi menu ⋯ baris Hana Kusuma memuat `Detail`, `Edit Home Group`, dan `Resend Activation Email`
5. Verifikasi `Resend Confirmation Email` tidak tampil di menu ⋯ baris Hana Kusuma
6. Klik `Resend Activation Email`
7. Verifikasi toast "Success, activation email has been sent." tampil tanpa nama pengguna
8. Klik ⋯ pada baris Hana Kusuma lagi, hover `Resend Activation Email`
9. Verifikasi `Resend Activation Email` pada baris Hana Kusuma Disabled dengan tooltip "Please wait 60 seconds before resending."
10. Lepaskan pembekuan jam, hover ulang `Resend Activation Email` pada baris Hana Kusuma
11. Verifikasi tooltip menghitung mundur: nilai `[Seconds]` pada "Please wait [Seconds] seconds before resending." kurang dari 60
12. Bekukan jam server dan jam browser bersamaan

### TC-FA-SU-136: Resend Confirmation Email dari row action pengguna Pending Email Confirmation

13. Ganti isi kotak search dengan `Indra`, tekan Enter
14. Klik ⋯ pada baris Indra Wijaya
15. Verifikasi menu ⋯ baris Indra Wijaya memuat `Resend Confirmation Email`
16. Verifikasi menu ⋯ baris Indra Wijaya tidak memuat `Resend Activation Email`
17. Klik `Resend Confirmation Email`
18. Verifikasi toast "Success, confirmation email has been sent to Indra Wijaya."
19. Klik ⋯ pada baris Indra Wijaya lagi, hover `Resend Confirmation Email`
20. Verifikasi `Resend Confirmation Email` pada baris Indra Wijaya Disabled dengan tooltip "Please wait 60 seconds before resending."
21. Lepaskan pembekuan jam, hover ulang `Resend Confirmation Email` pada baris Indra Wijaya
22. Verifikasi tooltip menghitung mundur: nilai `[Seconds]` pada "Please wait [Seconds] seconds before resending." kurang dari 60

### Pencatatan log (Expected d TC-FA-SU-135 dan TC-FA-SU-136)

23. Buka Detail Hana Kusuma > Tab Changelog, muat ulang sampai entri tampil
24. Verifikasi entri `Resend Activation Email` / Object `User` / Field `Activation Email` / Old Value `—` / New Value `hana.kusuma@corp.id` / Name `Hana Kusuma` tercatat satu kali (selisih 1 dari baseline) di Tab Changelog Hana Kusuma
25. Buka Detail Indra Wijaya > Tab Changelog, muat ulang sampai entri tampil
26. Verifikasi entri `Resend Confirmation Email` / Object `User` / Field `Confirmation Email` / Old Value `—` / New Value berisi alamat email baru pending / Name `Indra Wijaya` tercatat satu kali (selisih 1 dari baseline) di Tab Changelog Indra Wijaya
27. Buka Tab System Log aktor, muat ulang sampai entri tampil
28. Verifikasi entri `Resend Activation Email` Hana Kusuma tercatat satu kali (selisih 1 dari baseline) di Tab System Log aktor
29. Verifikasi entri `Resend Confirmation Email` Indra Wijaya tercatat satu kali (selisih 1 dari baseline) di Tab System Log aktor
30. Buka Activity Log, muat ulang sampai entri tampil
31. Verifikasi entri `Resend Activation Email` Hana Kusuma tercatat satu kali (selisih 1 dari baseline) di Activity Log
32. Verifikasi entri `Resend Confirmation Email` Indra Wijaya tercatat satu kali (selisih 1 dari baseline) di Activity Log

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Urutan: entri log kedua TC dibaca di akhir (langkah 23 sampai 32) supaya tiap surface log dibuka sekali; tiap entri tetap punya `Verifikasi` sendiri (S-01).
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1, 10, 12, dan 21 (pembekuan dan pelepasan jam, bagian 6), langkah 2 dan 13 (Search untuk menemukan baris target, R-16), langkah 23, 25, 27, dan 30 (membuka surface log; jalur Tab System Log aktor dan Activity Log tidak disebut TC).
- Asersi tambahan di luar Expected TC: langkah 11 dan 22 (nilai tooltip kurang dari 60) menerjemahkan frasa "menghitung mundur" pada Expected c; nilai per detik diuji di spec cooldown.
- Temuan untuk QA:
  - Post Condition TC-FA-SU-135 butir c dan TC-FA-SU-136 butir c ("Auth: email aktivasi atau konfirmasi terkirim") serta butir a (status tetap Pending) tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - TC tidak menyebut jalur navigasi ke Tab System Log aktor dan Activity Log; TC hanya membuka Tab Changelog target di Langkah Uji.
  - Alamat email baru pending Indra Wijaya tidak tertulis di Pre-setup #37 ("berisi alamat email baru pending"); disediakan tim FE.
  - Kolom Expected c TC-FA-SU-136 menulis tooltip "menghitung mundur" tanpa nilai; spec mengasersi nilai 60 saat jam dibekukan dan nilai di bawah 60 sesudah dilepas.
