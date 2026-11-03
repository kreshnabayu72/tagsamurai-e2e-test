---
id: TC-FA-FAAL-E2E-002-screening-tab-user-action-loading-dan-halaman-tanpa-kontrol-tulis
title: "Screening Tab User Action, Urutan Default, dan Loading"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAL-4
  - TC-FA-FAAL-6
  - TC-FA-FAAL-9
coverage:
  web: automated
---

# Screening Tab User Action, Urutan Default, dan Loading

## Prerequisites

- Mode: FE+BE. Platform: web, Fixed Asset > Reports & Logs > Activity Log. Penundaan respons list (TC-FA-FAAL-9) memakai intercept jaringan parsial di atas backend nyata.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Env var `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture.
- Data: Data Log Tab User Action UA-01 sampai UA-15 (Pre-setup #12), 15 baris, dan Data Log Tab Session SS-01 sampai SS-11 (Pre-setup #11), dipulihkan ke keadaan Pre-setup oleh fixture backend sebelum spec. Baris terbaru Tab User Action: UA-01 (18/06/26 14:30). Format Date mengikuti General Settings default staf (`dd/MM/yy`, `HH:mm`, `(UTC+07:00) Bangkok, Hanoi, Jakarta`).
- Kemampuan teknis: intercept jaringan untuk menunda (hold) respons list Tab Session dan respons list Tab User Action lalu melepasnya; intercept dilepas segera setelah dipakai (S-09).
- Flag Guided Tooltip: mengikuti butir "Flag Guided Tooltip" di `suite.md` (flag akun Total Control bernilai true lewat hook suite).
- Seed dan pemulihan lewat API disediakan tim FE/BE (butir "Seed dan pemulihan lewat API" di `suite.md`).
- Identitas data Pre-setup dibaca dari `fixtures/activity-log.json` (belum ada; disediakan tim FE, nama kunci ditetapkan tim FE).

## Test Steps

### TC-FA-FAAL-4: Screening Tab User Action: Header, Body, Footer

1. Klik tab User Action
2. Verifikasi Breadcrumb tampil `Reports & Logs > Activity Log`
3. Verifikasi Tab tampil `Session | User Action`
4. Verifikasi tab User Action aktif
5. Verifikasi Table Tools tampil `Search | Filter | Download`
6. Verifikasi header kolom Date, Action, Object, Name, Field, Old Value, New Value, dan Modified By masing-masing sortable
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
17. Verifikasi sel kolom Action tampil sebagai plain text (bukan badge)

### TC-FA-FAAL-6: Urutan default Tab User Action: Date terbaru di atas

18. Verifikasi baris pertama adalah UA-01 dengan Date `18/06/26, 14:30` (Date Newest First)
19. Verifikasi tidak ada indikator panah sort aktif pada header kolom manapun

### TC-FA-FAAL-9: Loading state saat data dimuat di kedua tab

20. Tunda respons list Tab Session lewat intercept jaringan
21. Muat ulang halaman
22. Verifikasi Loading component tampil pada tabel Tab Session selama respons tertunda
23. Lepas penundaan respons list Tab Session
24. Verifikasi tabel Tab Session tampil dengan data
25. Tunda respons list Tab User Action lewat intercept jaringan
26. Klik tab User Action
27. Verifikasi Loading component tampil pada tabel Tab User Action selama respons tertunda
28. Lepas penundaan respons list Tab User Action
29. Verifikasi tabel Tab User Action tampil dengan data

## Notes

- Sumber: `fixed-asset/activity-log/TestCases/tc-activity-log.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 10 (menutup overlay Column Visibility yang dibuka langkah 8).
- Langkah 8 sampai 9 mengamati klausa Expected "header klik membuka overlay Column Visibility" milik TC-FA-FAAL-4 butir b yang tidak punya langkah klik di TC; klik ditambahkan hanya untuk mengamati klausa itu.
- TC-FA-FAAL-9 menahan respons hanya untuk mengamati Loading; bukan kelas fault injection (bagian 3 prinsip 13b). Loading diasersi selama respons ditahan, sebelum penundaan dilepas (bagian 8b butir 5).
- Langkah 26 membuka tab User Action sesudah penundaan respons list Tab User Action dipasang, sehingga pemuatan list yang dipicu klik tab teramati sebagai Loading.
- Teks footer pada langkah 14 diasersi sebagai format; nilai X, Y, Z tidak diasersi sebagai angka absolut karena log tumbuh (S-12).
- TC-FA-FAAL-261 (halaman tanpa kontrol ubah) ada di spec 077.
- TC-FA-FAAL-3 dan TC-FA-FAAL-5 (Tab Session) ada di spec 063.
- Temuan untuk QA:
  - TC-FA-FAAL-6 butir a menyebut UA-01 sebagai baris pertama; Activity Log adalah audit trail yang tumbuh, sehingga urutan ini hanya terjamin bila log dipulihkan ke Pre-setup (Catatan TC: fixture dipulihkan sebelum tiap TC); pemulihan itu kemampuan tim FE/BE (S-14).
  - TC-FA-FAAL-4 butir b menyebut Column Visibility "unsortable"; cara mengamati "unsortable" tidak disebut TC.
