---
id: TC-AC-ACAL-E2E-052-absence-aksi-dibatalkan-dan-gagal-di-modul-sumber-tidak-tercatat
title: "Absence: Aksi Dibatalkan dan Gagal di Modul Sumber Tidak Tercatat"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACAL-146
  - TC-AC-ACAL-175
coverage:
  web: automated
---

# Absence: Aksi Dibatalkan dan Gagal di Modul Sumber Tidak Tercatat

## Prerequisites

- Mode: FE+BE.
- Kelas harness g (asersi absence, bagian 3 prinsip 13): semua TC di spec ini mengasersi "tidak ada baris atau entri log" untuk kondisi yang ditolak atau tidak dicatat. Tiap TC punya baseline dan data sendiri.
- Suite serial (`parallel: false`); hook suite dinyatakan di suite.md.
- Guided Tooltip: hook suite before/after menyetel flag seen halaman Activity Log untuk akun Total Control Principal (lihat suite.md).
- Akun aktor: Total Control (Principal), `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), `Spectra.env.AC_TC_PASSWORD` (terdaftar di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Spec tidak berganti akun UI dan hook `after` tidak perlu memulihkan sesi (akun default suite).
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), dibuat lewat sesi API di hook `before`:
  - Client `PT Sejahtera {runId}-052` dengan PIC Name awal `PIC Awal {runId}-052` (TC memakai `PT Sejahtera`; bersuffix karena data uji tulis milik spec).
  - Partner `Partner Uji {runId}-052` berstatus Active (target dialog Suspend TC-AC-ACAL-146).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Client dan Partner dinamis di atas bila masih ada. Entri log tidak dapat dihapus; nama bersuffix run.
- Kemampuan teknis (disediakan tim FE/BE):
  - Pemasangan intercept pada request Edit Client (respons pertama 5xx, respons kedua error validasi; kode status dan body mengikuti kontrak modul Client) dan pelepasannya (S-09); intercept hanya sebagai pemicu (P-5 butir a).
  - Pembacaan state Client lewat fixture BE (nilai PIC Name tersimpan).
  - Baseline (S-12): jumlah total entri dibaca dari footer `Showing X–Y of Z entries` sebelum aksi pemicu dan dibandingkan sebagai selisih, bukan angka absolut.
- Jam server dan jam browser tidak diatur. Tidak ada state global yang diubah (semua data milik spec).

## Test Steps

1. Klik tab "User Action"

### TC-AC-ACAL-146: Aksi yang dibatalkan di modul sumber tidak tercatat

2. Catat jumlah total entri dari footer `Showing X–Y of Z entries` (nilai Z) sebagai baseline E0
3. Buka Admin Console > Client, ketik Search `PT Sejahtera {runId}-052`, tekan Enter, lalu buka form Edit pada baris itu
4. Ubah PIC Name menjadi `PIC Batal {runId}-052`
5. Klik `[×]` pada header form Edit
6. Verifikasi dialog `Unsaved Changes` tampil
7. Klik [Leave]
8. Buka Admin Console > Partner, ketik Search `Partner Uji {runId}-052`, tekan Enter, lalu buka dialog Suspend pada baris itu
9. Klik [Cancel] pada dialog Suspend
10. Buka Admin Console > Activity Log > User Action
11. Verifikasi jumlah total entri pada footer sama dengan baseline E0, sehingga tidak ada entri baru untuk kedua aksi

### TC-AC-ACAL-175: Aksi sumber yang gagal di server tidak meninggalkan entri log

12. Catat jumlah total entri dari footer `Showing X–Y of Z entries` (nilai Z) sebagai baseline F0
13. Pasang intercept pada request Edit Client `PT Sejahtera {runId}-052`: respons pertama 5xx, respons kedua error validasi
14. Buka Admin Console > Client, ketik Search `PT Sejahtera {runId}-052`, tekan Enter, lalu buka form Edit pada baris itu
15. Ubah PIC Name menjadi `PIC Gagal {runId}-052`
16. Klik [Save] (respons 5xx)
17. Klik [Save] (respons error validasi)
18. Lepas intercept pada request Edit Client
19. Verifikasi data Client `PT Sejahtera {runId}-052` tidak berubah: PIC Name tersimpan tetap `PIC Awal {runId}-052` (dibaca lewat fixture BE)
20. Klik `[×]` pada header form Edit
21. Verifikasi dialog `Unsaved Changes` tampil
22. Klik [Leave]
23. Buka Admin Console > Activity Log > User Action
24. Verifikasi jumlah total entri pada footer sama dengan baseline F0
25. Ketik Search `PT Sejahtera {runId}-052`, tekan Enter
26. Verifikasi baris `Create` `Client` `PT Sejahtera {runId}-052` tampil
27. Verifikasi tidak ada baris `Edit` `Client` Field `PIC Name` untuk `PT Sejahtera {runId}-052`
28. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-146, 175).
- P-5 butir (a): spec absence boleh memuat pemicu kelas lain bila hanya membentuk kondisi yang diasersi tidak tercatat. Pemicu di sini: intercept respons 5xx dan error validasi (kelas b, TC-AC-ACAL-175). Intercept dilepas segera setelah pemicu selesai (langkah 18, S-09). Tiap TC punya baseline sendiri.
- Langkah penghubung (tanpa awalan `Verifikasi`): pindah tab dan menu (langkah 1, 10, 23), pencatatan baseline (langkah 2, 12), dan mencari baris target di modul sumber lewat Search (langkah 3, 8, 14). Langkah 25 sampai 28 adalah Search pembanding dan pemulihannya.
- Asersi tambahan di luar Expected TC (S-03): langkah 26 (baris `Create` hasil seeding sebagai anchor positif sebelum asersi absence) dan langkah 19 (data Client tidak berubah mengikuti Expected b TC-AC-ACAL-175). Asersi absence jumlah memakai baseline selisih pada surface agregat (bagian 8b butir 2).
- Jalur penutupan form Edit pada langkah 5 sampai 7 dan 20 sampai 22 mengikuti konvensi label tombol (bagian 9 konvensi; S-08): form Edit ditutup lewat `[×]`, dialog `Unsaved Changes`, lalu [Leave], sesuai TC-AC-ACAL-146 (tutup form lewat `[×]`, lalu klik `[Leave]`).
- Temuan untuk QA:
  - Form Edit Client tidak punya `[Cancel]` menurut konvensi label tombol (PRD §24.1); penutupan form memakai `[×]` dan `[Leave]` sesuai TC-AC-ACAL-146.
  - TC-AC-ACAL-146 dan 175 tidak menyebut data uji pelengkap (Client yang diedit, Partner yang di-Suspend); spec memakai data bersuffix milik spec. TC-AC-ACAL-175 memakai `PT Sejahtera` yang berbeda dari Client Sejahtera pada Pre-setup No 8; QA konfirmasi apakah keduanya entitas yang sama.
  - TC-AC-ACAL-175 tidak menyebut kode status dan body respons "error validasi"; kontrak modul Client menetapkannya (kemampuan intercept disediakan tim FE).
  - Email Pre-setup memakai placeholder `{namaCompany}` dan password memakai `AC_TC_PASSWORD` (terdaftar di `.env.example` dan `spectra.config.ts`).
