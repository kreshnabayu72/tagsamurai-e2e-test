# Coverage E2E — Global Settings > User

Sumber: `global-settings/user/TestCases/tc-user.md`. Cakupan saat ini: section 3a (Create, 42 TC, 35 tercakup di 4 spec, 7 dicakup TC frontend, sisi Distributor dan Partner pada TC-15 belum ada) dan section 3c–3e (Delete, Bulk, Toggle Active, Remove Access, 33 TC, 32 tercakup di 2 spec, 1 dicatat sebagai gap PRD).
Suite: `specs/GlobalSettings/User/`. Status semua spec: `draft`, belum ada script.

## TC granular → spec e2e

| Spec | Isi | TC sumber |
|---|---|---|
| TC-GS-USER-E2E-001 | Screening, validasi, dan menutup modal (2 sesi modal, tidak membuat data) | TC-GS-USER-14, 15 (bagian Client), 25, 457, 16, 17, 19, 192, 420 (121 karakter), 18, 340, 347, 482, 431, 22, 487 |
| TC-GS-USER-E2E-002 | Create sukses: 3 user dalam 1 sesi modal dengan Stay | TC-GS-USER-13, 20, 469, 471, 473, 191, 440, 341, 489, 468, 470, 472, 474, 476, 420 (batas 120), 65, 346, 21 |
| TC-GS-USER-E2E-003 | Entity Principal | TC-GS-USER-15 (bagian Principal), 467 |
| TC-GS-USER-E2E-004 | Scan & Pair TAG | TC-GS-USER-475 |
| TC-GS-USER-E2E-005 | Delete, Select All, Bulk Delete/Deactivate/Activate, Toggle Active, dan Remove Access — semua Role Total Control, entity Client, digabung karena akun/entity/role sama | TC-GS-USER-36, 44, 52, 37, 45, 258, 38, 434, 433, 33, 353, 453, 34, 35, 42, 435, 41, 447, 43, 446, 46, 480, 443, 47, 445, 444, 449, 49, 352, 425, 351, 387, 50 |
| TC-GS-USER-E2E-006 | Deactivate memaksa logout sesi target (dua sesi browser, dua akun) | TC-GS-USER-481 |

TC-15 dan TC-420 terbelah di dua spec (dicatat di `## Notes` kedua spec).

## TC yang tidak dijadikan spec

| TC | Alasan |
|---|---|
| TC-GS-USER-23, 24, 193, 342, 343, 344, 345 | Sudah dicakup TC frontend (TC-GS-USER-FE-037, 038, 043, 046, 047, 048, 049) |
| TC-GS-USER-15 (bagian Distributor dan Partner) | Hanya entity Principal yang dicakup spec 003. Belum ada TC lain untuk Distributor dan Partner |
| TC-GS-USER-39, 40, 451, 452, 48, 53 | Error, race, atau perubahan izin di tengah aksi yang hanya bisa dipicu mock (TC-GS-USER-FE-082, 083, 084, 085, 104, 110) |
| TC-GS-USER-448, 458, 459, 398 | Copy dan state UI murni tanpa efek backend (TC-GS-USER-FE-102, 098, 099, 105) |
| TC-GS-USER-51 | Expected result TC sendiri ambigu ("diblokir ATAU diizinkan"), PRD belum menegaskan salah satu. Dicatat sebagai `GAP-245` di `prd-gap-registry.md`, bukan ditulis spec dengan menebak |

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
| 41 | P0 | FE-087 | E2E-005 |  |
| 435 | P2 | FE-088 | E2E-005 |  |
| 42 | P0 | FE-089 | E2E-005 |  |
| 43 | P1 | FE-090 | E2E-005 |  |
| 44 | P0 | FE-091 | E2E-005 |  |
| 45 | P0 | FE-092 | E2E-005 |  |
| 46 | P2 | FE-093 | E2E-005 |  |
| 47 | P1 | FE-094 | E2E-005 |  |
| 443 | P2 | FE-095 | E2E-005 |  |
| 444 | P1 | FE-096 | E2E-005 |  |
| 445 | P2 | FE-097 | E2E-005 |  |
| 446 | P1 | FE-100 | E2E-005 |  |
| 447 | P2 | FE-101 | E2E-005 |  |
| 448 | P2 | FE-102 | — |  |
| 449 | P1 | FE-103 | E2E-005 |  |
| 451 | P1 | FE-084 | — |  |
| 452 | P1 | FE-085 | — |  |
| 458 | P1 | FE-098 | — |  |
| 459 | P1 | FE-099 | — |  |
| 48 | P2 | FE-104 | — |  |
| 398 | P2 | FE-105 | — |  |
| 49 | P0 | FE-106 | E2E-005 |  |
| 50 | P1 | FE-107 | E2E-005 |  |
| 51 | P2 | FE-108 | — | Dicatat sebagai `GAP-245`, tidak dijadikan spec |
| 52 | P1 | FE-109 | E2E-005 |  |
| 53 | P2 | FE-110 | — |  |
| 351 | P1 | FE-111 | E2E-005 |  |
| 352 | P2 | FE-112 | E2E-005 |  |
| 387 | P1 | FE-113 | E2E-005 |  |
| 425 | P2 | FE-114 | E2E-005 |  |
| 480 | P1 | — | E2E-005 |  |
| 481 | P1 | — | E2E-006 |  |

Semua TC P0 di section ini (33, 36, 37, 41, 42, 44, 45, 49) punya dua lapisan (FE dan E2E), jadi tidak ada P0 satu lapisan di 3c–3e.

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
