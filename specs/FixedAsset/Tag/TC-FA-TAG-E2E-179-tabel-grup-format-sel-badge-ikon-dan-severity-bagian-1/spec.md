---
id: TC-FA-TAG-E2E-179-tabel-grup-format-sel-badge-ikon-dan-severity-bagian-1
title: "Tabel Grup: Format Sel, Badge, Ikon, dan Severity (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-731
  - TC-FA-TAG-732
  - TC-FA-TAG-733
  - TC-FA-TAG-734
  - TC-FA-TAG-735
  - TC-FA-TAG-736
  - TC-FA-TAG-737
  - TC-FA-TAG-738
  - TC-FA-TAG-739
  - TC-FA-TAG-740
  - TC-FA-TAG-741
coverage:
  web: automated
---

# Tabel Grup: Format Sel, Badge, Ikon, dan Severity (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk grup dan aset Paired. Grup bernama panjang untuk TC-FA-TAG-733 dibuat lewat fixture backend. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE). Nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; seeding idempotent (dilewati bila sudah ada):

| Data | Nilai | Kunci |
|---|---|---|
| Dataset Paired | Grup 'Excavator 20 Ton' / Plant A / RFID / Total Assets 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; 'Excavator 20 Ton' / Plant B / RFID / 20 / 2 / 5 / 0; 'Laptop Pro 14' / HQ / NFC, QR / 25 / 1 / 0 / 2; 'Forklift Manual' / Plant A / Non TAG / 10 / 0 / 3 / 0 | `datasetPaired` |
| Hierarki Group | Plant A berada di bawah Head Office | `hierarkiPlantA` |
| Grup bernama panjang | Group 'Regional Distribution Center Jakarta' (lebih dari 25 karakter) yang dipakai satu baris grup milik spec, bersuffix `{runId}-179` pada Asset Name baris itu; dibuat sebelum TC-FA-TAG-733 | `grupNamaPanjang` |

- State yang diubah dan pemulihannya: grup dan baris dengan Group 'Regional Distribution Center Jakarta' dibuat sebelum TC-FA-TAG-733 dan dihapus di hook `after`; tidak ada perubahan lain.

## Test Steps

### TC-FA-TAG-731

1. Arahkan pointer ke Asset Name 'Forklift Manual'
2. Verifikasi Asset Name tampil sebagai Text link
3. Klik Asset Name 'Forklift Manual'
4. Verifikasi Popup Detail `Assets` untuk Forklift Manual / Plant A terbuka
5. Tutup Popup Detail

### TC-FA-TAG-732

6. Arahkan pointer ke badge Group pada baris Forklift Manual
7. Verifikasi badge Group berseverity primary
8. Verifikasi tooltip hover menampilkan hierarki penuh `Head Office > Plant A`

### TC-FA-TAG-733

9. Buat baris grup dengan Group 'Regional Distribution Center Jakarta' lewat fixture backend hingga tersimpan, lalu muat ulang halaman
10. Verifikasi badge Group pada baris yang memakai group itu menampilkan `Regional Dis..nter Jakarta`
11. Arahkan pointer ke badge tersebut
12. Verifikasi hover menampilkan nama dan hierarki penuh

### TC-FA-TAG-734

13. Verifikasi ikon NFC dan ikon QR tampil berdampingan pada kolom TAG Type baris Laptop Pro 14 / HQ

### TC-FA-TAG-735

14. Verifikasi badge `Non TAG` tampil tanpa ikon tipe pada kolom TAG Type baris Forklift Manual / Plant A
15. Verifikasi baris grup Non-TAG tampil di tab Paired

### TC-FA-TAG-736

16. Arahkan pointer ke ikon pada baris Excavator 20 Ton / Plant A
17. Verifikasi tooltip `RFID` tampil

### TC-FA-TAG-737

18. Verifikasi semua angka pada kolom Total Assets, Reported, Non-standard, dan Not Paired Yet berupa bilangan bulat tanpa pemisah desimal
19. Verifikasi semua angka pada kolom Total Assets, Reported, Non-standard, dan Not Paired Yet rata kanan

### TC-FA-TAG-738

20. Verifikasi sel bernilai nol pada baris Excavator 20 Ton / Plant A (Reported 0, Non-standard 0) dan Excavator 20 Ton / Plant B (Not Paired Yet 0) menampilkan `0` (bukan kosong atau strip)
21. Verifikasi sel bernilai nol tampil tanpa badge severity

### TC-FA-TAG-739

22. Verifikasi angka `2` pada sel Reported baris Excavator 20 Ton / Plant B tampil dengan severity danger

### TC-FA-TAG-740

23. Verifikasi angka `3` pada sel Non-standard baris Forklift Manual / Plant A tampil dengan severity warning

### TC-FA-TAG-741

24. Verifikasi angka `2` pada sel Not Paired Yet baris Laptop Pro 14 / HQ tampil dengan severity warning

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-731, TC-FA-TAG-732, TC-FA-TAG-733, TC-FA-TAG-734, TC-FA-TAG-735, TC-FA-TAG-736, TC-FA-TAG-737, TC-FA-TAG-738, TC-FA-TAG-739, TC-FA-TAG-740, TC-FA-TAG-741). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik format sel tabel grup ada di spec 179 (TC-FA-TAG-731 s.d. 741) dan spec 180 (TC-FA-TAG-742).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): langkah 5, 9 (menutup Popup Detail dan seeding baris dengan Group bernama panjang lewat fixture backend).
- Temuan untuk QA:
  - Langkah TC-FA-TAG-737 s.d. 741 hanya berupa pengamatan tanpa aksi; spec menuliskannya sebagai Verifikasi langsung tanpa langkah aksi.
  - TC-FA-TAG-733 tidak menyebut cara membentuk baris dengan Group bernama panjang (aset atau grup); spec memintanya dari fixture backend tim FE/BE.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
