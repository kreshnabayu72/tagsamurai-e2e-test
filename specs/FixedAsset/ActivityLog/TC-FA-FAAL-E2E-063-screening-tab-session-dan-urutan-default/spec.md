---
id: TC-FA-FAAL-E2E-063-screening-tab-session-dan-urutan-default
title: "Screening Tab Session dan Urutan Default Tab Session"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-3
  - TC-FA-FAAL-5
coverage:
  web: automated
---

# Screening Tab Session dan Urutan Default Tab Session

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Reports & Logs > Activity Log > Session.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Data: Data Log Tab Session SS-01 sampai SS-11 (Pre-setup #11), 11 baris, dipulihkan ke keadaan Pre-setup oleh fixture backend sebelum spec. Urutan Date terbaru ke terlama: SS-11 (16/07/26 09:00), SS-10 (16/07/26 08:00), lalu SS-09 dan seterusnya sampai SS-01 (14/07/26 08:05). Format Date mengikuti General Settings default staf (`dd/MM/yy`, `HH:mm`, `(UTC+07:00) Bangkok, Hanoi, Jakarta`).
- Flag Guided Tooltip: mengikuti butir "Flag Guided Tooltip" di `suite.md` (flag akun Total Control bernilai true lewat hook suite).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).

## Test Steps

### TC-FA-FAAL-3: Screening Tab Session: Header, Body, Footer

1. Klik tab Session
2. Verifikasi Breadcrumb tampil `Reports & Logs > Activity Log`
3. Verifikasi Tab tampil `Session | User Action`
4. Verifikasi tab Session aktif
5. Verifikasi Table Tools tampil `Search | Filter | Download`
6. Verifikasi header kolom Date, User, Employee ID, Position, Division, Activity, Status, Note, IP Address, dan Device/Browser masing-masing sortable
7. Verifikasi header kolom Column Visibility (⋯) unsortable
8. Klik header kolom Column Visibility (⋯)
9. Verifikasi overlay Column Visibility terbuka
10. Tutup overlay Column Visibility
11. Verifikasi body tanpa row action
12. Verifikasi baris data tampil
13. Verifikasi tabel menampilkan 10 baris per halaman
14. Verifikasi footer menampilkan teks berformat `Showing X–Y of Z entries`
15. Verifikasi Rows per page `10`
16. Verifikasi kontrol `[← Prev] [Page] [Next →]` tampil

### TC-FA-FAAL-5: Urutan default Tab Session: Date terbaru di atas

17. Verifikasi baris pertama adalah SS-11 dengan Date `16/07/26, 09:00` (Date Newest First)
18. Verifikasi baris kedua adalah SS-10 dengan Date `16/07/26, 08:00`
19. Verifikasi tidak ada indikator panah sort aktif pada header kolom manapun

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 (memastikan tab Session aktif), langkah 10 (menutup overlay Column Visibility yang dibuka langkah 8).
- Langkah 8 sampai 9 mengamati klausa Expected "header klik membuka overlay Column Visibility" milik TC-FA-FAAL-3 butir b yang tidak punya langkah klik di TC; klik ditambahkan hanya untuk mengamati klausa itu.
- Teks footer pada langkah 14 diasersi sebagai format; nilai X, Y, Z tidak diasersi sebagai angka absolut karena log tumbuh (S-12).
- TC-FA-FAAL-1, 2 ada di spec 001; TC-FA-FAAL-4, 6 ada di spec 002.
- Temuan untuk QA:
  - TC-FA-FAAL-5 butir a menyebut SS-11 di baris pertama; Activity Log adalah audit trail yang tumbuh, sehingga urutan ini hanya terjamin bila log dipulihkan ke Pre-setup (Catatan TC: fixture dipulihkan sebelum tiap TC). Pemulihan itu dinyatakan sebagai kemampuan tim FE/BE (S-14).
  - TC-FA-FAAL-3 butir b menyebut Column Visibility "sortable atau unsortable" sebagai atribut kolom; cara mengamati "unsortable" (tidak ada indikator atau sort tidak berubah saat diklik) tidak disebut TC.
