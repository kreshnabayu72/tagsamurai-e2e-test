---
id: TC-GS-UOM-E2E-018-create-screening-clear-field-dan-tutup-bersih
title: "Screening Popup Create Unit, Focus Trap, Clear Field, dan Tutup Form Kosong"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-UOM-37
  - TC-GS-UOM-38
  - TC-GS-UOM-54
  - TC-GS-UOM-57
coverage:
  web: automated
---

# Screening Popup Create Unit, Focus Trap, Clear Field, dan Tutup Form Kosong

## Prerequisites

- Mode: mock. Seluruh API di-mock (integration test FE tanpa backend nyata); spec ini hanya menguji tampilan dan perilaku popup Create Unit di browser.
- Hook suite (login akun default, `beforeEach` membuka Measurement, flag Guided Tooltip `guided_tooltip_seen_gs-measurement`): lihat `suite.md`; pada run mock, API pendukung di luar modul (identitas pengguna, menu, flag Guided Tooltip) disediakan tim FE.
- Respons daftar Brand dan API pendukung halaman Master Reference: disediakan tim FE (lihat `suite.md`, bagian Data bersama).
- Kebutuhan mock (path endpoint mengikuti `openapi.yaml` dan `low-level-design.md` modul Measurement dan dilengkapi tim FE di skrip; tidak disalin di spec ini):
  - Sesi dan payload izin akun Total Control Client A `totalControl_automated_qaTeam1@qwertysystem.net` (Sari Dewi) dengan capability Manage master reference lengkap (Read, Create, Update, Delete). Login di hook `before` (env `GS_TC_PASSWORD` untuk run non-mock; tidak ditulis di spec).
  - Respons List Measurement: 8 unit Pre-setup Client A (Box, Dozen, Gram, Kilogram, Liter, Meter, Pack, Pieces), supaya halaman Measurement dan tombol [+ Unit] tampil.
  - Respons cek keunikan Unit Name saat mengetik (debounce sekitar 500 ms): nama tersedia untuk semua nilai yang diketik kecuali `Kilogram` (tanpa membedakan huruf besar kecil), yang dibalas sudah ada, sehingga error `Unit name already exists` muncul untuk `Kilogram`.
  - Endpoint Create Measurement tidak boleh terpanggil di spec ini; bila terpanggil, spec dianggap gagal (tidak ada TC di spec ini yang men-submit).
- Data: tidak ada data yang dibuat atau diubah, sehingga tidak ada cleanup.
- Kemampuan teknis: navigasi keyboard (Tab, Esc) dan pembacaan fokus elemen; pengecekan ukuran modal.
- State global: tidak ada yang diubah. Sesi tetap di akun default suite, sehingga hook `after` tidak perlu memulihkan sesi.

## Test Steps

### TC-GS-UOM-37: Screening Popup Create Unit

1. Klik [+ Unit]
2. Verifikasi Header: Title `Create Unit` dan icon close `[✕]`
3. Verifikasi Body: field `Unit Name *` dengan placeholder `e.g. Kilogram, Meter, Unit`, kosong
4. Verifikasi Body: field `Symbol *` dengan placeholder `e.g. kg, m, pcs`, kosong
5. Verifikasi Body: checkbox `Stay on this form after submitting` unchecked
6. Verifikasi Footer (rata kanan): `[Clear Field]` (text, primary) dan `[Submit]` (filled, success)
7. Verifikasi tidak ada tombol `[Cancel]` (Must NOT)
8. Verifikasi modal berukuran md

### TC-GS-UOM-38: Accessibility Popup Create Unit: focus trap dan Esc pada form kosong

9. Tekan Tab berulang melewati elemen fokus terakhir di modal
10. Verifikasi fokus keyboard tetap berputar di dalam modal
11. Tekan Esc
12. Verifikasi modal tertutup
13. Verifikasi dialog Unsaved Changes tidak muncul

### TC-GS-UOM-54: Clear Field mengosongkan field dan menghapus error tanpa dialog

14. Klik [+ Unit]
15. Centang checkbox `Stay on this form after submitting`
16. Ketik Unit Name `Kilogram` sampai error inline duplikat muncul
17. Verifikasi error inline `Unit name already exists` tampil
18. Isi Symbol `x`
19. Klik [Clear Field]
20. Verifikasi field Unit Name kosong
21. Verifikasi field Symbol kosong
22. Verifikasi error inline hilang
23. Verifikasi border danger hilang
24. Verifikasi dialog Unsaved Changes tidak muncul
25. Verifikasi modal tetap terbuka
26. Verifikasi checkbox `Stay on this form after submitting` tetap tercentang
27. Verifikasi fokus kursor kembali ke field Unit Name

### TC-GS-UOM-57: Menutup form Create yang kosong tidak memunculkan dialog Unsaved Changes

28. Klik `[✕]` untuk menutup form dari TC-GS-UOM-54 (field kosong, tidak dirty)
29. Klik [+ Unit] (form baru yang bersih)
30. Klik icon `[✕]`
31. Verifikasi modal tertutup langsung
32. Verifikasi dialog Unsaved Changes tidak muncul

## Notes

- Mode: mock. Sumber: `global-settings/measurement/TestCases/tc-measurement.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pembukaan form ada tiga: (1) untuk TC-GS-UOM-37 dan TC-GS-UOM-38 (screening, focus trap, lalu ditutup dengan Esc), (2) untuk TC-GS-UOM-54 (Clear Field; ditutup lewat `[✕]` di langkah 28 karena form pasca-[Clear Field] kosong sehingga tidak dirty), dan (3) form baru untuk TC-GS-UOM-57 supaya penutupan bersih tidak bercampur dengan sisa state Clear Field (prinsip 6 konvensi). Jumlah buka form sama dengan jumlah kejadian menutup.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 18 (mengisi Symbol `x` agar Clear Field mengosongkan kedua field; TC hanya menyebut Symbol `x` di Langkah Uji 3) dan langkah 28 (menutup form TC-GS-UOM-54). Langkah 17 memverifikasi prasyarat Expected Result b ("error inline ... hilang") dan tidak ada di Expected Result TC.
- Expected Result b TC-GS-UOM-54 ("Error inline dan border danger hilang") dipecah per klausa (langkah 22 dan 23); Expected Result a TC-GS-UOM-54 dipecah per field (langkah 20 dan 21) sesuai S-01.
- TC-GS-UOM-37 sampai 57 memakai Total Control yang sama, sehingga tidak ada ganti akun.
- Spec ini berdiri terpisah dari `TC-GS-UOM-E2E-019-create-unsaved-changes-dialog` karena gabungan keduanya 59 langkah (32 + 27), jauh melewati batas 35 langkah, dan 019 membutuhkan kemampuan penanganan dialog `beforeunload` yang tidak dibutuhkan spec ini. Tiap spec membuka popup Create sendiri sehingga kegagalan satu spec tidak membuat spec lain kehilangan makna.
- Temuan untuk QA:
  - Langkah Uji TC-GS-UOM-54 menulis "Isi Unit Name `Kilogram` hingga error duplikat muncul, Symbol `x`" tanpa menyebut bahwa pemicu error adalah cek keunikan real-time; spec mengikuti TC dan mock cek keunikan mengembalikan nama sudah ada untuk `Kilogram`.
  - Path dan skema endpoint mock disediakan tim FE sesuai `openapi.yaml` dan `low-level-design.md` modul (S-13).
