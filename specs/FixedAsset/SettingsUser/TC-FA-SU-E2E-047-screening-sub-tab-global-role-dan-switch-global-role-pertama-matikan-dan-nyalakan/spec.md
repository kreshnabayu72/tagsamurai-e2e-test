---
id: TC-FA-SU-E2E-047-screening-sub-tab-global-role-dan-switch-global-role-pertama-matikan-dan-nyalakan
title: "Screening Sub-tab Global Role dan Switch Global Role Pertama, Matikan, dan Nyalakan Kembali"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-159
  - TC-FA-SU-160
  - TC-FA-SU-161
  - TC-FA-SU-162
coverage:
  web: automated
---

# Screening Sub-tab Global Role dan Switch Global Role Pertama, Matikan, dan Nyalakan Kembali

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite: lihat `suite.md` (flag Guided Tooltip `seen`, sesi API aktor, pemulihan Pre-setup bersama lewat seed API).
- Data Pre-setup (Client `FaUserMain`, #20; penugasan #23): target Gita Permata dengan Global Role Import Data ON, Manage accounting ON (Create dan Read tercentang; Update dan Delete tidak tercentang), serta Manage asset ID configuration dan Manage global license OFF tanpa nilai tersimpan. Seed API memulihkan keadaan ini di hook `before` dan `after` (Catatan TC).
- Baseline log: hook `before` mencatat jumlah entri Tab Changelog Gita Permata, Tab System Log aktor, dan Activity Log (kemampuan baca disediakan tim FE/BE; bagian 8b butir 10). Entri log muncul eventual (NC-03): pemeriksaan memuat ulang tiap 5 detik sampai entri tampil, batas 2 menit.
- Kemampuan teknis (disediakan tim FE/BE): `Spectra.intercept()` untuk menahan respons request switch (hanya untuk mengamati indikator loading, bukan kegagalan; bagian 3 prinsip 13b); jalur navigasi ke Tab System Log aktor dan Activity Log (tidak disebut TC).
- State global dan pemulihan: penugasan Global Role Gita berubah (Manage asset ID configuration ON; Manage accounting kembali ke ON setelah blok TC-FA-SU-162 mematikannya) dan dipulihkan lewat seed API di hook `after`; entri log Assign dan Remove bertambah permanen (audit trail). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-159: Screening Sub-tab Global Role

1. Ketik Search `Gita`, tekan Enter di User List, klik nama Gita Permata, lalu buka Tab Role > Sub-tab Global Role
2. Klik header kolom Role Name
3. Verifikasi tabel berisi kolom `Active`, `Role Name`, `Create`, `Read`, `Update`, `Delete` serta header kolom Actions (⋯) sebagai pintu Column Visibility
4. Verifikasi header kolom data tidak mengurutkan baris setelah diklik pada langkah 2
5. Verifikasi baris berurut Role Name A-Z (Import Data, Manage accounting, Manage asset ID configuration, Manage asset master data, Manage global license, ...)
6. Verifikasi tabel Sub-tab Global Role tanpa paginasi
7. Verifikasi TableTools memuat ikon Changelog
8. Verifikasi Search, Filter, dan Download tidak tampil di TableTools
9. Verifikasi sel Create dan Delete pada baris Manage global license tampil `—`, bukan checkbox
10. Verifikasi baris Manage asset ID configuration (OFF) menampilkan Read dan Update sebagai checkbox tidak tercentang

### TC-FA-SU-160: Tab Role dan Sub-tab Global Role aktif awal

11. Kembali ke User List, klik nama Gita Permata di User List
12. Verifikasi Tab `Role` terpilih dan Sub-tab `Global Role` aktif
13. Verifikasi urutan Sub-tab: Global Role, Group Role, Transaction Role
14. Verifikasi Tab lain berurut Responsibilities (N), Non-Login User (N), Changelog, System Log, Transaction Admin Log, User Log

### TC-FA-SU-161: Nyalakan switch Global Role pertama kali

15. Tahan respons request switch Global Role selama 3 detik (`Spectra.intercept()`, hanya untuk mengamati loading)
16. Nyalakan switch pada baris Manage asset ID configuration
17. Verifikasi switch menampilkan indikator loading mini selama request
18. Lepaskan tahanan respons
19. Verifikasi switch Manage asset ID configuration berpindah ON
20. Verifikasi toast "Success, role has been updated."
21. Verifikasi checkbox Read baris Manage asset ID configuration tercentang dan Disabled
22. Verifikasi checkbox Update baris Manage asset ID configuration tidak tercentang dan Enabled
23. Verifikasi sel Create dan Delete baris Manage asset ID configuration tampil `—`
24. Buka Tab Changelog Gita Permata, muat ulang sampai entri tampil
25. Verifikasi entri `Assign` / Object `Global Role` / Field `Manage asset ID configuration` / Old Value `—` / New Value `Assigned` tercatat satu kali (selisih 1 dari baseline) di Tab Changelog
26. Buka Tab System Log aktor, muat ulang sampai entri tampil
27. Verifikasi entri `Assign` Object `Global Role` Field `Manage asset ID configuration` tercatat satu kali (selisih 1 dari baseline) di Tab System Log aktor
28. Buka Activity Log, muat ulang sampai entri tampil
29. Verifikasi entri `Assign` Object `Global Role` Field `Manage asset ID configuration` tercatat satu kali (selisih 1 dari baseline) di Activity Log

### TC-FA-SU-162: Matikan switch Global Role

30. Buka Detail Gita Permata > Tab Role > Sub-tab Global Role
31. Catat jumlah entri Tab Changelog Gita Permata sebagai baseline blok ini
32. Matikan switch pada baris Manage accounting
33. Verifikasi switch Manage accounting berpindah OFF
34. Verifikasi toast "Success, role has been updated."
35. Verifikasi checkbox Create, Read, Update, dan Delete baris Manage accounting tetap tampil namun Disabled
36. Hover checkbox Update baris Manage accounting
37. Verifikasi tooltip "Turn on this role first."
38. Buka Tab Changelog Gita Permata, muat ulang sampai entri tampil
39. Verifikasi entri `Remove` / Object `Global Role` / Field `Manage accounting` / Old Value `Assigned` / New Value `—` tercatat satu kali
40. Verifikasi jumlah entri Tab Changelog bertambah tepat satu dibanding baseline langkah 31 (tidak ada entri per permission)

## Notes

- Sumber TC: `fixed-asset/settings-user/TestCases/tc-settings-user.md`.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1 dan 11 (Search untuk menemukan baris target atau kembali ke User List, R-16), langkah 15 dan 18 (menahan dan melepas respons; intercept dilepas segera setelah pengamatan, S-09), langkah 24, 26, 28, 30, dan 38 (membuka surface log atau sub-tab), langkah 31 (mencatat baseline).
- Asersi tambahan di luar Expected TC: langkah 4 menerjemahkan "header kolom data tidak dapat diklik untuk sort" lewat urutan baris tidak berubah; langkah 39 adalah anchor positif bagi asersi jumlah langkah 40 (bagian 8b butir 2).
- Spec ini 40 langkah. Alasan melewati sekitar 35 langkah: keempat blok satu topik (Sub-tab Global Role pada target Gita Permata) dan satu pembukaan halaman Detail yang sama; blok screening dan blok switch berdiri sendiri karena seed API memulihkan penugasan sebelum tiap TC.
- Temuan untuk QA:
  - Post Condition TC-FA-SU-161 butir c dan TC-FA-SU-162 butir c ("Settings > Role & Permission > Detail Role Global Role: perubahan tampil") tidak punya langkah observasi di TC dan tidak diasersi (S-01); sinkronisasi dua arah diuji di spec 056.
  - Post Condition TC-FA-SU-161 butir a dan b serta TC-FA-SU-162 butir a dan b hanya diasersi lewat Expected (S-01).
  - Expected b TC-FA-SU-161 ("indikator loading mini selama request") memerlukan respons ditahan; Langkah Uji TC tidak menyebut intercept. Spec menahan respons 3 detik seperti TC-FA-SU-172 (spec 049).
  - Header tab "Responsibilities (N)" dan "Non-Login User (N)" pada Expected a TC-FA-SU-160 memakai placeholder N tanpa nilai; spec mengasersi nama tab dan urutan tanpa angka.
