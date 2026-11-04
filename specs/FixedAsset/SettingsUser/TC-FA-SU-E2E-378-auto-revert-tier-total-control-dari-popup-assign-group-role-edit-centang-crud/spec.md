---
id: TC-FA-SU-E2E-378-auto-revert-tier-total-control-dari-popup-assign-group-role-edit-centang-crud
title: "Auto-Revert Tier Total Control dari Popup Assign Group Role: Edit Centang CRUD"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1076
coverage:
  web: automated
---

# Auto-Revert Tier Total Control dari Popup Assign Group Role: Edit Centang CRUD

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21) dan penugasan (Pre-setup #23).
- Pengguna target: Lina Marlina, Total Control (Pre-setup #1 dan #23): seluruh baris Group Role di semua group dengan CRUD penuh (kecuali Manage user & role) dan baris pola Transaction Role.
- Data uji: popup Assign Group Role `Manage files`, baris grup `IT Infrastructure`, centang `Delete` dihapus.
- Kemampuan teknis (disediakan tim FE/BE): seed API untuk memulihkan penugasan Lina Marlina ke Pre-setup #23; pembacaan jumlah entri Tab Changelog target, Tab System Log aktor, Activity Log, dan jumlah notifikasi in-app Lina Marlina sebelum aksi sebagai baseline (bagian 8b butir 10); jalur navigasi ke Tab System Log aktor dan Activity Log (tidak disebut TC). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: tier Total Control dan baris Group Role Manage files x IT Infrastructure milik Lina Marlina; dipulihkan ke Pre-setup #23 lewat seed API pada langkah penghubung dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1076: Edit CRUD baris Group Role target Total Control: dialog Auto-Revert D-05a, tier lepas, dan role lain tetap utuh

1. Catat jumlah entri Tab Changelog Lina Marlina, Tab System Log aktor, dan Activity Log, serta jumlah notifikasi in-app Lina Marlina, sebagai baseline
2. Ketik Search `Lina Marlina`, tekan Enter, lalu klik Name `Lina Marlina`
3. Klik Tab Role lalu Sub-tab Group Role
4. Verifikasi banner `This user has Total Control access.` tampil di Sub-tab Group Role
5. Buka popup Assign Group Role Manage files
6. Hapus centang Delete pada IT Infrastructure
7. Klik `[Save]`
8. Verifikasi dialog Auto-Revert D-05a dengan Title `Remove Total Control`
9. Verifikasi Body bullet `• Lina Marlina`
10. Verifikasi kalimat `This edit will remove this user's Total Control access level. Their individual role permissions will remain as edited.`
11. Verifikasi penutup `Are you sure you want to remove it?`
12. Verifikasi tombol `[Cancel]` dan `[Remove]` tampil dan dialog bukan dialog Remove Group Role biasa
13. Klik `[Remove]`
14. Verifikasi toast T-06a "Success, permissions have been updated. Lina Marlina is no longer Total Control."
15. Buka popup Assign Group Role Manage files
16. Verifikasi centang Delete pada IT Infrastructure tidak tercentang
17. Tutup popup lewat `[✕]`
18. Verifikasi banner `This user has Total Control access.` hilang di Sub-tab Group Role
19. Klik Sub-tab Global Role
20. Verifikasi banner `This user has Total Control access.` hilang di Sub-tab Global Role
21. Klik Sub-tab Transaction Role
22. Verifikasi banner `This user has Total Control access.` hilang di Sub-tab Transaction Role
23. Verifikasi baris pola Transaction Role Lina Marlina tidak berubah
24. Klik Sub-tab Global Role
25. Verifikasi Global Role Lina Marlina tidak berubah
26. Klik Sub-tab Group Role
27. Verifikasi baris Group Role lain (role x group lain) tidak berubah
28. Buka Tab Changelog, Search `Lina Marlina`, tekan Enter, lalu muat ulang sampai entri tampil
29. Verifikasi entri `Edit` Object `Group Role` / Field `Manage files — IT Infrastructure — Delete` / Old Value `Active` / New Value `Inactive` tercatat satu kali (selisih baseline) di Tab Changelog Lina Marlina
30. Verifikasi entri `Auto-Revert` Object `Total Control` tercatat satu kali (selisih baseline) di Tab Changelog Lina Marlina
31. Buka Tab System Log aktor
32. Verifikasi entri `Edit` dan entri `Auto-Revert` tercatat satu kali (selisih baseline) di Tab System Log aktor
33. Buka Activity Log
34. Verifikasi entri `Edit` dan entri `Auto-Revert` tercatat satu kali (selisih baseline) di Activity Log
35. Verifikasi jumlah notifikasi in-app view-only ke Lina Marlina bertambah sesuai baseline
36. Pulihkan penugasan Lina Marlina ke Pre-setup #23 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 17, 19, 21, 24, 26, 28, 31, 33 dan 36. Search `Lina Marlina` pada langkah 2 dan 28 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Baseline log dan notifikasi mengikuti S-12; pemulihan lewat seed API memulihkan Pre-setup #23 (S-06, S-09).
- Langkah pola baca-log: langkah 28 sampai 34.
- Alasan di atas sekitar 35 langkah (blok baca-log berpola tidak dihitung menurut bagian 3 prinsip 13, Smell): satu TC dengan satu kelas (fungsional), tanpa kelas harness. Expected TC memuat empat butir bermajemuk yang masing-masing wajib satu `Verifikasi` per klausa (S-01) dan tiga surface log yang dibaca satu per satu; langkah tidak dapat dikurangi tanpa menghilangkan klausa Expected.
- TC-FA-SU-1077 (target Read Only, hapus grup) ada di spec 383.
- Temuan untuk QA:
  - TC-FA-SU-1076 butir d dan Post Condition menyebut notifikasi in-app "view-only" ke Lina Marlina tanpa cara menghitung; spec memakai baseline jumlah notifikasi per penerima lewat kemampuan baca BE (8b butir 10).
  - TC-FA-SU-1076 langkah 5 ("Periksa Sub-tab ... serta banner") tidak menyebut nilai yang dibandingkan untuk baris Group Role lain; spec membandingkan terhadap keadaan Pre-setup #23 (CRUD penuh, kecuali Manage files x IT Infrastructure Delete).
  - Toast T-06a: Expected menyebut kalimat lengkap pada butir b; spec mengasersi sebelum `Verifikasi` state persisten karena butir b memuat lebih dari tiga klausa persisten (8b butir 5).
