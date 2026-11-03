---
id: TC-FA-SU-E2E-051-resilience-global-role-switch-dan-checkbox-gagal-disimpan-serta-auto-revert-gagal
title: "Resilience Global Role: Switch dan Checkbox Gagal Disimpan serta Auto-Revert Gagal"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-SU-167
  - TC-FA-SU-168
  - TC-FA-SU-191
coverage:
  web: automated
---

# Resilience Global Role: Switch dan Checkbox Gagal Disimpan serta Auto-Revert Gagal

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor kedua (langkah 22): Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (Client `FaUserMain`, #20; penugasan #23): target Gita Permata dengan Manage asset ID configuration OFF tanpa nilai tersimpan dan Manage accounting ON dengan Update tidak tercentang (TC-FA-SU-167 dan 168); target Lina Marlina (Total Control) dengan Manage accounting ON dan Update tercentang (TC-FA-SU-191, mengikuti TC-FA-SU-175). Seed API memulihkan keadaan ini di hook `before` dan `after` (Catatan TC).
- Kemampuan teknis (disediakan tim FE/BE): `Spectra.intercept()` atas respons HTTP request switch dan request checkbox Global Role menjadi 5xx; jalur navigasi ke Tab System Log aktor dan Activity Log (tidak disebut TC); kemampuan baca jumlah entri log.
- Baseline log: hook `before` mencatat jumlah entri `Assign` dan `Edit` Gita dan jumlah entri `Auto-Revert` dan `Edit` Lina pada Tab Changelog target, Tab System Log aktor, dan Activity Log (bagian 8b butir 10).
- Jeda nyata: langkah 15 menunggu 10 detik waktu nyata (bukan jam beku) sebelum toast error diperiksa kembali; batas 30 detik bagian 6 tidak terlampaui.
- State global dan pemulihan: intercept dilepas segera setelah pemicu (S-09); tidak ada perubahan tersimpan oleh spec ini; sesi dikembalikan ke akun default suite di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-167: Switch Global Role gagal disimpan

1. Cegat respons request switch Global Role menjadi 5xx (`Spectra.intercept()`)
2. Buka Detail Gita Permata > Tab Role > Sub-tab Global Role
3. Nyalakan switch pada baris Manage asset ID configuration
4. Verifikasi toast error "Error, failed to update role."
5. Verifikasi switch Manage asset ID configuration kembali ke posisi awal (OFF)
6. Lepaskan cegatan respons
7. Muat ulang halaman Detail Gita Permata > Tab Role > Sub-tab Global Role
8. Verifikasi switch Manage asset ID configuration OFF (data tidak berubah)
9. Buka Tab Changelog Gita Permata
10. Verifikasi jumlah entri `Assign` Gita Permata di Tab Changelog sama dengan baseline (tidak ada entri log)

### TC-FA-SU-168: Checkbox Global Role gagal disimpan

11. Cegat respons request checkbox Global Role menjadi 5xx (`Spectra.intercept()`)
12. Buka Tab Role > Sub-tab Global Role Gita Permata
13. Centang Update pada baris Manage accounting
14. Verifikasi toast error "Error, failed to update permissions."
15. Tunggu 10 detik tanpa menutup toast
16. Verifikasi toast error "Error, failed to update permissions." masih tampil
17. Tutup toast error
18. Verifikasi checkbox Update baris Manage accounting kembali ke nilai sebelum klik (tidak tercentang)
19. Lepaskan cegatan respons
20. Buka Tab Changelog Gita Permata
21. Verifikasi jumlah entri `Edit` Gita Permata di Tab Changelog sama dengan baseline (tidak ada entri log)

### TC-FA-SU-191: Konfirmasi Auto-Revert gagal di server

22. Ganti akun: logout, login sebagai Default User Ahmad Dahlan (`Spectra.env.FA_DU_PASSWORD`), lalu buka Fixed Asset > Settings > User
23. Cegat respons request checkbox Global Role menjadi 5xx (`Spectra.intercept()`)
24. Buka Detail Lina Marlina > Tab Role > Sub-tab Global Role
25. Hapus centang Update pada baris Manage accounting
26. Klik `[Remove]` pada dialog
27. Verifikasi toast error "Error, failed to update permissions."
28. Verifikasi tidak ada toast gagal khusus Auto-Revert
29. Verifikasi checkbox Update baris Manage accounting kembali ke nilai sebelum klik (tercentang)
30. Verifikasi banner `This user has Total Control access.` tetap tampil (tier Total Control Lina Marlina tetap)
31. Lepaskan cegatan respons
32. Buka Tab Changelog Lina Marlina
33. Verifikasi jumlah entri `Auto-Revert` dan `Edit` Lina Marlina di Tab Changelog sama dengan baseline
34. Buka Tab System Log aktor
35. Verifikasi jumlah entri `Auto-Revert` dan `Edit` Lina Marlina di Tab System Log aktor sama dengan baseline
36. Buka Activity Log
37. Verifikasi jumlah entri `Auto-Revert` dan `Edit` Lina Marlina di Activity Log sama dengan baseline

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Kelas b: semua blok memakai respons 5xx yang dipaksakan; tidak ada TC kelas lain.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1, 11, dan 23 (menyetel cegatan), langkah 6, 19, dan 31 (melepas cegatan segera setelah pemicu, S-09), langkah 7 (memuat ulang halaman untuk membaca state tersimpan), langkah 9, 20, 32, 34, dan 36 (membuka surface log), langkah 15 (jeda pendek 10 detik untuk mengamati toast persisten; di bawah batas 30 detik pada bagian 6), langkah 22 (ganti akun eksplisit, S-07).
- Asersi tambahan di luar Expected TC: langkah 8 menerjemahkan "data tidak berubah" pada Expected b TC-FA-SU-167 lewat muat ulang; langkah 16 menerjemahkan "bertahan sampai ditutup" pada Expected a TC-FA-SU-168; toast error langkah 4, 14, dan 27 menjadi anchor bagi asersi jumlah entri log (bagian 8b butir 2).
- Spec ini 37 langkah. Alasan melewati sekitar 35 langkah: seluruh blok satu kelas harness (fault injection pada Global Role) dengan dataset yang sama; tiap blok berdiri sendiri karena cegatan dilepas dan tidak ada state tersimpan yang berubah, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - Post Condition ketiga TC ("tidak ada entri baru pada tiga permukaan log") tidak punya langkah observasi pada TC-FA-SU-167 dan TC-FA-SU-168 (Expected b hanya menyebut "tidak ada entri log" tanpa surface), sehingga spec memakai Tab Changelog target; TC-FA-SU-191 Expected c menyebut tiga permukaan dan diasersi pada ketiganya.
  - Expected b TC-FA-SU-168 ("bertahan sampai ditutup") tidak menyebut durasi; spec memakai jeda 10 detik sebagai pembuktian bahwa toast tidak hilang otomatis dan mencatatnya sebagai pilihan spec.
  - Nilai awal checkbox Update Lina Marlina pada TC-FA-SU-191 tidak tertulis; spec mengikuti TC-FA-SU-175 (tercentang).
