---
id: TC-AC-ACTS-E2E-155-pencatatan-log-field-delete-stock-sync-condition-kolom-modified-by-dan-tanpa-duplikat
title: "Pencatatan Log: Entri Delete Stock Satuan, Sync Condition, Kolom Modified By Activity Log, Tanpa Entri Ganda atau Nyasar, Isolasi Log Distributor, dan Scope Activity Log Tanpa Event Global Settings"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-522
  - TC-AC-ACTS-525
  - TC-AC-ACTS-526
  - TC-AC-ACTS-666
  - TC-AC-ACTS-667
  - TC-AC-ACTS-668
coverage:
  web: automated
---

# Pencatatan Log: Entri Delete Stock Satuan, Sync Condition, Kolom Modified By Activity Log, Tanpa Entri Ganda atau Nyasar, Isolasi Log Distributor, dan Scope Activity Log Tanpa Event Global Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Akun aktor kedua (Ganti akun): Distributor Toggle ON (Pre-setup #9) `distributorOn_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DIST_ON_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Data tambahan: aktivitas Principal dan Distributor lain pada SKU yang sama (TC-AC-ACTS-525); Activate TAG dan Delete TAG sudah terjadi di Global Settings (TC-AC-ACTS-526) dan event Condition Damaged/Missing untuk unit In Use (TC-AC-ACTS-666), disediakan lewat fixture BE oleh tim FE/BE (pemicu tidak disebut di TC, PRD, atau LLD). Pembacaan log memakai baseline jumlah entri sebelum aksi (S-12).
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.

## Test Steps

### TC-AC-ACTS-522: Entri Delete Stock satuan memiliki Field `TAG Code`, Old Value tag code, New Value `—`

1. Reset dataset: U1 sampai U4 lewat fixture BE (Data Dinamis #5; U1 = Available `TAG-4F7K2XQ9`)
2. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
3. Catat baseline jumlah entri Activity Log `Delete Stock` (filter Object `TAG Stock`; kemampuan baca)
4. Klik (⋯) pada unit Available U1, klik `Delete`, lalu klik `[Delete]`
5. Tunggu aksi selesai
6. Buka Activity Log (filter Object `TAG Stock`)
7. Verifikasi jumlah entri Activity Log `Delete Stock` bertambah 1 dari baseline
8. Verifikasi baris teratas (urutan default `Date` terbaru): Name = kode unit U1, Field `TAG Code`, Old Value = kode unit, New Value `—`

### TC-AC-ACTS-667: Activity Log memiliki kolom Modified By tambahan dibanding System Log

9. Buka User Detail > System Log dan Activity Log
10. Bandingkan entri `Delete Stock` unit U1 di System Log dan Activity Log
11. Verifikasi System Log memuat kolom Date, Action, Object, Name, Field, Old Value, New Value
12. Verifikasi Activity Log memuat kolom yang sama ditambah Modified By

### TC-AC-ACTS-668: Tidak ada entri log ganda, hilang, atau nyasar untuk satu aksi

13. Reset dataset: unit A dan B (Available) serta C dan D (Damaged/Missing) lewat fixture BE
14. Catat baseline jumlah entri Activity Log `TAG Stock` per unit A, B, C, D dan entri `Audit` SKU
15. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available, lalu klik `[Audit TAG]`, `[Start Scan]`, scan unit C saja, klik `[Stop]`, klik `[Submit]`, lalu klik `[Confirm]` dengan checkbox `D-03` dicentang (A dan B ditandai Damaged/Missing, C dipulihkan, D tidak berubah)
16. Tunggu aksi selesai
17. Buka Activity Log (filter Object `TAG Stock`)
18. Verifikasi tepat satu entri per unit yang berubah (`Mark as Damaged/Missing` atau `Mark as Available`) bertambah dari baseline langkah 14
19. Verifikasi tepat satu entri level-sesi `Audit` bertambah dari baseline
20. Verifikasi unit D (tidak berubah) dan record lain tidak mendapat entri baru (jumlah sama dengan baseline)

### TC-AC-ACTS-666: Log Sync Condition dari event Global Settings

21. Catat baseline jumlah entri Activity Log `Sync Condition` dan jumlah entri System Log pengguna (User Detail)
22. Terima event Condition Damaged/Missing untuk unit In Use (pemicu event dari Global Settings)
23. Buka User Detail > System Log dan Activity Log
24. Verifikasi jumlah entri Activity Log `Sync Condition` bertambah 1 dari baseline langkah 21, dengan entri baru: Action `Sync Condition`, Field `Condition`, Old/New sesuai perubahan, Modified By `System`
25. Verifikasi jumlah entri System Log pengguna sama dengan baseline (tidak ada entri `Sync Condition`)

### TC-AC-ACTS-526: Activity Log TAG Stock tidak memuat Activate TAG dan Delete TAG dari Global Settings

26. Buka Activity Log (filter Object `TAG Stock`)
27. Verifikasi Activity Log memuat entri `TAG Stock` lain (misalnya `Sync Condition`) tampil
28. Cari entri aktivasi dan penghapusan tag dari Global Settings (Search `Activate TAG` dan `Delete TAG`)
29. Verifikasi tidak ada entri `Activate TAG` atau `Delete TAG` di Activity Log TAG Stock

### TC-AC-ACTS-525: Distributor hanya melihat entri log unit dan sesi batch miliknya

30. Ganti akun: Logout, lalu login sebagai Distributor Toggle ON (`Spectra.env.AC_DIST_ON_PASSWORD`)
31. Buka Activity Log (filter Object `TAG Stock`)
32. Verifikasi Activity Log memuat sedikitnya satu entri unit batch registrasi Distributor itu (termasuk keputusan approval Principal atas unit tersebut)
33. Verifikasi Activity Log tidak memuat entri unit Principal dan Distributor lain (Search TAG Code unit Principal menghasilkan `No results found`)
34. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available, lalu klik `[Event Log]`
35. Verifikasi modal Event Log memuat sedikitnya satu baris sesi Distributor itu
36. Verifikasi modal Event Log hanya memuat sesi Distributor itu

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu topik (pembacaan log setelah aksi) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Blok baca-log berpola (buka surface, cari entri, Verifikasi kolom) berulang.
- Cara baca entri audit trail baru (S-12, S-14): jumlah entri dicatat sebelum aksi pemicu, selisihnya diverifikasi, lalu baris teratas urutan default `Date` terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya. Pada TC-AC-ACTS-522 selisih satu entri (`Delete Stock` unit U1).
- Langkah penghubung (S-03): langkah 2 (membuka Detail SKU), pencatatan baseline, "Tunggu aksi selesai", Search TAG Code, dan navigasi ke Activity Log, User Detail, dan modal Event Log. Urutan TC: 522, 667, 668, 666, 526, 525; TC-AC-ACTS-525 terakhir karena Ganti akun. Dataset U1 sampai U4 di-reset fixture BE sebelum TC-AC-ACTS-522; dataset 2 Available dan 2 Damaged/Missing (A sampai D) di-reset fixture BE sebelum TC-AC-ACTS-668.
- P-1: asersi "tanpa System Log" TC-AC-ACTS-666 diasersi sebagai jumlah entri System Log sama dengan baseline di spec ini karena bergantung pada event Condition yang baru diterima pada TC yang sama; tidak ada spec absence untuk TC itu.
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun perlu dikonfirmasi tim FE.
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - TC-AC-ACTS-526 Expected "tidak ada entri Activate TAG atau Delete TAG" tidak menyebut kata kunci pencarian; spec memakai Search `Activate TAG` dan `Delete TAG` dengan anchor entri TAG Stock lain.
  - TC-AC-ACTS-525 "Event Log hanya memuat sesi Distributor itu" tidak menyebut baris pembanding; spec memakai satu baris sesi Distributor sebagai anchor lewat seeding.
  - TC-AC-ACTS-667 dan 522 memakai entri log yang sama (Delete Stock) dengan 665; kecocokan format entri dibaca dari TC.
  - TC-AC-ACTS-668 "tidak ada entri untuk unit yang tidak berubah atau milik record lain" diasersi sebagai jumlah entri sama dengan baseline (S-12).
