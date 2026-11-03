---
id: TC-FA-SU-E2E-055-eksklusivitas-global-role-manage-global-user-dan-role-vs-group-role-manage-user-dan
title: "Eksklusivitas Global Role Manage global user & role vs Group Role Manage user & role"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-186
  - TC-FA-SU-187
  - TC-FA-SU-1054
coverage:
  web: automated
---

# Eksklusivitas Global Role Manage global user & role vs Group Role Manage user & role

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (Client `FaUserMain`, #20; pohon grup #21; penugasan #23): target Nanda Pratama (Pre-setup #11) dengan Group Role Manage user & role pada Finance & Accounting dan Global Role Manage global user & role OFF. Seed API memulihkan keadaan ini di hook `before`, langkah 18, dan hook `after` (Catatan TC).
- Baseline log: hook `before` mencatat jumlah entri `Assign` dan `Remove` Nanda di Tab Changelog (kemampuan baca disediakan tim FE/BE; bagian 8b butir 10); langkah 18 mencatat ulang. Entri log muncul eventual (NC-03): pemeriksaan memuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- Kemampuan teknis (disediakan tim FE/BE): kemampuan baca state BE penugasan grup Group Role Nanda (langkah 23); seed API untuk memulihkan Nanda.
- State global dan pemulihan: penugasan Global Role dan Group Role Nanda berubah dan dipulihkan lewat seed API di hook `after`; entri log `Assign` dan `Remove` bertambah permanen (audit trail). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-186: Switch Global Role Manage global user & role ON menghapus penugasan grup

1. Ketik Search `Nanda`, tekan Enter di User List, klik nama Nanda Pratama, lalu buka Tab Role > Sub-tab Global Role
2. Nyalakan switch pada baris Manage global user & role
3. Verifikasi switch Manage global user & role berpindah ON
4. Verifikasi tidak ada dialog tambahan yang tampil (termasuk dialog Auto-Revert Group Manager)
5. Klik Sub-tab Group Role
6. Verifikasi baris Group Role lain tampil di Sub-tab Group Role
7. Verifikasi baris Group Role `Manage user & role` tidak tampil lagi
8. Buka Tab Changelog Nanda Pratama, muat ulang sampai entri tampil
9. Verifikasi entri `Assign` / Object `Global Role` / Field `Manage global user & role` tercatat satu kali (selisih 1 dari baseline)
10. Verifikasi entri `Remove` / Object `Group Role` / Field `Manage user & role — Finance & Accounting` / Old Value `Assigned` / New Value `—` tercatat satu kali, disusul sesudah entri `Assign`

### TC-FA-SU-187: Switch Manage global user & role OFF kembali

11. Buka Tab Role > Sub-tab Global Role Nanda Pratama
12. Matikan switch pada baris Manage global user & role
13. Klik Sub-tab Group Role
14. Verifikasi baris Group Role `Manage user & role` muncul kembali dengan kolom Group `—`
15. Verifikasi kolom Group baris `Manage user & role` tidak memuat Finance & Accounting (penugasan grup tidak dipulihkan)
16. Buka Tab Changelog Nanda Pratama, muat ulang sampai entri tampil
17. Verifikasi entri `Remove` / Object `Global Role` / Field `Manage global user & role` tercatat satu kali

### TC-FA-SU-1054: Assign Global Role lewat Detail Role menghapus penugasan grup

18. Pulihkan Nanda Pratama (Global Role Manage global user & role OFF; Group Role Manage user & role pada Finance & Accounting) lewat seed API, lalu catat baseline jumlah entri `Assign` dan `Remove` Nanda di Tab Changelog
19. Buka Settings > Role & Permission > Detail Role Global Role Manage global user & role
20. Assign Nanda Pratama sebagai pengguna Global Role Manage global user & role
21. Buka Settings > User > Detail Nanda Pratama > Tab Role > Sub-tab Group Role
22. Verifikasi baris Group Role lain tampil di Sub-tab Group Role
23. Verifikasi penugasan grup Group Role `Manage user & role` Nanda Pratama tidak ada di state BE (terhapus dalam transaksi yang sama)
24. Verifikasi baris Group Role `Manage user & role` tidak tampil lagi di Sub-tab Group Role
25. Buka Tab Changelog Nanda Pratama, muat ulang sampai entri tampil
26. Verifikasi entri `Assign` Global Role tercatat satu kali (selisih 1 dari baseline langkah 18)
27. Verifikasi entri `Remove` per grup Group Role tercatat satu kali (selisih 1 dari baseline langkah 18), disusul sesudah entri `Assign`

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1 (Search untuk menemukan baris target, R-16), langkah 5, 8, 11, 13, 16, 21, dan 25 (membuka sub-tab atau surface log), langkah 18 (memulihkan Nanda lewat seed API dan mencatat baseline).
- Asersi tambahan di luar Expected TC: langkah 6, 22 adalah anchor positif bagi asersi absence langkah 7, 24 (bagian 8b butir 2); langkah 4 menerjemahkan "tanpa dialog tambahan dan tanpa Auto-Revert Group Manager" (Expected a TC-FA-SU-186) sebagai satu `Verifikasi` karena keduanya satu dialog.
- Temuan untuk QA:
  - Langkah Uji TC-FA-SU-1054 ("Assign Nanda Pratama sebagai pengguna Global Role") tidak merinci UI Role & Permission; spec menulis satu langkah dan UI-nya diuji di suite Settings Role & Permission.
  - Expected c TC-FA-SU-1054 ("switch OFF kembali tidak memulihkan grup") tidak punya langkah OFF di Langkah Uji; pernyataan yang sama diasersi di TC-FA-SU-187 (langkah 15) sehingga tidak diasersi lagi.
  - Post Condition TC-FA-SU-186 butir a, b, dan c serta TC-FA-SU-187 butir a dan b tidak punya langkah observasi tersendiri dan tidak diasersi di luar Expected (S-01). Post Condition TC-FA-SU-186 butir c (Role & Permission Detail Role) diuji di spec 056.
  - Judul TC-FA-SU-186 menyebut "log Assign disusul Remove per grup"; urutan diasersi lewat kata "disusul" pada langkah 10 dan 27.
