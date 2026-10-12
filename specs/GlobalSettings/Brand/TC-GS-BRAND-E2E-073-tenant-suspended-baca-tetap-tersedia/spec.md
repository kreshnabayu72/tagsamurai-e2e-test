---
id: TC-GS-BRAND-E2E-073-tenant-suspended-baca-tetap-tersedia
title: "Baca Data Brand Tetap Tersedia saat Client Suspended"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-BRAND-241
coverage:
  web: automated
---

# Baca Data Brand Tetap Tersedia saat Client Suspended

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji:

  | Peran dalam spec | Role | Email | Environment variable password |
  |---|---|---|---|
  | Aktor UI | Total Control Client A (Sari Dewi, `Sari D`) | `totalControl_automated_qaTeam1@qwertysystem.net` | `GS_TC_PASSWORD` |
  | Pengubah status Client A (hanya lewat API, tanpa login UI) | Total Control (Principal, Hendra Wijaya) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `GS_PRINCIPAL_TC_PASSWORD` |

  Login aktor UI di hook `before` spec ini; akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Master Reference > Brand.
- Environment variable: `GS_TC_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (hanya dibaca, tanpa suffix `{runId}`): `Vertex Labs` (FAMS Laptop dan Monitor; Supply Printer Ink, Scanner Paper, Toner Cartridge).
- Spec tidak membuat atau mengubah data, sehingga tidak ada seeding dan cleanup data.
- Kemampuan teknis: mengubah status Client A menjadi Suspended lewat API dengan sesi akun Total Control (Principal) di atas; akun itu harus berhak mengubah status Client A dan endpoint ubah status harus tersedia bagi tim FE (kebutuhan fixture/FE yang belum terkonfirmasi). Perubahan status dilakukan sebagai langkah eksplisit di spec.
- Syarat eksekusi: status Client A diubah untuk seluruh tenant, sehingga spec ini dijalankan sendiri pada tahap atau suite terpisah tanpa spec Client A lain yang berjalan bersamaan (konvensi bagian 3: urutan suite paralel tidak dijamin); spec Client A lain berjalan sebelum atau sesudahnya saat Client A Active.
- State global yang dipulihkan (hook `after`, tetap jalan walau spec gagal di tengah): status Client A dikembalikan ke Active lewat API dengan akun yang sama.
- TC-GS-BRAND-241: login sebagai Total Control dan berada di Global Settings > Master Reference > Brand; Client A berstatus Suspended.

## Test Steps

### TC-GS-BRAND-241: Baca data tetap tersedia saat entitas suspended

1. Ubah status Client A menjadi Suspended (lewat API dengan akun Total Control Principal)
2. Muat ulang halaman Global Settings > Master Reference > Brand
3. Buka Tab Brand
4. Verifikasi tabel Brand tampil normal
5. Search `Vertex Labs`
6. Buka Detail Vertex Labs
7. Verifikasi Detail Vertex Labs tampil normal

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`. Kelas state tenant (prinsip 13h) verifikasi baca murni, dipisah dari write-lockdown di spec `TC-GS-BRAND-E2E-072-tenant-suspended-expired-write-lockdown`.
- "Tampil normal" mengikuti Expected Result TC (tabel dan Detail tampil); perilaku detail kolom dan isi Detail dicakup spec screening lain, tidak diulang di sini.
- Langkah penghubung: langkah 2 (memuat ulang halaman setelah status Client A berubah, supaya halaman memakai status terbaru) dan langkah 5 (Search `Vertex Labs` supaya baris berada di tabel yang terlihat sebelum Detail dibuka). Langkah 1 (mengubah status Client A) adalah prasyarat TC (Client A berstatus Suspended) yang dijadikan langkah eksplisit.
- Akun pengubah status, hak ubahnya, dan endpoint-nya sudah dicatat sebagai kebutuhan di Prerequisites.
