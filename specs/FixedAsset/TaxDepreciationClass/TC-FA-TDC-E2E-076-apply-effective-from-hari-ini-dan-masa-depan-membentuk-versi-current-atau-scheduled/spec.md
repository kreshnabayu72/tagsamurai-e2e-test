---
id: TC-FA-TDC-E2E-076-apply-effective-from-hari-ini-dan-masa-depan-membentuk-versi-current-atau-scheduled
title: "Apply Effective From Hari Ini Langsung Membentuk Versi Current dan Effective From Masa Depan Membentuk Versi Scheduled"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-267
  - TC-FA-TDC-268
sourceRules: ["T-02b", "§[F-FATDC-02] Edit Tax Depreciation Class#b6", "§4.1.1#r5", "§4.1.1#r6", "§4.1.1#r7", "§4.1.1#r10", "FATDC-LOGIC-03f.1", "FATDC-LOGIC-03f.2", "FATDC-LOGIC-04ad", "§4.1.2#r10", "ST-30", "§4.1.6#r4", "§4.1.6#r5", "§4.1.6#r6", "FATDC-LOGIC-04g.2", "T-02c", "FATDC-LOGIC-04h", "FATDC-LOGIC-04q.3", "FLD-05", "FATDC-LOGIC-04ab", "FATDC-LOGIC-04p.5"]
smoke: []
dependsOn: []
trace:
  "T-02b": 7
  "§[F-FATDC-02] Edit Tax Depreciation Class#b6": [8, 24]
  "§4.1.1#r5": [9, 25]
  "§4.1.1#r6": [9, 25]
  "§4.1.1#r7": [9, 25]
  "§4.1.1#r10": [9, 25, 27]
  "FATDC-LOGIC-03f.1": [9, 25, 29]
  "FATDC-LOGIC-03f.2": [9, 25, 29]
  "FATDC-LOGIC-04ad": [11, 32]
  "§4.1.2#r10": 11
  "ST-30": [12, 29]
  "§4.1.6#r4": [14, 15]
  "§4.1.6#r5": [14, 15, 32, 33]
  "§4.1.6#r6": [14, 15]
  "FATDC-LOGIC-04g.2": 15
  "T-02c": 23
  "FATDC-LOGIC-04h": 25
  "FATDC-LOGIC-04q.3": 27
  "FLD-05": 29
  "FATDC-LOGIC-04ab": 30
  "FATDC-LOGIC-04p.5": 33
coverage:
  web: automated
---

# Apply Effective From Hari Ini Langsung Membentuk Versi Current dan Effective From Masa Depan Membentuk Versi Scheduled

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- State global: jam sistem uji `15 Okt 2026 10:00 WIB` (Time Zone entitas Asia/Jakarta, UTC+07:00) dan Fiscal Year Start Januari diatur di hook `before` (jam server dan browser bersama) dan dipulihkan di hook `after`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`; Non-building, Useful Life 8, Straight Line dan Declining Balance, Active, Used By 0, satu versi Current tanpa Effective From, tanpa versi Scheduled; Straight Line Rate 12.5% dan Declining Balance Rate 25%):

| TC | Class (Class Code bersuffix) | Keterangan |
|---|---|---|
| TC-267 | `KHS-V1-{runId}-076` | state awal TC-267 |
| TC-268 | `KHS-V1B-{runId}-076` | state awal TC-268 (kelas kedua karena TC-267 mengubah class pertama) |

- Pencarian baris target memakai kata kunci `{runId}-076` yang menampilkan kedua class milik spec ini (R-16).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `{runId}-076`, tekan Enter

### TC-FA-TDC-267: Apply dengan Effective From pada atau sebelum hari ini langsung membentuk versi Current

2. Klik link Class Code `KHS-V1-{runId}-076` pada tabel
3. Ganti Useful Life menjadi `10`
4. Klik `[Save]`
5. Pilih Effective From `Jan 2026`
6. Klik `[Apply]`
7. Verifikasi toast sukses `Success, tax depreciation class has been updated.`
8. Verifikasi dialog Save Changes dan Drawer Edit tertutup
9. Verifikasi baris tabel `KHS-V1-{runId}-076`: Useful Life (years) `10`, Straight Line Rate `10%`, Declining Balance Rate `20%`, Effective From `Jan 2026`
10. Klik link Class Code `KHS-V1-{runId}-076` pada tabel
11. Verifikasi tautan View versions tampil pada Drawer Edit
12. Verifikasi Alert versi Scheduled tidak tampil pada Drawer Edit
13. Klik tautan View versions
14. Verifikasi modal Versions: baris `Jan 2026` berstatus `Current` dengan Useful Life 10
15. Verifikasi modal Versions: baris `—` berstatus `Past` dengan Useful Life 8
16. Tutup modal Versions
17. Klik `[×]` pada Drawer Edit

### TC-FA-TDC-268: Apply dengan Effective From di masa depan membentuk versi Scheduled dan versi Current tetap berlaku

18. Klik link Class Code `KHS-V1B-{runId}-076` pada tabel
19. Ganti Useful Life menjadi `10`
20. Klik `[Save]`
21. Pilih Effective From `Jan 2027`
22. Klik `[Apply]`
23. Verifikasi toast sukses `Success, tax depreciation class has been updated.`
24. Verifikasi dialog Save Changes dan Drawer Edit tertutup
25. Verifikasi baris tabel `KHS-V1B-{runId}-076` tetap: Useful Life (years) `8`, Straight Line Rate `12.5%`, Declining Balance Rate `25%`, Effective From `—`
26. Arahkan kursor ke sel Effective From baris `KHS-V1B-{runId}-076`
27. Verifikasi tooltip sel Effective From `Next version starts Jan 2027.`
28. Klik link Class Code `KHS-V1B-{runId}-076` pada tabel
29. Verifikasi Drawer Edit memuat Alert info `Next version starts Jan 2027: 10 years, Straight Line 10%, Declining Balance 20%, Straight Line · Declining Balance.`
30. Verifikasi Alert memuat tombol `[Cancel scheduled version]`
31. Klik tautan View versions
32. Verifikasi modal Versions: baris `Jan 2027` berstatus `Scheduled`
33. Verifikasi modal Versions: baris `—` tetap berstatus `Current`
34. Tutup modal Versions
35. Klik `[×]` pada Drawer Edit

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target; R-16), langkah 16, 17, 34, dan 35 (menutup modal Versions dan Drawer Edit yang tidak dirty), langkah 26 (hover sebagai pemicu tooltip).
- TC-267 dan TC-268 memakai class milik spec yang berbeda karena TC-267 mengubah class pertama menjadi dua versi (S-06); TC sumber memakai nama class yang sama (`KHS-V1`) untuk keduanya.
- Absence pada langkah 12: anchor positif adalah langkah 11 (Drawer Edit tampil dengan tautan View versions).
- Langkah 8 dan 24 memuat klausa "Setelah langkah 5: dialog D-09 dan Drawer Edit tertutup" (TC-267 Expected e, TC-268 Expected f); klausa "tabel menampilkan data terbaru" dibuktikan oleh langkah 9 dan 25.
- Temuan untuk QA:
  - TC-267 Post Condition b dan TC-268 Post Condition a, b, c (entri log L-03 dan L-11, "versi pertama tidak menjadi Past", fakta untuk Preferences) tidak punya langkah observasi di TC dan tidak diasersi (S-01). Pada TC-268, versi pertama tetap `Current` diasersi pada langkah 33 karena ada di Expected e.
  - TC-267 dan TC-268 tidak menyebut email akun Total Control maupun company uji; disediakan tim FE.
  - Kode class milik spec bersuffix `{runId}-076` (S-12); batas panjang Class Code tidak tertulis di TC.
