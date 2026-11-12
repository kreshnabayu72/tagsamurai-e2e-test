---
id: TC-FA-TAG-E2E-387-isi-berkas-unduhan-tab-paired-asset-value-pending-kosong-dan-no-access-teks
title: "Isi Berkas Unduhan XLSX: Sel Asset Value Pending Kosong dan No access Teks"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1503
coverage:
  web: automated
---

# Isi Berkas Unduhan XLSX: Sel Asset Value Pending Kosong dan No access Teks

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Manage asset & TAG (Read) (Read: Plant B; View asset value hanya pada sebagian aset) [MR] `manageAssetTagRead_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TAG_MR_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): pembaca berkas unduhan XLSX (tipe sel dan isi sel); penanganan unduhan file di browser; seed idempotent aset, Tag, dan Asset Value; penghapusan preferensi kolom Setup Column di browser pada hook `after` (Setup Column disimpan pada langkah 3).

- Data TC-FA-TAG-1503: Aset AST-0020 (Plant B, berhak) belum ada Purchase Cost sehingga Asset Value (Commercial) dan Asset Value (Fiscal) berstatus Pending; sebagian aset Plant B lain di luar hak View asset value sehingga kedua kolom berstatus No access.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom Setup Column di browser dan kembalikan data seed ke keadaan awal. Spec ini hanya membaca data (aksi hanya membaca).
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-1503: Download XLSX menulis sel Asset Value Pending sebagai kosong dan sel No access sebagai teks No access

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
2. Klik header `⋯` lalu `Setup Column...`
3. Centang kolom curated Asset Value (Commercial) dan Asset Value (Fiscal) lalu klik `[Save]`
4. Tutup Popup Detail
5. Klik ikon Download
6. Klik `Download as XLSX`
7. Verifikasi sel Asset Value (Commercial) dan Asset Value (Fiscal) pada baris AST-0020 (`Pending`) kosong (bukan `-`, bukan teks `Pending`)
8. Verifikasi sel kedua kolom pada baris di luar hak berisi teks `No access`
9. Verifikasi sel bernilai ditulis angka asli sebagai sel angka (number)

## Notes

- Spec isi berkas (kelas f, binary buffer). Tipe sel dan isi sel dibaca lewat pembaca berkas.
- Langkah penghubung (tanpa awalan `Verifikasi`): 1 sampai 4 (menampilkan kolom lewat Setup Column).
- Setup Column disimpan sisi klien tanpa request tulis ke server, sehingga tidak ada langkah "Tunggu aksi selesai" sesudah `[Save]`.
- Temuan untuk QA:
  - Role "Read: Plant B; View asset value hanya pada sebagian aset" tidak punya baris Pre-setup sendiri; spec memakai akun Manage asset & TAG (Read) [MR] dan menandai pembagian View asset value per aset serta AST-0020 tanpa Purchase Cost sebagai kebutuhan fixture BE.
  - Hook suite pada `suite.md` yang menghapus preferensi kolom Setup Column tidak mencantumkan spec ini; spec memulihkannya sendiri di hook `after`.
  - TC tidak menyebut nama berkas unduhan; tidak diasersi. Post Condition TC ("aksi hanya membaca") tidak diasersi.
