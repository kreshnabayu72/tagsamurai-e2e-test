---
id: TC-AC-DS-E2E-100-sort-list-default-tie-breaker-dan-pergantian-kolom
title: "Sort List: Default SKU A-Z, Tie-breaker Deterministik, Pergantian Kolom, dan Tetap di Halaman yang Sama"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-342
  - TC-AC-DS-343
  - TC-AC-DS-344
  - TC-AC-DS-345
coverage:
  web: automated
---

# Sort List: Default SKU A-Z, Tie-breaker Deterministik, Pergantian Kolom, dan Tetap di Halaman yang Sama

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`, Brand `Arcturus`, Current Stock 0; total 129 SKU Principal): hanya dibaca, tidak diubah. Dipasang idempoten oleh seeding di hook `before`. Brand dan Current Stock yang diurutkan memiliki sedikitnya dua nilai distinct di data itu.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat; Sort dipulihkan ke netral di langkah 16.

## Test Steps

### TC-AC-DS-342: Default sort SKU A-Z

1. Verifikasi 10 baris halaman 1 berurutan SKU A-Z: `BLE-KIN-GW1`, `HHR-ARC-100`, `HHR-ARC-200`, `HHR-BIG-01`, `SEED-001`, `SEED-002`, `SEED-003`, `SEED-004`, `SEED-005`, `SEED-006`
2. Verifikasi tidak ada kolom dengan indikator sort aktif selain urutan bawaan SKU A-Z

### TC-AC-DS-343: Tie-breaker deterministik

3. Urutkan kolom Brand Ascending dengan mengklik header kolom Brand sekali
4. Verifikasi baris Brand `Arcturus` yang bernilai sama berurutan menurut default sort SKU A-Z: `HHR-ARC-100`, `HHR-ARC-200`, `SEED-001`, dan seterusnya
5. Pindah ke halaman 2
6. Verifikasi halaman 2 menyambung dari halaman 1 tanpa baris ganda atau terlewat: baris pertama `SEED-009`
7. Pindah ke halaman 1
8. Verifikasi urutan tidak berubah: tiga baris pertama tetap `HHR-ARC-100`, `HHR-ARC-200`, dan `SEED-001`

### TC-AC-DS-344: Mengganti kolom Sort

9. Klik header kolom Current Stock sekali
10. Verifikasi Brand kembali netral (indikator sort nonaktif)
11. Verifikasi Current Stock Ascending aktif

### TC-AC-DS-345: Mengganti Sort tetap di halaman yang sama

12. Klik nomor halaman 3
13. Catat baris pertama halaman 3, lalu klik header kolom Brand sekali
14. Verifikasi nomor halaman aktif tetap 3
15. Verifikasi urutan dataset berubah: baris pertama halaman 3 berbeda dari yang dicatat di langkah 13
16. Klik header kolom Brand dua kali lagi sampai netral

## Notes

- Langkah penghubung (S-03, S-09): langkah 13 mencatat nilai pembanding sebelum sort diganti; langkah 16 memulihkan Sort ke netral; tanpa asersi.
- Langkah 6 dan 8 memakai baris turunan data Pre-setup #29 dan #30 untuk mengamati "tidak ada baris ganda atau terlewat" dan "urutan tidak berubah"; TC tidak menyebut nilai barisnya.
- Temuan untuk QA:
  - S-12: asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `HHR-ARC-100`, `SEED-001` sampai `SEED-006`). Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal masih terbuka.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya bila menutupi layar belum ditetapkan.
