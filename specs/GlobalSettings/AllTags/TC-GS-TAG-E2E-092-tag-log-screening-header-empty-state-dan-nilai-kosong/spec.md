---
id: TC-GS-TAG-E2E-092-tag-log-screening-header-empty-state-dan-nilai-kosong
title: "Popup TAG Log: Screening Header dan Daftar Kronologis, Empty State S-05, dan Header Nilai Kosong"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-274
  - TC-GS-TAG-275
  - TC-GS-TAG-276
coverage:
  web: automated
---

# Popup TAG Log: Screening Header dan Daftar Kronologis, Empty State S-05, dan Header Nilai Kosong

## Prerequisites

- Mode: FE+BE.
- Akun aktor utama: Total Control Client A Sari Dewi `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup TC); kredensial `Spectra.env.GS_TC_PASSWORD` (terdaftar di `.env.example`; password tidak ditulis di spec atau fixture). Login sekali di hook `before` (akun default suite), sehingga hook `after` mengembalikan sesi ke akun ini.
- Akun kedua (langkah 27 sampai 28, TC-275): Total Control Client Log Wulan Sari `totalControl_automated_qaLog@qwertysystem.net`; kredensial `Spectra.env.GS_TC_LOG_PASSWORD` (belum terdaftar di `.env.example` dan `spectra.config.ts`; perlu didaftarkan pemilik repositori, tanpa nilai).
- Flag Guided Tooltip `gs-tag-registry` dan `gs-tag-activate` untuk kedua akun mengikuti hook suite `before` dan `after` (lihat `suite.md`, bagian Hook Guided Tooltip).
- Suite serial (`parallel: false`). Hook `beforeEach`: buka Global Settings > TAG, Tab All.
- Data Pre-setup (dibaca saja, tanpa aksi tulis; seeding lewat fixture BE, mekanisme disediakan tim FE/BE, lihat Temuan untuk QA):
  - Client A, Seed Registri A: DD-01 `E2801160600002054D8A0001` (RFID, Official, Object TAG, Paired; Device Name `Handheld Scanner X1`, SKU `SKU-8821`, Brand `Zebra`, Model/Type `ZT410`) dengan tiga entri TAG Log fixture: `Activated` (10/09/26 08:00, Budi Santoso), `Reserved` (15/09/26 10:00, Siti Amalia; Asset `Handheld Scanner X1`, Asset Code `AST-0001`), dan `Paired` (16/09/26 14:30, Budi Santoso; Type `Asset`); DD-05 `TAG-QR-00512` (QR, Official, Paired; Device Name, SKU, Brand, Model/Type kosong) tanpa entri TAG Log.
  - Client Log: DD-56 `E2801160600002054D8C0056` (RFID Object, Available) tanpa entri TAG Log (disisipkan fixture).
- Format tanggal General Settings Client A default `dd/MM/yy`, 24-hour.
- Kemampuan teknis: mengarahkan kursor ke nama pelaku untuk membaca tooltip; mempersempit viewport sehingga daftar TAG Log dapat di-scroll (langkah 15); mengganti akun (Logout lalu login) di tengah spec.
- State global yang diubah: tidak ada selain viewport browser, yang dipulihkan pada langkah 17; hook `after` memulihkan viewport ke ukuran awal sebagai cadangan (tetap jalan walau spec gagal di tengah).

## Test Steps

### TC-GS-TAG-274: Screening Popup TAG Log, header grid, daftar bullet kronologis tanpa toolbar dan footer

1. Ketik Search `E2801160600002054D8A0001`, tekan Enter
2. Buka menu baris DD-01, klik `TAG Log`
3. Verifikasi judul popup `TAG Log`
4. Verifikasi badge Status `Paired`
5. Verifikasi grid label:value `Code` `E2801160600002054D8A0001` dan `TAG Type · Source` `RFID – Object TAG` `Official`
6. Verifikasi grid label:value `Device Name` `Handheld Scanner X1`, `SKU` `SKU-8821`, `Brand` `Zebra`, `Model/Type` `ZT410`
7. Verifikasi daftar log berupa bullet kronologis terbaru di atas: `TAG Paired by Budi S` (16/09/26 14:30), `TAG Reserved by Siti A` (15/09/26 10:00), lalu `TAG Activated by Budi S` (10/09/26 08:00)
8. Verifikasi tiap entri memuat judul kalimat plain text dan Date & Time
9. Verifikasi entri `TAG Reserved by Siti A` dan `TAG Paired by Budi S` memuat Description
10. Verifikasi pelaku pada entri teratas tampil sebagai ikon user dengan teks `Budi S` (`[First Name] [Last Initial]`)
11. Arahkan kursor ke pelaku `Budi S` pada entri teratas
12. Verifikasi tooltip nama lengkap `Budi Santoso`
13. Verifikasi tidak ada badge Event dan tidak ada baris PIC terpisah pada entri
14. Verifikasi tidak ada Search, Filter, Sort, Setup Column, Download, paginasi, maupun footer pada popup
15. Persempit viewport sehingga daftar log dapat di-scroll, lalu scroll daftar log
16. Verifikasi header popup tetap tampil sementara daftar log di-scroll
17. Pulihkan viewport, lalu klik `[✕]` pada popup
18. Verifikasi popup TAG Log tertutup
19. Buka menu baris DD-01, klik `TAG Log`, lalu tekan Esc
20. Verifikasi popup TAG Log tertutup

### TC-GS-TAG-276: Header TAG Log menampilkan nilai kosong sebagai —, tag Tab Paired tetap menampilkan Badge Status

21. Klik `(←)` pada kotak Search, klik Tab Paired, ketik Search `TAG-QR-00512`, tekan Enter
22. Buka menu baris DD-05, klik `TAG Log`
23. Verifikasi badge Status `Paired`
24. Verifikasi Device Name, SKU, Brand, dan Model/Type `—`
25. Verifikasi `TAG Type · Source` `QR` `Official`
26. Tutup popup lewat `[✕]`

### TC-GS-TAG-275: TAG Log tanpa riwayat menampilkan header dan empty state S-05

27. Klik avatar akun, pilih `Logout`
28. Login sebagai Total Control Client Log Wulan Sari (`Spectra.env.GS_TC_LOG_PASSWORD`)
29. Buka Global Settings > TAG, Tab All, ketik Search `E2801160600002054D8C0056`, tekan Enter
30. Buka menu baris tag tanpa riwayat (DD-56), klik `TAG Log`
31. Verifikasi header popup tampil (judul `TAG Log` dan Code `E2801160600002054D8C0056`)
32. Verifikasi empty state `No history yet` dengan deskripsi `Activity for this TAG will appear here.`
33. Tutup popup lewat `[✕]`

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md`. Subjudul `###` memetakan langkah ke id TC granular. Spec hanya membaca data.
- Urutan TC dalam spec: 274, 276, 275 (bukan urutan sumber). TC-276 (Client A, Tab Paired) mendahului TC-275 agar semua blok Client A berurutan sebelum ganti akun eksplisit (langkah 27 sampai 28); TC-275 tetap bermakna bila bagian sebelumnya gagal.
- Langkah penghubung (tanpa `Verifikasi`, tidak ada di TC): langkah 1, 21, 29 (Search agar baris target tampil), langkah 15 dan 17 (menyiapkan dan memulihkan viewport agar scroll teramati), langkah 17, 26, 33 (menutup popup), langkah 27 sampai 28 (ganti akun).
- Langkah 14 (absence kontrol) memakai daftar log pada langkah 7 sebagai anchor positif (bagian 8b butir 2). Langkah 8 dan 9 dipecah karena entri `Activated` DD-01 diasumsikan tanpa Description (lihat Temuan untuk QA).
- Temuan untuk QA:
  - TC-274 Expected b menyatakan tiap entri memuat Description, sedangkan TC-277 menyatakan entri `Activated` tanpa reader tidak memuat Description; spec mengasersi Description hanya untuk entri `Reserved` dan `Paired` DD-01 dan Date & Time untuk semua entri. TC-274 perlu menyebut isi Description per entri DD-01.
  - Isi entri TAG Log DD-01 diambil dari catatan fixture Tabel Data Uji Dinamis (`Activated`, `Reserved`, `Paired`); TC-274 hanya menyebut "≥3 entri" dan contoh judul `TAG Activated by 👤 Budi S`.
  - TC-274 langkah 3 ("Scroll daftar log") tidak menyebut apakah tiga entri DD-01 cukup panjang untuk di-scroll; spec menyempitkan viewport sebagai kemampuan teknis (disediakan tim FE).
  - TC-276 Expected tidak menyebut empty state `No history yet` walau DD-05 tanpa entri TAG Log menurut catatan fixture; spec tidak mengasersi empty state pada DD-05.
  - TC-275 Expected menyebut "Header tampil" tanpa merinci isi; spec mengasersi judul dan Code.
  - Seeding fixture TAG Log antar spec tidak didefinisikan di TC (Q-4, Q-15).
