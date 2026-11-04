---
id: TC-FA-SU-E2E-383-auto-revert-tier-read-only-dari-popup-assign-group-role-hapus-grup
title: "Auto-Revert Tier Read Only dari Popup Assign Group Role: Hapus Grup"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1077
coverage:
  web: automated
---

# Auto-Revert Tier Read Only dari Popup Assign Group Role: Hapus Grup

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan penugasan (Pre-setup #23).
- Pengguna target: Citra Lestari, Read Only (Pre-setup #3 dan #23): seluruh baris Group Role di semua group dengan Read saja dan baris pola Monitoring & Report.
- Data uji: popup Assign Group Role `Manage files`, grup `Branch Surabaya` dihapus lewat ikon hapus.
- Kemampuan teknis (disediakan tim FE/BE): seed API untuk memulihkan penugasan Citra Lestari ke Pre-setup #23; pembacaan jumlah entri Tab Changelog target, Tab System Log aktor, Activity Log, dan jumlah notifikasi in-app Citra Lestari sebelum aksi sebagai baseline (bagian 8b butir 10); jalur navigasi ke Tab System Log aktor dan Activity Log (tidak disebut TC). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: tier Read Only dan baris Group Role Manage files x Branch Surabaya milik Citra Lestari; dipulihkan ke Pre-setup #23 lewat seed API pada langkah penghubung dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1077: Remove baris Group Role (hapus grup dari popup) target Read Only: dialog Auto-Revert D-05b dan tier lepas

1. Catat jumlah entri Tab Changelog Citra Lestari, Tab System Log aktor, dan Activity Log, serta jumlah notifikasi in-app Citra Lestari, sebagai baseline
2. Ketik Search `Citra Lestari`, tekan Enter, lalu klik Name `Citra Lestari`
3. Klik Tab Role lalu Sub-tab Group Role
4. Verifikasi banner `This user has Read Only access.` tampil di Sub-tab Group Role
5. Buka popup Assign Group Role Manage files
6. Klik ikon hapus pada Branch Surabaya
7. Klik `[Save]`
8. Verifikasi dialog Auto-Revert D-05b dengan Title `Remove Read Only` tampil sebelum penyimpanan
9. Verifikasi Body bullet `• Citra Lestari`
10. Verifikasi kalimat `This edit will remove this user's Read Only access level. Their individual role permissions will remain as edited.`
11. Verifikasi penutup `Are you sure you want to remove it?`
12. Verifikasi dialog bukan dialog Remove Group Role biasa
13. Klik `[Remove]`
14. Verifikasi toast T-06a "Success, permissions have been updated. Citra Lestari is no longer Read Only."
15. Buka popup Assign Group Role Manage files
16. Verifikasi Branch Surabaya terlepas dari Manage files Citra Lestari
17. Tutup popup lewat `[✕]`
18. Verifikasi banner `This user has Read Only access.` hilang di Sub-tab Group Role
19. Verifikasi baris Group Role lain (role x group lain) tidak berubah
20. Klik Sub-tab Global Role
21. Verifikasi Global Role Citra Lestari tidak berubah
22. Klik Sub-tab Transaction Role
23. Verifikasi baris pola Transaction Role Citra Lestari tidak berubah
24. Buka Tab Changelog, Search `Citra Lestari`, tekan Enter, lalu muat ulang sampai entri tampil
25. Verifikasi entri `Remove` Object `Group Role` / Field `Manage files — Branch Surabaya` tercatat di Tab Changelog Citra Lestari
26. Verifikasi entri `Auto-Revert` Object `Read Only` tercatat di Tab Changelog Citra Lestari
27. Buka Tab System Log aktor
28. Verifikasi entri `Remove` dan entri `Auto-Revert` tercatat (selisih baseline) di Tab System Log aktor
29. Buka Activity Log
30. Verifikasi entri `Remove` dan entri `Auto-Revert` tercatat (selisih baseline) di Activity Log
31. Verifikasi jumlah notifikasi in-app ke Citra Lestari bertambah sesuai baseline
32. Pulihkan penugasan Citra Lestari ke Pre-setup #23 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 17, 20, 22, 24, 27, 29 dan 32. Search `Citra Lestari` pada langkah 2 dan 24 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Baseline log dan notifikasi mengikuti S-12; pemulihan lewat seed API memulihkan Pre-setup #23 (S-06, S-09).
- Langkah pola baca-log: langkah 24 sampai 30.
- TC-FA-SU-1076 (target Total Control, edit centang) ada di spec 378.
- Temuan untuk QA:
  - TC-FA-SU-1077 langkah 1 menyebut "Login sebagai Total Control (Ahmad Dahlan)" sedangkan ACC, precondition (a) dan Pre-setup #2 menyebut Ahmad Dahlan sebagai Default User; spec memakai Default User Ahmad Dahlan. Mohon dikonfirmasi aktor yang dimaksud.
  - TC-FA-SU-1077 butir d dan Post Condition menyebut notifikasi in-app ke Citra Lestari tanpa cara menghitung; spec memakai baseline jumlah notifikasi per penerima lewat kemampuan baca BE (8b butir 10).
