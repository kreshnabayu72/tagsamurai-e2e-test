---
id: TC-GS-DIV-E2E-056-changelog-filter-panel-screening-dan-opsi-dropdown
title: "Modal Changelog: Filter Panel Screening dan Sumber Opsi Dropdown"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-195
  - TC-GS-DIV-196
  - TC-GS-DIV-197
  - TC-GS-DIV-231
  - TC-GS-DIV-232
coverage:
  web: automated
---

# Modal Changelog: Filter Panel Screening dan Sumber Opsi Dropdown

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1). Login di hook `before` spec ini (kredensial `Spectra.env.GS_TC_PASSWORD`); akun ini adalah akun default suite, sehingga hook `after` tidak mengganti sesi. Halaman awal: Global Settings > User > Division.
- Akun aksi lewat API (tidak login UI): Create+Read, Rina Marlina (`Rina M`), `createOnly_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_CREATE_PASSWORD`; Update+Read, Agus Wijaya (`Agus W`), `updateOnly_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_UPDATE_PASSWORD`; Delete+Read, Dewi Lestari (`Dewi L`), `deleteOnly_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_DELETE_PASSWORD`. Rina Marlina dipakai juga sebagai "admin lain" di langkah 29 dan Dewi Lestari di langkah 42.
- Environment variable: `GS_TC_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Seeding minimal (S-11; lewat API di hook `before`, urutan sebagai berikut). Hanya data yang dipakai `Verifikasi` yang di-seed; tidak ada Population D-02:
  - Division `Log Mixed Div {runId}-056` dibuat oleh Rina Marlina (entri Create oleh `Rina M`), diubah oleh Agus Wijaya menjadi Name `Log Mixed Div Renamed {runId}-056` dan Code `LMD056` (entri Edit Field `Division Name` dan `Code` oleh `Agus W`), lalu dihapus oleh Dewi Lestari (entri Delete oleh `Dewi L`). Menyediakan nama yang di-rename dan dihapus tetapi masih punya entri (TC-GS-DIV-196 precondition d), kedua Field Edit, dan keempat user Modified By (bersama `Sari D` pada entri Create `Snapshot Unit`).
  - Division `Snapshot Unit {runId}-056` (Code `SNU`, D-21, setara dibuat lewat `[+ Division]`) dibuat oleh Sari Dewi. Sebelum dibuat, hook `before` menghapus sisa Division bernama `Snapshot Unit {runId lama}-056` yang masih ada dari run sebelumnya (berdasarkan nama bersuffix spec ini, bukan berdasarkan Code `SNU` saja, karena Code `SNU` juga dipakai spec lain), supaya Code `SNU` bebas. Code `SNU` literal (pengecualian S-12 untuk nama dan kode literal; seeding idempotent, suite serial).
- Aksi di tengah spec lewat API oleh akun lain (kemampuan "aksi Division lewat API oleh akun lain", bukan sesi browser kedua): langkah 29 Rina Marlina membuat `Legal Compliance {runId}-056` (D-14, Code auto-generate); langkah 42 Dewi Lestari menghapus `Snapshot Unit {runId}-056`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API `Legal Compliance {runId}-056`, `Snapshot Unit {runId}-056`, dan `Log Mixed Div Renamed {runId}-056` bila masih ada. Entri Changelog tidak bisa dihapus.
- Kapasitas: Master Data Count Limit environment automation cukup untuk Division Pre-setup (6) dan Division milik spec ini (disediakan tim FE).
- Kemampuan teknis: `Spectra.intercept()` untuk menahan respons pemuatan opsi filter Changelog selama 3 detik (langkah 33) dan melepasnya (langkah 38); endpoint tidak didefinisikan di TC/PRD sehingga disediakan tim FE (lihat Temuan untuk QA).
- State global yang disyaratkan: Division `Compliance` (Pre-setup) tidak memiliki entri Changelog (langkah 19); `Maya Putri` (Read Only, `readOnly_automated_qaTeam1@qwertysystem.net`) dan `Fajar Nugroho` (Tanpa Capability, `noCapability_automated_qaTeam1@qwertysystem.net`) tidak pernah memutasi Division Client A (langkah 24 dan 25; keduanya hanya dirujuk sebagai nama, tidak ada login). Nama singkat Modified By mengikuti aturan tampilan `[First Name] [Last Initial]` (prd-conventions.md §9.13): `Maya P` untuk Maya Putri dan `Fajar N` untuk Fajar Nugroho.
- Precondition TC-GS-DIV-195, 196, 197, 231, 232: login sebagai Total Control dan berada di Global Settings > User > Division; riwayat Changelog terisi (Modified By: `Sari D`, `Rina M`, `Agus W`, `Dewi L`).
- Suite serial (`parallel: false`) karena Code `SNU` literal dipakai bersama spec lain.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang dipulihkan: intercept dilepas di langkah 38 (cadangan di hook `after`).

## Test Steps

### TC-GS-DIV-195: Screening Filter Panel Modal Changelog

1. Klik icon Changelog di Table Tools
2. Klik icon Filter di modal
3. Verifikasi field `Date` berupa date range picker
4. Verifikasi field `Date` memiliki placeholder `Select date`
5. Verifikasi field `Action` berupa multi-select searchable
6. Verifikasi field `Action` memiliki placeholder `All actions`
7. Verifikasi field `Division Name` berupa multi-select searchable
8. Verifikasi field `Division Name` memiliki placeholder `All divisions`
9. Verifikasi field `Field` berupa multi-select searchable
10. Verifikasi field `Field` memiliki placeholder `All fields`
11. Verifikasi field `Modified By` berupa multi-select searchable
12. Verifikasi field `Modified By` memiliki placeholder `All users`
13. Verifikasi aksi `[Clear Field]` dan `[Apply]` tampil

### TC-GS-DIV-196: Opsi dropdown filter Changelog bersumber dari isi tabel Changelog

14. Buka dropdown Action
15. Verifikasi opsi Action hanya `Create`, `Edit`, `Delete`
16. Buka dropdown Division Name
17. Verifikasi opsi Division Name memuat `Log Mixed Div Renamed {runId}-056` (Division yang di-rename dan sudah dihapus tetapi punya entri)
18. Verifikasi opsi Division Name memuat `Log Mixed Div {runId}-056` (nama sebelum rename)
19. Verifikasi opsi Division Name tidak memuat `Compliance`
20. Buka dropdown Field
21. Verifikasi opsi Field `Division Name` dan `Code`
22. Buka dropdown Modified By
23. Verifikasi opsi Modified By memuat `Sari D`, `Rina M`, `Agus W`, dan `Dewi L`
24. Verifikasi opsi Modified By tidak memuat `Maya P` (Maya Putri)
25. Verifikasi opsi Modified By tidak memuat `Fajar N` (Fajar Nugroho)

### TC-GS-DIV-197: Opsi filter bertambah saat entri Changelog baru tercatat

26. Buka dropdown Division Name
27. Verifikasi opsi Division Name memuat `Log Mixed Div Renamed {runId}-056` (pembanding sebelum asersi ketiadaan)
28. Verifikasi opsi Division Name belum memuat `Legal Compliance {runId}-056`
29. Admin lain (Rina Marlina, lewat API) membuat Division `Legal Compliance {runId}-056`
30. Tutup lalu buka kembali dropdown Division Name
31. Verifikasi opsi `Legal Compliance {runId}-056` muncul pada dropdown Division Name tanpa reload halaman

### TC-GS-DIV-231: Dropdown filter Changelog menampilkan loading saat opsi masih diambil

32. Klik icon `[✕]` untuk menutup Modal Changelog, lalu klik icon Changelog di Table Tools
33. Tahan respons pemuatan opsi filter selama 3 detik
34. Klik icon Filter di modal
35. Buka dropdown Division Name
36. Verifikasi dropdown menampilkan skeleton atau spinner (bukan daftar kosong tanpa indikator)
37. Verifikasi opsi tampil setelah respons diterima
38. Lepas penahanan respons pemuatan opsi filter

### TC-GS-DIV-232: Filter Division Name tetap berlaku pada snapshot setelah Division dihapus pihak lain

39. Klik icon `[✕]` untuk menutup Modal Changelog, lalu klik icon Changelog di Table Tools
40. Klik icon Filter di modal
41. Pilih Division Name `Snapshot Unit {runId}-056`, klik `[Apply]`
42. Admin lain (Dewi Lestari, lewat API) menghapus Division `Snapshot Unit {runId}-056`
43. Klik icon `[✕]` untuk menutup Modal Changelog, lalu klik icon Changelog di Table Tools
44. Klik icon Filter di modal, lalu buka dropdown Division Name
45. Verifikasi opsi `Snapshot Unit {runId}-056` tetap ada pada dropdown Division Name
46. Pilih Division Name `Snapshot Unit {runId}-056`, klik `[Apply]`
47. Verifikasi entri Changelog `Snapshot Unit {runId}-056` tetap tampil

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-DIV-195, 196, 197, 231, 232. Alasan: screening (195) dan pembacaan opsi (196) lebih dulu; TC-GS-DIV-197 menambah opsi; TC-GS-DIV-231 memakai intercept; TC-GS-DIV-232 terakhir karena menghapus Division yang dipakai filter. Urutan sama dengan slice sumber.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 32 dan 39 (menutup lalu membuka kembali Modal Changelog agar pemuatan opsi atau pemilihan filter dimulai dari modal baru, S-09) dan langkah 38 (melepas penahanan respons). Pilihan filter dan Apply di TC-GS-DIV-232 sudah sesuai langkah TC.
- Langkah 27 (anchor positif: opsi `Log Mixed Div Renamed {runId}-056` tampil, S-03, bagian 8b butir 2) dan langkah 28 (baseline: opsi `Legal Compliance {runId}-056` belum ada sebelum aksi admin lain) menambahkan `Verifikasi` di luar Expected TC-GS-DIV-197, supaya perubahan sungguh berasal dari aksi pada langkah 29 dan state sementara diasersi sebelum langkah yang mengubahnya (S-12, bagian 8b butir 5).
- "Admin lain" pada TC-GS-DIV-197 dan 232 dijalankan lewat API oleh akun Pre-setup lain (Rina Marlina, Dewi Lestari) sebagai pelaku kedua yang hanya memicu perubahan state (P-2), bukan objek asersi; tidak ada sesi browser kedua.
- Spec melewati sekitar 35 langkah (47 langkah) karena lima TC memakai Filter Panel Modal Changelog yang sama dan tiap klausa Expected menjadi satu `Verifikasi` (S-01); semua blok satu kelas harness (Filter Panel Changelog), satu akun aktor, dan satu dataset. Blok 195, 196, dan 197 memakai Modal Changelog yang dibuka di langkah 1; blok 231 dan 232 membuka modal sendiri.
- Temuan untuk QA:
  - TC-GS-DIV-196 Expected d "hanya user yang tercatat di riwayat" tidak stabil di environment bersama karena aktor lain dapat memutasi Division Client A; spec mengasersi keempat nama ada dan `Maya P` serta `Fajar N` tidak ada, syaratnya ada di Prerequisites.
  - TC-GS-DIV-197 dan 232 menyebut "Admin lain" tanpa menyebut akun dan mekanismenya; spec memakai aksi API oleh Rina Marlina dan Dewi Lestari (Tabel Data Uji Pre-setup).
  - TC-GS-DIV-231 tidak menyebut endpoint opsi filter yang ditahan ("Tahan (delay) respons opsi filter"); disediakan tim FE tanpa mengarang endpoint.
  - TC-GS-DIV-232 menyebut Division dibuat lewat `[+ Division]`; spec men-seed lewat API di `before` (entri Create setara).
  - Placeholder Date `Select date` mengikuti NC-11 (Dikonfirmasi).
  - TC-GS-DIV-232 Post Condition (Division terhapus; entri Create dan Delete tetap di Changelog) tidak punya langkah observasi atau Expected padanan di TC, sehingga tidak diasersi.
