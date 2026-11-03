---
id: TC-AC-ACTS-E2E-005-distributor-stock-list-metrik-di-scope-unit-sendiri
title: "Distributor di Stock List: Total Registered, Available, Damaged/Missing, In Use, dan Last Updated di-Scope ke Unit Sendiri"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-16
  - TC-AC-ACTS-17
  - TC-AC-ACTS-18
  - TC-AC-ACTS-19
  - TC-AC-ACTS-890
coverage:
  web: automated
---

# Distributor di Stock List: Total Registered, Available, Damaged/Missing, In Use, dan Last Updated di-Scope ke Unit Sendiri

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Distributor Toggle ON `distributorOn_automated_{namaCompany}@qwertysystem.net` (Pre-setup #9), password dari `Spectra.env.AC_DIST_ON_PASSWORD` (nama env baru; didaftarkan di `executionConfig.environmentVariables` dan `.env.example` oleh pemilik repo e2e). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control). Tidak ada ganti akun di tengah spec.
- Hook suite (flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen`, sesi API aktor, jaring pengaman dialog `beforeunload`, pemulihan flag) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali dinyatakan di bawah.
- Fixture `Fixture.tagStock` (berkas fixture belum ada; disediakan tim FE) memuat identitas data Pre-setup: `skuRfid` (`RFID-ASSET-CORE-R5`), `deviceRfid` (`RFID Asset Tag`), `skuNfc` (`NFC-CARD-BETA-N2`), `deviceNfc` (`NFC Access Card`), `skuBle` (`BLE-BEACON-ALPHA-B1`), `deviceBle` (`BLE Beacon Alpha`), `skuGps` (`GPS-TRACK-CORE-G3`), `deviceGps` (`GPS Tracker Core`), `skuEmpty` (`RFID-SEAL-DELTA-R1`), `skuPlain` (`RFID-PLAIN-X1`), `skuGpsNew` (`GPS-NEW-TEST-G9`). Tidak ada password atau token di fixture.
- Data seed milik spec (SKU bersuffix `{runId}-005`, di-seed lewat fixture BE di hook `before`, dihapus di hook `after`): SKU P (Distributor A: 30 Available, 4 Damaged/Missing, 20 In Use dari batch sendiri, total 54 unit lokal; Principal 500 unit; Distributor B 50 unit SKU yang sama); SKU Q (Distributor A punya unit lokal dengan aktivitas; waktu aktivitas unit lokal terbaru dibaca lewat kemampuan baca BE); SKU R (belum ada unit lokal tetapi ada aktivitas Principal).
- Angka 500 (Principal) dan 50 (Distributor B) pada TC-AC-ACTS-16 dan 19 adalah volume besar (kelas e, ambang 100 baris); angka tersebut diwujudkan fixture BE (disediakan tim FE/BE). Perbandingan memakai nilai seed spec ini, bukan angka bersama.
- Asersi Last Updated (TC-AC-ACTS-18) membandingkan dengan waktu aktivitas unit lokal terbaru SKU Q yang dicatat lewat kemampuan baca BE (disediakan tim FE/BE) dengan toleransi satu menit; jam server dan jam browser sinkron.
- Distributor B dan Principal hanya sebagai pemilik data seed (tidak ada login); tidak ada sesi UI kedua.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-ACTS-16: Total Registered berisi stok lokal Distributor dengan header tetap

1. Ketik Search nama SKU P, tekan Enter
2. Verifikasi Header kolom `Total Registered` tetap bernama `Total Registered`
3. Verifikasi Angka Total Registered baris SKU P `54` (stok lokal Distributor A)
4. Verifikasi Total Principal 500 tidak tampil di baris SKU P
5. Klik teks Device Name baris SKU P untuk membuka Detail SKU, lalu lihat Summary bar
6. Verifikasi Label Summary bar `Total Registered` dengan angka `54`
7. Klik breadcrumb `Stock`

### TC-AC-ACTS-17: Available, Damaged/Missing, In Use di-scope ke unit sendiri

8. Ganti isi kotak search dengan nama SKU P, tekan Enter
9. Verifikasi Available `30` hanya dari batch registrasi Distributor A
10. Verifikasi Damaged/Missing `4` hanya dari batch registrasi Distributor A
11. Verifikasi In Use `20` hanya dari batch registrasi Distributor A

### TC-AC-ACTS-890: Available di-scope ke unit sendiri

12. Verifikasi Available `30` baris SKU P hanya dari batch registrasi Distributor A
13. Klik icon Filter, isi Available Min `30` dan Max `30`, klik `[Apply]`
14. Verifikasi Baris SKU P muncul pada hasil filter Min 30 Max 30
15. Klik icon Filter, klik `[Clear Field]`, klik `[Apply]`

### TC-AC-ACTS-18: Last Updated hanya dari unit lokal

16. Klik `(←)` pada kotak Search
17. Ketik Search `{runId}-005`, tekan Enter
18. Verifikasi Stock List memuat baris SKU Q dan SKU R
19. Catat waktu aktivitas unit lokal terbaru SKU Q lewat kemampuan baca BE
20. Verifikasi Last Updated SKU Q sama dengan waktu aktivitas yang dicatat pada langkah 19 (toleransi satu menit)
21. Verifikasi Last Updated SKU R `—`
22. Verifikasi Sort default memakai nilai Last Updated lokal tersebut (SKU Q berada di atas SKU R)

### TC-AC-ACTS-19: Distributor A tidak melihat stok Distributor B

23. Ganti isi kotak search dengan nama SKU P, tekan Enter, lalu klik teks Device Name baris SKU P untuk membuka Detail SKU Tab Available
24. Verifikasi Tab Available memuat sedikitnya satu unit milik Distributor A
25. Verifikasi Unit milik Distributor B tidak muncul di Tab Available
26. Klik tab `In Use`
27. Verifikasi Tab In Use memuat sedikitnya satu unit milik Distributor A
28. Verifikasi Unit milik Distributor B tidak muncul di Tab In Use
29. Verifikasi Angka milik Distributor B (50) tidak muncul di Detail SKU

## Notes

- TC-AC-ACTS-16 dan 19: volume Principal 500 unit dan Distributor B 50 unit (Distributor A 54 unit) diwujudkan fixture BE menurut ambang 100 baris kelas e; spec memakai seeding fixture BE dan tidak dipisah karena seluruh TC satu kelas harness (Distributor scope).
- Langkah penghubung (S-03): Search nama SKU seed untuk menemukan baris target (R-16); `[Clear Field]` dan `[Apply]` mengosongkan Filter sebelum TC berikutnya (S-09); breadcrumb `Stock` kembali ke Stock List.
- Temuan untuk QA (S-15): ACC TC-AC-ACTS-16 sampai 19 dan 890 menyebut Distributor Toggle ON dengan "Manage TAG stock, Local Registration aktif"; email akun mengikuti Pre-setup #9. Pre-setup #9 menulis "71 TC" sebagai jumlah penggunaan yang tidak cocok dengan hitungan aktual. TC-AC-ACTS-18 butir c ("Sort default memakai nilai lokal") tidak menyebut urutan yang diharapkan; spec mengasersi SKU Q di atas SKU R.
- Langkah penghubung tambahan (S-03, S-14, R-16): Search `{runId}-005` (langkah 17) sesudah `(←)` supaya baris SKU Q dan SKU R (SKU seed spec ini) tampil di halaman teramati, tidak bergantung pada posisi di ujung daftar; langkah Search berikutnya ditulis "ganti isi kotak search" karena kotak masih terisi (8b butir 9).
