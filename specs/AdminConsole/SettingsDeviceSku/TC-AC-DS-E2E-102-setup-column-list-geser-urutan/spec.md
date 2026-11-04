---
id: TC-AC-DS-E2E-102-setup-column-list-geser-urutan
title: "Setup Column List: Geser Urutan Kolom Kelas SC-A Hideable dan SC-B Curated"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-349
  - TC-AC-DS-352
coverage:
  web: automated
---

# Setup Column List: Geser Urutan Kolom Kelas SC-A Hideable dan SC-B Curated

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima, `totalControlSku_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.AC_DS_TC_PASSWORD` (Pre-setup #1). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Data Pre-setup #29 (SKU Principal inti) dan #30 (`SEED-001` sampai `SEED-119`; total 129 SKU Principal): hanya dibaca, tidak diubah. Dipasang idempoten oleh seeding di hook `before`.
- Urutan awal daftar kolom: `Photo | Device Name | SKU | Category | Brand | Model/Type | Current Stock | Last Modified | Hardware Type | Range Type | TAG Type`.
- Tabel "Geser Hideable" untuk langkah 4 sampai 5 (diproses berurutan dari atas ke bawah; tujuan "tepat di bawah" dihitung dari urutan terkini, sehingga urutan akhir `Last Modified | Photo | Device Name | SKU | Category | Brand | Model/Type | Current Stock`):

| Kolom | Seret ke posisi |
|---|---|
| `Photo` | tepat di bawah `Device Name` |
| `Device Name` | tepat di bawah `SKU` |
| `SKU` | tepat di bawah `Category` |
| `Category` | tepat di bawah `Brand` |
| `Brand` | tepat di bawah `Model/Type` |
| `Model/Type` | tepat di bawah `Current Stock` |
| `Current Stock` | tepat di bawah `Last Modified` |
| `Last Modified` | posisi paling atas daftar |

- Tabel "Geser Curated" untuk langkah 14 sampai 15 (diproses berurutan; urutan akhir ketiganya `TAG Type | Hardware Type | Range Type`):

| Kolom | Seret ke posisi |
|---|---|
| `Hardware Type` | tepat di bawah `Range Type` |
| `Range Type` | tepat di bawah `TAG Type` |
| `TAG Type` | tepat di atas `Hardware Type` |

- Preferensi kolom List: langkah 6 dan 16 menyimpan konfigurasi kolom di cache browser dan langkah 21 sampai 25 memulihkannya ke urutan dan kolom bawaan. Hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Nilai data diacu lewat `Fixture.deviceSku.<kunci>`; berkas fixture disediakan tim FE (lihat Temuan untuk QA).
- Tidak ada state global lain yang diubah dan tidak ada entitas yang dibuat.

## Test Steps

1. Klik header kolom Actions (⋯)
2. Klik `Setup Column...` pada overlay

### TC-AC-DS-349: Geser urutan kolom kelas SC-A Hideable

3. Untuk setiap baris tabel "Geser Hideable", lakukan langkah 4 sampai 5
4. Seret kolom {Kolom} ke posisi {Seret ke posisi} pada daftar
5. Verifikasi urutan kolom {Kolom} pada preview mengikuti hasil drag
6. Klik `[Save]`
7. Verifikasi urutan kolom pada tabel mengikuti hasil seluruh drag: `Last Modified`, `Photo`, `Device Name`, `SKU`, `Category`, `Brand`, `Model/Type`, `Current Stock`
8. Muat ulang halaman dengan F5
9. Verifikasi urutan tersimpan dan tetap berlaku setelah muat ulang
10. Verifikasi tidak ada kolom yang posisinya terkunci

### TC-AC-DS-352: Geser urutan kolom kelas SC-B Curated

11. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
12. Centang kolom `Hardware Type`, `Range Type`, dan `TAG Type` pada popup
13. Untuk setiap baris tabel "Geser Curated", lakukan langkah 14 sampai 15
14. Seret kolom {Kolom} ke posisi {Seret ke posisi} pada daftar
15. Verifikasi urutan kolom {Kolom} pada preview mengikuti hasil drag
16. Klik `[Save]`
17. Verifikasi urutan kolom curated pada tabel mengikuti hasil drag: `TAG Type`, `Hardware Type`, `Range Type`
18. Muat ulang halaman dengan F5
19. Verifikasi urutan tersimpan dan tetap berlaku setelah muat ulang
20. Verifikasi tidak ada kolom yang posisinya terkunci

### Pemulihan state akhir

21. Klik header kolom Actions (⋯), lalu klik `Setup Column...`
22. Seret kolom `Last Modified` ke posisi tepat di bawah `Current Stock` pada daftar
23. Seret kolom `TAG Type` ke posisi tepat di bawah `Range Type` pada daftar
24. Hilangkan centang kolom `Hardware Type`, `Range Type`, dan `TAG Type` pada popup
25. Klik `[Save]`

## Notes

- Langkah 4 sampai 5 diulang untuk delapan baris tabel "Geser Hideable" dan langkah 14 sampai 15 untuk tiga baris tabel "Geser Curated" (ekspansi 16 dan 6 langkah; total spec 41 langkah dengan ekspansi). Parameter tiap iterasi ada di tabel Prerequisites, tanpa langkah bersyarat.
- Alasan melewati sekitar 35 langkah: kedua blok memakai popup Setup Column yang sama dan satu dataset; iterasi per kolom identik dan berdiri sendiri, dan kegagalan satu kolom tidak membuat kolom lain kehilangan makna.
- Langkah penghubung pemulihan (tanpa `Verifikasi`, S-03, S-09): langkah 21 sampai 25 memindahkan `Last Modified` dan `TAG Type` kembali ke posisi awal, menyembunyikan kembali kolom curated, lalu menyimpan; hook `after` tetap menghapus preferensi kolom sebagai cadangan.
- Langkah penghubung (S-03, S-14): langkah 1 sampai 2 dan 11 membuka overlay dan popup; langkah 12 mencentang kolom curated agar urutannya teramati di preview dan tabel (TC-AC-DS-352 tidak memuat langkah ini); tanpa asersi tambahan.
- Temuan untuk QA:
  - TC-AC-DS-349 dan TC-AC-DS-352 menyebut "ke posisi lain" tanpa menetapkan posisi tujuan; posisi pada tabel Prerequisites adalah pilihan spec. Expected "tidak ada kolom yang posisinya terkunci" diasersi melalui seluruh kolom yang dapat diseret.
  - TC-AC-DS-352 mengharapkan urutan kolom curated pada tabel, tetapi kolom curated Hidden secara default dan langkah TC tidak mencentangnya; spec menambah langkah 12.
  - S-12: asersi bergantung pada Pre-setup #29 dan #30. Lampiran A tidak memuat butir modul ini. Spec mengikuti TC dengan seeding idempoten dan suite serial; keputusan pengecualian nama literal masih terbuka.
  - `suite.md` belum mendaftarkan pemulihan konfigurasi kolom yang disimpan spec (konvensi bagian 4); pemulihan lewat penghapusan preferensi kolom di browser membutuhkan kemampuan dari tim FE.
  - Env `AC_DS_TC_PASSWORD` dan berkas fixture `Fixture.deviceSku` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE. Walkthrough tooltip Settings > Device dimiliki modul lain; cara menyetel flag-nya belum ditetapkan.
