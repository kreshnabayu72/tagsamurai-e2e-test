---
id: TC-GS-BRAND-E2E-033-master-data-count-limit-race-slot-terakhir
title: "Master Data Count Limit: Dua Admin Rebutan Slot Terakhir"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-BRAND-234
coverage:
  web: automated
---

# Master Data Count Limit: Dua Admin Rebutan Slot Terakhir

## Prerequisites

- Mode: FE+BE. Spec membuat race antar-sesi (kelas multi-konteks) di atas backend nyata.
- Akun admin pertama: Total Control Client Limit, `Wulan Sari`, `totalControl_automated_qaTeam4@qwertysystem.net`, password `Spectra.env.GS_LIMIT_TC_PASSWORD`. Login dan navigasi ke Global Settings > Master Reference > Brand dilakukan sekali di hook `before`.
- Akun admin kedua: Total Control Client Limit, `Yoga Permana`, `totalControlSecond_automated_qaTeam4@qwertysystem.net`, password `Spectra.env.GS_LIMIT_TC2_PASSWORD` (fixture baru, belum ada). Hook `before` membuka sesi browser kedua (konteks terpisah), login dengan akun ini, dan membuka Global Settings > Master Reference > Brand.
- Environment variable: `GS_LIMIT_TC_PASSWORD`, `GS_LIMIT_TC2_PASSWORD`, dan `GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture. Nama `GS_LIMIT_TC2_PASSWORD` didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Pemulihan sesi: hook `after` menutup sesi browser kedua dan mengembalikan sesi ke akun default suite (Total Control Client A, `totalControl_automated_qaTeam1@qwertysystem.net`, `Spectra.env.GS_TC_PASSWORD`).
- Fixture yang perlu disiapkan tim FE (belum ada): Client Limit dengan Master Data Count Limit 1.000 dan Selection Limit 100, berisi tepat 999 brand `Lim 001` sampai `Lim 999` (D-26) yang dibuat lewat Import Type Brand. Hook `before` memastikan jumlah brand 999 dan Master Data Count Limit 1.000 sebelum spec berjalan.
- State global bersama: spec 031, 032, dan 033 memakai tenant Client Limit yang sama dengan jumlah brand sebagai syarat. Ketiganya dijalankan serial (tidak paralel satu sama lain); spec ini mensyaratkan tepat 999 brand saat mulai, dan spec 032 memulihkan jumlah ke 999 di hook `after`-nya.
- Cleanup: hook `after` menghapus `Lim A {runId}-033` dan `Lim B {runId}-033` (bila ada) lewat API sehingga jumlah brand kembali 999, tanpa berasumsi langkah spec berhasil penuh.
- Kemampuan teknis: dua sesi browser paralel dan pemicu klik [Submit] hampir bersamaan di kedua sesi.
- TC-GS-BRAND-234: Master Data Count Limit 1.000, 999 brand; admin kedua siap; data uji `Lim A {runId}-033` dan `Lim B {runId}-033`.

## Test Steps

### TC-GS-BRAND-234: Dua admin rebutan slot terakhir Master Data Count Limit

1. Di sesi admin pertama: klik [+ Brand]
2. Di sesi admin pertama: isi Brand Name `Lim A {runId}-033`
3. Di sesi admin kedua: klik [+ Brand]
4. Di sesi admin kedua: isi Brand Name `Lim B {runId}-033`
5. Klik [Submit] di kedua sesi hampir bersamaan
6. Verifikasi salah satu admin mendapat toast sukses: "Success, brand has been created."
7. Verifikasi admin lainnya mendapat Dialog `Limit Reached` (bukan pesan duplikat)
8. Verifikasi form admin lainnya tetap terbuka
9. Di sesi admin yang mendapat Dialog `Limit Reached`: klik [OK]

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`.
- Admin pemenang race tidak deterministik; langkah 6 sampai 8 diasersi simetris untuk kedua sesi.
- Langkah penghubung (aksi tanpa `Verifikasi`): 9 (menutup Dialog `Limit Reached`). Langkah 1 sampai 4 memecah langkah TC "Kedua admin membuka [+ Brand] dan mengisi nama berbeda" per sesi.
- Dialog `Limit Reached` memakai teks `You've reached the platform limit of 1000 brands. Contact support if you need a higher limit.` dengan `[OK]` saja (lihat spec `TC-GS-BRAND-E2E-032-master-data-count-limit-create-dan-dialog`).
- Brand dibuat dengan suffix `{runId}-033` (nomor spec).
- Kelas harness: multi-konteks (dua admin, prinsip 13c) dan volume data (999 brand, prinsip 13e).
- Kebutuhan fixture belum ada (akun admin kedua dan 999 brand) sudah dicatat sebagai kebutuhan di Prerequisites.
