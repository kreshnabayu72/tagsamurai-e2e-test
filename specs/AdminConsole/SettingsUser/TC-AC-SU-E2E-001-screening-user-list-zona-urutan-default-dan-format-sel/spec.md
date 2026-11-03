---
id: TC-AC-SU-E2E-001-screening-user-list-zona-urutan-default-dan-format-sel
title: "Screening User List: Tiga Zona, Urutan Default Name, serta Format Sel Active dan Name"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-1
  - TC-AC-SU-2
  - TC-AC-SU-4
coverage:
  web: automated
---

# Screening User List: Tiga Zona, Urutan Default Name, serta Format Sel Active dan Name

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #2) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke Default User.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-user` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: entitas Principal memiliki user Pre-setup (aktor dan DS-UL) sehingga total user di entitas lebih dari 10; pagination dan ukuran halaman 10 teramati dari data itu. Spec tidak mengubah data Pre-setup.
- Data Dinamis (nama tampil dan email bersuffix per run; Tabel Data Uji Dinamis TC kosong, nilai diturunkan dari kolom Precondition dan Data Uji TC):

| TC | Nama TC | Nama seed | Email seed | State |
|---|---|---|---|---|
| TC-AC-SU-2 | `anggun lestari` | `anggun lestari {runId}-001` | `anggunlestari+{runId}-001@qwertysystem.net` | Activated, Active |
| TC-AC-SU-2 | `Andi Wijaya` | `Andi Wijaya {runId}-001` | `andiwijaya+{runId}-001@qwertysystem.net` | Activated, Active |
| TC-AC-SU-2 | `Budi Santoso` | `Budi Santoso {runId}-001` | `budisantoso+{runId}-001@qwertysystem.net` | Activated, Active |
| TC-AC-SU-4 | `John Doe` | `John Doe {runId}-001` | `johndoe+{runId}-001@qwertysystem.net` | Activated, Active, tanpa foto |
| TC-AC-SU-4 | `Mike Tan` | `Mike Tan {runId}-001` | `miketan+{runId}-001@qwertysystem.net` | Pending Activation, Active |
| TC-AC-SU-4 | `Rina Putri` | `Rina Putri {runId}-001` | `rinaputri+{runId}-001@qwertysystem.net` | Pending Email Confirmation, Active |

- Seeding di hook `before`, penghapusan data milik spec di hook `after`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SU-1: Screening halaman User List 3 zona

1. Amati halaman Settings > User dari atas ke bawah
2. Verifikasi Header: Breadcrumb `Settings > User`
3. Verifikasi Header: kedua segmen Breadcrumb berupa label statis (tidak bisa diklik)
4. Verifikasi Header: tidak ada Page Title terpisah di bawah Breadcrumb
5. Verifikasi Header: Table Tools `Search | Filter | Download | Changelog` tampil
6. Verifikasi Header: Table Tools rata kanan
7. Verifikasi Body: kolom berurutan `Checkbox | Active | Name | Email | Role | Position | Division | Employee ID | Modified By | Last Updated | Column Visibility (⋯)`
8. Verifikasi Body: kolom Active, Name, Email, Role, Position, Division, Employee ID, Modified By, dan Last Updated sortable
9. Verifikasi Body: kolom Column Visibility (⋯) unsortable
10. Klik header kolom Column Visibility (⋯)
11. Verifikasi overlay Column Visibility terbuka dengan CTA `[Setup Column]` di dalamnya
12. Tutup overlay Column Visibility dengan Esc
13. Verifikasi Body: body kolom Column Visibility pada tiap baris berisi row action menu (⋯)
14. Verifikasi Body: kolom Activation Status, Temporary User, Temporary Until, TAG, dan Custom Field aktif tidak tampil (default Hidden)
15. Verifikasi Body: Sidebar Group tampil di kanan
16. Verifikasi Body: Sidebar Group berada dalam SectionCard terpisah dari SectionCard Table
17. Verifikasi Body: Filter Panel collapsed
18. Verifikasi Footer: pagination tampil
19. Verifikasi Footer: pagination default 10 baris/halaman

### TC-AC-SU-2: Default sort User List Name A-Z case-insensitive

20. Ketik Search `{runId}-001`, tekan Enter
21. Verifikasi urutan baris kolom Name (A-Z case-insensitive): `Andi Wijaya {runId}-001`, `anggun lestari {runId}-001`, `Budi Santoso {runId}-001`
22. Verifikasi header Name tidak menampilkan ikon arah sort aktif lain selain default

### TC-AC-SU-4: Format sel kolom Active dan Name

23. Amati kolom Active dan Name pada baris `John Doe {runId}-001`, `Mike Tan {runId}-001`, dan `Rina Putri {runId}-001`
24. Verifikasi `John Doe {runId}-001`: switch Active ON
25. Verifikasi `John Doe {runId}-001`: switch Active berwarna primary Admin Console
26. Verifikasi `John Doe {runId}-001`: switch Active berada di kolom paling kiri setelah Checkbox
27. Verifikasi `John Doe {runId}-001`: sel Name berisi avatar initials `JD` dan Full Name dalam satu sel
28. Verifikasi `John Doe {runId}-001`: warna teks Name default netral
29. Verifikasi `John Doe {runId}-001`: tidak ada badge status di samping Name
30. Hover nama `John Doe {runId}-001`
31. Verifikasi warna teks Name berubah ke primary Admin Console (merah)
32. Verifikasi Name tanpa underline
33. Verifikasi `Mike Tan {runId}-001`: badge `Pending Activation` (warning) di samping nama
34. Verifikasi `Rina Putri {runId}-001`: badge `Pending Email Confirmation` (warning) di samping nama
35. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Langkah penghubung (S-03): langkah 12 (tutup overlay), langkah 20 (Search atas suffix `{runId}-001` agar tabel hanya berisi user seed milik spec; Search hanya penghubung, R-16), langkah 35 (reset Search). Layar awal Settings > User dibuka hook `beforeEach` suite sehingga langkah klik sidebar pada TC-AC-SU-1, TC-AC-SU-2, dan TC-AC-SU-4 tidak diulang.
- Temuan untuk QA:
  - Nama user TC (`anggun lestari`, `Andi Wijaya`, `Budi Santoso`, `John Doe`, `Mike Tan`, `Rina Putri`) dipakai sebagai nama bersuffix `{runId}-001` sesuai S-12 (Lampiran A tidak memuat pengecualian modul Settings > User). Initials `JD` dan urutan A-Z diasumsikan tidak berubah oleh suffix; perlu konfirmasi QA/FE bahwa initials diambil dari dua kata pertama nama.
  - TC-AC-SU-1 precondition b hanya menyebut "Data pre-setup User List tersedia" tanpa jumlah user; spec mengasumsikan total user entitas lebih dari 10 untuk asersi pagination 10 baris per halaman.
  - TC-AC-SU-4 hover menyebut warna "primary Admin Console (merah)" tanpa nilai warna terukur; spec mengasersi kelas warna primary Admin Console.
