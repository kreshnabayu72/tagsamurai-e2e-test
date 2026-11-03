---
id: TC-FA-TAG-E2E-254-modal-event-log-screening-format-sel-dan-penutupan-bagian-1
title: "Modal Event Log To Be Returned: Screening, Urutan Bawaan, Format Sel, dan Hover Tooltip (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1030
  - TC-FA-TAG-1031
  - TC-FA-TAG-1032
  - TC-FA-TAG-1033
  - TC-FA-TAG-1034
coverage:
  web: automated
---

# Modal Event Log To Be Returned: Screening, Urutan Bawaan, Format Sel, dan Hover Tooltip (Bagian 1)

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

- Data TC-FA-TAG-1034: entri Event Log yang sama dengan tabel di atas; 'Disposal Center' berada di bawah group induk 'Operations' dan 'Dedi K.' bernama lengkap Dedi Kurniawan.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk entri Event Log To Be Returned; tidak ada endpoint yang dikarang di spec ini.
- Pemulihan di hook `after`: entri Event Log To Be Returned dikembalikan ke keadaan Pre-setup tiga entri lewat fixture backend bila seeding mengubahnya.

## Test Steps

### TC-FA-TAG-1030: screening Modal Event Log

1. Klik tab `To Be Returned`
2. Klik tombol `Event Log`
3. Verifikasi modal berjudul "Event Log: To Be Returned" terbuka
4. Verifikasi modal hanya memiliki ikon close
5. Verifikasi toolbar rata kanan di atas tabel berisi ikon Search, Filter, dan Download
6. Klik ikon Search pada toolbar modal
7. Verifikasi input Search memiliki placeholder "Search TAG code, last asset, group..."
8. Klik `(←)` pada kotak Search modal
9. Verifikasi header kolom berurutan: "Received At", "TAG Code", "Last Asset", "Return Group", "Handed Over By", "Received By", "Method", "Final Status"
10. Verifikasi footer pagination tampil
11. Verifikasi tidak ada aksi baris, checkbox, atau tombol Create (read-only)

### TC-FA-TAG-1031: urutan bawaan Received At terbaru di atas

12. Verifikasi baris berurutan dari atas: RF-00093 (27 Okt 2026 14:15), RF-00071 (26 Okt 2026 10:02), NF-00092 (26 Okt 2026 09:40)

### TC-FA-TAG-1032: format sel dan badge tiap kolom

13. Verifikasi kolom "TAG Code" pada baris RF-00071, NF-00092, dan RF-00093 menampilkan ikon tipe diikuti kode dan bukan tautan
14. Verifikasi kolom "Method" menampilkan badge dengan teks persis "Scan", "Manual", atau "Assigned"
15. Verifikasi kolom "Final Status" menampilkan badge "Available" (severity success), "Damaged/Missing" (severity warning), dan "Paired" (severity info)
16. Verifikasi kolom "Handed Over By" dan "Received By" memakai format [First Name] [Last Initial] (nilai "Dedi K." dan "Budi S.")
17. Verifikasi kolom "Return Group" menampilkan badge Primary

### TC-FA-TAG-1033: pasangan Method dan Final Status

18. Verifikasi Method "Scan" selalu berpasangan dengan Final Status "Available"
19. Verifikasi Method "Manual" selalu berpasangan dengan Final Status "Damaged/Missing"
20. Verifikasi Method "Assigned" selalu berpasangan dengan Final Status "Paired"

### TC-FA-TAG-1034: hover Return Group dan nama pengguna menampilkan bentuk lengkap

21. Arahkan kursor ke badge "Disposal Center" baris RF-00071
22. Verifikasi tooltip Return Group menampilkan "Operations > Disposal Center"
23. Arahkan kursor ke teks "Dedi K." baris RF-00071
24. Verifikasi tooltip nama menampilkan nama lengkap Dedi Kurniawan
25. Tutup modal Event Log lewat ikon close

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1030 s.d. 1034). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-1030 s.d. 1036 ada di spec 254 dan 255; TC-FA-TAG-1037 s.d. 1045 dan 1488 ada di spec 256 dan 257; TC-FA-TAG-1046 s.d. 1054 ada di spec 258 dan 259; TC-FA-TAG-1055 s.d. 1066 ada di spec 260, 261, dan 262; TC-FA-TAG-1067, 1068, dan 1070 ada di spec 263; TC-FA-TAG-1069 ada di spec lain.
- TC-FA-TAG-1030 Expected butir b menyebut placeholder ikon Search yang hanya terlihat setelah input dibuka; spec membuka input lewat langkah penghubung dan menutupnya kembali.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 6 (membuka input Search untuk memeriksa placeholder); 8 (mengosongkan Search lewat `(←)`); 25 (menutup modal Event Log).
- Asersi tambahan di luar Expected TC: tidak ada selain langkah penghubung placeholder di atas.
- Temuan untuk QA:
  - TC-FA-TAG-1030 s.d. 1033 tidak menyebut cara membuka input Search untuk memeriksa placeholder; spec menambah langkah penghubung.
  - TC-FA-TAG-1032 Expected "severity success, warning, info" dan "badge Primary" tidak menyebut cara mengamati severity; mekanismenya tidak didefinisikan di TC, PRD, atau LLD dan diminta dari tim FE.
  - TC-FA-TAG-1034 menyebut nama lengkap hanya untuk "Dedi K." (Dedi Kurniawan); nama lengkap pengguna lain tidak diasersi.
  - Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada kode, urutan, dan jumlah persis; Lampiran A belum memuat butir modul ini, sehingga seeding idempotent dan pemulihan lewat fixture backend (suite serial) dicatat sebagai kebutuhan.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
