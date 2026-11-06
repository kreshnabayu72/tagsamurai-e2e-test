---
id: TC-FA-SU-E2E-392-edit-baris-pola-group-manager-pada-node-turunan-dialog-auto-revert
title: "Edit Baris Pola Group Manager pada Node Turunan: Dialog Auto-Revert D-05c dan Baris Pola Dipertahankan sebagai Baris Biasa"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-1082
coverage:
  web: automated
---

# Edit Baris Pola Group Manager pada Node Turunan: Dialog Auto-Revert D-05c dan Baris Pola Dipertahankan sebagai Baris Biasa

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (`suite.md`): flag Guided Tooltip `seen`, sesi API aktor, dan pemulihan Pre-setup bersama dirujuk tanpa diulang di sini.
- Client `FaUserMain` (Pre-setup #20) dengan pohon grup (Pre-setup #21), penugasan (Pre-setup #23), dan varian Group Manager (Pre-setup #48).
- Pengguna target: Putri Anggraeni, Group Manager Finance & Accounting (turunan: Accounts Payable) dengan baris pola Group Manager pada kedua node, ditambah penugasan non-pola: Group Role Manage user & role pada Finance & Accounting (Read dan Update), Transaction Role Disposal × Staff pada IT Infrastructure, dan Damaged × Monitoring & Report pada Branch Surabaya (Pre-setup #48).
- Data uji: baris Manage files × Accounts Payable (node turunan, bukan node penugasan Group Manager), centang Delete dihapus.
- Kemampuan teknis (disediakan tim FE/BE): seed API untuk memulihkan Putri Anggraeni ke Pre-setup #48; pembacaan jumlah entri Tab Changelog Putri Anggraeni sebelum aksi sebagai baseline (bagian 8b butir 10). Entri log muncul eventual: permukaan dimuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- State global yang diubah: status Group Manager dan seluruh baris pola Putri Anggraeni; dipulihkan ke Pre-setup #48 lewat seed API pada langkah penghubung dan di hook `after`. Suite berjalan serial.
- Fixture: nama pengguna, grup, dan nilai Data Uji ditulis apa adanya dari TC; fixture `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan pada tahap script.

## Test Steps

### TC-FA-SU-1082: Edit CRUD baris pola Group Manager pada node turunan: dialog Auto-Revert D-05c, status GM terlepas, seluruh baris pola dipertahankan sebagai baris biasa, dan penugasan non-pola tetap

1. Ketik Search `Putri Anggraeni`, tekan Enter
2. Catat label Role Putri Anggraeni di User List dan jumlah entri Tab Changelog Putri Anggraeni sebagai baseline
3. Klik Name `Putri Anggraeni`
4. Klik Tab Role lalu Sub-tab Group Role
5. Klik `[Assign Group]` pada baris Manage files
6. Hapus centang Delete pada Accounts Payable
7. Klik `[Save]`
8. Verifikasi dialog Title `Remove Group Manager` tampil sebelum penyimpanan walau baris yang diedit berada pada node turunan
9. Verifikasi Body bullet `• Putri Anggraeni`
10. Verifikasi kalimat `This edit will remove Group Manager status for this group.`
11. Verifikasi kalimat `Their individual role permissions will remain as edited.`
12. Verifikasi penutup `Are you sure you want to remove it?`
13. Verifikasi tombol `[Cancel]` (Text, Contrast) dan `[Remove]` tampil
14. Verifikasi dialog Remove/edit Group Role biasa tidak tampil
15. Klik `[Remove]`
16. Verifikasi toast "Success, permissions have been updated. Putri Anggraeni is no longer Group Manager for Finance & Accounting." (T-06b)
17. Verifikasi banner Group Manager hilang di Sub-tab Group Role
18. Verifikasi seluruh baris pola Group Manager pada Finance & Accounting dan Accounts Payable di Sub-tab Group Role (Group Role katalog selain Manage user & role) tetap tersimpan sebagai baris biasa, termasuk baris Manage files yang disimpangkan aksi pemicu
19. Verifikasi baris Manage files × Accounts Payable tetap tampil dengan Delete tidak dicentang
20. Verifikasi Group Role Manage user & role pada Finance & Accounting (penugasan non-pola) tetap
21. Klik Sub-tab Transaction Role
22. Verifikasi banner Group Manager hilang di Sub-tab Transaction Role
23. Verifikasi seluruh baris pola Transaction Role Asset Admin dan Approver pada seluruh Jenis Transaksi di Finance & Accounting dan Accounts Payable tetap tersimpan sebagai baris biasa
24. Verifikasi Transaction Role Disposal × Staff pada IT Infrastructure tetap
25. Verifikasi Transaction Role Damaged × Monitoring & Report pada Branch Surabaya tetap
26. Klik Sub-tab Global Role
27. Verifikasi banner Group Manager hilang di Sub-tab Global Role
28. Verifikasi Global Role tidak berubah
29. Buka Settings > User lewat sidebar lalu ketik Search `Putri Anggraeni`, tekan Enter
30. Verifikasi label Role Putri Anggraeni di User List tidak berkurang dibanding baseline (seluruh baris pola yang dipertahankan tetap dihitung sebagai penugasan biasa, tanpa badge)
31. Klik Name `Putri Anggraeni`, buka Tab Changelog, lalu muat ulang sampai entri tampil
32. Verifikasi entri `Auto-Revert` / Object `Group Manager` / Field `Group Manager — Finance & Accounting` / Old Value `Assigned` / New Value `—` tercatat (bertambah satu dibanding baseline) di Tab Changelog Putri Anggraeni
33. Verifikasi entri aksi pemicu (Manage files × Accounts Payable) tercatat di Tab Changelog Putri Anggraeni
34. Pulihkan Putri Anggraeni ke Pre-setup #48 lewat seed API

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari TC): langkah 1, 2, 3, 21, 26, 29, 31 dan 34. Search `Putri Anggraeni` pada langkah 1, 29 dan 31 adalah langkah penghubung untuk menemukan baris target (R-16, R-23). Baseline log mengikuti S-12; pemulihan lewat seed API memulihkan Pre-setup #48 (S-06, S-09).
- Langkah pola baca-log: langkah 31 sampai 33. Entri aksi pemicu pada langkah 33 diasersi tanpa jumlah (lihat Temuan untuk QA).
- Verifikasi kolom Old Value, New Value, dan Field entri `Auto-Revert` pada langkah 32 digabung sebagai kolom satu baris log dari satu entri (S-01).
- TC-FA-SU-1098 (Auto-Revert tidak menulis entri `Remove (via Group Manager)` per baris pola, Expected f TC-FA-SU-1082) diasersi di spec 403; spec ini tidak memuat `Verifikasi` untuknya.
- Temuan untuk QA:
  - Tombol `[Remove]` pada dialog D-05c ditandai "copy usulan, perlu persetujuan PM" (`settings-role-permission` Open Item #7d), sedangkan label tombol pada TC lain di modul yang sama memakai `[Revoke]` (D-10/D-05); spec memakai `[Remove]` apa adanya dari TC. Mohon dikonfirmasi.
  - TC-FA-SU-1082 Expected butir c ("dalam transaksi atomik yang sama") tidak punya langkah observasi atomisitas; spec hanya mengasersi hasil akhir baris pola tetap tersimpan.
  - TC-FA-SU-1082 Expected butir e menyebut label Role "tidak berkurang" (baris pola yang dipertahankan tetap dihitung) tanpa angka; spec membandingkan label dengan baseline dan tidak mengasersi angka (angka turunan seperti 48 dan 25 di Pre-setup #43 dihitung per assignment termasuk baris pola, PRD Open Item 3 belum diputuskan PM).
  - TC-FA-SU-1082 Expected butir f ("entri aksi pemicu tercatat") tidak menyebut Action, Object, maupun surface log. Belum jelas apakah baris pemicu `Edit` dicatat bersama entri `Auto-Revert`; spec hanya mengasersi bahwa entri aksi pemicu tercatat di Tab Changelog target.
  - TC-FA-SU-1082 Expected butir b menyebut banner hilang di "ketiga sub-tab"; spec mengasersi banner pada Sub-tab Group Role, Transaction Role, dan Global Role.
  - TC-FA-SU-1082 Post Condition butir b (entri `Auto-Revert` pada Tab System Log aktor dan Activity Log) dan butir c (notifikasi in-app ke Putri) tidak punya langkah observasi dan tidak diasersi di spec ini; butir b dan c diamati TC-FA-SU-1098 di spec 403. Butir d dipenuhi lewat langkah 34.
  - Kalimat penutup D-05 `Their individual role permissions will remain as edited.` (Expected a TC-FA-SU-1082) adalah copy usulan (PM, `settings-role-permission` Open Item #7d); spec mengasersinya apa adanya.
