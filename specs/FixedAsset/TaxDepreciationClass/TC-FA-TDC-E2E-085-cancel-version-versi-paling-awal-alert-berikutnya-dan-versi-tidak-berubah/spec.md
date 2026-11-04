---
id: TC-FA-TDC-E2E-085-cancel-version-versi-paling-awal-alert-berikutnya-dan-versi-tidak-berubah
title: "Cancel Version pada Dua Versi Scheduled: Alert Berpindah ke Versi Berikutnya dan Versi Terbentuk Tidak Berubah"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-303
  - TC-FA-TDC-304
  - TC-FA-TDC-314
coverage:
  web: automated
---

# Cancel Version pada Dua Versi Scheduled: Alert Berpindah ke Versi Berikutnya dan Versi Terbentuk Tidak Berubah

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam sistem: tanggal sistem uji `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00) dengan Fiscal Year Start Januari; jam server dan jam browser diatur bersama di hook `before` dan dipulihkan di hook `after`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`; semua Active, Used By 0):

| TC | Class (Class Code bersuffix) | Isi |
|---|---|---|
| TC-303 | `KHS-C4-{runId}-085` | Current tanpa Effective From (Useful Life 8); Scheduled Jan 2027 (Useful Life 10) dan Jan 2028 (Useful Life 12); Straight Line dan Declining Balance |
| TC-304 | `KHS-C5-{runId}-085` | Sama dengan `KHS-C4` (dua versi Scheduled Jan 2027 dan Jan 2028) |
| TC-314 | `KHS-C7-{runId}-085` | Satu versi Current tanpa Effective From (Useful Life 8, Straight Line dan Declining Balance, Regulation Reference `UU HPP 7/2021; PMK 72/2023`) |

- Tabel berisi tujuh class seed bawaan dan ketiga class di atas (10 baris pada satu halaman, page size default 10); baris `KHS-*` berada di halaman pertama sehingga dibuka tanpa Search.
- Kemampuan teknis: seeding class dengan dua versi Scheduled lewat API; hover pada sel tabel untuk membaca tooltip.
- State yang diubah: class milik spec; dihapus di hook `after`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-303: Membatalkan versi Scheduled paling awal

1. Klik link Class Code `KHS-C4-{runId}-085` pada tabel
2. Klik `[Cancel scheduled version]` pada Alert
3. Klik `[Cancel version]`
4. Verifikasi toast sukses "Success, scheduled version has been cancelled."
5. Verifikasi Alert menampilkan: "Next version starts Jan 2028: 12 years, Straight Line 8.33%, Declining Balance 16.67%, Straight Line · Declining Balance."
6. Klik `[×]` pada header Drawer
7. Arahkan kursor ke sel Effective From baris `KHS-C4-{runId}-085`
8. Verifikasi tooltip sel Effective From: "Next version starts Jan 2028."

### TC-FA-TDC-304: Membatalkan versi Scheduled yang bukan paling awal lewat modal Versions

9. Klik link Class Code `KHS-C5-{runId}-085` pada tabel
10. Klik tautan View versions
11. Pada baris "Jan 2028" klik `[Cancel]`
12. Amati D-10
13. Verifikasi D-10 menampilkan "Effective From Jan 2028"
14. Klik `[Cancel version]`
15. Verifikasi toast sukses "Success, scheduled version has been cancelled."
16. Verifikasi Alert tetap menampilkan versi paling awal: "Next version starts Jan 2027: 10 years, Straight Line 10%, Declining Balance 20%, Straight Line · Declining Balance."
17. Klik tautan View versions
18. Verifikasi modal Versions: "Jan 2028" berstatus "Cancelled"; "Jan 2027" tetap "Scheduled"
19. Tutup modal Versions
20. Klik `[×]` pada header Drawer

### TC-FA-TDC-314: Versi yang sudah dibentuk tidak berubah saat versi baru dibentuk

21. Klik link Class Code `KHS-C7-{runId}-085` pada tabel
22. Klik tautan View versions dan catat nilai baris (Useful Life 8, Straight Line Rate 12.5%, Declining Balance Rate 25%, Regulation Reference "UU HPP 7/2021; PMK 72/2023")
23. Tutup modal Versions
24. Ganti Useful Life menjadi `10` dan Regulation Reference menjadi `PMK 72/2023`, klik `[Save]`
25. Pilih Effective From "Jan 2026"
26. Klik `[Apply]`
27. Tunggu aksi selesai
28. Klik link Class Code `KHS-C7-{runId}-085` pada tabel
29. Klik tautan View versions
30. Verifikasi baris "—" berstatus "Past" tetap Useful Life 8, Straight Line Rate 12.5%, Declining Balance Rate 25%, Regulation Reference "UU HPP 7/2021; PMK 72/2023"
31. Verifikasi baris "Jan 2026" berstatus "Current" memuat nilai baru (Useful Life 10, Regulation Reference "PMK 72/2023")
32. Tutup modal Versions
33. Klik `[×]` pada header Drawer

## Notes

- Langkah penghubung (S-03): langkah 6, 20, dan 33 (menutup Drawer tanpa perubahan, tanpa dialog `Unsaved Changes`), langkah 19, 23, dan 32 (menutup modal Versions), langkah 27 ("Tunggu aksi selesai", 8b.8; hasil Apply tidak diasersi TC), dan langkah 12 ("Amati" tanpa asersi).
- Langkah 28 membuka Drawer lagi karena Drawer Edit tertutup setelah Apply sukses (NC-21).
- Langkah 22 mencatat nilai baris awal; langkah 30 membandingkannya dengan Expected TC-314 butir a.
- Aksi yang mengubah versi (membatalkan, menerapkan) memakai class berbeda per TC karena pembatalan dan Apply tidak dapat diulang pada class yang sama.
- Post Condition tidak ada pada ketiga TC.
- Temuan untuk QA:
  - TC-303/304/314 memakai `KHS-C4`, `KHS-C5`, `KHS-C7` tanpa suffix; spec memakai `-{runId}-085` (S-12).
  - TC-314 langkah 3 menggabungkan ganti nilai, `[Save]`, pilih Effective From, dan `[Apply]` dalam satu langkah; spec memecahnya per aksi. Tidak ada Expected toast pada Apply sukses.
  - TC-304 langkah 4 menggabungkan "Amati D-10" dan `[Cancel version]`; spec memecahnya.
  - Email akun Total Control tidak tertulis di TC.
