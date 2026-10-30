---
id: TC-GS-ACTLOG-E2E-039-filter-date-batas-inklusif-rentang-terbalik-dan-sebagian-terisi
title: "Filter Date Kedua Tab: Batas Inklusif, Rentang Terbalik, Sebagian Terisi"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ACTLOG-74
  - TC-GS-ACTLOG-76
  - TC-GS-ACTLOG-77
coverage:
  web: automated
---

# Filter Date Kedua Tab: Batas Inklusif, Rentang Terbalik, Sebagian Terisi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (bersuffix `{runId}-039`): Entri Session untuk user `John Doe {runId}-039` dan entri User Action dengan Name `Acme Corp {runId}-039`, masing-masing enam entri dengan cap waktu seed (zona UTC+07:00) dan tampilan sesuai Date Format `dd MMM yy` dan Time Format `HH:mm`:
  - E1 seed `2026-07-13 23:59:59`, tampil `13 Jul 26, 23:59`.
  - E2 seed `2026-07-14 00:00:00`, tampil `14 Jul 26, 00:00`.
  - E3 seed `2026-07-14 23:59:59`, tampil `14 Jul 26, 23:59`.
  - E4 seed `2026-07-15 00:00:00`, tampil `15 Jul 26, 00:00`.
  - E5 `10 Jul 2026` (jam bebas).
  - E6 `18 Jul 2026` (jam bebas).
  - Himpunan yang sama dipakai TC-GS-ACTLOG-74 dan TC-GS-ACTLOG-77.
- Kemampuan teknis (disediakan tim FE/BE): seed BE entri Session dan User Action dengan timestamp di atas; baris log bertanggal masa lalu tidak dapat dihasilkan lewat aksi nyata modul sumber.
- General Settings (Precondition TC-GS-ACTLOG-74): Date Format `dd MMM yy`, Time Format `HH:mm`, dan Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`. Hook `before` mencatat nilai awal ketiganya lalu menyetelnya ke nilai di atas; hook `after` memulihkannya. Detik `:59` hanya ada pada cap waktu seed sebagai batas dan tidak tampil.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- State global yang diubah: Time Zone, Date Format, dan Time Format General Settings (dipulihkan seperti di atas); pemulihan menambah entri Edit General Settings di User Action dan mengubah Last Updated General Settings. Entri log tidak dapat dihapus (ACTLOG-LOGIC-01); seed memakai nama bersufiks run sehingga run berikutnya tidak bentrok, dan asersi tahan terhadap baris dari run lain. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-ACTLOG-74: Filter Date inklusif di kedua ujung

1. Buka Global Settings > Activity Log > Tab "Session", ketik Search `{runId}-039`, tekan Enter
2. Klik icon Filter, pilih rentang `14 Jul 2026` sampai `14 Jul 2026`, klik [Apply]
3. Verifikasi baris E2 `14 Jul 26, 00:00` dan E3 `14 Jul 26, 23:59` tampil di Tab Session
4. Verifikasi baris E1 `13 Jul 26, 23:59` dan E4 `15 Jul 26, 00:00` tidak tampil di Tab Session
5. Klik tab "User Action", ketik Search `{runId}-039`, tekan Enter
6. Klik icon Filter, pilih rentang `14 Jul 2026` sampai `14 Jul 2026`, klik [Apply]
7. Verifikasi baris E2 `14 Jul 26, 00:00` dan E3 `14 Jul 26, 23:59` tampil di Tab User Action
8. Verifikasi baris E1 `13 Jul 26, 23:59` dan E4 `15 Jul 26, 00:00` tidak tampil di Tab User Action

### Pemulihan state antar TC

9. Pada Tab User Action klik icon Filter, klik [Clear Field], klik [Apply]; klik tab "Session", klik icon Filter, klik [Clear Field], klik [Apply]

### TC-GS-ACTLOG-76: Tanggal akhir sebelum tanggal mulai tidak dapat dipilih

10. Pada Tab Session klik icon Filter, klik field Date, pilih tanggal mulai `14 Jul 2026`, lalu coba pilih tanggal akhir `10 Jul 2026`
11. Verifikasi tanggal sebelum `14 Jul 2026` tidak dapat dipilih sebagai tanggal akhir di picker Tab Session
12. Tutup Filter Panel tanpa [Apply], klik tab "User Action", klik icon Filter, klik field Date, pilih tanggal mulai `14 Jul 2026`, lalu coba pilih tanggal akhir `10 Jul 2026`
13. Verifikasi tanggal sebelum `14 Jul 2026` tidak dapat dipilih sebagai tanggal akhir di picker Tab User Action

### Pemulihan state antar TC

14. Tutup Filter Panel tanpa [Apply]

### TC-GS-ACTLOG-77: Filter Date dengan hanya tanggal mulai atau hanya tanggal akhir

15. Klik tab "Session", klik icon Filter, isi hanya tanggal mulai `14 Jul 2026`, klik [Apply]
16. Verifikasi baris E2 dan E3 (`14 Jul 2026`) serta E6 (`18 Jul 2026`) tampil di Tab Session
17. Verifikasi baris E5 (`10 Jul 2026`) tidak tampil di Tab Session
18. Klik icon Filter, kosongkan tanggal mulai, isi hanya tanggal akhir `14 Jul 2026`, klik [Apply]
19. Verifikasi baris E5 (`10 Jul 2026`) serta E2 dan E3 (`14 Jul 2026`) tampil di Tab Session
20. Verifikasi baris E6 (`18 Jul 2026`) tidak tampil di Tab Session
21. Klik tab "User Action", klik icon Filter, isi hanya tanggal mulai `14 Jul 2026`, klik [Apply]
22. Verifikasi baris E2 dan E3 (`14 Jul 2026`) serta E6 (`18 Jul 2026`) tampil di Tab User Action
23. Verifikasi baris E5 (`10 Jul 2026`) tidak tampil di Tab User Action
24. Klik icon Filter, kosongkan tanggal mulai, isi hanya tanggal akhir `14 Jul 2026`, klik [Apply]
25. Verifikasi baris E5 (`10 Jul 2026`) serta E2 dan E3 (`14 Jul 2026`) tampil di Tab User Action
26. Verifikasi baris E6 (`18 Jul 2026`) tidak tampil di Tab User Action

### Pemulihan state akhir

27. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md`. Urutan TC-GS-ACTLOG-74, 76, 77 dipertahankan.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1 dan 5 (Search `{runId}-039` menyempitkan tabel ke entri seed milik spec; ditambahkan agar asersi tidak bercampur dengan baris lain; Search dipertahankan per tab sampai langkah 27), langkah pemulihan 9, 14, dan 27, serta langkah 12 yang menutup panel sebelum pindah tab.
- Asersi absence (langkah 4, 8, 17, 20, 23, 26) didahului `Verifikasi` baris lain pada tabel yang sama yang tampil (langkah 3, 7, 16, 19, 22, 25).
- Entri seed TC-GS-ACTLOG-77 (`10`, `14`, `18 Jul 2026`) memakai himpunan E1 sampai E6 yang sama dengan TC-GS-ACTLOG-74; entri E1 dan E4 ikut tampil atau tersaring sesuai rentang dan tidak diasersi pada TC-GS-ACTLOG-77.
- TC-GS-ACTLOG-75 (zona waktu) ada di spec 040.
- Temuan untuk QA:
  - TC-77 tidak menyebut Date Format, Time Format, dan Time Zone; spec memakai nilai yang diatur pada Precondition TC-74.
  - TC-77 menyebut tanggal `10 Jul`, `14 Jul`, `18 Jul 2026` tanpa jam; spec memakai jam bebas untuk E5 dan E6.
  - TC-76 menyebut "coba pilih tanggal akhir `10 Jul 2026`" tanpa Expected tambahan selain tanggal tidak dapat dipilih; asersi mengikuti Expected.
  - Apakah [Apply] menutup Filter Panel atau panel tetap terbuka belum ditetapkan PRD dan TC; langkah "klik icon Filter" sesudah [Apply] (langkah 9, 18, 24) mengikuti pola TC.
  - Post Condition ketiga TC bernilai `-`; tidak diasersi.
