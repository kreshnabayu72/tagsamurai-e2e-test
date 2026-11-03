---
id: TC-AC-ACAL-E2E-002-urutan-default-dan-tie-break-kedua-tab
title: "Urutan Default dan Tie-break Kedua Tab"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACAL-11
  - TC-AC-ACAL-12
  - TC-AC-ACAL-174
coverage:
  web: automated
---

# Urutan Default dan Tie-break Kedua Tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; kredensial `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Email akun memuat placeholder `{namaCompany}` seperti di Pre-setup TC (lihat Temuan untuk QA).
- Data Log yang di-seed di hook `before` (kemampuan seeding log dengan stempel waktu yang dapat ditentukan, termasuk stempel identik, disediakan tim FE/BE; lihat Temuan untuk QA):
  - Tab Session: dua entri bertanggal `22 Jun 2026, 10:00` milik `John Doe` dan `Budi Santoso` (stempel identik), satu entri `22 Jun 2026, 09:00`, dan satu entri `22 Jun 2026, 17:30`. Nama subjek literal menurut Lampiran A-3 (S-12) karena asersi bergantung pada singkatan nama dan urutan nama; seeding idempotent (dilewati bila sudah ada) dan tidak dihapus.
  - Tab User Action: tiga entri bertanggal `22 Jun 2026, 14:25`: `Edit`/`PIC Name`, `Edit`/`Email`, dan `Create`/`Company Name` (Name entri bersuffix `{runId}-002`), satu entri `22 Jun 2026, 13:00`, dan satu entri `22 Jun 2026, 14:30`.
  - Tidak ada entri lain bertanggal `22 Jun 2026` pada entitas aktor di luar seed ini; Filter Date `22 Jun 2026`–`22 Jun 2026` membatasi tabel pada tanggal itu (S-14).
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- State global: tidak ada yang diubah. Format tanggal mengikuti General Settings entitas aktor dan tidak diubah.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACAL-11: Urutan default Tab Session

1. Klik tab "Session" tanpa mengubah sort
2. Klik icon Filter, pilih Date `22 Jun 2026`–`22 Jun 2026`, klik `[Apply]`
3. Verifikasi entri `17:30` paling atas
4. Verifikasi entri `09:00` paling bawah
5. Verifikasi pada stempel `10:00`: `Budi S` di atas `John D` (User A-Z menurut nama lengkap)

### TC-AC-ACAL-12: Urutan default Tab User Action

6. Klik tab "User Action" tanpa mengubah sort
7. Klik icon Filter, pilih Date `22 Jun 2026`–`22 Jun 2026`, klik `[Apply]`
8. Verifikasi entri `14:30` paling atas
9. Verifikasi entri `13:00` paling bawah
10. Verifikasi pada stempel `14:25` urutan: `Create`/`Company Name`, `Edit`/`Email`, `Edit`/`PIC Name`

### TC-AC-ACAL-174: Tie-break berlaku juga saat Date diurutkan Oldest First, kedua tab

11. Klik tab "Session"
12. Klik sort Date sekali (Oldest First)
13. Verifikasi Session: `Budi S` di atas `John D` pada stempel `10:00` (User A-Z tetap)
14. Klik tab "User Action"
15. Klik sort Date sekali (Oldest First)
16. Verifikasi User Action: pada stempel `14:25` urutan `Create`/`Company Name`, `Edit`/`Email`, `Edit`/`PIC Name` (Action lalu Field A-Z tetap)

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-11, 12, 174). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 2 dan 7 (Filter Date `22 Jun 2026` membatasi tabel pada entri seed supaya urutan teratas dan terbawah dapat diasersi pada audit trail yang tumbuh; S-14). Langkah 11 dan 14 (klik tab Session dan tab User Action untuk TC-174): TC-174 menyebut kedua tab sebagai konteks ("Tab Session:", "Tab User Action:") tanpa langkah klik dan precondition-nya hanya entri berstempel identik, sehingga klik tab adalah langkah penghubung (S-03). Filter Date tiap tab tetap aktif pada TC-174 karena Filter tiap tab dipertahankan saat berpindah tab.
- Pada TC-174 sort Date dipicu sekali pada tiap tab; Expected TC hanya meminta tie-break tetap, sehingga arah Date (Oldest First) tidak diasersi terpisah.
- Temuan untuk QA:
  - Mekanisme seeding entri log dengan stempel identik tidak didefinisikan di TC, PRD, atau LLD yang dibaca; kemampuan itu diminta dari tim FE/BE.
  - TC-11 dan TC-12 mengasersi "paling atas" dan "paling bawah" tanpa menyebut pembatas; pada audit trail yang tumbuh entri baru bisa berada di atas entri seed, sehingga spec menambah Filter Date `22 Jun 2026`. QA perlu memastikan tidak ada entri lain bertanggal sama pada entitas aktor.
  - Tanggal seed `22 Jun 2026` dikhususkan untuk TC-11, TC-12, dan TC-174 (TC diperbarui 2026-11-02, hasil e2e-audit delta 1); spec lain tidak memakai tanggal ini, sehingga klaim "tidak ada entri lain pada tanggal itu" di Prerequisites terpenuhi pada entitas aktor.
  - Pembatasan tanggal bergantung pada format tanggal General Settings entitas aktor; stempel TC (`22 Jun 2026, 10:00`) diasumsikan format bawaan.
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD` (akun `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`), terdaftar di `.env.example` dan `spectra.config.ts`.
