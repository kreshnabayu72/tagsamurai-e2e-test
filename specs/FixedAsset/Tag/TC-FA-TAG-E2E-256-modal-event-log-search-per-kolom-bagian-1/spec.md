---
id: TC-FA-TAG-E2E-256-modal-event-log-search-per-kolom-bagian-1
title: "Modal Event Log To Be Returned: Empty State dan Search per Kolom TAG Code sampai Received By (Bagian 1)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1037
  - TC-FA-TAG-1038
  - TC-FA-TAG-1039
  - TC-FA-TAG-1040
  - TC-FA-TAG-1041
  - TC-FA-TAG-1042
coverage:
  web: automated
---

# Modal Event Log To Be Returned: Empty State dan Search per Kolom TAG Code sampai Received By (Bagian 1)

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
- Pemulihan di hook `after`: entri Event Log To Be Returned dikembalikan ke keadaan Pre-setup tiga entri lewat fixture backend bila seeding mengubahnya. Search dikosongkan di akhir tiap kasus.
- Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Isolasi audit trail (butir A-18 iii): asersi yang bergantung pada isi Changelog atau Event Log lengkap (hanya memuat entri seed) memakai isolasi fixture per scope akun yang dinyatakan di `suite.md` (Kemampuan teknis, 2026-11-05); kemampuan itu disediakan tim FE/BE dan belum dikonfirmasi.

## Test Steps

### TC-FA-TAG-1037: tanpa hasil pencarian

1. Klik tab `To Be Returned`
2. Klik tombol `Event Log`
3. Ketik Search `tidak-ada`, tekan Enter
4. Verifikasi tampil ilustrasi, judul "No results found", dan deskripsi "Try adjusting your search or filter."
5. Klik `(←)` pada kotak Search modal

### TC-FA-TAG-1038: Search kolom TAG Code

6. Ketik Search `NF-00092`, tekan Enter
7. Verifikasi tabel hanya menampilkan baris NF-00092
8. Klik `(←)` pada kotak Search modal

### TC-FA-TAG-1039: Search kolom Last Asset

9. Ketik Search `Laptop`, tekan Enter
10. Verifikasi tabel hanya menampilkan baris NF-00092
11. Klik `(←)` pada kotak Search modal

### TC-FA-TAG-1040: Search kolom Return Group

12. Ketik Search `HQ`, tekan Enter
13. Verifikasi tabel hanya menampilkan baris NF-00092
14. Klik `(←)` pada kotak Search modal

### TC-FA-TAG-1041: Search kolom Handed Over By

15. Ketik Search `Rina`, tekan Enter
16. Verifikasi tabel hanya menampilkan baris NF-00092
17. Klik `(←)` pada kotak Search modal

### TC-FA-TAG-1042: Search kolom Received By

18. Ketik Search `Budi`, tekan Enter
19. Verifikasi tabel hanya menampilkan baris RF-00071, RF-00093
20. Klik `(←)` pada kotak Search modal
21. Tutup modal Event Log lewat ikon close

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1037 s.d. 1042). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-1030 s.d. 1036 ada di spec 254 dan 255; TC-FA-TAG-1037 s.d. 1045 dan 1488 ada di spec 256 dan 257; TC-FA-TAG-1046 s.d. 1054 ada di spec 258 dan 259; TC-FA-TAG-1055 s.d. 1066 ada di spec 260, 261, dan 262; TC-FA-TAG-1067, 1068, dan 1070 ada di spec 263; TC-FA-TAG-1069 ada di spec lain.
- Urutan TC mengikuti nomor TC; TC-FA-TAG-1037 (tanpa hasil) berada di awal sebelum Search dengan hasil, dan `Verifikasi` empty state menjadi anchor positif tanpa hasil.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 5, 8, 11, 14, 17, 20 (mengosongkan Search lewat `(←)`); 21 (menutup modal Event Log).
- Asersi tambahan di luar Expected TC: tidak ada.
- A-15: nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` karena asersi bergantung pada kode, urutan, dan jumlah persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-1037 s.d. 1042 tidak menyebut cara mengosongkan Search antar kasus; spec menambah `(←)` sebagai langkah penghubung.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
