---
id: TC-AC-ACHS-E2E-244-tidak-ada-plan-gating-add-stock-per-tier
title: "Tidak Ada Plan Gating: Add Stock Identik pada Tiap Tier Plan"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-578
coverage:
  web: automated
---

# Tidak Ada Plan Gating: Add Stock Identik pada Tiap Tier Plan

## Prerequisites

- Mode: FE+BE.
- Akun default suite: Total Control Principal `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Pre-setup No 1; password `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Tabel "Company per tier" (parameter langkah 2 sampai 9; Pre-setup No 29, lima company Principal): akun Total Control tiap company tidak tertulis di Pre-setup TC dan disediakan tim FE (lihat Temuan untuk QA); password memakai nama env `AC_<ROLE>_PASSWORD` yang ditetapkan tim FE (belum terdaftar).

  | Tier plan | Company | Serial Number yang ditambahkan |
  |---|---|---|
  | Starter | company plan Starter | `SN-PLAN-{runId}-244-ST` |
  | Growth | company plan Growth | `SN-PLAN-{runId}-244-GR` |
  | Professional | company plan Professional | `SN-PLAN-{runId}-244-PR` |
  | Enterprise | company plan Enterprise | `SN-PLAN-{runId}-244-EN` |
  | Custom | company plan Custom | `SN-PLAN-{runId}-244-CU` |

- Data Pre-setup: SKU `{skuFx}` (SKU Smart Fixed Reader dengan 8 unit Available, Pre-setup No 16, Tabel A; nilai persis dibaca dari Tabel A TC, tidak ditulis ulang di spec ini) ada pada katalog tiap company (asumsi; lihat Temuan untuk QA). Data Dinamis: kelima unit di atas dibuat spec ini dan dihapus lewat sesi API aktor tiap company di hook `after` (tetap jalan walau spec gagal di tengah).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{skuFx}` | #16 Tabel A baris 3; #27 | kode SKU Smart Fixed Reader, 8 Available | `Fixture.hardwareStock.p16.a[3].sku` |

- Guided Tooltip: hook suite `before`/`after` menyetel flag seen untuk akun aktor default suite. Flag halaman Stock List akun tiap company disetel true di hook `before` spec ini dan dipulihkan di hook `after`; kemampuan disediakan tim FE/BE.
- Suite serial: `parallel: false` (lihat suite.md).

## Test Steps

### Add Stock pada tiap tier plan

1. Untuk setiap baris tabel "Company per tier" pada Prerequisites, lakukan langkah 2 sampai 9
2. Logout, lalu login sebagai Total Control company pada baris tabel
3. Klik menu Hardware > Stock di sidebar
4. Verifikasi Table Tools Stock List `Search | Filter | Download` tampil tanpa elemen upsell, pesan batas berbeda, atau fitur yang disembunyikan
5. Klik `(⋯)` pada baris `{skuFx}`, klik opsi `Add Stock`
6. Verifikasi halaman Add Stock tampil tanpa elemen upsell, pesan batas berbeda, atau fitur yang disembunyikan
7. Ketik Serial Number pada kolom "Serial Number yang ditambahkan" baris tabel di textarea
8. Klik `[Submit]`
9. Verifikasi toast sukses "Success, unit has been added to stock."

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-578). Tidak ada TC hanya-BE di spec ini.
- Kelas h (state tenant, perubahan plan tier) satu TC, satu spec. Perilaku identik pada lima tier diasersi sebagai perilaku yang sama pada tiap iterasi perulangan langkah 2 sampai 9 (lima iterasi, ekspansi 40 langkah); tidak ada pembanding antar-iterasi selain Expected yang sama.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): Step ganti akun (langkah 2) dan klik menu sidebar. Langkah pembukaan halaman Add Stock lewat row action adalah bagian Langkah Uji TC-578 ("jalankan Add Stock").
- Spec di atas smell 35 langkah setelah ekspansi (40 langkah, 9 langkah nominal). Alasan: satu TC dengan satu alur identik yang diulang per tier, tiap iterasi berdiri sendiri, dan menyebarnya menjadi lima spec menambah login dan hook tanpa pemisah nyata.
- Temuan untuk QA:
  - TC-578 tidak menyebut akun Total Control tiap company (Pre-setup No 29 hanya menyebut lima company dan tier plan); akun dan password disediakan tim FE.
  - Tidak ada literal Pre-setup: SKU dirujuk lewat `{skuFx}` sehingga tidak memerlukan pengecualian S-12. Serial Number `SN-PLAN-*` adalah data buatan spec.
  - TC-578 mensyaratkan SKU `{skuFx}` tersedia pada tiap company; Pre-setup No 29 tidak menyebut katalog SKU tiap company, sehingga ketersediaan SKU diasumsikan.
  - Expected a ("tidak ada upsell, batas berbeda, atau fitur disembunyikan") tidak menyebut elemen yang diperiksa; spec mengasersi Table Tools Stock List dan halaman Add Stock tanpa elemen upsell atau pesan batas.
  - Kemampuan menghapus unit yang dibuat di tiap company (hook `after`) disediakan tim FE/BE.
  - Password akun company memakai nama env `AC_<ROLE>_PASSWORD` yang belum terdaftar; diminta dari tim FE.
