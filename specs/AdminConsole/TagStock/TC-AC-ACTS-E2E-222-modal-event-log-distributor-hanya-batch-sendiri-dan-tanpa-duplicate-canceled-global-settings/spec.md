---
id: TC-AC-ACTS-E2E-222-modal-event-log-distributor-hanya-batch-sendiri-dan-tanpa-duplicate-canceled-global-settings
title: "Modal Event Log: Distributor Hanya Melihat Sesi Batch Miliknya pada Kedua Tab dan Tanpa Duplicate Canceled dari Event Delete TAG Global Settings"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-942
  - TC-AC-ACTS-943
coverage:
  web: automated
---

# Modal Event Log: Distributor Hanya Melihat Sesi Batch Miliknya pada Kedua Tab dan Tanpa Duplicate Canceled dari Event Delete TAG Global Settings

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Distributor Toggle ON (Pre-setup #9) `distributorOn_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_DIST_ON_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Akun aktor kedua: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`, dipakai pada Ganti akun di blok TC-AC-ACTS-943.
- Env var `AC_DIST_ON_PASSWORD` adalah nama baru; harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Data seed: SKU `Fixture.tagStock.skuRfid` memiliki sesi Add Stock, Delete Stock, dan Audit milik Distributor A (akun aktor pertama), milik Principal, dan milik Distributor B; sesi Distributor A dari batch registrasi miliknya. Subject Activation Collision pending untuk SKU itu, yang tagnya akan dihapus Client di Global Settings. Di-seed fixture BE di hook `before`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Pembacaan lewat fixture BE atas jumlah total entri sesi Event Log SKU per tab sebagai baseline (selain teks footer pagination); TC tidak menyebut cara membaca baseline (lihat Temuan untuk QA).
- Kemampuan teknis: Pelaku kedua (Client di Global Settings) lewat sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Pembacaan Activity Log lewat UI (Search atau Filter entri); jalur menu Activity Log tidak disebut TC (lihat Temuan untuk QA).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps


### TC-AC-ACTS-942: Distributor hanya melihat sesi Event Log dari batch registrasi miliknya (kedua tab)

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available
4. Verifikasi sedikitnya satu baris sesi Distributor A tampil pada Tab Add Stock
5. Verifikasi Tab Add Stock hanya memuat sesi Distributor A
6. Klik tab `Audit TAG`
7. Verifikasi sedikitnya satu baris sesi Distributor A tampil pada Tab Audit TAG
8. Verifikasi Tab Audit TAG hanya memuat sesi Distributor A
9. Klik (⋯) pada satu baris sesi, klik `Detail`
10. Verifikasi Popup Detail hanya memuat unit dari batch registrasi Distributor A
11. Verifikasi sesi Principal dan Distributor B tidak dikembalikan server (response daftar dan rincian tidak memuat sesi itu)
12. Tutup Popup Detail dan modal Event Log

### TC-AC-ACTS-943: Event Log tidak memuat Duplicate Canceled dari event Delete TAG Global Settings

13. Ganti akun: Logout, lalu login sebagai Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_TC_PASSWORD`
14. Catat jumlah total entri sesi Tab Add Stock SKU `Fixture.tagStock.skuRfid` sebagai baseline (kemampuan baca fixture BE)
15. Catat jumlah total entri sesi Tab Audit TAG SKU `Fixture.tagStock.skuRfid` sebagai baseline (kemampuan baca fixture BE)
16. Client menghapus tag Waiting for Approval milik Subject Activation Collision di Global Settings lewat sesi API hingga penghapusan tersimpan
17. Tunggu 5 detik tanpa memuat ulang halaman
18. Buka Approvals > TAG Stock lewat sidebar
19. Klik Tab `History`
20. Verifikasi Subject Activation Collision tercatat Canceled di Approvals > TAG Stock > Tab History
21. Buka Activity Log dan cari entri `Duplicate Canceled` untuk Subject itu
22. Verifikasi entri `Duplicate Canceled` ada di Activity Log
23. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
24. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
25. Klik icon `[Event Log]` di toolbar Tab Available
26. Verifikasi jumlah total entri Tab Add Stock sama dengan baseline sehingga tidak ada baris baru
27. Klik tab `Audit TAG`
28. Verifikasi jumlah total entri Tab Audit TAG sama dengan baseline sehingga tidak ada baris baru

## Notes

- Langkah penghubung (S-03): Search SKU di Stock List yang mendahului row action `Detail` mencari baris target (R-16); tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup modal, Popup, atau Overlay; mencatat baseline.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Blok TC-AC-ACTS-942 memakai akun Distributor A; blok TC-AC-ACTS-943 memakai Total Control sehingga akun diganti secara eksplisit (S-07).
- Temuan untuk QA (S-15):
  - Email akun Total Control di Pre-setup TC adalah `totalControl_automated_{namaCompany}`, sedangkan `.env.example` mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`; kesamaan akun dikonfirmasi tim FE. Pre-setup #1 menyebut "822 TC" yang tidak cocok dengan jumlah TC aktif.
  - TC-AC-ACTS-943 tidak menyebut cara membaca Activity Log dan jalur menunya; spec memakai pencarian entri sebagai langkah penghubung.
  - TC-AC-ACTS-943 menyebut "Tunggu event diproses" tanpa durasi; spec memakai jendela 5 detik tanpa memuat ulang halaman (pilihan spec, bukan nilai TC atau PRD).
  - Pre-setup #9 mencatat "71 TC" penggunaan, tidak cocok dengan jumlah TC aktif (lihat Temuan akun).
