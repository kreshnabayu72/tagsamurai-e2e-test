---
id: TC-GS-GSET-E2E-002-opsi-select-session-idle-timeout-date-format-dan-time-format
title: "Opsi Select statis"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-GSET-07
  - TC-GS-GSET-08
coverage:
  web: automated
---

# Opsi Select statis

## Prerequisites

- Mode: FE+BE.
- Hook suite (`suite.md`): login akun aktor, flag Guided Tooltip `guided_tooltip_seen_gs-general-settings` disetel seen, record Client A dipulihkan ke baseline, dan halaman Global Settings > General Settings dibuka di `beforeEach`.
- Akun aktor: Total Control (Budi Santoso, Pre-setup No 1) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.GS_TC_PASSWORD`. Login sekali di hook `before`.
- Data Pre-setup No 10 (record Client A, hanya dibaca): Session Idle Timeout `30 minutes`, Date Format `dd/MM/yy`, Time Format `HH:mm`. Spec hanya membuka dan menutup dropdown, tidak memilih opsi, dan tidak menekan `[Save]`. Daftar opsi dibaca dari `Fixture.generalSettings.<kunci>` (berkas `fixtures/generalSettings.json` belum ada; ditandai untuk tahap script).
- Tidak ada state global yang diubah.

## Test Steps

### TC-GS-GSET-07: Opsi Select Session Idle Timeout

1. Klik Select "Session Idle Timeout"
2. Verifikasi opsi berurutan: `15 minutes`, `30 minutes`, `1 hour`, `2 hours`, `4 hours`, `8 hours`
3. Verifikasi tidak ada opsi "Never"
4. Verifikasi tidak ada kotak pencarian di dalam Select (tidak Searchable)
5. Tutup dropdown dengan `Esc`

### TC-GS-GSET-08: Opsi Select Date Format dan Time Format

6. Klik Select "Date Format"
7. Verifikasi 5 opsi berurutan: `dd/MM/yy` (17/03/23, default), `M/d/yy` (3/17/23), `dd MMM yy` (17 Mar 23), `DDD, MMM dd, yy` (Fri, Mar 17, 23), `DDD, MMM dd, yyyy` (Fri, Mar 17, 2023)
8. Verifikasi tidak ada opsi ISO 8601 `YYYY-MM-DD`
9. Verifikasi Select "Date Format" tidak punya kotak pencarian (tidak Searchable)
10. Tutup dropdown dengan `Esc`
11. Klik Select "Time Format"
12. Verifikasi 2 opsi berurutan: `hh:mm a` (02:30 PM), `HH:mm` (14:30, default)
13. Verifikasi Select "Time Format" tidak punya kotak pencarian (tidak Searchable)
14. Tutup dropdown dengan `Esc`

## Notes

- Sumber: `global-settings/general-settings/TestCases/tc-general-settings.md`. 14 langkah, jauh di bawah batas sekitar 35 langkah.
- Langkah penghubung (tanpa `Verifikasi`): langkah 5, 10, dan 14 (menutup dropdown tanpa memilih opsi agar record dan form tidak berubah).
- Asersi absence (langkah 3, 4, 8) didahului `Verifikasi` daftar opsi pada dropdown yang sama (langkah 2 dan 7), sehingga dropdown terbukti sudah termuat.
- Temuan untuk QA:
  - TC-GS-GSET-08 langkah 2 menulis "Tutup, klik Select Time Format" tanpa menyebut cara menutup dropdown; spec memakai `Esc` sebagai langkah penghubung.
