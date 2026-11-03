---
id: TC-FA-TAG-E2E-270-tabel-to-be-returned-pagination-download-dan-state-per-tab-bagian-3
title: "Tabel To Be Returned: Pilihan Download dan Download CSV Mengikuti Filter dan Kolom Tampil (Bagian 3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1022
  - TC-FA-TAG-1023
coverage:
  web: automated
---

# Tabel To Be Returned: Pilihan Download dan Download CSV Mengikuti Filter dan Kolom Tampil (Bagian 3)

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
- Kemampuan teknis (disediakan tim FE/BE): pembaca berkas unduhan CSV/XLSX (nama berkas, ekstensi, header kolom, jumlah baris, isi sel, nama sheet) dan pendeteksi toast pada saat klik pilihan format.
- Pemulihan di hook `after`: dataset To Be Returned dikembalikan ke keadaan Pre-setup empat Tag lewat fixture backend bila seeding mengubahnya. Kolom Reason dipulihkan pada akhir spec; Filter dikosongkan di akhir spec.
- Pemulihan preferensi kolom: kolom Reason disembunyikan lewat Column Visibility (tersimpan di browser) dan ditampilkan kembali pada langkah 22.

## Test Steps

### TC-FA-TAG-1022: ikon Download menampilkan pilihan CSV dan XLSX

1. Klik tab `To Be Returned`
2. Klik ikon Download
3. Verifikasi overlay menampilkan "Download as CSV" dan "Download as XLSX"
4. Tutup overlay Download (Esc)

### TC-FA-TAG-1023: Download CSV mengikuti Search, Filter, dan kolom tampil

5. Klik ikon Filter
6. Pilih opsi "RFID" pada field "TAG Type"
7. Klik [Apply]
8. Buka Column Visibility lewat ikon di header kolom aksi
9. Sembunyikan kolom "Reason"
10. Tutup Column Visibility
11. Klik ikon Download
12. Klik "Download as CSV"
13. Verifikasi tidak ada toast sukses
14. Verifikasi file bernama "To-Be-Returned-TAGs" berekstensi .csv terunduh
15. Verifikasi file berisi header kolom yang tampil (tanpa "Reason")
16. Verifikasi file berisi 3 baris Tag RFID (satu baris per Tag)
17. Verifikasi kolom Return Group ditulis dengan hierarki penuh "Operations > Disposal Center"
18. Verifikasi kolom Current Holder ditulis dengan nama lengkap
19. Verifikasi nilai kosong ditulis "-"
20. Verifikasi pemisah CSV koma
21. Verifikasi encoding CSV UTF-8 BOM
22. Tampilkan kembali kolom "Reason" lewat Column Visibility, lalu tutup Column Visibility
23. Klik [Clear Field]
24. Klik [Apply]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1022 s.d. 1023). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-1018 s.d. 1021 ada di spec 252 dan TC-FA-TAG-1024, 1025, 1027, 1028, dan 1029 ada di spec 253.
- Absence toast sukses diletakkan sesudah pemicu klik pilihan format dan sebelum `Verifikasi` berkas (bagian 8b butir 11); pemicu itu menjadi anchor positif bagi `Verifikasi` berkas terunduh.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 4 (menutup overlay Download); 10 (menutup Column Visibility); 22 (memulihkan kolom Reason); 23 (mengosongkan Filter lewat [Clear Field]); 24 (menerapkan Filter kosong lewat [Apply]).
- Asersi tambahan di luar Expected TC: tidak ada.
- Temuan untuk QA:
  - TC-FA-TAG-1023 Expected butir c dan d memuat isi sel (hierarki Return Group, nama lengkap, nilai "-") serta pemisah dan encoding berkas, yang menurut bagian 3 prinsip 13 butir f termasuk asersi buffer biner; spec mengikuti TC dan menuliskannya sebagai `Verifikasi` terpisah di spec ini.
  - TC-FA-TAG-1023 Expected butir c "Current Holder ditulis dengan nama lengkap" dan "nilai kosong ditulis -" tidak menyebut nama lengkap yang diharapkan maupun kolom yang bernilai kosong pada tiga baris RFID; spec mengasersi sesuai TC tanpa menambah nilai.
  - TC-FA-TAG-1023 butir b "header kolom yang tampil" tidak menyebut urutan header; spec mengasersi himpunan header tanpa Reason.
  - Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada kode, urutan, dan jumlah persis; Lampiran A belum memuat butir modul ini, sehingga seeding idempotent dan pemulihan lewat fixture backend (suite serial) dicatat sebagai kebutuhan.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
