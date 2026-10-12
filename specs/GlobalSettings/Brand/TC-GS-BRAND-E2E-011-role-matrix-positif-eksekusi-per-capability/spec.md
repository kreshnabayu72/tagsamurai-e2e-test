---
id: TC-GS-BRAND-E2E-011-role-matrix-positif-eksekusi-per-capability
title: "Role Matrix Positif: Eksekusi Create, Update, Delete, dan Bulk Delete per Capability"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-36
  - TC-GS-BRAND-37
  - TC-GS-BRAND-38
  - TC-GS-BRAND-39
coverage:
  web: automated
---

# Role Matrix Positif: Eksekusi Create, Update, Delete, dan Bulk Delete per Capability

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji (tiap role memakai akunnya sendiri; langkah ganti akun ditulis eksplisit di Test Steps):

| Role | Akun (Client A) | Environment variable password | Aksi yang dieksekusi |
|---|---|---|---|
| System Role: Create dan Read | `createOnly_automated_qaTeam1@qwertysystem.net` (Rina Marlina) | `GS_CREATE_PASSWORD` | Create |
| System Role: Update dan Read | `updateOnly_automated_qaTeam1@qwertysystem.net` (Agus Wijaya) | `GS_UPDATE_PASSWORD` | Update |
| System Role: Delete dan Read | `deleteOnly_automated_qaTeam1@qwertysystem.net` (Dewi Lestari) | `GS_DELETE_PASSWORD` | Delete dan Bulk Delete |

- Akun aktor Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi, `Spectra.env.GS_TC_PASSWORD`) dipakai hanya di hook `before` dan `after` untuk seeding dan cleanup lewat API.
- Environment variable: `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data dinamis (suffix per run, ditambah nomor spec karena nama dipakai lebih dari satu spec):
  - `Mosaic Brands {runId}-011` dibuat lewat UI di TC-GS-BRAND-36, diubah menjadi `Mosaic Group {runId}-011` di TC-GS-BRAND-37, dihapus di TC-GS-BRAND-38 (rantai TC dalam spec yang sama; tidak menumpang spec lain).
  - `Pine Co {runId}-011` dan `Quartz Co {runId}-011`: brand bebas relasi, di-seed lewat API di hook `before` oleh Total Control (TC-GS-BRAND-39).
- Cleanup (hook `after`, tidak berasumsi seeding atau langkah UI berhasil penuh): hapus lewat API brand `Mosaic Brands {runId}-011`, `Mosaic Group {runId}-011`, `Pine Co {runId}-011`, `Quartz Co {runId}-011` bila masih ada, lalu pulihkan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`) karena spec berakhir pada akun Delete dan Read.
- Kemampuan teknis: logout dan login ulang dengan akun berbeda dalam satu spec; hook seeding dan cleanup memanggil API Brand sebagai Total Control.
- State global: tidak ada yang diubah.

## Test Steps

### TC-GS-BRAND-36: Aktor Create dan Read berhasil membuat Brand

1. Login sebagai System Role: Create dan Read (`createOnly_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_CREATE_PASSWORD`)
2. Buka Global Settings > Master Reference > Brand
3. Klik [+ Brand]
4. Isi Brand Name `Mosaic Brands {runId}-011`
5. Klik [Submit]
6. Verifikasi toast sukses: "Success, brand has been created."
7. Isi Search dengan `{runId}-011`
8. Verifikasi `Mosaic Brands {runId}-011` muncul di tabel

### TC-GS-BRAND-37: Aktor Update dan Read berhasil mengubah Brand

9. Logout, lalu login sebagai System Role: Update dan Read (`updateOnly_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_UPDATE_PASSWORD`)
10. Buka Global Settings > Master Reference > Brand
11. Isi Search dengan `{runId}-011`
12. Klik `⋯` baris `Mosaic Brands {runId}-011` > Edit
13. Ubah Brand Name menjadi `Mosaic Group {runId}-011`
14. Klik [Save]
15. Verifikasi toast sukses: "Success, brand has been updated."
16. Verifikasi baris berubah menjadi `Mosaic Group {runId}-011`

### TC-GS-BRAND-38: Aktor Delete dan Read berhasil menghapus Brand bebas relasi

17. Logout, lalu login sebagai System Role: Delete dan Read (`deleteOnly_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_DELETE_PASSWORD`)
18. Buka Global Settings > Master Reference > Brand
19. Isi Search dengan `{runId}-011`
20. Klik `⋯` baris `Mosaic Group {runId}-011` > Delete
21. Verifikasi dialog `Delete Brand` tampil
22. Klik [Delete] pada dialog
23. Verifikasi toast sukses: "Success, brand has been deleted."
24. Verifikasi `Mosaic Group {runId}-011` hilang dari tabel

### TC-GS-BRAND-39: Aktor Delete dan Read berhasil menjalankan Bulk Delete

25. Isi Search dengan `{runId}-011` agar `Pine Co {runId}-011` dan `Quartz Co {runId}-011` tampil di halaman aktif (akun Delete dan Read masih login)
26. Centang `Pine Co {runId}-011` dan `Quartz Co {runId}-011`
27. Klik `Bulk Action` > `Delete`
28. Verifikasi dialog `Delete Brands` tampil dengan 2 bullet: `Pine Co {runId}-011` dan `Quartz Co {runId}-011`
29. Klik [Delete] pada dialog
30. Verifikasi toast sukses: "Success, brand has been deleted."
31. Verifikasi `Pine Co {runId}-011` dan `Quartz Co {runId}-011` tidak lagi tampil di tabel

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber dipertahankan karena TC-GS-BRAND-37 dan TC-GS-BRAND-38 bergantung pada hasil TC sebelumnya (kolom Dependensi) dan aksi Delete memang paling akhir; rantai ini ada di dalam satu spec, jadi spec tetap bisa jalan sendiri.
- Search `{runId}-011` (langkah 7, 11, 19, 25) dipakai di setiap TC agar brand milik spec ini tampil di halaman aktif sebelum diverifikasi atau dipilih; ini hanya cara menemukan baris di tabel 10 per halaman, bukan bagian dari asersi TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 9 dan 17 (ganti akun) serta langkah 7, 11, 19, 25 (Search `{runId}-011`).
- Langkah 31 (kedua brand hilang) berasal dari Post Condition TC-GS-BRAND-39.
- Brand Name memakai suffix `{runId}-011` karena nama Mosaic dan Pine/Quartz juga dipakai spec lain.
