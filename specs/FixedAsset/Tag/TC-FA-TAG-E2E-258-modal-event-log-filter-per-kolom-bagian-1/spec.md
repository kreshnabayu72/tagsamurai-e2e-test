---
id: TC-FA-TAG-E2E-258-modal-event-log-filter-per-kolom-bagian-1
title: "Modal Event Log To Be Returned: Screening Filter Panel dan Filter Method, Final Status, Return Group, serta Handed Over By (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1046
  - TC-FA-TAG-1047
  - TC-FA-TAG-1048
  - TC-FA-TAG-1049
  - TC-FA-TAG-1050
coverage:
  web: automated
---

# Modal Event Log To Be Returned: Screening Filter Panel dan Filter Method, Final Status, Return Group, serta Handed Over By (Bagian 1)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env usulan; didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite; tab `To Be Returned` dibuka pada langkah 1. Spec tidak mengganti akun; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci `Fixture.fixedAssetTag.<kunci>` pada tabel data ditandai untuk dibuat tim FE (tahap script).
- Data Pre-setup Event Log To Be Returned (kunci `Fixture.fixedAssetTag.eventLog3`; tanpa suffix `{runId}`; Event Log berisi tepat tiga entri ini; 'Disposal Center' berada di bawah group induk 'Operations'; 'Dedi K.' bernama lengkap Dedi Kurniawan):

| Received At | TAG Code | Last Asset | Return Group | Handed Over By | Received By | Method | Final Status |
|---|---|---|---|---|---|---|---|
| 27 Okt 2026 14:15 | RF-00093 (RFID) | Excavator 20 Ton - 5 | Disposal Center | Dedi K. | Budi S. | Assigned | Paired |
| 26 Okt 2026 10:02 | RF-00071 (RFID) | Excavator 20 Ton - 2 | Disposal Center | Dedi K. | Budi S. | Scan | Available |
| 26 Okt 2026 09:40 | NF-00092 (NFC) | Laptop Pro 14 - 8 | HQ Warehouse | Rina T. | Sari W. | Manual | Damaged/Missing |

- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk entri Event Log To Be Returned; tidak ada endpoint yang dikarang di spec ini.
- Pemulihan di hook `after`: entri Event Log To Be Returned dikembalikan ke keadaan Pre-setup tiga entri lewat fixture backend bila seeding mengubahnya. Filter dikosongkan di akhir tiap kasus.
- Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Isolasi audit trail (butir A-18 iii): asersi yang bergantung pada isi Changelog atau Event Log lengkap (hanya memuat entri seed) memakai isolasi fixture per scope akun yang dinyatakan di `suite.md` (Kemampuan teknis, 2026-11-05); kemampuan itu disediakan tim FE/BE dan belum dikonfirmasi.

## Test Steps

### TC-FA-TAG-1046: screening Filter Panel Event Log

1. Klik tab `To Be Returned`
2. Klik tombol `Event Log`
3. Klik ikon Filter pada modal
4. Verifikasi field "Received At" (date range, placeholder "Select date"), "Return Group" (placeholder "All groups"), "Handed Over By" ("All users"), "Received By" ("All users"), "Method" ("All methods"), dan "Final Status" ("All statuses")
5. Klik field "Return Group"
6. Verifikasi field "Return Group" berupa multi-select berisi nilai yang ada di Event Log, bukan tree picker
7. Tutup daftar opsi field "Return Group" (Esc)
8. Verifikasi tidak ada field filter untuk "TAG Code" dan "Last Asset"
9. Verifikasi tombol [Clear Field] dan [Apply] tampil

### TC-FA-TAG-1047: Filter Method

10. Pilih opsi "Scan" pada field "Method"
11. Klik [Apply]
12. Verifikasi tabel hanya menampilkan baris RF-00071
13. Klik [Clear Field]
14. Klik [Apply]

### TC-FA-TAG-1048: Filter Final Status

15. Pilih opsi "Damaged/Missing" pada field "Final Status"
16. Klik [Apply]
17. Verifikasi tabel hanya menampilkan baris NF-00092
18. Klik [Clear Field]
19. Klik [Apply]

### TC-FA-TAG-1049: Filter Return Group

20. Pilih opsi "HQ Warehouse" pada field "Return Group"
21. Klik [Apply]
22. Verifikasi tabel hanya menampilkan baris NF-00092
23. Klik [Clear Field]
24. Klik [Apply]

### TC-FA-TAG-1050: Filter Handed Over By

25. Pilih opsi "Dedi K." pada field "Handed Over By"
26. Klik [Apply]
27. Verifikasi tabel hanya menampilkan baris RF-00071, RF-00093
28. Klik [Clear Field]
29. Klik [Apply]
30. Tutup modal Event Log lewat ikon close

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1046 s.d. 1050). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-1030 s.d. 1036 ada di spec 254 dan 255; TC-FA-TAG-1037 s.d. 1045 dan 1488 ada di spec 256 dan 257; TC-FA-TAG-1046 s.d. 1054 ada di spec 258 dan 259; TC-FA-TAG-1055 s.d. 1066 ada di spec 260, 261, dan 262; TC-FA-TAG-1067, 1068, dan 1070 ada di spec 263; TC-FA-TAG-1069 ada di spec lain.
- Panel Filter tetap terbuka sesudah [Apply]; kasus berikutnya dimulai dari panel yang sama sesudah Filter dikosongkan.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 7 (menutup daftar opsi); 13, 18, 23, 28 (mengosongkan Filter lewat [Clear Field]); 14, 19, 24, 29 (menerapkan Filter kosong lewat [Apply]); 30 (menutup modal Event Log).
- Asersi tambahan di luar Expected TC: tidak ada selain langkah penghubung di atas.
- A-15: nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` karena asersi bergantung pada kode, urutan, dan jumlah persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-1046 Expected butir b tidak menyebut cara memeriksa bahwa field "Return Group" bukan tree picker; spec membuka field dan mengasersi daftar opsinya berupa multi-select.
  - TC-FA-TAG-1047 s.d. 1050 tidak menyebut cara mengembalikan Filter antar kasus; spec menambah [Clear Field] dan [Apply] sebagai langkah penghubung.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
