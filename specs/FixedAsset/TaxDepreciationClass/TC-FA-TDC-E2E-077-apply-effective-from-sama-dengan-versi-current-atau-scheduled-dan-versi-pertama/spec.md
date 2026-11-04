---
id: TC-FA-TDC-E2E-077-apply-effective-from-sama-dengan-versi-current-atau-scheduled-dan-versi-pertama
title: "Apply Effective From Sama dengan Versi Current atau Scheduled Menggantikan Versi Itu, dan Versi Terakhir Adalah Versi Pertama"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-269
  - TC-FA-TDC-270
  - TC-FA-TDC-271
coverage:
  web: automated
---

# Apply Effective From Sama dengan Versi Current atau Scheduled Menggantikan Versi Itu, dan Versi Terakhir Adalah Versi Pertama

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- State global: jam sistem uji `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00) dan Fiscal Year Start Januari diatur di hook `before` (jam server dan browser bersama) dan dipulihkan di hook `after`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`; Non-building, Active, Used By 0, Straight Line dan Declining Balance):

| TC | Class (Class Code bersuffix) | Versi awal |
|---|---|---|
| TC-269 | `KHS-V3-{runId}-077` | versi pertama (Useful Life 8, tanpa Effective From, status Past) dan versi Current Effective From Jan 2026 (Useful Life 10) |
| TC-270 | `KHS-V4-{runId}-077` | versi Current tanpa Effective From (Useful Life 8) dan versi Scheduled Effective From Jan 2027 (Useful Life 10) |
| TC-271 | `KHS-V1-{runId}-077` | satu versi Current tanpa Effective From (Useful Life 8), tanpa versi Scheduled |

- Pencarian baris target memakai kata kunci `{runId}-077` yang menampilkan ketiga class milik spec ini (R-16).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `{runId}-077`, tekan Enter

### TC-FA-TDC-269: Apply dengan Effective From sama dengan versi Current bertanggal menggantikan versi itu

2. Klik link Class Code `KHS-V3-{runId}-077` pada tabel
3. Ganti Useful Life menjadi `12`
4. Klik `[Save]`
5. Pilih Effective From `Jan 2026`
6. Klik `[Apply]`
7. Verifikasi toast sukses `Success, tax depreciation class has been updated.`
8. Verifikasi dialog Save Changes dan Drawer Edit tertutup
9. Verifikasi baris tabel `KHS-V3-{runId}-077`: Useful Life (years) `12`, Effective From `Jan 2026`
10. Klik link Class Code `KHS-V3-{runId}-077` pada tabel
11. Klik tautan View versions
12. Verifikasi modal Versions memuat tiga baris berurutan (dua baris ber-Effective From sama diurutkan menurut waktu pembuatan terbaru di atas): `Jan 2026` Useful Life 12 berstatus `Current`; `Jan 2026` Useful Life 10 berstatus `Past`; `—` Useful Life 8 berstatus `Past`
13. Tutup modal Versions
14. Klik `[×]` pada Drawer Edit

### TC-FA-TDC-270: Apply dengan Effective From sama dengan versi Scheduled membatalkan versi Scheduled itu dan menggantinya

15. Klik link Class Code `KHS-V4-{runId}-077` pada tabel
16. Ganti Useful Life menjadi `12`
17. Klik `[Save]`
18. Pilih Effective From `Jan 2027`
19. Klik `[Apply]`
20. Verifikasi toast sukses `Success, tax depreciation class has been updated.`
21. Verifikasi dialog Save Changes dan Drawer Edit tertutup
22. Klik link Class Code `KHS-V4-{runId}-077` pada tabel
23. Verifikasi Alert info `Next version starts Jan 2027: 12 years, Straight Line 8.33%, Declining Balance 16.67%, Straight Line · Declining Balance.`
24. Klik tautan View versions
25. Verifikasi modal Versions memuat tiga baris berurutan (dua baris ber-Effective From sama diurutkan menurut waktu pembuatan terbaru di atas): `Jan 2027` Useful Life 12 berstatus `Scheduled`; `Jan 2027` Useful Life 10 berstatus `Cancelled`; `—` berstatus `Current`
26. Tutup modal Versions
27. Klik `[×]` pada Drawer Edit

### TC-FA-TDC-271: Versi terakhir adalah versi pertama tanpa Effective From

28. Klik link Class Code `KHS-V1-{runId}-077` pada tabel
29. Ganti Useful Life menjadi `10`
30. Klik `[Save]`
31. Pilih Effective From `Jan 2031`
32. Verifikasi tidak ada caption V-22 pada Effective From
33. Klik `[Apply]`
34. Verifikasi toast sukses `Success, tax depreciation class has been updated.`
35. Klik link Class Code `KHS-V1-{runId}-077` pada tabel
36. Klik tautan View versions
37. Verifikasi modal Versions: versi baru `Jan 2031` berstatus `Scheduled`
38. Verifikasi modal Versions: versi pertama `—` tetap berstatus `Current` (tidak digantikan)
39. Tutup modal Versions
40. Klik `[×]` pada Drawer Edit

## Notes

- Spec melewati sekitar 35 langkah (40 langkah): ketiga blok adalah fungsional kelas yang sama (Apply D-09 lalu modal Versions), memakai halaman dan dataset class yang sama, tiap blok memakai class milik sendiri, berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; memisahnya hanya menggandakan login, hook, dan cleanup.
- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target; R-16), langkah 13, 14, 26, 27, 39, dan 40 (menutup modal Versions dan Drawer Edit yang tidak dirty agar tabel dapat diakses).
- Langkah 32 (TC-271 Expected b) ditulis sebelum `[Apply]` karena caption V-22 hanya mungkin tampil pada dialog yang masih terbuka; sesudah Apply berhasil dialog tertutup. Urutan ini menyimpang dari urutan Expected TC.
- Langkah 8 dan 21 memuat klausa "dialog D-09 dan Drawer Edit tertutup" (TC-269 Expected d, TC-270 Expected d); tabel menampilkan data terbaru dibuktikan langkah 9. Langkah 35 dan 36 pada TC-271 adalah langkah observasi yang tidak ditulis TC (Expected c membutuhkan modal Versions).
- Temuan untuk QA:
  - TC-269 Post Condition (entri log L-03 hanya memuat baris Useful Life) dan TC-270 Post Condition (entri L-09 dan L-11 pada transaksi yang sama) tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - TC-271 tidak memberi langkah observasi untuk Expected c (status versi baru dan versi pertama); spec menambahkan langkah 35 dan 36 (membuka modal Versions) sebagai langkah penghubung.
  - TC-269 dan TC-270 Expected menyebut "diurutkan menurut waktu pembuatan terbaru di atas" tanpa menyatakan kolom waktu pembuatan terlihat di modal Versions; urutan diasersi sesuai teks TC.
  - Email akun Total Control dan company uji tidak tertulis di TC; disediakan tim FE.
  - Kode class milik spec bersuffix `{runId}-077` (S-12); batas panjang Class Code tidak tertulis di TC.
