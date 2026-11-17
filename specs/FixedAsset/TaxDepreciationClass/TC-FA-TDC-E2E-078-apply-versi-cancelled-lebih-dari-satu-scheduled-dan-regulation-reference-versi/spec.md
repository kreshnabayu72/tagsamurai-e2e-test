---
id: TC-FA-TDC-E2E-078-apply-versi-cancelled-lebih-dari-satu-scheduled-dan-regulation-reference-versi
title: "Apply D-09: Versi Cancelled Tidak Dihitung Versi Terakhir, Lebih dari Satu Versi Scheduled, dan Regulation Reference Menjadi Milik Versi Baru"
layer: ui-e2e
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-272
  - TC-FA-TDC-273
  - TC-FA-TDC-274
sourceRules: ["FATDC-LOGIC-04t", "FATDC-LOGIC-04u.1", "V-22", "T-02c", "§4.1.6#r5", "FATDC-LOGIC-04i", "FATDC-LOGIC-04ad", "FATDC-LOGIC-04q.3", "FLD-05", "ST-30", "FATDC-LOGIC-04aa", "FATDC-LOGIC-04q.2", "§4.1.6#r11", "FATDC-LOGIC-04r.1"]
smoke: []
dependsOn: []
trace:
  "FATDC-LOGIC-04t": 5
  "FATDC-LOGIC-04u.1": [5, 7]
  "V-22": 7
  "T-02c": [9, 20, 35]
  "§4.1.6#r5": [12, 26]
  "FATDC-LOGIC-04i": 12
  "FATDC-LOGIC-04ad": 12
  "FATDC-LOGIC-04q.3": 22
  "FLD-05": 24
  "ST-30": 24
  "FATDC-LOGIC-04aa": 24
  "FATDC-LOGIC-04q.2": 26
  "§4.1.6#r11": [38, 39]
  "FATDC-LOGIC-04r.1": [38, 39]
coverage:
  web: automated
---

# Apply D-09: Versi Cancelled Tidak Dihitung Versi Terakhir, Lebih dari Satu Versi Scheduled, dan Regulation Reference Menjadi Milik Versi Baru

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- State global: jam sistem uji `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00) dan Fiscal Year Start Januari diatur di hook `before` (jam server dan browser bersama) dan dipulihkan di hook `after`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`; Non-building, Active, Used By 0, Straight Line dan Declining Balance):

| TC | Class (Class Code bersuffix) | Versi awal |
|---|---|---|
| TC-272 | `KHS-V11-{runId}-078` | versi Current Effective From Jan 2026 dan satu versi yang pernah Scheduled Effective From Jan 2028 lalu di-Cancel (status Cancelled); Useful Life 8 |
| TC-273 | `KHS-V5-{runId}-078` | versi Current tanpa Effective From (Useful Life 8) dan versi Scheduled Effective From Jan 2027 (Useful Life 10) |
| TC-274 | `KHS-V1-{runId}-078` | satu versi Current tanpa Effective From (Useful Life 8), tanpa versi Scheduled; Regulation Reference `UU HPP 7/2021; PMK 72/2023` |

- Pencarian baris target memakai kata kunci `{runId}-078` yang menampilkan ketiga class milik spec ini (R-16).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `{runId}-078`, tekan Enter

### TC-FA-TDC-272: Versi Cancelled tidak dihitung sebagai versi terakhir

2. Klik link Class Code `KHS-V11-{runId}-078` pada tabel
3. Ganti Useful Life menjadi `10`
4. Klik `[Save]`
5. Verifikasi nilai awal Select Effective From adalah `Jan 2026` (bukan `Jan 2028`) karena versi Cancelled tidak dihitung sebagai versi terakhir
6. Pilih Effective From `Jan 2027`
7. Verifikasi tidak ada caption V-22 pada Effective From
8. Klik `[Apply]`
9. Verifikasi toast sukses `Success, tax depreciation class has been updated.`
10. Klik link Class Code `KHS-V11-{runId}-078` pada tabel
11. Klik tautan View versions
12. Verifikasi modal Versions memuat tiga baris: `Jan 2027` berstatus `Scheduled`, `Jan 2028` berstatus `Cancelled`, dan `Jan 2026` berstatus `Current`
13. Tutup modal Versions
14. Klik `[×]` pada Drawer Edit

### TC-FA-TDC-273: Lebih dari satu versi Scheduled diizinkan; Alert dan tooltip merujuk Effective From paling awal

15. Klik link Class Code `KHS-V5-{runId}-078` pada tabel
16. Ganti Useful Life menjadi `12`
17. Klik `[Save]`
18. Pilih Effective From `Jan 2028`
19. Klik `[Apply]`
20. Verifikasi toast sukses `Success, tax depreciation class has been updated.`
21. Arahkan kursor ke sel Effective From baris `KHS-V5-{runId}-078`
22. Verifikasi tooltip sel Effective From `Next version starts Jan 2027.`
23. Klik link Class Code `KHS-V5-{runId}-078` pada tabel
24. Verifikasi Alert info merujuk versi `Jan 2027`: `Next version starts Jan 2027: 10 years, Straight Line 10%, Declining Balance 20%, Straight Line · Declining Balance.`
25. Klik tautan View versions
26. Verifikasi modal Versions memuat dua baris `Scheduled`: `Jan 2028` dan `Jan 2027`
27. Tutup modal Versions
28. Klik `[×]` pada Drawer Edit

### TC-FA-TDC-274: Regulation Reference yang berubah bersama Useful Life menjadi milik versi baru

29. Klik link Class Code `KHS-V1-{runId}-078` pada tabel
30. Ganti Regulation Reference menjadi `PMK 72/2023`
31. Ganti Useful Life menjadi `10`
32. Klik `[Save]`
33. Pilih Effective From `Jan 2027`
34. Klik `[Apply]`
35. Verifikasi toast sukses `Success, tax depreciation class has been updated.`
36. Klik link Class Code `KHS-V1-{runId}-078` pada tabel
37. Klik tautan View versions
38. Verifikasi modal Versions: baris `Jan 2027` (Scheduled) kolom Regulation Reference `PMK 72/2023`
39. Verifikasi modal Versions: baris `—` (Current) kolom Regulation Reference tetap `UU HPP 7/2021; PMK 72/2023`
40. Tutup modal Versions
41. Klik `[×]` pada Drawer Edit

## Notes

- Spec melewati sekitar 35 langkah (41 langkah): ketiga blok adalah fungsional kelas yang sama (Apply D-09 lalu modal Versions), memakai halaman dan dataset class yang sama, tiap blok memakai class milik sendiri, berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna; memisahnya hanya menggandakan login, hook, dan cleanup.
- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target; R-16), langkah 13, 14, 27, 28, 40, dan 41 (menutup modal Versions dan Drawer Edit yang tidak dirty agar tabel dapat diakses), langkah 21 (hover sebagai pemicu tooltip), langkah 10, 11, 23, 25, 36, dan 37 (membuka Drawer Edit dan tautan View versions untuk mengamati Alert dan modal Versions).
- Langkah 7 (TC-272 Expected b) ditulis sebelum `[Apply]` karena caption V-22 hanya mungkin tampil pada dialog yang masih terbuka; anchor positif adalah pilihan `Jan 2027` pada langkah 6.
- Temuan untuk QA:
  - TC-274 Post Condition (entri L-11 mencatat Regulation Reference pada versi baru) tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - TC-274 tidak menyebut nilai Regulation Reference awal class pada Precondition; nilai `UU HPP 7/2021; PMK 72/2023` diambil dari Expected c.
  - TC-272 tidak menyebut Straight Line Rate maupun Declining Balance Rate; tidak diasersi.
  - Email akun Total Control dan company uji tidak tertulis di TC; disediakan tim FE.
  - Kode class milik spec bersuffix `{runId}-078` (S-12); batas panjang Class Code tidak tertulis di TC.
