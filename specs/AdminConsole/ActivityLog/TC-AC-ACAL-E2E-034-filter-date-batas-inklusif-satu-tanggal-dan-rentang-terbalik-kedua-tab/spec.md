---
id: TC-AC-ACAL-E2E-034-filter-date-batas-inklusif-satu-tanggal-dan-rentang-terbalik-kedua-tab
title: "Filter Date: Batas Inklusif, Satu Tanggal, dan Rentang Terbalik Kedua Tab"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACAL-59
  - TC-AC-ACAL-61
  - TC-AC-ACAL-62
  - TC-AC-ACAL-63
  - TC-AC-ACAL-99
coverage:
  web: automated
---

# Filter Date: Batas Inklusif, Satu Tanggal, dan Rentang Terbalik Kedua Tab

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Principal) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture. Spec tidak mengganti akun.
- Guided Tooltip: hook suite `before`/`after` menyetel flag seen (lihat suite.md).
- Data Dinamis (bersuffix `{runId}-034`), cap waktu seed dalam zona waktu tampilan General Settings entitas akun aktor (General Settings tidak diubah spec ini). Kolom Date berketelitian menit sehingga detik tidak tampil; baris dikenali dari tanggal dan jam pada kolom Date:
  - Tab Session, user `Uji Tanggal {runId}-034` (Position, Division, dan Employee ID bebas):
    - S1 seed `17 Jun 2026, 23:59:59`.
    - S2 seed `18 Jun 2026, 00:00:00`.
    - S3 seed `19 Jun 2026, 23:59:59`.
    - S4 seed `20 Jun 2026, 00:00:00`.
    - S5 seed `25 Jun 2026` (jam bebas).
  - Tab User Action, Name `Objek Tanggal {runId}-034` (Action dan Object bebas, satu nilai yang sama untuk keempat baris):
    - U1 seed `17 Jun 2026, 23:59:59`.
    - U2 seed `18 Jun 2026, 00:00:00`.
    - U3 seed `18 Jun 2026, 23:59:59`.
    - U4 seed `19 Jun 2026, 00:00:00`.
  - Himpunan S1 sampai S5 dipakai TC-AC-ACAL-59 dan TC-AC-ACAL-62 (TC-AC-ACAL-62 menyebut entri `17 Jun`, `18 Jun`, dan `25 Jun`; S3 ikut tersaring oleh rentang satu hari dan S4 tidak diasersi pada TC itu).
- Subjek dinamis `Uji Tanggal {runId}-034` dan Name `Objek Tanggal {runId}-034` hanya nama snapshot di dalam baris log seed; tidak ada akun yang dibuat dan tidak ada yang perlu dibersihkan (R-08), karena baris log tidak dapat dihapus.
- Kemampuan teknis (disediakan tim FE/BE): seed BE entri Session dan User Action dengan cap waktu masa lalu di atas, karena baris log bertanggal 17 sampai 25 Jun 2026 tidak dapat dihasilkan lewat aksi nyata modul sumber. Baris log tidak dapat dihapus (append-only); seed bersuffix run sehingga run berikutnya tidak bentrok.
- State yang diubah dan dipulihkan: Search dan Filter kedua tab (dibersihkan di langkah 18, 21, dan 29). Suite serial (`parallel: false`).

## Test Steps

### TC-AC-ACAL-61: Tanggal akhir sebelum tanggal mulai tidak dapat dipilih, kedua tab

1. Klik icon Filter pada tab Session, klik field Date, pilih tanggal mulai `18 Jun 2026`, lalu coba pilih tanggal akhir `17 Jun 2026`
2. Verifikasi tanggal sebelum `18 Jun 2026` disabled di picker dan tidak dapat dipilih sebagai tanggal akhir di tab Session
3. Tutup Filter Panel tanpa [Apply] dengan klik icon Filter, lalu klik tab "User Action"
4. Klik icon Filter, klik field Date, pilih tanggal mulai `18 Jun 2026`, lalu coba pilih tanggal akhir `17 Jun 2026`
5. Verifikasi tanggal sebelum `18 Jun 2026` disabled di picker dan tidak dapat dipilih sebagai tanggal akhir di tab User Action
6. Tutup Filter Panel tanpa [Apply] dengan klik icon Filter

### TC-AC-ACAL-59: Filter Date rentang inklusif kedua ujung, tab Session

7. Klik tab "Session", ketik Search `{runId}-034`, tekan Enter
8. Klik icon Filter, pilih rentang `18 Jun 2026` sampai `19 Jun 2026`, klik [Apply]
9. Verifikasi baris S2 (`18 Jun 2026, 00:00`) dan S3 (`19 Jun 2026, 23:59`) tampil di tab Session
10. Verifikasi baris S1 (`17 Jun 2026, 23:59`) dan S4 (`20 Jun 2026, 00:00`) tidak tampil di tab Session
11. Klik icon Filter, ubah rentang menjadi `18 Jun 2026` sampai `18 Jun 2026`, klik [Apply]
12. Verifikasi hanya baris S2 (`18 Jun 2026, 00:00`) yang tampil di tab Session

### TC-AC-ACAL-62: Filter Date satu tanggal menjadi rentang satu hari, tab Session

13. Klik icon Filter, klik [Clear Field], klik satu tanggal `18 Jun 2026` di picker, klik [Apply]
14. Verifikasi baris S2 (`18 Jun 2026, 00:00`) tampil di tab Session
15. Verifikasi baris S1 (`17 Jun 2026`), S3 (`19 Jun 2026`), dan S5 (`25 Jun 2026`) tidak tampil di tab Session

### TC-AC-ACAL-63: Field Date satu date range picker tanpa input tanggal akhir terpisah, kedua tab

16. Klik icon Filter
17. Verifikasi Filter Panel tab Session hanya memiliki satu field Date (date range picker) tanpa input tanggal akhir terpisah
18. Klik [Clear Field], klik [Apply], lalu klik `(←)` pada kotak Search
19. Klik tab "User Action", klik icon Filter
20. Verifikasi Filter Panel tab User Action hanya memiliki satu field Date (date range picker) tanpa input tanggal akhir terpisah
21. Klik [Clear Field], klik [Apply]

### TC-AC-ACAL-99: Filter Date rentang inklusif dan satu tanggal, tab User Action

22. Ketik Search `{runId}-034`, tekan Enter
23. Klik icon Filter, pilih rentang `18 Jun 2026` sampai `18 Jun 2026`, klik [Apply]
24. Verifikasi baris U2 (`18 Jun 2026, 00:00`) dan U3 (`18 Jun 2026, 23:59`) tampil di tab User Action
25. Verifikasi baris U1 (`17 Jun 2026, 23:59`) dan U4 (`19 Jun 2026, 00:00`) tidak tampil di tab User Action
26. Klik icon Filter, klik [Clear Field], klik satu tanggal `18 Jun 2026` di picker, klik [Apply]
27. Verifikasi baris U2 dan U3 (`18 Jun 2026`) tampil di tab User Action
28. Verifikasi baris U1 (`17 Jun 2026`) dan U4 (`19 Jun 2026`) tidak tampil di tab User Action
29. Klik icon Filter, klik [Clear Field], klik [Apply], lalu klik `(←)` pada kotak Search

## Notes

- Sumber: `admin-console/activity-log/TestCases/tc-activity-log.md`. Urutan TC dalam spec: 61, 59, 62, 63, 99 (kasus picker yang tidak mengubah tabel lebih dulu, lalu tab Session, lalu tab User Action). Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 3 dan 6 (menutup Filter Panel tanpa [Apply]; perubahan yang belum di-Apply dibuang menurut `prd-conventions.md` §9.8), langkah 7 dan 22 (Search `{runId}-034` menyempitkan tabel ke baris seed milik spec, supaya asersi tidak bercampur dengan baris lain; Search dipertahankan sampai langkah 18 dan 29), langkah 11, 13, dan 26 (mengganti rentang atau tanggal), langkah 16 dan 19 (membuka Filter Panel, pindah tab), langkah 18, 21, dan 29 (pemulihan Filter dan Search kedua tab, S-09).
- Asersi absence (langkah 10, 15, 25, 28) didahului `Verifikasi` baris lain pada tabel yang sama yang tampil (langkah 9, 14, 24, 27), sehingga hasil kosong bukan karena tabel belum dimuat.
- Langkah 12 mengasersi "hanya" satu baris: baris S2 tampil dan tidak ada baris lain di tabel yang sudah disempitkan Search.
- Stempel waktu batas `00:00:00` dan `23:59:59` hanya ada pada data seed; tampilan kolom Date tanpa detik.
- Temuan untuk QA:
  - TC-AC-ACAL-59, 62, 99 menyebut entri dengan tanggal dan jam tetapi tidak menyebut cara membuat entri bertanggal masa lalu dan tidak menyebut Date Format, Time Format, atau Time Zone; spec memakai General Settings entitas aktor apa adanya dan meminta seed BE (S-13).
  - TC-AC-ACAL-62 menyebut entri `17 Jun`, `18 Jun`, `25 Jun` tanpa jam; spec memakai himpunan S1 sampai S5 yang sama dengan TC-AC-ACAL-59 dan jam bebas untuk S5.
  - TC-AC-ACAL-61 tidak menyebut apakah tanggal mulai dipilih lebih dulu atau tanggal akhir ditolak oleh picker pada klik pertama; spec mengikuti urutan Langkah Uji TC.
  - Apakah [Apply] menutup Filter Panel belum ditetapkan PRD dan TC; langkah "klik icon Filter" sesudah [Apply] mengikuti pola TC.
  - Post Condition kelima TC bernilai `-`; tidak diasersi.
  - `caseType` Edge mengikuti alur dominan spec (batas inklusif); TC-AC-ACAL-61 sendiri bertipe Negative.
