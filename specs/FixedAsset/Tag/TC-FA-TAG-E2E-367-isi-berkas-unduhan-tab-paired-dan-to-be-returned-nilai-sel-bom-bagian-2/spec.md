---
id: TC-FA-TAG-E2E-367-isi-berkas-unduhan-tab-paired-dan-to-be-returned-nilai-sel-bom-bagian-2
title: "Isi Berkas Unduhan: Asset Value Numerik, Transactional Policy, Category Berhierarki, dan Current Holder Nama Lengkap"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1434
  - TC-FA-TAG-1435
  - TC-FA-TAG-1436
  - TC-FA-TAG-1437
coverage:
  web: automated
---

# Isi Berkas Unduhan: Asset Value Numerik, Transactional Policy, Category Berhierarki, dan Current Holder Nama Lengkap

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): pembaca berkas unduhan XLSX dan CSV (tipe sel, isi sel, nama berkas); penanganan unduhan file di browser; seed idempotent aset, Tag, dan Asset Value; penghapusan preferensi kolom Setup Column di browser pada hook `after` (Setup Column disimpan pada langkah 3, 11, dan 19).
- Data Pre-setup tab Paired (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis): grup Excavator 20 Ton / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0. AST-0011 'Excavator 20 Ton - 11' (Group Plant B) punya Asset Value (Commercial) 125000000, Transactional Policy Borrow `On` dan Assign `On` (policy lain `Off`), dan Category Heavy Equipment > Excavator (Heavy Equipment adalah root).
- Data Pre-setup Tag To Be Returned: [RFID] RF-00071 (Last Asset Excavator 20 Ton - 2, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 (Excavator 20 Ton - 5, Disposal Center, Dedi K.); [NFC] NF-00092 (Laptop Pro 14 - 8, HQ Warehouse, Rina T.); Current Holder Dedi K. bernama lengkap Dedi Kurniawan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): hapus preferensi kolom Setup Column di browser dan kembalikan data seed ke keadaan awal. Spec ini hanya membaca data (aksi hanya membaca).
- State global: preferensi kolom Setup Column pada browser (dipulihkan seperti di atas). Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1434: Asset Value (Commercial) pada XLSX

1. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
2. Klik header `⋯` lalu `Setup Column...`
3. Centang kolom curated Asset Value (Commercial) lalu klik `[Save]`
4. Tutup Popup Detail
5. Klik ikon Download
6. Klik `Download as XLSX`
7. Verifikasi sel Asset Value (Commercial) baris AST-0011 berisi angka 125000000 sebagai sel angka (number), bukan teks terformat
8. Verifikasi sel tanpa simbol atau kode mata uang dan tanpa pemisah ribuan maupun format tampilan

### TC-FA-TAG-1435: Transactional Policy pada CSV

9. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
10. Klik header `⋯` lalu `Setup Column...`
11. Centang kolom curated Transactional Policy lalu klik `[Save]`
12. Tutup Popup Detail
13. Klik ikon Download
14. Klik `Download as CSV`
15. Verifikasi sel Transactional Policy baris AST-0011 memuat label aksesibilitas ikon, yaitu nama transaksi `Borrow` dan `Assign` dalam urutan tetap ikon
16. Verifikasi sel tidak memuat nama komponen atau kelas ikon

### TC-FA-TAG-1436: Category pada CSV

17. Klik Asset Name `Excavator 20 Ton` pada baris Plant B untuk membuka Popup Detail
18. Klik header `⋯` lalu `Setup Column...`
19. Centang kolom curated Category lalu klik `[Save]`
20. Tutup Popup Detail
21. Klik ikon Download
22. Klik `Download as CSV`
23. Verifikasi sel Category baris AST-0011 memuat hierarki penuh dari root `Heavy Equipment > Excavator`, bukan nama Category tunggal

### TC-FA-TAG-1437: Current Holder pada CSV To Be Returned

24. Buka Fixed Asset > TAG > To Be Returned
25. Klik ikon Download
26. Klik `Download as CSV`
27. Verifikasi nama file `To-Be-Returned-TAGs`
28. Verifikasi sel Current Holder baris RF-00071 berisi nama lengkap `Dedi Kurniawan`, bukan format tampilan `Dedi K.`

## Notes

- Spec isi berkas (kelas f, binary buffer). Nama berkas adalah asersi fungsional; tipe sel dan isi sel dibaca lewat pembaca berkas.
- Langkah penghubung (tanpa awalan `Verifikasi`): 1 sampai 4, 9 sampai 12, 17 sampai 20 (menampilkan kolom lewat Setup Column), 24 (navigasi).
- Setup Column disimpan sisi klien tanpa request tulis ke server, sehingga tidak ada langkah "Tunggu aksi selesai" sesudah `[Save]`.
- Temuan untuk QA:
  - Hook suite pada `suite.md` yang menghapus preferensi kolom Setup Column tidak mencantumkan spec ini; spec memulihkannya sendiri di hook `after`.
  - TC-FA-TAG-1434 dan TC-FA-TAG-1437 tidak menyebut Post Condition selain "aksi hanya membaca"; tidak diasersi.
  - Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) tidak bisa bersuffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
