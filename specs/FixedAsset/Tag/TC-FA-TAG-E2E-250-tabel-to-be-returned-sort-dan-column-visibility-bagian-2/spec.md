---
id: TC-FA-TAG-E2E-250-tabel-to-be-returned-sort-dan-column-visibility-bagian-2
title: "Tabel To Be Returned: Sort Kolom Reason, Sort dengan Filter Aktif, dan Column Visibility (Bagian 2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1010
  - TC-FA-TAG-1011
  - TC-FA-TAG-1012
  - TC-FA-TAG-1013
coverage:
  web: automated
---

# Tabel To Be Returned: Sort Kolom Reason, Sort dengan Filter Aktif, dan Column Visibility (Bagian 2)

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
- Pemulihan di hook `after`: dataset To Be Returned dikembalikan ke keadaan Pre-setup empat Tag lewat fixture backend bila seeding mengubahnya. Filter dan sort dikembalikan ke netral pada akhir kasus terkait; kolom Since dipulihkan pada langkah 32.
- Pemulihan preferensi kolom: hook `after` spec ini menghapus preferensi kolom di browser (kemampuan disediakan tim FE; bukan lewat `[Reset to Default]`), sesuai daftar di `suite.md`. Kolom tersembunyi pada TC-FA-TAG-1013 tersimpan di browser dan diasersi tetap tersembunyi setelah F5.
- Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom di browser lewat Column Visibility (langkah 20, 22, 26, 32), dipulihkan hook `after` (lihat `suite.md`).

## Test Steps

### TC-FA-TAG-1010: ikon sort kolom Reason

1. Klik tab `To Be Returned`
2. Klik ikon sort kolom "Reason" (klik pertama)
3. Verifikasi klik pertama menampilkan panah naik pada kolom "Reason"
4. Klik ikon sort kolom "Reason" (klik kedua)
5. Verifikasi klik kedua menampilkan panah turun pada kolom "Reason"
6. Klik ikon sort kolom "Reason" (klik ketiga)
7. Verifikasi klik ketiga: indikator netral dan urutan kembali ke urutan bawaan Since terlama di atas (RF-00071, RF-00110, RF-00088, NF-00092)

### TC-FA-TAG-1011: sort tidak mereset Search dan Filter

8. Klik ikon Filter
9. Pilih opsi "RFID" pada "TAG Type"
10. Klik [Apply]
11. Klik ikon sort kolom "Last Asset"
12. Verifikasi tabel tetap hanya memuat Tag RFID (RF-00071, RF-00088, RF-00110)
13. Verifikasi filter "TAG Type" tetap aktif
14. Klik ikon sort kolom "Last Asset" dua kali lagi hingga indikator netral
15. Klik [Clear Field]
16. Klik [Apply]

### TC-FA-TAG-1012: Column Visibility diterapkan langsung

17. Arahkan kursor ke ikon di header kolom aksi
18. Verifikasi tooltip ikon menampilkan "Column Visibility"
19. Klik ikon di header kolom aksi untuk membuka Column Visibility
20. Hilangkan centang kolom "Reason"
21. Verifikasi kolom "Reason" langsung hilang dari tabel
22. Centang kembali kolom "Reason"
23. Verifikasi kolom "Reason" tampil lagi
24. Tutup Column Visibility

### TC-FA-TAG-1013: pengaturan kolom tersimpan setelah muat ulang

25. Buka Column Visibility lewat ikon di header kolom aksi
26. Sembunyikan kolom "Since"
27. Tutup Column Visibility
28. Tekan F5 untuk memuat ulang halaman
29. Klik tab `To Be Returned`
30. Verifikasi kolom "TAG Code" tetap tampil setelah halaman dimuat ulang
31. Verifikasi kolom "Since" tetap tersembunyi setelah halaman dimuat ulang
32. Tampilkan kembali kolom "Since" lewat Column Visibility, lalu tutup Column Visibility

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1010 s.d. 1013). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-1005 s.d. 1009 ada di spec 249, TC-FA-TAG-1014 dan 1015 ada di spec 269, dan TC-FA-TAG-1016 dan 1017 ada di spec 251.
- TC-FA-TAG-1010 menulis "klik ikon sort tiga kali berturut-turut" dengan satu butir Expected; spec memverifikasi sesudah tiap klik karena indikator berubah tiap klik (bagian 8b butir 5).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 14 (mengembalikan sort kolom Last Asset ke netral); 15 (mengosongkan Filter lewat [Clear Field]); 16 (menerapkan Filter kosong lewat [Apply]); 24, 27 (menutup Column Visibility); 32 (memulihkan kolom Since).
- Asersi tambahan di luar Expected TC: tidak ada.
- A-15: nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` karena asersi bergantung pada kode, urutan, dan jumlah persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan menyimpan preferensi kolom di browser lewat Column Visibility (langkah 20, 22, 26, 32), dipulihkan hook `after` (lihat `suite.md`).
- Temuan untuk QA:
  - TC-FA-TAG-1011 Expected "filter TAG Type tetap aktif" tidak menyebut cara memeriksanya; spec memeriksa nilai field "TAG Type" pada panel Filter.
  - TC-FA-TAG-1011 s.d. 1013 tidak menyebut cara mengembalikan sort, Filter, dan kolom; spec menambah langkah penghubung.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
