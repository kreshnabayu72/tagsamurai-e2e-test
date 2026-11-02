---
id: TC-AC-RP-E2E-110-multi-konteks-race-dua-sesi
title: "Multi-Konteks: Dua Reviewer Approve Bersamaan, Permission Baru pada Sesi Paralel, Dua Admin Edit Cell Sama, dan Dua Assign Bersamaan"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-RP-365
  - TC-AC-RP-370
  - TC-AC-RP-406
  - TC-AC-RP-409
coverage:
  web: automated
---

# Multi-Konteks: Dua Reviewer Approve Bersamaan, Permission Baru pada Sesi Paralel, Dua Admin Edit Cell Sama, dan Dua Assign Bersamaan

## Prerequisites

- Mode: FE+BE (backend nyata; seeding via API).
- Akun aktor Sesi A: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`, Pre-setup #1), password dari `Spectra.env.AC_RP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza).
- Konteks browser kedua (Sesi B, kelas c; hasil di Sesi B diasersi sehingga bukan pemicu): dibuka dan ditutup per blok TC dengan sesi login browser terkait dihapus (S-09). Akun Sesi B: Group Manager `Fajar Nugroho` (Pre-setup #6, `Spectra.env.AC_RP_GM_PASSWORD`) pada TC-AC-RP-365; Standard `John Dohan` (peran `Manage device master data` C/R/U; Pre-setup #15) pada TC-AC-RP-370; Total Control kedua (Admin B, Pre-setup #24) pada TC-AC-RP-406 dan TC-AC-RP-409. Email dan password `John Dohan` dan Admin B tidak tertulis di Pre-setup TC: disediakan tim FE (lihat Temuan untuk QA). Dua sesi paralel mengikuti Pre-setup #24.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #11 (tree group Principal), #12 (`Alex Tan`, `John Dohan`), #14 dan #15 (penugasan GM dan peran individual), #17 (toggle `Region Jawa` ON), #24 (dua sesi browser paralel), dan #26 (Device Allocation, Approvals, Device Master Data).
- Data Dinamis: allocation C `Waiting for Approval` di `Region Jawa` (toggle ON) untuk TC-AC-RP-365 dibuat di hook `before` lewat seeding API (kemampuan disediakan tim BE/FE), identitas unik per run dengan suffix `+{runId}-110`, dan dibersihkan di hook `after`. Target aksi TC-AC-RP-370, TC-AC-RP-406, dan TC-AC-RP-409 adalah user Pre-setup bernama literal (S-06).
- Kemampuan teknis: modal Changelog `Manage distributor` (Table Tools) untuk baseline jumlah entri (langkah 33); jumlah dibaca sebelum aksi karena Changelog adalah audit trail permanen (S-12).
- Pemulihan baseline: data Pre-setup dan Data Dinamis yang diubah spec ini dipulihkan ke kondisi Tabel Data Uji Pre-setup TC lewat kemampuan reset yang disediakan tim FE/BE, dijalankan di hook `before` dan `after` spec ini serta sebagai langkah penghubung "Pulihkan baseline" antar blok TC (dinyatakan di `suite.md`; pengecualian S-06 untuk data Pre-setup bersama). Efek yang tidak dipulihkan: Modified By, Last Updated, dan audit trail (Changelog, System Log, Activity Log) bertambah.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Env var yang dipakai spec ini (`AC_RP_TC_PASSWORD`, `AC_RP_GM_PASSWORD`) baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`); spec ini mengubah state bersama.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.

## Test Steps

### TC-AC-RP-365: Dua reviewer approve hampir bersamaan

1. Sesi A: buka Approvals > Device Allocation lalu buka allocation C
2. Sesi B: buka konteks browser kedua dan login sebagai GM `Fajar Nugroho` (`Spectra.env.AC_RP_GM_PASSWORD`)
3. Sesi B: buka Approvals > Device Allocation lalu buka allocation C
4. Sesi A dan Sesi B klik Approve hampir bersamaan
5. Verifikasi allocation C berstatus `Approved`
6. Verifikasi tepat satu dari kedua sesi menampilkan dialog konflik "Approval cannot be made"
7. Tutup dialog konflik, lalu tutup konteks browser Sesi B beserta sesi loginnya

### TC-AC-RP-370: Permission baru berlaku pada request berikutnya

8. Sesi B: buka konteks browser kedua dan login sebagai `John Dohan`
9. Sesi B: buka menu Device Master Data
10. Sesi A: buka halaman `Settings > Role & Permission` lalu klik tab `System`
11. Sesi A: pada section Global Role, klik `⋯` pada baris `Manage device master data` lalu klik `Detail`
12. Sesi A: centang D baris `John Dohan`
13. Tunggu aksi selesai (Sesi A tersimpan)
14. Sesi B: muat ulang halaman (F5)
15. Verifikasi sesi `John Dohan` tidak di-logout (menu Device Master Data tampil)
16. Verifikasi hak Delete berlaku pada request berikutnya (aksi Delete tersedia bagi `John Dohan`)
17. Pulihkan baseline: D `John Dohan` pada `Manage device master data` dicabut, lalu tutup konteks browser Sesi B beserta sesi loginnya

### TC-AC-RP-406: Dua admin mengedit cell CRUD yang sama: last-write-wins

18. Sesi A: muat ulang halaman Detail Role `Manage device master data` (F5)
19. Sesi B: buka konteks browser kedua dan login sebagai Total Control kedua (Admin B)
20. Sesi B: buka halaman `Settings > Role & Permission`, klik tab `System`, lalu pada section Global Role klik `⋯` pada baris `Manage device master data` dan klik `Detail`
21. Sesi A: centang D baris `John Dohan`
22. Tunggu aksi selesai (Sesi A tersimpan)
23. Sesi B (render sebelum perubahan Sesi A): hapus centang D baris `John Dohan`
24. Verifikasi tidak ada dialog konflik pada Sesi B
25. Tunggu aksi selesai (Sesi B tersimpan)
26. Sesi A: muat ulang halaman (F5)
27. Sesi B: muat ulang halaman (F5)
28. Verifikasi D baris `John Dohan` tidak tercentang di Sesi A (nilai yang terakhir diterima server berlaku)
29. Verifikasi D baris `John Dohan` tidak tercentang di Sesi B (nilai yang terakhir diterima server berlaku)

### TC-AC-RP-409: Satu user tidak dapat memiliki dua assignment role yang sama

30. Sesi A: buka halaman `Settings > Role & Permission`, klik tab `System`, lalu pada section Group Role klik `⋯` pada baris `Manage distributor` dan klik `Detail`
31. Sesi B: buka halaman `Settings > Role & Permission`, klik tab `System`, lalu pada section Group Role klik `⋯` pada baris `Manage distributor` dan klik `Detail`
32. Sesi A: buka modal Changelog `Manage distributor` lewat Table Tools
33. Sesi A: catat jumlah entri Changelog sebagai baseline
34. Sesi A: tutup modal Changelog
35. Sesi A dan Sesi B masing-masing: klik `+ Assign`, pilih group `Sumatera`, dan centang `Alex Tan`
36. Sesi A dan Sesi B klik `[Assign]` hampir bersamaan
37. Verifikasi hanya satu baris `Alex Tan` — `Sumatera`
38. Verifikasi tepat satu dari kedua sesi menampilkan alert "Alex Tan is no longer eligible. Please select another." (`V-09`) dan Assign kedua ditolak seluruhnya
39. Sesi A: buka modal Changelog `Manage distributor` lewat Table Tools
40. Verifikasi Changelog hanya menambah satu entri Assign dibanding baseline langkah 33
41. Sesi A: tutup modal Changelog
42. Pulihkan baseline: D `John Dohan` dan penugasan `Alex Tan` — `Sumatera` dikembalikan, lalu tutup konteks browser Sesi B beserta sesi loginnya

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Alasan spec melewati sekitar 35 langkah (bagian 3 prinsip 13, `## Notes` wajib): keempat blok TC adalah kelas yang sama (multi-konteks, dua sesi paralel), tiap blok berdiri sendiri dengan konteks Sesi B yang dibuka dan ditutup sendiri serta pemulihan baseline sendiri, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; memecahnya hanya menambah login, hook, dan cleanup tanpa pemisah nyata.
- Penyimpangan urutan (S-10): TC-AC-RP-365 (allocation), TC-AC-RP-370 (D `John Dohan`), TC-AC-RP-406 (D `John Dohan`), dan TC-AC-RP-409 (Assign) dikelompokkan menurut permukaan; TC-AC-RP-370 dari bagian 7a ditempatkan di spec kelas c ini karena hasil di sesi `John Dohan` diasersi.
- Langkah penghubung (S-03, S-09): langkah 33 (baseline Changelog), langkah 17 dan 42 (pemulihan baseline dan penutupan konteks Sesi B); langkah "Tunggu aksi selesai" sesudah aksi yang hasilnya tidak diasersi (bagian 8b butir 8).
- Jendela SSE: tidak ada asersi absence atas propagasi antar-tab; "tidak ada dialog konflik" (TC-AC-RP-406) diasersi segera sesudah pemicu pada Sesi B.
- Temuan untuk QA:
  - Email dan password `John Dohan` dan Admin B (Pre-setup #24) tidak tertulis di Pre-setup TC (S-11): disediakan tim FE.
  - TC-AC-RP-365, 370, 406, dan 409 berautomation `Manual Only — (d) dua sesi paralel` (TC-AC-RP-370 dan 365 pada kolom Automation); spec memakai konteks browser kedua sehingga dapat diotomasi dan hasil sesi kedua diasersi.
  - TC-AC-RP-365 tidak menyebut precondition allocation `Waiting for Approval` dan group-nya; spec menyiapkan allocation C di `Region Jawa` (toggle ON) lewat seeding. Expected "Yang pertama menang" tidak menentukan sesi mana yang menang; spec mengasersi tepat satu sesi menampilkan dialog.
  - TC-AC-RP-370 langkah "refresh atau klik Delete" menyebut dua alternatif; spec memakai muat ulang (F5) lalu mengasersi hak Delete tersedia tanpa mengeksekusi Delete (menghindari menghapus data device).
  - TC-AC-RP-406 kontradiktif: pada render Sesi B sebelum perubahan Sesi A, D `John Dohan` belum tercentang sehingga "hapus centang D" tidak mengubah kotak yang sudah kosong; spec tetap mengikuti TC dan menulis langkah apa adanya. Mohon QA menetapkan kondisi awal D yang membuat last-write-wins teramati.
  - TC-AC-RP-409 tidak menyebut sesi mana yang ditolak dan surface Changelog yang dihitung; spec memakai modal Changelog `Manage distributor` dan mengasersi tepat satu sesi menampilkan alert V-09.
  - Mekanisme "dipulihkan automation baseline" (Post Condition TC) tidak didefinisikan di TC, PRD, atau LLD; spec menyebutnya kemampuan reset yang disediakan tim FE/BE (S-13).
