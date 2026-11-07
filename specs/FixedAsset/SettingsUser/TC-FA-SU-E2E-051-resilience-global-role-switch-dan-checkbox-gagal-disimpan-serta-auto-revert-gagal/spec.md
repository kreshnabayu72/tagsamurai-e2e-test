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
- Akun aktor kedua (langkah 23): Default User Ahmad Dahlan (Pre-setup #2) `defaultUser_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_DU_PASSWORD`. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (Client `FaUserMain`, #20; penugasan #23): target Gita Permata dengan Manage asset ID configuration OFF tanpa nilai tersimpan dan Manage accounting ON dengan Update tidak tercentang (TC-FA-SU-167 dan 168); target Lina Marlina (Total Control) dengan Manage accounting ON dan Update tercentang (TC-FA-SU-191, mengikuti TC-FA-SU-175). Seed API memulihkan keadaan ini di hook `before` dan `after` (Catatan TC).
- Kemampuan teknis (disediakan tim FE/BE): `Spectra.intercept()` atas respons HTTP request switch dan request checkbox Global Role menjadi 5xx; jalur navigasi ke Tab System Log aktor dan Activity Log (tidak disebut TC); kemampuan baca jumlah entri log.
- Baseline log: hook `before` mencatat jumlah entri `Assign` dan `Edit` Gita (Tab Changelog target) serta jumlah entri `Auto-Revert` dan `Edit` Lina pada Tab Changelog target dan Activity Log (bagian 8b butir 10). Baseline Tab System Log aktor dicatat di langkah 24 pada sesi Ahmad Dahlan (aktor pembanding langkah 38), bukan di hook `before` pada sesi Lina, karena System Log tercatat per aktor.
- Jeda nyata: langkah 16 menunggu 10 detik waktu nyata (bukan jam beku) sebelum toast error diperiksa kembali; batas 30 detik bagian 6 tidak terlampaui.
- State global dan pemulihan: intercept dilepas segera setelah pemicu (S-09); tidak ada perubahan tersimpan oleh spec ini; sesi dikembalikan ke akun default suite di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-167: Switch Global Role gagal disimpan

1. Cegat respons request switch Global Role menjadi 5xx (`Spectra.intercept()`)
2. Ketik Search `Gita Permata`, tekan Enter
3. Buka Detail Gita Permata > Tab Role > Sub-tab Global Role
4. Nyalakan switch pada baris Manage asset ID configuration
5. Verifikasi toast error "Error, failed to update role."
6. Verifikasi switch Manage asset ID configuration kembali ke posisi awal (OFF)
7. Lepaskan cegatan respons
8. Muat ulang halaman Detail Gita Permata > Tab Role > Sub-tab Global Role
9. Verifikasi switch Manage asset ID configuration OFF (data tidak berubah)
10. Buka Tab Changelog Gita Permata
11. Verifikasi jumlah entri `Assign` Gita Permata di Tab Changelog sama dengan baseline (tidak ada entri log)

### TC-FA-SU-168: Checkbox Global Role gagal disimpan

12. Cegat respons request checkbox Global Role menjadi 5xx (`Spectra.intercept()`)
13. Buka Tab Role > Sub-tab Global Role Gita Permata
14. Centang Update pada baris Manage accounting
15. Verifikasi toast error "Error, failed to update permissions."
16. Tunggu 10 detik tanpa menutup toast
17. Verifikasi toast error "Error, failed to update permissions." masih tampil
18. Tutup toast error
19. Verifikasi checkbox Update baris Manage accounting kembali ke nilai sebelum klik (tidak tercentang)
20. Lepaskan cegatan respons
21. Buka Tab Changelog Gita Permata
22. Verifikasi jumlah entri `Edit` Gita Permata di Tab Changelog sama dengan baseline (tidak ada entri log)

### TC-FA-SU-191: Konfirmasi Auto-Revert gagal di server

23. Ganti akun: logout, login sebagai Default User Ahmad Dahlan (`Spectra.env.FA_DU_PASSWORD`), lalu buka Fixed Asset > Settings > User
24. Buka Tab System Log aktor (Ahmad Dahlan), catat jumlah entri `Auto-Revert` dan `Edit` Lina Marlina sebagai baseline System Log, lalu kembali ke Fixed Asset > Settings > User
25. Cegat respons request checkbox Global Role menjadi 5xx (`Spectra.intercept()`)
26. Ketik Search `Lina Marlina`, tekan Enter
27. Buka Detail Lina Marlina > Tab Role > Sub-tab Global Role
28. Hapus centang Update pada baris Manage accounting
29. Klik `[Remove]` pada dialog
30. Verifikasi toast error "Error, failed to update permissions."
31. Verifikasi tidak ada toast gagal khusus Auto-Revert
32. Verifikasi checkbox Update baris Manage accounting kembali ke nilai sebelum klik (tercentang)
33. Verifikasi banner `This user has Total Control access.` tetap tampil (tier Total Control Lina Marlina tetap)
34. Lepaskan cegatan respons
35. Buka Tab Changelog Lina Marlina
36. Verifikasi jumlah entri `Auto-Revert` dan `Edit` Lina Marlina di Tab Changelog sama dengan baseline
37. Buka Tab System Log aktor
38. Verifikasi jumlah entri `Auto-Revert` dan `Edit` Lina Marlina di Tab System Log aktor sama dengan baseline
39. Buka Activity Log
40. Verifikasi jumlah entri `Auto-Revert` dan `Edit` Lina Marlina di Activity Log sama dengan baseline

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Kelas b: semua blok memakai respons 5xx yang dipaksakan; tidak ada TC kelas lain.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1, 12, dan 25 (menyetel cegatan), langkah 7, 20, dan 34 (melepas cegatan segera setelah pemicu, S-09), langkah 8 (memuat ulang halaman untuk membaca state tersimpan), langkah 10, 21, 35, 37, dan 39 (membuka surface log), langkah 24 (mencatat baseline System Log di sesi Ahmad Dahlan), langkah 16 (jeda pendek 10 detik untuk mengamati toast persisten; di bawah batas 30 detik pada bagian 6), langkah 23 (ganti akun eksplisit, S-07).
- Langkah penghubung Search (R-16, S-03; bagian 8b butir 9 dan 13): langkah 2 dan 26 mencari baris target dengan nama persis sebelum aksi pada baris itu, tanpa `Verifikasi`; tabel User List dapat memuat lebih dari satu halaman (25 pengguna, 3 halaman).
- Asersi tambahan di luar Expected TC: langkah 9 menerjemahkan "data tidak berubah" pada Expected b TC-FA-SU-167 lewat muat ulang; langkah 17 menerjemahkan "bertahan sampai ditutup" pada Expected a TC-FA-SU-168; toast error langkah 5, 15, dan 30 menjadi anchor bagi asersi jumlah entri log (bagian 8b butir 2).
- Spec ini 40 langkah. Alasan melewati sekitar 35 langkah: seluruh blok satu kelas harness (fault injection pada Global Role) dengan dataset yang sama; tiap blok berdiri sendiri karena cegatan dilepas dan tidak ada state tersimpan yang berubah, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Temuan untuk QA:
  - Post Condition ketiga TC ("tidak ada entri baru pada tiga permukaan log") tidak punya langkah observasi pada TC-FA-SU-167 dan TC-FA-SU-168 (Expected b hanya menyebut "tidak ada entri log" tanpa surface), sehingga spec memakai Tab Changelog target; TC-FA-SU-191 Expected c menyebut tiga permukaan dan diasersi pada ketiganya.
  - Expected b TC-FA-SU-168 ("bertahan sampai ditutup") tidak menyebut durasi; spec memakai jeda 10 detik sebagai pembuktian bahwa toast tidak hilang otomatis dan mencatatnya sebagai pilihan spec.
  - Nilai awal checkbox Update Lina Marlina pada TC-FA-SU-191 tidak tertulis; spec mengikuti TC-FA-SU-175 (tercentang).
