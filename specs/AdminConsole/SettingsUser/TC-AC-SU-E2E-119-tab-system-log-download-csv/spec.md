---
id: TC-AC-SU-E2E-119-tab-system-log-download-csv
title: "Tab System Log: Download CSV tanpa Search atau Filter"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SU-422
coverage:
  web: automated
---

# Tab System Log: Download CSV tanpa Search atau Filter

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD` (sudah terdaftar). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Suite berjalan serial (`parallel: false`). Flag Guided Tooltip disetel `seen` oleh hook suite; sesi API aktor dan Fixture BE disediakan tim FE/BE (lihat `suite.md`). Spec tidak memakai endpoint karangan.
- General Settings (Date Format, Time Format, Time Zone) entitas Principal tidak diubah spec ini; format tanggal yang diasersi dibaca dari General Settings tersebut.
- Data seeding (Fixture BE): user `Jane Smith {runId}-119` (email `janesmith+{runId}-119@qwertysystem.net`) sebagai aktor dengan 12 entri System Log (lebih dari satu halaman pada ukuran halaman bawaan). N total dibaca lewat kemampuan baca Fixture BE sebelum aksi dan tidak diasersi sebagai angka absolut.
- Kemampuan teknis: pembacaan berkas unduhan (nama berkas, header kolom, jumlah baris) oleh tim FE; kemampuan seed dan baca entri System Log disediakan tim FE/BE. Isi sel berkas tidak diasersi (kelas f).
- Hook `before` men-seed data milik spec ini lewat Fixture BE; hook `after` menghapus user seeding di atas lewat Fixture BE. Entri audit trail yang dibuat sistem tidak dihapus. Fixture `settingsUser` (berkas belum ada; dibuat tim FE) menyimpan nama dan email user seeding; password tidak disimpan di fixture.

## Test Steps

### TC-AC-SU-422: Download Tab System Log sebagai CSV tanpa search atau filter

1. Cari `Jane Smith {runId}-119` di Search pada User List, tekan Enter, lalu buka Detail user tersebut
2. Klik tab `System Log`
3. Catat jumlah total entri System Log user target lewat kemampuan baca Fixture BE (N)
4. Verifikasi tabel menampilkan lebih dari 1 halaman data
5. Hover icon Download
6. Verifikasi tooltip `Download` tampil
7. Klik icon Download
8. Verifikasi overlay menampilkan `Download as CSV` dan `Download as XLSX`
9. Klik `Download as CSV`
10. Verifikasi tidak ada toast sukses
11. Verifikasi file `System-Log-Jane-Smith-{runId}-119.csv` terunduh
12. Verifikasi file berisi seluruh baris Tab System Log dari semua halaman (jumlah baris data sama dengan N)
13. Verifikasi kolom pada file sesuai kolom yang visible pada tabel

## Notes

- Langkah pembuka yang mencari user target lewat Search pada User List lalu membuka Detail adalah langkah penghubung (R-16, S-03); kotak Search User List tidak dipakai sebagai objek uji.
- Asersi absence toast sukses diletakkan segera setelah pemicu `Download as CSV` dan sebelum asersi berkas (bagian 8b butir 11); berkas yang terunduh adalah anchor positif bahwa respons sudah diproses.
- TC-423 (XLSX dengan search atau filter aktif) ada di spec 195 karena Expected-nya memuat nilai sel berkas.
- Temuan untuk QA:
  - Nama berkas pada TC (mis. `Changelog-Jane-Smith.csv`) diturunkan dari nama user dengan spasi diganti `-`; dengan nama bersuffix, spec menulis nama berkas dengan suffix `{runId}-NNN`. Aturan penamaan berkas untuk nama yang memuat suffix tidak dinyatakan di TC.
  - Cara men-seed entri System Log (Date, Action, Object, Name, Field, Old Value, New Value, aktor, termasuk snapshot full path untuk Object `Group`) tidak dinyatakan di TC, PRD, atau LLD; kemampuan ini ditulis 'disediakan tim FE/BE' tanpa endpoint karangan (S-13).
  - Nama target `Jane Smith` pada TC dipakai sebagai nama bersuffix `Jane Smith {runId}-NNN` per run (S-12); asersi spec memakai nilai kolom log, bukan urutan atau Search atas nama user.
