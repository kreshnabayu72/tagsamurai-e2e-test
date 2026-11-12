---
id: TC-AC-ACAL-E2E-047-screening-layout-tab-user-action-dan-tanpa-kontrol-tulis
title: "Screening Layout 3 Zona Tab User Action dan Tanpa Kontrol Tulis"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-02
  - TC-AC-ACAL-17
coverage:
  web: automated
---

# Screening Layout 3 Zona Tab User Action dan Tanpa Kontrol Tulis

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1; kredensial `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture; nama env `AC_TC_PASSWORD` mengikuti bagian 5 konvensi dan sudah terdaftar di `.env.example` dan `spectra.config.ts`. Email akun memuat placeholder `{namaCompany}` seperti di Pre-setup TC (lihat Temuan untuk QA).
- Data Log (dipakai sebagai precondition TC dan diasersi sebagai baris pembanding): tab User Action memuat sedikitnya dua baris dengan nilai Date berbeda (Pre-setup No 10); tab Session memuat sedikitnya satu baris (Pre-setup No 9). Mekanisme seeding log tidak didefinisikan di TC, PRD, atau LLD yang dibaca; seeding disediakan tim FE/BE (lihat Temuan untuk QA). Tidak ada total entri yang diasersi.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Kemampuan teknis (disediakan tim FE): tombol Esc untuk menutup Overlay Column Visibility.
- State global: tidak ada yang diubah (spec read-only, tanpa aksi tulis).
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### TC-AC-ACAL-02: Screening 3 zona Tab User Action

1. Klik tab "User Action"
2. Verifikasi Header: Breadcrumb `Activity Log > User Action`
3. Verifikasi Header: segmen `User Action` pada Breadcrumb bukan link
4. Verifikasi Header: Tab `Session | User Action (aktif)`
5. Verifikasi Header: Table Tools memuat `Search | Filter | Download`
6. Verifikasi Header: Table Tools rata kanan
7. Verifikasi Header: tidak ada tombol create
8. Verifikasi Body: kolom `Date (sortable) | Action (sortable) | Object (sortable) | Name (sortable) | Field (sortable) | Old Value (sortable) | New Value (sortable) | Modified By (sortable) | Actions (⋯)`
9. Klik header kolom `⋯`
10. Verifikasi header `⋯` membuka Overlay Column Visibility
11. Tutup Overlay Column Visibility dengan `Esc`
12. Verifikasi Body: sel kolom Actions (⋯) pada tiap baris kosong dan tidak ada row action
13. Verifikasi Body: tidak ada kolom checkbox
14. Verifikasi Body: sedikitnya dua baris log User Action tampil
15. Verifikasi Body: Date terbaru di atas
16. Verifikasi Footer: pagination `Showing X–Y of Z entries`
17. Verifikasi Footer: Rows per page `10`
18. Verifikasi Footer: `[← Prev] [Page] [Next →]`

### TC-AC-ACAL-17: Tidak ada kontrol tulis apa pun di halaman, kedua tab

19. Klik tab "Session"
20. Verifikasi tab Session: baris data log tampil
21. Verifikasi tab Session: tidak ada tombol Create, Edit, Delete, checkbox, Bulk Action, atau row action pada toolbar, header, dan body tabel
22. Klik header kolom `⋯`
23. Verifikasi tab Session: isi Overlay Column Visibility tidak memuat tombol Create, Edit, Delete, checkbox, Bulk Action, atau row action
24. Tutup Overlay Column Visibility dengan `Esc`
25. Verifikasi tab Session: satu-satunya aksi adalah `Download`
26. Klik tab "User Action"
27. Verifikasi tab User Action: baris data log tampil
28. Verifikasi tab User Action: tidak ada tombol Create, Edit, Delete, checkbox, Bulk Action, atau row action pada toolbar, header, dan body tabel
29. Klik header kolom `⋯`
30. Verifikasi tab User Action: isi Overlay Column Visibility tidak memuat tombol Create, Edit, Delete, checkbox, Bulk Action, atau row action
31. Tutup Overlay Column Visibility dengan `Esc`
32. Verifikasi tab User Action: satu-satunya aksi adalah `Download`

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-02, 17). Tidak ada TC hanya-BE di spec ini.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 11, 24, dan 31 (tutup Overlay Column Visibility dengan `Esc`) serta langkah 19 dan 26 (klik tab "Session" dan tab "User Action" untuk mengulang pemeriksaan TC-17 pada tiap tab; TC-17 hanya menyebut "ulangi pada tab User Action").
- Langkah "Verifikasi ... sedikitnya dua baris ... tampil" (langkah 14) pada TC-02 dan "baris data log tampil" (langkah 20 dan 27) pada TC-17 adalah `Verifikasi` data pembanding (anchor) untuk asersi universal (Date terbaru di atas, tanpa kontrol tulis) pada surface yang sama; Expected TC tidak memuatnya.
- TC-17 Expected menyebut "kedua tab"; spec mengasersi tab Session (mulai dari langkah 19) lalu tab User Action.
- Temuan untuk QA:
  - Email akun Pre-setup memakai placeholder `{namaCompany}` (Pre-setup No 1) dan password memakai `AC_TC_PASSWORD` (akun `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`), terdaftar di `.env.example` dan `spectra.config.ts`.
  - Mekanisme seeding Data Log (Pre-setup No 9 dan No 10) tidak didefinisikan di TC, PRD, atau LLD yang dibaca; kemampuan seeding diminta dari tim FE/BE.
  - TC-02 menyebut header `⋯` pada kolom Actions; spec mengikuti TC.
