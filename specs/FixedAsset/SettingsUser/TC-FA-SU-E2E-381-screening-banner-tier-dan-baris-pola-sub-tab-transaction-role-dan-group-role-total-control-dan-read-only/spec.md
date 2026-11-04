---
id: TC-FA-SU-E2E-381-screening-banner-tier-dan-baris-pola-sub-tab-transaction-role-dan-group-role-total-control-dan-read-only
title: "Screening Banner Tier dan Baris Pola Sub-tab Transaction Role dan Group Role: Total Control dan Read Only"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1072
  - TC-FA-SU-1080
coverage:
  web: automated
---

# Screening Banner Tier dan Baris Pola Sub-tab Transaction Role dan Group Role: Total Control dan Read Only

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21), penugasan (Pre-setup #23), dan Transaction Role (Pre-setup #39).
- Pengguna target: Lina Marlina, Total Control (Pre-setup #1 dan #23), dan Citra Lestari, Read Only (Pre-setup #3 dan #23).
- Data uji: tanpa data yang dibuat atau diubah; spec hanya membaca.
- Kemampuan teknis: tidak ada tambahan.
- State global yang diubah: tidak ada; tidak butuh pemulihan.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1072: Sub-tab Transaction Role target Total Control dan Read Only: banner tier dan baris pola tampil biasa

1. Ketik Search `Lina Marlina`, tekan Enter, lalu klik Name `Lina Marlina`
2. Klik Tab Role lalu Sub-tab Transaction Role
3. Verifikasi banner `This user has Total Control access.` tampil di atas tabel
4. Verifikasi tabel memuat baris pola Asset Admin
5. Verifikasi tabel memuat baris pola Approver
6. Verifikasi tabel tanpa kolom atau baris tier tambahan
7. Verifikasi banner tanpa tombol aksi
8. Kembali ke daftar User lewat Breadcrumb
9. Ganti isi kotak search dengan `Citra Lestari`, tekan Enter, lalu klik Name `Citra Lestari`
10. Klik Tab Role lalu Sub-tab Transaction Role
11. Verifikasi banner `This user has Read Only access.` tampil di atas tabel
12. Verifikasi tabel memuat baris pola Monitoring & Report
13. Verifikasi tabel tidak memuat baris Approver
14. Verifikasi banner tanpa tombol aksi

### TC-FA-SU-1080: Sub-tab Group Role target Total Control dan Read Only: banner tier dan baris pola tampil biasa tanpa tanda khusus

15. Klik Sub-tab Group Role
16. Verifikasi banner `This user has Read Only access.` tampil di atas tabel
17. Verifikasi baris Group Role tampil dengan seluruh group
18. Buka popup Assign Group Role Manage files
19. Verifikasi hanya centang Read yang tercentang pada popup
20. Verifikasi tanpa baris atau kolom tier tambahan
21. Verifikasi baris Manage user & role tidak dirender
22. Klik `[✕]` untuk menutup popup
23. Kembali ke daftar User lewat Breadcrumb
24. Ganti isi kotak search dengan `Lina Marlina`, tekan Enter, lalu klik Name `Lina Marlina`
25. Klik Tab Role lalu Sub-tab Group Role
26. Verifikasi banner `This user has Total Control access.` tampil di atas tabel
27. Verifikasi baris Group Role tampil dengan seluruh group
28. Verifikasi tanpa baris atau kolom tier tambahan pada tabel
29. Buka popup Assign Group Role Manage files
30. Verifikasi popup memuat centang CRUD penuh sesuai kapabilitas role
31. Verifikasi tanpa baris atau kolom tier tambahan pada popup
32. Verifikasi baris Manage user & role tidak dirender selama Global Role Manage global user & role aktif
33. Klik `[✕]` untuk menutup popup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. TC-FA-SU-1072 diselesaikan untuk kedua target (Lina Marlina lalu Citra Lestari) sebelum TC-FA-SU-1080; TC-FA-SU-1080 dibaca pada Citra Lestari lebih dulu (target yang sudah terbuka), lalu Lina Marlina; hasil per target tidak saling memengaruhi.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 8, 9, 23, 24. Search pada langkah 1, 9 dan 24 adalah langkah penghubung untuk menemukan baris target (R-16, R-23).
- Spec membaca saja (screening); tidak ada state yang diubah (S-09 tidak relevan).
- Alasan di atas sekitar 35 langkah (blok baca-log berpola tidak dihitung menurut bagian 3 prinsip 13, Smell): layar dan topik sama (Tab Role dua target), kelas fungsional tunggal tanpa harness; seluruh langkah adalah `Verifikasi` per klausa Expected (S-01) dan sedikit navigasi.
- TC-FA-SU-1074 (banner Group Manager per sub-tab Role) ada di spec 386.
- Temuan untuk QA:
  - TC-FA-SU-1080 langkah 1 menyebut "Login sebagai Total Control (Ahmad Dahlan)" sedangkan ACC menyebut Total Control dan Pre-setup #2 menyebut Ahmad Dahlan sebagai Default User; spec memakai Total Control Lina Marlina (Pre-setup #1, sesuai ACC dan akun default suite). Mohon dikonfirmasi aktor yang dimaksud.
  - TC-FA-SU-1080 butir c ("Manage user & role tidak dirender selama Global Role Manage global user & role aktif") tidak menyebut apakah Lina Marlina atau Citra Lestari memegang Global Role itu; spec mengasersi baris tidak dirender pada Lina Marlina saja (sesuai Pre-setup #23) dan tidak memverifikasi kondisi Global Role-nya.
  - TC-FA-SU-1072 butir c ("Banner tanpa tombol aksi") tidak menyebut target; spec mengasersinya pada kedua target.
