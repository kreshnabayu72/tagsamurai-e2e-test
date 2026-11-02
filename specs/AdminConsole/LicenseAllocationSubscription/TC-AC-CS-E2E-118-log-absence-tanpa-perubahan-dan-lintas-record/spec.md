---
id: TC-AC-CS-E2E-118-log-absence-tanpa-perubahan-dan-lintas-record
title: "Log Absence: Tanpa Perubahan dan Lintas Record"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-231
  - TC-AC-CS-458
  - TC-AC-CS-464
coverage:
  web: automated
---

# Log Absence: Tanpa Perubahan dan Lintas Record

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Create-Only (capability Create saja), Distributor PT Maju Bersama (Pre-setup #6) `createOnlySub_automated_{namaCompany}@qwertysystem.net` (`Fajar Nugroho`), password `Spectra.env.AC_SUB_CREATE_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password di atas didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh tim FE, sesuai `suite.md`.
- Suite berjalan serial (`parallel: false`). Hook `beforeEach` suite membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09 (lihat `suite.md`); flag Guided Tooltip diatur hook suite (`seen`), sehingga walkthrough tidak muncul.
- Sesi API aktor: aksi pemicu (kolom Dependensi TC) dijalankan lewat login API akun aktor sesuai `suite.md`; kemampuan menulis lewat API, endpoint, dan payloadnya tidak tertulis di TC, PRD, atau LLD sehingga disediakan tim BE/FE (S-13). Sesi UI aktor tidak terpengaruh (bagian 5).
- Baseline S-12: jumlah entri Changelog, Activity Log, dan System Log per Client, Action, dan user pelaku dicatat di hook `before` lewat kemampuan membaca audit trail (disediakan tim FE/BE, bagian 8b butir 10) sebelum aksi pemicu pertama; Changelog, Activity Log, dan System Log adalah audit trail permanen sehingga asersi "entri baru" memakai selisih terhadap baseline itu dan entri dicari lewat Action, Client, dan email pelaku (bukan posisi teratas).
- Data seed milik spec, dibuat lewat sesi API aktor di hook `before` dan dibersihkan di hook `after` (S-06, S-12; bersuffix `+{runId}-118`). Spec tidak menulis ke baris Pre-setup bersama dan tidak memerlukan langkah pemulihan antar blok; entri audit trail (Changelog, Activity Log, System Log) yang dihasilkan aksi pemicu permanen dan dibaca lewat selisih terhadap baseline. Seed: Client `Apotek Sehat Sentosa+{runId}-118` dengan pengajuan FAMS plan Growth status Waiting for Approval, Plan Owner PT Maju Bersama (Distributor), milik aktor `Fajar N` (bentuk Pre-setup #49), dan term lain Client yang sama berupa term Pending SIEM, Plan Owner PT Maju Bersama (Distributor) (bentuk Pre-setup #90).
- Kelas asersi absence (g): tiap asersi absence didahului `Verifikasi` anchor positif pada permukaan yang sama (bagian 8b butir 2), dengan baseline jumlah entri per surface (S-12). Kemampuan membaca `Modified By` dan `Last Updated` record (TC-AC-CS-458 Expected b) serta pengamat request jaringan browser (TC-AC-CS-231 Expected c) disediakan tim FE/BE.

## Test Steps

### TC-AC-CS-231 dan TC-AC-CS-458: Save tanpa perubahan menampilkan toast netral tanpa log

1. Buka modal Changelog, ketik Search `Apotek Sehat Sentosa+{runId}-118`, tekan Enter, dan catat jumlah entri Client `Apotek Sehat Sentosa+{runId}-118` — FAMS (baseline)
2. Buka Admin Console > Activity Log, saring Object `Client Subscription`, dan catat jumlah entri Client `Apotek Sehat Sentosa+{runId}-118` — FAMS (baseline)
3. Buka Detail user Fajar N, tab System Log, dan catat jumlah entri Client `Apotek Sehat Sentosa+{runId}-118` — FAMS (baseline)
4. Catat `Modified By` dan `Last Updated` record pengajuan `Apotek Sehat Sentosa+{runId}-118 — FAMS` (baseline)
5. Buka Allocation > Client Subscription tab Current, ketik Search `Apotek Sehat Sentosa+{runId}-118`, tekan Enter
6. Klik ikon `⋯` pada baris pengajuan `Apotek Sehat Sentosa+{runId}-118 — FAMS`, lalu pilih `Edit`
7. Klik `[Save]` tanpa mengubah nilai
8. Verifikasi toast netral "No changes to save."
9. Verifikasi modal Edit tetap terbuka
10. Verifikasi form tidak dirty
11. Verifikasi tidak ada request mutasi yang dikirim
12. Klik `[✕]` untuk menutup modal Edit
13. Buka modal Changelog dan cari entri baru Action berawalan `Edit` untuk Client `Apotek Sehat Sentosa+{runId}-118`
14. Verifikasi jumlah entri Changelog Client `Apotek Sehat Sentosa+{runId}-118` — FAMS sama dengan baseline
15. Buka Activity Log, saring Object `Client Subscription`, dan hitung entri Client yang sama
16. Verifikasi jumlah entri Activity Log sama dengan baseline
17. Buka Detail user Fajar N, tab System Log, dan hitung entri Client yang sama
18. Verifikasi jumlah entri System Log sama dengan baseline
19. Verifikasi jumlah entri baru dengan Action berawalan `Edit` adalah nol
20. Verifikasi `Modified By` dan `Last Updated` record tidak berubah dibanding baseline

### TC-AC-CS-464: Aksi pada satu record tidak menghasilkan entri pada record lain

21. Catat jumlah entri Changelog Client `Apotek Sehat Sentosa+{runId}-118` — SIEM (term lain Client yang sama), jumlah entri Client lain, dan total entri Changelog tanpa filter pada baseline
22. Pemicu (sesi API): batalkan pengajuan (Cancel Request) `Apotek Sehat Sentosa+{runId}-118 — FAMS` sebagai requester hingga perubahan tersimpan
23. Buka menu Allocation > Client Subscription, buka modal Changelog dan filter Client `Apotek Sehat Sentosa+{runId}-118`
24. Verifikasi entri Action `Cancel Request` untuk `Apotek Sehat Sentosa+{runId}-118 — FAMS` tampil
25. Verifikasi tidak ada entri log baru pada term lain Client yang sama (`Apotek Sehat Sentosa+{runId}-118` — SIEM)
26. Hapus filter Client pada modal Changelog
27. Verifikasi tabel Changelog tanpa filter menampilkan sedikitnya satu entri Client lain
28. Verifikasi tidak ada entri log baru pada Client lain: total entri Changelog tanpa filter bertambah tepat satu terhadap baseline (entri `Cancel Request` di atas)
29. Verifikasi field yang tidak berubah tidak menghasilkan entri

## Notes

- Mode: FE+BE. Sumber: `admin-console/license-allocation-subscription/TestCases/tc-license-allocation-subscription.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Aksi pemicu tiap blok adalah aksi pada kolom Dependensi TC (bukan Langkah Uji TC ini); spec memicunya lewat sesi API aktor yang sama dan menulis langkah pemicu "... hingga ... tersimpan" (R-20). Sesi API bukan konteks kedua dan tidak memakai `P-2`.
- Kelas g: TC-AC-CS-231 dan TC-AC-CS-458 dijalankan sebagai satu aksi nyata (Save tanpa perubahan) karena TC-AC-CS-458 adalah verifier berantai dari TC-AC-CS-231; Expected c TC-AC-CS-231 dan Expected a TC-AC-CS-458 diasersi pada satu rangkaian langkah.
- Anchor positif asersi absence: toast netral "No changes to save." (bagian 8b butir 2, hasil server yang sudah diasersi) untuk blok TC-AC-CS-231 dan TC-AC-CS-458, serta entri `Cancel Request` pada term target untuk blok TC-AC-CS-464.
- Langkah penghubung (S-03): langkah mencatat baseline jumlah entri dan nilai record sebelum aksi (S-12), langkah menutup modal Edit setelah `[Save]`, langkah menyaring Object `Client Subscription` di Activity Log, langkah Search pada daftar Client Subscription sebelum `⋯` > Edit, langkah membuka kembali menu Allocation > Client Subscription sesudah System Log, dan langkah Search/filter Client untuk menemukan entri target (R-16).
- Temuan untuk QA:
  - TC-AC-CS-231 Expected c ("tidak ada request mutasi") tidak menyebut cara mengamatinya; spec memakai pengamat request jaringan browser yang disediakan tim FE.
  - TC-AC-CS-458 Expected b (`Modified By` dan `Last Updated` record tidak berubah) tidak menyebut surface pembacaan; spec memakai kemampuan baca record yang disediakan tim FE/BE.
  - TC-AC-CS-464 Expected a ("tidak ada entri log baru pada term lain atau Client lain") tidak menyebut field atau surface yang diperiksa untuk "Client lain"; spec memakai total entri Changelog tanpa filter terhadap baseline dan perlu penegasan field atau surface dari QA.
  - TC-AC-CS-464 butir Langkah Uji ke-2 ("Periksa entri term lain milik Client yang sama dan Client lain") tidak menyebut term dan Client yang diperiksa; spec memakai term SIEM `#90` dan baseline Client lain. Aksi pemicu TC-AC-CS-464 (Cancel Request) berasal dari kolom Dependensi dan dipicu lewat sesi API (kemampuan disediakan tim BE/FE).
  - Precondition TC menyebut aktor Create-Only atau Group Manager membuka Activity Log dan Detail user tab System Log; hak akses role itu ke surface tersebut tidak dinyatakan di TC. Spec mengikuti Precondition TC.
