---
id: TC-AC-SU-E2E-179-resilience-error-load-user-list-dan-tab-detail
title: "Resilience Error Load User List dan Tab Responsibilities, Changelog, System Log, dan User Log Menampilkan Pesan Error dengan Try Again"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-SU-20
  - TC-AC-SU-335
  - TC-AC-SU-372
  - TC-AC-SU-407
  - TC-AC-SU-430
coverage:
  web: automated
---

# Resilience Error Load User List dan Tab Responsibilities, Changelog, System Log, dan User Log Menampilkan Pesan Error dengan Try Again

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default suite.
- Tidak ada ganti akun di tengah spec.
- Data Dinamis di-seed di hook `before` lewat Fixture BE (disediakan tim FE/BE) dan dihapus atau dipulihkan di hook `after`; nama dan email bersuffix `{runId}-NNN` (S-12), baseline entri audit trail nol karena nama unik. Data Pre-setup bersama tidak diubah. User milik spec: A `Jane Smith {runId}-179`, email `janesmith+{runId}-179@qwertysystem.net`, Activated, dengan sedikitnya satu baris pada Tab Responsibilities (Approval milik A), Tab Changelog, Tab System Log, dan Tab User Log (data seeding dibaca ulang setelah intercept dilepas).
- Kemampuan teknis (kelas b): `Spectra.intercept()` pada respons HTTP daftar user (500 pada request pertama, normal pada request kedua) dan data tabel tiap tab (500 sampai intercept dilepas); endpoint tidak disebut TC, PRD, atau LLD, sehingga pola request disediakan tim FE/BE tanpa endpoint karangan di spec. Spec memakai backend nyata dengan intercept parsial (bukan `Mode: mock`) karena data pemulihan dibaca dari backend nyata. Intercept dilepas segera setelah asersi kegagalan (S-09).
- Suite berjalan serial (`parallel: false`). Env var yang dipakai sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo (lihat suite.md).

## Test Steps

### TC-AC-SU-20: Error load User List
1. Atur intercept: respons request pertama daftar user dikembalikan 500, request kedua normal
2. Klik menu Settings > User di sidebar
3. Verifikasi tabel menampilkan icon dengan copy `"Unable to load this data."` dan tombol `[Try Again]` (bukan empty state)
4. Klik `[Try Again]`
5. Verifikasi tabel memuat ulang dan baris user tampil
### TC-AC-SU-335: Error load Tab Responsibilities
6. Ketik Search `Jane Smith {runId}-179`, tekan Enter, lalu klik Name baris A untuk membuka Detail
7. Atur intercept: respons request data tabel Responsibilities dikembalikan 500
8. Klik tab `Responsibilities (N)`
9. Verifikasi tabel menampilkan copy `"Unable to load this data."` dan tombol `[Try Again]` (bukan empty state)
10. Lepas intercept, lalu klik `[Try Again]`
11. Verifikasi tabel Tab Responsibilities menampilkan data
### TC-AC-SU-372: Error load Tab Changelog
12. Atur intercept: respons request data tabel Changelog dikembalikan 500
13. Klik tab `Changelog`
14. Verifikasi tabel menampilkan copy `"Unable to load this data."` dan tombol `[Try Again]` (bukan empty state)
15. Lepas intercept, lalu klik `[Try Again]`
16. Verifikasi tabel Tab Changelog menampilkan data
### TC-AC-SU-407: Error load Tab System Log
17. Atur intercept: respons request data tabel System Log dikembalikan 500
18. Klik tab `System Log`
19. Verifikasi tabel menampilkan copy `"Unable to load this data."` dan tombol `[Try Again]` (bukan empty state)
20. Lepas intercept, lalu klik `[Try Again]`
21. Verifikasi tabel Tab System Log menampilkan data
### TC-AC-SU-430: Error load Tab User Log
22. Atur intercept: respons request data tabel User Log dikembalikan 500
23. Klik tab `User Log`
24. Verifikasi tabel menampilkan copy `"Unable to load this data."` dan tombol `[Try Again]` (bukan empty state)
25. Lepas intercept, lalu klik `[Try Again]`
26. Verifikasi tabel Tab User Log menampilkan data

## Notes

- Langkah penghubung tanpa Verifikasi (S-03): pemasangan dan pelepasan intercept, Search baris target dan pembukaan Detail (R-16), dan pemilihan tab.
- Asersi "bukan empty state" ditulis dalam satu `Verifikasi` dengan copy dan tombol error karena Expected TC menyebutnya dalam satu butir; TC-20 menambah icon pada butir yang sama.
- TC-AC-SU-447, TC-AC-SU-483, dan TC-AC-SU-507 (error load modal Changelog) ada di spec 200.
- Temuan untuk QA:
  - TC-20 menyatakan "Endpoint list mengembalikan 5xx pada request pertama, normal pada request kedua"; spec memasang intercept sebelum membuka ulang Settings > User lewat sidebar.
  - TC-335 sampai TC-430 menyebut "Response: 500" tanpa endpoint; spec menyatakannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-335 menyebut tab `Responsibilities (N)` tanpa menyebut nilai N; spec mengklik tab berlabel `Responsibilities` dengan hitungan apa pun. TC memakai nama literal `Jane Smith`; spec memakai nama bersuffix (S-12).
