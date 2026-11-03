---
id: TC-AC-RP-E2E-138-absence-log-selection-limit-request-langsung
title: "Absence Log: Selection Limit lewat Request Langsung Ditolak Tanpa Entri Changelog (Bulk Remove dan Assign Total Control)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-RP-435
  - TC-AC-RP-436
coverage:
  web: automated
---

# Absence Log: Selection Limit lewat Request Langsung Ditolak Tanpa Entri Changelog (Bulk Remove dan Assign Total Control)

## Prerequisites

- Mode: FE+BE (backend nyata; request langsung ke endpoint modul lewat klien HTTP sebagai pemicu, pembacaan audit trail pelaku lewat kemampuan baca)
- Akun aktor: Total Control `Distributor Seleksi Besar` `totalControlBigRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Hadi Gunawan`, Pre-setup #20), password `Spectra.env.AC_RP_BIG_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #20 (entitas `Distributor Seleksi Besar` dengan 105 user Standard memegang `Manage group`), #21 (System Limits: Selection Limit 100), dan #25 (klien HTTP). Request berisi 101 baris/user, dipilih dari 105 user Standard tersebut. Kedua request ditolak server; tidak ada Data Dinamis bersuffix `+{runId}-138` yang dibuat spec ini.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak ditulis karena tidak disebut TC, PRD, atau LLD): klien HTTP untuk request langsung (Pre-setup #25) dan sesi API aktor (dinyatakan di `suite.md`) sebagai pemicu.
- Kemampuan teknis: membaca jumlah entri audit trail pelaku (Detail User `Siti Nurhaliza` > Tab System Log dan Activity Log Admin Console) lewat kemampuan baca tanpa mengasersi angka absolut (dinyatakan di `suite.md`, disediakan tim FE; bagian 8b butir 10). Langkah "Catat baseline" mencatat jumlah entri sebelum pemicu; asersi memakai selisih terhadap baseline (S-12).
- Pemulihan baseline: kedua request ditolak sehingga data Pre-setup tidak diubah; kemampuan reset data Pre-setup yang disediakan tim FE/BE (dinyatakan di `suite.md`) dijalankan di hook `before` dan `after` spec ini sebagai jaring pengaman.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Env var `AC_RP_BIG_TC_PASSWORD` baru dan perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user, role, dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

### TC-AC-RP-435: Bulk Remove Role Detail di atas Selection Limit tidak menghasilkan entri log

1. Catat baseline jumlah entri Detail User `Siti Nurhaliza` (pelaku) > Tab System Log dan Activity Log Admin Console pelaku
2. Sesi API `Hadi Gunawan`: kirim request Bulk Remove untuk 101 baris di Role Detail `Manage group`
3. Verifikasi respons request ditolak seluruhnya dengan status 422
4. Verifikasi pesan respons "You've reached the maximum selection of 100 rows."
5. Verifikasi jumlah entri Detail User `Siti Nurhaliza` (pelaku) > Tab System Log sama dengan baseline langkah 1 (selisih 0, tidak ada entri log)
6. Verifikasi jumlah entri Activity Log Admin Console pelaku sama dengan baseline langkah 1 (selisih 0, tidak ada entri log)

### TC-AC-RP-436: Assign Total Control melebihi Selection Limit tidak menghasilkan entri log

7. Catat baseline jumlah entri Detail User `Siti Nurhaliza` (pelaku) > Tab System Log dan Activity Log Admin Console pelaku
8. Sesi API `Hadi Gunawan`: kirim request Assign Total Control untuk 101 user
9. Verifikasi respons request ditolak seluruhnya dengan status 422
10. Verifikasi pesan respons "You've reached the maximum selection of 100 rows."
11. Verifikasi jumlah entri Detail User `Siti Nurhaliza` (pelaku) > Tab System Log sama dengan baseline langkah 7 (selisih 0, tidak ada entri log)
12. Verifikasi jumlah entri Activity Log Admin Console pelaku sama dengan baseline langkah 7 (selisih 0, tidak ada entri log)

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Kelas harness g (absence log); request langsung yang ditolak (kelas a) adalah pemicu pembentuk kondisi yang diasersi tidak tercatat (P-5 butir a), bukan objek uji.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03, S-09): langkah 1 dan 7 (baseline jumlah entri audit trail pelaku, satu baseline per TC, S-12).
- Pembagian dengan spec `TC-AC-RP-E2E-116-defense-selection-limit-request-langsung`: spec 116 memuat klausa penolakan, pesan, dan state data TC-AC-RP-435 dan 436; spec ini memuat klausa "tidak ada entri log" (S-05). Status 422 dan pesan respons pada langkah 3, 4, 9, dan 10 hanya menjadi anchor positif asersi absence (bagian 8b butir 2) karena menunjukkan pemicu benar-benar diproses dan ditolak; state data (jumlah pemegang `Manage group` dan Total Control) tidak diasersi ulang di spec ini. TC-AC-RP-435 dan 436 tercantum di `sourceTc` spec 116 dan spec ini karena terbelah antara presence dan absence (S-05).
- Pemulihan baseline: kemampuan reset yang disediakan tim FE/BE (mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; S-13); dijalankan di hook `before` dan `after`.
- Temuan untuk QA:
  - TC-AC-RP-435 dan TC-AC-RP-436 Expected menyebut surface Detail User `Siti Nurhaliza` (pelaku) > Tab System Log dan Activity Log Admin Console dengan selisih 0 terhadap baseline; spec mengasersi keduanya per TC (langkah 5, 6, 11, 12) dengan baseline di langkah 1 dan 7, dibaca lewat kemampuan baca yang disediakan tim FE/BE.
  - TC-AC-RP-435 dan TC-AC-RP-436: Precondition menyebut login `Hadi Gunawan` (entitas Distributor) dan request dikirim sesi `Hadi Gunawan`, sedangkan surface log yang dibaca adalah milik `Siti Nurhaliza` (pelaku, entitas Principal); spec mengikuti teks TC dan mohon QA mengonfirmasi akun pelaku yang dimaksud.
  - TC-AC-RP-435 dan TC-AC-RP-436: 101 baris/user yang dikirim tidak ditentukan siapa saja; spec memilih dari 105 user Standard Pre-setup #20 (S-13).
  - TC-AC-RP-435 dan TC-AC-RP-436 tidak menyebut endpoint, method, atau body request; spec menulis aksi seperti di TC tanpa mengarang endpoint (S-13).
  - Mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
