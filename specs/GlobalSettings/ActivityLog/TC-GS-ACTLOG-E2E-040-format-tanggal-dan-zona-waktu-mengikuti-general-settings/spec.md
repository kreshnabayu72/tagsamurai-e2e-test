---
id: TC-GS-ACTLOG-E2E-040-format-tanggal-dan-zona-waktu-mengikuti-general-settings
title: "Format Tanggal dan Zona Waktu Mengikuti General Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-ACTLOG-75
  - TC-GS-ACTLOG-191
  - TC-GS-ACTLOG-192
  - TC-GS-ACTLOG-193
  - TC-GS-ACTLOG-194
coverage:
  web: automated
---

# Format Tanggal dan Zona Waktu Mengikuti General Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net` (kredensial `Spectra.env.GS_TC_PASSWORD`). Login sekali di hook `before`; hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Data Dinamis (bersuffix `{runId}-040`): satu entri Session untuk user `John Doe {runId}-040` dan satu entri User Action dengan Name `Acme Corp {runId}-040`, keduanya tersimpan UTC `14 Jul 2026, 17:30`.
- Kemampuan teknis (disediakan tim FE/BE): seed BE kedua entri dengan timestamp UTC di atas; baris log bertanggal masa lalu tidak dapat dihasilkan lewat aksi nyata modul sumber. Tab browser kedua pada sesi yang sama untuk mengubah General Settings pada TC-GS-ACTLOG-194.
- General Settings: Time Zone, Date Format, dan Time Format diubah spec lewat Global Settings > General Settings pada tiap blok. Hook `before` mencatat nilai awal ketiganya lalu menyetel keadaan awal blok TC-GS-ACTLOG-75 (Precondition TC): Date Format `dd MMM yy`, Time Format `HH:mm`, dan Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`, sehingga entri tampil `15 Jul 26, 00:30`. Hook `after` memulihkan ketiga nilai awal.
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Guided Tooltip: hook before/after spec ini menyetel dan memulihkan flag seen untuk akun Total Control Client A (Sari Dewi) dan halaman Global Settings > General Settings (kemampuan disediakan tim FE/BE).
- State global yang diubah: Time Zone, Date Format, dan Time Format di General Settings (dipulihkan seperti di atas); tiap perubahan menambah entri Edit General Settings di User Action dan mengubah Last Updated General Settings. Suite berjalan serial (`parallel: false`). Entri log tidak dapat dihapus (ACTLOG-LOGIC-01); seed memakai nama bersufiks run sehingga run berikutnya tidak bentrok, dan asersi tahan terhadap baris dari run lain.

## Test Steps

### TC-GS-ACTLOG-75: Filter Date dibandingkan dalam zona waktu tampilan General Settings

1. Buka Global Settings > Activity Log > Tab "Session", ketik Search `{runId}-040`, tekan Enter
2. Klik icon Filter, pilih Date `15 Jul 2026` sampai `15 Jul 2026`, klik [Apply]
3. Verifikasi entri berstempel UTC `14 Jul 2026, 17:30` tampil di Tab Session
4. Verifikasi tampilan Date entri itu di Tab Session `15 Jul 26, 00:30`
5. Klik icon Filter, ubah rentang menjadi `14 Jul 2026` sampai `14 Jul 2026`, klik [Apply]
6. Verifikasi ilustrasi `"No results found"` tampil di Tab Session
7. Verifikasi entri itu tidak tampil di Tab Session
8. Klik tab "User Action", ketik Search `{runId}-040`, tekan Enter
9. Klik icon Filter, pilih Date `15 Jul 2026` sampai `15 Jul 2026`, klik [Apply]
10. Verifikasi entri berstempel UTC `14 Jul 2026, 17:30` tampil di Tab User Action
11. Verifikasi tampilan Date entri itu di Tab User Action `15 Jul 26, 00:30`
12. Klik icon Filter, ubah rentang menjadi `14 Jul 2026` sampai `14 Jul 2026`, klik [Apply]
13. Verifikasi ilustrasi `"No results found"` tampil di Tab User Action
14. Verifikasi entri itu tidak tampil di Tab User Action

### Pemulihan state antar TC

15. Pada Tab User Action klik icon Filter, klik [Clear Field], klik [Apply]; klik tab "Session", klik icon Filter, klik [Clear Field], klik [Apply]

### TC-GS-ACTLOG-191: Timestamp kolom Date mengikuti Date Format DD/MM/YY, 24 jam, UTC+07:00

16. Di Global Settings > General Settings atur Date Format `DD/MM/YY`, Time Format `HH:mm`, Time Zone `(UTC+07:00) Bangkok, Hanoi, Jakarta`, lalu klik [Save]
17. Tunggu aksi selesai: tombol [Save] menjadi Disabled (form Unchanged setelah Save sukses)
18. Klik menu Activity Log di sidebar, klik tab "Session", ketik Search `{runId}-040`, tekan Enter
19. Verifikasi sel Date entri uji di Tab Session memuat tanggal `15/07/26` dan jam `00:30`
20. Klik tab "User Action", ketik Search `{runId}-040`, tekan Enter
21. Verifikasi sel Date entri uji di Tab User Action memuat tanggal `15/07/26` dan jam `00:30`

### TC-GS-ACTLOG-193: Teks tanggal di field Date Filter Panel mengikuti Date Format

22. Klik tab "Session", klik icon Filter, pilih tanggal `14 Jul 2026` sebagai awal dan akhir pada field Date
23. Verifikasi teks field Date Tab Session memuat `14/07/26`
24. Tutup Filter Panel tanpa [Apply], klik tab "User Action", klik icon Filter, pilih tanggal `14 Jul 2026` sebagai awal dan akhir pada field Date
25. Verifikasi teks field Date Tab User Action memuat `14/07/26`

### Pemulihan state antar TC

26. Tutup Filter Panel tanpa [Apply]

### TC-GS-ACTLOG-194: Perubahan format di General Settings langsung terlihat di Activity Log

27. Klik tab "Session", lalu catat sel Date entri uji (kotak Search Tab Session masih berisi `{runId}-040`)
28. Verifikasi sebelum perubahan sel Date entri uji memuat `15/07/26` dan `00:30`
29. Di tab browser lain, buka Global Settings > General Settings, ubah Date Format menjadi `DD MMM YY` dan Time Format menjadi `hh:mm a`, lalu klik [Save]
30. Tunggu aksi selesai di tab browser lain: tombol [Save] menjadi Disabled (form Unchanged setelah Save sukses)
31. Kembali ke tab Activity Log, muat ulang halaman (kotak Search Tab Session tetap terisi `{runId}-040`)
32. Verifikasi setelah perubahan dan muat ulang sel Date entri yang sama memuat `15 Jul 26` dan `12:30 AM`

### Pemulihan state antar TC

33. Tutup tab browser lain

### TC-GS-ACTLOG-192: Timestamp kolom Date mengikuti Date Format DD MMM YY, 12 jam, UTC+08:00

34. Di Global Settings > General Settings atur Date Format `DD MMM YY`, Time Format `hh:mm a`, Time Zone `(UTC+08:00) Kuala Lumpur, Singapore, Makassar`, lalu klik [Save]
35. Tunggu aksi selesai: tombol [Save] menjadi Disabled (form Unchanged setelah Save sukses)
36. Klik menu Activity Log di sidebar, klik tab "Session", ketik Search `{runId}-040`, tekan Enter
37. Verifikasi sel Date entri uji di Tab Session memuat tanggal `15 Jul 26` dan jam `01:30 AM`
38. Klik tab "User Action", ketik Search `{runId}-040`, tekan Enter
39. Verifikasi sel Date entri uji di Tab User Action memuat tanggal `15 Jul 26` dan jam `01:30 AM`

### Pemulihan state akhir

40. Klik menu Activity Log di sidebar sehingga kedua tab kembali ke default

## Notes

- Sumber TC: `global-settings/activity-log/TestCases/tc-activity-log.md`.
- Urutan TC: TC-GS-ACTLOG-75, 191, 193, 194, lalu 192. TC-GS-ACTLOG-194 dijalankan sebelum TC-GS-ACTLOG-192 karena TC-GS-ACTLOG-194 berakhir pada Date Format `DD MMM YY` dan Time Format `hh:mm a` di UTC+07:00, sehingga TC-GS-ACTLOG-192 hanya mengubah Time Zone dan menghemat satu perubahan format.
- Subjudul `###` memetakan langkah ke id TC untuk report per langkah.
- Spec di atas smell 35 langkah (40 langkah nominal, tanpa perulangan). Alasan: kelima blok berada pada satu topik (tampilan Date mengikuti General Settings) dengan dua entri seed yang sama, dan tiap blok menyetel format sendiri sehingga berdiri sendiri; kegagalan satu blok tidak menghilangkan makna blok lain.
- Langkah penghubung tanpa awalan `Verifikasi`: langkah 1, 8, 18, 20, 36, dan 38 (Search `{runId}-040` menyempitkan tabel ke entri seed milik spec; Search diketik sekali per tab sesudah klik menu sidebar atau pada tab yang kotaknya kosong), langkah 16 dan 34 (menyetel General Settings sesuai Precondition TC), langkah 17, 30, dan 35 (menunggu [Save] selesai, ditandai tombol [Save] menjadi Disabled sesuai PRD General Settings S-07, sebelum berpindah halaman atau tab), langkah 27 dan 31 (memakai Search yang bertahan pada tab Session dan sesudah muat ulang), langkah 29, serta langkah pemulihan 15, 26, 33, dan 40.
- Asersi tambahan di luar Expected TC: langkah 6 dan 13 (ilustrasi `"No results found"`, PRD §7 S-03) sebagai anchor positif bahwa tabel sudah termuat sebelum asersi absence langkah 7 dan 14 (S-03).
- P-2: tab browser lain pada langkah 29 hanya berfungsi sebagai pemicu perubahan General Settings (TC-GS-ACTLOG-194) dan bukan objek asersi; asersi dilakukan di tab Activity Log setelah muat ulang.
- TC-GS-ACTLOG-74 (batas inklusif Date) ada di spec 039.
- Activity Log dibuka kembali lewat menu sidebar (state default) sesudah mengunjungi General Settings, dan Search diketik ulang.
- Temuan untuk QA:
  - State kotak Search saat user keluar dari halaman Activity Log lalu kembali belum ditetapkan PRD; spec tidak mengandalkannya.
  - Apakah [Apply] menutup Filter Panel atau panel tetap terbuka belum ditetapkan PRD dan TC; langkah "klik icon Filter" sesudah [Apply] (langkah 5, 12, 15) mengikuti pola TC.
  - Token Date Format di TC-191 sampai TC-194 ditulis huruf besar (`DD/MM/YY`, `DD MMM YY`), sedangkan token opsi PRD General Settings §4.3b huruf kecil (`dd/MM/yy`, `dd MMM yy`) dan TC-74/75 memakai huruf kecil; spec mengikuti TC apa adanya, dan pemilik TC perlu menyeragamkan token. Pemilihan opsi di dropdown memakai label yang tampil.
  - Konvensi 8b.8 mencontohkan penanda selesai "tombol aktif kembali"; contoh itu tidak berlaku untuk form single-record General Settings karena [Save] menjadi Disabled setelah Save sukses (PRD General Settings S-04, S-07); spec memakai tombol Disabled sebagai penanda (pemilik: konvensi).
  - TC-191, 192, dan 194 tidak menyebut cara menyimpan perubahan General Settings; spec menulis klik [Save].
  - Judul TC-194 menyebut "tanpa muat ulang berkas", sedangkan Langkah 3 TC menuntut muat ulang halaman; spec mengikuti langkah dan Expected TC (dengan muat ulang).
  - Post Condition semua TC bernilai `-`; tidak diasersi.
