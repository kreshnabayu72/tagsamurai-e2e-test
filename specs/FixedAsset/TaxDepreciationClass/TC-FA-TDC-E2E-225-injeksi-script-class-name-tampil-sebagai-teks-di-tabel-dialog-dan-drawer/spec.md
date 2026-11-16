---
id: TC-FA-TDC-E2E-225-injeksi-script-class-name-tampil-sebagai-teks-di-tabel-dialog-dan-drawer
title: "Injeksi Script pada Class Name Tampil sebagai Teks di Tabel, Dialog, dan Drawer"
layer: ui-e2e
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TDC-865
  - TC-FA-TDC-866
  - TC-FA-TDC-867
  - TC-FA-TDC-868
  - TC-FA-TDC-869
sourceRules: ["§4.1.1#r3", "§4.1.2#p1", "D-01", "D-06", "D-02"]
smoke: []
dependsOn: []
trace:
  "§4.1.1#r3": 1
  "§4.1.2#p1": 5
  "D-01": 9
  "D-06": 14
  "D-02": 19
anchor: [2, 3, 6, 10, 15, 20]
coverage:
  web: automated
---

# Injeksi Script pada Class Name Tampil sebagai Teks di Tabel, Dialog, dan Drawer

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control (company uji Fixed Asset); password lewat `Spectra.env.FA_TC_PASSWORD`. Akun dan email disediakan tim FE (email tidak tertulis di TC; lihat Temuan untuk QA). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Kemampuan suite yang dipakai (dinyatakan di `suite.md`): seed dan pemulihan lewat API (Class Name berisi script dan Used By lewat Asset Class pemakai), flag Guided Tooltip disetel true oleh hook suite, dan hook `beforeEach` mengonfirmasi `beforeunload`. Pengamatan dialog JavaScript (alert) oleh test runner.
- Data milik spec (seed idempotent di hook `before` lewat API, dipulihkan di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; nilai mengacu ke `Fixture.fixedAssetTaxDepreciationClass.<kunci>`, fixture disediakan tim FE):

| Kunci fixture (usulan) | Class Code | Nilai |
|---|---|---|
| `nb4` | `NB-4` | Class Name `<script>alert(1)</script>`, Active, Used By 0 |
| `nb3` | `NB-3` | Active, Used By 0 (tanpa script pada Class Name) |
| `nb2` | `NB-2` | Class Name `<script>alert(1)</script>`, Active, Used By 3 (Asset Class pemakai disediakan tim FE) |

- Tabel berisi tujuh class seed bawaan (NB-1, NB-2, NB-3, NB-4, BLD-P, BLD-NP, LAND) dalam satu halaman Pagination (10 baris per halaman), sehingga baris target tampil tanpa Search.
- Pemulihan: hook `after` mengembalikan Class Name `NB-4` dan `NB-2` ke nilai seed lewat API.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-865: Class Name berisi script ditampilkan sebagai teks pada tabel

1. Verifikasi kolom Class Name baris `NB-4` menampilkan teks `<script>alert(1)</script>` apa adanya
2. Verifikasi tidak ada dialog alert JavaScript yang muncul
3. Verifikasi markup tidak dirender sebagai elemen pada kolom Class Name baris `NB-4`

### TC-FA-TDC-869: Class Name berisi script ditampilkan sebagai teks pada header Drawer Edit

4. Klik link Class Code `NB-4`
5. Verifikasi baris di bawah judul Drawer menampilkan `Class Name: <script>alert(1)</script>` apa adanya
6. Verifikasi tidak ada dialog alert JavaScript yang muncul
7. Klik `[×]` pada header Drawer Edit

### TC-FA-TDC-866: Class Name berisi script ditampilkan sebagai teks pada dialog Deactivate

8. Klik toggle `Active` baris `NB-4`
9. Verifikasi bullet dialog menampilkan teks `• NB-4 – <script>alert(1)</script>` apa adanya
10. Verifikasi tidak ada dialog alert JavaScript yang muncul
11. Klik `[Cancel]` pada dialog Deactivate

### TC-FA-TDC-867: Class Name berisi script ditampilkan sebagai teks pada dialog Delete jamak

12. Centang baris `NB-4` dan `NB-3`
13. Klik `Delete` pada Bulk Action Bar
14. Verifikasi bullet dialog menampilkan teks `• NB-4 – <script>alert(1)</script>` apa adanya
15. Verifikasi tidak ada dialog alert JavaScript yang muncul
16. Klik `[Cancel]` pada dialog Delete
17. Klik `Unselect All` pada Bulk Action Bar

### TC-FA-TDC-868: Class Name berisi script ditampilkan sebagai teks pada dialog blok

18. Klik toggle `Active` baris `NB-2`
19. Verifikasi bullet dialog blok menampilkan teks `• NB-2 – <script>alert(1)</script>` apa adanya
20. Verifikasi tidak ada dialog alert JavaScript yang muncul
21. Tekan Esc untuk menutup dialog blok

## Notes

- Urutan TC: TC-FA-TDC-865, 869, 866, 867, 868. TC-FA-TDC-869 (Drawer, tanpa perubahan data) diletakkan sebelum blok dialog; seluruh dialog ditutup tanpa Confirm sehingga data tidak berubah.
- Langkah penghubung (S-03): langkah 7 (menutup Drawer Edit yang field-nya tidak diubah, sehingga tanpa dialog `Unsaved Changes`); langkah 11, 16, dan 21 (menutup dialog tanpa Confirm); langkah 17 (membersihkan seleksi, S-09).
- Asersi absence dialog alert JavaScript (langkah 2, 6, 10, 15, dan 20) selalu didahului `Verifikasi` teks script tampil pada surface yang sama (langkah 1, 5, 9, 14, dan 19) sebagai anchor positif (8b.2). Langkah 3 didahului langkah 1 pada kolom yang sama.
- Temuan untuk QA:
  - TC-FA-TDC-867 mensyaratkan Class Name script hanya pada `NB-4` (dan `NB-3` tanpa script); spec hanya mengasersi bullet `NB-4`.
  - TC-FA-TDC-866 dan TC-FA-TDC-867 tidak menyebut cara menutup dialog; spec memakai `[Cancel]` agar data tidak berubah.
  - TC-FA-TDC-868 tidak menyebut judul dialog blok; spec mengasersi bullet saja.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga data milik spec memakai kode literal tanpa suffix `{runId}-<NNN>` (S-12); perlu konfirmasi QA.
