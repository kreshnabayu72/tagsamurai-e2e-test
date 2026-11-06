---
id: TC-FA-TAG-E2E-269-tabel-to-be-returned-sort-dan-column-visibility-bagian-4
title: "Tabel To Be Returned: Kolom Visible Terakhir dan Setup Column Tersimpan Setelah Save (Bagian 4)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-1014
  - TC-FA-TAG-1015
coverage:
  web: automated
---

# Tabel To Be Returned: Kolom Visible Terakhir dan Setup Column Tersimpan Setelah Save (Bagian 4)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env usulan; didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite; tab `To Be Returned` dibuka pada langkah 1. Spec tidak mengganti akun; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci `Fixture.fixedAssetTag.<kunci>` pada tabel data ditandai untuk dibuat tim FE (tahap script).
- Data Pre-setup tab To Be Returned (kunci `Fixture.fixedAssetTag.tbr4`; tanpa suffix `{runId}` karena asersi bergantung pada kode, urutan, dan jumlah; tabel To Be Returned dalam scope akun berisi tepat empat Tag ini; Return Group 'Disposal Center' berada di bawah group induk 'Operations'):

| TAG Code | Last Asset | Reason | Return Group | Current Holder | Since |
|---|---|---|---|---|---|
| RF-00071 (RFID) | Excavator 20 Ton - 2 | Disposal | Disposal Center | Dedi K. | 01 Sep 2026 |
| RF-00088 (RFID) | Excavator 20 Ton - 5 | Disposal | Disposal Center | Dedi K. | 20 Sep 2026 |
| NF-00092 (NFC) | Laptop Pro 14 - 8 | Disposal | HQ Warehouse | Rina T. | 22 Sep 2026 |
| RF-00110 (RFID) | Excavator 20 Ton - 10 | Disposal | Disposal Center | Dedi K. | 10 Sep 2026 |

- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned (kode, Last Asset, Reason, Return Group, Current Holder, Since) dan Return Group; tidak ada endpoint yang dikarang di spec ini.
- Pemulihan preferensi kolom: hook `after` spec ini menghapus preferensi kolom di browser (kemampuan disediakan tim FE; bukan lewat `[Reset to Default]`), sesuai daftar di `suite.md`. Spec ini menyimpan konfigurasi kolom pada TC-FA-TAG-1015 (langkah 12).
- Pemulihan di hook `after`: dataset To Be Returned dikembalikan ke keadaan Pre-setup empat Tag lewat fixture backend bila seeding mengubahnya.
- Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 12).

## Test Steps

### TC-FA-TAG-1014: kolom visible terakhir tidak dapat disembunyikan

1. Klik tab `To Be Returned`
2. Buka Column Visibility lewat ikon di header kolom aksi
3. Sembunyikan semua kolom kecuali "TAG Code"
4. Arahkan kursor ke centang kolom "TAG Code"
5. Verifikasi centang kolom "TAG Code" Disabled (tetap tampil) dengan tooltip "At least one column must remain visible."
6. Tampilkan kembali kolom "Last Asset", "Reason", "Return Group", "Current Holder", dan "Since" lewat Column Visibility
7. Tutup Column Visibility

### TC-FA-TAG-1015: Setup Column, perubahan tersimpan setelah Save

8. Buka modal "Setup Column"
9. Verifikasi modal berjudul "Setup Column" dengan deskripsi "Drag and drop to reorder columns, check/uncheck to show/hide, or pin columns."
10. Hilangkan centang kolom "Current Holder" (preview langsung berubah)
11. Verifikasi tabel di balik modal langsung menyembunyikan kolom "Current Holder" sebagai preview
12. Klik [Save]
13. Verifikasi modal menutup
14. Verifikasi kolom "Current Holder" tetap tersembunyi
15. Tampilkan kembali kolom "Current Holder" lewat Column Visibility, lalu tutup Column Visibility

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1014 s.d. 1015). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-1005 s.d. 1009 ada di spec 249, TC-FA-TAG-1010 s.d. 1013 ada di spec 250, dan TC-FA-TAG-1016 dan 1017 ada di spec 251.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 6 (memulihkan kolom yang disembunyikan); 7 (menutup Column Visibility); 15 (memulihkan kolom Current Holder).
- Asersi tambahan di luar Expected TC: tidak ada.
- A-15: nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` karena asersi bergantung pada kode, urutan, dan jumlah persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom lewat `[Save]` Setup Column (langkah 12).
- Temuan untuk QA:
  - TC-FA-TAG-1015 Expected butir c ("kolom tetap tersembunyi") tidak menyebut cara menguji persistensi selain menutup modal; spec mengasersi keadaan sesudah Save tanpa muat ulang.
  - TC-FA-TAG-1014 tidak menyebut cara mengembalikan kolom; spec menambah langkah penghubung.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
