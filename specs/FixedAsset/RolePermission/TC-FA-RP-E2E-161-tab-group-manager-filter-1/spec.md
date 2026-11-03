---
id: TC-FA-RP-E2E-161-tab-group-manager-filter-1
title: "Tab Group Manager: Filter (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-545
  - TC-FA-RP-546
  - TC-FA-RP-547
coverage:
  web: automated
---

# Tab Group Manager: Filter (1/2)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #38 (Tab Group Manager enam baris) dan #18 (pohon group). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Tabel Filter multi-select searchable (TC-FA-RP-546):

| Field | Opsi | Baris yang tampil |
|---|---|---|
| Position | `Network Engineer` | kedua baris Kevin Susanto |
| Division | `General Affairs` | hanya Fajar Nugroho |
| Status | `Inactive` | hanya Lina Marlina |
| Modified By | `Admin Utama` | Lina Marlina dan Cahyo Aji |

## Test Steps

### Screening Filter Panel (TC-FA-RP-545)

1. Klik Tab `Group Manager`
2. Klik ikon Filter
3. Verifikasi Filter Panel memuat field `Position` (`All positions`), `Division` (`All divisions`), `Status` (`All statuses`), `Modified By` (`All users`), dan `Last Updated` (date range picker, `Select date`)
4. Verifikasi Filter Panel memuat field curated `Activation Status`, `Temporary User`, `Temporary Until`, dan Custom Field aktif
5. Verifikasi tidak ada field `Group` pada Filter Panel
6. Verifikasi Sidebar Group Tree tampil sebagai jalur penyaringan group
7. Verifikasi footer Filter Panel memuat `[Clear Field]` dan `[Apply]`
8. Tutup Filter Panel

### Filter multi-select searchable (TC-FA-RP-546)

9. Untuk setiap baris pada Tabel Filter multi-select searchable, lakukan langkah 10 sampai 12
10. Klik ikon Filter, pilih opsi `<Opsi>` pada field `<Field>`, klik `[Apply]`
11. Verifikasi baris yang tampil sesuai kolom "Baris yang tampil" pada tabel
12. Klik ikon Filter, klik `[Clear Field]` lalu `[Apply]`

### Filter date range (TC-FA-RP-547)

13. Catat teks sel Last Updated baris Dimas Pranata
14. Klik ikon Filter, pilih rentang tanggal field Last Updated yang mencakup waktu penugasan Dimas Pranata saja, klik `[Apply]`
15. Verifikasi baris Dimas Pranata tampil
16. Verifikasi hanya baris dengan Last Updated di dalam rentang yang tampil
17. Klik ikon Filter, klik `[Clear Field]` lalu `[Apply]`

## Notes

- Langkah yang diulang: 10 sampai 12 (empat iterasi menurut Tabel Filter multi-select searchable); nominal 17 langkah, ekspansi 26 langkah.
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab, membuka dan menutup Filter Panel, membersihkan Filter (langkah 1, 2, 8, 12, 17); mencatat teks sel (langkah 13).
- Langkah 15 adalah pembanding yang membuktikan sedikitnya satu baris tampil sebelum asersi universal "hanya baris ..." (bagian 8b butir 2); ditambahkan spec.
- Temuan untuk QA:
  - TC-FA-RP-545 Expected b ("penyaringan group hanya lewat Sidebar Group Tree") tidak memuat langkah observasi; spec mengasersi bahwa Sidebar Group Tree tampil (langkah 6).
  - TC-FA-RP-547 meminta rentang tanggal yang mencakup waktu penugasan Dimas Pranata saja, sedangkan Pre-setup #38 hanya menyebut urutan Last Updated tanpa jarak antar baris; filter tanggal berketelitian hari hanya dapat memisahkan Dimas Pranata dari baris lain bila seeding menempatkan penugasannya pada hari berbeda. Spec mengikuti TC dan mengandalkan seeding itu.
  - TC tidak menyebut apakah Filter Panel menutup sesudah `[Apply]`; spec mengasumsikan panel menutup dan dibuka ulang lewat ikon Filter.
  - TC-FA-RP-546 Expected tidak menyebut urutan baris pada hasil dua baris; spec mengasersi himpunan baris.
