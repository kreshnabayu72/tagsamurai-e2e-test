---
id: TC-AC-RP-E2E-116-defense-selection-limit-request-langsung
title: "Defense-in-depth: Selection Limit lewat Request Langsung Ditolak (Bulk Remove dan Assign Total Control)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-RP-435
  - TC-AC-RP-436
coverage:
  web: automated
---

# Defense-in-depth: Selection Limit lewat Request Langsung Ditolak (Bulk Remove dan Assign Total Control)

## Prerequisites

- Mode: FE+BE (backend nyata; request langsung ke endpoint modul lewat klien HTTP, tanpa browser)
- Akun aktor: Total Control `Distributor Seleksi Besar` `totalControlBigRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Hadi Gunawan`, Pre-setup #20), password `Spectra.env.AC_RP_BIG_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Flag Guided Tooltip halaman ini mengikuti pernyataan di `suite.md`.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #20 (entitas `Distributor Seleksi Besar` dengan 105 user Standard memegang `Manage group`), #21 (System Limits: Selection Limit 100), dan #25 (klien HTTP). Request berisi 101 baris/user, dipilih dari 105 user Standard tersebut. Kedua request ditolak server; tidak ada Data Dinamis bersuffix `+{runId}-116` yang dibuat spec ini.
- Kemampuan teknis (disediakan tim FE/BE; endpoint tidak ditulis karena tidak disebut TC, PRD, atau LLD): klien HTTP untuk request langsung (Pre-setup #25); sesi API aktor (dinyatakan di `suite.md`); kemampuan membaca state data lewat fixture BE (jumlah pemegang `Manage group` dan jumlah pemegang Total Control di entitas `Distributor Seleksi Besar`). Volume 105 user bukan hasil seed spec ini (Pre-setup #20).
- Pemulihan baseline: kedua request ditolak sehingga data Pre-setup tidak diubah; kemampuan reset data Pre-setup yang disediakan tim FE/BE (dinyatakan di `suite.md`) dijalankan di hook `before` dan `after` spec ini sebagai jaring pengaman.
- Suite berjalan serial (`parallel: false`).
- Env var `AC_RP_BIG_TC_PASSWORD` baru dan perlu terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`.
- Fixture `fixtures/settings-role-permission.json` belum ada; nama user, role, dan group pada langkah ditulis sesuai TC sampai fixture dibuat.

## Test Steps

1. Catat lewat fixture BE sebagai baseline: jumlah pemegang `Manage group` dan jumlah pemegang Total Control di entitas `Distributor Seleksi Besar`

### TC-AC-RP-435: Bulk Remove Role Detail di atas Selection Limit

2. Sesi API `Hadi Gunawan`: kirim request Bulk Remove untuk 101 baris di Role Detail `Manage group`
3. Verifikasi respons request ditolak seluruhnya dengan status 422
4. Verifikasi pesan respons "You've reached the maximum selection of 100 rows."
5. Verifikasi lewat fixture BE bahwa jumlah pemegang `Manage group` sama dengan baseline langkah 1 (tidak ada baris terhapus)

### TC-AC-RP-436: Assign Total Control melebihi Selection Limit

6. Sesi API `Hadi Gunawan`: kirim request Assign Total Control untuk 101 user
7. Verifikasi respons request ditolak seluruhnya dengan status 422
8. Verifikasi pesan respons "You've reached the maximum selection of 100 rows."
9. Verifikasi lewat fixture BE bahwa jumlah pemegang Total Control sama dengan baseline langkah 1 (tidak ada user menjadi Total Control)

## Notes

- K-1: TC-AC-RP-435 dan TC-AC-RP-436 adalah TC defense-in-depth (kelas a) dengan Expected respons API; tetap berada di spec FE+BE karena TC granular adalah sumber dan tiap TC tepat satu spec, walau isinya tumpang tindih dengan `tc-settings-role-permission-backend.md`; BE mencatatnya pada tingkat endpoint.
- Asersi hanya status respons, pesan respons, dan state data lewat fixture BE (bagian 8b butir 1); perilaku FE untuk respons yang sama tidak diasersi di spec ini.
- Langkah penghubung (S-03): langkah 1 (baseline state).
- Temuan untuk QA:
  - TC-AC-RP-435 dan TC-AC-RP-436: Expected "tidak ada entri log" di Detail User `Siti Nurhaliza` (pelaku) > Tab System Log dan Activity Log Admin Console (selisih 0) beserta Langkah baseline jumlah entri log itu tidak diasersi di spec ini; baseline dan asersinya ada di spec 138. Baseline langkah 1 spec ini adalah baseline state data (pemegang), bukan baseline log. Request langsung yang ditolak (kelas a) bukan state berat menurut `P-1`; asersi absence log atas penolakan itu masuk spec absence (kelas g) dengan request ini sebagai pemicu (S-05, `P-5` butir a) dengan baseline sendiri. Asersi itu ada di spec `TC-AC-RP-E2E-138-absence-log-selection-limit-request-langsung` (kelas g), yang memuat TC-AC-RP-435 dan 436 di `sourceTc` bersama spec ini.
  - TC-AC-RP-435 dan TC-AC-RP-436: 101 baris/user yang dikirim tidak ditentukan siapa saja; spec memilih dari 105 user Standard Pre-setup #20 (S-13).
  - TC-AC-RP-435 dan TC-AC-RP-436 tidak menyebut endpoint, method, atau body request; spec menulis aksi seperti di TC tanpa mengarang endpoint (S-13).
  - Mekanisme "dipulihkan automation baseline" tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
