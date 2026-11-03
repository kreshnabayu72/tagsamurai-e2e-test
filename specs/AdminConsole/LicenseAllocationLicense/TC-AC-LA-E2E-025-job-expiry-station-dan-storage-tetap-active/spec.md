---
id: TC-AC-LA-E2E-025-job-expiry-station-dan-storage-tetap-active
title: "Job Expiry Transition: Station dan Storage Tetap Active di Tab Current"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-30
coverage:
  web: automated
---

# Job Expiry Transition: Station dan Storage Tetap Active di Tab Current

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var password di atas adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status) bersifat baca-saja untuk spec ini; spec tidak menulis data. Data destruktif dipulihkan baseline automation sebelum tiap spec (Catatan TC).
- Data Pre-setup: #23 Bengkel Cahaya Motor (FAMS Professional Paid Active, End Date 31 Dec 2026), #52 alokasi `Active` Asset Control Station +2 dan Storage +50 GB Client-wide Klinik Harapan Bunda. Spec membuat sendiri satu alokasi `Active` Concurrent User +10 pada FAMS Professional Bengkel Cahaya Motor (seperti Pre-setup #47, `Dewi A`) lewat seeding backend di hook `before`; Allocation ID dirujuk lewat `Fixture.license-allocation-license` (kunci seedStation, seedStorage, ownConcurrentActive).
- Kemampuan teknis (kelas d, disediakan tim FE/BE): atur jam server dan jam browser absolut (fixture waktu, tanggal acuan uji `22 Dec 2026`, zona waktu General Settings milik Plan Owner term Target); picu dan baca status job Expiry Transition lewat kueri fixture status job (batas tunggu 2 menit).
- State global yang diubah: jam server dan jam browser digeser ke tanggal setelah End Date `31 Dec 2026`; keduanya dipulihkan di langkah penghubung sebelum aksi aktor berikutnya dan di hook `after`. Job Expiry Transition juga mengubah alokasi `Active` lain pada term itu (termasuk Pre-setup #47); pemulihan dilakukan fixture backend yang disediakan tim FE/BE di hook `after`. Suite berjalan serial.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-30: Station dan Storage tetap Active di tab Current sesudah Expiry Transition

1. Ketik Search Allocation ID seed Station (`Fixture.license-allocation-license.seedStation`), tekan Enter
2. Verifikasi baris Asset Control Station +2 berstatus `Active` tampil pada tab Current (kondisi awal)
3. Ganti isi kotak search dengan Allocation ID seed Storage (`Fixture.license-allocation-license.seedStorage`), tekan Enter
4. Verifikasi baris Storage +50 GB berstatus `Active` tampil pada tab Current (kondisi awal)
5. Ganti isi kotak search dengan Allocation ID alokasi `Active` Concurrent User milik spec pada Bengkel Cahaya Motor (`Fixture.license-allocation-license.ownConcurrentActive`), tekan Enter
6. Verifikasi baris Concurrent User Bengkel Cahaya Motor berstatus `Active` tampil pada tab Current (kondisi awal)
7. Atur jam server dan jam browser ke tanggal absolut setelah End Date term Bengkel Cahaya Motor
8. Jalankan Expiry Transition dan tunggu job selesai (kueri fixture status job, batas 2 menit)
9. Pulihkan jam server dan jam browser
10. Klik menu `License Allocation` di sidebar
11. Ketik Search Allocation ID seed Station (`Fixture.license-allocation-license.seedStation`), tekan Enter
12. Verifikasi baris Station tetap berstatus `Active` pada tab Current
13. Ganti isi kotak search dengan Allocation ID seed Storage (`Fixture.license-allocation-license.seedStorage`), tekan Enter
14. Verifikasi baris Storage tetap berstatus `Active` pada tab Current
15. Klik tab `History`
16. Ketik Search Allocation ID seed Station (`Fixture.license-allocation-license.seedStation`), tekan Enter
17. Verifikasi hasil Search kosong dengan empty state `No results found`; baris Station tidak tampil di tab History
18. Ganti isi kotak search dengan Allocation ID seed Storage (`Fixture.license-allocation-license.seedStorage`), tekan Enter
19. Verifikasi hasil Search kosong dengan empty state `No results found`; baris Storage tidak tampil di tab History
20. Ganti isi kotak search dengan Allocation ID alokasi Concurrent User milik spec (`Fixture.license-allocation-license.ownConcurrentActive`), tekan Enter
21. Verifikasi baris Concurrent User Bengkel Cahaya Motor tampil pada tab History

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah Search untuk menemukan baris target (R-16), langkah mengatur dan memulihkan jam, langkah menjalankan Expiry Transition dan menunggu job, dan langkah klik menu `License Allocation` yang mereset Search.
- P-2: Expiry Transition adalah proses sistem yang hanya memicu kondisi yang diuji (baris berpindah tab), bukan objek asersi job; asersi tertuju pada isi tab List.
- Jam dipulihkan sebelum aksi aktor berikutnya (S-09). Alokasi Concurrent User milik spec dipakai sebagai target job supaya Pre-setup #47 tidak menjadi satu-satunya target (S-06).
- Temuan untuk QA:
  - TC-AC-LA-30 langkah 1 menyebut `tanggal setelah End Date term Bengkel Cahaya Motor` tetapi tidak menyebut nilai tanggal, jam, dan zona waktu; nilai absolut disepakati tim FE/BE.
  - TC-AC-LA-30 tidak menyebut cara menjalankan job Expiry Transition (hanya `Jalankan Expiry Transition`); spec memakai kueri fixture status job tanpa endpoint karangan (S-13).
  - Expected c (`Alokasi Concurrent User Bengkel Cahaya Motor pindah ke tab History`) memakai alokasi yang tidak disebut Allocation ID-nya (Pre-setup #47); spec memakai alokasi milik spec supaya data Pre-setup tidak berubah.
