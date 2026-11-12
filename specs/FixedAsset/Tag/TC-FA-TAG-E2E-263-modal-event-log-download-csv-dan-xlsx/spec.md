---
id: TC-FA-TAG-E2E-263-modal-event-log-download-csv-dan-xlsx
title: "Modal Event Log To Be Returned: Download CSV Mengikuti Filter dan Kolom, Download XLSX, serta Download Tanpa Hasil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1067
  - TC-FA-TAG-1068
  - TC-FA-TAG-1070
coverage:
  web: automated
---

# Modal Event Log To Be Returned: Download CSV Mengikuti Filter dan Kolom, Download XLSX, serta Download Tanpa Hasil

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
- Kemampuan teknis (disediakan tim FE/BE): pembaca berkas unduhan CSV/XLSX (nama berkas, ekstensi, header kolom, jumlah baris, isi sel, nama sheet) dan pendeteksi toast pada saat klik pilihan format.
- Pemulihan di hook `after`: entri Event Log To Be Returned dikembalikan ke keadaan Pre-setup tiga entri lewat fixture backend bila seeding mengubahnya. Filter dikosongkan, kolom Method dipulihkan, dan Search dikosongkan pada akhir spec.
- Pemulihan preferensi kolom: kolom Method disembunyikan lewat Column Visibility (tersimpan di browser) dan ditampilkan kembali pada langkah 16.
- Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom di browser lewat Column Visibility (langkah 7, 16), dipulihkan hook `after` (lihat `suite.md`).
- Isolasi audit trail (butir A-18 iii): asersi yang bergantung pada isi Changelog atau Event Log lengkap (hanya memuat entri seed) memakai isolasi fixture per scope akun yang dinyatakan di `suite.md` (Kemampuan teknis, 2026-11-05); kemampuan itu disediakan tim FE/BE dan belum dikonfirmasi.

## Test Steps

### TC-FA-TAG-1067: Download Event Log CSV mengikuti Search, Filter, dan kolom tampil

1. Klik tab `To Be Returned`
2. Klik tombol `Event Log`
3. Klik ikon Filter pada modal
4. Pilih opsi "Scan" pada field "Method"
5. Klik [Apply]
6. Buka Column Visibility pada tabel modal
7. Sembunyikan kolom "Method"
8. Tutup Column Visibility
9. Klik ikon Download
10. Klik "Download as CSV"
11. Verifikasi tidak ada toast sukses
12. Verifikasi file bernama "Event-Log-To-Be-Returned" berekstensi .csv terunduh
13. Verifikasi file berisi header kolom yang tampil (tanpa "Method")
14. Verifikasi file berisi satu baris RF-00071
15. Verifikasi kolom Handed Over By dan Received By pada baris RF-00071 berupa nama lengkap
16. Tampilkan kembali kolom "Method" lewat Column Visibility, lalu tutup Column Visibility
17. Klik [Clear Field]
18. Klik [Apply]

### TC-FA-TAG-1068: Download Event Log XLSX

19. Klik ikon Download
20. Klik "Download as XLSX"
21. Verifikasi tidak ada toast sukses
22. Verifikasi file bernama "Event-Log-To-Be-Returned" berekstensi .xlsx terunduh
23. Verifikasi file memuat satu sheet bernama "Sheet1"
24. Verifikasi sheet berisi 3 baris entri

### TC-FA-TAG-1070: Download Event Log dengan hasil nol baris

25. Ketik Search `tidak-ada`, tekan Enter
26. Verifikasi tabel modal menampilkan empty state "No results found"
27. Klik ikon Download
28. Klik "Download as CSV"
29. Verifikasi tidak ada toast
30. Verifikasi file terunduh hanya berisi baris header kolom visible
31. Klik `(←)` pada kotak Search modal
32. Tutup modal Event Log lewat ikon close

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1067 s.d. 1070). Tidak ada TC hanya-BE. TC-FA-TAG-1069 (Download Event Log gagal dengan respons 5xx) bukan bagian spec ini.
- Pembagian TC lintas spec: TC-FA-TAG-1030 s.d. 1036 ada di spec 254 dan 255; TC-FA-TAG-1037 s.d. 1045 dan 1488 ada di spec 256 dan 257; TC-FA-TAG-1046 s.d. 1054 ada di spec 258 dan 259; TC-FA-TAG-1055 s.d. 1066 ada di spec 260, 261, dan 262; TC-FA-TAG-1067, 1068, dan 1070 ada di spec 263; TC-FA-TAG-1069 ada di spec lain.
- Absence toast diletakkan sesudah pemicu klik pilihan format dan sebelum `Verifikasi` berkas (bagian 8b butir 11); pemicu itu menjadi anchor positif bagi `Verifikasi` berkas terunduh.
- Absence toast pada TC-FA-TAG-1070 didahului `Verifikasi` empty state "No results found" sebagai anchor positif surface (bagian 8b butir 2).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 8 (menutup Column Visibility); 16 (memulihkan kolom Method); 17 (mengosongkan Filter lewat [Clear Field]); 18 (menerapkan Filter kosong lewat [Apply]); 31 (mengosongkan Search lewat `(←)`); 32 (menutup modal Event Log).
- Asersi tambahan di luar Expected TC: `Verifikasi` empty state "No results found" sebelum klik Download (TC-FA-TAG-1070) sebagai anchor positif absence toast dan isi berkas (bagian 8b butir 2).
- A-15: nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` karena asersi bergantung pada kode, urutan, dan jumlah persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom di browser lewat Column Visibility (langkah 7, 16), dipulihkan hook `after` (lihat `suite.md`).
- Temuan untuk QA:
  - TC-FA-TAG-1067 Expected butir b "nama lengkap" untuk Handed Over By dan Received By tidak menyebut nama lengkap yang diharapkan (hanya "Dedi K." bernama lengkap Dedi Kurniawan di TC lain); spec mengasersi "berupa nama lengkap" tanpa menambah nilai.
  - TC-FA-TAG-1067 butir b "header kolom yang tampil" tidak menyebut urutan header; spec mengasersi himpunan header tanpa Method.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
