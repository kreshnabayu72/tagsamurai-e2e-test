---
id: TC-AC-ACAL-E2E-045-pencatatan-aksi-modul-ac-create-edit-tiga-field-delete-dan-event-sesi
title: "Pencatatan Aksi Modul AC: Create, Edit Tiga Field, Delete, dan Event Sesi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACAL-143
  - TC-AC-ACAL-144
  - TC-AC-ACAL-145
  - TC-AC-ACAL-147
coverage:
  web: automated
---

# Pencatatan Aksi Modul AC: Create, Edit Tiga Field, Delete, dan Event Sesi

## Prerequisites

- Mode: FE+BE.
- Suite serial (`parallel: false`); spec ini menghapus Brand sumber dan dijalankan paling akhir bersama spec 046 (suite.md); hook suite dinyatakan di suite.md.
- Guided Tooltip: hook suite before/after menyetel flag seen halaman Activity Log untuk akun Total Control Principal (lihat suite.md). Untuk akun Total Control Distributor Alfa, hook before/after spec ini menyetel dan memulihkan flag seen yang sama (kemampuan disediakan tim FE/BE).
- Akun aktor (password tidak ditulis di spec atau fixture; di antara nama env AC_* hanya `AC_TC_PASSWORD` yang sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`, nama lain adalah usulan tim FE (lihat Temuan untuk QA)):

| Akun | Email | Env var password |
|---|---|---|
| Total Control (Principal), akun hook `before` | `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1) | `Spectra.env.AC_TC_PASSWORD` |
| Staf `John Doe {runId}-045` (Distributor Alfa), dinamis | `Fixture.activityLog.emailJohnDoe045` (ditetapkan tim FE) | `Spectra.env.AC_DYN_PASSWORD` |
| Total Control (Distributor Alfa) | `totalControlAdminConsoleDistributorAlfa_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 7) | `Spectra.env.AC_ALFA_TC_PASSWORD` |

- Login akun pertama (Total Control Principal) di hook `before` spec ini; halaman Admin Console > Activity Log (tab Session) dibuka hook `beforeEach` suite. Spec berakhir di akun Total Control Distributor Alfa; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal).
- Akses Global Settings: Brand dikelola di Global Settings > Master Reference > Brand (foundation Admin Console), sehingga akun Total Control (Principal) harus dapat membuka Global Settings > Master Reference dan menghapus Brand; akses itu disediakan tim FE/BE (lihat Temuan untuk QA). Spec tidak mengganti akun untuk langkah 26 sampai 28.
- Data Dinamis (suffix per run dan nomor spec, bagian 5 konvensi), dibuat lewat sesi API di hook `before`:
  - Distributor `PT Nusantara Jaya {runId}-045` dibuat lewat UI pada langkah 1 sampai 4 (pengganti `PT Nusantara Jaya` Dinamis No 1). Nilai field wajib Distributor selain Company Name mengikuti PRD Distributor dan disediakan tim FE (TC tidak menyebutnya). Lifecycle TC: tetap ada; hook `after` menghapusnya lewat API bila kemampuan itu tersedia.
  - Client `PT Sejahtera {runId}-045` dengan PIC Name awal `PIC Awal {runId}-045`, PIC Email awal `pic.awal+{runId}-045@qwertysystem.net`, dan Address awal `Alamat Awal {runId}-045` (pengganti `PT Sejahtera`).
  - Brand `Acme {runId}-045` (pengganti Brand `Acme` Dinamis No 2; Pre-setup dihapus di TC), dihapus pada langkah 26 sampai 28.
  - User `John Doe {runId}-045` (First Name `John`, Last Name `Doe {runId}-045`; singkatan `John D`), staf Distributor Alfa, belum punya baris Session sebelum langkah 33 (baseline nol, nama bersuffix unik).
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus lewat API Client, Brand, user, dan Distributor dinamis di atas bila masih ada. Entri log tidak dapat dihapus; nama bersuffix run.
- Kemampuan teknis (disediakan tim FE/BE): sesi API pembuatan Client, Brand, dan user dinamis; baseline tidak diperlukan karena nama bersuffix unik (baseline nol, S-12).
- Nama tampil Principal di kolom Modified By: `Fixture.activityLog.modifiedByPrincipalTc` (ditetapkan tim FE).
- Tidak ada state global yang diubah selain data milik spec.

## Test Steps

### TC-AC-ACAL-143: Aksi Create di modul AC tercatat dengan Old Value kosong

1. Buka Admin Console > Distributor, lalu buka form Create Distributor
2. Isi Company Name dengan `PT Nusantara Jaya {runId}-045` dan field wajib lain sesuai Prerequisites
3. Klik [Submit]
4. Tunggu aksi selesai: form Create tertutup atau tombol [Submit] aktif kembali
5. Buka Admin Console > Activity Log > User Action
6. Ketik Search `PT Nusantara Jaya {runId}-045`, tekan Enter
7. Verifikasi baris Action `Create`, Object `Distributor`, Name `PT Nusantara Jaya {runId}-045`, Field `Company Name`, Old Value `—`, New Value `PT Nusantara Jaya {runId}-045`, dan Modified By `Fixture.activityLog.modifiedByPrincipalTc` tampil
8. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-AC-ACAL-144: Satu Save yang mengubah tiga field menghasilkan tiga entri

9. Buka Admin Console > Client, ketik Search `PT Sejahtera {runId}-045`, tekan Enter, lalu buka form Edit pada baris itu
10. Ubah PIC Name menjadi `PIC Baru {runId}-045`, PIC Email menjadi `pic.baru+{runId}-045@qwertysystem.net`, dan Address menjadi `Alamat Baru {runId}-045`; field lain tidak disentuh
11. Klik [Save]
12. Tunggu aksi selesai: form Edit tertutup atau tombol [Save] aktif kembali
13. Buka Admin Console > Activity Log > User Action
14. Klik icon Filter, pilih Action `Edit`, klik [Apply]
15. Ketik Search `PT Sejahtera {runId}-045`, tekan Enter
16. Verifikasi hasil memuat tepat tiga entri `Edit` `Client` `PT Sejahtera {runId}-045` (footer `Showing 1–3 of 3 entries`)
17. Verifikasi ketiga entri bertanggal sama
18. Verifikasi entri Field `PIC Name` memuat Old Value `PIC Awal {runId}-045` dan New Value `PIC Baru {runId}-045`
19. Verifikasi entri Field `PIC Email` memuat Old Value `pic.awal+{runId}-045@qwertysystem.net` dan New Value `pic.baru+{runId}-045@qwertysystem.net`
20. Verifikasi entri Field `Address` memuat Old Value `Alamat Awal {runId}-045` dan New Value `Alamat Baru {runId}-045`
21. Verifikasi ketiga entri tampil dengan tiga Field berbeda `PIC Name`, `PIC Email`, dan `Address`
22. Verifikasi tidak ada entri ganda
23. Verifikasi tidak ada entri untuk Field lain
24. Klik icon Filter, klik [Clear Field], lalu klik [Apply]
25. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-AC-ACAL-145: Aksi Delete tercatat dengan New Value kosong

26. Buka Global Settings > Master Reference > Brand, ketik Search `Acme {runId}-045`, tekan Enter, lalu buka dialog Delete pada baris itu
27. Klik [Delete] pada dialog konfirmasi
28. Tunggu aksi selesai: dialog Delete tertutup
29. Buka Admin Console > Activity Log > User Action
30. Ketik Search `Acme {runId}-045`, tekan Enter
31. Verifikasi baris Action `Delete`, Object `Brand`, Name `Acme {runId}-045`, Field `Brand Name`, Old Value `Acme {runId}-045`, dan New Value `—` tampil
32. Klik `(←)` pada kotak Search untuk menutup Search dan mereset tabel

### TC-AC-ACAL-147: Event buka/tutup Admin Console tercatat di Tab Session

33. Ganti akun: logout, lalu login platform sebagai staf `John Doe {runId}-045` dengan `Spectra.env.AC_DYN_PASSWORD`
34. Klik card Admin Console di Portal
35. Logout
36. Login sebagai Total Control (Distributor Alfa) dengan `Spectra.env.AC_ALFA_TC_PASSWORD`
37. Buka Admin Console > Activity Log > Session
38. Ketik Search `John Doe {runId}-045`, tekan Enter
39. Verifikasi baris Note `Session started` milik `John D` tampil
40. Verifikasi baris Note `Session ended` milik `John D` tampil

## Notes

- Sumber TC: `admin-console/activity-log/TestCases/tc-activity-log.md` (TC-AC-ACAL-143, 144, 145, 147).
- Urutan TC di spec berbeda dari urutan sumber: TC-AC-ACAL-145 (Delete Brand) ditaruh sesudah TC-AC-ACAL-143 dan 144 (aksi yang menghabisi data setelah kasus lain di akun Principal), lalu TC-AC-ACAL-147 terakhir karena berganti akun ke staf dan Distributor Alfa; Brand `Acme {runId}-045` tidak dipakai lagi sesudah langkah 32.
- Spec 40 langkah, di atas smell 35. Alasan: seluruh TC satu topik (pencatatan aksi sumber ke Tab User Action dan Tab Session) dan satu permukaan; tiap blok berdiri sendiri dengan data bersuffix sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung (tanpa awalan `Verifikasi`): membuka modul sumber, form, dan menu (langkah 1, 5, 9, 13, 26, 29, 37), mengisi dan menyimpan form sumber (langkah 2, 3, 10, 11, 27), "Tunggu aksi selesai" (langkah 4, 12, 28; bagian 8b butir 8), mengetik dan menutup Search dan Filter (langkah 6, 8, 14, 15, 24, 25, 30, 32, 38), serta ganti akun dan aksi sesi staf (langkah 33 sampai 36).
- Search nama (langkah 6, 15, 30, 38) dan Filter Action `Edit` (langkah 14) menemukan entri target di antara log lain (R-16); Search di modul sumber (langkah 9 dan 26) menemukan baris Client dan Brand target.
- Baseline: nama bersuffix unik memberi baseline nol; asersi "tepat 3 entri" pada langkah 16 dihitung dalam hasil Filter Action `Edit` dan Search nama (S-12).
- Perilaku Delete Brand pada TC-AC-ACAL-145 (dialog konfirmasi, tombol [Delete]) mengikuti konvensi label tombol; Brand dihapus lewat UI Global Settings > Master Reference > Brand sebagai pemicu entri log.
- Temuan untuk QA:
  - Sumber Tier 2 TC-AC-ACAL-147, `auth/_foundation/auth-foundation.md` (§9.1), tidak ditemukan di workspace; aturan event buka/tutup Admin Console tidak dapat dicek ke sumber. Spec mengikuti Expected c.
  - TC-AC-ACAL-147 Expected a dan b berisi `-` (tanpa Expected); hanya Expected c yang diasersi. Langkah Uji TC tidak menyebut cara menutup Admin Console selain Logout; spec mengikuti dan mengasersi Note `Session ended`.
  - TC-AC-ACAL-143 tidak menyebut field wajib lain Distributor; disediakan tim FE. TC-AC-ACAL-145 tidak menyebut modul tempat Brand dihapus; spec memakai Global Settings > Master Reference > Brand menurut foundation Admin Console. QA diminta mengonfirmasi jalur modul ini.
  - TC-AC-ACAL-144 tidak menyebut nilai PIC Name, PIC Email, dan Address (awal dan baru); spec memakai nilai bersuffix. TC memakai `PT Sejahtera` sedangkan hierarki Pre-setup No 8 memakai `Client Sejahtera`; QA konfirmasi apakah keduanya entitas yang sama.
  - TC-AC-ACAL-147 menyebut `John Doe` (Distributor Alfa) literal; spec memakai nama bersuffix agar tidak bentrok dengan spec lain. Email Pre-setup memakai placeholder `{namaCompany}` password: `AC_TC_PASSWORD` sudah terdaftar di `.env.example` dan `spectra.config.ts`; `AC_ALFA_TC_PASSWORD`, `AC_DYN_PASSWORD` adalah nama usulan tim FE dan belum terdaftar di `.env.example` maupun `spectra.config.ts`.
