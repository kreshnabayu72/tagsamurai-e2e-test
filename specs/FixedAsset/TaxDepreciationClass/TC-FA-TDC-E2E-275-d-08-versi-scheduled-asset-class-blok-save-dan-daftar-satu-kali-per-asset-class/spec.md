---
id: TC-FA-TDC-E2E-275-d-08-versi-scheduled-asset-class-blok-save-dan-daftar-satu-kali-per-asset-class
title: "Dialog D-08 karena Versi Scheduled Asset Class: Blok Save dan Daftar Satu Kali per Asset Class"
layer: ui-e2e
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TDC-962
  - TC-FA-TDC-965
sourceRules: ["F-FATDC-02.k6d", "FATDC-LOGIC-10a", "FATDC-LOGIC-10b.1", "FATDC-LOGIC-10c", "D-08", "E-FATDC-94", "§4.2c#b1"]
smoke: []
dependsOn: []
trace:
  "F-FATDC-02.k6d": [5, 18]
  "FATDC-LOGIC-10a": [5, 18]
  "FATDC-LOGIC-10b.1": [5, 18]
  "FATDC-LOGIC-10c": [5, 6, 7, 10, 18, 19, 20, 21, 22]
  "D-08": [5, 6, 7, 8, 18, 19, 20, 21, 22]
  "E-FATDC-94": [5, 10]
  "§4.2c#b1": [9, 23]
coverage:
  web: automated
---

# Dialog D-08 karena Versi Scheduled Asset Class: Blok Save dan Daftar Satu Kali per Asset Class

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (akun default suite). Email akun dan nama env password disediakan tim FE (usulan nama env `FA_TC_PASSWORD`); email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook, sesi API aktor, seed dan pemulihan lewat API, kendali jam, dan flag Guided Tooltip mengikuti `suite.md`.
- Jam sistem: tanggal sistem uji 15 Okt 2026 10:00 WIB (Time Zone entitas Asia/Jakarta) dengan Fiscal Year Start Januari; jam server dan jam browser diatur bersama lewat kendali jam (`suite.md`) di hook `before` dan dipulihkan di hook `after`.
- Kemampuan teknis (disediakan tim FE/BE, lihat `suite.md`): seeding class dan Asset Class pemakai beserta versi Current dan versi Scheduled Asset Class lewat API (versi Scheduled Asset Class dibentuk di modul Asset Class); pembacaan jumlah versi class lewat fixture BE (langkah 3 dan 10).
- Nilai data mengacu ke `Fixture.fixedAssetTaxDepreciationClass` (fixture belum ada, disediakan tim FE; nama kunci ditetapkan tim FE).
- Data milik spec (seed idempotent di hook `before` lewat API, dihapus di hook `after`; kode memakai literal TC karena Class Code maksimal 15 karakter sehingga suffix `{runId}-<NNN>` tidak muat; Non-building, Useful Life 8, Straight Line dan Declining Balance):

| Kunci fixture (usulan) | Class Code | Keterangan |
|---|---|---|
| `khsV15` | `KHS-V15` | Used By 1: Asset Class `AC-SCH1 – Mesin Gerinda` memakai Straight Line pada versi Current dan Declining Balance pada versi Scheduled Jan 2027 Asset Class (TC-962) |
| `khsV16` | `KHS-V16` | Used By 2: `AC-SCH2 – Pompa Sentrifugal` (Declining Balance pada versi Current dan pada versi Scheduled Jan 2027 Asset Class) dan `AC-SCH3 – Mesin Pres` (Straight Line pada versi Current, Declining Balance pada versi Scheduled Jan 2027 Asset Class) (TC-965) |

- Tabel memuat tujuh class seed bawaan dan dua class milik spec (9 baris dalam satu halaman) sehingga baris target dibuka tanpa Search (8b.13, R-23).
- State global yang diubah: jam server dan jam browser (hook `before`, dipulihkan di hook `after`). Drawer ditutup dengan `[Leave]` sehingga Allowed Methods class tidak berubah.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-TDC-962: Save yang mempersempit Allowed Methods diblokir D-08 karena versi Scheduled Asset Class memakai metode yang dihapus

1. Klik link Class Code `KHS-V15` pada tabel
2. Lepas `Declining Balance` dari Allowed Methods
3. Catat baseline jumlah versi class `KHS-V15` lewat fixture BE
4. Klik `[Save]`
5. Verifikasi judul dialog adalah `Cannot Remove This Method`
6. Verifikasi teks `1 asset class uses Declining Balance. Change it first.`
7. Verifikasi satu bullet `• AC-SCH1 – Mesin Gerinda` tampil di bawah teks
8. Verifikasi footer memuat satu tombol `[OK]`
9. Verifikasi dialog D-09 tidak muncul
10. Verifikasi tidak ada versi baru: jumlah versi `KHS-V15` sama dengan baseline langkah 3
11. Klik `[OK]` pada dialog D-08
12. Klik `[×]` pada Drawer Edit
13. Verifikasi dialog `Unsaved Changes` tampil
14. Klik `[Leave]`

### TC-FA-TDC-965: D-08 mendaftar Asset Class yang memakai metode yang dihapus pada versi Current dan Scheduled satu kali per Asset Class

15. Klik link Class Code `KHS-V16` pada tabel
16. Lepas `Declining Balance` dari Allowed Methods
17. Klik `[Save]`
18. Verifikasi dialog D-08 dengan teks `2 asset classes use Declining Balance. Change them first.`
19. Verifikasi tepat dua bullet tampil di bawah teks
20. Verifikasi bullet `• AC-SCH2 – Pompa Sentrifugal` tampil
21. Verifikasi bullet `• AC-SCH3 – Mesin Pres` tampil
22. Verifikasi `AC-SCH2 – Pompa Sentrifugal` tidak muncul dua kali
23. Verifikasi dialog D-09 tidak muncul
24. Klik `[OK]` pada dialog D-08
25. Klik `[×]` pada Drawer Edit
26. Verifikasi dialog `Unsaved Changes` tampil
27. Klik `[Leave]`

## Notes

- Langkah penghubung (S-03): langkah 3 (baseline jumlah versi untuk asersi "tanpa versi baru", S-12), langkah 11 sampai 14 dan 24 sampai 27 (menutup D-08 dan Drawer yang dirty lewat `[OK]`, `[×]`, dialog `Unsaved Changes`, `[Leave]`; S-08).
- Absence pada langkah 9, 10, 23: anchor positif adalah dialog D-08 yang tampil (langkah 5 sampai 8 dan 18 sampai 22). Langkah 10 mengasersi klausa "tidak ada versi baru" Expected c TC-962; klausa "tidak ada entri log" TC-962 diasersi di spec absence 253 dengan aksi nyata dan baseline sendiri (S-05).
- Langkah 22 memecah klausa Expected b TC-965 ("tepat dua bullet" dan "AC-SCH2 tidak muncul dua kali") menjadi `Verifikasi` terpisah (S-01); langkah 19 sampai 21 menyatakan tepat dua bullet beserta isinya.
- Pembagian TC lintas spec: TC-283, 286, 287 ada di spec 081; TC-284, 285 di spec 237; TC-288, 289, 290, 292 di spec 082; TC-963 (re-cek server saat Apply) di spec 276; TC-964 (request langsung) di spec 220 dan 270.
- Temuan untuk QA:
  - TC-962 dan TC-965 menyebut Asset Class pemakai hanya dengan kode dan nama (`AC-SCH1`, `AC-SCH2`, `AC-SCH3`) tanpa cara membentuk versi Scheduled Asset Class; spec memakai seeding lewat API yang disediakan tim FE/BE.
  - TC-962 butir c menyebut "tidak ada entri log" tanpa surface; asersinya ada di spec 253 (Changelog, mengikuti TC-696).
  - Class Code dibatasi 15 karakter (TC-136, 137), sehingga data milik spec memakai kode literal TC tanpa suffix `{runId}-<NNN>` (S-12); perlu konfirmasi QA.
  - Email akun Total Control dan identitas company uji tidak tertulis di TC.
