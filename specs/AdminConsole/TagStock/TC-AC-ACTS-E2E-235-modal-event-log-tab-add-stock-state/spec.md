---
id: TC-AC-ACTS-E2E-235-modal-event-log-tab-add-stock-state
title: "Modal Event Log Tab Add Stock: State Kosong, Empty-Filtered, Error Load, dan Loading"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-510
  - TC-AC-ACTS-511
  - TC-AC-ACTS-512
  - TC-AC-ACTS-513
coverage:
  web: automated
---

# Modal Event Log Tab Add Stock: State Kosong, Empty-Filtered, Error Load, dan Loading

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuNewNoHistory` = SKU RFID baru tanpa riwayat Event Log (disediakan fixture BE); `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Event Log Tab Add Stock SKU `Fixture.tagStock.skuRfid`: sedikitnya 5 sesi Add Stock dan Delete Stock dengan sedikitnya dua nilai distinct pada tiap kolom (Activity `Add Stock` dan `Delete Stock`; Success, Waiting for Approval, dan Failed beragam; Hardware `Zebra RFD40 (SN-2201)` dan `—`; Modified By `Budi S` dan `Sari D` dari Data Uji Dinamis #3). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10), bukan dibaca dari satu halaman tabel.
- Data seed: SKU `Fixture.tagStock.skuNewNoHistory` tanpa riwayat Event Log (TC-AC-ACTS-510).
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Intercept respons 5xx dan penahanan respons (delay) di atas backend nyata lewat `Spectra.intercept()`; intercept dilepas segera setelah dipakai dan hook `after` memastikan tidak ada intercept tersisa.
- State global: tidak ada yang diubah selain intercept respons yang dilepas segera setelah dipakai.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available

### TC-AC-ACTS-511: Empty-filtered modal Event Log (Tab Add Stock): search atau filter tanpa hasil

4. Verifikasi sedikitnya satu baris sesi tampil pada tabel
5. Ketik Search `zzz-tidak-ada`, tekan Enter
6. Verifikasi empty state tampil dengan ilustrasi, judul `No results found`, dan deskripsi `Try adjusting your search or filter.`
7. Verifikasi tampilan bukan tampilan error
8. Klik `(←)` pada kotak Search

### TC-AC-ACTS-512: Error load modal Event Log (Tab Add Stock): fetch gagal bukan empty state

9. Gagalkan request daftar data dengan intercept respons 5xx pada endpoint daftar
10. Muat ulang tampilan modal Event Log (tutup lalu klik icon `[Event Log]` di toolbar Tab Available)
11. Verifikasi body modal menampilkan `Unable to load this data.` dan `[Try Again]`
12. Verifikasi header, tab bar, dan tombol close tetap tampil
13. Verifikasi tampilan bukan empty state
14. Lepas intercept respons 5xx
15. Klik `[Try Again]`
16. Verifikasi tombol `[Try Again]` memuat ulang data sehingga tabel sesi tampil

### TC-AC-ACTS-513: Loading state modal Event Log (Tab Add Stock)

17. Tahan respons daftar data (delay jaringan), lalu muat ulang modal Event Log (tutup lalu klik icon `[Event Log]`)
18. Verifikasi komponen loading tampil selama data diambil
19. Lepas tahanan respons daftar data
20. Verifikasi tabel menggantikan komponen loading

### TC-AC-ACTS-510: Empty state genuine modal Event Log (Tab Add Stock)

21. Tutup modal Event Log dengan klik (X)
22. Buka TAG > Stock lewat sidebar
23. Ketik Search `Fixture.tagStock.skuNewNoHistory`, tekan Enter
24. Klik row action `Detail` pada SKU `Fixture.tagStock.skuNewNoHistory`
25. Klik icon `[Event Log]` di toolbar Tab Available
26. Verifikasi empty state tampil dengan ilustrasi, judul `No event logs yet`, dan deskripsi `Add Stock and Delete Stock sessions for this SKU will appear here.`
27. Verifikasi tidak ada baris data pada tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), dan langkah 3 (membuka modal Event Log) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup modal, Popup, atau Overlay; menutup kotak Search lewat `(←)`.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Urutan blok: TC-AC-ACTS-510 (empty state genuine, pindah ke SKU lain) diletakkan terakhir karena menutup modal SKU yang dipakai blok lain (S-10).
- Temuan untuk QA (S-15):
