---
id: TC-FA-SU-E2E-048-nyalakan-kembali-switch-ubah-checkbox-update-dan-checkbox-read-terkunci
title: "Nyalakan Kembali Switch, Ubah Checkbox Update, dan Checkbox Read Terkunci"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-163
  - TC-FA-SU-164
  - TC-FA-SU-165
coverage:
  web: automated
---

# Nyalakan Kembali Switch, Ubah Checkbox Update, dan Checkbox Read Terkunci

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (Client `FaUserMain`, #20; penugasan #23): target Gita Permata dengan Global Role Import Data ON, Manage accounting ON (Create dan Read tercentang; Update dan Delete tidak tercentang), dan Manage asset ID configuration OFF tanpa nilai tersimpan. Seed API memulihkan keadaan ini di hook `before` dan `after` (Catatan TC).
- Baseline log: hook `before` mencatat jumlah entri `Assign` dan `Edit` Gita Permata di Tab Changelog (kemampuan baca disediakan tim FE/BE; bagian 8b butir 10); langkah 2 mencatat ulang sebelum TC-FA-SU-163. Entri log muncul eventual (NC-03): pemeriksaan memuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- Kemampuan teknis (disediakan tim FE/BE): pencatat request jaringan halaman (observasi, tanpa mengubah respons) untuk TC-FA-SU-165.
- State global dan pemulihan: penugasan Global Role Gita berubah (Manage asset ID configuration ON dengan Update tidak tercentang; Manage accounting tetap ON) dan dipulihkan lewat seed API di hook `after`; entri log Remove, Assign, dan Edit bertambah permanen (audit trail). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-163: Nyalakan kembali switch Global Role

1. Ketik Search `Gita`, tekan Enter di User List, klik nama Gita Permata, lalu buka Tab Role > Sub-tab Global Role
2. Catat jumlah entri `Assign` Manage accounting di Tab Changelog Gita Permata sebagai baseline
3. Matikan switch pada baris Manage accounting
4. Nyalakan switch yang sama pada baris Manage accounting
5. Verifikasi toast "Success, role has been updated."
6. Verifikasi tidak ada popup atau dialog tambahan yang tampil
7. Verifikasi checkbox Create dan Read baris Manage accounting tercentang serta Update dan Delete tidak tercentang
8. Verifikasi checkbox baris Manage accounting Enabled kecuali Read yang Disabled
9. Buka Tab Changelog Gita Permata, muat ulang sampai entri tampil
10. Verifikasi entri `Assign` / Object `Global Role` / Field `Manage accounting` tercatat satu kali (selisih 1 dari baseline langkah 2)

### TC-FA-SU-164: Ubah checkbox Update Global Role

11. Buka Tab Role > Sub-tab Global Role Gita Permata
12. Nyalakan switch pada baris Manage asset ID configuration
13. Centang Update pada baris Manage asset ID configuration
14. Verifikasi toast "Success, permissions have been updated."
15. Verifikasi tidak ada tombol `[Save]` pada Sub-tab Global Role (perubahan tersimpan otomatis)
16. Hapus centang Update pada baris Manage asset ID configuration
17. Verifikasi toast "Success, permissions have been updated."
18. Buka Tab Changelog Gita Permata, muat ulang sampai entri tampil
19. Verifikasi entri `Edit` / Object `Global Role` / Field `Manage asset ID configuration — Update` / Old Value `Inactive` / New Value `Active` tercatat satu kali
20. Verifikasi entri `Edit` / Object `Global Role` / Field `Manage asset ID configuration — Update` / Old Value `Active` / New Value `Inactive` tercatat satu kali

### TC-FA-SU-165: Checkbox Read selalu tercentang dan Disabled selama role aktif

21. Buka Tab Role > Sub-tab Global Role Gita Permata
22. Klik checkbox Read pada baris Import Data (ON)
23. Verifikasi checkbox Read baris Import Data tercentang dan Disabled
24. Verifikasi nilai checkbox Read baris Import Data tidak berubah setelah klik
25. Verifikasi tidak ada request ubah permission yang terkirim ke server setelah klik
26. Hover checkbox Read baris Import Data
27. Verifikasi tidak ada tooltip tambahan yang tampil

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1 (Search untuk menemukan baris target, R-16), langkah 2 (mencatat baseline), langkah 9, 11, 18, dan 21 (membuka sub-tab atau surface log).
- Asersi tambahan di luar Expected TC: langkah 24 menerjemahkan "klik tidak mengubah nilai" pada Expected a TC-FA-SU-165 dan langkah 25 menerjemahkan "tidak mengirim request"; langkah 27 menerjemahkan Expected b ("tidak memunculkan tooltip tambahan"). Langkah 15 menerjemahkan "tanpa tombol Save" pada Expected a TC-FA-SU-164.
- Temuan untuk QA:
  - Post Condition TC-FA-SU-163 butir b ("Entri `Remove` lalu `Assign`") dan butir c, TC-FA-SU-164 butir a sampai c, dan Post Condition TC-FA-SU-165 tidak punya langkah observasi tersendiri dan tidak diasersi di luar Expected (S-01).
  - Expected c TC-FA-SU-163 ("tercatat satu kali") hanya menyebut entri `Assign`; entri `Remove` dari langkah 3 tidak diasersi karena tidak ada di Expected.
  - Expected b TC-FA-SU-165 menyebut "S-40" tanpa menjelaskan; spec mengasersi tidak ada tooltip pada Read yang Disabled pada baris role aktif, sesuai sisi Expected yang dapat diamati.
  - TC-FA-SU-163 mencantumkan dependensi TC-FA-SU-162; langkah 3 sampai 4 mengulang matikan dan nyalakan sehingga spec berdiri sendiri (S-04).
