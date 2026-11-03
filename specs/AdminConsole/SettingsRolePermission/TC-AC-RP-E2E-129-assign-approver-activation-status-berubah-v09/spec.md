---
id: TC-AC-RP-E2E-129-assign-approver-activation-status-berubah-v09
title: "Assign Approver: Activation Status User Berubah Menjadi Tidak Eligible (V-09)"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-228
coverage:
  web: automated
---

# Assign Approver: Activation Status User Berubah Menjadi Tidak Eligible (V-09)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `AC_RP_TC_PASSWORD` harus terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Admin B: sesi API sesuai Hook suite "Sesi API aktor" untuk mereset Activation Status user; akun Admin B disediakan tim FE. Email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA). Pelaku kedua lewat sesi API tidak membuka konteks UI kedua.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal), #12 (`Alex Tan` Active Activated), #17 (approver `Manage TAG stock` = `Sarah Kimura`), #24 (Admin B).
- Data Dinamis: spec ini tidak membuat Data Dinamis; user yang diubah Admin B adalah user Pre-setup `Alex Tan`. Nilai bersuffix `+{runId}-129` tidak dipakai karena tidak ada data yang dibuat spec.
- Perubahan Pre-setup: Activation Status `Alex Tan` menjadi bukan Activated (reset aktivasi). Pemulihan ke Activated memakai kemampuan reset yang dinyatakan di `suite.md` (Pemulihan baseline automation), dijalankan di hook `before` dan `after`. Efek: Changelog Settings > User menerima entri; Last Updated berubah.
- Suite berjalan serial (`parallel: false`).
- Flag Guided Tooltip `guided_tooltip_seen_role-permission`: mengikuti pernyataan di Hook suite `suite.md`.

## Test Steps

### TC-AC-RP-228: Approver yang Activation Status-nya berubah menjadi tidak eligible

1. Klik tab `System`
2. Pada section Global Role, klik `⋯` pada baris `Manage TAG stock` lalu klik `Detail`
3. Klik "+ Assign" pada section Approvers
4. Centang `Alex Tan`
5. Sesi B (sesi API Admin B): ubah Activation Status `Alex Tan` menjadi bukan Activated (reset aktivasi) hingga tersimpan
6. Sesi A: klik `[Assign]`
7. Verifikasi alert "Alex Tan is no longer eligible. Please select another."
8. Klik `✕` pada popup
9. Verifikasi tabel Approvers memuat `Sarah Kimura`
10. Verifikasi tidak ada approver ditambahkan: tabel Approvers tidak memuat `Alex Tan`

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular. Tanda "→" pada kolom Langkah Uji TC tidak diasersi.
- Pembagian TC lintas spec: TC-AC-RP-225, TC-AC-RP-226, dan TC-AC-RP-229 ada di spec 068; TC-AC-RP-223, TC-AC-RP-224, dan TC-AC-RP-227 ada di spec 067.
- Langkah penghubung (S-03): langkah 8 (tutup popup tanpa dialog Unsaved Changes karena popup picker bukan form), 9 (anchor positif untuk asersi absence langkah 10, bagian 8b butir 2).
- Langkah 5 memakai sesi API Admin B hanya sebagai pemicu perubahan state; tidak memakai `P-2`.
- Temuan untuk QA:
  - TC-AC-RP-228 menyebut "dua sesi paralel" (Manual Only kriteria d) dengan Sesi B hanya memicu perubahan state; spec memakai sesi API. Bila QA menghendaki sesi UI kedua, spec dipindah ke kelas c.
  - TC-AC-RP-228 Expected "tidak ada approver ditambahkan" tidak punya langkah observasi; spec mengamatinya dengan menutup popup dan membaca tabel Approvers (langkah 8 sampai 10).
  - Mekanisme "reset aktivasi" lewat Admin B dan pemulihannya tidak didefinisikan di TC, PRD, atau LLD (S-13); ditulis sebagai kemampuan yang disediakan tim FE/BE.
  - Email Admin B (Pre-setup #24) tidak tertulis; ditulis "disediakan tim FE".
