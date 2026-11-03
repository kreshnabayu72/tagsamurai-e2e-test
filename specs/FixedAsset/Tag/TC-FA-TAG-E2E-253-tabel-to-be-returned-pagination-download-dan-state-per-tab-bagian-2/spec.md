---
id: TC-FA-TAG-E2E-253-tabel-to-be-returned-pagination-download-dan-state-per-tab-bagian-2
title: "Tabel To Be Returned: Download XLSX, Download Tanpa Hasil, dan State Tab Setelah Pindah Tab serta Refresh (Bagian 2)"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1024
  - TC-FA-TAG-1025
  - TC-FA-TAG-1027
  - TC-FA-TAG-1028
  - TC-FA-TAG-1029
coverage:
  web: automated
---

# Tabel To Be Returned: Download XLSX, Download Tanpa Hasil, dan State Tab Setelah Pindah Tab serta Refresh (Bagian 2)

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

- Data Pre-setup tab To Be Returned (kunci `Fixture.fixedAssetTag.tbr25`): 25 Tag To Be Returned dalam scope akun (kode dan atribut Tag ditentukan seeding; TC hanya menyebut jumlahnya), dimuat pada langkah 26 untuk TC-FA-TAG-1027.
- Data Pre-setup tab Paired (dipakai hanya sebagai pembanding pada TC-FA-TAG-1028; kunci `Fixture.fixedAssetTag.pairedGrup`; tanpa suffix `{runId}`): grup Excavator 20 Ton / Plant A, Excavator 20 Ton / Plant B, Laptop Pro 14 / HQ, dan Forklift Manual / Plant A tampil di tabel grup T-TAG-01.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned (kode, Last Asset, Reason, Return Group, Current Holder, Since) dan Return Group; tidak ada endpoint yang dikarang di spec ini.
- Kemampuan teknis (disediakan tim FE/BE): pembaca berkas unduhan CSV/XLSX (nama berkas, ekstensi, header kolom, jumlah baris, isi sel, nama sheet) dan pendeteksi toast pada saat klik pilihan format.
- Pemulihan di hook `after`: dataset To Be Returned dikembalikan ke keadaan Pre-setup empat Tag lewat fixture backend bila seeding mengubahnya. Search dikosongkan dan sort dikembalikan ke netral pada akhir spec.

## Test Steps

### TC-FA-TAG-1024: Download XLSX tab To Be Returned

1. Klik tab `To Be Returned`
2. Klik ikon Download
3. Klik "Download as XLSX"
4. Verifikasi tidak ada toast sukses
5. Verifikasi file bernama "To-Be-Returned-TAGs" berekstensi .xlsx terunduh
6. Verifikasi file memuat satu sheet bernama "Sheet1"
7. Verifikasi sheet berisi 4 baris Tag

### TC-FA-TAG-1025: Download saat hasil nol baris

8. Ketik Search `tidak-ada`, tekan Enter
9. Verifikasi tabel menampilkan empty state "No results found"
10. Verifikasi tombol Download tetap aktif
11. Klik ikon Download
12. Klik "Download as CSV"
13. Verifikasi tidak ada toast
14. Verifikasi file terunduh hanya berisi baris header kolom visible
15. Klik `(←)` pada kotak Search

### TC-FA-TAG-1028: state tab To Be Returned tidak memengaruhi tab Paired

16. Ketik Search `RF`, tekan Enter
17. Pindah ke tab `Paired`
18. Verifikasi Search tab `Paired` kosong
19. Verifikasi tabel grup menampilkan keempat grup Pre-setup tab Paired tanpa tersaring oleh kata kunci `RF`
20. Kembali ke tab `To Be Returned`

### TC-FA-TAG-1029: refresh manual mempertahankan tab dan state

21. Ganti isi kotak search dengan `Laptop`, tekan Enter
22. Tekan F5
23. Verifikasi tab `To Be Returned` tetap aktif
24. Verifikasi Search `Laptop` masih berlaku
25. Verifikasi tabel menampilkan NF-00092

### TC-FA-TAG-1027: state Search, Filter, Sort, dan halaman dipulihkan setelah pindah tab

26. Atur dataset tab To Be Returned menjadi 25 Tag dalam scope (kunci `tbr25`) lewat fixture backend hingga tersimpan, muat ulang halaman (F5), lalu klik tab `To Be Returned`
27. Ganti isi kotak search dengan `RF`, tekan Enter
28. Klik ikon sort kolom "TAG Code", lalu catat baris yang tampil pada tabel
29. Pindah ke tab `Paired`
30. Kembali ke tab `To Be Returned`
31. Verifikasi input Search masih berisi `RF`
32. Verifikasi sort kolom "TAG Code" masih aktif
33. Verifikasi tabel menampilkan hasil yang sama dengan baris yang dicatat
34. Klik ikon sort kolom "TAG Code" dua kali lagi hingga indikator netral, lalu klik `(←)` pada kotak Search

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1024 s.d. 1029). Tidak ada TC hanya-BE. TC-FA-TAG-1026 (Download gagal dengan respons 5xx) bukan bagian spec ini.
- Pembagian TC lintas spec: TC-FA-TAG-1018 s.d. 1021 ada di spec 252 dan TC-FA-TAG-1022 dan 1023 ada di spec 270.
- Urutan TC di dalam spec: TC-FA-TAG-1024, 1025, 1028, 1029, lalu 1027, karena TC-FA-TAG-1027 memakai dataset 25 Tag (beda dari empat Tag Pre-setup) sehingga dataset diganti satu kali di akhir (S-10).
- Absence toast (TC-FA-TAG-1024 dan 1025) diletakkan sesudah pemicu klik pilihan format dan sebelum `Verifikasi` berkas (bagian 8b butir 11).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 15 (mengosongkan Search lewat `(←)`); 20 (kembali ke tab To Be Returned); 26 (memuat dataset 25 Tag dan membuka tab); 34 (mengembalikan sort dan mengosongkan Search).
- Asersi tambahan di luar Expected TC: `Verifikasi` empty state "No results found" sebelum `Verifikasi` tombol Download (TC-FA-TAG-1025) sebagai anchor positif absence toast dan isi berkas (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-TAG-1028 Expected menyebut "tabel grup tidak tersaring" tetapi precondition TC hanya memuat Tag To Be Returned dan tidak menyebut dataset tab Paired; spec memakai grup Pre-setup tab Paired yang dipakai spec lain sebagai pembanding.
  - TC-FA-TAG-1027 Expected "tabel menampilkan hasil yang sama" tidak menyebut baris yang diharapkan; spec mencatat baris yang tampil sebelum pindah tab dan membandingkannya.
  - TC-FA-TAG-1027 memakai precondition 25 Tag (bukan empat Tag Pre-setup); dataset itu dimuat lewat fixture sebagai langkah penghubung.
  - Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada kode, urutan, dan jumlah persis; Lampiran A belum memuat butir modul ini, sehingga seeding idempotent dan pemulihan lewat fixture backend (suite serial) dicatat sebagai kebutuhan.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
