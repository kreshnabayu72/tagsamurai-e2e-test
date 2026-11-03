---
id: TC-FA-RP-E2E-178-tabel-role-transaksi-search-filter-dan-sort-2
title: "Tabel Role Transaksi: Search, Filter, dan Sort (2/4)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-596
  - TC-FA-RP-597
  - TC-FA-RP-598
  - TC-FA-RP-599
coverage:
  web: automated
---

# Tabel Role Transaksi: Search, Filter, dan Sort (2/4)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #40 (tabel Role Transaksi `IT Infrastructure` sub-tab `Disposal`, section Asset Admin: Nadia Putri, Ahmad Fauzi, Dimas Pranata) dan #18 (pohon group). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Urutan default sort tabel (Name A-Z): Ahmad Fauzi, Dimas Pranata, Nadia Putri.
- Tabel Filter multi-select searchable (TC-FA-RP-596):

| Field | Opsi | Baris yang tampil |
|---|---|---|
| Position | `IT Support` | hanya Dimas Pranata |
| Division | `Logistics` | Nadia Putri dan Ahmad Fauzi |

- Tabel Sort kelas teks (TC-FA-RP-599; descending adalah urutan ascending dibalik):

| Kolom | Urutan ascending |
|---|---|
| Name | Ahmad Fauzi, Dimas Pranata, Nadia Putri |
| Position | Asset Custodian (Ahmad Fauzi), Asset Staff (Nadia Putri), IT Support (Dimas Pranata) |
| Division | IT Operations (Dimas Pranata), Logistics (Ahmad Fauzi, Nadia Putri) |

## Test Steps

1. Klik Tab `Transaction Role`
2. Klik node `IT Infrastructure` di Sidebar Group Tree, lalu klik sub-tab `Disposal`
3. Buka section `Asset Admin`

### Filter multi-select searchable (TC-FA-RP-596)

4. Untuk setiap baris pada Tabel Filter multi-select searchable, lakukan langkah 5 sampai 7
5. Klik ikon Filter, pilih opsi `<Opsi>` pada field `<Field>`, klik `[Apply]`
6. Verifikasi baris yang tampil sesuai kolom "Baris yang tampil" pada tabel
7. Klik ikon Filter, klik `[Clear Field]` lalu `[Apply]`

### Isi opsi dropdown Filter (TC-FA-RP-597)

8. Klik ikon Filter
9. Buka dropdown field Position
10. Verifikasi opsi Position: `Asset Staff`, `Asset Custodian`, `IT Support` (hanya nilai pada baris section itu)
11. Buka dropdown field Division
12. Verifikasi opsi Division: `Logistics`, `IT Operations` (hanya nilai pada baris section itu)
13. Tutup Filter Panel

### Sort default (TC-FA-RP-598)

14. Verifikasi tabel terurut Name A-Z: Ahmad Fauzi, Dimas Pranata, Nadia Putri

### Sort siklus tiga state kelas teks (TC-FA-RP-599)

15. Untuk setiap baris pada Tabel Sort kelas teks, lakukan langkah 16 sampai 21
16. Klik header kolom `<Kolom>` sekali
17. Verifikasi klik 1 ascending sesuai urutan pada tabel
18. Klik header kolom `<Kolom>` sekali lagi
19. Verifikasi klik 2 descending (urutan ascending dibalik)
20. Klik header kolom `<Kolom>` sekali lagi
21. Verifikasi klik 3 kembali ke default sort tabel (Name A-Z: Ahmad Fauzi, Dimas Pranata, Nadia Putri)

## Notes

- Langkah yang diulang: 5 sampai 7 (dua iterasi) dan 16 sampai 21 (tiga iterasi); nominal 21 langkah, ekspansi 36 langkah.
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab, node, sub-tab, dan section (langkah 1, 2, 3); membuka dan menutup Filter Panel serta dropdown (langkah 7, 8, 9, 11, 13); klik header kolom (langkah 16, 18, 20).
- Asersi "hanya baris X" menyebut nama baris yang tampil sehingga baris itu sendiri menjadi anchor positif (bagian 8b butir 2).
- Temuan untuk QA:
  - Langkah Uji TC-FA-RP-596 sampai TC-FA-RP-599 tidak menyebut section yang dibuka, sedangkan judul menyebut section Asset Admin; spec membuka section `Asset Admin` (langkah 3) seperti Langkah Uji TC-FA-RP-1071.
  - TC-FA-RP-597 langkah 3 meminta membuka dropdown "tiap field multi-select" tetapi Expected hanya menyebut Position dan Division; spec mengasersi kedua field itu.
  - TC-FA-RP-596 Expected b menyebut baris Nadia Putri dan Ahmad Fauzi tanpa urutan; spec mengasersi himpunan baris.
  - TC tidak menyebut apakah Filter Panel menutup sesudah `[Apply]`; spec mengasumsikan panel menutup dan dibuka ulang lewat ikon Filter.
