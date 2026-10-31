---
id: TC-GS-UOM-E2E-015-role-matrix-positif-eksekusi-per-capability
title: "Role Matrix Positif: Eksekusi Create, Update, Delete, dan Bulk Delete per Capability"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-32
  - TC-GS-UOM-33
  - TC-GS-UOM-34
  - TC-GS-UOM-35
coverage:
  web: automated
---

# Role Matrix Positif: Eksekusi Create, Update, Delete, dan Bulk Delete per Capability

## Prerequisites

- Mode: FE+BE (backend nyata).
- Hook suite (login akun default, `beforeEach` membuka Measurement, flag Guided Tooltip `guided_tooltip_seen_gs-measurement`): lihat `suite.md`; flag disetel true untuk ketiga akun di bawah oleh hook suite.
- Role yang diuji (tiap role memakai akunnya sendiri; langkah ganti akun ditulis eksplisit):

| TC | Role | Akun (Client A) | Env var password | Aksi yang dieksekusi |
|---|---|---|---|---|
| TC-GS-UOM-32 | System Role: Create dan Read | `createOnly_automated_qaTeam1@qwertysystem.net` (Rina Marlina) | `Spectra.env.GS_CREATE_PASSWORD` | Create |
| TC-GS-UOM-33 | System Role: Update dan Read | `updateOnly_automated_qaTeam1@qwertysystem.net` (Agus Wijaya) | `Spectra.env.GS_UPDATE_PASSWORD` | Update |
| TC-GS-UOM-34, TC-GS-UOM-35 | System Role: Delete dan Read | `deleteOnly_automated_qaTeam1@qwertysystem.net` (Dewi Lestari) | `Spectra.env.GS_DELETE_PASSWORD` | Delete dan Bulk Delete |

- Hook `before`: Total Control Client A (`totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`) men-seed lewat API dua unit bebas relasi `Furlong {runId}-015` (Symbol `fur`) dan `Fathom {runId}-015` (Symbol `ftm`) untuk TC-GS-UOM-35 (Data Dinamis D-10, nama bersuffix), lalu login sebagai System Role: Create dan Read (aktor pertama spec). Hook `after` mengembalikan sesi ke akun default suite.
- Environment variable: `GS_CREATE_PASSWORD`, `GS_UPDATE_PASSWORD`, `GS_DELETE_PASSWORD`, `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture; nama env didaftarkan di `executionConfig.environmentVariables`.
- Data dinamis (suffix per run dan nomor spec): `Kilometer {runId}-015` (Symbol `km`) dibuat lewat UI di TC-GS-UOM-32, diubah Symbol-nya di TC-GS-UOM-33, dihapus di TC-GS-UOM-34 (rantai dalam spec yang sama; tidak menumpang spec lain). Unit Pre-setup tidak dipakai sebagai target tulis.
- Cleanup (hook `after`, tidak berasumsi seeding atau langkah UI berhasil penuh): hapus lewat API `Kilometer {runId}-015`, `Furlong {runId}-015`, dan `Fathom {runId}-015` bila masih ada.
- Kemampuan teknis: logout dan login ulang dengan akun berbeda dalam satu spec; Total Control memanggil API Measurement untuk seeding dan cleanup.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-UOM-32: Aktor Create dan Read berhasil membuat Measurement

1. Klik [+ Unit]
2. Isi Unit Name `Kilometer {runId}-015`, Symbol `km`
3. Klik [Submit]
4. Verifikasi toast sukses: "Success, unit has been created."
5. Ketik Search `{runId}-015`, tekan Enter
6. Verifikasi `Kilometer {runId}-015` muncul di tabel

### TC-GS-UOM-33: Aktor Update dan Read berhasil mengubah Symbol Measurement

7. Logout, lalu login sebagai System Role: Update dan Read
8. Buka Tab Measurement (Global Settings > Master Reference > Measurement)
9. Ketik Search `Kilometer {runId}-015`, tekan Enter
10. Klik `⋯` baris `Kilometer {runId}-015` > Edit
11. Ubah Symbol menjadi `KM`
12. Ubah Symbol menjadi `kms`
13. Klik [Save]
14. Verifikasi toast sukses: "Success, unit has been updated."
15. Verifikasi Symbol baris `Kilometer {runId}-015` menjadi `kms`

### TC-GS-UOM-34: Aktor Delete dan Read berhasil menghapus Measurement bebas relasi

16. Logout, lalu login sebagai System Role: Delete dan Read
17. Buka Tab Measurement (Global Settings > Master Reference > Measurement)
18. Ketik Search `Kilometer {runId}-015`, tekan Enter
19. Klik `⋯` baris `Kilometer {runId}-015` > Delete
20. Verifikasi dialog `Delete Unit` tampil
21. Klik [Delete] pada dialog
22. Verifikasi toast sukses: "Success, unit has been deleted."
23. Verifikasi `Kilometer {runId}-015` hilang dari tabel

### TC-GS-UOM-35: Aktor Delete dan Read berhasil menjalankan Bulk Delete

24. Ganti isi kotak search dengan `{runId}-015`, tekan Enter
25. Centang `Furlong {runId}-015` dan `Fathom {runId}-015`
26. Buka `Bulk Action` pada Bulk Action Bar, pilih `Delete`
27. Verifikasi dialog `Delete Units` tampil
28. Klik [Delete] pada dialog
29. Verifikasi toast sukses: "Success, unit has been deleted."

## Notes

- Mode: FE+BE. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC sumber (32, 33, 34, 35) dipertahankan: TC-GS-UOM-33 dan 34 bergantung pada hasil TC sebelumnya (kolom Dependensi) dan aksi Delete memang paling akhir; rantai ada di dalam satu spec sehingga spec tetap bisa jalan sendiri. TC-GS-UOM-35 tidak punya dependensi dan memakai akun yang sama dengan TC-GS-UOM-34.
- Nama TC sumber diganti nama bersuffix milik spec (Kilometer menjadi `Kilometer {runId}-015`; Furlong dan Fathom menjadi `Furlong {runId}-015` dan `Fathom {runId}-015`) sesuai S-12; Symbol tetap nilai TC.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 7 dan 16 (ganti akun), 8 dan 17 (membuka Tab Measurement sesudah ganti akun), serta langkah 5, 9, 18, dan 24 (Search agar baris milik spec tampil di halaman aktif pada tabel 10 per halaman; bukan bagian asersi TC).
- Temuan untuk QA:
  - TC-GS-UOM-33 menulis "Ubah Symbol menjadi `KM`, lalu `kms`" tanpa menyebut maksud nilai antara `KM`. Spec mengetik `KM` lalu menggantinya `kms` sebelum [Save] (langkah 11 dan 12) dan hanya mengasersi hasil akhir `kms` sesuai Expected Result.
  - Post Condition TC-GS-UOM-35 ("Furlong dan Fathom terhapus") tidak punya Expected Result padanan atau langkah observasi di TC, sehingga tidak diasersi di spec; hasil Bulk Delete hanya diasersi lewat toast (Expected Result b).
  - Expected Result TC-GS-UOM-32 sampai 35 tidak menyebut keadaan Table Tools setelah aksi; tidak ditambahkan.
