---
id: TC-GS-BRAND-E2E-072-tenant-suspended-expired-write-lockdown
title: "Write Lockdown Brand saat Client Suspended atau Expired: Create, Edit, Delete, dan Bulk Delete Ditolak"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-BRAND-239
  - TC-GS-BRAND-240
  - TC-GS-BRAND-244
coverage:
  web: automated
---

# Write Lockdown Brand saat Client Suspended atau Expired: Create, Edit, Delete, dan Bulk Delete Ditolak

## Prerequisites

- Mode: FE+BE.
- Akun yang diuji:

  | Peran dalam spec | Role | Email | Environment variable password |
  |---|---|---|---|
  | Aktor UI | Total Control Client A (Sari Dewi, `Sari D`) | `totalControl_automated_qaTeam1@qwertysystem.net` | `GS_TC_PASSWORD` |
  | Pengubah status Client A (hanya lewat API, tanpa login UI) | Total Control (Principal, Hendra Wijaya) | `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` | `GS_PRINCIPAL_TC_PASSWORD` |

  Login aktor UI di hook `before` spec ini; akun ini adalah akun default suite, sehingga hook `after` tidak perlu memulihkan sesi. Halaman awal: Global Settings > Master Reference > Brand.
- Environment variable: `GS_TC_PASSWORD`, `GS_PRINCIPAL_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Data Pre-setup Client A (tetap di environment, tidak berubah karena semua aksi tulis ditolak, tanpa suffix `{runId}`): `Orion Tech` dan `Brightway` (keduanya bebas relasi).
- Data dinamis: tidak ada. Input `Frozen Co` dan `Orion E` adalah input yang submit-nya ditolak sehingga tidak membuat data.
- Kemampuan teknis: mengubah status Client A menjadi Suspended dan Expired lewat API dengan sesi akun Total Control (Principal) di atas; akun itu harus berhak mengubah status Client A dan endpoint ubah status harus tersedia bagi tim FE (kebutuhan fixture/FE yang belum terkonfirmasi). Perubahan status dilakukan sebagai langkah eksplisit di spec.
- Syarat eksekusi: status Client A diubah untuk seluruh tenant, sehingga spec ini dijalankan sendiri pada tahap atau suite terpisah tanpa spec Client A lain yang berjalan bersamaan (konvensi bagian 3: urutan suite paralel tidak dijamin); spec Client A lain berjalan sebelum atau sesudahnya saat Client A Active.
- State global yang dipulihkan (hook `after`, tetap jalan walau spec gagal di tengah): status Client A dikembalikan ke Active lewat API dengan akun yang sama, sedangkan page size Pagination (diubah ke 25 di langkah 11, dikembalikan ke 10 di langkah 19) dipulihkan ke 10 sebagai cadangan.
- Cleanup (hook `after`): hapus lewat API `Frozen Co` bila sempat terbuat.
- TC-GS-BRAND-239, 240, 244: login sebagai Total Control dan berada di Global Settings > Master Reference > Brand.

## Test Steps

### TC-GS-BRAND-239: Create saat entitas suspended/expired

1. Ubah status Client A menjadi Suspended (lewat API dengan akun Total Control Principal)
2. Muat ulang halaman Global Settings > Master Reference > Brand
3. Klik [+ Brand], isi Brand Name `Frozen Co`
4. Klik [Submit]
5. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
6. Verifikasi modal tertutup
7. Verifikasi list di-refresh
8. Search `Frozen Co` pada tabel Brand
9. Verifikasi `Frozen Co` tidak dibuat (tidak ada di tabel)
10. Kosongkan Search
11. Ubah page size Pagination menjadi 25 sehingga seluruh brand Client A tampil dalam satu halaman

### TC-GS-BRAND-244: Bulk Delete saat entitas suspended ditolak

12. Centang Orion Tech dan Brightway
13. Klik `Bulk Action` > `Delete`
14. Klik [Delete] pada dialog konfirmasi
15. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
16. Verifikasi dialog tertutup
17. Verifikasi list di-refresh
18. Verifikasi Orion Tech dan Brightway tetap ada
19. Kembalikan page size Pagination ke 10

### TC-GS-BRAND-240: Edit dan Delete saat entitas expired

20. Ubah status Client A menjadi Expired (lewat API dengan akun Total Control Principal)
21. Muat ulang halaman Global Settings > Master Reference > Brand
22. Search `Orion Tech` pada tabel Brand
23. Klik `⋯` pada baris Orion Tech > Edit, ubah Brand Name menjadi `Orion E`, klik [Save]
24. Verifikasi toast error: "Changes can't be saved while this workspace is suspended or expired."
25. Klik `⋯` pada baris Orion Tech > Delete → dialog `Delete Brand` tampil, klik [Delete]
26. Verifikasi toast error yang sama: "Changes can't be saved while this workspace is suspended or expired."
27. Verifikasi Orion Tech tetap ada di tabel

## Notes

- Mode: FE+BE. Sumber: `global-settings/brand/TestCases/tc-brand.md`. Kelas state tenant (prinsip 13h): write-lockdown dipisah dari verifikasi baca murni, yang ada di spec `TC-GS-BRAND-E2E-073-tenant-suspended-baca-tetap-tersedia`.
- Urutan TC di spec berbeda dari urutan sumber: dua TC bersyarat Suspended (239, 244) berurutan, lalu status diubah ke Expired untuk 240. Semua aksi ditolak sehingga tidak ada data terhapus atau berubah.
- Toast penolakan mengikuti keputusan NC-04 di TC sumber. Penolakan aksi tulis menutup modal dan me-refresh list (`global-settings/brand/PRD/brand.md` §7.2), sehingga tidak ada langkah menutup form sesudah Edit ditolak (langkah 24).
- Langkah penghubung: langkah 2 dan 21 (memuat ulang halaman setelah status Client A berubah, supaya halaman memakai status terbaru); langkah 8, 10, dan 22 (Search nama brand supaya baris atau absensinya terlihat di tabel, lalu mengosongkan Search); langkah 11 dan 19 (page size 25 sekali supaya Orion Tech dan Brightway terlihat dalam satu halaman dan dapat dicentang bersama, lalu dipulihkan). Langkah 1 dan 20 (mengubah status Client A) adalah prasyarat TC (Client A berstatus Suspended atau Expired) yang dijadikan langkah eksplisit.
- Status Client A diubah saat sesi Total Control sudah aktif; apakah sesi tetap valid setelah status berubah adalah asumsi TC (precondition TC menyebut Client A berstatus Suspended/Expired dan user berada di Brand). Akun pengubah status, hak ubahnya, dan endpoint-nya sudah dicatat sebagai kebutuhan di Prerequisites.
