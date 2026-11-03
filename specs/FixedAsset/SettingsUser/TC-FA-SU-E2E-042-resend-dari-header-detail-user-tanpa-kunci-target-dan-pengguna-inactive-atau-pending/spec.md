---
id: TC-FA-SU-E2E-042-resend-dari-header-detail-user-tanpa-kunci-target-dan-pengguna-inactive-atau-pending
title: "Resend dari Header Detail User, Tanpa Kunci Target, dan Pengguna Inactive atau Pending"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-137
  - TC-FA-SU-150
  - TC-FA-SU-151
coverage:
  web: automated
---

# Resend dari Header Detail User, Tanpa Kunci Target, dan Pengguna Inactive atau Pending

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (Client `FaUserMain`, #20; layanan #37; aktor #2): Hana Kusuma (Pending Activation), Indra Wijaya (Pending Email Confirmation), Gita Permata (Activated), Kartika Sari (Pending Activation, Inactive), Lukman Hakim (Pending Email Confirmation, Inactive), Ahmad Dahlan (Default User), dan Lina Marlina (akun aktor sendiri).
- Kondisi awal TC-FA-SU-150: Ahmad Dahlan berstatus Pending Activation dan Lina Marlina berstatus Pending Email Confirmation. Pre-setup #2 dan #1 menyebut keduanya aktor yang dapat login sehingga kondisi ini disediakan tim FE lewat seed API di hook `before` dan dipulihkan lewat seed API di hook `after` (S-06; lihat Temuan untuk QA).
- Kondisi awal semua blok: cooldown Resend untuk tiap pengguna dan jenis email belum berjalan; dipastikan hook `before` lewat seed API.
- Jam: jam server dan jam browser dibekukan bersama pada langkah 1 supaya tooltip cooldown bernilai tepat 60 detik, dilepas pada langkah 12; hook `after` memulihkan jam.
- State global dan pemulihan: jam; cooldown Resend dan entri log Resend bertambah (audit trail permanen) dan cooldown dipulihkan lewat seed API di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

1. Bekukan jam server dan jam browser bersamaan

### TC-FA-SU-137: Resend dari header Detail User

2. Ketik Search `Hana`, tekan Enter, klik nama Hana Kusuma di User List untuk membuka Detail
3. Verifikasi header Detail Hana Kusuma menampilkan tombol `[Resend Activation Email]`
4. Klik `[Resend Activation Email]`, lalu hover tombol
5. Verifikasi toast "Success, activation email has been sent." (sama dengan row action)
6. Verifikasi tombol `[Resend Activation Email]` langsung Disabled dengan tooltip "Please wait 60 seconds before resending."
7. Kembali ke User List, ketik Search `Indra`, tekan Enter, klik nama Indra Wijaya
8. Verifikasi header Detail Indra Wijaya menampilkan tombol `[Resend Confirmation Email]`
9. Klik `[Resend Confirmation Email]`, lalu hover tombol
10. Verifikasi toast "Success, confirmation email has been sent to Indra Wijaya."
11. Verifikasi tombol `[Resend Confirmation Email]` langsung Disabled dengan tooltip "Please wait 60 seconds before resending."
12. Lepaskan pembekuan jam
13. Kembali ke User List, ketik Search `Gita`, tekan Enter, klik nama Gita Permata
14. Verifikasi header Detail Gita Permata tampil dengan nama Gita Permata
15. Verifikasi tombol `[Resend Activation Email]` tidak tampil di header Detail Gita Permata
16. Verifikasi tombol `[Resend Confirmation Email]` tidak tampil di header Detail Gita Permata

### TC-FA-SU-150: Resend tidak punya kunci target

17. Kembali ke User List, ketik Search `Ahmad`, tekan Enter, klik ⋯ pada baris Ahmad Dahlan (Default User, Pending Activation)
18. Verifikasi `Resend Activation Email` Enabled di menu ⋯ baris Ahmad Dahlan
19. Klik `Resend Activation Email`
20. Verifikasi toast "Success, activation email has been sent."
21. Ganti isi kotak search dengan `Lina`, tekan Enter, klik ⋯ pada baris Lina Marlina (akun sendiri, Pending Email Confirmation)
22. Verifikasi `Resend Confirmation Email` Enabled di menu ⋯ baris Lina Marlina
23. Klik `Resend Confirmation Email`
24. Verifikasi toast "Success, confirmation email has been sent to Lina Marlina."

### TC-FA-SU-151: Resend untuk pengguna Inactive dan Pending

25. Ganti isi kotak search dengan `Kartika`, tekan Enter, klik ⋯ pada baris Kartika Sari
26. Verifikasi `Resend Activation Email` Enabled di menu ⋯ baris Kartika Sari
27. Klik `Resend Activation Email`
28. Verifikasi toast "Success, activation email has been sent."
29. Ganti isi kotak search dengan `Lukman`, tekan Enter, klik ⋯ pada baris Lukman Hakim
30. Verifikasi `Resend Confirmation Email` Enabled di menu ⋯ baris Lukman Hakim
31. Klik `Resend Confirmation Email`
32. Verifikasi toast "Success, confirmation email has been sent to Lukman Hakim."

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1, 12 (pembekuan dan pelepasan jam, bagian 6), langkah 2, 7, 13, 17, 21, 25, dan 29 (Search untuk menemukan baris target atau kembali ke User List, R-16).
- Asersi tambahan di luar Expected TC: langkah 14 (nama Gita Permata tampil di header) adalah anchor positif bagi asersi absence langkah 15 dan 16 (bagian 8b butir 2); langkah 18, 22, 26, dan 30 memeriksa tombol Enabled yang disebut Expected a dan b TC sebelum klik.
- Toast sukses langkah 20, 24, 28, dan 32 memakai template copy dari Catatan TC (`Success, confirmation email has been sent to [User].`); Expected TC-FA-SU-150 butir c dan TC-FA-SU-151 hanya menulis "toast sukses yang sama" dan "berhasil" (R-14).
- Temuan untuk QA:
  - Post Condition ketiga TC (cooldown berjalan, satu entri log per Resend, status aktif tetap Inactive) tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - Kondisi awal TC-FA-SU-150 (Default User dan akun sendiri berstatus pending) tidak ada di Tabel Data Uji Pre-setup: #1 dan #2 adalah akun aktor berstatus Activated. Spec menuliskannya sebagai kemampuan seed "disediakan tim FE" (S-13).
  - Header Detail TC-FA-SU-137 langkah 4 (Detail Gita Permata) tidak memuat langkah klik untuk "pengguna Activated tanpa email pending"; spec hanya membuka Detail dan memeriksa header.
