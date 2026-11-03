---
id: TC-AC-DS-E2E-098-sort-list-alfabetis-tiga-tahap-dan-current-stock-numerik
title: "Sort List: Alfabetis Tiga Tahap dan Current Stock Numerik"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-336
  - TC-AC-DS-337
coverage:
  web: automated
---

# Sort List: Alfabetis Tiga Tahap dan Current Stock Numerik

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`, Current Stock 0; total 129 SKU Principal, 13 halaman pada 10 baris per halaman): hanya dibaca, tidak diubah. Dipasang idempoten oleh seeding di hook `before`. Setiap kolom yang diuji memiliki sedikitnya dua nilai distinct di data itu.
- Tabel "Sort Curated" untuk langkah 14 sampai 17:

| Kolom | Baris pertama Ascending | Baris pertama Descending |
|---|---|---|
| Category | badge `Asset TAG` (tie-breaker SKU: `SEED-001`) | badge `Wearable TAG` (`TAG-ARC-USR`) |
| Brand | badge `Arcturus` | badge `Veltrix` (`SFR-VEL-4P`, `SFR-ZERO-01`) |
| Model/Type | `GW-1` (`BLE-KIN-GW1`) | `T-USR` (`TAG-ARC-USR`) |

- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global yang diubah dan tidak ada entitas yang dibuat; Sort dipulihkan ke netral di langkah 24 dan oleh klik sidebar hook `beforeEach` suite.

## Test Steps

### TC-AC-DS-336: Sort alfabetis tiga tahap

1. Klik header kolom Device Name sekali
2. Verifikasi Ascending: baris pertama `SFR-VEL-4P` (`4-Port Fixed Reader`), lalu `anggur sensor` dan `Apel sensor` (tidak membedakan huruf besar-kecil)
3. Klik header kolom Device Name sekali lagi
4. Verifikasi Descending: baris pertama `TAG-ARC-USR` (`Wearable TAG`)
5. Klik header kolom Device Name sekali lagi
6. Verifikasi kembali ke urutan default SKU A-Z: baris pertama `BLE-KIN-GW1`
7. Klik header kolom SKU sekali
8. Verifikasi Ascending: baris pertama `BLE-KIN-GW1`
9. Klik header kolom SKU sekali lagi
10. Verifikasi Descending: baris pertama `TAG-ARC-USR`
11. Klik header kolom SKU sekali lagi
12. Verifikasi kembali ke urutan default SKU A-Z: baris pertama `BLE-KIN-GW1`
13. Untuk setiap baris tabel "Sort Curated", lakukan langkah 14 sampai 17
14. Klik header kolom {Kolom} sekali
15. Verifikasi Ascending: baris pertama {Baris pertama Ascending}
16. Klik header kolom {Kolom} sekali lagi
17. Verifikasi Descending: baris pertama {Baris pertama Descending}

### TC-AC-DS-337: Sort Current Stock numerik natural

18. Klik header kolom Current Stock sekali
19. Pindah ke halaman 13 (halaman terakhir)
20. Verifikasi Ascending: halaman 13 menutup dengan nilai `8`, `36`, `120`, `500`, `12500` berurutan numerik (bukan urutan teks)
21. Klik header kolom Current Stock sekali lagi
22. Pindah ke halaman 1
23. Verifikasi Descending: halaman 1 dimulai `12500`, `500`, `120`, `36`, `8` lalu baris berstok `0`
24. Klik header kolom Current Stock sekali lagi
25. Verifikasi kembali ke urutan default SKU A-Z: baris pertama `BLE-KIN-GW1`

## Notes

- Langkah 14 sampai 17 diulang untuk tiga baris tabel "Sort Curated" (ekspansi 12 langkah; total spec 32 langkah dengan ekspansi). Parameter tiap iterasi ada di tabel Prerequisites, tanpa langkah bersyarat.
- Langkah penghubung (S-03, S-14): langkah 19 dan 22 memindahkan halaman agar asersi "halaman terakhir" dan "halaman 1" menunjuk halaman yang benar (mengganti arah sort tetap di halaman yang sama); tanpa asersi.
- Klik ketiga kolom Category, Brand, dan Model/Type tidak ditulis karena TC tidak memberi Expected untuknya; klik header kolom berikutnya mengembalikan kolom sebelumnya ke netral.
- Sumber TC-AC-DS-338 (Sort Last Modified) ada di spec TC-AC-DS-E2E-191.
- Temuan untuk QA:
  - S-12: asersi bergantung pada nama literal Pre-setup #29 dan #30 (mis. `BLE-KIN-GW1`, Current Stock `12500`, total 129 SKU). Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal masih terbuka.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya bila menutupi layar belum ditetapkan.
