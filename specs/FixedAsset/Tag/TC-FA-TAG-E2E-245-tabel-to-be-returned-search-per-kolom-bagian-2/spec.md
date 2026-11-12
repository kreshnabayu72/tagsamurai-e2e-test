---
id: TC-FA-TAG-E2E-245-tabel-to-be-returned-search-per-kolom-bagian-2
title: "Tabel To Be Returned: Search Tidak Peka Huruf, Kolom Since dan Kolom Tersembunyi, serta Kembali ke Halaman 1 (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-987
  - TC-FA-TAG-988
  - TC-FA-TAG-989
  - TC-FA-TAG-990
  - TC-FA-TAG-991
coverage:
  web: automated
---

# Tabel To Be Returned: Search Tidak Peka Huruf, Kolom Since dan Kolom Tersembunyi, serta Kembali ke Halaman 1 (Bagian 2)

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

- Data kasus TC-FA-TAG-991 (kunci `Fixture.fixedAssetTag.tbr25`): 25 Tag To Be Returned dalam scope akun, sehingga tabel berisi lebih dari satu halaman (10 baris per halaman); dimuat pada langkah 29.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned (kode, Last Asset, Reason, Return Group, Current Holder, Since) dan Return Group; tidak ada endpoint yang dikarang di spec ini.
- Pemulihan di hook `after`: dataset To Be Returned dikembalikan ke keadaan Pre-setup empat Tag lewat fixture backend. Kolom Current Holder dipulihkan pada langkah 14; Search dikosongkan pada tiap akhir kasus.
- Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 29) yang menyiapkan atau memulihkan state.

## Test Steps

### TC-FA-TAG-987: huruf besar kecil dan substring

1. Klik tab `To Be Returned`
2. Ketik Search `excavator 20`, tekan Enter
3. Verifikasi tabel menampilkan RF-00071, RF-00088, dan RF-00110 (Last Asset memuat "Excavator 20" sebagai substring)
4. Klik `(←)` pada kotak Search

### TC-FA-TAG-988: kolom Since tidak ikut dicari

5. Ketik Search `Sep`, tekan Enter
6. Verifikasi tabel menampilkan empty state "No results found" dengan deskripsi "Try adjusting your search or filter."
7. Klik `(←)` pada kotak Search

### TC-FA-TAG-989: kolom yang disembunyikan tidak dapat dicari

8. Buka Column Visibility lewat ikon di header kolom aksi
9. Hilangkan centang kolom "Current Holder"
10. Tutup Column Visibility
11. Ketik Search `Rina`, tekan Enter
12. Verifikasi tabel menampilkan empty state "No results found"
13. Buka Column Visibility lewat ikon di header kolom aksi
14. Centang kembali kolom "Current Holder"
15. Tutup Column Visibility
16. Tekan Enter pada kotak Search yang masih berisi `Rina`
17. Verifikasi tabel menampilkan NF-00092
18. Klik `(←)` pada kotak Search

### TC-FA-TAG-990: Search baru berjalan saat Enter dan dibersihkan lewat x lalu Enter

19. Klik ikon Search, ketik `Laptop` tanpa menekan Enter
20. Verifikasi tabel masih menampilkan 4 baris
21. Tekan Enter
22. Verifikasi tabel menampilkan NF-00092 saja
23. Klik ikon `✕` di dalam input Search
24. Verifikasi input Search kosong
25. Verifikasi tabel masih menampilkan hasil pencarian terakhir (NF-00092 saja)
26. Tekan Enter pada input kosong
27. Verifikasi tabel kembali menampilkan 4 baris
28. Klik `(←)` pada kotak Search

### TC-FA-TAG-991: Search dari halaman 2 kembali ke halaman 1

29. Atur dataset tab To Be Returned menjadi 25 Tag dalam scope (kunci `tbr25`) lewat fixture backend hingga tersimpan, muat ulang halaman (F5), lalu klik tab `To Be Returned`
30. Pindah ke halaman 2 tabel
31. Ketik Search `RF`, tekan Enter
32. Verifikasi tabel berada di halaman 1
33. Verifikasi tabel menampilkan hasil pencarian `RF`
34. Klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-987 s.d. 991). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-980 s.d. 986 ada di spec 244.
- Urutan TC mengikuti nomor TC; TC-FA-TAG-991 berada di akhir karena memakai dataset 25 Tag (beda dari empat Tag Pre-setup) dan dimuat sekali lewat fixture.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 4, 7, 18, 28, 34 (mengosongkan Search lewat `(←)` yang menutup input dan mereset tabel); 10, 15 (menutup Column Visibility); 29 (memuat dataset 25 Tag dan membuka tab).
- Asersi tambahan di luar Expected TC: tidak ada.
- A-15: nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` karena asersi bergantung pada kode, urutan, dan jumlah persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 29) yang menyiapkan atau memulihkan state.
- Temuan untuk QA:
  - TC-FA-TAG-989 menulis "ulangi pencarian" tanpa menyebut apakah pencarian dijalankan ulang otomatis saat kolom ditampilkan; spec menekan Enter pada kotak Search yang masih berisi "Rina".
  - TC-FA-TAG-991 memakai precondition 25 Tag (bukan empat Tag Pre-setup); spec memuat dataset itu lewat fixture sebagai langkah penghubung dan tidak mengarang kode Tag-nya.
  - TC-FA-TAG-991 Expected tidak menyebut jumlah baris atau kode hasil Search `RF`; spec mengasersi "hasil pencarian" dan halaman 1.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
