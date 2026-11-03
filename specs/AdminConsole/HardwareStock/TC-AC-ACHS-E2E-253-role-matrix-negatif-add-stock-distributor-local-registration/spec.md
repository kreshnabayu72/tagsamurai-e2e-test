---
id: TC-AC-ACHS-E2E-253-role-matrix-negatif-add-stock-distributor-local-registration
title: "Role Matrix Negatif: Add Stock Distributor Tanpa Local Registration"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHS-113
  - TC-AC-ACHS-114
coverage:
  web: automated
---

# Role Matrix Negatif: Add Stock Distributor Tanpa Local Registration

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Hook suite (`suite.md`): flag Guided Tooltip halaman Stock List untuk akun aktor suite, sesi API aktor, seeding Population Stock Pre-setup #16 s.d. #20 dan #27. Suite serial (`parallel: false`). Flag Guided Tooltip halaman Stock List untuk kedua akun Distributor di bawah disetel true di hook `before` spec ini dan dipulihkan di hook `after`.
- Login di hook `before` spec ini: Distributor akun `{fullNameSj}` (baris pertama tabel); halaman Hardware > Stock dibuka hook `beforeEach` suite. Akun kedua login lewat Step ganti akun eksplisit (langkah 7); hook `after` mengembalikan sesi ke akun default suite.
- Role yang diuji:

| Role | Akun (Pre-setup) | Env password | Kondisi toggle Local Registration | Blok langkah |
|---|---|---|---|---|
| Distributor Manage hardware stock, toggle nonaktif | `distributorSumberJaya_automated_qaTeam1@qwertysystem.net` (#12) | `Spectra.env.AC_DISTRIBUTOR_SUMBER_JAYA_PASSWORD` | nonaktif sejak awal | langkah 1 sampai 6 (TC-113) |
| Distributor Manage hardware stock, toggle aktif lalu dimatikan Principal | `distributorCakra_automated_qaTeam1@qwertysystem.net` (#10) | `Spectra.env.AC_DISTRIBUTOR_CAKRA_PASSWORD` | aktif, dimatikan sesi API Principal di langkah 13 | langkah 7 sampai 29 (TC-114) |

- Nama env password Distributor mengikuti pola `AC_<ROLE>_PASSWORD` dan ditetapkan tim FE; nama pastinya tidak tertulis di TC (lihat Temuan untuk QA).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{skuFx}` | #16 Tabel A baris 3; #27 | kode SKU Smart Fixed Reader, 8 Available | `Fixture.hardwareStock.p16.a[3].sku` |
| `{snWfa28}` | #17 Tabel E baris N = 28 | Serial Number unit Waiting for Approval SKU Long Range, milik Distributor Pre-setup #12 | `Fixture.hardwareStock.p17.e[28].serialNumber` |
| `{emailCakra}` | #10 | email akun Distributor PT Cakra Distribusi | `Fixture.hardwareStock.account.p10.distributorCakra.email` |
| `{fullNameCakra}` | #10 | nama lengkap user Distributor PT Cakra Distribusi | `Fixture.hardwareStock.account.p10.distributorCakra.fullName` |
| `{fullNameSj}` | #12 | nama lengkap user Distributor PT Sumber Jaya | `Fixture.hardwareStock.account.p12.distributorSumberJaya.fullName` |

- Data Pre-setup (hanya dibaca): SKU `{skuFx}` (Pre-setup #16, #27). `SN-TOG-0001-{runId}-253` (Data Dinamis) diketik tetapi tidak pernah tersimpan.
- Kemampuan teknis (disediakan tim FE/BE): sesi API Principal yang mengubah toggle Local Registration entitas Distributor akun `{fullNameCakra}` (langkah 13 dan 29; aktor pengubah dan endpoint tidak disebut TC, PRD, atau LLD, S-13); pemulihan toggle ke aktif di hook `after`.
- State global: toggle Local Registration entitas Distributor akun `{fullNameCakra}` dimatikan pada langkah 13 dan diaktifkan kembali pada langkah 29 serta hook `after` (walau spec gagal di tengah). Suite berjalan serial.

## Test Steps

### TC-AC-ACHS-113: Toggle Local Registration nonaktif

1. Ketik Search `{skuFx}`, tekan Enter
2. Klik `(⋯)` pada baris SKU `{skuFx}`
3. Verifikasi overlay baris hanya berisi `Detail`
4. Klik row action `Detail` pada baris SKU `{skuFx}`
5. Verifikasi tombol `[Add Stock]` Hidden di toolbar Tab Available
6. Verifikasi Stock Detail dan Tab Available SKU terbuka (pembacaan stok Local Registration yang sudah ada tetap tersedia)

### TC-AC-ACHS-114: Toggle dimatikan Principal setelah form dibuka

7. Logout, lalu login sebagai Distributor `{emailCakra}` (`Spectra.env.AC_DISTRIBUTOR_CAKRA_PASSWORD`)
8. Buka Hardware > Stock lewat sidebar
9. Ketik Search `{skuFx}`, tekan Enter
10. Klik `(⋯)` pada baris SKU `{skuFx}`
11. Klik opsi `Add Stock`
12. Ketik `SN-TOG-0001-{runId}-253` tanpa Submit
13. Nonaktifkan toggle Local Registration entitas Distributor akun `{fullNameCakra}` lewat sesi API Principal hingga toggle nonaktif tersimpan
14. Klik `[Submit]`
15. Verifikasi toast error "You don't have permission to do this."
16. Verifikasi halaman tetap Add Stock (Breadcrumb `Hardware > Stock > Add Stock`, tidak ada redirect)
17. Klik segmen `Stock` pada breadcrumb
18. Verifikasi dialog Unsaved Changes tampil
19. Klik `[Leave]`
20. Ketik Search `{skuFx}`, tekan Enter
21. Klik `(⋯)` pada baris SKU `{skuFx}`
22. Verifikasi overlay baris memuat `Detail` dan tidak memuat opsi `Add Stock` (row action `Add Stock` Hidden)
23. Klik row action `Detail` pada baris SKU `{skuFx}`
24. Verifikasi tombol `[Add Stock]` Hidden di toolbar Tab Available
25. Verifikasi Tab Available akun `{fullNameCakra}` menampilkan sedikitnya satu baris
26. Ketik Search `SN-TOG-0001-{runId}-253` pada Tab Available, tekan Enter
27. Verifikasi tidak ada unit tersimpan: hasil Search menampilkan empty state `No results found`
28. Tunggu aksi selesai
29. Aktifkan kembali toggle Local Registration entitas Distributor akun `{fullNameCakra}` lewat sesi API Principal hingga toggle aktif tersimpan

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-113, 114). Tidak ada TC hanya-BE di spec ini.
- Spec Role Matrix negatif ditulis per blok role karena langkah tiap role berbeda dan ganti akun menuntut Step eksplisit. Pelaku Principal pada TC-114 memakai sesi API (pelaku kedua yang hanya mengubah state), bukan konteks UI kedua, sehingga tanpa `P-2`.
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (langkah 1, 9, 20, 26), logout dan login (langkah 7), buka Hardware > Stock (langkah 8), pengetikan tanpa Submit (langkah 12), `Tunggu aksi selesai` sebelum memulihkan state (langkah 28), dan pemulihan toggle (langkah 29). Langkah 17 sampai 19 menutup form dirty secara deterministik (S-08); `Verifikasi` dialog Unsaved Changes pada langkah 18 adalah wajib S-08.
- Expected TC-114 butir b ("tidak ada unit tersimpan") diamati pada langkah 25 sampai 27 sesudah form ditutup (form yang menolak Submit tidak menampilkan daftar unit); `Verifikasi` hidden elemen UI memakai overlay baris dan halaman yang sudah termuat sebagai anchor permukaan (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-113 Expected c ("Pembacaan stok Local Registration yang sudah ada tetap tersedia") tidak menyebut data stok apa yang harus tampil untuk akun `{fullNameSj}` pada SKU {skuFx}; Pre-setup #12 hanya menyebut unit WFA `{snWfa28}`. Spec mengasersi Stock Detail dan Tab Available terbuka.
  - TC-114 langkah 6 memuat langkah bersyarat ("bila dialog Unsaved Changes tampil"); spec mengasersi dialog tampil karena form berisi `SN-TOG-0001` (S-08).
  - Nama env password Distributor tidak tertulis di TC; disediakan tim FE.
  - TC-113 dan TC-114 tidak memuat Post Condition.
