---
id: TC-FA-TAG-E2E-189-popup-setup-column-modal-changelog-reorder-dan-pin-bagian-1
title: "Popup Setup Column Modal Changelog: Column Visibility, Save, Reset, dan Reorder (Bagian 1)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-971
  - TC-FA-TAG-972
  - TC-FA-TAG-973
  - TC-FA-TAG-974
  - TC-FA-TAG-1429
coverage:
  web: automated
---

# Popup Setup Column Modal Changelog: Column Visibility, Save, Reset, dan Reorder (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun: Total Control, `totalControl_automated_{namaCompany}@qwertysystem.net`, password lewat `Spectra.env.FA_TC_PASSWORD` (nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed entri Changelog Paired TAG lewat fixture backend. Tidak ada endpoint yang dikarang di spec ini.
- Pemulihan konfigurasi kolom: hook `after` spec ini menghapus preferensi kolom Setup Column di browser (kemampuan disediakan tim FE), bukan lewat `[Reset to Default]`.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE). Nilai literal Pre-setup dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah persis; seeding idempotent (dilewati bila sudah ada):

| Data | Nilai | Kunci |
|---|---|---|
| Changelog Paired TAG | E1 26/10/26 10:02 Replace / Excavator 20 Ton - 50 / TAG / [NFC] NF-00090 / [RFID] RF-00420 / Sari W.; E2 26/10/26 10:02 Replace / Excavator 20 Ton - 50 / TAG / [QR] QR-00240 / — / Sari W.; E3 26/10/26 09:20 Replace / Excavator 20 Ton - 20 / TAG / [RFID] RF-00130 / [RFID] RF-00415 / Budi S.; E4 26/10/26 09:14 Replace / Excavator 20 Ton - 42 / TAG / [QR] QR-00230 / [RFID] RF-00412 / Budi S.; E5 25/10/26 16:40 Replace / Forklift Manual - 61 / TAG / [QR] QR-00251 / — / Dedi K.; E6 25/10/26 08:00 Report TAG / Excavator 20 Ton - 20 / Report Type / — / Damaged / Rina T. | `entriChangelog` |

- State yang diubah dan pemulihannya: konfigurasi kolom tabel Changelog di cache browser, terpisah dari tabel utama (Field disembunyikan lalu ditampilkan kembali, Modified By dan Action diubah, urutan kolom diubah); penghapusan preferensi kolom Setup Column di browser oleh hook `after` spec ini.

## Test Steps

### TC-FA-TAG-971

1. Klik tombol `Changelog` pada Table Tools
2. Klik header kolom `⋯` pada tabel modal
3. Verifikasi tooltip header `Column Visibility` tampil
4. Verifikasi overlay memuat tujuh kolom tercentang (Date, Action, Name, Field, Old Value, New Value, Modified By) dan `Setup Column...`

### TC-FA-TAG-972

5. Hilangkan centang kolom Field
6. Verifikasi kolom Field langsung tidak tampil tanpa Save
7. Centang kembali kolom Field

### TC-FA-TAG-973

8. Tekan Esc untuk menutup overlay Column Visibility
9. Klik header kolom `⋯` pada tabel modal
10. Klik `Setup Column...`
11. Verifikasi Popup Setup Column memuat judul `Setup Column`
12. Verifikasi Popup Setup Column memuat tujuh kolom tanpa kolom curated
13. Verifikasi footer Popup Setup Column memuat `[Reset to Default]` dan `[Save]`
14. Hilangkan centang kolom Modified By
15. Klik `[Save]`
16. Verifikasi kolom Modified By tersembunyi pada tabel modal
17. Klik header kolom `⋯` pada tabel modal
18. Klik `Setup Column...`
19. Klik `[Reset to Default]`
20. Verifikasi kolom default kembali tampil (pratinjau)
21. Klik `[Save]`
22. Verifikasi kolom default tersimpan permanen setelah Save

### TC-FA-TAG-974

23. Klik header kolom `⋯` pada tabel modal
24. Klik `Setup Column...`
25. Hilangkan centang kolom Action
26. Klik ikon close pada Popup Setup Column
27. Verifikasi kolom Action tetap tampil pada tabel modal
28. Tutup Modal Changelog
29. Verifikasi konfigurasi kolom Modal Changelog tidak memengaruhi kolom tabel grup (ketujuh kolom tabel grup tetap tampil)

### TC-FA-TAG-1429

30. Klik tombol `Changelog` pada Table Tools
31. Klik header kolom terakhir `⋯` pada tabel Changelog
32. Klik `Setup Column...`
33. Seret kolom Modified By ke posisi pertama
34. Klik `[Save]`
35. Verifikasi kolom Modified By menjadi kolom paling kiri tabel Changelog

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-971, TC-FA-TAG-972, TC-FA-TAG-973, TC-FA-TAG-974, TC-FA-TAG-1429). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: topik Popup Setup Column Modal Changelog ada di spec 189 (TC-FA-TAG-971 s.d. 974 dan 1429) dan spec 190 (TC-FA-TAG-1430).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan langkah TC): langkah 7, 8, 28 (menampilkan kembali kolom Field, menutup overlay dengan Esc, dan menutup Modal Changelog).
- Temuan untuk QA:
  - Langkah "Klik header kolom `⋯` pada tabel modal" pada TC-FA-TAG-973 dan TC-FA-TAG-974 mengikuti TC; overlay Column Visibility sebelumnya ditutup dengan Esc (langkah penghubung).
  - Precondition TC-FA-TAG-973 butir c tidak menyebut kolom mana yang di-Reset; spec mereset konfigurasi sesudah Modified By disimpan tersembunyi.
  - Nama dan kode literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
