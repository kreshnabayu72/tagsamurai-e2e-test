---
id: TC-FA-FAAL-E2E-077-halaman-tanpa-kontrol-ubah-tab-user-action
title: "Halaman Activity Log Tanpa Kontrol Ubah, Hapus, atau Buat (Tab User Action)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-FAAL-261
coverage:
  web: automated
---

# Halaman Activity Log Tanpa Kontrol Ubah, Hapus, atau Buat (Tab User Action)

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Reports & Logs > Activity Log.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Data: Data Log Tab User Action UA-01 sampai UA-15 (Pre-setup #12), 15 baris, dan Data Log Tab Session SS-01 sampai SS-11 (Pre-setup #11), dipulihkan ke keadaan Pre-setup oleh fixture backend sebelum spec. Baris terbaru Tab User Action: UA-01 (18/06/26 14:30). Format Date mengikuti General Settings default staf (`dd/MM/yy`, `HH:mm`, `(UTC+07:00) Bangkok, Hanoi, Jakarta`).
- Flag Guided Tooltip: mengikuti butir "Flag Guided Tooltip" di `suite.md` (flag akun Total Control bernilai true lewat hook suite).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).

## Test Steps

### TC-FA-FAAL-261: Halaman tidak memiliki kontrol ubah, hapus, atau buat

1. Klik tab User Action
2. Verifikasi Toolbar hanya memuat `Search | Filter | Download`
3. Verifikasi tidak ada tombol Create, kolom Checkbox, maupun row action
4. Klik sel Name baris UA-01
5. Verifikasi Breadcrumb tetap tampil
6. Verifikasi klik sel Name tidak membuka halaman, popup, maupun drawer
7. Klik sel Action baris UA-01
8. Verifikasi Breadcrumb tetap tampil
9. Verifikasi klik sel Action tidak membuka halaman, popup, maupun drawer
10. Klik kanan baris UA-01
11. Klik header Actions (⋯)
12. Verifikasi header Actions (⋯) hanya membuka Column Visibility

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- TC-FA-FAAL-4, 6, dan 9 ada di spec 002.
- Langkah penghubung (S-03): langkah 1 (klik tab User Action agar klik sel Name, Action, dan baris UA-01 dilakukan di tab yang sesuai), langkah 5 dan 8 (anchor positif Breadcrumb tetap tampil, sebelum asersi absence popup, drawer, dan halaman, Expected b TC-FA-FAAL-261).
- Temuan untuk QA:
  - TC-FA-FAAL-261 langkah 3 ("klik kanan baris UA-01") tidak punya Expected sendiri; spec melakukan klik kanan pada langkah 10 tanpa `Verifikasi` tambahan (S-02).
