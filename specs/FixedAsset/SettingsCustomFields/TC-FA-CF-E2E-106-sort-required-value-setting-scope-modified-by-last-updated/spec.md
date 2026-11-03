---
id: TC-FA-CF-E2E-106-sort-required-value-setting-scope-modified-by-last-updated
title: "Sort: Required, Value Setting, Scope, Modified By, dan Last Updated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-CF-399
  - TC-FA-CF-400
  - TC-FA-CF-401
  - TC-FA-CF-402
  - TC-FA-CF-403
coverage:
  web: automated
---

# Sort: Required, Value Setting, Scope, Modified By, dan Last Updated

## Prerequisites

- Mode: FE+BE (backend nyata). Suite berjalan serial (`parallel: false`).
- Akun aktor: Total Control Company Alpha (Pre-setup #1, Sarah Johnson) `totalControl_automated_{namaCompany}@qwertysystem.net` dengan namaCompany Company Alpha. Login di hook `before` spec ini dengan `Spectra.env.FA_TC_PASSWORD`; halaman dibuka hook `beforeEach` suite. Password tidak ditulis di spec atau fixture. Nama env `FA_TC_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh tim FE.
- Data Pre-setup (tetap di environment, tidak diubah spec ini, bernama literal tanpa suffix karena asersi urutan bergantung pada nama, nilai kolom, Modified By, dan Last Updated seed; fixture baru belum ada, `Fixture.faCustomFields.alphaGeneral`): Company Alpha (Pre-setup #11), General Settings Date Format `dd/MM/yy`, baseline tab General (Pre-setup #12) delapan field:
  - `Asset Serial Tag`: Required Yes; Value Setting `—`; Scope General; Modified By Budi Santoso; Last Updated 17/10/26 10:45.
  - `Storage Capacity`: Required No; Value Setting `0 Decimal Places`; Scope `Generator`, `Pump`; Modified By Siti Amelia; Last Updated 16/10/26 14:20.
  - `Equipment Class`: Required No; Value Setting `Class A, Class B, Class C`; Scope `Compressor`, `Generator`, `Pump`; Modified By Siti Amelia; Last Updated 15/10/26 11:30.
  - `Operating Voltage`: Required Yes; Value Setting `—`; Scope `Generator`; Modified By Budi Santoso; Last Updated 14/10/26 09:05.
  - `Total Cost`: Required `—`; Value Setting `—`; Scope General; Modified By Joko Widodo; Last Updated 13/10/26 16:30.
  - `Depreciated Ratio`: Required No; Value Setting `2 Decimal Places`; Scope General; Modified By Joko Widodo; Last Updated 10/10/26 11:15.
  - `Compliance File`: Required No; Value Setting `—`; Scope General; Modified By Budi Santoso; Last Updated 03/10/26 08:50.
  - `Legacy Tag`: Required No; Value Setting `—`; Scope `—` (kosong); Modified By Joko Widodo; Last Updated 02/10/26 15:10.
- Data Dinamis: tidak ada; spec ini tidak membuat atau mengubah data.
- Hook suite yang berlaku (lihat `suite.md`): seed reset baseline Company Alpha di hook `before`, flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` true untuk akun aktor di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis: pembacaan ikon sort per header kolom dan urutan baris tabel pada halaman teramati (delapan baris tampil pada satu halaman, ukuran halaman bawaan 10).
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-CF-399: Sort kolom Required mengikuti Yes First lalu No First dengan nilai kosong di ujung

1. Klik header `Required` sekali
2. Verifikasi urutan menaik (Yes First): `Asset Serial Tag`, `Operating Voltage`, lima baris `No`, lalu `—` (`Total Cost`) di akhir
3. Klik header `Required` sekali lagi
4. Verifikasi urutan menurun (No First): `—` (`Total Cost`) di awal, lima baris `No`, lalu dua baris `Yes`

### TC-FA-CF-400: Sort kolom Value Setting berdasarkan teks lengkap dengan baris strip di akhir saat menaik

5. Klik header `Value Setting` sekali
6. Verifikasi urutan menaik: `Storage Capacity` (`0 Decimal Places`), `Depreciated Ratio` (`2 Decimal Places`), `Equipment Class` (`Class A, Class B, Class C`), lalu lima baris `—`
7. Klik header `Value Setting` sekali lagi
8. Verifikasi urutan menurun: lima baris `—` di awal, lalu urutan terbalik (`Equipment Class`, `Depreciated Ratio`, `Storage Capacity`)

### TC-FA-CF-401: Sort kolom Scope berdasarkan teks Scope lengkap dengan baris strip di akhir saat menaik

9. Klik header `Scope` sekali
10. Verifikasi urutan menaik: `Equipment Class` (`Compressor, Generator, Pump`), empat baris `General` (`Asset Serial Tag`, `Compliance File`, `Depreciated Ratio`, `Total Cost`), `Operating Voltage` (`Generator`), `Storage Capacity` (`Generator, Pump`), lalu `Legacy Tag` (`—`)
11. Klik header `Scope` sekali lagi
12. Verifikasi urutan menurun: `Legacy Tag` (`—`) di awal lalu urutan terbalik

### TC-FA-CF-402: Sort kolom Modified By berdasarkan nama lengkap, bukan bentuk singkat

13. Klik header `Modified By` sekali
14. Verifikasi urutan menaik berdasarkan nama lengkap: `Budi Santoso` (`Asset Serial Tag`, `Compliance File`, `Operating Voltage`), `Joko Widodo` (`Depreciated Ratio`, `Legacy Tag`, `Total Cost`), `Siti Amelia` (`Equipment Class`, `Storage Capacity`)

### TC-FA-CF-403: Sort kolom Last Updated Oldest First lalu Newest First

15. Klik header `Last Updated` sekali
16. Verifikasi urutan Oldest First: `Legacy Tag` (02/10/26) di atas hingga `Asset Serial Tag` (17/10/26) di bawah
17. Klik header `Last Updated` sekali lagi
18. Verifikasi urutan Newest First: `Asset Serial Tag` di atas hingga `Legacy Tag` di bawah

## Notes

- Spec memuat 18 langkah, di bawah ambang sekitar 35 langkah. Satu topik (Sort tabel utama kolom lanjutan), satu dataset, satu akun.
- Tidak ada langkah penghubung: mengklik header kolom lain mereset sort kolom sebelumnya (TC-FA-CF-405), sehingga tiap TC mulai dari klik pertama kolomnya.
- Kolom Modified By diasersi berurutan berdasarkan nama lengkap (`Budi Santoso`, `Joko Widodo`, `Siti Amelia`) sesuai Expected TC-FA-CF-402; sel tabel sendiri menampilkan bentuk `[First Name] [Last Initial]` (R-14).
- Pada langkah 14, urutan di dalam tiap kelompok nama tidak diasersi (Expected TC hanya menyebut urutan antar nama).
- Temuan untuk QA:
  - TC-FA-CF-402 hanya memuat satu klik (menaik); arah menurun Modified By tidak diuji TC.
  - TC-FA-CF-400 Expected b menyebut "urutan terbalik" tanpa nama baris; langkah 8 menyebut tiga baris bernilai berdasarkan Expected a (`Equipment Class`, `Depreciated Ratio`, `Storage Capacity`).
  - Urutan enam baris `—` pada TC-FA-CF-400 dan empat baris `General` pada TC-FA-CF-401 mengikuti default sort (Field Name A-Z) yang tidak disebut Expected; spec tidak mengasersi urutan di dalam kelompok itu selain yang disebut TC.
  - Seluruh TC pada spec ini tidak memiliki Post Condition (kolom `-`); tidak ada yang diasersi.
