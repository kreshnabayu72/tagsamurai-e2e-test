---
id: TC-AC-ACTS-E2E-156-pencatatan-log-snapshot-audit-level-sesi-dan-activation-collision-waiting
title: "Pencatatan Log: Audit Multi-Unit Satu Entri per Unit, Snapshot Log Tidak Berubah, Activation Collision Waiting dengan Aktor Client, dan Log Audit Level Sesi"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-671
  - TC-AC-ACTS-672
  - TC-AC-ACTS-751
  - TC-AC-ACTS-777
coverage:
  web: automated
---

# Pencatatan Log: Audit Multi-Unit Satu Entri per Unit, Snapshot Log Tidak Berubah, Activation Collision Waiting dengan Aktor Client, dan Log Audit Level Sesi

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Sesi API aktor (login API password, token tidak dihitung sebagai sesi web) untuk pelaku kedua yang hanya memicu perubahan state, disediakan tim BE/FE (lihat `suite.md`).
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Data per blok TC (di-reset fixture BE lewat langkah Reset dataset): 3 unit Available yang tidak di-scan (TC-AC-ACTS-671; seeding hook `before` hanya 2 Available sehingga dataset ini di-reset sebelum blok); unit Available U1 dihapus lalu Device Name SKU diubah (TC-AC-ACTS-672); Subject Activation Collision pending dari Client (TC-AC-ACTS-751); 2 Available (A, B) dan 1 Damaged/Missing (C) (TC-AC-ACTS-777). Perubahan Device Name SKU Pre-setup `RFID-ASSET-CORE-R5` dilakukan lewat sesi API aktor yang disediakan tim FE/BE dan nama dipulihkan fixture BE di hook `after` (efek pada Last Updated dicatat; S-06).
- Pembacaan log memakai baseline jumlah entri sebelum aksi (S-12).

## Test Steps

### TC-AC-ACTS-671: Audit multi-unit menulis satu entri per unit

1. Reset dataset: 3 unit Available lewat fixture BE
2. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
3. Buka User Detail > System Log dan Activity Log, lalu catat baseline jumlah entri `Mark as Damaged/Missing`
4. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
5. Klik `[Audit TAG]`, klik `[Start Scan]`, tidak men-scan 3 unit Available, klik `[Stop]`, klik `[Submit]`, lalu klik `[Confirm]` dengan checkbox dicentang
6. Tunggu aksi selesai
7. Buka User Detail > System Log dan Activity Log
8. Verifikasi jumlah entri `Mark as Damaged/Missing` bertambah 3 dari baseline langkah 3
9. Verifikasi himpunan 3 baris `Mark as Damaged/Missing` teratas (urutan default `Date` terbaru; tanpa mengandalkan urutan di antaranya) memiliki pelaku dan timestamp Submit yang sama

### TC-AC-ACTS-777: Log Audit level sesi (Action `Audit`) di System Log dan Activity Log

10. Reset dataset: 2 Available (A, B) dan 1 Damaged/Missing (C) lewat fixture BE
11. Buka User Detail > System Log dan Activity Log, lalu catat baseline jumlah entri Activity Log `Audit`, `Mark as Damaged/Missing`, dan `Mark as Available` serta jumlah entri System Log `Audit`
12. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available, lalu klik `[Audit TAG]`, `[Start Scan]`, scan unit C, klik `[Stop]`, klik `[Submit]`
13. Pada dialog `Confirm Audit` biarkan checkbox dicentang, klik `[Confirm]`
14. Tunggu aksi selesai
15. Buka User Detail > System Log dan Activity Log
16. Verifikasi jumlah entri Activity Log `Audit` bertambah 1 dari baseline langkah 11, dengan entri teratas (urutan default `Date` terbaru) baru: satu entri Action `Audit`, Name `RFID-ASSET-CORE-R5 (RFID)`, Field `Quantity`, Old Value `—`, New Value `1`, Modified By `[First Name] [Last Initial]`
17. Verifikasi jumlah entri System Log `Audit` bertambah 1 dari baseline langkah 11, dengan entri teratas baru: Action `Audit`, Object `TAG Stock`, Name `RFID-ASSET-CORE-R5 (RFID)`, Field `Quantity`, Old `—`, New `1`, tanpa Modified By
18. Verifikasi kolom Activity Log sama dengan System Log ditambah Modified By
19. Verifikasi entri per unit tetap ada: jumlah `Mark as Damaged/Missing` bertambah 2 (A, B) dan jumlah `Mark as Available` bertambah 1 (C) dari baseline langkah 11

### TC-AC-ACTS-751: Entri Activity Log Waiting for Approval Activation Collision ditulis dengan aktor user Client

20. Buka User Detail > System Log dan Activity Log, lalu catat baseline jumlah entri System Log Admin Console pengguna dan jumlah entri Activity Log `Waiting for Approval` (filter Object `TAG Stock`)
21. Reset dataset: Subject Activation Collision pending dari Client lewat fixture BE (Client mengaktivasi TAG yang identifier-nya sudah In Use di Global Settings)
22. Buka Activity Log (filter Object `TAG Stock`)
23. Verifikasi jumlah entri Activity Log `Waiting for Approval` naik tepat 1 dari baseline langkah 20
24. Verifikasi entri Activity Log `Waiting for Approval` teratas (urutan default `Date` terbaru) untuk identifier itu tampil dengan Modified By nama user Client pemohon berformat `[First Name] [Last Initial]`
25. Buka User Detail > System Log
26. Verifikasi jumlah entri System Log Admin Console sama dengan baseline langkah 20 (tidak ada entri System Log dari aktivasi Client)

### TC-AC-ACTS-672: Snapshot log tidak berubah setelah record terkait berubah

27. Buka Activity Log (filter Object `TAG Stock`) dan catat baseline jumlah entri `Delete Stock`
28. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
29. Klik (⋯) pada unit Available U1, klik `Delete`, lalu klik `[Delete]`
30. Tunggu aksi selesai (dialog `Delete Unit` tertutup)
31. Buka Activity Log (filter Object `TAG Stock`)
32. Verifikasi jumlah entri `Delete Stock` naik tepat 1 dari baseline langkah 27
33. Catat nilai entri `Delete Stock` teratas (urutan default `Date` terbaru) untuk U1 (Name dan Old Value)
34. Sesi API mengubah Device Name SKU `RFID-ASSET-CORE-R5` hingga nama baru tersimpan
35. Buka Activity Log (filter Object `TAG Stock`)
36. Verifikasi entri `Delete Stock` U1 lama tetap menampilkan Name dan Old Value yang dicatat (nilai saat itu)
37. Pulihkan Device Name SKU ke nilai awal lewat fixture BE

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 2 (membuka Detail SKU), "Reset dataset", pencatatan baseline, "Tunggu aksi selesai", pencarian entri, dan navigasi ke User Detail dan Activity Log. Aksi menghapus data (TC-AC-ACTS-672) diletakkan terakhir; urutan TC: 671, 777, 751, 672. Langkah "Tunggu aksi selesai" ditambahkan sebelum pindah surface atau ganti akun sesudah aksi yang hasilnya tidak diasersi langsung (bagian 8b butir 8).
- P-1: bagian "tanpa System Log" TC-AC-ACTS-751 diasersi sebagai jumlah entri System Log sama dengan baseline di spec ini karena Subject Activation Collision dibangun fixture BE pada TC yang sama; tidak ada spec absence untuk bagian itu.
- Cara baca entri audit trail baru (S-12, S-14): jumlah entri dicatat sebelum aksi pemicu, selisihnya diverifikasi, lalu baris teratas urutan default `Date` terbaru dibaca; bila beberapa entri baru jatuh dalam menit yang sama, himpunan baris teratas sebanyak selisih diasersi tanpa mengandalkan urutan di antaranya. Pada TC-AC-ACTS-671 selisih tiga entri `Mark as Damaged/Missing` dibaca sebagai himpunan 3 baris teratas; pada TC-AC-ACTS-672 selisih satu entri `Delete Stock` U1.
- Temuan untuk QA:
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - TC-AC-ACTS-751 butir b ("Entri yang sama tampil di Activity Log; tidak ada entri System Log Admin Console") menyebut Activity Log dua kali; spec mengasersi entri di Activity Log dan jumlah System Log sama dengan baseline.
  - TC-AC-ACTS-672 menyebut "ubah nama Device Name SKU" tanpa jalur; spec memakai sesi API aktor (kemampuan disediakan tim FE/BE) karena perubahan Device SKU ada di modul lain.
  - TC-AC-ACTS-671 tidak menyebut cara menandai 3 unit; spec memakai Audit yang tidak men-scan 3 unit Available.
  - TC-AC-ACTS-777 butir b menulis kolom System Log "tanpa Modified By" dan butir c mengulang perbandingan kolom; spec mengasersi keduanya sebagai Verifikasi terpisah.
