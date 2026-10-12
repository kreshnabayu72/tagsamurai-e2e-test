---
id: TC-GS-BRAND-E2E-012-capability-dicabut-saat-aksi-berjalan
title: "Capability Dicabut Saat Aksi Sedang Berjalan"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-BRAND-35
  - TC-GS-BRAND-68
  - TC-GS-BRAND-91
  - TC-GS-BRAND-107
  - TC-GS-BRAND-129
coverage:
  web: automated
---

# Capability Dicabut Saat Aksi Sedang Berjalan

## Prerequisites

- Mode: FE+BE (backend nyata). Pencabutan capability dilakukan lewat API oleh admin, bukan lewat UI aktor.
- Role yang diuji (setiap TC memakai role aktor sendiri; langkah ganti akun ditulis eksplisit):

| TC | Role aktor | Akun (Client A) | Environment variable password | Capability yang dicabut |
|---|---|---|---|---|
| TC-GS-BRAND-35 | System Role: Read saja | `readCapability_automated_qaTeam1@qwertysystem.net` (Tono Hartono) | `GS_READ_PASSWORD` | Manage master reference (Read) |
| TC-GS-BRAND-68 | System Role: Create dan Read | `createOnly_automated_qaTeam1@qwertysystem.net` (Rina Marlina) | `GS_CREATE_PASSWORD` | Create |
| TC-GS-BRAND-91 | System Role: Update dan Read | `updateOnly_automated_qaTeam1@qwertysystem.net` (Agus Wijaya) | `GS_UPDATE_PASSWORD` | Update |
| TC-GS-BRAND-107, TC-GS-BRAND-129 | System Role: Delete dan Read | `deleteOnly_automated_qaTeam1@qwertysystem.net` (Dewi Lestari) | `GS_DELETE_PASSWORD` | Delete |

- Aktor admin (pencabut dan pemulih capability) adalah Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi, `Spectra.env.GS_TC_PASSWORD`), dipanggil lewat API di langkah spec dan di hook `after`.
- Environment variable: `GS_READ_PASSWORD`, `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data dinamis milik spec ini (suffix per run dan nomor spec, di-seed lewat API oleh Total Control di hook `before`; tidak memakai brand Pre-setup bersama):
  - `Cap Edit Co {runId}-012` (D-44, bebas relasi): target Edit TC-GS-BRAND-91.
  - `Cap Delete Co {runId}-012` (D-45, bebas relasi): target Delete TC-GS-BRAND-107.
  - `Cap Bulk A {runId}-012` dan `Cap Bulk B {runId}-012` (D-46, bebas relasi): target Bulk Delete TC-GS-BRAND-129.
  - Nilai yang hanya diketik dan seharusnya tidak pernah tersimpan: `Zephyr Co {runId}-012` (TC-GS-BRAND-68) dan `Cap Edit Z` (TC-GS-BRAND-91).
- Cleanup (hook `after`, tidak berasumsi seeding atau langkah UI berhasil penuh): hapus lewat API keempat brand seeding berdasarkan id hasil seeding (apa pun namanya saat itu) dan brand `Zephyr Co {runId}-012` bila ternyata tercipta, lalu pulihkan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`).
- State global yang diubah dan dipulihkan: capability role aktor (Manage master reference: Read, Create, Update, Delete). Setiap TC memulihkan capability yang dicabutnya lewat API segera setelah asersi (langkah eksplisit), dan hook `after` memulihkan seluruh capability keempat role ke kondisi awal walau spec gagal di tengah.
- Kemampuan teknis: API admin untuk mencabut dan memulihkan capability role; API Brand untuk seeding dan penghapusan sebagai Total Control; ganti akun dalam satu spec; muat ulang halaman.

## Test Steps

### TC-GS-BRAND-35: Satu capability Manage master reference men-gate Brand dan Measurement sekaligus

1. Login sebagai System Role: Read saja (`readCapability_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_READ_PASSWORD`)
2. Buka Global Settings > Master Reference
3. Periksa Tab Brand dan Tab Measurement
4. Verifikasi sebelum capability dicabut, Tab Brand dan Tab Measurement tampil
5. Admin (Total Control) mencabut capability Manage master reference dari role aktor lewat API
6. Muat ulang halaman
7. Verifikasi setelah capability dicabut, Tab Brand dan Tab Measurement keduanya Hidden
8. Admin memulihkan capability Manage master reference role System Role: Read saja lewat API

### TC-GS-BRAND-68: Create saat capability dicabut ketika form terbuka

9. Logout, lalu login sebagai System Role: Create dan Read (`createOnly_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_CREATE_PASSWORD`)
10. Buka Global Settings > Master Reference > Brand
11. Klik [+ Brand]
12. Isi Brand Name `Zephyr Co {runId}-012`
13. Admin (Total Control) mencabut capability Create dari role aktor lewat API
14. Klik [Submit]
15. Verifikasi toast error: "You don't have permission to do this."
16. Verifikasi modal tertutup
17. Verifikasi list di-refresh
18. Verifikasi `[+ Brand]` Hidden
19. Isi Search dengan `Zephyr Co {runId}-012`
20. Verifikasi `Zephyr Co {runId}-012` tidak dibuat (tidak ada di tabel)
21. Kosongkan Search
22. Admin memulihkan capability Create role System Role: Create dan Read lewat API

### TC-GS-BRAND-91: Edit saat capability Update dicabut ketika form terbuka

23. Logout, lalu login sebagai System Role: Update dan Read (`updateOnly_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_UPDATE_PASSWORD`)
24. Buka Global Settings > Master Reference > Brand
25. Isi Search dengan `Cap Edit Co {runId}-012`
26. Klik `⋯` baris `Cap Edit Co {runId}-012` > Edit
27. Ubah Brand Name menjadi `Cap Edit Z`
28. Admin (Total Control) mencabut capability Update dari role aktor lewat API
29. Klik [Save]
30. Verifikasi toast error: "You don't have permission to do this."
31. Verifikasi modal tertutup
32. Verifikasi list di-refresh
33. Verifikasi row action Edit Hidden
34. Admin memulihkan capability Update role System Role: Update dan Read lewat API

### TC-GS-BRAND-107: Delete saat capability Delete dicabut ketika dialog terbuka

35. Logout, lalu login sebagai System Role: Delete dan Read (`deleteOnly_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_DELETE_PASSWORD`)
36. Buka Global Settings > Master Reference > Brand
37. Isi Search dengan `Cap Delete Co {runId}-012`
38. Klik `⋯` baris `Cap Delete Co {runId}-012` > Delete
39. Admin (Total Control) mencabut capability Delete dari role aktor lewat API
40. Klik [Delete] pada dialog
41. Verifikasi toast error: "You don't have permission to do this."
42. Verifikasi dialog tertutup
43. Verifikasi list di-refresh
44. Verifikasi `Cap Delete Co {runId}-012` tetap ada di tabel
45. Admin memulihkan capability Delete role System Role: Delete dan Read lewat API
46. Muat ulang halaman agar akun Delete dan Read memuat capability yang sudah dipulihkan

### TC-GS-BRAND-129: Bulk Delete saat capability Delete dicabut

47. Isi Search dengan `Cap Bulk`
48. Centang `Cap Bulk A {runId}-012` dan `Cap Bulk B {runId}-012` (akun Delete dan Read masih login)
49. Klik `Bulk Action` > `Delete`
50. Admin (Total Control) mencabut capability Delete dari role aktor lewat API
51. Klik [Delete] pada dialog
52. Verifikasi toast error: "You don't have permission to do this."
53. Verifikasi dialog tertutup
54. Verifikasi list di-refresh
55. Verifikasi checkbox baris Hidden
56. Verifikasi `Cap Bulk A {runId}-012` dan `Cap Bulk B {runId}-012` tetap ada di tabel
57. Admin memulihkan capability Delete role System Role: Delete dan Read lewat API

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Seluruh TC di spec ini berkelas "perubahan izin di tengah aksi" (bagian 2 poin 3 konvensi) dan satu-satunya yang mengubah capability role, sehingga dikumpulkan di satu spec; semua penolakan terjadi di server dan target aksi adalah brand milik spec ini, jadi bila penolakan gagal tidak ada Pre-setup bersama yang rusak.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 19 dan 21 (Search lalu kosongkan, untuk memeriksa Zephyr Co tidak dibuat di tabel 10 per halaman), langkah 25, 37, dan 47 (Search agar baris target tampil di halaman aktif), langkah 8, 22, 34, 45, dan 57 (pemulihan capability), serta langkah 46 (muat ulang) agar TC berikutnya yang memakai role sama (TC-GS-BRAND-107 lalu TC-GS-BRAND-129) mulai dari kondisi capability penuh.
- TC-GS-BRAND-35 dijalankan paling awal karena hanya baca; urutan 68, 91, 107, 129 mengikuti urutan TC sumber (tidak ada aksi yang menghapus data).
- Langkah 20 berasal dari ER c TC-GS-BRAND-68; langkah 44 dan 56 dari ER c TC-GS-BRAND-107 dan TC-GS-BRAND-129.
- Kebutuhan seeding brand dinamis dan pemulihan capability sudah dicatat di Prerequisites.
