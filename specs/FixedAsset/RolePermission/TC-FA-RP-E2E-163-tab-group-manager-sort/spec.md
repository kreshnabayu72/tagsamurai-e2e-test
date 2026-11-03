---
id: TC-FA-RP-E2E-163-tab-group-manager-sort
title: "Tab Group Manager: Sort"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-549
  - TC-FA-RP-550
  - TC-FA-RP-1062
  - TC-FA-RP-1063
coverage:
  web: automated
---

# Tab Group Manager: Sort

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #38 (Tab Group Manager enam baris), #18 (pohon group), dan #22 (Custom Field). Spec tidak mengubah data; di-seed ulang di hook `before` dan dipulihkan di hook `after`.
- Urutan default sort tabel (Name A-Z): Cahyo Aji, Dimas Pranata, Fajar Nugroho, Kevin Susanto, Kevin Susanto, Lina Marlina.
- Descending pada tiap tabel di bawah adalah urutan ascending dibalik.
- Tabel Sort kelas teks (TC-FA-RP-550):

| Kolom | Urutan ascending |
|---|---|
| Name | Cahyo Aji, Dimas Pranata, Fajar Nugroho, Kevin Susanto (dua baris berdampingan), Lina Marlina |
| Group | `Data Center` (Kevin Susanto), `Head Office` (Lina Marlina), `Helpdesk` (Kevin Susanto), `International Operations Distribution Center` (Cahyo Aji), `IT Infrastructure` (Fajar Nugroho), `Rack A1` (Dimas Pranata) |

- Tabel Sort kolom Position, Division, Status, Modified By, Last Updated (TC-FA-RP-1062):

| Kolom | Urutan ascending |
|---|---|
| Position | Branch Manager (Cahyo Aji), Facility Manager (Fajar Nugroho), IT Support (Dimas Pranata), Network Engineer (Kevin Susanto, dua baris), Regional Coordinator (Lina Marlina) |
| Division | Corporate Affairs (Cahyo Aji), General Affairs (Fajar Nugroho), IT Operations (Dimas Pranata, Kevin Susanto, Kevin Susanto), Operations (Lina Marlina) |
| Status | `Active` (lima baris) lalu `Inactive` (Lina Marlina) |
| Modified By | berdasarkan nama lengkap: Admin Utama (Cahyo Aji, Lina Marlina) lalu Siti Rahmawati (Dimas Pranata, Fajar Nugroho, Kevin Susanto, Kevin Susanto) |
| Last Updated | Oldest First: Lina Marlina, Cahyo Aji, Kevin Susanto (`Helpdesk`), Kevin Susanto (`Data Center`), Dimas Pranata, Fajar Nugroho (descending: Newest First) |

- Tabel Sort kolom curated (TC-FA-RP-1063):

| Kolom | Urutan ascending |
|---|---|
| Email | nilai email berurut A-Z |
| Activation Status | `Activated` (lima baris) lalu `Pending Activation` (Dimas Pranata) |
| Temporary User | `No` (Cahyo Aji, Dimas Pranata, Fajar Nugroho, Lina Marlina) sebelum `Yes` (Kevin Susanto, dua baris) |
| Temporary Until | Oldest First: dua baris Kevin Susanto lebih dulu lalu empat baris tanpa nilai di akhir (descending: Newest First) |
| TAG | Dimas Pranata (`TAG-2001`) lebih dulu lalu lima baris tanpa nilai di akhir; descending: lima baris tanpa nilai di awal lalu Dimas Pranata |
| Cost Center | Fajar Nugroho (`CC-100`), Cahyo Aji (`CC-200`), lalu empat baris tanpa nilai di akhir; descending: empat baris tanpa nilai di awal lalu Cahyo Aji, Fajar Nugroho |
| Joined Date | Oldest First: Fajar Nugroho, Cahyo Aji, lalu empat baris tanpa nilai di akhir (descending: Newest First) |
| Badge No | Fajar Nugroho (`BN-77`), Cahyo Aji (`BN-88`), lalu empat baris tanpa nilai di akhir; descending: empat baris tanpa nilai di awal lalu Cahyo Aji, Fajar Nugroho |

- State yang diubah: konfigurasi kolom Setup Column Tab Group Manager (kolom curated ditampilkan); hook `after` menghapus preferensi kolom di browser, bukan `[Reset to Default]` (kemampuan disediakan tim FE).

## Test Steps

### Sort default (TC-FA-RP-549)

1. Klik Tab `Group Manager`
2. Verifikasi tabel terurut Name A-Z: Cahyo Aji, Dimas Pranata, Fajar Nugroho, Kevin Susanto, Kevin Susanto, Lina Marlina

### Sort siklus tiga state kelas teks (TC-FA-RP-550)

3. Untuk setiap baris pada Tabel Sort kelas teks, lakukan langkah 4 sampai 9
4. Klik header kolom `<Kolom>` sekali
5. Verifikasi klik 1 ascending sesuai urutan pada tabel
6. Klik header kolom `<Kolom>` sekali lagi
7. Verifikasi klik 2 descending (urutan ascending dibalik)
8. Klik header kolom `<Kolom>` sekali lagi
9. Verifikasi klik 3 kembali ke default sort tabel (Name A-Z: Cahyo Aji, Dimas Pranata, Fajar Nugroho, Kevin Susanto, Kevin Susanto, Lina Marlina)

### Sort siklus tiga state kolom Position, Division, Status, Modified By, Last Updated (TC-FA-RP-1062)

10. Untuk setiap baris pada Tabel Sort kolom Position, Division, Status, Modified By, Last Updated, ulangi langkah 4 sampai 9

### Sort siklus tiga state kolom curated (TC-FA-RP-1063)

11. Klik header `(⋯)` kolom Column Visibility, klik `Setup Column...`, centang kolom `Email`, `Activation Status`, `Temporary User`, `Temporary Until`, `TAG`, `Cost Center`, `Joined Date`, dan `Badge No`, lalu klik `[Save]`
12. Untuk setiap baris pada Tabel Sort kolom curated, ulangi langkah 4 sampai 9

## Notes

- Alasan di atas 35 langkah (dengan ekspansi): langkah 4 sampai 9 adalah blok berulang dengan parameter pada tiga tabel Sort (2, 5, dan 8 iterasi); nominal 12 langkah, ekspansi 96 langkah. Seluruh blok berkelas fungsional sama (Sort tabel Tab Group Manager), dataset sama (Pre-setup #38), dan tiap iterasi berdiri sendiri karena siklus tiga klik mengembalikan sort ke default (S-09). Langkah yang diulang: 4 sampai 9 (langkah 10 dan 12 mengulang blok yang sama dengan parameter tabel lain).
- Langkah penghubung (S-03, tanpa `Verifikasi`): klik tab (langkah 1); klik header untuk membangun siklus (langkah 4, 6, 8); membuka Setup Column dan menyimpan (langkah 11).
- Verifikasi pada langkah 5, 7, dan 9 tiap iterasi memetakan klausa "klik 1 ascending", "klik 2 descending", dan "klik 3 kembali ke default" pada Expected (S-01).
- Temuan untuk QA:
  - TC-FA-RP-1063 Expected a (Email) hanya menyebut "nilai email berurut A-Z" tanpa nama baris; spec mengasersi urutan email A-Z pada baris yang tampil.
  - Baris Kevin Susanto muncul dua kali (`Data Center` dan `Helpdesk`) dengan nilai identik pada kolom Name, Position, Division; urutan antar dua baris itu pada sort kolom tersebut tidak ditentukan TC, sehingga spec tidak mengasersi urutan relatif keduanya.
