---
id: TC-AC-CS-E2E-122-subscription-log-modal-dan-header
title: "Subscription Log: Modal dan Header"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-587
  - TC-AC-CS-588
  - TC-AC-CS-589
coverage:
  web: automated
---

# Subscription Log: Modal dan Header

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun pemicu lewat sesi API (bukan sesi UI): Create-Only Distributor (Pre-setup #6) `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`), password `Spectra.env.AC_SUB_CREATE_PASSWORD`.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Data milik spec, dibuat lewat API di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-122`). Tidak ada baris Pre-setup bersama yang ditulis spec ini:
  1. Pengajuan `{idPengajuan}` (setara `SUBS-20260819-00001`, #49): Client `Apotek Sehat Sentosa+{runId}-122`, FAMS, plan Growth, Duration `1` year(s), Waiting for Approval, tanggal - / -, Plan Owner PT Maju Bersama, riwayat Add Subscription oleh `Fajar Nugroho`. Subscription ID dibaca lewat API seeding.
  2. Term `{idAktif}` (setara `SUBS-20260101-00001`, #61): Client `PT Sejahtera+{runId}-122`, FAMS, plan Professional, Active, 01/01/26 sampai 31/12/26, Plan Owner PT Maju Bersama. Subscription ID dibaca lewat API seeding.
- Riwayat `{idPengajuan}` memuat entri Edit Duration `1 year(s)` menjadi `2 year(s)` oleh `Fajar Nugroho`; entri itu dibuat oleh langkah pemicu lewat sesi API aktor (aksi pada kolom Dependensi TC-AC-CS-223). Seed dibersihkan di hook `after`; entri audit trail yang terbentuk bersifat permanen.
- Kemampuan teknis (disediakan tim FE/BE): sesi API aktor Create-Only; membaca isi clipboard; membaca jumlah entri Subscription Log, Changelog, dan Activity Log sebelum dan sesudah aksi (audit trail permanen, jumlah dibaca sebagai baseline per surface, S-12).
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`; pemulihan state Pre-setup oleh fixture backend. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-587: Screening modal Subscription Log dari row action List

1. Picu lewat sesi API aktor `Fajar Nugroho`: Edit Duration `{idPengajuan}` dari `1` menjadi `2` hingga perubahan tersimpan
2. Klik menu `Client Subscription` di sidebar sampai List termuat ulang pada tab `Current` (langkah penghubung)
3. Ketik Search `{idPengajuan}`, tekan Enter
4. Klik ikon `⋯` pada baris `{idPengajuan}`
5. Klik `Subscription Log`
6. Verifikasi judul "Subscription Log" diikuti Subscription ID `{idPengajuan}` dan ikon Copy di kanan ID
7. Verifikasi `Status:` badge Waiting for Approval dengan severity warning
8. Verifikasi `Client:` Apotek Sehat Sentosa+{runId}-122
9. Verifikasi `Product:` FAMS
10. Verifikasi `Plan:` Growth
11. Verifikasi riwayat tampil sebagai daftar kronologis
12. Verifikasi riwayat bukan tabel
13. Verifikasi entri terbaru di atas
14. Verifikasi tiap entri memuat baris judul `[Event] by [PIC]`
15. Verifikasi Date & Time tiap entri berformat General Settings (`dd/MM/yy HH:mm`)
16. Verifikasi entri teratas `Subscription edited by Fajar Nugroho` dengan baris Description `Duration: 2 year(s)`
17. Verifikasi entri terbawah `Subscription created by Fajar Nugroho` dengan baris Description `Type: Paid`, `Plan: Growth`, `Duration: 1 year(s)`, dan `Start Date`
18. Verifikasi tidak ada Search pada modal
19. Verifikasi tidak ada Filter pada modal
20. Verifikasi tidak ada Sort pada modal
21. Verifikasi tidak ada Setup Column pada modal
22. Verifikasi tidak ada Download pada modal
23. Verifikasi tidak ada paginasi pada modal
24. Verifikasi tidak ada footer pada modal
25. Verifikasi tidak ada tombol `[Close]` pada modal
26. Scroll daftar log ke bawah
27. Verifikasi header modal tetap di atas saat daftar di-scroll
28. Verifikasi judul entri tampil sebagai teks biasa, bukan badge

### TC-AC-CS-588: Ikon Copy Subscription ID pada header modal Subscription Log

29. Klik `[✕]` pada modal (langkah penghubung)
30. Catat baseline jumlah entri Subscription Log `{idAktif}`, Changelog, dan Activity Log (kemampuan baca jumlah)
31. Ganti isi kotak search dengan `{idAktif}`, tekan Enter (langkah penghubung)
32. Klik ikon `⋯` pada baris `{idAktif}`, klik `Subscription Log`
33. Arahkan kursor ke ikon Copy
34. Verifikasi tooltip "Copy to clipboard" tampil
35. Klik ikon Copy
36. Verifikasi tooltip inline "Copied to clipboard" tampil dan bukan toast
37. Verifikasi clipboard berisi `{idAktif}`
38. Tunggu 2 detik
39. Verifikasi tooltip "Copied to clipboard" menutup
40. Klik `[✕]` lalu buka kembali Subscription Log `{idAktif}` lewat row action
41. Verifikasi jumlah entri Subscription Log `{idAktif}`, Changelog, dan Activity Log sama dengan baseline langkah 30

### TC-AC-CS-589: Modal Subscription Log ditutup lewat silang atau Esc dan tidak punya tombol Close

42. Verifikasi header modal memuat tombol silang `[✕]`
43. Verifikasi modal tidak punya footer maupun tombol `[Close]`
44. Klik `[✕]`
45. Verifikasi modal tertutup
46. Verifikasi List tab `Current` tampil dengan Search `{idAktif}` masih terisi (state non-default yang diset pada langkah 31)
47. Klik ikon `⋯` pada baris `{idAktif}`, klik `Subscription Log`, tekan `Esc`
48. Verifikasi modal tertutup
49. Verifikasi List tab `Current` tampil dengan Search `{idAktif}` masih terisi (state non-default yang diset pada langkah 31)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): langkah 2 (memuat ulang List sesudah pemicu API), langkah 3 dan 31 (Search untuk menemukan baris target, R-16; Search pada langkah 31 menjadi state non-default untuk Verifikasi langkah 46 dan 49), langkah 29 (menutup modal), langkah 40 (menutup dan membuka kembali modal, bagian Expected d TC-AC-CS-588), dan langkah 47 (membuka modal untuk menguji `Esc`).
- Spec ini melewati ~35 langkah (49). Alasan: satu topik (modal Subscription Log) dan satu permukaan dengan seed yang sama; kenaikan dari pemecahan Verifikasi per klausa (S-01), bukan dari TC tambahan, dan pemecahan hanya menambah login dan hook.
- Langkah 1 adalah pemicu pelaku kedua lewat sesi API (R-20), bukan konteks UI kedua; `P-2` tidak dipakai.
- Temuan untuk QA:
  - TC-AC-CS-587 dan TC-AC-CS-588 bergantung pada riwayat yang dibuat TC lain (Dependensi TC-AC-CS-223); endpoint tulis untuk memicunya tidak tertulis di TC, PRD, atau LLD, sehingga ditulis sebagai kemampuan sesi API aktor yang disediakan tim FE/BE (S-13).
  - TC-AC-CS-588 Expected d menyebut "Activity Log" tanpa menyebut lokasi surface-nya; spec memakai kemampuan baca jumlah entri yang disediakan tim FE/BE.
  - TC-AC-CS-589 Expected b menyebut "filter, sort, dan paginasi tidak berubah" tanpa menyebut state awal non-default; spec menyetel Search `{idAktif}` sebelum modal dibuka dan hanya Search itu yang diasersi tidak berubah. Filter, sort, dan paginasi non-default perlu dinyatakan TC.
  - TC-AC-CS-587 Expected c ("tanpa footer") dan TC-AC-CS-589 Expected a (modal tidak punya footer maupun `[Close]`) tumpang tindih; keduanya diasersi di tempatnya masing-masing.
