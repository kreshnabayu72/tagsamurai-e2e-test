---
id: TC-AC-RP-E2E-004-screening-tab-read-only
title: "Screening Tab Read Only: Toolbar, Kolom, Baris, Row Action, dan Placeholder Search"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-15
  - TC-AC-RP-16
  - TC-AC-RP-17
coverage:
  web: automated
---

# Screening Tab Read Only: Toolbar, Kolom, Baris, Row Action, dan Placeholder Search

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: Tabel Data Uji Pre-setup #11 (tree group Principal) dan #13 (pemegang Read Only: `Dewi Anggraini`, Auditor, Finance, Modified By "Bambang H", Last Updated "16 Jun 2026, 09:00"; `Lisa Wong`, HR Officer, HR, Inactive, "Siti N", "16 Jun 2026, 09:05"). Berkas fixture Pre-setup modul belum ada dan disediakan tim FE.
- Spec read-only: tidak membuat, mengubah, atau menghapus data; aksi `Remove` tidak dijalankan. Tidak ada data Dinamis, seeding, atau suffix `{runId}`. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_TC_PASSWORD` adalah nama baru; harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-15: Screening Tab Read Only

1. Klik tab `Read Only`
2. Susuri toolbar, header tabel, dan baris
3. Verifikasi Toolbar sama dengan Tab Total Control: Search, Filter, Download, Changelog, "+ Assign"
4. Verifikasi kolom default sama dengan Tab Total Control: Name, Position, Division, Status, Modified By, Last Updated, Actions
5. Verifikasi tidak ada kolom CRUD
6. Verifikasi 2 baris berurutan Name A-Z: `Dewi Anggraini` lalu `Lisa Wong`
7. Verifikasi baris `Dewi Anggraini`: Position "Auditor", Division "Finance", Status `Active`, Modified By "Bambang H", Last Updated "16 Jun 2026, 09:00"
8. Verifikasi baris `Lisa Wong`: Position "HR Officer", Division "HR", Status `Inactive`, Modified By "Siti N", Last Updated "16 Jun 2026, 09:05"
9. Verifikasi tidak ada baris Default User di Tab Read Only

### TC-AC-RP-16: Overlay row action Tab Read Only

10. Klik `⋯` pada baris `Lisa Wong`
11. Verifikasi overlay memuat aksi `Remove` dalam keadaan enabled
12. Verifikasi overlay tidak memuat aksi lain
13. Tutup overlay row action

### TC-AC-RP-17: Placeholder Search Tab Read Only

14. Klik ikon Search
15. Verifikasi field Search terbuka dengan placeholder "Search name..."
16. Klik `(←)` pada kotak Search untuk menutup input

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Seluruh TC spec ini TC FE; spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Langkah penghubung tanpa awalan Verifikasi (S-03): langkah 2 (susur toolbar, header, dan baris yang menjadi prasyarat asersi), langkah 13 (menutup overlay row action), dan langkah 16 (menutup input Search agar spec berakhir tanpa state Search terbuka, S-09).
- Pemecahan Expected c TC-AC-RP-15 (dua baris dengan nilai kolom masing-masing) menjadi tiga Verifikasi mengikuti S-01 (urutan, lalu isi tiap baris).
- Temuan untuk QA:
  - TC-AC-RP-15 Expected b menyebut kolom default "sama dengan Tab Total Control" sehingga asersi mengacu daftar kolom TC-AC-RP-2; tidak ada nilai independen.
  - TC-AC-RP-17 tidak menyatakan cara menutup input Search; spec memakai `(←)` pada kotak Search (konvensi 8b butir 9).
