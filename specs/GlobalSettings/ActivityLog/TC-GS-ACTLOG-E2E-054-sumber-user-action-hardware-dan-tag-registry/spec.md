---
id: TC-GS-ACTLOG-E2E-054-sumber-user-action-hardware-dan-tag-registry
title: "Sumber User Action: Hardware (BLE Gateway)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-205
coverage:
  web: automated
---

# Sumber User Action: Hardware (BLE Gateway)

## Prerequisites

- Mode: FE+BE.
- Akun pengamat: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control Client A). Password tidak ditulis di spec atau fixture. Akun ini membaca Changelog dan Activity Log; aksi sumber tidak dijalankan olehnya.
- Akun pelaku aksi sumber: admin `Hendra Pratama` (Client A), `Fixture.activityLog.adminHendra` (email ditetapkan tim FE, fixture baru), kredensial `Spectra.env.GS_HENDRA_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Aksi sumber (aktifkan BLE Gateway) dijalankan lewat sesi API admin ini; kemampuan itu dan kapabilitas aktivasi BLE Gateway disediakan tim FE/BE tanpa mengarang endpoint. Nilai Modified By yang diasersi `Hendra P`.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Data Pre-setup: tidak ada data tetap yang diubah atau dipakai sebagai target aksi.
- Data Dinamis (bersuffix per run, dibersihkan di hook `after` tanpa berasumsi seeding berhasil penuh): BLE Gateway `BLE Gateway {runId}-054` berstatus nonaktif, di-seed lewat API di hook `before`; diaktifkan oleh admin `Hendra Pratama` lewat sesi API pada TC-GS-ACTLOG-205; dihapus di hook `after`.
- Kemampuan teknis: akses baca Changelog modul Hardware (BLE Gateway) untuk menyalin baris aksi yang sama beserta kolom Date.
- Spec hanya menambah baris log. Suite serial (`parallel: false`) mengikuti `suite.md`.

## Test Steps

### TC-GS-ACTLOG-205: Aksi di modul Hardware tercatat di Tab User Action

1. Lewat sesi API admin `Hendra Pratama`, aktifkan BLE Gateway `BLE Gateway {runId}-054` dan tunggu respons sukses
2. Buka Changelog modul Hardware (BLE Gateway) dan catat baris Changelog aksi Activate BLE Gateway (Object, Name, Field, Old Value, New Value, Date)
3. Buka Global Settings > Activity Log > User Action
4. Ketik Search `BLE Gateway {runId}-054`, tekan Enter
5. Verifikasi entri dengan Action `Activate BLE Gateway` untuk `BLE Gateway {runId}-054` tampil
6. Verifikasi Object, Name, Field, Old Value, dan New Value entri identik dengan baris Changelog modul Hardware yang dicatat pada langkah 2
7. Verifikasi Modified By entri `Hendra P`
8. Verifikasi Date entri sama dengan Date baris Changelog yang dicatat pada langkah 2

### Pemulihan state akhir spec

9. Klik `(←)` pada kotak Search

## Notes

- Sumber: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 2 (membaca baris Changelog modul sumber sebagai pembanding Expected "identik dengan baris Changelog" dan Date); langkah 9 (membersihkan Search). Aksi sumber lewat API menunggu respons sukses sebelum langkah berikutnya (S-03). Subjudul "Pemulihan state" bukan TC sumber.
- Baseline entri adalah nol karena nama BLE Gateway bersuffix unik per run (S-12).
- Pembagian TC lintas spec: TC-GS-ACTLOG-206 ada di spec 037; TC-GS-ACTLOG-199, 200, dan 201 ada di spec 052; TC-GS-ACTLOG-202, 203, 204, dan 210 di spec 053; TC-GS-ACTLOG-207, 208, dan 209 di spec 055.
- Temuan untuk QA:
  - Email admin `Hendra Pratama` (Modified By `Hendra P`) dan cara menjalankan aksi lewat sesi API ditetapkan tim FE (fixture `Fixture.activityLog.adminHendra`).
  - TC-GS-ACTLOG-205 tidak menyebut lokasi Changelog modul Hardware (BLE Gateway); spec membaca Changelog modul itu.
  - TC-GS-ACTLOG-205 menyebut BLE Gateway tanpa nama; spec memakai nama bersuffix per run.
