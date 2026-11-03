---
id: TC-AC-ACTS-E2E-154-pencatatan-log-damaged-missing-duplicate-approved-rejected-canceled-dan-delete-stock
title: "Pencatatan Log: Mark as Damaged/Missing dan Available, Duplicate Approved (Register Duplicate, Activation Collision, Bypass E2a), Rejected, Canceled oleh Sistem, dan Delete Stock"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-658
  - TC-AC-ACTS-659
  - TC-AC-ACTS-660
  - TC-AC-ACTS-661
  - TC-AC-ACTS-662
  - TC-AC-ACTS-663
  - TC-AC-ACTS-664
  - TC-AC-ACTS-665
coverage:
  web: automated
---

# Pencatatan Log: Mark as Damaged/Missing dan Available, Duplicate Approved (Register Duplicate, Activation Collision, Bypass E2a), Rejected, Canceled oleh Sistem, dan Delete Stock

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Data per blok TC (di-reset fixture BE): 2 Available dan 2 Damaged/Missing (TC-AC-ACTS-658, 659); Subject Register Duplicate pending (TC-AC-ACTS-660, 663); Subject Activation Collision pending (TC-AC-ACTS-661); identifier yang cocok existing (TC-AC-ACTS-662); unit Waiting for Approval beserta Subject Activation Collision yang tag-nya dihapus Client di Global Settings (TC-AC-ACTS-664); unit Available U1 (TC-AC-ACTS-665). Entri log dibaca dengan baseline jumlah entri sebelum aksi (S-12).
- Kemampuan teknis: Pemicu event Delete TAG dari Global Settings (TC-AC-ACTS-664; Client menghapus tag Waiting di registri) disediakan tim FE/BE; aktor dan mekanismenya tidak disebut di TC, PRD, atau LLD.

## Test Steps

### TC-AC-ACTS-658: Log Mark as Damaged/Missing di System Log dan Activity Log

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Buka User Detail > System Log dan Activity Log, lalu catat baseline jumlah entri `Mark as Damaged/Missing`
3. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
4. Klik `[Audit TAG]`, klik `[Start Scan]`, scan unit Available A saja (U-lain), klik `[Stop]`, klik `[Submit]`, lalu klik `[Confirm]` dengan checkbox `D-03` dicentang (unit Available B, U-hilang, ditandai Damaged/Missing)
5. Tunggu aksi selesai
6. Buka User Detail > System Log dan Activity Log
7. Verifikasi jumlah entri Activity Log dan System Log `Mark as Damaged/Missing` bertambah 1 dari baseline langkah 2, dengan entri baru: Action `Mark as Damaged/Missing`, Field `Status`, Old Value `Available`, New Value `Damaged/Missing`
8. Verifikasi Name entri System Log adalah TAG Code unit B (U-hilang)

### TC-AC-ACTS-659: Log Mark as Available (recovery) di System Log dan Activity Log

9. Reset dataset: 2 Available dan 2 Damaged/Missing lewat fixture BE
10. Buka User Detail > System Log dan Activity Log, lalu catat baseline jumlah entri `Mark as Available`
11. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available, lalu klik `[Audit TAG]`, `[Start Scan]`, scan semua unit, klik `[Stop]`, klik `[Submit]` (recovery unit Damaged/Missing)
12. Tunggu aksi selesai
13. Buka User Detail > System Log dan Activity Log
14. Verifikasi jumlah entri Activity Log dan System Log `Mark as Available` bertambah 2 dari baseline langkah 10 (satu per unit Damaged/Missing yang dipulihkan), dengan entri baru: Action `Mark as Available`, Field `Status`, Old Value `Damaged/Missing`, New Value `Available`

### TC-AC-ACTS-660: Log Duplicate Approved Register Duplicate di System Log dan Activity Log

15. Buka User Detail > System Log dan Activity Log, lalu catat baseline jumlah entri `Duplicate Approved`
16. Buka Approvals > TAG Stock > Tab Active, klik `Review` pada Subject Register Duplicate, lalu Approve
17. Tunggu aksi selesai
18. Buka User Detail > System Log dan Activity Log
19. Verifikasi jumlah entri Activity Log dan System Log `Duplicate Approved` bertambah 1 dari baseline langkah 15, dengan entri baru: Action `Duplicate Approved`, Field `Status`, Old Value `Waiting for Approval`, New Value `Available`, dengan TAG Code baru

### TC-AC-ACTS-661: Log Duplicate Approved Activation Collision di System Log dan Activity Log

20. Buka User Detail > System Log dan Activity Log, lalu catat baseline jumlah entri `Duplicate Approved`
21. Buka Approvals > TAG Stock > Tab Active, klik `Review` pada Subject Activation Collision, lalu Approve
22. Tunggu aksi selesai
23. Buka User Detail > System Log dan Activity Log
24. Verifikasi jumlah entri Activity Log dan System Log `Duplicate Approved` bertambah 1 dari baseline langkah 20, dengan entri baru: Action `Duplicate Approved`, Old Value `Waiting for Approval`, New Value `In Use`

### TC-AC-ACTS-662: Log Duplicate Approved hasil bypass E2a

25. Buka User Detail > System Log dan Activity Log, lalu catat baseline jumlah entri `Duplicate Approved`; buka modal Event Log SKU (Tab Add Stock), catat baseline jumlah baris, lalu tutup modal Event Log
26. Buka halaman Add Stock SKU `RFID-ASSET-CORE-R5` sebagai Total Control, scan identifier yang cocok existing, klik `[Stop]`, lalu klik `[Submit]`
27. Tunggu aksi selesai
28. Buka User Detail > System Log dan Activity Log
29. Verifikasi jumlah entri Activity Log dan System Log `Duplicate Approved` bertambah 1 dari baseline langkah 25, dengan entri baru: Action `Duplicate Approved`, Field `Status`, Old Value `—`, New Value `Available`, Modified By requester
30. Buka modal Event Log SKU (Tab Add Stock)
31. Verifikasi Event Log memuat baris lain sebagai pembanding tampil
32. Verifikasi Event Log tidak memuat baris unit bypass (jumlah baris sama dengan baseline langkah 25)
33. Verifikasi kolom Old Value dan New Value tidak memuat teks bypass
34. Tutup modal Event Log

### TC-AC-ACTS-663: Log Duplicate Rejected di System Log dan Activity Log

35. Buka User Detail > System Log dan Activity Log, lalu catat baseline jumlah entri `Duplicate Rejected`
36. Buka Approvals > TAG Stock > Tab Active, klik `Review` pada Subject Register Duplicate, lalu Reject dengan alasan
37. Tunggu aksi selesai
38. Buka User Detail > System Log dan Activity Log
39. Verifikasi jumlah entri Activity Log dan System Log `Duplicate Rejected` bertambah 1 dari baseline langkah 35, dengan entri baru: Action `Duplicate Rejected`, Name `[identifier]` yang ditolak, Old Value `Waiting for Approval`, New Value `Rejected`

### TC-AC-ACTS-664: Log Duplicate Canceled oleh sistem hanya di Activity Log

40. Catat baseline jumlah entri Activity Log `Duplicate Canceled` dan jumlah entri System Log pengguna (User Detail)
41. Hapus tag Waiting di Global Settings (pemicu event Delete TAG), tunggu event diproses
42. Buka User Detail > System Log dan Activity Log
43. Verifikasi jumlah entri Activity Log `Duplicate Canceled` bertambah 1 dari baseline langkah 40, dengan entri baru: Action `Duplicate Canceled`, Modified By `System`
44. Verifikasi jumlah entri System Log pengguna sama dengan baseline (tidak ada entri `Duplicate Canceled`)

### TC-AC-ACTS-665: Log Delete Stock di System Log dan Activity Log

45. Buka User Detail > System Log dan Activity Log, lalu catat baseline jumlah entri `Delete Stock`
46. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available, klik (⋯) pada unit Available U1, klik `Delete`, lalu klik `[Delete]`
47. Tunggu aksi selesai
48. Buka User Detail > System Log dan Activity Log
49. Verifikasi jumlah entri Activity Log dan System Log `Delete Stock` bertambah 1 dari baseline langkah 45, dengan entri baru: Action `Delete Stock`, Field `TAG Code`, Old Value tag code U1, New Value `—`

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu topik (pembacaan log setelah aksi) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Blok baca-log berpola (buka surface, cari entri, Verifikasi kolom) berulang.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), "Reset dataset", pencatatan baseline, dan "Tunggu aksi selesai"; aksi menghapus data (TC-AC-ACTS-665) diletakkan terakhir. Langkah "Tutup modal Event Log" menutup modal sebelum pindah surface atau ganti akun (pemulihan state, S-09).
- P-1: bagian "tidak ada entri di System Log" TC-AC-ACTS-664 diasersi sebagai jumlah entri System Log sama dengan baseline di spec ini karena bergantung pada Subject Activation Collision yang baru dibangun fixture BE pada TC yang sama; bagian "Event Log tidak memuat baris unit bypass" TC-AC-ACTS-662 memakai anchor baris Event Log lain.
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun perlu dikonfirmasi tim FE.
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - TC-AC-ACTS-658 sampai 665 memuat Precondition "Aksi dijalankan pada SKU RFID-ASSET-CORE-R5" tanpa menyebut data; spec memakai dataset seeding yang menjalankan aksi masing-masing.
  - TC-AC-ACTS-660, 661, 663 tidak menyebut jalur Approve atau Reject; spec memakai dialog Review di Approvals > TAG Stock > Tab Active.
  - TC-AC-ACTS-664 tidak menyebut aktor dan mekanisme penghapusan tag Waiting di Global Settings; spec memakai pemicu yang disediakan tim FE/BE.
  - TC-AC-ACTS-662 menyebut "Event Log tidak memuat baris unit bypass" tanpa baseline; spec membandingkan terhadap baris Event Log sebelum aksi.
