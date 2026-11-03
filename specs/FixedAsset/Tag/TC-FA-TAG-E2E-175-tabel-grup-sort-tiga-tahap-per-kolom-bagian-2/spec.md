---
id: TC-FA-TAG-E2E-175-tabel-grup-sort-tiga-tahap-per-kolom-bagian-2
title: "Tabel Grup: Sort Kolom Non-standard dan Not Paired Yet, Urutan Bawaan, dan Pindah Kolom (Bagian 2)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-707
  - TC-FA-TAG-708
  - TC-FA-TAG-709
  - TC-FA-TAG-710
  - TC-FA-TAG-711
coverage:
  web: automated
---

# Tabel Grup: Sort Kolom Non-standard dan Not Paired Yet, Urutan Bawaan, dan Pindah Kolom (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk grup dan aset Paired. Grup tambahan milik spec untuk TC-FA-TAG-711 (delapan grup sehingga tabel grup lebih dari 10 baris). Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE). Nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; seeding idempotent (dilewati bila sudah ada):

| Data | Nilai | Kunci |
|---|---|---|
| Dataset Paired | Grup 'Excavator 20 Ton' / Plant A / RFID / Total Assets 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; 'Excavator 20 Ton' / Plant B / RFID / 20 / 2 / 5 / 0; 'Laptop Pro 14' / HQ / NFC, QR / 25 / 1 / 0 / 2; 'Forklift Manual' / Plant A / Non TAG / 10 / 0 / 3 / 0 | `datasetPaired` |
| Grup tambahan TC-FA-TAG-711 | Delapan grup tambahan milik spec bersuffix `{runId}-175-<n>`; dibuat sebelum TC-FA-TAG-711, dihapus di hook `after` | `grupTambahan175` |

- State yang diubah dan pemulihannya: grup tambahan dibuat sebelum TC-FA-TAG-711; hook `after` menghapusnya.

## Test Steps

### TC-FA-TAG-707

1. Klik header kolom Non-standard
2. Verifikasi indikator naik aktif pada kolom Non-standard dan urutan: Excavator 20 Ton / Plant A (0), Laptop Pro 14 (0), Forklift Manual (3), Excavator 20 Ton / Plant B (5)
3. Klik header kolom Non-standard sekali lagi
4. Verifikasi indikator turun aktif pada kolom Non-standard dan urutan: Excavator 20 Ton / Plant B (5), Forklift Manual (3), Excavator 20 Ton / Plant A (0), Laptop Pro 14 (0)
5. Klik header kolom Non-standard sekali lagi
6. Verifikasi indikator sort nonaktif dan urutan kembali ke bawaan Asset Name A-Z

### TC-FA-TAG-708

7. Klik header kolom Not Paired Yet
8. Verifikasi indikator naik aktif pada kolom Not Paired Yet dan urutan: Excavator 20 Ton / Plant B (0), Forklift Manual (0), Excavator 20 Ton / Plant A (2), Laptop Pro 14 (2)
9. Klik header kolom Not Paired Yet sekali lagi
10. Verifikasi indikator turun aktif pada kolom Not Paired Yet dan urutan: Excavator 20 Ton / Plant A (2), Laptop Pro 14 (2), Excavator 20 Ton / Plant B (0), Forklift Manual (0)
11. Klik header kolom Not Paired Yet sekali lagi
12. Verifikasi indikator sort nonaktif dan urutan kembali ke bawaan Asset Name A-Z

### TC-FA-TAG-709

13. Buka menu Fixed Asset > TAG
14. Verifikasi baris terurut Asset Name A-Z: Excavator 20 Ton, Excavator 20 Ton, Forklift Manual, Laptop Pro 14
15. Verifikasi tidak ada indikator sort aktif pada kolom lain

### TC-FA-TAG-710

16. Klik header kolom Total Assets
17. Klik header kolom Reported
18. Verifikasi indikator sort Total Assets kembali netral
19. Verifikasi kolom Reported memulai siklus dari menaik (klik pertama): urutan Reported menaik

### TC-FA-TAG-711

20. Buat delapan grup tambahan lewat fixture backend hingga tersimpan, lalu klik menu Fixed Asset > TAG di sidebar (mereset Sort)
21. Verifikasi paginasi tabel grup memuat lebih dari satu halaman
22. Pindah ke halaman 2
23. Klik header kolom Total Assets
24. Verifikasi tabel tetap berada di halaman 2
25. Verifikasi tabel menampilkan urutan baru (Total Assets menaik)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-707, TC-FA-TAG-708, TC-FA-TAG-709, TC-FA-TAG-710, TC-FA-TAG-711). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik sort tiga tahap per kolom ada di spec 174 (TC-FA-TAG-702 s.d. 706) dan spec 175 (TC-FA-TAG-707 s.d. 711).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): langkah 20 (seeding grup tambahan dan reset Sort lewat menu sidebar).
- Temuan untuk QA:
  - TC-FA-TAG-711 mensyaratkan lebih dari 10 baris grup tanpa menyebut cara membentuknya, dan tidak menyebut kolom yang disort; spec memakai Total Assets sesuai langkah TC dan menambah grup tambahan hanya sebelum TC itu agar TC-FA-TAG-707 s.d. 710 tetap pada empat baris dataset.
  - Expected tiap tahap sort pada TC-FA-TAG-707 dan 708 menggabungkan indikator sort dan urutan baris dalam satu butir; spec menulisnya sebagai satu Verifikasi per butir TC.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
