# Coverage E2E — Global Settings > User

Sumber: `global-settings/user/TestCases/tc-user.md`. Cakupan saat ini: section 3a (Create, 42 TC, 35 tercakup di 4 spec, 7 dicakup TC frontend, sisi Distributor dan Partner pada TC-15 belum ada), section 3c–3e (Delete, Bulk, Toggle Active, Remove Access, 45 TC, 35 tercakup di 4 spec: Delete, Toggle Active, Remove Access, dan force-logout; 10 TC dicakup TC frontend), section 5a (Search/Filter/Sort/Pagination/Download, 44 TC tercakup di 1 spec dari 104 TC section 5a — sisanya Setup Column dan state retention, sudah dicakup TC frontend), dan Role Matrix section 2 + 3k (19 TC ditambah 6 TC baru 581–586, tercakup di 11 spec: 5 positif, 6 negatif).
Suite: `specs/GlobalSettings/User/`. Status semua spec: `draft`, belum ada script.

**Aturan seleksi (2026-09-30):** spec e2e merangkap TC FE. Semua TC masuk spec kecuali hanya-BE. Spec hanya-FE ditandai `Mode: mock`. Kalimat "sudah dicakup TC frontend" di paragraf cakupan berikut adalah keadaan sebelum perubahan ini dan sekarang berarti antrean spec hanya-FE.

## TC granular → spec e2e

| Spec | Isi | TC sumber |
|---|---|---|
| TC-GS-USER-E2E-001 | Screening, validasi, dan menutup modal (2 sesi modal, tidak membuat data) | TC-GS-USER-14, 15 (bagian Client), 25, 457, 16, 17, 19, 192, 420 (121 karakter), 18, 340, 347, 482, 431, 22, 487, 169 |
| TC-GS-USER-E2E-002 | Create sukses: 3 user dalam 1 sesi modal dengan Stay | TC-GS-USER-13, 20, 469, 471, 473, 191, 440, 341, 489, 468, 470, 472, 474, 476, 420 (batas 120), 65, 346, 21, 143, 405 |
| TC-GS-USER-E2E-003 | Entity Principal | TC-GS-USER-15 (bagian Principal), 467 |
| TC-GS-USER-E2E-004 | Scan & Pair TAG | TC-GS-USER-475 |
| TC-GS-USER-E2E-005 | Delete user: guard, Delete single, lalu Select All dan Bulk Delete di akhir (harus dijalankan terakhir dan tidak paralel) | TC-GS-USER-36, 37, 433, 33, 353, 453, 34, 35, 258, 38, 434, 145, 406, 164, 168, 367 |
| TC-GS-USER-E2E-006 | Deactivate memaksa logout sesi target (dua sesi browser, dua akun) | TC-GS-USER-481, 251 |
| TC-GS-USER-E2E-007 | Search, Filter, Sort, Pagination, Download — semua yang benar-benar memukul backend dan mempengaruhi baris/urutan data nyata | TC-GS-USER-358, 359, 360, 361, 362, 554, 555, 556, 557, 357, 127, 197, 198, 199, 200, 201, 202, 207, 208, 364, 128, 218, 219, 220, 221, 222, 223, 224, 225, 227, 228, 229, 230, 210, 211, 212, 216, 132, 131, 490, 491, 492, 493, 494, 496, 497 |
| TC-GS-USER-E2E-008 | Toggle Active single dan bulk pada berbagai kondisi data | TC-GS-USER-44, 45, 42, 435, 41, 447, 43, 446, 46, 480, 91, 443, 47, 445, 444, 449, 146, 408 |
| TC-GS-USER-E2E-009 | Remove Access lewat Modal Edit pada berbagai kondisi data | TC-GS-USER-52, 51, 31, 49, 352, 425, 351, 387, 50, 147 |
| TC-GS-USER-E2E-010 | Role Matrix positif Create (Full CRUD, Create-only) | TC-GS-USER-394, 586 |
| TC-GS-USER-E2E-011 | Role Matrix positif Edit dan Remove Access (Full CRUD, Update-only) | TC-GS-USER-09, 395, 585, 586 |
| TC-GS-USER-E2E-012 | Role Matrix positif Toggle Active (Full CRUD, Update-only) | TC-GS-USER-584, 586 |
| TC-GS-USER-E2E-013 | Role Matrix positif Delete (Full CRUD, Delete-only) | TC-GS-USER-396, 586 |
| TC-GS-USER-E2E-014 | Role Matrix positif kontrol dan target Total Control (Total Control, Default User) | TC-GS-USER-07, 79, 82 |
| TC-GS-USER-E2E-015 | Role Matrix negatif Create (Read Only, Update-only, Delete-only) | TC-GS-USER-08, 582, 583 |
| TC-GS-USER-E2E-016 | Role Matrix negatif Edit, Toggle Active, Resend (Read Only, Create-only, Delete-only) | TC-GS-USER-08, 85, 581, 583 |
| TC-GS-USER-E2E-017 | Role Matrix negatif Delete (Read Only, Create-only, Update-only) | TC-GS-USER-08, 85, 581, 582 |
| TC-GS-USER-E2E-018 | Role Matrix negatif target terlindungi Default User dan akun sendiri (Total Control, Default User) | TC-GS-USER-80, 81, 83, 86 |
| TC-GS-USER-E2E-019 | Role Matrix negatif Full CRUD ke target Total Control | TC-GS-USER-339, 84 |
| TC-GS-USER-E2E-020 | Role Matrix negatif akses halaman (Read Only, No Role) | TC-GS-USER-486, 10, 12, 11 |
| TC-GS-USER-E2E-021 | **Varian B (tidak dipakai, file dibiarkan)**: Role Matrix positif gabungan per role — Full CRUD, Total Control, Default User, Create-only, Update-only, Delete-only. Alternatif untuk 010–014 | TC-GS-USER-09, 586, 07, 79, 82, 394, 395, 585, 584, 396 |
| TC-GS-USER-E2E-022 | **Varian B (tidak dipakai, file dibiarkan)**: Role Matrix negatif gabungan per role — Read Only, Create-only, Update-only, Delete-only, Full CRUD, Total Control, Default User, No Role. Alternatif untuk 015–020 | TC-GS-USER-486, 08, 85, 581, 582, 583, 339, 84, 80, 81, 83, 86, 10, 12, 11 |
| TC-GS-USER-E2E-023 | Validasi form Edit dan menutup modal Edit (pasangan Edit dari 001) | TC-GS-USER-254, 30, 422, 424, 464, 348, 432, 423, 488 |
| TC-GS-USER-E2E-024 | Edit user berhasil dan pencatatan Changelog | TC-GS-USER-195, 26, 196, 495, 144, 409 |
| TC-GS-USER-E2E-025 | Ubah email user dan alur Pending Email Change (butuh mailbox uji) | TC-GS-USER-403, 350, 27, 404, 349, 479, 421, 430, 477, 391, 174 |
| TC-GS-USER-E2E-026 | Edit Access untuk produk yang subscription-nya tidak aktif (blokir data) | TC-GS-USER-389, 478 |
| TC-GS-USER-E2E-027 | Edit info dasar Default User (ruang lingkup dibatasi sampai `GAP-274` diputuskan) | TC-GS-USER-29 (sebagian: langkah 1 sampai 2) |
| TC-GS-USER-E2E-028 | Token konfirmasi perubahan email kedaluwarsa (butuh pemicu waktu) | TC-GS-USER-28, 174 |
| TC-GS-USER-E2E-029 | Kirim ulang email aktivasi dan konfirmasi (single, bulk, screening tombol tersembunyi) | TC-GS-USER-56, 439, 95, 54, 57, 438, 442 |
| TC-GS-USER-E2E-030 | Kirim ulang diblokir selama cooldown 60 detik (blokir data) | TC-GS-USER-55, 463 |
| TC-GS-USER-E2E-031 | Pasang, ganti, dan lepas TAG RFID (butuh simulasi scan) | TC-GS-USER-59, 64, 437, 436, 63, 148 |
| TC-GS-USER-E2E-032 | Validasi Scan TAG untuk TAG tidak valid, Detail dan modal Create (blokir data) | TC-GS-USER-60, 62, 61, 343, 344, 345 |
| TC-GS-USER-E2E-033 | Create, Edit, Delete identik di semua tier plan dan Scan TAG hanya Growth ke atas (lima entity) | TC-GS-USER-397, 342 |
| TC-GS-USER-E2E-034 | Buat dan ubah Temporary User dengan tanggal expiry | TC-GS-USER-66, 336, 68 |
| TC-GS-USER-E2E-035 | Temporary User nonaktif otomatis saat expiry (berbasis waktu) | TC-GS-USER-67, (perbaikan: Auto-Deactivate di Changelog dan Activity Log, bukan System Log) |
| TC-GS-USER-E2E-036 | Reaktivasi Temporary User expired dan Bulk Activate yang melewatinya (blokir data) | TC-GS-USER-89, 333, 335, 90, 354, 332, 334, 337 |
| TC-GS-USER-E2E-037 | Reset Authenticator user lain, akun sendiri, dan Default User (dua sesi login) | TC-GS-USER-71, 72, 94, 69 |
| TC-GS-USER-E2E-038 | Reset Authenticator tidak tersedia untuk user belum enrolled (blokir data) | TC-GS-USER-70 |
| TC-GS-USER-E2E-039 | Kelola foto profil dari User Detail dan Modal Edit | TC-GS-USER-75, 76, 74, 371, 78, 542, 373, 541, 372, 77, 407, 163 |
| TC-GS-USER-E2E-040 | Pembuatan user diblokir saat Master Data Count Limit tercapai (jalan terakhir dan sendirian) | TC-GS-USER-255, 23, 87, 402 |
| TC-GS-USER-E2E-041 | Data master dihapus atau di-rename saat form terbuka (dua sesi login) | TC-GS-USER-88, 461, 462 |
| TC-GS-USER-E2E-042 | Dua admin mengubah user yang sama bersamaan (dua sesi login) | TC-GS-USER-441, 401, 399, 400 |
| TC-GS-USER-E2E-043 | Custom Field Phone tersimpan gabungan dan terbaca kembali di Edit | TC-GS-USER-514 |
| TC-GS-USER-E2E-044 | Perubahan master data Position tercermin di dropdown form User | TC-GS-USER-166, 415, 416 |
| TC-GS-USER-E2E-045 | Siklus Custom Field User (buat, deactivate, reactivate, ganti tipe, hapus) tercermin di form dan detail | TC-GS-USER-414, 167, 411, 413, 412 |
| TC-GS-USER-E2E-046 | Status Active Global tercermin di Settings User Admin Console (dua aplikasi) | TC-GS-USER-170 |
| TC-GS-USER-E2E-047 | User yang dinonaktifkan hilang dari pilihan transaksi baru di Fixed Asset | TC-GS-USER-388, 579, 580 |
| TC-GS-USER-E2E-048 | User hasil Import tampil dan bisa di-Edit sama seperti user manual | TC-GS-USER-417, 418 |
| TC-GS-USER-E2E-049 | Status user menjadi Activated setelah user mengaktifkan akunnya (mailbox uji) | TC-GS-USER-419 |
| TC-GS-USER-E2E-050 | Konfirmasi ganti email membatalkan token Reset Password lama (mailbox uji) | TC-GS-USER-544, 174 |
| TC-GS-USER-E2E-051 | User entity lain tidak bocor ke User List (banyak entity) | TC-GS-USER-171, 392 |
| TC-GS-USER-E2E-052 | Seleksi bulk dibatasi Bulk Action Checkbox Limit (jalan sendirian) | TC-GS-USER-410, 393 |
| TC-GS-USER-E2E-053 | Assign, Check Out, Check In, Unassign Handheld tercatat di log user | TC-GS-USER-390 |
| TC-GS-USER-E2E-054 | Tab Role: tampilan, edit CRUD inline, dan sinkron dua arah dengan Role & Permission | TC-GS-USER-96, 578, 454, 355, 98, 165 |
| TC-GS-USER-E2E-055 | Auto-Revert Total Control dari Tab Role: batal dulu, lalu lanjut (jalan sendirian) | TC-GS-USER-483, 455, 575 |
| TC-GS-USER-E2E-056 | Target menerima notifikasi saat Total Control atau Read Only dicabut otomatis | TC-GS-USER-252, 253 |
| TC-GS-USER-E2E-057 | Tab Role tidak bisa diedit aktor Read Only atau capability holder pada target Total Control | TC-GS-USER-498, 499 |
| TC-GS-USER-E2E-058 | Modal Changelog User > Role: kolom, Action, Filter, Search, Download, Setup Column, sinkron | TC-GS-USER-568, 569, 570, 571, 572, 573, 574 |
| TC-GS-USER-E2E-059 | Tab Responsibilities menyesuaikan sub-tab dengan entity dan subscription (banyak entity) | TC-GS-USER-100, 101, 484, 104, 380 |
| TC-GS-USER-E2E-060 | Kolom, urutan, dan toolbar tiap sub-tab Responsibilities | TC-GS-USER-550, 551, 552, 553, 103, 546, 105, 106, 107, 381 |
| TC-GS-USER-E2E-061 | Empty state per sub-tab Responsibilities dan pencarian tanpa kecocokan | TC-GS-USER-102, 547, 548, 549 |
| TC-GS-USER-E2E-062 | Tab Non-Login User di Detail Login User (reverse-lookup) | TC-GS-USER-108, 109, 560, 561, 562, 565 |
| TC-GS-USER-E2E-063 | Filter, Search, sort, Download, Setup Column di Tab Non-Login User | TC-GS-USER-563, 564, 566, 567 |
| TC-GS-USER-E2E-064 | Ubah Custom Field langsung di User Detail dengan inline-edit | TC-GS-USER-374, 375, 376, 377, 378, 379, 120, 119 |
| TC-GS-USER-E2E-065 | Inline-edit Custom Field tidak tersedia untuk aktor Read Only dan capability holder | TC-GS-USER-500, 501 |
| TC-GS-USER-E2E-066 | Custom Field dinonaktifkan admin lain saat inline-edit terbuka (dua sesi, jalan sendirian) | TC-GS-USER-121 |
| TC-GS-USER-E2E-067 | Tab Changelog dan modal Changelog identik, System Log mencatat aksi yang dilakukan user | TC-GS-USER-110, 111 |
| TC-GS-USER-E2E-068 | Tab User Log: kolom, format Device / Browser, sort IP Address berbasis string | TC-GS-USER-112, 356 |
| TC-GS-USER-E2E-069 | Activity Log level Global Settings menampilkan aksi semua user | TC-GS-USER-116 |
| TC-GS-USER-E2E-070 | Product Selector: opsi produk dan navigasi ke Detail User produk lain | TC-GS-USER-117, 118, 485, 545 |
| TC-GS-USER-E2E-071 | Opsi Product Selector yang tidak boleh dibaca aktor hilang dari daftar | TC-GS-USER-456 |
| TC-GS-USER-E2E-072 | Badge User Type dan status Authenticator | TC-GS-USER-122, 123, 124, 426, 125 |
| TC-GS-USER-E2E-073 | Header dan General Information User Detail, termasuk tampilan Custom Fields | TC-GS-USER-382, 383, 384, 385, 386, 536 |
| TC-GS-USER-E2E-074 | Toggle Active dan menu Header Disabled untuk target yang dilindungi | TC-GS-USER-502, 503, 504 |
| TC-GS-USER-E2E-075 | Inline-edit Custom Field gagal karena error server (`Mode: mock`) | TC-GS-USER-577 |
| TC-GS-USER-E2E-076 | Tombol Save modal Edit loading dan tidak bisa diklik ganda (`Mode: mock`) | TC-GS-USER-194 |
| TC-GS-USER-E2E-077 | Batalkan perubahan email gagal server (`Mode: mock`) | TC-GS-USER-559 |
| TC-GS-USER-E2E-078 | Hapus foto profil dari Avatar gagal server (`Mode: mock`) | TC-GS-USER-576 |
| TC-GS-USER-E2E-079 | Ganti foto profil gagal server, foto lama tidak berubah (`Mode: mock`) | TC-GS-USER-450 |
| TC-GS-USER-E2E-080 | Download User List gagal server (`Mode: mock`) | TC-GS-USER-363 |
| TC-GS-USER-E2E-081 | Delete user yang sudah dihapus admin lain saat dialog terbuka (dua sesi) | TC-GS-USER-451 |
| TC-GS-USER-E2E-082 | Delete ditolak saat role aktor dicabut ketika dialog terbuka (dua sesi) | TC-GS-USER-452 |
| TC-GS-USER-E2E-083 | Create menolak emoji yang lolos guard FE lewat manipulasi DOM | TC-GS-USER-193 |
| TC-GS-USER-E2E-084 | Edit menolak emoji yang lolos guard FE lewat manipulasi DOM | TC-GS-USER-465 |
| TC-GS-USER-E2E-085 | Dialog bulk Activate/Deactivate: satu user, daftar panjang, aksi disembunyikan | TC-GS-USER-458, 459, 448, 398 |
| TC-GS-USER-E2E-086 | Overlay hover Avatar di User Detail dan modal Edit (`Mode: mock`) | TC-GS-USER-370, 540 |
| TC-GS-USER-E2E-087 | Foto di modal Create hanya staged sampai Submit (`Mode: mock`) | TC-GS-USER-537, 538, 539 |
| TC-GS-USER-E2E-088 | Perubahan foto di modal Edit dibuang saat modal ditutup (`Mode: mock`) | TC-GS-USER-543 |
| TC-GS-USER-E2E-089 | Setup Column User List: overlay, popup modal, Live Preview (`Mode: mock`) | TC-GS-USER-259, 260, 129, 133 |
| TC-GS-USER-E2E-090 | Setup Column User List: sembunyikan dan munculkan kolom (`Mode: mock`) | TC-GS-USER-261–274 |
| TC-GS-USER-E2E-091 | Setup Column User List: urutan kolom (`Mode: mock`) | TC-GS-USER-276–289, 130 |
| TC-GS-USER-E2E-092 | Setup Column User List: pin dan unpin (`Mode: mock`) | TC-GS-USER-291–304 |
| TC-GS-USER-E2E-093 | Setup Column User List: Reset to Default dan Cancel (`Mode: mock`) | TC-GS-USER-306, 307 |
| TC-GS-USER-E2E-094 | Siklus interaksi search box toolbar User List (`Mode: mock`) | TC-GS-USER-126 |
| TC-GS-USER-E2E-095 | Tampilan kolom Name dan Access (`Mode: mock`) | TC-GS-USER-177, 466, 460 |
| TC-GS-USER-E2E-096 | Filter Access: isi opsi, pencarian, OR, chip | TC-GS-USER-203, 204, 205, 256 |
| TC-GS-USER-E2E-097 | Search, Filter, Sort, seleksi baris tidak saling mereset | TC-GS-USER-213, 214, 215, 217 |
| TC-GS-USER-E2E-098 | Search parsial, case-insensitive, Filter Division dengan Active | TC-GS-USER-140, 141, 142 |
| TC-GS-USER-E2E-099 | Badge Pending Activation dan Pending Email Confirmation mutually exclusive | TC-GS-USER-338 |
| TC-GS-USER-E2E-100 | Download User List mengikuti kolom yang terlihat | TC-GS-USER-494 |
| TC-GS-USER-E2E-101 | Sub-tab Login User dan Non-Login User menyimpan state sendiri | TC-GS-USER-134, 135 |
| TC-GS-USER-E2E-102 | Setup Column tab log berbeda dari User List (`Mode: mock`) | TC-GS-USER-136 |
| TC-GS-USER-E2E-103 | Search, Filter, Download di tiga tab log User Detail | TC-GS-USER-137, 138, 139 |
| TC-GS-USER-E2E-104 | Guided Tooltip User List: auto-trigger, replay, navigasi, keluar tanpa selesai | TC-GS-USER-185–190 |
| TC-GS-USER-E2E-105 | Aksesibilitas keyboard: kontrol, tooltip, dialog (`Mode: mock`) | TC-GS-USER-182, 183, 184 |
| TC-GS-USER-E2E-106 | Input Custom Field di modal Create | TC-GS-USER-505–513 |
| TC-GS-USER-E2E-107 | Input Custom Field di modal Edit | TC-GS-USER-527–535 |
| TC-GS-USER-E2E-108 | Placeholder Custom Field bawaan dan kustom (`Mode: mock`) | TC-GS-USER-515–526 |
| TC-GS-USER-E2E-109 | Modal Changelog User List: struktur, kolom, Search | TC-GS-USER-232, 233, 250, 558 |
| TC-GS-USER-E2E-110 | Modal Changelog User List: Filter | TC-GS-USER-234–241, 257, 558 |
| TC-GS-USER-E2E-111 | Modal Changelog User List: sort tiga keadaan | TC-GS-USER-242–246 |
| TC-GS-USER-E2E-112 | Modal Changelog User List: Download | TC-GS-USER-249 |
| TC-GS-USER-E2E-113 | Modal Changelog User List: hover truncate (`Mode: mock`) | TC-GS-USER-247 |
| TC-GS-USER-E2E-114 | Setup Column modal Changelog: overlay, popup, sembunyikan kolom (`Mode: mock`) | TC-GS-USER-248, 308–315 |
| TC-GS-USER-E2E-115 | Setup Column modal Changelog: urutan dan pin (`Mode: mock`) | TC-GS-USER-316–329 |
| TC-GS-USER-E2E-116 | Setup Column modal Changelog: Reset to Default dan Cancel (`Mode: mock`) | TC-GS-USER-330, 331 |
| TC-GS-USER-E2E-117 | Tampilan awal User List | TC-GS-USER-1, 2 |
| TC-GS-USER-E2E-118 | Baris Default User dan akun sendiri di User List | TC-GS-USER-5, 6 |
| TC-GS-USER-E2E-119 | User List: loading, hasil kosong, gagal memuat (`Mode: mock`) | TC-GS-USER-3 |
| TC-GS-USER-E2E-120 | Create user gagal server (`Mode: mock`) | TC-GS-USER-24 |
| TC-GS-USER-E2E-121 | Edit user gagal server (`Mode: mock`) | TC-GS-USER-32 |
| TC-GS-USER-E2E-122 | Delete satu user gagal server (`Mode: mock`) | TC-GS-USER-40 |
| TC-GS-USER-E2E-123 | Bulk Delete sebagian gagal (`Mode: mock`) | TC-GS-USER-39 |
| TC-GS-USER-E2E-124 | Toggle Active gagal server (`Mode: mock`) | TC-GS-USER-48 |
| TC-GS-USER-E2E-125 | Remove Access gagal server (`Mode: mock`) | TC-GS-USER-53 |
| TC-GS-USER-E2E-126 | Resend email gagal server (`Mode: mock`) | TC-GS-USER-58 |
| TC-GS-USER-E2E-127 | Reset Authenticator gagal server (`Mode: mock`) | TC-GS-USER-73 |

TC-15 dan TC-420 terbelah di dua spec (dicatat di `## Notes` kedua spec).

**Role Matrix (2026-09-29):** dipilih varian A (spec 010–020, satu spec per aksi, positif dan negatif terpisah) karena lebih partikular. Varian B (spec 021 dan 022, disusun per role) tidak dipakai tetapi filenya dibiarkan untuk sementara. Keduanya mencakup TC yang sama, dan tabel "Lapisan per TC" di bawah menyebut varian A.

## TC yang belum punya spec (antrean)

**Perubahan aturan 2026-09-30:** dokumen e2e merangkap TC FE (`docs/e2e-conventions.md` bagian 2). Satu-satunya TC yang tidak masuk spec adalah TC hanya-BE. Baris di bawah dulu berstatus "tidak dijadikan spec karena sudah dicakup TC frontend"; sekarang semuanya masuk antrean spec. Kolom FE pada tabel "Lapisan per TC" di bawah dipertahankan sementara sebagai referensi.

| TC | Status | Rencana spec |
|---|---|---|
| TC-GS-USER-24, 193 | Antrean | Spec hanya-FE (mock): Create gagal 500 dan fallback emoji lewat DOM injection. TC-23 sudah di spec 040, TC-342 di spec 033, TC-343, 344, 345 di spec 032 |
| TC-GS-USER-15 (bagian Distributor dan Partner) | Belum ada TC | Hanya entity Principal yang dicakup spec 003 |
| TC-GS-USER-39, 40, 451, 452, 48, 53 | Antrean | Spec hanya-FE (mock): error, race, dan perubahan izin di tengah aksi |
| TC-GS-USER-448, 458, 459, 398 | Antrean | Spec hanya-FE: copy dan state UI |
| Setup Column (129, 130, 259–307 dan sejenisnya, ~40 TC) | Antrean | Spec hanya-FE per layar: Setup Column |
| Retensi state kombinasi (213, 214, 215, 217) | Antrean | Spec hanya-FE: retensi state |
| Chip rendering/overflow, badge severity/urutan, z-index popover, ekstensi nama file (203, 204, 205, 256, 460, 466, 133, dan sejenisnya) | Antrean | Spec hanya-FE: tampilan |
| TC-GS-USER-363 | Antrean | Spec hanya-FE (mock): Download gagal server error |
| TC-GS-USER-129, 130, 202, 466 | Antrean | Spec hanya-FE. Sebelumnya tidak ada rujukan di `tc-user-frontend.md`; dengan aturan baru gap itu selesai karena spec menjadi acuannya |
| TC-GS-USER-58, 73, 576, 450 | Antrean | Spec hanya-FE (mock): kegagalan server pada Resend, Reset Authenticator, hapus foto, ganti foto |
| Langkah 5–7 spec 002 (Create gagal server error) | Dipertahankan | Sudah di spec 002, tandai `Mode: mock` saat script dibuat |

## Lapisan per TC (section 3a)

FE dari tabel pemetaan `tc-user-frontend.md`. BE tidak dapat dipetakan per TC granular (`tc-user-backend.md` tidak merujuk id TC granular).

| TC | Prioritas | FE | E2E | Catatan |
|---|---|---|---|---|
| 13 | P0 | FE-027 | E2E-002 |  |
| 14 | P1 | FE-028 | E2E-001 |  |
| 15 | P1 | FE-029 | E2E-001, E2E-003 |  |
| 16 | P0 | FE-030 | E2E-001 |  |
| 17 | P1 | FE-031 | E2E-001 |  |
| 18 | P0 | FE-032 | E2E-001 |  |
| 19 | P1 | FE-033 | E2E-001 |  |
| 20 | P1 | — | E2E-002 |  |
| 341 | P1 | FE-045 | E2E-002 |  |
| 489 | P0 | — | E2E-002 | P0 hanya satu lapisan |
| 467 | P1 | — | E2E-003 |  |
| 65 | P1 | FE-132 | E2E-002 |  |
| 468 | P2 | — | E2E-002 |  |
| 469 | P1 | — | E2E-002 |  |
| 470 | P2 | — | E2E-002 |  |
| 471 | P1 | — | E2E-002 |  |
| 472 | P2 | — | E2E-002 |  |
| 473 | P1 | — | E2E-002 |  |
| 474 | P2 | — | E2E-002 |  |
| 475 | P1 | — | E2E-004 |  |
| 476 | P2 | — | E2E-002 |  |
| 21 | P2 | FE-034 | E2E-002 |  |
| 22 | P2 | FE-035 | E2E-001 |  |
| 431 | P2 | FE-036 | E2E-001 |  |
| 487 | P2 | — | E2E-001 |  |
| 23 | P2 | FE-037 | — |  |
| 24 | P2 | FE-038 | — |  |
| 25 | P1 | FE-039 | E2E-001 |  |
| 191 | P2 | FE-040 | E2E-002 |  |
| 440 | P1 | FE-041 | E2E-002 |  |
| 192 | P2 | FE-042 | E2E-001 |  |
| 193 | P2 | FE-043 | — |  |
| 340 | P1 | FE-044 | E2E-001 |  |
| 342 | P1 | FE-046 | — |  |
| 343 | P1 | FE-047 | — |  |
| 344 | P1 | FE-048 | — |  |
| 345 | P1 | FE-049 | — |  |
| 346 | P1 | FE-050 | E2E-002 |  |
| 347 | P1 | FE-051 | E2E-001 |  |
| 482 | P1 | — | E2E-001 |  |
| 420 | P2 | FE-052 | E2E-001, E2E-002 |  |
| 457 | P1 | FE-053 | E2E-001 |  |

## Lapisan per TC (section 3c–3e)

| TC | Prioritas | FE | E2E | Catatan |
|---|---|---|---|---|
| 33 | P0 | FE-074 | E2E-005 |  |
| 353 | P2 | — | E2E-005 |  |
| 453 | P1 | FE-086 | E2E-005 |  |
| 433 | P2 | FE-075 | E2E-005 |  |
| 34 | P1 | FE-076 | E2E-005 |  |
| 35 | P1 | — | E2E-005 |  |
| 36 | P0 | FE-077 | E2E-005 |  |
| 37 | P0 | FE-078 | E2E-005 |  |
| 258 | P1 | FE-081 | E2E-005 |  |
| 38 | P1 | FE-079 | E2E-005 |  |
| 434 | P2 | FE-080 | E2E-005 |  |
| 39 | P2 | FE-082 | — |  |
| 40 | P2 | FE-083 | — |  |
| 41 | P0 | FE-087 | E2E-008 |  |
| 435 | P2 | FE-088 | E2E-008 |  |
| 42 | P0 | FE-089 | E2E-008 |  |
| 43 | P1 | FE-090 | E2E-008 |  |
| 44 | P0 | FE-091 | E2E-008 |  |
| 45 | P0 | FE-092 | E2E-008 |  |
| 46 | P2 | FE-093 | E2E-008 |  |
| 47 | P1 | FE-094 | E2E-008 |  |
| 443 | P2 | FE-095 | E2E-008 |  |
| 444 | P1 | FE-096 | E2E-008 |  |
| 445 | P2 | FE-097 | E2E-008 |  |
| 446 | P1 | FE-100 | E2E-008 |  |
| 447 | P2 | FE-101 | E2E-008 |  |
| 448 | P2 | FE-102 | — |  |
| 449 | P1 | FE-103 | E2E-008 |  |
| 451 | P1 | FE-084 | — |  |
| 452 | P1 | FE-085 | — |  |
| 458 | P1 | FE-098 | — |  |
| 459 | P1 | FE-099 | — |  |
| 48 | P2 | FE-104 | — |  |
| 398 | P2 | FE-105 | — |  |
| 31 | P2 | - | E2E-009 | Skenario identik dengan TC-51 (Edit hapus semua Access diblokir, minimal 1), dicakup lewat TC-51. Duplikasi di tabel TC sumber dibiarkan |
| 49 | P0 | FE-106 | E2E-009 |  |
| 50 | P1 | FE-107 | E2E-009 | Dikoreksi 2026-09-29 (minimal 1 Access), dicakup bersama TC-387 |
| 51 | P2 | FE-108 | E2E-009 | Sudah diputuskan tunggal (`GAP-248`): diblokir inline "Access must not be empty" |
| 52 | P1 | FE-109 | E2E-009 |  |
| 53 | P2 | FE-110 | — |  |
| 351 | P1 | FE-111 | E2E-009 |  |
| 352 | P2 | FE-112 | E2E-009 |  |
| 387 | P1 | FE-113 | E2E-009 |  |
| 425 | P2 | FE-114 | E2E-009 |  |
| 480 | P1 | — | E2E-008 |  |
| 481 | P1 | — | E2E-006 |  |

Semua TC P0 di section ini (33, 36, 37, 41, 42, 44, 45, 49) punya dua lapisan (FE dan E2E), jadi tidak ada P0 satu lapisan di 3c–3e.

## Lapisan per TC (section 5a)

Tidak ada TC P0 di section ini (tertinggi P1). FE di sini memakai pola representative — satu FE TC bisa mewakili beberapa TC granular yang mekanismenya sama; kolom FE menampilkan id itu untuk semuanya.

| TC | Prioritas | FE | E2E | Catatan |
|---|---|---|---|---|
| 358 | P1 | — | E2E-007 |  |
| 359 | P1 | — | E2E-007 |  |
| 360 | P1 | — | E2E-007 |  |
| 361 | P1 | — | E2E-007 |  |
| 362 | P2 | — | E2E-007 |  |
| 554 | P2 | — | E2E-007 |  |
| 555 | P2 | — | E2E-007 |  |
| 556 | P2 | — | E2E-007 |  |
| 557 | P2 | — | E2E-007 |  |
| 357 | P2 | — | E2E-007 |  |
| 127 | P1 | FE-210 | E2E-007 | Overlap sengaja, lihat aturan hibrida |
| 197 | P1 | FE-210 | E2E-007 |  |
| 198 | P1 | FE-210 | E2E-007 |  |
| 199 | P1 | FE-210 | E2E-007 |  |
| 200 | P1 | FE-211 | E2E-007 |  |
| 201 | P1 | FE-210 | E2E-007 |  |
| 202 | P1 | — | — | Tidak ada FE, tercakup tidak langsung lewat E2E-007 langkah 55 |
| 207 | P2 | FE-210 | E2E-007 |  |
| 208 | P2 | FE-211 | E2E-007 |  |
| 364 | P1 | — | E2E-007 |  |
| 128 | P2 | FE-220 | E2E-007 |  |
| 218 | P2 | FE-220 | E2E-007 |  |
| 219 | P2 | FE-220 | E2E-007 |  |
| 220 | P2 | FE-220 | E2E-007 |  |
| 221 | P2 | FE-220 | E2E-007 |  |
| 222 | P2 | FE-220 | E2E-007 |  |
| 223 | P2 | FE-220 | E2E-007 |  |
| 224 | P2 | FE-220 | E2E-007 |  |
| 225 | P2 | FE-220 | E2E-007 |  |
| 227 | P2 | FE-220 | E2E-007 |  |
| 228 | P2 | FE-220 | E2E-007 |  |
| 229 | P2 | FE-220 | E2E-007 |  |
| 230 | P3 | FE-220 | E2E-007 |  |
| 132 | P2 | FE-231 | E2E-007 |  |
| 131 | P1 | FE-230 | E2E-007 |  |
| 490 | P2 | FE-268 | E2E-007 |  |
| 491 | P2 | FE-269 | E2E-007 |  |
| 492 | P2 | FE-270 | E2E-007 |  |
| 493 | P2 | FE-271 | E2E-007 |  |
| 494 | P2 | FE-272 | — | Duplikat TC-496 (`GAP-161` Closed), dicakup lewat TC-496 |
| 496 | P1 | FE-272 | E2E-007 |  |
| 497 | P2 | FE-273 | E2E-007 |  |
| 210 | P2 | FE-216 | E2E-007 |  |
| 211 | P2 | FE-216 | E2E-007 |  |
| 212 | P2 | FE-218 | E2E-007 |  |
| 216 | P2 | FE-217 | E2E-007 |  |
| 129 | P1 | — | — | Tidak ada FE, murni state UI. Dilaporkan sebagai kemungkinan gap TC frontend |
| 130 | P2 | — | — | Sama seperti TC-129 |
| 466 | P2 | — | — | Tidak ada FE, murni rendering. Dilaporkan sebagai kemungkinan gap TC frontend |

## Lapisan per TC (section 2 dan 3k)

| TC | Prioritas | FE | E2E | Catatan |
|---|---|---|---|---|
| 07 | P0 | FE-017 | E2E-014 |  |
| 08 | P0 | FE-018 | E2E-015, E2E-016, E2E-017 |  |
| 09 | P0 | FE-019 | E2E-011 |  |
| 10 | P0 | FE-020 | E2E-020 |  |
| 486 | P1 | — | E2E-020 | Tidak ada FE, E2E satu-satunya lapisan (bukan P0) |
| 11 | P0 | FE-021 | E2E-020 |  |
| 12 | P1 | FE-022 | E2E-020 |  |
| 339 | P1 | FE-023 | E2E-019 |  |
| 394 | P1 | FE-024 | E2E-010 |  |
| 395 | P1 | FE-025 | E2E-011 |  |
| 396 | P1 | FE-026 | E2E-013 |  |
| 79 | P0 | FE-153 | E2E-014 |  |
| 80 | P0 | FE-154 | E2E-018 |  |
| 81 | P0 | FE-155 | E2E-018 |  |
| 82 | P1 | FE-156 | E2E-014 |  |
| 83 | P1 | FE-157 | E2E-018 |  |
| 84 | P1 | FE-158 | E2E-019 |  |
| 85 | P0 | FE-159 | E2E-016, E2E-017 |  |
| 86 | P1 | FE-160 | E2E-018 |  |
| 581 | P1 | — | E2E-016, E2E-017 | TC baru 2026-09-29, belum ada padanan FE |
| 582 | P1 | — | E2E-015, E2E-017 | TC baru 2026-09-29, belum ada padanan FE |
| 583 | P1 | — | E2E-015, E2E-016 | TC baru 2026-09-29, belum ada padanan FE |
| 584 | P1 | — | E2E-012 | TC baru 2026-09-29, belum ada padanan FE |
| 585 | P1 | — | E2E-011 | TC baru 2026-09-29, belum ada padanan FE |
| 586 | P1 | — | E2E-010, E2E-011, E2E-012, E2E-013 | TC baru 2026-09-29, belum ada padanan FE |

Semua TC P0 di section ini punya dua lapisan (FE dan E2E), jadi tidak ada P0 satu lapisan. Role Matrix dipisah positif dan negatif per aksi, satu spec untuk banyak role (`docs/e2e-conventions.md` bagian 3a).

## Temuan untuk QA (sumber TC, bukan spec)

1. **Nama field tidak konsisten (sudah diperbaiki di `tc-user.md` 2026-09-26).** TC-GS-USER-13 dan 14 menyebut "Full Name", sedangkan TC-16, 192, dan 420 memakai First Name dan Last Name. PRD `user.md` baris 411 menetapkan form Create memakai First/Last Name\* (maks 120), dan "Full Name" hanya untuk tampilan tabel dan header Detail. Spec mengikuti PRD. `tc-user.md` TC-13, TC-14, dan TC-254 sudah disesuaikan.
2. **Division wajib (sudah diperbaiki di `tc-user.md` 2026-09-26).** PRD `user.md` baris 411 dan 853 menetapkan Division wajib dengan error "Division must not be empty". TC-14 tidak menandai Division dengan `*`. Spec memperlakukan Division wajib. TC-14 sekarang menandai Division, First Name, Last Name, Email, dan Access sebagai wajib.
3. **Data pre-setup belum tercatat (masih terbuka).** Custom Field `Blood Type` (TC-25) dan user dengan Employee ID `EMP-001` (TC-340) dipakai sebagai precondition, tetapi tidak ada di tabel Data Uji Pre-setup `tc-user.md`. Perlu dipastikan datanya ada di environment QA.
4. **(Masih terbuka.) TC-18 mencakup duplikasi lintas Login dan Non-Login User**, tetapi datanya hanya user Login ("Doni Pratama"). Varian duplikat terhadap Non-Login User belum punya data uji, dan spec 001 hanya menguji sisi Login.
5. **Teks toast.** TC-13 dan TC-489 menyebut "User created successfully.". Spec memakai teks ini.
6. **TC-GS-USER-196 dan 418 memakai "Full Name" gabungan pada Edit dan Changelog (sudah diperbaiki di `tc-user.md` 2026-09-26).** PRD `user.md` baris 989: di Edit, First Name dan Last Name adalah field terpisah, dan Changelog mencatat 1 baris per field yang berubah. Kedua TC sekarang memakai Last Name dengan Changelog `Field=Last Name, Old, New`. Tidak memengaruhi spec e2e section Create.
7. **Label checkbox Create tidak konsisten (sudah diperbaiki di `tc-user.md` 2026-09-26).** TC-GS-USER-21 memakai "Create another" di langkah dan "Stay on this form after submitting" di Expected, dan TC-GS-USER-255 memakai "after creating". Label kanonik "Stay on this form after submitting" (`foundation/functions/toast-copy.md` dan PRD `user.md` baris 411). TC-21 dan TC-255 sudah diseragamkan, dan TC-21 kini menyebut toast "User created successfully." pada save pertama.
8. **TC-GS-USER-91 terpecah jadi dua baris tabel (sudah diperbaiki di `tc-user.md` 2026-09-26).** Ada line break nyata di dalam sel Expected, sehingga hanya 5 dari 15 kolom terbaca. Diganti literal `\n` mengikuti PRD `user.md` baris 1161. Setelah perbaikan, semua baris TC di `tc-user.md` berjumlah 15 kolom.
9. **TC-GS-USER-192 menyebut "emoji atau simbol tidak diizinkan", padahal konvensi platform hanya memblok emoji (sudah diperbaiki di `tc-user.md` 2026-09-26).** `foundation/process/prd-process/prd-conventions.md` bagian "Karakter yang Diizinkan (Name Fields)" menetapkan pendekatan blocklist: hanya emoji yang diblok di input, semua karakter cetak lain (termasuk simbol) diizinkan. Ini bukan gap PRD, sehingga tidak dicatat di `prd-gap-registry.md`. TC-192 diperbaiki: hanya emoji diblok, ditambah langkah dan data `Budi-O'Neil` yang harus tetap bisa diketik. Spec 001 langkah 19 memverifikasinya.
10. **TC-GS-USER-467 dan 475 kini diotomasi (spec 003 dan 004).** Spec 004 butuh scan RFID hardware yang tidak bisa dilakukan browser, dan spec 003 butuh akun Total Control di entity Principal. Kebutuhan teknis keduanya dicatat sebagai permintaan ke tim FE (bukan hambatan seleksi).
11. **Label tombol dan penutupan modal di TC tidak selaras dengan konvensi platform (sudah diperbaiki di `tc-user.md` 2026-09-28).** `prd-conventions.md` §24.1: Create wajib `[Submit]` dan `[Clear Field]`, Edit wajib `[Save]` dan `[Clear Field]`, modal Create dan Edit tidak punya `[Cancel]` dan ditutup lewat `✕` atau `Esc`. TC memakai `[Save]` dan `[Cancel]` pada modal Create. 29 TC Create, 8 TC penutupan modal, TC-14, dan 3 TC Edit yang memakai `[Submit]` sudah diperbaiki. TC-66 diperjelas berlaku di modal Create dan modal Edit (`[Submit]` atau `[Save]`), dikonfirmasi user.
12. **Pengelompokan spec diubah dari 14 spec menjadi 4 spec (2026-09-28).** Prinsip baru ada di `docs/e2e-conventions.md` bagian 3: satu spec = satu atau beberapa sesi modal berurutan, screening di awal, validasi sebelum aksi sukses, kasus menutup form di akhir. Id spec di-renumber karena masih `draft` dan belum di-commit.
13. **Error Custom Field wajib saat submit kosong tidak tercakup di TC-GS-USER-16 dan TC-GS-USER-25 (sudah diperbaiki di `tc-user.md` 2026-09-28).** Custom Field wajib divalidasi seperti field wajib lain: copy `"[Field] must not be empty"` muncul setelah Submit (pola global `prd-conventions.md` baris 207 dan 846). Ini bukan gap PRD, sehingga tidak dicatat di `prd-gap-registry.md`. TC-16 sekarang punya precondition Custom Field `Blood Type` (required) dan error ke-6 `"Blood Type must not be empty"`, dan TC-25 menyebut teks error yang sama. Spec 001 langkah 11 dan 17 memverifikasinya.
14. **TC-GS-USER-50 dikoreksi (2026-09-29).** Precondition dan Expected menyebut Access menjadi kosong, bertentangan dengan minimal 1 Access. Sekarang memakai user `[Global Settings, FAMS]` dan hasil `[FAMS]`, dicakup spec 009 bersama TC-387.
15. **Role Matrix: kombinasi role parsial belum ada TC, ditambahkan 6 TC baru (2026-09-29).** TC-GS-USER-581 sampai 586 ditambahkan ke `tc-user.md` section 2, berdasarkan tabel gerbang UI `user.md` §4.8. Nama akun aktor baru (Create-only, Update-only, Delete-only) di tabel Data Uji Pre-setup adalah usulan dan boleh disesuaikan tim FE.
16. **Gap TC-51 diselesaikan sesi lain.** Entri gap yang saya buat bernomor `GAP-245` dinomori ulang menjadi `GAP-248`, dan TC-51 sudah diputuskan tunggal. Spec 009 memakainya.
17. **Pemecahan spec 005 (2026-09-29).** Spec 005 lama (Delete, Bulk, Toggle Active, Remove Access) dipecah menjadi 005 Delete, 008 Toggle Active, dan 009 Remove Access, karena topik aksinya berbeda dan kondisi datanya bervariasi. Spec role lama 008–016 diganti oleh 010–020 (Role Matrix positif dan negatif).

18. **TC-GS-USER-28 direvisi mengikuti PRD (2026-09-30).** Expected lama (badge hilang, email kembali) tidak ada di PRD; PRD menyatakan pending berakhir hanya lewat konfirmasi atau Cancel admin. TC-28 ditulis ulang di `tc-user.md` dan sekarang konsisten dengan TC-56. Perbedaan kode respons link kedaluwarsa (PRD 404 vs API 410) dilaporkan sebagai `GAP-275`.
19. **Badge dan label Pending Email Change diselaraskan ke PRD (2026-09-30).** Badge di baris adalah "Pending Email Confirmation" (TC-27, 28 sebelumnya menulis "Pending Email Change"), label di modal Edit adalah "Pending email change to [new email]" (TC-421, 479 sebelumnya "Pending Email Change: [new email]"). Diperbaiki di `tc-user.md`.
20. **Access Default User (2026-09-30).** UIUX menyatakan Default User otomatis punya semua modul dan Access-nya tidak bisa diedit, berbeda dengan PRD/API dan TC-29. Dilaporkan sebagai `GAP-274`. Spec 027 hanya menguji info dasar sampai keputusan.
21. **Toast perubahan email (2026-09-30).** TC-27 memakai toast `"Confirmation email sent to new address."` yang tidak ada di PRD (hanya toast Edit standar). Dilaporkan sebagai `GAP-276`. Spec 025 mengikuti TC sampai diputuskan.
22. **Timing validasi Edit dan Create diselaraskan ke PRD (2026-09-30).** PRD `user.md` bagian 6: error duplikat Email, duplikat Employee ID, dan batas 120 karakter muncul langsung saat mengetik, bukan setelah submit. Spec 023 dan 001 diperbaiki. Error kewajiban field tetap setelah submit.
23. **TC-GS-USER-23 diselaraskan ke PRD (2026-09-30).** Sebelumnya menyebut "limit lisensi" dan hasil ambigu (`[+ User]` disabled ATAU Submit diblokir). PRD tidak punya user cap per tier dan menetapkan Dialog Blok saat klik `[+ User]` pada Master Data Count Limit. TC-23 sekarang identik dengan TC-87 dan dipertahankan sebagai pasangannya, duplikasi diputuskan QA.
24. **TC-GS-USER-75 dan 76 diselaraskan ke PRD (2026-09-30).** `prd-conventions.md` bagian File Upload (Photo): format difilter di file picker tanpa pesan error, ukuran melebihi 1 MB di-resize otomatis tanpa pesan error. TC lama mengharapkan inline error keduanya. Diperbaiki di `tc-user.md` (Tipe 76 dan 75 menjadi Positive).
25. **Gap baru dari pencocokan PRD (2026-09-30).** `GAP-277`: aturan dan copy error tanggal Temporary Until lampau (PRD "≥ hari ini" tanpa copy error; copy hanya di API). `GAP-278`: copy Dialog Blok Master Data Count Limit untuk User tidak didefinisikan (Position punya). Spec 034 dan 040 menyesuaikan.
26. **TC-GS-USER-91 dicakup spec 008.** Skenarionya sama dengan TC-480 (Deactivate single dengan approval in-flight).
27. **Audit Log diselaraskan ke PRD §8 (2026-09-30).** TC-67 (Auto-Deactivate hanya di Changelog dan Activity Log, bukan System Log), TC-143 (judul salah: Create ada di System Log aktor, bukan User Log), TC-144 dan TC-146 (baris System Log lengkap dan Field `Status (Global)`) diperbaiki di `tc-user.md`. Spec 035 diperbaiki sesuai.
28. **Section 6, 8, 9, 11 (bagian A) ditambahkan sebagai langkah di spec yang sudah ada (2026-09-30).** Pengecekan log dan efek lintas modul yang menempel pada aksi yang sama tidak dibuat spec baru: 143/405 (002), 144/409 (024), 145/406/164/168/367 (005), 146/408 (008), 147 (009), 391/174 (025 dan 028), 442 (029), 148 (031), 407/163 (039), 251 (006), 169 (001).
29. **Section 6–11 selesai diproses (2026-09-30).** Hanya-BE: TC-173 (hash token di database) dan TC-176 (penegakan limit server-side lewat API langsung, `TC-GS-USER-BE-117`). Section 7 (API Contract) tidak punya TC granular dan Section 10 hanya tabel silang. TC-165, 252, 253 ditunda ke Tab Role lalu selesai di spec 054 dan 056. `TC-GS-USER-175` tidak pernah ditulis (bukan gap).
30. **GAP-274 sampai GAP-278 sudah ditutup PRD owner (2026-09-30) dan spec disesuaikan.** Access Default User derived dan terkunci (spec 027 memverifikasi checkbox Access Disabled), link konfirmasi yang tidak live menghasilkan 410 (spec 025, 028, 050), toast Edit ubah email memakai toast standar (spec 025), batas Temporary Until adalah besok (spec 034, 036), dan Dialog Blok "Limit Reached" (spec 040). `tc-user.md` digabung dengan versi remote: TC-23, 27, 28, 29, 66, 333 mengikuti keputusan PRD, dengan koreksi Auto-Deactivate (TC-67), foto (TC-75, 76), dan Audit Log (TC-143, 144, 146) dari sesi ini.
31. **GAP-279 (baru): teks badge Pending Email tidak konsisten di dalam `user.md`.** [F-USER-03] versi baru menulis badge "Pending Email Change", sedangkan §3, §4.1, §4.2, dan API menulis "Pending Email Confirmation". TC-27 dan 28 serta spec 025, 028, 050 memakai "Pending Email Confirmation" sampai PRD owner memutuskan.
32. **Section 4b, 4c, 4d, 4g diproses menjadi spec 054–066 (2026-09-30).** Tab Role (054–058), Responsibilities (059–061), Non-Login User (062–063), dan inline-edit Custom Field (064–066). Selaras PRD kecuali dua temuan: `GAP-281` (empty state Tab Role tidak didefinisikan dan bertentangan dengan 6 baris tetap, sehingga TC-99 tidak masuk spec) dan PRD `user.md` §4.1 menyebut tabel Tab Role "sortable" sedangkan §4.2a menyebut tanpa sort (spec 054 mengikuti §4.2a dan TC-355).
33. **Antrean `Mode: mock` bertambah dari Section 4:** TC-577 (Save custom field gagal server), TC-536 (tampilan Phone), dan Section 4a (382–386, 502–504) serta 4e, 4f, 4h yang belum dibahas. Teks TC-121 menyebut `404 field_not_found` yang tidak ada di `user.md`; spec 066 hanya memverifikasi perilaku FE.
34. **GAP-282 (baru): empty state Tab Responsibilities Principal dengan nol approval ambigu.** `user.md` §7 punya baris empty global dan empty Pending Approvals yang sama-sama berlaku untuk entity dengan satu sub-tab. Bagian Principal TC-548 dikeluarkan dari spec 061 sampai PRD owner memutuskan.
35. **Section 4a, 4e, 4f, 4h diproses menjadi spec 067–075 (2026-09-30).** TC-113 ditambahkan sebagai langkah di spec 050, TC-115 di spec 037, dan TC-114 dicatat di sourceTc spec 035 (baris Changelog-nya sudah diverifikasi di sana). Spec 075 adalah spec hanya-FE pertama (`Mode: mock`).
36. **`TC-GS-USER-117` dikoreksi ke PRD §4.1 (Changelog `tc-user.md` 2026-09-30 (9)).** Expected lama menyebut data di halaman yang sama ter-update, sedangkan PRD tegas klik opsi Product Selector adalah navigasi penuh ke Detail User produk tujuan.
37. **GAP-294 (baru): warna badge User Type (selain Non Login) tidak didefinisikan di PRD.** TC-122, 123, 124, 426 menyebut warna; spec 072 hanya memverifikasi teks badge.
38. **Contoh IP TC-356 tidak membedakan sort string dan numerik.** `10.0.0.1` dan `192.168.1.5` berurutan sama pada kedua cara. Spec 068 memakai `9.1.1.1` dan `10.0.0.1`. Contoh di `tc-user.md` belum diubah.
39. **Antrean `Mode: mock` dan sisa Section 1, 3, 5 diproses menjadi spec 076–116 (2026-09-30).** Kegagalan server (077–080), latensi (076), dua sesi (081, 082), bypass DOM (083, 084), dialog bulk (085), foto (086–088), Setup Column User List (089–093), tampilan dan perilaku List (094–101), tab log (102, 103), Guided Tooltip dan A11y (104, 105), input Custom Field (106–108), dan Modal Changelog List (109–116). Per-kolom Setup Column dan Modal Changelog digabung per aksi karena perilakunya identik untuk semua kolom.
40. **`TC-GS-USER-465` dikoreksi ke PRD §7 (Changelog `tc-user.md` 2026-09-30 (10)).** Toast `"Failed to update user."` diganti `"Error, failed to update user."`.
41. **GAP-295 (baru): placeholder search box User List tidak didefinisikan di PRD.** TC-126 mengharapkan `"Search name or email..."`; spec 094 tidak memverifikasi teks placeholder.
42. **Sisa belum ada spec (2026-09-30):** TC-GS-USER-99 (ditahan `GAP-281`), TC-GS-USER-173 dan 176 (hanya BE), dan bagian Distributor dan Partner dari TC-15 (belum ada TC). Semua TC lain sudah tercatat di sourceTc salah satu spec (dicek dengan skrip terhadap 546 TC).
