---
id: TC-AC-LA-E2E-103-sort-list-numerik-allocated-by-payment-dan-default
title: "Sort List: Numerik Quantity dan Cost serta Allocated By"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-LA-307
  - TC-AC-LA-308
coverage:
  web: automated
---

# Sort List: Numerik Quantity dan Cost serta Allocated By

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlLic_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_LA_TC_PRINCIPAL_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-license` (belum ada; disediakan tim FE). Nama env var di atas adalah usulan yang belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; didaftarkan tim FE.
- Data seed Pre-setup #54 (minimal 30 alokasi lintas enam status pada kedua tab, lebih dari 25 baris di tab Current; Quantity `+2`, `+5`, `+10`, `+50 GB`, `—`; Cost `$100.00`, `$150.00`, `$3,650.00`, `—`; Allocated By `Dewi A` untuk dua pengguna `Dewi Anggraini` dan `Dewi Angkasa`; Payment `Free` dan `Wallet`) bersifat baca-saja untuk spec ini. Ukuran halaman 100 dipakai agar seluruh nilai distinct Quantity dan Cost berada di halaman teramati (S-14).
- Kemampuan teknis: spec menyimpan konfigurasi kolom Setup Column (menampilkan `Cost`). Hook `after` menghapus preferensi kolom di peramban (bukan `[Reset to Default]`); kemampuan itu disediakan tim FE (konvensi bagian 4).
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > License Allocation pada tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.

## Test Steps

### TC-AC-LA-307: Sort numerik Quantity dan Cost

1. Ubah page size ke 100
2. Klik header Quantity
3. Verifikasi ascending natural 2, 5, 10, 50 (bukan 10, 2, 5, 50)
4. Verifikasi nilai `—` di akhir
5. Klik header Quantity
6. Verifikasi descending kebalikan dari ascending
7. Verifikasi nilai `—` di awal
8. Klik `⋯` pada header kolom Actions
9. Klik `Setup Column...`
10. Centang `Cost`
11. Klik `[Save]`
12. Klik header Cost
13. Verifikasi Cost mengurut berdasarkan nilai numerik (100, 150, 3650), bukan string tampilan
14. Klik header Cost
15. Verifikasi Cost descending berdasarkan nilai numerik

### TC-AC-LA-308: Sort Allocated By menurut nama lengkap

16. Klik header Allocated By
17. Verifikasi ascending: baris `Dewi Anggraini` sebelum `Dewi Angkasa` (nama lengkap pada tooltip), lalu nama lain menurut nama lengkap
18. Klik header Allocated By
19. Verifikasi descending: urutan kebalikan menurut nama lengkap

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-license/TestCases/tc-license-allocation-license.md`.
- Subjudul `###` memetakan langkah ke id TC granular. TC-AC-LA-309, 310, dan 311 dipindah ke spec 096 (spesifik Payment, pindah kolom, dan default sort).
- Langkah penghubung (S-03): langkah 1 (ukuran halaman 100 agar seluruh nilai distinct teramati), langkah 8 sampai 11 (menampilkan kolom Cost sesuai langkah TC).
- Temuan untuk QA:
  - TC-AC-LA-307 tidak menyebut ukuran halaman; spec memakai 100 karena urutan natural dan posisi `—` hanya teramati bila seluruh nilai distinct berada pada satu halaman.
  - TC-AC-LA-307 butir b menyebut Cost ascending; urutan descending Cost (langkah 15) diturunkan dari kata "ulangi" pada langkah 2 TC.
  - TC-AC-LA-308 tidak menyebut cara membaca nama lengkap; spec memakai tooltip sel Allocated By (TC-AC-LA-6).
