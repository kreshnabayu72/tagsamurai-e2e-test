---
id: TC-AC-ACAL-E2E-004-loading-state-dan-no-result-akibat-search-dan-filter
title: "Loading State dan No-result Akibat Search dan Filter"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-04
  - TC-AC-ACAL-07
  - TC-AC-ACAL-08
coverage:
  web: automated
---

# Loading State dan No-result Akibat Search dan Filter

## Prerequisites

- Mode: FE+BE (backend nyata; respons List ditahan hanya untuk mengamati loading, bukan kegagalan).
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; kredensial `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Email akun memuat placeholder `{namaCompany}` seperti di Pre-setup TC (lihat Temuan untuk QA).
- Data Log: tab Session dan tab User Action memuat sedikitnya satu baris (Pre-setup No 9 dan No 10); tidak ada entri Session maupun User Action bertanggal `1 Jan 2020` pada entitas aktor (precondition TC-AC-ACAL-08). Seeding log disediakan tim FE/BE.
- Kemampuan teknis (disediakan tim FE): menahan dan melepas respons List Session (`session-logs/list`) dan List User Action (`change-logs/list`) (throttle atau intercept). Penahanan dilepas pada langkah spec dan di hook `after`.
- Nilai uji: Search `zzznotfound`; Filter Date `1 Jan 2020`–`1 Jan 2020`.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACAL-04: Loading state tabel, kedua tab

1. Tahan respons List Session dan List User Action
2. Buka Admin Console > Activity Log > Session dengan memuat ulang halaman (F5)
3. Verifikasi tab Session: loading component tampil di area tabel
4. Klik tab "User Action"
5. Verifikasi tab User Action: loading component tampil di area tabel
6. Lepas penahanan respons List Session dan List User Action
7. Verifikasi tab User Action: tabel normal tampil
8. Verifikasi tab User Action: pagination tampil
9. Klik tab "Session"
10. Verifikasi tab Session: tabel normal tampil
11. Verifikasi tab Session: pagination tampil

### TC-AC-ACAL-07: No-result state akibat Search, kedua tab

12. Ketik Search `zzznotfound`, tekan Enter
13. Verifikasi tab Session: ilustrasi dengan Title `No results found` dan Description `Try adjusting your search or filter.`
14. Verifikasi tab Session: bukan alert error
15. Klik `(←)` pada kotak Search tab Session
16. Klik tab "User Action"
17. Ketik Search `zzznotfound`, tekan Enter
18. Verifikasi tab User Action: ilustrasi dengan Title `No results found` dan Description `Try adjusting your search or filter.`
19. Verifikasi tab User Action: bukan alert error
20. Klik `(←)` pada kotak Search tab User Action

### TC-AC-ACAL-08: No-result state akibat Filter, kedua tab

21. Klik icon Filter, pilih Date `1 Jan 2020`–`1 Jan 2020`, klik `[Apply]`
22. Verifikasi tab User Action: ilustrasi dengan Title `No results found` dan Description `Try adjusting your search or filter.`
23. Klik tab "Session"
24. Klik icon Filter, pilih Date `1 Jan 2020`–`1 Jan 2020`, klik `[Apply]`
25. Verifikasi tab Session: ilustrasi dengan Title `No results found` dan Description `Try adjusting your search or filter.`

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-04, 07, 08). Tidak ada TC hanya-BE di spec ini.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 dan 6 (menahan dan melepas respons sesuai precondition dan langkah 3 TC-04), langkah 9 (kembali ke tab Session untuk mengamati hasil pelepasan pada tab itu), langkah 15 dan 20 (mengosongkan kotak Search tiap tab supaya Filter pada TC-08 tidak bercampur dengan Search TC-07), dan langkah 23 (berpindah ke tab Session setelah Filter pada tab User Action).
- TC-04 menahan respons List kedua tab sejak halaman dimuat ulang; asersi loading memakai respons yang ditahan (bukan kelas b), sehingga digabung di spec fungsional ini.
- Pada TC-08 Filter Date diterapkan dari tab yang sedang aktif lebih dulu (User Action) lalu Session; urutan ini berbeda dari TC (Session lalu User Action) demi menghemat satu perpindahan tab, dan Expected TC-08 a dan b tetap diasersi satu per satu.
- "No results found" yang diproses Search atau Filter menjadi anchor positif bahwa tabel sudah termuat (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-04 tidak menyebut apakah penahanan berlaku untuk permintaan tab User Action yang baru dipicu saat tab diklik; spec menahan respons kedua tab sejak awal.
  - TC-04 Expected c menyebut "(S-05)" sebagai rujukan state PRD §7; spec mengasersi tabel normal dan pagination tampil.
  - TC-08 hanya menyebut "pilih Date `1 Jan 2020`–`1 Jan 2020`" tanpa cara memilih tanggal pada Filter Panel; langkah mengikuti TC.
  - Email akun Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD` (akun `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`), terdaftar di `.env.example` dan `spectra.config.ts`.
