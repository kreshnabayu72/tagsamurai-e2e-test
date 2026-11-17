---
id: TC-FA-TDC-E2E-095-job-j-03-last-posted-tax-year-memajukan-nilai-dan-kunci-class-code
title: "Job J-03: Posting Penyusutan Fiskal Memajukan Last Posted Tax Year dan Mengunci Class Code"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-353
  - TC-FA-TDC-354
  - TC-FA-TDC-355
  - TC-FA-TDC-356
  - TC-FA-TDC-357
sourceRules: ["§4.1.2#r11", "F-FATDC-11.k1a", "ST-06", "§4.3#r16", "D-04", "FATDC-LOGIC-09a", "F-FATDC-11.k2"]
smoke: []
dependsOn: []
trace:
  "§4.1.2#r11": [4, 15]
  "F-FATDC-11.k1a": [4, 15]
  "ST-06": 6
  "§4.3#r16": 6
  "D-04": 9
  "FATDC-LOGIC-09a": 11
  "F-FATDC-11.k2": [20, 25]
coverage:
  web: automated
---

# Job J-03: Posting Penyusutan Fiskal Memajukan Last Posted Tax Year dan Mengunci Class Code

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Email akun tidak tertulis di Pre-setup TC (lihat Temuan untuk QA); password lewat `Spectra.env.FA_TC_PASSWORD`. Hook, sesi API aktor, seed dan pemulihan lewat API, dan flag Guided Tooltip mengikuti `suite.md`.
- Kemampuan teknis: memicu posting penyusutan fiskal untuk tahun pajak tertentu pada class lewat fixture BE (job J-03; Depreciation Run belum tersedia; disediakan tim FE/BE, mekanismenya tidak disebut TC, S-13).
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`; semua Active, Non-building, Used By 0):

| TC | Class (Class Code bersuffix) | Last Posted Tax Year awal |
|---|---|---|
| TC-353 | `KHS-LP-{runId}-095` | kosong |
| TC-354 | `KHS-LP2-{runId}-095` (Class Name `Kelompok posting`) | `2026` |
| TC-355 | `KHS-LP3-{runId}-095` | `2025` |
| TC-356 | `KHS-LP4-{runId}-095` | `2026` |
| TC-357 | `KHS-LP5-{runId}-095` | `2026` |

- Tabel berisi tujuh class seed bawaan dan kelima class di atas (12 baris); baris `KHS-*` berada di halaman pertama (urutan default Class Code A-Z, `KHS-*` sebelum `LAND`) sehingga dibuka tanpa Search.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-353: Posting pertama memajukan Last Posted Tax Year dari kosong dan mengunci Class Code

1. Picu posting penyusutan fiskal tahun pajak 2026 untuk `KHS-LP-{runId}-095` lewat fixture BE (J-03)
2. Muat ulang halaman
3. Klik link Class Code `KHS-LP-{runId}-095` pada tabel
4. Verifikasi Last Posted Tax Year bernilai "2026"
5. Arahkan kursor ke ikon gembok pada Class Code
6. Verifikasi Class Code Disabled dengan ikon gembok dan tooltip "Code can't be changed after fiscal depreciation has been posted."
7. Klik `[×]` pada header Drawer

### TC-FA-TDC-354: Setelah J-03, Delete class ditolak oleh Guard 1

8. Pada baris `KHS-LP2-{runId}-095` klik ikon ⋯ → `Delete`
9. Verifikasi dialog D-04: judul "Cannot Delete Tax Depreciation Class", bullet "• KHS-LP2-{runId}-095 – Kelompok posting", teks "It was used for fiscal depreciation in 2026.", tombol `[OK]`
10. Klik `[OK]`
11. Verifikasi class `KHS-LP2-{runId}-095` tetap ada di tabel

### TC-FA-TDC-355: Tahun pajak lebih baru memajukan nilai

12. Picu posting penyusutan fiskal tahun pajak 2026 untuk `KHS-LP3-{runId}-095` lewat fixture BE (J-03)
13. Muat ulang halaman
14. Klik link Class Code `KHS-LP3-{runId}-095` pada tabel
15. Verifikasi Last Posted Tax Year bernilai "2026"
16. Klik `[×]` pada header Drawer

### TC-FA-TDC-356: Tahun pajak sama dengan nilai tersimpan tidak berefek

17. Picu posting penyusutan fiskal tahun pajak 2026 untuk `KHS-LP4-{runId}-095` lewat fixture BE (J-03)
18. Muat ulang halaman
19. Klik link Class Code `KHS-LP4-{runId}-095` pada tabel
20. Verifikasi Last Posted Tax Year tetap "2026"
21. Klik `[×]` pada header Drawer

### TC-FA-TDC-357: Tahun pajak lebih lama tidak memundurkan Last Posted Tax Year

22. Picu posting penyusutan fiskal tahun pajak 2025 untuk `KHS-LP5-{runId}-095` lewat fixture BE (J-03)
23. Muat ulang halaman
24. Klik link Class Code `KHS-LP5-{runId}-095` pada tabel
25. Verifikasi Last Posted Tax Year tetap "2026"
26. Klik `[×]` pada header Drawer

## Notes

- Langkah penghubung (S-03): langkah 2, 13, 18, 23 (muat ulang agar nilai dari fixture BE terbaca), dan langkah 7, 16, 21, 26 (menutup Drawer tanpa perubahan, tanpa dialog `Unsaved Changes`). Langkah 10 (`[OK]`) menutup dialog D-04 yang diasersi pada langkah 9.
- Langkah 5 membuka tooltip yang diasersi bersama ikon gembok pada langkah 6 (state sementara diasersi sebelum langkah yang mengubahnya, 8b.5).
- Satu class per TC karena tiap TC membutuhkan nilai Last Posted Tax Year awal berbeda.
- Post Condition TC-353 (satu entri L-10 Modified By System; Guard 1 berlaku), TC-355 (satu entri L-10: Old Value "2025", New Value "2026"), TC-356 dan TC-357 ("tidak ada entri L-10 baru") tidak punya langkah observasi di TC; tidak diasersi di spec ini (S-01). "Guard 1 berlaku" TC-353 diamati pada TC-354. Pencatatan L-10 ada di spec 096.
- Temuan untuk QA:
  - Post Condition TC-353, 355, 356, 357 tanpa langkah observasi di TC.
  - TC-354 tidak menyebut Class Code/Name dengan suffix; spec memakai `-{runId}-095` (S-12), sehingga bullet D-04 memuat Class Code bersuffix.
  - TC-353 sampai 357 memakai `KHS-LP`, `KHS-LP2` sampai `KHS-LP5` tanpa suffix (S-12).
  - Email akun Total Control tidak tertulis di TC.
