---
id: TC-FA-RP-E2E-143-tab-total-control-sort-1
title: "Tab Total Control: Sort (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-496
  - TC-FA-RP-497
  - TC-FA-RP-498
  - TC-FA-RP-499
coverage:
  web: automated
---

# Tab Total Control: Sort (1/2)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #36 (Tab Total Control terisi sembilan baris; tiap kolom yang di-sort memiliki dua nilai distinct atau lebih) dan #37 (Tab Read Only empat baris). Spec ini tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Konfigurasi kolom Setup Column disimpan di browser; hook `after` menghapus preferensi kolom di browser (kemampuan disediakan tim FE).
- Default sort tabel: Name A-Z (Admin Utama, Ahmad Fauzi, Budi Santoso, Eka Saputra, Fitri Handayani, Rina Wulandari, Rudi Hartono, Siti Rahayu, Siti Rahmawati).
- Tabel Sort kolom teks (TC 497):

| Kolom | Urutan ascending |
|---|---|
| Name | Admin Utama, Ahmad Fauzi, Budi Santoso, Eka Saputra, Fitri Handayani, Rina Wulandari, Rudi Hartono, Siti Rahayu, Siti Rahmawati |
| Position | Asset Custodian (Ahmad), Facility Officer (Eka), Finance Officer (Fitri, Siti Rahmawati), Finance Supervisor (Rudi), HR Manager (Siti Rahayu), `Operations Manager, Region 1` (Rina), System Administrator (Admin Utama), Warehouse Staff (Budi) |
| Division | Accounting & Tax (Siti Rahmawati), `Asset Management "North"` (Rina), Finance (Fitri, Rudi), General Affairs (Eka), HR (Siti Rahayu), IT Operations (Admin Utama), Logistics (Ahmad, Budi) |
| Modified By | Admin Utama (Rina, Siti Rahmawati), Prasetyo Hadi (Budi, Fitri), Siti Rahmawati (Ahmad, Eka, Rudi, Siti Rahayu), System (Admin Utama), berdasarkan nama lengkap |

- Tabel Sort kolom badge (TC 498 dan TC 499):

| Kolom | Urutan ascending |
|---|---|
| Status | `Active` (delapan baris urut Name) lalu `Inactive` (Siti Rahayu) |
| Activation Status | `Activated` (tujuh baris) lalu `Pending Activation` (Eka Saputra) lalu `Pending Email Confirmation` (Fitri Handayani) |
| Temporary User | `No` (delapan baris) sebelum `Yes` (Rudi Hartono) |

## Test Steps

### Sort default dan ikon sort (TC 496)

1. Verifikasi tabel terurut Name A-Z (default): Admin Utama, Ahmad Fauzi, Budi Santoso, Eka Saputra, Fitri Handayani, Rina Wulandari, Rudi Hartono, Siti Rahayu, Siti Rahmawati.
2. Verifikasi ikon sort terlihat pada kolom bersortir.
3. Verifikasi header kolom Column Visibility tidak punya ikon sort.

### Siklus tiga state kelas teks (TC 497)

4. Untuk setiap kolom pada Tabel Sort kolom teks, lakukan langkah 5 sampai 10.
5. Klik header kolom sekali.
6. Verifikasi baris terurut ascending sesuai Tabel Sort kolom teks.
7. Klik header kolom kedua kali.
8. Verifikasi baris terurut descending (nilai kolom itu berurutan terbalik dari ascending).
9. Klik header kolom ketiga kali.
10. Verifikasi urutan kembali ke default sort tabel (Name A-Z).

### Siklus tiga state kelas badge dan kolom Temporary User (TC 498 dan TC 499)

11. Tampilkan kolom Activation Status dan Temporary User lewat Setup Column, lalu klik `[Save]`.
12. Untuk setiap kolom pada Tabel Sort kolom badge, lakukan langkah 13 sampai 18.
13. Klik header kolom sekali.
14. Verifikasi baris terurut ascending sesuai Tabel Sort kolom badge.
15. Klik header kolom kedua kali.
16. Verifikasi baris terurut descending (urutan kelompok nilai terbalik dari ascending).
17. Klik header kolom ketiga kali.
18. Verifikasi urutan kembali ke default sort tabel (Name A-Z).
19. Sembunyikan kolom Activation Status dan Temporary User lewat Setup Column, lalu klik `[Save]`.

## Notes

- Alasan di atas 35 langkah: langkah 5 sampai 10 (empat iterasi) dan langkah 13 sampai 18 (tiga iterasi) adalah blok berulang dengan parameter pada tabel Prerequisites; seluruh blok berkelas fungsional sama, dataset sama, dan tiap kolom berdiri sendiri karena klik ketiga mengembalikan tabel ke default. Langkah yang diulang: 5 sampai 10 dan 13 sampai 18.
- Tabel Sort kolom badge memuat kolom Status dan Activation Status (TC 498) serta Temporary User (TC 499).
- Langkah penghubung (S-03): langkah 4, 5, 7, 9, 11, 12, 13, 15, 17, dan 19. Langkah 11 menampilkan kolom Activation Status dan Temporary User (kolom curated yang disembunyikan secara default) lewat Setup Column sebelum header di-klik, sesuai langkah TC 498 dan TC 499; langkah 19 memulihkan kolom (S-09).
- Temuan untuk QA:
  - TC 497 dan TC 498 hanya merinci urutan ascending; urutan descending tidak merinci posisi baris bernilai sama sehingga diasersi pada tingkat nilai kolom, bukan urutan baris sama nilai.
