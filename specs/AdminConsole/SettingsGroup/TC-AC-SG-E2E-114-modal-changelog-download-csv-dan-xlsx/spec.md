---
id: TC-AC-SG-E2E-114-modal-changelog-download-csv-dan-xlsx
title: "Modal Changelog: Download CSV dan XLSX dengan Filename Changelog-Group"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-269
coverage:
  web: automated
---

# Modal Changelog: Download CSV dan XLSX dengan Filename Changelog-Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas `Distributor Changelog` (Pre-setup #42) `totalControlChangelog_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_CHANGELOG_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja): entitas `Distributor Changelog` (Pre-setup #42) dengan riwayat Changelog Group seed: 12 entri campuran Create/Edit/Delete oleh `Admin Alpha` (tampil `Admin A`), `Admin Bravo` (`Admin B`), dan `Admin Charlie` (`Admin C`), tanggal 14 Jul 2026 08:00 sampai 08:15 dan variasi tanggal lain, termasuk entri Create `Region B` dan `Branch 3`, Edit `Region A1` menjadi `Region A`, dan Delete `Branch 4` (snapshot path `Region B > Branch 4`). Total entri tidak diasersi sebagai angka absolut (S-12); baris seed dikenali lewat isi kolom. Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini.
- Kemampuan teknis tambahan: membaca nama berkas, header, dan nilai sel berkas CSV dan XLSX yang diunduh, disediakan tim FE (cara membaca isi file tidak disebut TC, PRD, atau LLD).
- Kemampuan teknis: Fixture BE (pembacaan state BE, seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada; ditandai untuk tahap script).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global dan tidak menulis data.

## Test Steps

### TC-AC-SG-269: Download Changelog CSV dan XLSX dengan filename Changelog-Group

1. Klik ikon Changelog pada toolbar
2. Klik ikon Download di toolbar modal
3. Pilih `Download as CSV`
4. Verifikasi tidak ada toast sukses
5. Verifikasi berkas `Changelog-Group.csv` terunduh
6. Verifikasi header kolom berkas CSV sama dengan kolom yang visible di modal
7. Verifikasi kolom Group Name pada berkas CSV berisi snapshot full path breadcrumb node saat entri ditulis
8. Klik ikon Download di toolbar modal
9. Pilih `Download as XLSX`
10. Verifikasi tidak ada toast sukses
11. Verifikasi berkas `Changelog-Group.xlsx` terunduh
12. Verifikasi header kolom berkas XLSX sama dengan kolom yang visible di modal
13. Verifikasi kolom Group Name pada berkas XLSX berisi snapshot full path breadcrumb node saat entri ditulis
14. Tutup modal Changelog lewat `[✕]`

## Notes

- Langkah penghubung (S-03): penutupan modal di akhir. Asersi "tidak ada toast sukses" ditaruh segera setelah pemicu dan sebelum asersi berkas terunduh yang menjadi anchor positif (bagian 8b butir 11).
- Pembagian TC lintas spec: TC-AC-SG-269 ada di spec ini; spec Modal Changelog lain (067 sampai 074) tidak memuat Download.
- Temuan untuk QA:
  - TC-AC-SG-269 butir b (nilai sel Group Name pada berkas) menyentuh isi berkas (nilai sel). TC ini diperlakukan sebagai asersi fungsional (nama berkas, header, dan nilai sel Group Name); pembacaan isi berkas bergantung pada kemampuan baca yang disediakan tim FE.
  - TC-AC-SG-269 tidak menyebut nilai snapshot path yang diharapkan pada berkas; spec mengasersi bentuk snapshot path tanpa nilai literal.
  - "Kolom sesuai kolom visible" diasersi pada header berkas terhadap kolom visible default modal (7 kolom).
