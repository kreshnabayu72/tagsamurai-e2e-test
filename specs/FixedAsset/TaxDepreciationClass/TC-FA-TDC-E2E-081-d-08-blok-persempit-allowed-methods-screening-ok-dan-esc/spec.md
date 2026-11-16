---
id: TC-FA-TDC-E2E-081-d-08-blok-persempit-allowed-methods-screening-ok-dan-esc
title: "Dialog D-08 Blok Persempit Allowed Methods: Screening untuk Lebih dari Satu Asset Class, Tombol OK, dan Esc"
layer: ui-e2e
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TDC-283
  - TC-FA-TDC-286
  - TC-FA-TDC-287
sourceRules: ["D-08", "F-FATDC-02.k6b", "E-FATDC-17", "§7.3#b1", "§7.3#b2", "F-FATDC-02.k6c", "§4.2c#b1"]
smoke: []
dependsOn: []
trace:
  "D-08": [5, 6, 7, 8, 14, 20]
  "F-FATDC-02.k6b": 7
  "E-FATDC-17": [9, 15, 21]
  "§7.3#b1": [16, 21]
  "§7.3#b2": 17
  "F-FATDC-02.k6c": 22
  "§4.2c#b1": 24
coverage:
  web: automated
---

# Dialog D-08 Blok Persempit Allowed Methods: Screening untuk Lebih dari Satu Asset Class, Tombol OK, dan Esc

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Kemampuan teknis: pembacaan nilai class lewat fixture BE (untuk asersi "tidak ada yang tersimpan"; disediakan tim FE/BE).
- Data Dinamis (di-seed di hook `before` lewat API, dihapus di hook `after`):

| TC | Class (Class Code bersuffix) | Keterangan |
|---|---|---|
| TC-283, 286, 287 | `KHS-V8-{runId}-081` | Non-building, Useful Life 8, Straight Line dan Declining Balance, Used By 2: Asset Class `AC-DB1 – Pompa Air Gudang` dan `AC-DB2 – Genset Pabrik` keduanya memakai Declining Balance (Asset Class pemakai disediakan tim FE/BE) |

- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `KHS-V8-{runId}-081`, tekan Enter
2. Klik link Class Code `KHS-V8-{runId}-081` pada tabel

### TC-FA-TDC-283: Screening dialog D-08 untuk lebih dari satu Asset Class yang memakai metode yang dihapus

3. Lepas `Declining Balance` dari Allowed Methods
4. Klik `[Save]`
5. Verifikasi judul dialog adalah `Cannot Remove This Method`
6. Verifikasi teks body `2 asset classes use Declining Balance. Change them first.`
7. Verifikasi dua bullet `• AC-DB1 – Pompa Air Gudang` dan `• AC-DB2 – Genset Pabrik` tampil di bawah teks
8. Verifikasi footer memuat satu tombol `[OK]`
9. Verifikasi dialog D-09 tidak muncul

### TC-FA-TDC-286: Tombol OK pada D-08 menutup dialog dan Drawer tetap terbuka dengan nilai form utuh

10. Klik `[OK]` pada dialog D-08
11. Ganti Class Name menjadi `Kelompok V8 baru`
12. Klik `[Save]`
13. Klik `[OK]` pada dialog D-08
14. Verifikasi dialog D-08 tertutup
15. Verifikasi Drawer Edit tetap terbuka dengan Allowed Methods hanya `Straight Line`
16. Verifikasi Class Name `Kelompok V8 baru` dipertahankan pada Drawer Edit
17. Verifikasi tidak ada toast

### TC-FA-TDC-287: Esc pada D-08 menutup dialog

18. Klik `[Save]`
19. Tekan `Esc`
20. Verifikasi dialog D-08 tertutup
21. Verifikasi Drawer Edit tetap terbuka dengan nilai form utuh
22. Verifikasi tidak ada yang tersimpan: Class Name class `KHS-V8-{runId}-081` tetap nilai awal (dibaca lewat fixture BE)
23. Klik `[×]` pada Drawer Edit
24. Verifikasi dialog `Unsaved Changes` tampil
25. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target; R-16), langkah 10 (menutup D-08 TC-283 agar Class Name dapat diganti), langkah 23 sampai 25 (menutup Drawer yang dirty lewat `[×]`, dialog `Unsaved Changes`, `[Leave]`; S-08).
- Ketiga TC memakai satu class dan satu sesi Drawer Edit yang dibuka pada langkah 2; Allowed Methods yang dilepas pada langkah 3 dipertahankan di form, sehingga langkah 1 dan 2 TC-286 dan TC-287 identik dengan keadaan yang sudah terbentuk. Urutan TC: 283, 286, 287.
- Absence pada langkah 9: anchor positif adalah dialog D-08 yang tampil (langkah 5 sampai 8). Absence pada langkah 17: anchor positif adalah Drawer Edit yang tetap terbuka (langkah 15 dan 16).
- TC-284 dan TC-285 (D-08 untuk tepat satu Asset Class dan untuk Straight Line) ada di spec 237; TC-288, 289, 290, 292 ada di spec 082.
- Temuan untuk QA:
  - TC-286 Post Condition (tidak ada data tersimpan, tidak ada entri log) tidak punya langkah observasi di TC dan tidak diasersi (S-01).
  - TC-283, 286, 287 tidak menyebut tanggal sistem uji maupun Fiscal Year Start (tidak relevan untuk D-08); jam tidak diatur di spec ini.
  - TC-287 Expected "tidak ada yang tersimpan" diasersi lewat fixture BE (Class Name tetap nilai awal); TC tidak memberi langkah observasi lain.
  - Email akun Total Control dan company uji tidak tertulis di TC; disediakan tim FE.
  - Kode class milik spec bersuffix `{runId}-081` (S-12); batas panjang Class Code tidak tertulis di TC.
