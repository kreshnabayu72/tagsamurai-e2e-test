---
id: TC-FA-TAG-E2E-047-bulk-action-bar-dan-kebab-aksi-grup-visibilitas-dan-seleksi-bagian-2
title: "Seleksi Checkbox Header dan Select All, Tabel Grup Tanpa Bulk Action, serta Kebab Aksi Grup"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-206
  - TC-FA-TAG-207
  - TC-FA-TAG-208
  - TC-FA-TAG-209
  - TC-FA-TAG-210
  - TC-FA-TAG-211
coverage:
  web: automated
---

# Seleksi Checkbox Header dan Select All, Tabel Grup Tanpa Bulk Action, serta Kebab Aksi Grup

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji:

| Role | Kode | Email (Pre-setup TC) | Env password | Blok |
|---|---|---|---|---|
| Total Control | TC | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` | TC-FA-TAG-206 sampai TC-FA-TAG-210 |
| Read Only | RO | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_RO_PASSWORD` | TC-FA-TAG-211 |

- Nama env password usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`. Login Total Control di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` untuk kedua akun, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script.
- Data Pre-setup tab Paired (tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah): grup Excavator 20 Ton / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. Grup Excavator 20 Ton / Plant B memuat 20 aset (page size default 10, sehingga halaman 2 berisi 10 aset).
- Kemampuan teknis (disediakan tim FE/BE): seed idempotent dan pemulihan aset dan Tag lewat fixture backend (lihat `suite.md`).
- Pemulihan di hook `after`: kembalikan data Pre-setup tab Paired ke keadaan awal bila seeding mengubahnya. Spec ini tidak mengubah data bisnis.
- State global: tidak ada. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-206: checkbox header memilih baris halaman aktif

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B
2. Centang checkbox header kolom Checkbox
3. Verifikasi 10 baris halaman aktif tercentang
4. Pindah ke halaman 2 pada Pagination Popup Detail
5. Verifikasi tabel halaman 2 memuat sedikitnya satu baris
6. Verifikasi baris halaman lain tidak tercentang
7. Pindah ke halaman 1 pada Pagination Popup Detail
8. Verifikasi Bulk Action Bar tampil dengan jumlah 10

### TC-FA-TAG-207: Select All lintas halaman

9. Klik ikon `×` di sisi kanan Bulk Action Bar
10. Centang satu baris
11. Klik tombol `Select All (20 records)`
12. Verifikasi seluruh 20 aset terpilih lintas halaman
13. Verifikasi tombol berubah menjadi `Unselect All`
14. Klik tombol `Unselect All`, lalu tutup Popup Detail

### TC-FA-TAG-208: tabel grup tanpa Bulk Action

15. Verifikasi tabel grup T-TAG-01 memuat sedikitnya satu baris grup
16. Verifikasi tabel grup tidak punya kolom checkbox maupun Bulk Action Bar

### TC-FA-TAG-209 dan TC-FA-TAG-210: kebab aksi grup

17. Klik kebab baris Forklift Manual / Plant A (Non-standard 3)
18. Verifikasi aksi `Detail` (ikon `FileInfoLine`, dark) lalu `Replace non-standard TAGs` (ikon `ReplaceTag`, dark) tampil
19. Tutup kebab
20. Klik kebab baris Excavator 20 Ton / Plant A (Non-standard 0)
21. Verifikasi kebab hanya memuat `Detail`; `Replace non-standard TAGs` tidak tampil
22. Tutup kebab

### TC-FA-TAG-211: kebab grup Read Only

23. Ganti akun: Logout dari akun Total Control, login sebagai Read Only, lalu buka Fixed Asset > TAG tab Paired
24. Klik kebab baris Forklift Manual / Plant A
25. Verifikasi kebab hanya memuat `Detail`

## Notes

- Mode: FE+BE. Subjudul `###` memetakan langkah ke id TC granular. Blok TC-FA-TAG-211 ditulis sebagai blok role tersendiri karena ganti akun menuntut langkah eksplisit (bagian 3a).
- Langkah penghubung (tanpa awalan `Verifikasi`): 4 dan 7 (pindah halaman untuk memeriksa halaman lain), 9 (membersihkan seleksi, S-09), 14 (menutup Popup Detail sesudah `Unselect All`), 19 dan 22 (menutup kebab), 23 (ganti akun).
- Asersi tambahan di luar Expected TC (S-03): langkah 5 (baris halaman 2 tampil sebagai anchor untuk "tidak tercentang" langkah 6, bagian 8b butir 2); langkah 15 (baris grup tampil sebagai anchor untuk absence langkah 16). Langkah 21: Expected TC-FA-TAG-210 "hanya memuat Detail" sudah memuat `Detail` sebagai anchor positif.
- Temuan untuk QA:
  - TC-FA-TAG-206 Expected a ("baris halaman lain tidak tercentang") tidak menyebut apakah seleksi bertahan saat pindah halaman; spec mengasersi baris halaman 2 tidak tercentang setelah halaman 1 dicentang (langkah 6).
  - TC-FA-TAG-206 dan TC-FA-TAG-207 tidak menyebut Popup Detail dibuka dari grup mana selain "baris Plant B"; spec memakai grup Excavator 20 Ton / Plant B (20 aset).
  - Nilai literal Pre-setup (Asset Name, ID aset) tidak bisa bersuffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; Lampiran A belum memuat butir untuk modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
