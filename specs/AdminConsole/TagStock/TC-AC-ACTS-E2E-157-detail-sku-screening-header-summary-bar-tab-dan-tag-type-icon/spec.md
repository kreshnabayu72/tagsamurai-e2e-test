---
id: TC-AC-ACTS-E2E-157-detail-sku-screening-header-summary-bar-tab-dan-tag-type-icon
title: "Detail SKU: Screening Header, Summary Bar, Tab, Toolbar Tab Available SKU GPS dan BLE, dan Icon TAG Type di Header"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-374
  - TC-AC-ACTS-375
  - TC-AC-ACTS-856
coverage:
  web: automated
---

# Detail SKU: Screening Header, Summary Bar, Tab, Toolbar Tab Available SKU GPS dan BLE, dan Icon TAG Type di Header

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`).
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (#12), `BLE-BEACON-ALPHA-B1` (#14), dan `GPS-TRACK-CORE-G3` (#15). Subject Register Duplicate pending pada SKU RFID di Approvals untuk TC-AC-ACTS-856 (milik spec, di-seed fixture BE); reader RFID terhubung (simulator) sesuai Precondition TC-AC-ACTS-856.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.

## Test Steps

### TC-AC-ACTS-374: Screening halaman Detail SKU: header, Summary bar, Tab

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List
2. Amati halaman dari atas ke bawah
3. Verifikasi Breadcrumb `TAG > Stock > Detail`
4. Klik segmen `Stock` pada Breadcrumb
5. Verifikasi segmen `Stock` membuka Stock List
6. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List
7. Verifikasi header SKU memuat Photo, Device Name, SKU, icon TAG Type, Type, Brand, dan Model/Type
8. Verifikasi Summary bar berisi `Total Registered`, `Available`, dan `In Use` berurutan
9. Verifikasi Summary bar tanpa kartu `Allocated` atau `Damaged/Missing`
10. Verifikasi Tab `Available | In Use` dengan Available aktif
11. Verifikasi footer memuat pagination tabel tab aktif
12. Verifikasi tidak ada info banner kuota alokasi di tab
13. Verifikasi tidak ada tab `Allocation History`

### TC-AC-ACTS-375: Detail SKU GPS dan BLE, toolbar Tab Available tanpa `[Audit TAG]`

14. Buka Stock List, lalu klik row action `Detail` pada SKU BLE `BLE-BEACON-ALPHA-B1`
15. Verifikasi toolbar Tab Available SKU BLE berisi Search, Filter, Download, `[Event Log]`, `[Delete by Scan]`, `[Add Stock]` tanpa `[Audit TAG]`
16. Buka Stock List, lalu klik row action `Detail` pada SKU GPS `GPS-TRACK-CORE-G3`
17. Verifikasi toolbar Tab Available SKU GPS berisi Search, Filter, Download, `[Event Log]`, `[Add Stock]` tanpa `[Delete by Scan]` dan tanpa `[Audit TAG]`

### TC-AC-ACTS-856: TAG Type tampil sebagai icon di header Detail SKU, Add Stock, Audit TAG, dan Dialog Detail Approval

18. Buka Stock List, lalu klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5`
19. Verifikasi header Detail SKU menampilkan icon TAG Type (bukan badge teks)
20. Arahkan kursor ke icon TAG Type pada header Detail SKU
21. Verifikasi accessibility label `RFID`
22. Klik `[Add Stock]`
23. Verifikasi SKU info card Add Stock menampilkan icon TAG Type (bukan badge teks)
24. Arahkan kursor ke icon TAG Type pada SKU info card
25. Verifikasi accessibility label `RFID`
26. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available, lalu klik `[Audit TAG]`
27. Verifikasi header Audit TAG menampilkan icon TAG Type (bukan badge teks)
28. Arahkan kursor ke icon TAG Type pada header Audit TAG
29. Verifikasi accessibility label `RFID`
30. Klik `✕` pada popup untuk menutup popup Idle
31. Buka Approvals > TAG Stock > Tab Active, lalu klik `Review` pada Subject Register Duplicate
32. Verifikasi header Dialog Detail Approval menampilkan icon TAG Type (bukan badge teks)
33. Arahkan kursor ke icon TAG Type pada header dialog
34. Verifikasi accessibility label `RFID`
35. Verifikasi badge `Type` pada dialog tetap badge

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu topik (Detail SKU, satu SKU dan satu dataset); tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah pembukaan Detail SKU dan pemulihan state diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), klik segmen `Stock` dan kembali ke Detail SKU, navigasi antar SKU, Add Stock, popup Audit, dan Approvals, serta penutup popup Idle.
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun dikonfirmasi tim FE.
  - TC-AC-ACTS-374 butir a menulis "segmen `Stock` bisa diklik membuka Stock List" tanpa langkah klik; spec menambah klik segmen `Stock` dan kembali ke Detail SKU untuk mengasersinya.
  - Langkah Uji TC-AC-ACTS-856 nomor 4 menyebut hover "pada tiap halaman" tanpa menyebut elemen; spec meng-hover icon TAG Type di keempat halaman.
  - TC-AC-ACTS-375 dan 856 memakai SKU Pre-setup (#14, #15) dan Subject pending seeding yang tidak disebut di Pre-setup TC.
