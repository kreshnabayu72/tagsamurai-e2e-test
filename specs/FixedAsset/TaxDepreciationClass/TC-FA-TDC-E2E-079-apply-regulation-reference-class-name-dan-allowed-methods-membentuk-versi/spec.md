---
id: TC-FA-TDC-E2E-079-apply-regulation-reference-class-name-dan-allowed-methods-membentuk-versi
title: "Apply D-09: Regulation Reference Diwarisi, Class Name Ditulis Langsung, dan Perubahan Allowed Methods Tanpa Guard Persempit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-275
  - TC-FA-TDC-276
  - TC-FA-TDC-277
  - TC-FA-TDC-278
coverage:
  web: automated
---

# Apply D-09: Regulation Reference Diwarisi, Class Name Ditulis Langsung, dan Perubahan Allowed Methods Tanpa Guard Persempit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- State global: jam sistem uji `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00) dan Fiscal Year Start Januari diatur di hook `before` (jam server dan browser bersama) dan dipulihkan di hook `after`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`; semua Non-building, Useful Life 8, Active, satu versi Current tanpa Effective From, tanpa versi Scheduled):

| TC | Class (Class Code bersuffix) | Allowed Methods | Used By | Keterangan |
|---|---|---|---|---|
| TC-275 | `KHS-V1-{runId}-079` | Straight Line dan Declining Balance | 0 | Regulation Reference `UU HPP 7/2021; PMK 72/2023` |
| TC-276 | `KHS-V1B-{runId}-079` | Straight Line dan Declining Balance | 0 | state awal yang sama dengan TC-275 |
| TC-277 | `KHS-V6-{runId}-079` | Straight Line saja | 1 | Asset Class `AC-SL1` memakai Straight Line (disediakan tim FE/BE) |
| TC-278 | `KHS-V7-{runId}-079` | Straight Line dan Declining Balance | 1 | Asset Class `AC-SL1` memakai Straight Line (disediakan tim FE/BE) |

- Pencarian baris target memakai kata kunci `{runId}-079` yang menampilkan keempat class milik spec ini (R-16).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `{runId}-079`, tekan Enter

### TC-FA-TDC-275: Versi baru yang tidak mengubah Regulation Reference mewarisi versi sebelumnya

2. Klik link Class Code `KHS-V1-{runId}-079` pada tabel
3. Ganti Useful Life menjadi `10`
4. Klik `[Save]`
5. Pilih Effective From `Jan 2027`
6. Klik `[Apply]`
7. Verifikasi toast sukses `Success, tax depreciation class has been updated.`
8. Klik link Class Code `KHS-V1-{runId}-079` pada tabel
9. Klik tautan View versions
10. Verifikasi modal Versions: baris `Jan 2027` kolom Regulation Reference `UU HPP 7/2021; PMK 72/2023` (sama dengan versi sebelumnya)
11. Tutup modal Versions
12. Klik `[×]` pada Drawer Edit

### TC-FA-TDC-276: Class Name berubah bersama Useful Life ditulis langsung

13. Klik link Class Code `KHS-V1B-{runId}-079` pada tabel
14. Ganti Class Name menjadi `Kelompok versi uji`
15. Ganti Useful Life menjadi `10`
16. Klik `[Save]`
17. Pilih Effective From `Jan 2027`
18. Klik `[Apply]`
19. Verifikasi toast sukses `Success, tax depreciation class has been updated.`
20. Verifikasi baris tabel `KHS-V1B-{runId}-079` langsung menampilkan Class Name `Kelompok versi uji`
21. Verifikasi Useful Life tabel tetap `8` (versi baru Scheduled)

### TC-FA-TDC-277: Menambah Declining Balance membentuk versi baru lewat D-09 tanpa guard persempit

22. Klik link Class Code `KHS-V6-{runId}-079` pada tabel
23. Tambahkan `Declining Balance` pada Allowed Methods
24. Klik `[Save]`
25. Verifikasi dialog D-09 muncul
26. Verifikasi dialog D-08 tidak muncul
27. Pilih Effective From `Jan 2026`
28. Klik `[Apply]`
29. Verifikasi toast sukses `Success, tax depreciation class has been updated.`
30. Verifikasi baris tabel `KHS-V6-{runId}-079`: Declining Balance Rate `25%`, Allowed Methods `Straight Line · Declining Balance`

### TC-FA-TDC-278: Mempersempit Allowed Methods diizinkan bila tidak ada Asset Class yang memakai metode yang dihapus

31. Klik link Class Code `KHS-V7-{runId}-079` pada tabel
32. Lepas `Declining Balance` dari Allowed Methods
33. Klik `[Save]`
34. Verifikasi dialog D-09 muncul
35. Verifikasi dialog D-08 tidak muncul
36. Pilih Effective From `Jan 2026`
37. Klik `[Apply]`
38. Verifikasi toast sukses `Success, tax depreciation class has been updated.`
39. Verifikasi baris tabel `KHS-V7-{runId}-079`: Declining Balance Rate `—`, Allowed Methods `Straight Line`

## Notes

- Spec melewati sekitar 35 langkah (39 langkah): keempat blok adalah fungsional kelas yang sama (Apply D-09 dengan class berbeda), memakai halaman dan dataset class yang sama, tiap blok memakai class milik sendiri, berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; memisahnya hanya menggandakan login, hook, dan cleanup.
- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target; R-16), langkah 8 dan 9 (membuka Drawer Edit dan tautan View versions untuk mengamati modal Versions), langkah 11 dan 12 (menutup modal Versions dan Drawer Edit yang tidak dirty).
- Absence pada langkah 26 dan 35: anchor positif adalah dialog D-09 yang tampil (langkah 25 dan 34).
- Temuan untuk QA:
  - TC-278 Post Condition ("Declining Balance Rate tidak disimpan pada versi baru") dan TC-276 Post Condition (entri L-02 dan L-11) tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - TC-277 dan TC-278 Data Uji menyebut Asset Class `AC-SL1` tanpa nama; Asset Class pemakai disediakan tim FE/BE.
  - TC-277 dan TC-278 menyebut "Declining Balance Rate" tabel `25%` dan `—` tetapi tidak menyebut Useful Life setelah versi baru; tidak diasersi.
  - Email akun Total Control dan company uji tidak tertulis di TC; disediakan tim FE.
  - Kode class milik spec bersuffix `{runId}-079` (S-12); batas panjang Class Code tidak tertulis di TC.
