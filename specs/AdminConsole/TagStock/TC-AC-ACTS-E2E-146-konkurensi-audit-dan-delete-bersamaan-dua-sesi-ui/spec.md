---
id: TC-AC-ACTS-E2E-146-konkurensi-audit-dan-delete-bersamaan-dua-sesi-ui
title: "Konkurensi Audit dan Delete: Dua Sesi Audit pada Unit yang Sama, Delete Dua Kali, dan Delete Bersamaan dengan Audit"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-710
  - TC-AC-ACTS-711
  - TC-AC-ACTS-714
coverage:
  web: automated
---

# Konkurensi Audit dan Delete: Dua Sesi Audit pada Unit yang Sama, Delete Dua Kali, dan Delete Bersamaan dengan Audit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Akun aktor kedua (Admin 2, Total Control lain): password `Spectra.env.AC_TC2_PASSWORD`; email akun ini tidak tertulis di Pre-setup TC (lihat Temuan untuk QA), disediakan tim FE.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Kemampuan teknis: Konteks browser kedua (Admin 2) yang hasilnya diasersi (sesi UI kedua, kelas c), dibuka dan login pada langkah pertama spec dan ditutup di akhir spec; pembacaan Last Updated SKU dan Activity Log memakai baseline sebelum aksi (S-12).
- Data per blok TC (di-reset fixture BE): TC-AC-ACTS-710 memakai unit A (Available) sebagai satu-satunya baris Not Scanned di kedua sesi dan semua baris lain Verified; TC-AC-ACTS-711 memakai unit Available A; TC-AC-ACTS-714 memakai tepat dua unit eligible A dan B (keduanya Available).

## Test Steps

### TC-AC-ACTS-710: Dua sesi Audit menandai unit yang sama, yang kedua di-skip

1. Buka konteks browser kedua dan login sebagai Admin 2 (`Spectra.env.AC_TC2_PASSWORD`)
2. Admin 1: Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
3. Admin 2: Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
4. Admin 1: klik `[Audit TAG]`, klik `[Start Scan]`, scan semua unit eligible kecuali unit A, klik `[Stop]`
5. Admin 2: klik `[Audit TAG]`, klik `[Start Scan]`, scan semua unit eligible kecuali unit A, klik `[Stop]`
6. Admin 1: catat baseline jumlah entri Activity Log `Mark as Damaged/Missing` untuk unit A (Search TAG Code)
7. Admin 1: klik `[Submit]`, biarkan checkbox dicentang, klik `[Confirm]`
8. Verifikasi di sesi Admin 1 unit A menjadi Damaged/Missing
9. Admin 1: Buka Activity Log (filter Object `TAG Stock`)
10. Verifikasi satu entri `Mark as Damaged/Missing` baru untuk unit A bertambah dari baseline langkah 6
11. Admin 1: buka Stock List dan catat Last Updated SKU `RFID-ASSET-CORE-R5`
12. Admin 2: klik `[Submit]`, biarkan checkbox dicentang, klik `[Confirm]`
13. Verifikasi di sesi Admin 2 unit A dilewati sebagai no-op
14. Verifikasi di sesi Admin 2 toast netral `No changes to save.`
15. Admin 1: Buka Activity Log (filter Object `TAG Stock`)
16. Verifikasi jumlah entri `Mark as Damaged/Missing` untuk unit A tetap bertambah satu dari baseline langkah 6 (tidak bertambah akibat Admin 2)
17. Admin 1: buka Stock List dan baca Last Updated SKU `RFID-ASSET-CORE-R5`
18. Verifikasi Last Updated SKU tidak berubah dari nilai yang dicatat

### TC-AC-ACTS-711: Delete dua kali pada unit yang sama (idempotent)

19. Reset dataset: unit Available A lewat fixture BE; Admin 1 dan Admin 2 membuka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
20. Catat baseline jumlah entri Activity Log `Delete Stock` untuk unit A (Search TAG Code)
21. Admin 1: klik (⋯) pada unit A, lalu klik `Delete`
22. Admin 2: klik (⋯) pada unit A, lalu klik `Delete`
23. Admin 1: klik `[Delete]`
24. Tunggu aksi selesai (toast sukses Admin 1 tampil)
25. Admin 2: klik `[Delete]`
26. Verifikasi di sesi Admin 2 toast netral `This unit is no longer available.`
27. Admin 1: Buka Activity Log (filter Object `TAG Stock`)
28. Verifikasi satu entri `Delete Stock` untuk unit A bertambah dari baseline

### TC-AC-ACTS-714: Delete bersamaan dengan Audit Mark pada unit yang sama

29. Reset dataset: tepat dua unit eligible A dan B (keduanya Available) lewat fixture BE; Admin 1 dan Admin 2 membuka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
30. Catat baseline jumlah entri Activity Log untuk unit A dan B (Search TAG Code)
31. Admin 2: klik `[Audit TAG]`, klik `[Start Scan]`, scan unit B, klik `[Stop]`, klik `[Submit]` sehingga dialog `Confirm Audit` terbuka (unit A Not Scanned, checkbox dicentang)
32. Admin 1: klik (⋯) pada unit A, lalu klik `Delete`, klik `[Delete]`
33. Tunggu aksi selesai (toast sukses Admin 1 tampil)
34. Admin 2: klik `[Confirm]`
35. Verifikasi di sesi Admin 2 unit A di-skip karena sudah tidak ada dan batch tidak digagalkan
36. Verifikasi di sesi Admin 2 unit B Verified berstatus Available (no-op) dengan toast netral `No changes to save.` tanpa klausa skip
37. Admin 1: Buka Activity Log (filter Object `TAG Stock`)
38. Verifikasi jumlah entri Activity Log untuk unit A hanya bertambah satu entri `Delete Stock` dan untuk unit B sama dengan baseline
39. Tutup konteks browser kedua (Admin 2 logout)

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (c) dan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah "Reset dataset" dan pembukaan Detail SKU diulang per blok.
- Langkah penghubung (S-03): langkah 1 dan langkah terakhir (membuka dan menutup konteks browser kedua), langkah 2 (membuka Detail SKU), "Reset dataset", pencatatan baseline, navigasi ke Activity Log dan Stock List, serta "Tunggu aksi selesai".
- Pembagian TC lintas spec: TC-AC-ACTS-712 dan 713 (pelaku kedua lewat sesi API) ada di spec 164.
- Temuan untuk QA:
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - Admin 2 (Total Control lain) tidak ada di Pre-setup TC; email dan password (`AC_TC2_PASSWORD`) disediakan tim FE (S-13).
  - TC-AC-ACTS-710 butir b ("tanpa entri Activity Log baru dan tanpa perubahan Last Updated") diasersi sebagai jumlah entri dan Last Updated sama dengan nilai sebelum Submit Admin 2 (S-12); TC mengamati hanya setelah kedua Submit.
  - TC-AC-ACTS-714 butir a ("tanpa log" untuk unit A) diasersi sebagai jumlah entri sama dengan baseline; TC tidak menyebut baseline.
