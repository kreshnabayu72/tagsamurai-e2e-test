---
id: TC-GS-NLU-E2E-113-sinkronisasi-format-tanggal-general-settings
title: "Sinkronisasi format tanggal General Settings"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-411
  - TC-GS-NLU-412
  - TC-GS-NLU-413
coverage:
  web: automated
---

# Sinkronisasi format tanggal General Settings

## Prerequisites

- Mode: FE+BE. Spec berjalan di atas backend nyata; tidak ada respons yang di-mock atau di-intercept.
- Akun: Total Control, `Siti Nurhaliza (Siti N)`, `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Tabel Data Uji Pre-setup No. 1), password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture.
- Environment variable: `GS_TC_PASSWORD`.
- Flag Guided Tooltip `guided_tooltip_seen_gs-non-login-user`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Data Pre-setup No. 9 sampai 13 (Position `Driver` dan `Manager`; Division `Operations`, `Warehouse`, `Logistics`, `Finance`; Login User `Ahmad Fauzi` dan `Dewi Anggraini`; Custom Field dasar) hanya dibaca, tidak diubah atau dihapus.
- State global: General Settings Date Format `dd/MM/yy`, Time Format 24 jam, Timezone `Asia/Jakarta` (Tabel Data Uji Pre-setup No. 16). Hook `before` memastikan nilai itu terpasang (nilai awal dicatat) dan hook `after` memulihkan nilai awal; kemampuan membaca dan menyetel General Settings disediakan tim FE (akun pelaku tidak disebut TC, PRD, atau LLD). Suite berjalan serial (`parallel: false`).
- Data milik spec (di-seed hook `before` lewat API, dibersihkan hook `after`; mekanisme seeding dan penghapusan disediakan tim FE/BE): `Rina Marlina {runId}-113` (First Name `Rina`, Last Name `Marlina {runId}-113`, Position `Driver`, Division `Logistics`, Email `rinamarlina+{runId}-113@qwertysystem.net`, Represented By `Dewi Anggraini`, Active, Temporary dengan Temporary Until hari ini ditambah 30 hari) beserta satu transaksi Borrowed Asset dengan Due Return Date (transaksi FAMS disediakan tim FE/BE; lihat Temuan untuk QA). Entri Create dihasilkan seeding lewat endpoint Create standar.
- Kemampuan teknis: date picker pada Filter Panel dan pembacaan kolom tanggal.
- Pemulihan: hook `after` menghapus lewat API semua data `{runId}-113` dan memulihkan General Settings ke nilai awal.
- Fixture `fixtures/non-login-user.json` untuk nilai data Pre-setup dan Dinamis belum ada; disediakan tim FE (S-12). Nilai di langkah ditulis literal sampai fixture tersedia.

## Test Steps

### TC-GS-NLU-411: Format tanggal dan jam General Settings pada tabel List dan filter tanggal

1. Ketik Search `Rina Marlina {runId}-113`, tekan Enter
2. Verifikasi kolom Last Update baris `Rina Marlina {runId}-113` memakai format tanggal `dd/MM/yy` dan jam 24 jam
3. Verifikasi jam kolom Last Update mengikuti timezone `Asia/Jakarta`
4. Klik icon Filter untuk membuka Filter Panel, lalu pilih tanggal pada date picker Last Update
5. Verifikasi teks tanggal terpilih di kotak date picker Last Update mengikuti Date Format `dd/MM/yy`
6. Tutup Filter Panel tanpa menerapkan filter

### TC-GS-NLU-412: Format tanggal dan jam General Settings pada Modal Changelog agregat dan filter tanggalnya

7. Klik icon `Changelog` pada Table Tools sehingga Modal Changelog terbuka
8. Verifikasi kolom Date Modal Changelog agregat memakai format tanggal `dd/MM/yy` dan jam 24 jam
9. Buka Filter Panel Modal Changelog, lalu pilih tanggal pada date picker
10. Verifikasi teks tanggal terpilih di kotak date picker Modal Changelog mengikuti Date Format `dd/MM/yy`
11. Tutup Filter Panel tanpa menerapkan filter, lalu tutup Modal Changelog dengan `✕`

### TC-GS-NLU-413: Format tanggal dan jam General Settings pada Detail dan tab di dalamnya

12. Klik Name baris `Rina Marlina {runId}-113` untuk membuka Detail
13. Verifikasi `Temporary until` pada General Information memakai Date Format `dd/MM/yy`
14. Klik tab `Changelog`
15. Verifikasi kolom Date Tab Changelog memakai format tanggal `dd/MM/yy` dan jam 24 jam
16. Klik tab `Responsibilities`, lalu sub-tab `Borrowed Assets`
17. Verifikasi kolom Due Return Date Borrowed Assets memakai Date Format `dd/MM/yy`

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 1 (Search record yang dicari, R-16), langkah 6 dan 11 (menutup Filter Panel dan modal).
- State global: spec ini membaca format General Settings dan tidak mengubah nilainya selama langkah; hook `before` hanya memastikan nilai Pre-setup No. 16 terpasang dan `after` memulihkan nilai awal (R-08).
- Temuan untuk QA:
  - TC-GS-NLU-413 memakai Rina Marlina dengan Borrowed Assets (Due Return Date), tetapi Tabel Data Uji Pre-setup No. 14 hanya memuat transaksi Borrowed untuk Budi Kurniawan, Banyak Aset, dan Konversi Aset; transaksi Borrowed untuk Rina Marlina belum tertulis di Pre-setup dan disediakan tim FE/BE.
  - TC-GS-NLU-411 dan 412 tidak menyebut tanggal yang dipilih pada date picker dan cara menutup Filter Panel tanpa Apply; spec memilih tanggal bebas dan menutup panel tanpa menerapkan.
  - Expected TC-GS-NLU-411 menyebut jam 24 jam dan timezone sesuai General Settings tanpa contoh teks persis; spec mengasersi format `dd/MM/yy` dengan jam 24 jam dan mengamati timezone `Asia/Jakarta` dari jam entri seeding.
  - TC-GS-NLU-412 dan 413 menyatakan General Settings "sama seperti TC format tanggal List" sehingga nilainya mengikuti Pre-setup No. 16.
