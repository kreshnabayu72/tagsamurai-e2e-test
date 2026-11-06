---
id: TC-FA-TAG-E2E-246-tabel-to-be-returned-filter-per-kolom-dan-kombinasi-bagian-1
title: "Tabel To Be Returned: Screening Filter Panel dan Filter TAG Type, Reason, serta Return Group (Bagian 1)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-992
  - TC-FA-TAG-993
  - TC-FA-TAG-994
  - TC-FA-TAG-995
  - TC-FA-TAG-996
coverage:
  web: automated
---

# Tabel To Be Returned: Screening Filter Panel dan Filter TAG Type, Reason, serta Return Group (Bagian 1)

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
- Pemulihan di hook `after`: dataset To Be Returned dikembalikan ke keadaan Pre-setup empat Tag lewat fixture backend bila seeding mengubahnya. Filter dikosongkan di akhir tiap kasus.
- Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.

## Test Steps

### TC-FA-TAG-992: screening Filter Panel

1. Klik tab `To Be Returned`
2. Klik ikon Filter
3. Verifikasi ikon Filter berubah gelap
4. Verifikasi panel Filter tampil di bawah toolbar
5. Verifikasi field berlabel "TAG Type" (placeholder "All types"), "Reason" ("All reasons"), "Return Group" ("All groups"), "Current Holder" ("All users"), dan "Since" (date range, placeholder "Select date")
6. Verifikasi tombol [Clear Field] di kiri dan [Apply] di kanan
7. Verifikasi tidak ada field filter untuk "Last Asset"

### TC-FA-TAG-993: Filter TAG Type RFID

8. Pilih opsi "RFID" pada field "TAG Type"
9. Klik [Apply]
10. Verifikasi tabel menampilkan RF-00071, RF-00088, dan RF-00110
11. Verifikasi NF-00092 tidak tampil
12. Klik [Clear Field]
13. Klik [Apply]

### TC-FA-TAG-994: Filter TAG Type multi-pilih RFID dan NFC

14. Pilih opsi "RFID" dan "NFC" pada field "TAG Type"
15. Klik [Apply]
16. Verifikasi tabel menampilkan keempat Tag (RF-00071, RF-00088, NF-00092, RF-00110)
17. Klik [Clear Field]
18. Klik [Apply]

### TC-FA-TAG-995: Filter Reason Disposal

19. Buka daftar opsi field "Reason"
20. Verifikasi opsi pada field "Reason" hanya "Disposal"
21. Pilih opsi "Disposal" pada field "Reason"
22. Klik [Apply]
23. Verifikasi tabel menampilkan keempat Tag (RF-00071, RF-00088, NF-00092, RF-00110)
24. Klik [Clear Field]
25. Klik [Apply]

### TC-FA-TAG-996: Filter Return Group lewat tree picker

26. Klik field "Return Group" untuk membuka Modal Tree Picker
27. Centang node "Disposal Center"
28. Klik [Select]
29. Klik [Apply]
30. Verifikasi field "Return Group" menampilkan chip "Disposal Center"
31. Verifikasi tabel menampilkan RF-00071, RF-00088, dan RF-00110
32. Verifikasi NF-00092 tidak tampil
33. Klik [Clear Field]
34. Klik [Apply]

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-992 s.d. 996). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-997 s.d. 1001 ada di spec 247 dan TC-FA-TAG-1002 s.d. 1004 ada di spec 248.
- Panel Filter tetap terbuka sesudah [Apply]; kasus berikutnya dimulai dari panel yang sama sesudah Filter dikosongkan.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 12, 17, 24, 33 (mengosongkan Filter lewat [Clear Field]); 13, 18, 25, 34 (menerapkan Filter kosong lewat [Apply]).
- Asersi tambahan di luar Expected TC: tidak ada.
- A-15: nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` karena asersi bergantung pada kode, urutan, dan jumlah persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Spec ini hanya membaca data itu (Test Steps tanpa aksi tulis), sehingga tidak ada efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-993 dan 996 menulis Expected dengan dua klausa (baris yang tampil; NF-00092 tidak tampil); spec memecahnya menjadi dua `Verifikasi` dan klausa absence mengikuti `Verifikasi` baris yang tampil sebagai anchor.
  - TC-FA-TAG-995 Expected "opsi pada field Reason hanya Disposal" tidak menyebut kapan daftar dibuka; spec membuka daftar sebelum memilih opsi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
