---
id: TC-GS-TAG-E2E-097-format-tanggal-waktu-dan-timezone-general-settings-lintas-surface
title: "Format Tanggal, Waktu, dan Timezone General Settings: Tabel Registri, Filter Panel, Event Log, dan TAG Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-309
  - TC-GS-TAG-310
  - TC-GS-TAG-311
  - TC-GS-TAG-312
coverage:
  web: automated
---

# Format Tanggal, Waktu, dan Timezone General Settings: Tabel Registri, Filter Panel, Event Log, dan TAG Log

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control Client A Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup TC); kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before` (akun default suite), sehingga hook `after` tidak mengganti sesi. Akun yang sama mengubah General Settings (TC tidak menyebut akun pelaku perubahan General Settings; Total Control dipakai sebagai akun yang berwenang, lihat Temuan untuk QA).
- Flag Guided Tooltip `gs-tag-registry` dan `gs-tag-activate` mengikuti hook suite `before` dan `after` (lihat `suite.md`, bagian Hook Guided Tooltip).
- Suite serial (`parallel: false`) karena spec mengubah state global General Settings Client A.
- Tanggal sistem lingkungan run lebih besar dari 16/09/26; rentang Filter Date seed `16/09/26` sampai `16/09/26` (satu hari, baris `E-01`) berlaku.
- State global yang diubah: General Settings Client A, yaitu Date Format, Time Format, dan Time Zone. Hook `before` mencatat nilai awal lalu menyetel Date Format `dd/MM/yy`, Time Format 24-hour, dan Time Zone `Asia/Jakarta` (precondition TC-312 dan default Client A pada Catatan TC; mekanisme penyetelan lewat API disediakan tim FE). Hook `after` memulihkan nilai awal walau spec gagal di tengah. Konfigurasi kolom `Activated At` (Setup Column, state browser) dipulihkan di hook `after` ke Hidden.
- Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- Data Pre-setup Client A (dibaca saja, tanpa aksi tulis; lewat fixture BE, mekanisme disediakan tim FE/BE, lihat Temuan untuk QA):
  - Seed Registri A: DD-01 `E2801160600002054D8A0001` dengan Last Scanned 16/09/26 14:30 (Asia/Jakarta); TAG Log DD-01 memuat entri `Paired` 16/09/26 14:30 oleh Budi Santoso.
  - Seed Event Log: `E-01` (16/09/26 14:30, RFID, Activate, Success 22, Waiting for Approval 2, Failed 1, Hardware `Zebra RFD40 (SN-2201)`, PIC `Budi S`).
- Event Log menumpuk antar spec; baris `E-01` diidentifikasi dengan Filter Date satu hari 16/09/26 (hanya `E-01` yang bertanggal 16/09/26 pada Tab Activate TAG).
- Kemampuan teknis: mengubah Date Format, Time Format, dan Time Zone Client A di General Settings (UI pada langkah 1, 10, 11, dan 27; label kontrol disediakan tim FE); memilih tanggal pada date range picker; jam server dan jam browser tidak digeser (tidak ada langkah berbasis waktu nyata).

## Test Steps

### TC-GS-TAG-312: Timezone General Settings diterapkan pada seluruh timestamp modul

1. Buka Global Settings > General Settings, ubah Time Zone Client A dari `Asia/Jakarta` ke `Asia/Makassar`, lalu simpan
2. Tunggu aksi selesai
3. Buka Global Settings > TAG, Tab All, ketik Search `E2801160600002054D8A0001`, tekan Enter
4. Verifikasi Last Scanned baris DD-01 `16/09/26 15:30` (bergeser +1 jam)
5. Klik tombol `Event Log`, klik Filter, pilih Date `16/09/26` sampai `16/09/26`, klik `[Apply]`, lalu tutup Filter Panel dengan klik Filter
6. Verifikasi Date baris `E-01` `16/09/26 15:30`
7. Tutup modal lewat `✕`, buka menu baris DD-01, klik `TAG Log`
8. Verifikasi Date & Time entri `Paired` pada TAG Log DD-01 `16/09/26 15:30`
9. Tutup popup lewat `[✕]`
10. Buka Global Settings > General Settings, kembalikan Time Zone Client A ke `Asia/Jakarta`, lalu simpan

### TC-GS-TAG-309: Format tanggal dan waktu General Settings di tabel registri dan Filter Panel

11. Ubah Date Format Client A menjadi `M/d/yy` dan Time Format menjadi 12-hour di General Settings, lalu simpan
12. Tunggu aksi selesai
13. Buka Global Settings > TAG, Tab All, buka Setup Column lewat ikon (⋯) di header kolom Actions dan item `Setup Column...`, centang kolom `Activated At`, lalu klik `Save`
14. Ketik Search `E2801160600002054D8A0001`, tekan Enter
15. Verifikasi Last Scanned baris DD-01 `9/16/26 02:30 PM` (tanggal `9/16/26`, jam 12-hour `02:30 PM`)
16. Klik Filter, pilih `Last Scanned` tanggal `9/16/26` sampai `9/16/26`
17. Verifikasi isi input date range Last Scanned di Filter Panel memakai format `M/d/yy` (`9/16/26`)
18. Tutup Filter Panel dengan klik Filter

### TC-GS-TAG-310: Format tanggal dan waktu di Event Log dan Filter Date Event Log

19. Klik tombol `Event Log`, klik Filter, pilih `Date` `9/16/26` sampai `9/16/26`
20. Verifikasi isi input date filter Event Log memakai format yang sama (`9/16/26`)
21. Klik `[Apply]`, lalu tutup Filter Panel dengan klik Filter
22. Verifikasi kolom Date baris `E-01` tampil `9/16/26` dan `02:30 PM`
23. Tutup modal lewat `✕`

### TC-GS-TAG-311: Format tanggal dan waktu pada Date & Time entri TAG Log

24. Buka menu baris DD-01, klik `TAG Log`
25. Verifikasi Date & Time entri `Paired` pada TAG Log DD-01 tampil `9/16/26` dan `02:30 PM`
26. Tutup popup lewat `[✕]`
27. Pulihkan General Settings Client A ke Date Format `dd/MM/yy` dan Time Format 24-hour, lalu simpan
28. Sembunyikan kembali kolom `Activated At` lewat Setup Column, lalu klik `Save`

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular. Kelas h (state global General Settings); keempat TC berbagi satu topik (format tanggal, waktu, dan timezone), akun, dan state global yang sama, sehingga satu spec sesuai plan.
- Urutan TC dalam spec: 312, 309, 310, 311 (bukan urutan sumber). TC-312 memerlukan format default `dd/MM/yy` 24-hour (nilai `15:30` pada Expected 24-hour) dan TC-309 sampai TC-311 memerlukan Time Zone `Asia/Jakarta` dengan `M/d/yy` 12-hour; menjalankan TC-312 lebih dulu dan memulihkan Time Zone (langkah 10) sebelum mengubah format menghindari dua perubahan state yang bertabrakan. Perubahan urutan dicatat sesuai S-05.
- Langkah 22 dibaca setelah Filter Date (langkah 19 sampai 21) karena baris `E-01` tidak dijamin berada di halaman 1 saat Event Log menumpuk (S-12); dengan demikian Filter Date satu hari dipakai pada kedua surface sebagai langkah penghubung.
- Langkah penghubung (tanpa `Verifikasi`, tidak ada di TC): langkah 2 dan 12 (Tunggu aksi selesai, bagian 8b butir 8), langkah 3, 14 (Search agar baris target tampil), langkah 5 dan 19 (Filter Date satu hari agar `E-01` tampil), langkah 7, 9, 23, 26 (menutup modal dan popup), langkah 10, 27, 28 (pemulihan state; hook `after` sebagai cadangan), langkah 13 (precondition TC-309 "kolom Activated At ditampilkan"), langkah 1 dan 11 (precondition TC yang diubah lewat UI General Settings).
- Temuan untuk QA:
  - TC-312 menyebut Time Zone diubah tanpa menyebut akun pelaku dan tidak menyebut format tampil jam (24-hour) pada Expected `15:30`; spec menjalankan TC-312 pada format default `dd/MM/yy` 24-hour (Q-12). Zona tujuan `Asia/Makassar` dari precondition TC; pelaku disediakan tim FE.
  - TC-309 langkah 1 meminta mengamati Activated At DD-01 tetapi Expected tidak menyebut nilai Activated At (Seed Registri A: 10/09/26 08:00); spec tidak mengasersi Activated At.
  - TC-309 dan TC-310 mengubah format di General Settings Client A; format tidak dinyatakan literalnya selain `M/d/yy` dan 12-hour (pola Time Format `hh:mm a`, tidak dinyatakan di TC); kontrol General Settings disediakan tim FE.
  - TC-309 Expected b ("input date range di Filter Panel memakai format `M/d/yy`") tidak menyebut nilai yang dipilih; spec memilih `9/16/26` dan mengasersi isi input.
  - TC-311 mensyaratkan entri TAG Log DD-01 bertanggal 16 Sep 2026 14:30; entri itu adalah `Paired` pada fixture TAG Log DD-01 (Tabel Data Uji Dinamis).
  - Seeding dan reset Seed Registri A, Seed Event Log, dan fixture TAG Log antar spec tidak didefinisikan di TC (Q-4).
