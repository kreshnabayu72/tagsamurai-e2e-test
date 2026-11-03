---
id: TC-AC-ACAL-E2E-003-empty-state-genuinely-kosong-kedua-tab
title: "Empty State Genuinely Kosong Kedua Tab"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-05
  - TC-AC-ACAL-06
coverage:
  web: automated
---

# Empty State Genuinely Kosong Kedua Tab

## Prerequisites

- Mode: FE+BE (backend nyata dengan intercept parsial pada respons List; bukan resilience).
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; kredensial `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Email akun memuat placeholder `{namaCompany}` seperti di Pre-setup TC (lihat Temuan untuk QA).
- Kemampuan teknis (disediakan tim FE): intercept respons HTTP List Session (`session-logs/list`) dan List User Action (`change-logs/list`) agar mengembalikan 0 baris, lalu melepas intercept. TC-AC-ACAL-05 mensyaratkan intercept karena sesi aktor sendiri selalu tercatat; TC-AC-ACAL-06 mengizinkan entitas baru tanpa aksi atau intercept, dan spec memakai intercept yang sama supaya akun tidak perlu entitas khusus. Intercept dipasang tepat sebelum halaman meminta ulang data dan dilepas segera setelah asersi tiap TC (S-09); hook `after` melepas intercept yang tersisa.
- Data: tidak ada data log yang dibuat atau dibaca; state backend tidak diubah.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACAL-05: Empty state genuinely kosong, Tab Session

1. Pasang intercept List Session dengan respons 0 baris
2. Buka Admin Console > Activity Log > Session dengan memuat ulang halaman (F5)
3. Verifikasi tab Session: ilustrasi empty state dengan Title `No activity yet` dan Description `Admin Console session activity — when your staff open and close access — will appear here.`
4. Verifikasi tab Session: tanpa tombol aksi
5. Lepas intercept List Session

### TC-AC-ACAL-06: Empty state genuinely kosong, Tab User Action

6. Pasang intercept List User Action dengan respons 0 baris
7. Klik tab "User Action"
8. Verifikasi tab User Action: ilustrasi empty state dengan Title `No activity yet` dan Description `Admin Console user actions and changes will appear here.`
9. Verifikasi tab User Action: tanpa tombol aksi
10. Lepas intercept List User Action

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-05, 06). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 dan 6 (memasang intercept sesuai precondition TC), langkah 5 dan 10 (melepas intercept), dan memuat ulang halaman (F5) pada langkah sesudah 1 supaya List Session diminta ulang setelah intercept terpasang.
- Intercept hanya memaksa respons 0 baris sebagai kondisi data, bukan kegagalan server, sehingga spec bukan kelas harness b dan tidak memakai `P-2`.
- Ilustrasi, Title, dan Description empty state ditulis satu `Verifikasi` karena Expected TC menyebutnya sebagai satu butir utuh (S-01).
- Temuan untuk QA:
  - TC-06 menyebut dua cara memicu kondisi (entitas baru tanpa aksi, atau intercept); spec memilih intercept untuk keduanya.
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD` (akun `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`), terdaftar di `.env.example` dan `spectra.config.ts`.
