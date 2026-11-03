---
id: TC-FA-RP-E2E-162-tab-group-manager-filter-2
title: "Tab Group Manager: Filter (2/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-548
  - TC-FA-RP-1066
  - TC-FA-RP-1067
coverage:
  web: automated
---

# Tab Group Manager: Filter (2/2)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #38 (Tab Group Manager enam baris), #18 (pohon group), dan #22 (Custom Field `Cost Center`, `Joined Date`, `Badge No`). Tanggal Temporary Until Kevin Susanto dan Joined Date Cahyo Aji (15/02/26) dibaca dari fixture. Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Tabel Filter kolom curated (TC-FA-RP-1066):

| Field | Opsi | Baris yang tampil |
|---|---|---|
| Activation Status | `Pending Activation` | hanya Dimas Pranata |
| Temporary User | `Yes` | kedua baris Kevin Susanto |
| Cost Center | `CC-200` | hanya Cahyo Aji |

## Test Steps

### Isi opsi dropdown Filter (TC-FA-RP-548)

1. Klik Tab `Group Manager`
2. Klik ikon Filter
3. Buka dropdown field Position
4. Verifikasi opsi Position: `Facility Manager`, `Network Engineer`, `Regional Coordinator`, `IT Support`, dan `Branch Manager` (jabatan Cahyo Aji; hanya nilai yang ada pada baris tabel)
5. Buka dropdown field Status
6. Verifikasi opsi Status: `Active`, `Inactive`
7. Tutup Filter Panel

### Filter multi-select searchable kolom curated (TC-FA-RP-1066)

8. Untuk setiap baris pada Tabel Filter kolom curated, lakukan langkah 9 sampai 11
9. Klik ikon Filter, pilih opsi `<Opsi>` pada field `<Field>`, klik `[Apply]`
10. Verifikasi baris yang tampil sesuai kolom "Baris yang tampil" pada tabel
11. Klik ikon Filter, klik `[Clear Field]` lalu `[Apply]`

### Filter date range kolom curated (TC-FA-RP-1067)

12. Klik ikon Filter, pilih rentang tanggal field Temporary Until yang mencakup tanggal Temporary Until Kevin Susanto, klik `[Apply]`
13. Verifikasi kedua baris Kevin Susanto tampil
14. Klik ikon Filter, klik `[Clear Field]` lalu `[Apply]`
15. Klik ikon Filter, pilih rentang tanggal field Joined Date yang mencakup Joined Date Cahyo Aji saja, klik `[Apply]`
16. Verifikasi hanya baris Cahyo Aji yang tampil
17. Klik ikon Filter, klik `[Clear Field]` lalu `[Apply]`

## Notes

- Langkah yang diulang: 9 sampai 11 (tiga iterasi menurut Tabel Filter kolom curated); nominal 17 langkah, ekspansi 23 langkah.
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab, membuka dan menutup Filter Panel, membuka dropdown, membersihkan Filter (langkah 1, 2, 3, 5, 7, 11, 14, 17).
- Asersi "hanya baris X" menyebut nama baris yang tampil sehingga baris itu sendiri menjadi anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-RP-548 langkah 3 meminta membuka dropdown "tiap field multi-select" tetapi Expected hanya menyebut opsi Position dan Status; spec hanya mengasersi kedua field itu (Division dan Modified By tidak diasersi).
  - TC-FA-RP-548 Expected a menyebut "jabatan Cahyo Aji" tanpa nama jabatan; spec memakai `Branch Manager` dari Pre-setup #38 dan TC-FA-RP-1062.
  - TC-FA-RP-1067 Expected a menulis "kedua baris Kevin Susanto yang tampil"; spec mengasersi kedua baris Kevin Susanto tampil (tanpa klaim "hanya").
  - TC tidak menyebut apakah Filter Panel menutup sesudah `[Apply]`; spec mengasumsikan panel menutup dan dibuka ulang lewat ikon Filter.
