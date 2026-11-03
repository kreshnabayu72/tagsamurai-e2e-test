---
id: TC-AC-SU-E2E-033-selection-limit-lifecycle-settings
title: "Selection Limit: Live-block Checkbox ke-(Limit+1) dan Select All yang Melebihi Limit di-cap Otomatis"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SU-115
  - TC-AC-SU-116
coverage:
  web: automated
---

# Selection Limit: Live-block Checkbox ke-(Limit+1) dan Select All yang Melebihi Limit di-cap Otomatis

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- State global yang diubah: Selection Limit di Admin Console > Plans & Licensing > Lifecycle Settings > System Limits diturunkan ke 3 lewat Fixture BE (disediakan tim FE/BE; ambang 3 di bawah 100 baris sehingga bukan kelas e) dan dikembalikan ke nilai awal di hook `after` dan langkah akhir spec. Suite berjalan serial (`parallel: false`).
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-115, 116 | (user generik, TC tidak menyebut nama) | `User Seleksi 1 {runId}-033` sampai `User Seleksi 5 {runId}-033` | `userseleksiN+{runId}-033@qwertysystem.net` | 5 user Activated, Active (eligible) |

- N total dari seeding: Search atas suffix spec menampilkan 5 baris (N = 5; Default User dan aktor tidak ikut).
- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).

## Test Steps

### TC-AC-SU-115: Selection Limit, live-block checkbox ke-(limit+1)

1. Turunkan Selection Limit ke 3 lewat Fixture BE
2. Muat ulang halaman dengan F5
3. Ketik Search `{runId}-033`, tekan Enter
4. Centang baris 1, baris 2, dan baris 3 satu per satu
5. Verifikasi baris 1 sampai 3 tetap tercentang
6. Verifikasi Bulk Action Bar aktif
7. Hover checkbox baris ke-4
8. Verifikasi checkbox baris ke-4 tampil namun disabled dengan tooltip `You've reached the maximum selection of 3 rows.`
9. Klik checkbox baris ke-4
10. Verifikasi checkbox baris ke-5 disabled
11. Klik icon `×` pada Bulk Action Bar untuk membatalkan seleksi

### TC-AC-SU-116: Selection Limit, Select All melebihi limit di-cap otomatis

12. Centang 1 baris
13. Klik `[Select All (5 records)]`
14. Verifikasi hanya 3 baris pertama terseleksi
15. Verifikasi toast error: "Error, only the first 3 of 5 rows were selected. Narrow your filter to include the rest."
16. Verifikasi toast error tetap tampil sampai di-dismiss
17. Verifikasi Bulk Action Bar tetap bisa dipakai
18. Dismiss toast error, lalu klik icon `×` pada Bulk Action Bar
19. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
20. Kembalikan Selection Limit ke nilai awal lewat Fixture BE, lalu muat ulang halaman dengan F5

## Notes

- Langkah penghubung (S-03): langkah 1 (precondition state global Selection Limit), langkah 3 (Search atas suffix spec, R-16), langkah 11, 18, dan 19 (pemulihan seleksi, toast, dan Search, S-09), langkah 20 (pemulihan state global, R-08; hook `after` menjadi cadangan).
- Temuan untuk QA:
  - TC-AC-SU-115 butir b menyebut "baris ke-4 dan berikutnya" disabled; spec mengasersi baris ke-4 (hover dan tooltip) dan baris ke-5 (disabled).
  - TC-AC-SU-116 butir b: "persist sampai di-dismiss" tidak menyebut durasi pengamatan; spec mengasersi toast masih tampil sebelum di-dismiss secara eksplisit.
  - Nama user generik `User Seleksi N` dipilih penulis karena TC tidak menyebut nama.
