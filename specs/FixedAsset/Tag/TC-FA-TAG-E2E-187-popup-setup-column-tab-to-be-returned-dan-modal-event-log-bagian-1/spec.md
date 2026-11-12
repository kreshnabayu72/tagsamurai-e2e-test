---
id: TC-FA-TAG-E2E-187-popup-setup-column-tab-to-be-returned-dan-modal-event-log-bagian-1
title: "Popup Setup Column Tab To Be Returned dan Modal Event Log: Screening, Reorder, dan Pin (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1422
  - TC-FA-TAG-1423
  - TC-FA-TAG-1424
  - TC-FA-TAG-1425
coverage:
  web: automated
---

# Popup Setup Column Tab To Be Returned dan Modal Event Log: Screening, Reorder, dan Pin (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned, Return Group, dan entri Event Log. Pengubahan ukuran viewport browser (mempersempit lalu memulihkan). Tidak ada endpoint yang dikarang di spec ini.
- Pemulihan konfigurasi kolom: hook `after` spec ini menghapus preferensi kolom Setup Column di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE). Nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; seeding idempotent (dilewati bila sudah ada):

| Data | Nilai | Kunci |
|---|---|---|
| Tag To Be Returned | [RFID] RF-00071 (Last Asset Excavator 20 Ton - 2, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K., Since 01 Sep 2026); [RFID] RF-00088 (Excavator 20 Ton - 5, Disposal Center, Dedi K., Since 20 Sep 2026); [NFC] NF-00092 (Laptop Pro 14 - 8, HQ Warehouse, Rina T., Since 22 Sep 2026); [RFID] RF-00110 (Excavator 20 Ton - 10, Disposal Center, Dedi K., Since 10 Sep 2026). Return Group Disposal Center berada di bawah group induk Operations | `tagToBeReturned` |
| Event Log | 27 Okt 2026 14:15 [RFID] RF-00093, Excavator 20 Ton - 5, Disposal Center, Dedi K., Budi S., Assigned, Paired; 26 Okt 2026 10:02 [RFID] RF-00071, Last Asset Excavator 20 Ton - 2, Return Group Disposal Center, Handed Over By Dedi K., Received By Budi S., Method Scan, Final Status Available; 26 Okt 2026 09:40 [NFC] NF-00092, Laptop Pro 14 - 8, HQ Warehouse, Rina T., Sari W., Manual, Damaged/Missing | `eventLogToBeReturned` |

- State yang diubah dan pemulihannya: konfigurasi kolom tabel To Be Returned di cache browser; penghapusan preferensi kolom Setup Column di browser oleh hook `after` spec ini. Viewport dipulihkan oleh langkah penghubung.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 13, 19).

## Test Steps

### TC-FA-TAG-1422

1. Buka Fixed Asset > TAG > To Be Returned
2. Klik header kolom terakhir `⋯` pada tabel
3. Klik `Setup Column...`
4. Verifikasi Popup Setup Column memuat header: judul `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan ikon close
5. Verifikasi enam kolom tercentang (TAG Code, Last Asset, Reason, Return Group, Current Holder, Since)
6. Verifikasi tiap kolom punya drag handle dan kontrol pin
7. Verifikasi tidak ada kolom curated
8. Verifikasi footer memuat `[Reset to Default]` dan `[Save]`, tanpa `[Cancel]`

### TC-FA-TAG-1423

9. Klik ikon close pada Popup Setup Column
10. Klik header kolom terakhir `⋯` pada tabel
11. Klik `Setup Column...`
12. Seret kolom Since ke posisi sebelum Reason
13. Klik `[Save]`
14. Verifikasi urutan kolom tabel menjadi TAG Code, Last Asset, Since, Reason, Return Group, Current Holder

### TC-FA-TAG-1424

15. Persempit viewport sehingga tabel perlu scroll horizontal
16. Klik header kolom terakhir `⋯` pada tabel
17. Klik `Setup Column...`
18. Pin kolom TAG Code
19. Klik `[Save]`
20. Scroll tabel secara horizontal
21. Verifikasi kolom TAG Code tetap di posisinya saat scroll
22. Pulihkan ukuran viewport

### TC-FA-TAG-1425

23. Klik tombol "Event Log"
24. Klik header kolom terakhir `⋯` pada tabel Event Log
25. Klik `Setup Column...`
26. Verifikasi Popup Setup Column Modal Event Log memuat header: judul `Setup Column`, deskripsi `Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns.`, dan ikon close
27. Verifikasi delapan kolom tercentang (Received At, TAG Code, Last Asset, Return Group, Handed Over By, Received By, Method, Final Status)
28. Verifikasi tiap kolom punya drag handle dan kontrol pin
29. Verifikasi tidak ada kolom curated
30. Verifikasi footer memuat `[Reset to Default]` dan `[Save]`, tanpa `[Cancel]`

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1422, TC-FA-TAG-1423, TC-FA-TAG-1424, TC-FA-TAG-1425). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Popup Setup Column tab To Be Returned dan Modal Event Log ada di spec 187 (TC-FA-TAG-1422 s.d. 1425) dan spec 188 (TC-FA-TAG-1426 s.d. 1428).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): langkah 9, 15, 22 (menutup popup Setup Column dan mempersempit atau memulihkan viewport).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 13, 19).
- Temuan untuk QA:
  - Tab To Be Returned dibuka sekali (TC-FA-TAG-1422) dan tetap aktif sampai TC-FA-TAG-1425; langkah "Buka Fixed Asset > TAG > To Be Returned" tidak diulang di TC berikutnya, dan popup Setup Column ditutup dengan ikon close atau `[Save]`.
  - Akun aktor pada TC-FA-TAG-1425 tidak menyebut halaman awal (tidak ada baris "User berada di"); spec membuka tab To Be Returned lewat TC-FA-TAG-1422.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
