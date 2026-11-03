---
id: TC-FA-TAG-E2E-262-modal-event-log-sort-column-visibility-dan-pagination-bagian-3
title: "Modal Event Log To Be Returned: Column Visibility, Setup Column, dan Pagination (Bagian 3)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1063
  - TC-FA-TAG-1064
  - TC-FA-TAG-1065
  - TC-FA-TAG-1066
coverage:
  web: automated
---

# Modal Event Log To Be Returned: Column Visibility, Setup Column, dan Pagination (Bagian 3)

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

- Data TC-FA-TAG-1066 (kunci `Fixture.fixedAssetTag.eventLog25`): 25 entri Event Log To Be Returned dalam scope akun (kode dan atribut ditentukan seeding; TC hanya menyebut jumlahnya); dimuat pada langkah 24.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk entri Event Log To Be Returned; tidak ada endpoint yang dikarang di spec ini.
- Pemulihan di hook `after`: entri Event Log To Be Returned dikembalikan ke keadaan Pre-setup tiga entri lewat fixture backend.
- Pemulihan preferensi kolom: hook `after` spec ini menghapus preferensi kolom di browser (kemampuan disediakan tim FE; bukan lewat `[Reset to Default]`), sesuai daftar di `suite.md`. Spec ini menyimpan konfigurasi kolom pada TC-FA-TAG-1065 (langkah 20).

## Test Steps

### TC-FA-TAG-1063: Column Visibility menyembunyikan kolom Method

1. Klik tab `To Be Returned`
2. Klik tombol `Event Log`
3. Buka Column Visibility pada tabel modal
4. Hilangkan centang kolom "Method"
5. Verifikasi kolom "Method" langsung hilang dari tabel modal
6. Verifikasi kolom lain tetap tampil
7. Centang kembali kolom "Method"
8. Tutup Column Visibility

### TC-FA-TAG-1064: kolom visible terakhir tidak dapat disembunyikan

9. Buka Column Visibility
10. Sembunyikan semua kolom kecuali "Received At"
11. Arahkan kursor ke centang "Received At"
12. Verifikasi centang "Received At" Disabled (tetap tampil) dengan tooltip "At least one column must remain visible."
13. Tampilkan kembali semua kolom lain lewat Column Visibility, lalu tutup Column Visibility

### TC-FA-TAG-1065: Setup Column, Save menyimpan dan ikon close membuang perubahan

14. Buka modal "Setup Column"
15. Hilangkan centang kolom "Final Status"
16. Klik ikon close pada modal Setup Column
17. Verifikasi kolom "Final Status" tetap tampil di tabel
18. Buka modal "Setup Column"
19. Hilangkan centang kolom "Final Status"
20. Klik [Save]
21. Verifikasi kolom "Final Status" tersembunyi
22. Tampilkan kembali kolom "Final Status" lewat Column Visibility, lalu tutup Column Visibility

### TC-FA-TAG-1066: pagination Event Log

23. Tutup modal Event Log lewat ikon close
24. Atur Event Log To Be Returned menjadi 25 entri dalam scope (kunci `eventLog25`) lewat fixture backend hingga tersimpan
25. Klik tombol `Event Log`
26. Verifikasi halaman 1 menampilkan 10 baris
27. Buka pilihan jumlah baris per halaman
28. Verifikasi pilihan jumlah baris per halaman adalah 10, 25, 50, 100
29. Ganti jumlah baris per halaman menjadi 25
30. Verifikasi tabel kembali ke halaman 1
31. Verifikasi tabel menampilkan 25 baris
32. Tutup modal Event Log lewat ikon close

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1063 s.d. 1066). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-1030 s.d. 1036 ada di spec 254 dan 255; TC-FA-TAG-1037 s.d. 1045 dan 1488 ada di spec 256 dan 257; TC-FA-TAG-1046 s.d. 1054 ada di spec 258 dan 259; TC-FA-TAG-1055 s.d. 1066 ada di spec 260, 261, dan 262; TC-FA-TAG-1067, 1068, dan 1070 ada di spec 263; TC-FA-TAG-1069 ada di spec lain.
- Urutan TC mengikuti nomor TC; TC-FA-TAG-1066 berada di akhir karena memakai dataset 25 entri yang berbeda dari tiga entri Pre-setup dan dimuat sekali.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 7 (memulihkan kolom Method); 8 (menutup Column Visibility); 13 (memulihkan kolom yang disembunyikan); 22 (memulihkan kolom Final Status); 23, 32 (menutup modal Event Log); 24 (memuat dataset 25 entri).
- Asersi tambahan di luar Expected TC: tidak ada.
- Temuan untuk QA:
  - TC-FA-TAG-1063 Expected "kolom lain tetap tampil" tidak menyebut kolom yang dimaksud; spec mengasersi kolom lain tetap tampil tanpa mendaftarnya.
  - TC-FA-TAG-1066 tidak menyebut kode dan atribut 25 entri Event Log; spec hanya memakai jumlahnya.
  - TC-FA-TAG-1063 s.d. 1065 tidak menyebut cara mengembalikan kolom; spec menambah langkah penghubung.
  - Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada kode, urutan, dan jumlah persis; Lampiran A belum memuat butir modul ini, sehingga seeding idempotent dan pemulihan lewat fixture backend (suite serial) dicatat sebagai kebutuhan.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
