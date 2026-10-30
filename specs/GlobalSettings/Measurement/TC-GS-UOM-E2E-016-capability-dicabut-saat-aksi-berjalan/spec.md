---
id: TC-GS-UOM-E2E-016-capability-dicabut-saat-aksi-berjalan
title: "Capability Dicabut Saat Form atau Dialog Terbuka: Create, Edit, Delete Ditolak"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-UOM-397
  - TC-GS-UOM-92
  - TC-GS-UOM-260
coverage:
  web: automated
---

# Capability Dicabut Saat Form atau Dialog Terbuka: Create, Edit, Delete Ditolak

## Prerequisites

- Mode: FE+BE (backend nyata). Pencabutan capability dilakukan lewat API oleh admin, bukan lewat UI aktor.
- Hook suite (login akun default, `beforeEach` membuka Measurement, flag Guided Tooltip `guided_tooltip_seen_gs-measurement`): lihat `suite.md`; flag disetel true untuk ketiga akun di bawah oleh hook suite.
- Role yang diuji (tiap TC memakai role aktor sendiri; langkah ganti akun ditulis eksplisit):

| TC | Role aktor | Akun (Client A) | Env var password | Capability yang dicabut |
|---|---|---|---|---|
| TC-GS-UOM-397 | System Role: Create dan Read | `createOnly_automated_qaTeam1@qwertysystem.net` (Rina Marlina) | `Spectra.env.GS_CREATE_PASSWORD` | Create |
| TC-GS-UOM-92 | System Role: Update dan Read | `updateOnly_automated_qaTeam1@qwertysystem.net` (Agus Wijaya) | `Spectra.env.GS_UPDATE_PASSWORD` | Update |
| TC-GS-UOM-260 | System Role: Delete dan Read | `deleteOnly_automated_qaTeam1@qwertysystem.net` (Dewi Lestari) | `Spectra.env.GS_DELETE_PASSWORD` | Delete |

- Aktor admin (pencabut dan pemulih capability): Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi, `Spectra.env.GS_TC_PASSWORD`), lewat API admin untuk mengubah capability role (kemampuan disediakan tim FE, tanpa endpoint karangan), dipanggil di langkah spec dan di hook `after`.
- Environment variable: `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables`.
- Hook `before`: Total Control men-seed lewat API dua unit bebas relasi milik spec: `Cap Edit Unit {runId}-016` (Symbol `ce`, target Edit TC-GS-UOM-92) dan `Cap Delete Unit {runId}-016` (Symbol `cd`, target Delete TC-GS-UOM-260); lalu login sebagai System Role: Create dan Read (aktor pertama spec).
- Nilai yang hanya diketik dan seharusnya tidak pernah tersimpan: `Revoked Unit {runId}-016` / `rv` (TC-GS-UOM-397) dan Symbol `lt` (TC-GS-UOM-92).
- Cleanup (hook `after`, tidak berasumsi seeding atau langkah UI berhasil penuh): hapus lewat API kedua unit seeding berdasarkan id hasil seeding (apa pun namanya saat itu) dan `Revoked Unit {runId}-016` bila ternyata tercipta; pulihkan capability Create, Update, dan Delete ketiga role ke kondisi awal; pulihkan sesi ke akun default suite.
- State global yang diubah dan dipulihkan: capability role aktor (Manage master reference: Create, Update, Delete). Setiap TC memulihkan capability yang dicabutnya lewat API segera setelah asersi (langkah eksplisit 12, 27, dan 42). Suite berjalan serial (`parallel: false`).
- Kemampuan teknis: API admin untuk mencabut dan memulihkan capability role; API Measurement untuk seeding dan penghapusan sebagai Total Control; ganti akun dalam satu spec.

## Test Steps

### TC-GS-UOM-397: Capability Create dicabut saat form Create terbuka ditolak saat Submit

1. Klik [+ Unit]
2. Isi Unit Name `Revoked Unit {runId}-016`, Symbol `rv`
3. Admin (Total Control) mencabut capability Create dari role aktor lewat API
4. Klik [Submit]
5. Verifikasi toast error: "You don't have permission to do this."
6. Verifikasi modal tertutup otomatis
7. Verifikasi UI me-refresh
8. Verifikasi tombol [+ Unit] tidak tampil lagi
9. Ketik Search `Revoked Unit {runId}-016`, tekan Enter
10. Verifikasi empty state `No results found` (Title) untuk Search `Revoked Unit {runId}-016`, sehingga `Revoked Unit {runId}-016` tidak ada di tabel
11. Klik `(←)` pada kotak Search
12. Admin memulihkan capability Create role System Role: Create dan Read lewat API

### TC-GS-UOM-92: Capability Update dicabut saat form Edit terbuka ditolak saat Save

13. Logout, lalu login sebagai System Role: Update dan Read
14. Buka Tab Measurement (Global Settings > Master Reference > Measurement)
15. Ketik Search `Cap Edit Unit {runId}-016`, tekan Enter
16. Klik `⋯` baris `Cap Edit Unit {runId}-016` > Edit
17. Ubah Symbol menjadi `lt`
18. Admin (Total Control) mencabut capability Update dari role aktor lewat API
19. Klik [Save]
20. Verifikasi toast error: "You don't have permission to do this."
21. Verifikasi modal tertutup otomatis
22. Verifikasi UI me-refresh
23. Klik `⋯` baris `Cap Edit Unit {runId}-016`
24. Verifikasi row action `Edit` tidak tampil lagi
25. Tutup row action menu dengan Esc
26. Verifikasi Symbol baris `Cap Edit Unit {runId}-016` tetap `ce` (tidak berubah)
27. Admin memulihkan capability Update role System Role: Update dan Read lewat API

### TC-GS-UOM-260: Capability Delete dicabut saat dialog Delete terbuka ditolak saat konfirmasi

28. Logout, lalu login sebagai System Role: Delete dan Read
29. Buka Tab Measurement (Global Settings > Master Reference > Measurement)
30. Ketik Search `Cap Delete Unit {runId}-016`, tekan Enter
31. Klik `⋯` baris `Cap Delete Unit {runId}-016` > Delete (dialog `Delete Unit` tampil)
32. Admin (Total Control) mencabut capability Delete dari role aktor lewat API
33. Klik [Delete] pada dialog
34. Verifikasi toast error: "You don't have permission to do this."
35. Verifikasi dialog tertutup otomatis
36. Verifikasi UI me-refresh
37. Klik `⋯` baris `Cap Delete Unit {runId}-016`
38. Verifikasi row action `Delete` tidak tampil lagi
39. Tutup row action menu dengan Esc
40. Verifikasi checkbox baris tidak tampil lagi
41. Verifikasi `Cap Delete Unit {runId}-016` tidak terhapus (masih ada di tabel)
42. Admin memulihkan capability Delete role System Role: Delete dan Read lewat API

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Seluruh TC berkelas "perubahan izin di tengah aksi" (bagian 2 poin 3 konvensi) dan satu-satunya yang mengubah capability role selain TC-GS-UOM-31 (spec `TC-GS-UOM-E2E-014-role-matrix-negatif-tanpa-capability`); penolakan terjadi di server. Spec memakai tiga akun dengan langkah ganti akun eksplisit (langkah 13 dan 28); tiap blok memakai unit sendiri, sehingga kegagalan satu blok tidak menghilangkan makna blok lain.
- Target Edit dan Delete memakai unit milik spec (`Cap Edit Unit {runId}-016`, `Cap Delete Unit {runId}-016`) menggantikan Liter (TC-GS-UOM-92) dan Meter (TC-GS-UOM-260) di TC sumber, supaya baris Pre-setup bersama tidak berubah atau terhapus bila penolakan server gagal (S-06). Semua asersi "tidak berubah" dan "tidak terhapus" berlaku untuk unit milik spec itu.
- `Revoked Unit {runId}-016` memakai suffix per run dan nomor spec (S-12).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 9 dan 11 (Search agar `Revoked Unit` diperiksa di tabel 10 per halaman, lalu menutupnya), langkah 12, 27, dan 42 (pemulihan capability), langkah 13 dan 28 (ganti akun) disertai 14 dan 29 (membuka Tab Measurement), langkah 15 dan 30 (Search agar baris target tampil), serta langkah 25 dan 39 (menutup row action menu dengan Esc). Langkah 23 sampai 25 dan 37 sampai 39 membuka row action menu untuk memeriksa Edit dan Delete Hidden (Expected Result b TC-GS-UOM-92 dan 260); ketiadaan Edit dan Delete memakai `Detail` pada menu yang sama sebagai anchor.
- Verifikasi tambahan di luar Expected TC: langkah 10 memakai empty state `No results found` hasil Search sebagai anchor positif bagi asersi absence (bagian 8b butir 2).
- Langkah 41 berasal dari Expected Result c TC-GS-UOM-260; langkah 26 dari Expected Result c TC-GS-UOM-92.
- Spec ini di atas batas 35 langkah (42): seluruhnya satu kelas harness (fungsional, capability dicabut lewat API saat form atau dialog terbuka); tiap TC memakai unit dan sesi sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA:
  - Expected Result TC-GS-UOM-260 b menyebut "Dialog dan modal tertutup otomatis"; hanya dialog Delete yang terbuka pada TC itu, sehingga spec mengasersi dialog tertutup (langkah 35).
  - TC-GS-UOM-397, 92, dan 260 tidak menyebut akun admin pencabut capability; spec memakai Total Control Client A lewat API (kemampuan disediakan tim FE).
