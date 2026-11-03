---
id: TC-FA-TAG-E2E-257-modal-event-log-search-per-kolom-bagian-2
title: "Modal Event Log To Be Returned: Search Method dan Final Status, Received At Tidak Dicari, serta Handed Over By Kosong (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1043
  - TC-FA-TAG-1044
  - TC-FA-TAG-1045
  - TC-FA-TAG-1488
coverage:
  web: automated
---

# Modal Event Log To Be Returned: Search Method dan Final Status, Received At Tidak Dicari, serta Handed Over By Kosong (Bagian 2)

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

- Data TC-FA-TAG-1488 (kunci `Fixture.fixedAssetTag.eventLog72`): satu entri Event Log: 27 Okt 2026 14:15, RF-00072 (RFID), Last Asset 'Excavator 20 Ton - 3', Return Group 'Disposal Center', Handed Over By kosong (saat Tag dilepas aset tidak punya pemegang terakhir maupun pelaku disposal), Received By 'Budi S.', Method 'Scan', Final Status 'Available'; dimuat pada langkah 13.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk entri Event Log To Be Returned; tidak ada endpoint yang dikarang di spec ini.
- Pemulihan di hook `after`: entri Event Log To Be Returned dikembalikan ke keadaan Pre-setup tiga entri lewat fixture backend. Search dikosongkan di akhir tiap kasus.

## Test Steps

### TC-FA-TAG-1043: Search "Manual"

1. Klik tab `To Be Returned`
2. Klik tombol `Event Log`
3. Ketik Search `Manual`, tekan Enter
4. Verifikasi tabel hanya menampilkan baris NF-00092
5. Klik `(←)` pada kotak Search modal

### TC-FA-TAG-1044: Search "Paired"

6. Ketik Search `Paired`, tekan Enter
7. Verifikasi tabel hanya menampilkan baris RF-00093
8. Klik `(←)` pada kotak Search modal

### TC-FA-TAG-1045: kolom Received At tidak ikut dicari

9. Ketik Search `Okt`, tekan Enter
10. Verifikasi tabel menampilkan "No results found" dan "Try adjusting your search or filter."
11. Klik `(←)` pada kotak Search modal

### TC-FA-TAG-1488: Handed Over By kosong tampil dengan tanda "—"

12. Tutup modal Event Log lewat ikon close
13. Atur Event Log To Be Returned menjadi satu entri RF-00072 (kunci `eventLog72`) lewat fixture backend hingga tersimpan
14. Klik tombol `Event Log`
15. Verifikasi sel "Handed Over By" baris RF-00072 menampilkan "—"
16. Verifikasi sel "Received By" baris RF-00072 menampilkan "Budi S."
17. Tutup modal Event Log lewat ikon close

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1043 s.d. 1045). Tidak ada TC hanya-BE. Ditambah TC-FA-TAG-1488.
- Pembagian TC lintas spec: TC-FA-TAG-1030 s.d. 1036 ada di spec 254 dan 255; TC-FA-TAG-1037 s.d. 1045 dan 1488 ada di spec 256 dan 257; TC-FA-TAG-1046 s.d. 1054 ada di spec 258 dan 259; TC-FA-TAG-1055 s.d. 1066 ada di spec 260, 261, dan 262; TC-FA-TAG-1067, 1068, dan 1070 ada di spec 263; TC-FA-TAG-1069 ada di spec lain.
- Urutan TC: TC-FA-TAG-1043, 1044, 1045, lalu TC-FA-TAG-1488, karena TC-FA-TAG-1488 memakai dataset satu entri yang berbeda dari tiga entri Pre-setup dan dimuat sekali di akhir (S-10).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 5, 8, 11 (mengosongkan Search lewat `(←)`); 12, 17 (menutup modal Event Log); 13 (memuat dataset satu entri RF-00072).
- Asersi tambahan di luar Expected TC: tidak ada.
- Temuan untuk QA:
  - TC-FA-TAG-1488 Expected "tanda —" tidak menyebut karakter persisnya selain judul TC; spec memakai karakter "—" (em dash) seperti di judul dan Expected TC.
  - TC-FA-TAG-1488 hanya menyebut satu entri Event Log, sedangkan tiga entri Pre-setup lain tidak disebut; spec memakai dataset satu entri.
  - Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada kode, urutan, dan jumlah persis; Lampiran A belum memuat butir modul ini, sehingga seeding idempotent dan pemulihan lewat fixture backend (suite serial) dicatat sebagai kebutuhan.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
