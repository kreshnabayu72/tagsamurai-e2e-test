# Coverage E2E — Global Settings > User

Sumber: `global-settings/user/TestCases/tc-user.md`. Cakupan saat ini: section 3a (Create), 42 TC granular (35 tercakup di 14 spec, 7 dicakup TC frontend, sisi Distributor dan Partner pada TC-15 belum ada).
Suite: `specs/GlobalSettings/User/`. Status semua spec: `draft`, belum ada script.

## TC granular → spec e2e

| Spec | TC sumber |
|---|---|
| TC-GS-USER-E2E-001 | TC-GS-USER-13, 20, 469, 471, 473 |
| TC-GS-USER-E2E-002 | TC-GS-USER-468, 470, 472, 474, 476 |
| TC-GS-USER-E2E-003 | TC-GS-USER-65, 346 |
| TC-GS-USER-E2E-004 | TC-GS-USER-341, 489 |
| TC-GS-USER-E2E-005 | TC-GS-USER-14, 15 (bagian Client), 25, 457 |
| TC-GS-USER-E2E-006 | TC-GS-USER-16, 17, 19 |
| TC-GS-USER-E2E-007 | TC-GS-USER-192, 420 |
| TC-GS-USER-E2E-008 | TC-GS-USER-18, 340 |
| TC-GS-USER-E2E-009 | TC-GS-USER-347, 482 |
| TC-GS-USER-E2E-010 | TC-GS-USER-22, 431, 487 |
| TC-GS-USER-E2E-011 | TC-GS-USER-191, 440 |
| TC-GS-USER-E2E-012 | TC-GS-USER-21 |
| TC-GS-USER-E2E-013 | TC-GS-USER-15 (bagian Principal), 467 |
| TC-GS-USER-E2E-014 | TC-GS-USER-475 |

## TC yang tidak dijadikan spec

| TC | Alasan |
|---|---|
| TC-GS-USER-23, 24, 193, 342, 343, 344, 345 | Sudah dicakup TC frontend (TC-GS-USER-FE-037, 038, 043, 046, 047, 048, 049) |
| TC-GS-USER-15 (bagian Distributor dan Partner) | Hanya entity Principal yang dicakup spec 013. Belum ada TC lain untuk Distributor dan Partner |

## Temuan untuk QA (sumber TC, bukan spec)

1. **Nama field tidak konsisten (sudah diperbaiki di `tc-user.md` 2026-09-26).** TC-GS-USER-13 dan 14 menyebut "Full Name", sedangkan TC-16, 192, dan 420 memakai First Name dan Last Name. PRD `user.md` baris 411 menetapkan form Create memakai First/Last Name\* (maks 120), dan "Full Name" hanya untuk tampilan tabel dan header Detail. Spec mengikuti PRD. `tc-user.md` TC-13, TC-14, dan TC-254 sudah disesuaikan.
2. **Division wajib (sudah diperbaiki di `tc-user.md` 2026-09-26).** PRD `user.md` baris 411 dan 853 menetapkan Division wajib dengan error "Division must not be empty". TC-14 tidak menandai Division dengan `*`. Spec memperlakukan Division wajib. TC-14 sekarang menandai Division, First Name, Last Name, Email, dan Access sebagai wajib.
3. **Data pre-setup belum tercatat (masih terbuka).** Custom Field `Blood Type` (TC-25) dan user dengan Employee ID `EMP-001` (TC-340) dipakai sebagai precondition, tetapi tidak ada di tabel Data Uji Pre-setup `tc-user.md`. Perlu dipastikan datanya ada di environment QA.
4. **(Masih terbuka.) TC-18 mencakup duplikasi lintas Login dan Non-Login User**, tetapi datanya hanya user Login ("Doni Pratama"). Varian duplikat terhadap Non-Login User belum punya data uji, dan spec 008 hanya menguji sisi Login.
5. **Teks toast.** TC-13 dan TC-489 menyebut "User created successfully.". Spec memakai teks ini.
6. **TC-GS-USER-196 dan 418 memakai "Full Name" gabungan pada Edit dan Changelog (sudah diperbaiki di `tc-user.md` 2026-09-26).** PRD `user.md` baris 989: di Edit, First Name dan Last Name adalah field terpisah, dan Changelog mencatat 1 baris per field yang berubah. Kedua TC sekarang memakai Last Name dengan Changelog `Field=Last Name, Old, New`. Tidak memengaruhi spec e2e section Create.
7. **Label checkbox Create tidak konsisten (sudah diperbaiki di `tc-user.md` 2026-09-26).** TC-GS-USER-21 memakai "Create another" di langkah dan "Stay on this form after submitting" di Expected, dan TC-GS-USER-255 memakai "after creating". Label kanonik "Stay on this form after submitting" (`foundation/functions/toast-copy.md` dan PRD `user.md` baris 411). TC-21 dan TC-255 sudah diseragamkan, dan TC-21 kini menyebut toast "User created successfully." pada save pertama.
8. **TC-GS-USER-91 terpecah jadi dua baris tabel (sudah diperbaiki di `tc-user.md` 2026-09-26).** Ada line break nyata di dalam sel Expected, sehingga hanya 5 dari 15 kolom terbaca. Diganti literal `\n` mengikuti PRD `user.md` baris 1161. Setelah perbaikan, semua baris TC di `tc-user.md` berjumlah 15 kolom.
9. **TC-GS-USER-192 menyebut "emoji atau simbol tidak diizinkan", padahal konvensi platform hanya memblok emoji (sudah diperbaiki di `tc-user.md` 2026-09-26).** `foundation/process/prd-process/prd-conventions.md` bagian "Karakter yang Diizinkan (Name Fields)" menetapkan pendekatan blocklist: hanya emoji yang diblok di input, semua karakter cetak lain (termasuk simbol) diizinkan. Ini bukan gap PRD, sehingga tidak dicatat di `prd-gap-registry.md`. TC-192 diperbaiki: hanya emoji diblok, ditambah langkah dan data `Budi-O'Neil` yang harus tetap bisa diketik. Spec 007 langkah 4 memverifikasinya.
10. **TC-GS-USER-467 dan 475 kini diotomasi (spec 013 dan 014).** Spec 014 butuh scan RFID hardware yang tidak bisa dilakukan browser, dan spec 013 butuh akun Total Control di entity Principal. Kelayakan keduanya untuk dijalankan belum dikonfirmasi dan dinilai saat tahap script.
