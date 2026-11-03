---
id: TC-AC-ACAL-E2E-037-format-tanggal-dan-zona-waktu-general-settings-entitas-staf-login
title: "Format Tanggal dan Zona Waktu Mengikuti General Settings Entitas Staf Login"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-60
  - TC-AC-ACAL-135
  - TC-AC-ACAL-136
coverage:
  web: automated
---

# Format Tanggal dan Zona Waktu Mengikuti General Settings Entitas Staf Login

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Distributor Alfa `totalControlAdminConsoleDistributorAlfa_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 7, format email sama dengan akun lain), kredensial `Spectra.env.AC_ALFA_TC_PASSWORD` (nama env usulan tim FE yang belum terdaftar di `.env.example` maupun `spectra.config.ts`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture. Spec tidak mengganti akun.
- Guided Tooltip: hook `before`/`after` spec ini menyetel dan memulihkan flag seen untuk akun Distributor Alfa dan halaman Admin Console > Activity Log (kemampuan disediakan tim FE/BE).
- Hierarki entitas (Pre-setup No 8): Distributor Alfa memiliki Partner Beta; Partner Beta berada di jaringan Alfa sehingga barisnya tampil di Activity Log Alfa.
- State global yang diubah (General Settings entitas Distributor Alfa dan Partner Beta). Hook `before` mencatat nilai awal lalu menyetel:
  - Distributor Alfa: Date Format `dd/MM/yy`, Time Format 12-hour, Time Zone opsi berlabel `(UTC+07:00)` yang memuat Jakarta (tersimpan `Asia/Jakarta`). Nilai ini adalah Precondition TC-AC-ACAL-135 dan dipakai TC-AC-ACAL-60 (TC tidak menyebut Date Format dan Time Format-nya).
  - Partner Beta: Time Zone `Asia/Makassar` (Precondition TC-AC-ACAL-136).
  - Langkah 17 (Pemicu API) mengubah General Settings Alfa ke Date Format `dd MMM yy` dan Time Format 24-hour; nilai ini tetap berlaku untuk TC-AC-ACAL-136 (TC-AC-ACAL-136 tidak menyebut Time Format). Hook `after` memulihkan seluruh nilai awal Alfa dan Beta; langkah 31 (Pemicu API) memulihkannya juga sebagai aksi penghubung. Pemulihan menambah entri Edit General Settings pada audit trail dan mengubah Last Updated General Settings.
  - Kemampuan menyetel General Settings entitas lewat API disediakan tim FE/BE tanpa endpoint yang dikarang di spec ini.
- Data Dinamis (bersuffix `{runId}-037`), cap waktu seed dalam UTC (kemampuan seed BE entri log bercap waktu masa lalu disediakan tim FE/BE; baris log tidak dapat dihapus):
  - Tab Session entitas Alfa: user `Uji Zona {runId}-037`, event tersimpan `17 Jun 2026 18:30 UTC` (tampil `18 Jun 2026` pukul 01:30 pada zona Jakarta).
  - Tab User Action entitas Alfa: entri Name `Objek Zona {runId}-037`, tersimpan `17 Jun 2026 18:30 UTC`.
  - Tab Session entitas Partner Beta: user staf `Staf Beta {runId}-037`, event tersimpan `18 Jun 2026 09:00 UTC` (tampil `16:00` pada zona Jakarta milik staf login; `17:00` bila memakai zona Makassar milik Beta).
- Subjek dinamis `Uji Zona {runId}-037`, `Objek Zona {runId}-037`, dan `Staf Beta {runId}-037` hanya nama snapshot di dalam baris log seed; tidak ada akun yang dibuat dan tidak ada yang perlu dibersihkan (R-08), karena baris log tidak dapat dihapus.
- State yang diubah dan dipulihkan: Search dan Filter kedua tab (dibersihkan di langkah 4, 8, dan 30; klik menu Activity Log pada langkah 18 dan 27 mereset Search, Sort, dan Filter kedua tab). Suite serial (`parallel: false`).

## Test Steps

### TC-AC-ACAL-60: Filter Date dibandingkan dalam zona waktu tampilan General Settings

1. Pada tab Session, ketik Search `{runId}-037`, tekan Enter
2. Klik icon Filter, pilih rentang `18 Jun 2026` sampai `18 Jun 2026`, klik [Apply]
3. Verifikasi baris `Uji Zona {runId}-037` (tersimpan `17 Jun 2026 18:30 UTC`) tampil di tab Session
4. Klik icon Filter, klik [Clear Field], klik [Apply], lalu klik `(←)` pada kotak Search
5. Klik tab "User Action", ketik Search `{runId}-037`, tekan Enter
6. Klik icon Filter, pilih rentang `18 Jun 2026` sampai `18 Jun 2026`, klik [Apply]
7. Verifikasi baris `Objek Zona {runId}-037` (tersimpan `17 Jun 2026 18:30 UTC`) tampil di tab User Action
8. Klik icon Filter, klik [Clear Field], klik [Apply], lalu klik `(←)` pada kotak Search

### TC-AC-ACAL-135: Format Date, Time, dan Timezone milik entitas staf login pada tabel dan filter kedua tab

9. Klik tab "Session", ketik Search `{runId}-037`, tekan Enter
10. Verifikasi kolom Date baris `Uji Zona {runId}-037` tampil `18/06/26` dengan format `dd/MM/yy`
11. Verifikasi kolom Date baris `Uji Zona {runId}-037` menampilkan jam dalam notasi 12-hour pada zona Jakarta
12. Klik icon Filter, klik field Date, pilih tanggal `18 Jun 2026` lewat picker
13. Verifikasi input Date menampilkan `18/06/26`
14. Tutup Filter Panel tanpa [Apply] dengan klik icon Filter, klik tab "User Action", lalu ketik Search `{runId}-037`, tekan Enter
15. Verifikasi kolom Date baris `Objek Zona {runId}-037` tampil `18/06/26` dengan format `dd/MM/yy`
16. Verifikasi kolom Date baris `Objek Zona {runId}-037` menampilkan jam dalam notasi 12-hour pada zona Jakarta
17. Pemicu API: ubah General Settings Distributor Alfa ke Date Format `dd MMM yy` dan Time Format 24-hour hingga tersimpan
18. Klik menu Activity Log di sidebar (membuka tab Session)
19. Ketik Search `{runId}-037`, tekan Enter
20. Verifikasi kolom Date baris `Uji Zona {runId}-037` tab Session tampil `18 Jun 26` dengan format `dd MMM yy`
21. Verifikasi kolom Date baris `Uji Zona {runId}-037` tab Session menampilkan jam 24-hour `01:30`
22. Klik icon Filter, klik field Date, pilih tanggal `18 Jun 2026` lewat picker
23. Verifikasi input Date menampilkan `18 Jun 26`
24. Tutup Filter Panel tanpa [Apply] dengan klik icon Filter, klik tab "User Action", lalu ketik Search `{runId}-037`, tekan Enter
25. Verifikasi kolom Date baris `Objek Zona {runId}-037` tab User Action tampil `18 Jun 26` dengan format `dd MMM yy`
26. Verifikasi kolom Date baris `Objek Zona {runId}-037` tab User Action menampilkan jam 24-hour `01:30`

### TC-AC-ACAL-136: Zona waktu mengikuti entitas staf login, bukan entitas yang dilihat

27. Klik menu Activity Log di sidebar (membuka tab Session), ketik Search `{runId}-037`, tekan Enter
28. Verifikasi kolom Date baris sesi staf Partner Beta `Staf Beta {runId}-037` (event `09:00 UTC`) tampil dengan jam `16:00` (zona Jakarta)
29. Verifikasi kolom Date baris `Staf Beta {runId}-037` tidak tampil dengan jam `17:00` (zona Makassar)
30. Klik `(←)` pada kotak Search
31. Pemicu API: pulihkan General Settings Distributor Alfa dan Partner Beta ke nilai awal yang dicatat hook `before` hingga tersimpan

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md`. Urutan TC dalam spec: 60, 135, 136 (TC-AC-ACAL-136 sesudah TC-AC-ACAL-135 karena memakai Time Format 24-hour yang diatur pada langkah 17). Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1, 5, 9, 14, 19, 24, dan 27 (Search `{runId}-037` menyempitkan tabel ke baris seed milik spec; klik menu Activity Log mereset Search, Sort, dan Filter), langkah 4, 8, dan 30 (pemulihan Filter dan Search, S-09), langkah 14 dan 24 (menutup Filter Panel tanpa [Apply], pindah ke tab "User Action", dan mengetik Search `{runId}-037`), langkah 18 (klik menu Activity Log setelah General Settings tersimpan), serta Pemicu API pada langkah 17 (ubah General Settings Alfa; TC tidak menyebut mekanismenya) dan langkah 31 (pemulihan General Settings).
- Langkah 3 dan 7 mengasersi bahwa entri tersimpan `17 Jun 2026 18:30 UTC` tampil pada filter `18 Jun 2026`, yaitu dibandingkan dalam zona waktu tampilan (`18 Jun 2026` pukul 01:30), bukan sebagai `17 Jun` UTC; dasarnya Expected a dan b TC-AC-ACAL-60.
- Langkah 29 (tidak tampil `17:00`) memakai langkah 28 (baris yang sama tampil `16:00`) sebagai anchor positif.
- Asersi jam 24-hour pada langkah 21 dan 26 memakai `01:30`, diturunkan dari event `17 Jun 2026 18:30 UTC` pada zona Jakarta (UTC+07:00); asersi jam 12-hour (langkah 11 dan 16) hanya notasi karena TC tidak menyebut string persisnya.
- Temuan untuk QA:
  - TC-AC-ACAL-60 tidak menyebut Date Format dan Time Format Alfa; spec memakai Precondition TC-AC-ACAL-135 (`dd/MM/yy`, 12-hour).
  - TC-AC-ACAL-135 tidak menyebut cap waktu entri seed dan string persis jam 12-hour (penanda AM/PM dan pemisah); spec hanya mengasersi bagian tanggal (`18/06/26`, `18 Jun 26`) dan notasi jam sebagai format, tanpa string jam persis.
  - TC-AC-ACAL-135 langkah 4 tidak menyebut jalur mengubah General Settings Alfa; akun Total Control Admin Console belum tentu memiliki akses Global Settings, sehingga spec meminta kemampuan menyetelnya dari tim FE/BE.
  - TC-AC-ACAL-136 tidak menyebut tanggal event `09:00 UTC` dan tidak menyebut Time Format; spec memakai `18 Jun 2026` dan 24-hour sisa langkah 17 supaya `16:00` terbaca.
  - Email akun Distributor Alfa memakai placeholder `{namaCompany}` dan password memakai `AC_ALFA_TC_PASSWORD` (nama usulan tim FE dan belum terdaftar di `.env.example` maupun `spectra.config.ts`); nilai disediakan tim FE.
  - Post Condition ketiga TC bernilai `-`; tidak diasersi.
