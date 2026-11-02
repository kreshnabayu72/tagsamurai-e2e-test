---
id: TC-AC-SU-E2E-003-tooltip-toolbar-hover-baris-dan-klik-sel-selain-name
title: "User List: Tooltip Ikon Toolbar, Hover Baris, dan Klik Sel Selain Name"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-3
  - TC-AC-SU-13
  - TC-AC-SU-16
coverage:
  web: automated
---

# User List: Tooltip Ikon Toolbar, Hover Baris, dan Klik Sel Selain Name

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-13, 16 | `John Doe` | `John Doe {runId}-003` | `johndoe+{runId}-003@qwertysystem.net` | Activated, Active; Email dan Position terisi |

- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-3: Tooltip hover icon toolbar dan header Column Visibility

1. Hover icon Search
2. Verifikasi tooltip `Search`
3. Hover icon Filter
4. Verifikasi tooltip `Filter`
5. Hover icon Download
6. Verifikasi tooltip `Download`
7. Hover icon Changelog
8. Verifikasi tooltip `Changelog`
9. Hover icon (⋯) header kolom Actions
10. Verifikasi tooltip `Column Visibility`

### TC-AC-SU-13: Hover baris menampilkan highlight dan kolom Actions

11. Ketik Search `John Doe {runId}-003`, tekan Enter
12. Hover baris `John Doe {runId}-003`
13. Verifikasi baris ter-highlight
14. Verifikasi kolom Actions (⋯) baris tersebut tampil

### TC-AC-SU-16: Klik area baris selain Name tidak melakukan apa pun

15. Klik sel Email baris `John Doe {runId}-003`
16. Verifikasi tidak ada navigasi, popup, maupun perubahan data setelah klik sel Email
17. Klik sel Position baris `John Doe {runId}-003`
18. Verifikasi tidak ada navigasi, popup, maupun perubahan data setelah klik sel Position
19. Verifikasi halaman tetap Settings > User
20. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 11 (Search untuk menemukan baris target, R-16) dan langkah 20 (reset Search).
- Tooltip diasersi segera setelah hover sebelum hover berikutnya (bagian 8b butir 5).
- Temuan untuk QA:
  - TC-AC-SU-3 menyebut "header kolom Actions" sedangkan TC-AC-SU-1 menamai kolom itu Column Visibility (⋯); spec memakai header (⋯) yang sama.
  - TC-AC-SU-16 "tidak ada perubahan data" tidak menyebut cara cek; spec mengasersi nilai sel baris tidak berubah dari tampilan.
  - Nama user TC (`John Doe`) dipakai sebagai nama bersuffix `{runId}-003` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User).
