---
id: TC-AC-ACTS-E2E-243-modal-event-log-tab-audit-tag-state
title: "Modal Event Log Tab Audit TAG: State Kosong, Empty-Filtered, Error Load, dan Loading"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-920
  - TC-AC-ACTS-921
  - TC-AC-ACTS-922
  - TC-AC-ACTS-923
coverage:
  web: automated
---

# Modal Event Log Tab Audit TAG: State Kosong, Empty-Filtered, Error Load, dan Loading

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Env var `AC_TC_PASSWORD` dipakai juga oleh suite Admin Console lain dan sudah terdaftar; password tidak ditulis di spec atau fixture.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Fixture `Fixture.tagStock` (berkas `fixtures/tag-stock.json` belum ada; dibuat di tahap script) memuat identitas data berikut: `skuNewNoHistory` = SKU RFID baru tanpa riwayat Event Log (disediakan fixture BE); `skuRfid` = `RFID-ASSET-CORE-R5` (SKU RFID, Pre-setup #12).
- Data seed Event Log Tab Audit TAG SKU `Fixture.tagStock.skuRfid`: sedikitnya 5 sesi Audit dengan sedikitnya dua nilai distinct pada tiap kolom (Found dan Not Found beragam; Not Found Action `Marked as Damaged/Missing` dan `Kept previous status`; Hardware `Zebra RFD40 (SN-2201)` dan `—`; Modified By `Sari D` dan pengguna lain). Di-seed fixture BE di hook `before` dan dipulihkan di hook `after`; total entri berasal dari seeding (8b butir 10).
- Data seed: SKU `Fixture.tagStock.skuNewNoHistory` tanpa sesi Audit (TC-AC-ACTS-920).
- Kemampuan teknis: Fixture BE (seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`).
- Kemampuan teknis: Intercept respons 5xx dan penahanan respons (delay) di atas backend nyata lewat `Spectra.intercept()`; intercept dilepas segera setelah dipakai dan hook `after` memastikan tidak ada intercept tersisa.
- State global: tidak ada yang diubah selain intercept respons yang dilepas segera setelah dipakai.
- Suite berjalan serial (`parallel: false`).

## Test Steps

1. Ketik Search `Fixture.tagStock.skuRfid`, tekan Enter
2. Klik row action `Detail` pada SKU `Fixture.tagStock.skuRfid`
3. Klik icon `[Event Log]` di toolbar Tab Available
4. Klik tab `Audit TAG`

### TC-AC-ACTS-921: Empty-filtered modal Event Log (Tab Audit TAG): search atau filter tanpa hasil

5. Verifikasi sedikitnya satu baris sesi tampil pada tabel
6. Ketik Search `zzz-tidak-ada`, tekan Enter
7. Verifikasi empty state tampil dengan ilustrasi, judul `No results found`, dan deskripsi `Try adjusting your search or filter.`
8. Verifikasi tampilan bukan tampilan error
9. Klik `(←)` pada kotak Search

### TC-AC-ACTS-922: Error load modal Event Log (Tab Audit TAG): fetch gagal bukan empty state

10. Gagalkan request daftar data dengan intercept respons 5xx pada endpoint daftar
11. Muat ulang tampilan Tab Audit TAG (tutup modal, klik icon `[Event Log]`, klik tab `Audit TAG`)
12. Verifikasi body modal menampilkan `Unable to load this data.` dan `[Try Again]`
13. Verifikasi header, tab bar, dan tombol close tetap tampil
14. Verifikasi tampilan bukan empty state
15. Lepas intercept respons 5xx
16. Klik `[Try Again]`
17. Verifikasi tombol `[Try Again]` memuat ulang data sehingga tabel sesi tampil

### TC-AC-ACTS-923: Loading state modal Event Log (Tab Audit TAG)

18. Tahan respons daftar data (delay jaringan), lalu muat ulang Tab Audit TAG (tutup modal, klik icon `[Event Log]`, klik tab `Audit TAG`)
19. Verifikasi komponen loading tampil selama data diambil
20. Lepas tahanan respons daftar data
21. Verifikasi tabel menggantikan komponen loading

### TC-AC-ACTS-920: Empty state genuine modal Event Log (Tab Audit TAG)

22. Tutup modal Event Log dengan klik (X)
23. Buka TAG > Stock lewat sidebar
24. Ketik Search `Fixture.tagStock.skuNewNoHistory`, tekan Enter
25. Klik row action `Detail` pada SKU `Fixture.tagStock.skuNewNoHistory`
26. Klik icon `[Event Log]` di toolbar Tab Available, klik tab `Audit TAG`
27. Verifikasi empty state tampil dengan ilustrasi, judul `No audit sessions yet`, dan deskripsi `Audit TAG sessions for this SKU will appear here.`
28. Verifikasi tidak ada baris data pada tabel

## Notes

- Langkah penghubung (S-03): langkah 1 (Search SKU di Stock List untuk menemukan baris target, R-16), langkah 2 (row action `Detail`), langkah 3 (membuka modal Event Log), dan langkah 4 (memilih Tab `Audit TAG`) menyiapkan halaman kerja; tidak ada `Verifikasi` karena hanya menyiapkan state.
- Langkah penghubung lain tanpa `Verifikasi` (S-03, S-09): menutup modal, Popup, atau Overlay; menutup kotak Search lewat `(←)`.
- Beberapa TC berurutan memakai satu pembukaan halaman atau modal dengan state yang dibersihkan di antaranya (halaman yang sama dipakai berulang, bagian 3 prinsip 13).
- Urutan blok: TC-AC-ACTS-920 (empty state genuine, pindah ke SKU lain) diletakkan terakhir (S-10).
- Temuan untuk QA (S-15):
