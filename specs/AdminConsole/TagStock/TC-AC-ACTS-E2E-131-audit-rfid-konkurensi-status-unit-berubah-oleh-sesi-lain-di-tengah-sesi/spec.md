---
id: TC-AC-ACTS-E2E-131-audit-rfid-konkurensi-status-unit-berubah-oleh-sesi-lain-di-tengah-sesi
title: "Audit RFID Konkurensi: Unit Berubah Status oleh Sesi Lain Di-Skip (T-08 Tunggal dan Jamak) dan Nol Perubahan dengan Unit Di-Skip"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-327
  - TC-AC-ACTS-762
  - TC-AC-ACTS-767
coverage:
  web: automated
---

# Audit RFID Konkurensi: Unit Berubah Status oleh Sesi Lain Di-Skip (T-08 Tunggal dan Jamak) dan Nol Perubahan dengan Unit Di-Skip

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
- Pelaku kedua: sesi lain yang mengaktivasi unit (status In Use) memakai sesi API aktor dengan kemampuan aktivasi unit yang disediakan tim FE/BE (aktor tidak disebut di TC; S-13).
- Data per blok TC (di-reset fixture BE): TC-AC-ACTS-327 memakai 2 Available (A, B) dan 2 Damaged/Missing; TC-AC-ACTS-762 memakai 3 Available (A, B, C) dan 1 Damaged/Missing; TC-AC-ACTS-767 memakai 2 Available (A, B).
- Pembacaan Activity Log dan baris Event Log Tab Audit TAG dipakai untuk TC-AC-ACTS-767; asersi jumlah memakai baseline sebelum aksi (S-12).

## Test Steps

### TC-AC-ACTS-327: Unit berubah status oleh sesi lain di-skip dengan klausa T-08

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Klik `[Audit TAG]` di toolbar Tab Available
3. Klik `[Start Scan]`
4. Scan unit A
5. Klik `[Stop]`
6. Sesi API mengaktivasi unit A hingga status In Use tersimpan
7. Klik `[Submit]`
8. Biarkan checkbox dicentang pada dialog `Confirm Audit`, klik `[Confirm]`
9. Verifikasi unit A di-skip: status tetap In Use dan batch tidak digagalkan
10. Verifikasi unit B menjadi Damaged/Missing
11. Verifikasi dua unit yang sudah Damaged/Missing tidak berubah (no-op)
12. Verifikasi satu toast gabungan `Success, TAG has been marked as Damaged/Missing. 1 TAG was skipped because its status had changed.`

### TC-AC-ACTS-762: Dua unit berubah status oleh sesi lain di-skip dengan klausa T-08 bentuk jamak

13. Reset dataset: 3 Available dan 1 Damaged/Missing lewat fixture BE
14. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
15. Klik `[Audit TAG]` di toolbar Tab Available
16. Klik `[Start Scan]`
17. Scan unit A dan unit B
18. Klik `[Stop]`
19. Sesi API mengaktivasi unit A dan unit B hingga status In Use tersimpan
20. Klik `[Submit]`
21. Biarkan checkbox dicentang pada dialog `Confirm Audit`, klik `[Confirm]`
22. Verifikasi unit A dan unit B di-skip: status tetap In Use dan batch tidak digagalkan
23. Verifikasi unit C menjadi Damaged/Missing dan unit yang sudah Damaged/Missing tidak berubah (no-op)
24. Verifikasi satu toast gabungan `Success, TAG has been marked as Damaged/Missing. 2 TAGs were skipped because their status had changed.`

### TC-AC-ACTS-767: Nol perubahan status dengan unit di-skip memakai toast T-20 saja

25. Reset dataset: 2 Available (A, B) lewat fixture BE
26. Buka Activity Log dan catat baseline jumlah entri `TAG Stock`; buka modal `[Event Log]` Tab Audit TAG dan catat baseline jumlah baris, lalu tutup modal Event Log
27. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
28. Klik `[Audit TAG]` di toolbar Tab Available
29. Klik `[Start Scan]`
30. Scan unit A dan unit B
31. Klik `[Stop]`
32. Sesi API mengaktivasi unit A hingga status In Use tersimpan
33. Klik `[Submit]`
34. Verifikasi tanpa dialog Konfirmasi (semua baris Verified)
35. Verifikasi toast netral `No changes to save.` tanpa klausa unit di-skip
36. Buka Activity Log dan modal `[Event Log]` Tab Audit TAG
37. Verifikasi jumlah entri Activity Log dan jumlah baris Event Log Tab Audit TAG sama dengan baseline langkah sebelumnya

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), "Reset dataset", pencatatan baseline dan navigasi ke Activity Log dan Event Log, serta `[Stop]` yang membuka kunci popup (pemulihan state, S-09). Langkah "Tutup modal Event Log" menutup modal sebelum pindah surface atau ganti akun (pemulihan state, S-09).
- Temuan untuk QA:
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - Aktor dan mekanisme "sesi lain mengaktivasi unit" (Global Settings > Activate TAG) tidak didefinisikan di TC, PRD, atau LLD; spec memakai sesi API aktor dengan kemampuan yang disediakan tim FE/BE.
  - TC-AC-ACTS-767 butir c ("tidak ada entri Activity Log baru dan tidak ada baris baru di Event Log") diasersi sebagai jumlah sama dengan baseline (S-12); TC tidak memberi baseline.
  - TC-AC-ACTS-327 butir a dan TC-AC-ACTS-762 butir a ("tanpa log" untuk unit yang di-skip) tidak punya langkah observasi di TC; tidak diasersi terpisah, hanya status unit yang di-skip yang diasersi.
