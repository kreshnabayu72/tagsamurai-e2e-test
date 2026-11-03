---
id: TC-AC-ACTS-E2E-214-modal-event-log-buka-default-tab-add-stock-tutup-sesi-sku-ini-dan-popup-audit-tanpa-ikon
title: "Modal Event Log: Buka di Tab Add Stock, Screening, Tutup (X), Esc, dan Backdrop, Hanya Sesi SKU Ini, serta Popup Audit TAG Tanpa Ikon Event Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-472
  - TC-AC-ACTS-478
  - TC-AC-ACTS-479
  - TC-AC-ACTS-902
  - TC-AC-ACTS-903
  - TC-AC-ACTS-904
coverage:
  web: automated
---

# Modal Event Log: Buka di Tab Add Stock, Screening, Tutup (X), Esc, dan Backdrop, Hanya Sesi SKU Ini, serta Popup Audit TAG Tanpa Ikon Event Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `sessionOtherSku` = `Zebra RFD40 (SN-2202)` (Hardware yang hanya dipakai sesi seed SKU lain); `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed: SKU `Fixture.tagStock.skuRfid` memiliki sesi Add Stock dan Delete Stock (sedikitnya 5 sesi) di Event Log serta unit eligible Audit; SKU lain memiliki sesi dengan Hardware `Fixture.tagStock.sessionOtherSku` yang tidak dipakai sesi SKU `Fixture.tagStock.skuRfid`. Di-seed fixture BE di hook `before`.
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- State global: spec ini tidak mengubah state global suite (jam, Selection Limit, plan, status Suspended, toggle Local Registration).
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`

### TC-AC-ACTS-472: Buka modal Event Log dan screening

3. Klik icon `[Event Log]` di toolbar Tab Available
4. Verifikasi modal berjudul `Event Log` tampil dengan tombol close (X)
5. Verifikasi tab `Add Stock` aktif dan tab `Audit TAG` tersedia
6. Verifikasi toolbar Search, Filter, Download tampil
7. Verifikasi tabel memuat kolom `Date`, `Activity`, `Success`, `Waiting for Approval`, `Failed`, `Hardware`, `Modified By`, `Actions`

### TC-AC-ACTS-902: Modal Event Log terbuka di Tab Add Stock secara default

8. Tutup modal Event Log dengan klik (X)
9. Klik icon `[Event Log]` di toolbar Tab Available
10. Verifikasi modal terbuka dengan tab `Add Stock` aktif dan tab `Audit TAG` tersedia
11. Verifikasi tabel yang tampil adalah tabel Tab Add Stock (kolom `Activity` tampil)

### TC-AC-ACTS-903: Berpindah antar tab di modal Event Log

12. Klik tab `Audit TAG`
13. Verifikasi tabel Tab Audit TAG tampil dengan kolom `Date`, `Found`, `Not Found`, `Not Found Action`, `Hardware`, `Modified By`
14. Klik tab `Add Stock`
15. Verifikasi tabel Tab Add Stock tampil kembali dengan kolom `Date`, `Activity`, `Success`, `Waiting for Approval`, `Failed`, `Hardware`, `Modified By`
16. Verifikasi modal Event Log tidak tertutup selama berpindah tab

### TC-AC-ACTS-479: Menutup modal Event Log: (X) dan Esc menutup, klik backdrop diabaikan

17. Klik backdrop di luar modal Event Log
18. Verifikasi modal Event Log tidak tertutup oleh klik backdrop
19. Klik (X) pada modal Event Log
20. Verifikasi modal Event Log tertutup oleh (X)
21. Klik icon `[Event Log]` di toolbar Tab Available
22. Tekan Esc
23. Verifikasi modal Event Log tertutup oleh Esc
24. Klik icon `[Event Log]` di toolbar Tab Available
25. Verifikasi modal terbuka di Tab Add Stock
26. Verifikasi Search kosong dan Filter tidak aktif
27. Verifikasi Sort kembali ke urutan default Date Newest First
28. Verifikasi pagination kembali ke default 10 data per halaman

### TC-AC-ACTS-478: Event Log hanya memuat sesi SKU ini

29. Verifikasi sedikitnya satu baris sesi SKU `Fixture.tagStock.skuRfid` tampil pada tabel Tab Add Stock
30. Ketik Search `Fixture.tagStock.sessionOtherSku`, tekan Enter
31. Verifikasi empty state `No results found` tampil sehingga tidak ada sesi SKU lain pada modal Event Log SKU `Fixture.tagStock.skuRfid`
32. Klik `(←)` pada kotak Search

### TC-AC-ACTS-904: Popup Audit TAG tidak memiliki icon `[Event Log]` di header

33. Tutup modal Event Log dengan klik (X)
34. Klik `[Audit TAG]` di toolbar Tab Available
35. Verifikasi header Popup Audit TAG hanya berisi judul `Audit TAG` dan icon (X)
36. Verifikasi tidak ada icon `[Event Log]` di header Popup Audit TAG
37. Tutup Popup Audit TAG dengan klik (X)
38. Verifikasi icon `[Event Log]` tampil di toolbar Tab Available
39. Klik icon `[Event Log]` di toolbar Tab Available
40. Klik tab `Audit TAG`
41. Verifikasi tab `Audit TAG` aktif sebagai tempat membaca riwayat sesi Audit

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16) dan langkah 2 (row action `Detail`) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup modal, Popup, atau Overlay; menutup kotak Search lewat `(←)`.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Alasan di atas sekitar 35 langkah: spec ini 41 langkah dihitung dengan ekspansi; semua blok membuka modal Event Log SKU yang sama dengan dataset seed yang sama, dan tiap blok berdiri sendiri; jumlah langkah berasal dari `Verifikasi` per klausa Expected (S-01) dan langkah penutup atau pembuka modal antar TC (S-09).
- TC-AC-ACTS-478: bagian "untuk Distributor hanya sesi dari batch registrasi miliknya" diuji di spec 222 (TC-AC-ACTS-942).
- Temuan untuk QA (S-15):
  - TC-AC-ACTS-478 tidak menyebut cara membedakan sesi SKU A dan SKU B pada tabel (tabel tidak memiliki kolom SKU). Spec memakai Hardware seed khusus SKU lain dan Search; TC perlu menyebut data pembeda.
  - TC-AC-ACTS-479 Expected c (Search, Filter, Sort, Pagination kembali default) tidak didahului langkah yang mengubah state tersebut sebelum modal ditutup, sehingga asersi default tidak membedakan state. Spec mengikuti langkah TC.
  - TC-AC-ACTS-472 menyebut kolom `Actions` pada tabel, sedangkan TC-AC-ACTS-480 menyebut kolom Column Visibility (⋯) pada posisi yang sama; spec mengikuti rumusan masing-masing TC.
