---
id: TC-AC-SG-E2E-106-total-user-agregat-all-groups-user-distinct-bukan-penjumlahan-per-node
title: "Total User dan Total Member Agregat All Groups adalah Distinct, Bukan Penjumlahan per Node"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-32
coverage:
  web: automated
---

# Total User dan Total Member Agregat All Groups adalah Distinct, Bukan Penjumlahan per Node

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak diubah): `Pohon Uji Utama` entitas Principal (#16, 14 group); agregat All Groups "Total User: 10" dan "Total Member: 12" (#17, #19).
- Tabel "Total User per node" (Pre-setup #17), dipakai langkah 1; jumlah seluruh baris 37:

| Node | Total User |
|---|---|
| `Default Group` | 5 |
| `Region A` | 5 |
| `Region B` | 2 |
| `Region C` | 2 |
| `Head Office` | 2 |
| `Warehouse Jakarta` | 3 |
| `Branch 1` | 4 |
| `Branch 2` | 2 |
| `Floor 1` | 2 |
| `Room 301` | 2 |
| `Branch 3` | 2 |
| `Branch 4` | 2 |
| `Finance Dept` | 2 |
| `IT Dept` | 2 |

- Data Dinamis: tidak ada; spec tidak membuat atau mengubah data sehingga tidak ada seeding, suffix `{runId}-106`, maupun cleanup.
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-32: Total User agregat pada All Groups adalah user distinct, bukan penjumlahan per node

1. Untuk setiap baris tabel "Total User per node" (langkah 1): klik node tersebut di Sidebar Group Tree, lalu catat nilai "Total User" pada Group Context Header
2. Verifikasi penjumlahan Total User seluruh 14 node yang dicatat adalah 37
3. Klik root "All Groups (14)"
4. Verifikasi Group Context Header All Groups menampilkan "Total User: 10" (user yang muncul di lebih dari satu node dihitung sekali)
5. Verifikasi Group Context Header All Groups menampilkan "Total Member: 12" (entitas distinct yang ter-assign langsung ke node mana pun)

## Notes

- Langkah 1 diulang untuk 14 baris tabel "Total User per node" (idiom bagian 8b butir 7); dihitung dengan ekspansi spec ini 18 langkah. Memilih node baru memindahkan pilihan secara exclusive, sehingga tidak perlu melepas pilihan di antara iterasi; langkah 3 mengembalikan node `All Groups`.
- Default Sidebar Group Tree: seluruh tree ter-expand (PRD §4.2b), sehingga spec ini tidak memuat langkah expand node.
- Langkah 1 adalah aksi pembacaan tanpa asersi sendiri (nilai per node bukan butir Expected TC); penjumlahan 37 pada langkah 2 adalah Expected a.
- Temuan untuk QA:
  - TC-AC-SG-32 Expected a menyebut "Penjumlahan Total User per node adalah 37" tanpa langkah yang menjumlahkan; langkah 2 dihitung dari nilai yang dicatat pada langkah 1.
