---
id: TC-FA-TAG-E2E-265-seleksi-tabel-to-be-returned-select-all-selection-limit-dan-bagian-2
title: "Seleksi Tabel To Be Returned: Ikon x, Unselect All, serta Filter dan Sort Tidak Mereset Seleksi (Bagian 2)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-1408
  - TC-FA-TAG-1409
  - TC-FA-TAG-1410
  - TC-FA-TAG-1411
coverage:
  web: automated
---

# Seleksi Tabel To Be Returned: Ikon x, Unselect All, serta Filter dan Sort Tidak Mereset Seleksi (Bagian 2)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env usulan; didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite; tab `To Be Returned` dibuka pada langkah 1. Spec tidak mengganti akun; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci `Fixture.fixedAssetTag.<kunci>` pada tabel data ditandai untuk dibuat tim FE (tahap script).
- Data Pre-setup tab To Be Returned: dataset berganti per kasus lewat fixture backend dan diatur pada langkah penghubung: TC-FA-TAG-1408 memakai 25 Tag dalam scope (kunci `Fixture.fixedAssetTag.tbr25`, dimuat hook `before`); TC-FA-TAG-1409 memakai 12 Tag (kunci `tbr12`, langkah 13); TC-FA-TAG-1410 dan 1411 memakai tiga Tag Pre-setup: RF-00071 (RFID; Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.), RF-00088 (RFID; 'Excavator 20 Ton - 5', Disposal Center, Dedi K.), dan NF-00092 (NFC; 'Laptop Pro 14 - 8', HQ Warehouse, Rina T.) (kunci `tbr3`, langkah 20). Kode dan atribut Tag selain tiga Tag Pre-setup ditentukan seeding; TC hanya menyebut jumlahnya.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned (kode, Last Asset, Reason, Return Group, Current Holder, Since) dan Return Group; tidak ada endpoint yang dikarang di spec ini.
- Pemulihan di hook `after`: dataset To Be Returned dikembalikan ke keadaan Pre-setup empat Tag lewat fixture backend bila seeding mengubahnya. Spec ini tidak mengubah Selection Limit.
- Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 13, 20) yang menyiapkan atau memulihkan state.

## Test Steps

### TC-FA-TAG-1408: ikon x pada Bulk Action Bar membatalkan seleksi lintas halaman

1. Klik tab `To Be Returned`
2. Centang baris pertama halaman 1
3. Pindah ke halaman 2
4. Centang baris pertama halaman 2
5. Verifikasi Bulk Action Bar menampilkan jumlah terpilih 2
6. Klik ikon `×` di sisi kanan Bulk Action Bar
7. Verifikasi Bulk Action Bar tertutup
8. Verifikasi seleksi kembali 0
9. Kembali ke halaman 1
10. Verifikasi tidak ada baris tercentang di halaman 1
11. Pindah ke halaman 2
12. Verifikasi tidak ada baris tercentang di halaman 2

### TC-FA-TAG-1409: Unselect All membatalkan seluruh seleksi dan menutup Bulk Action Bar

13. Atur dataset tab To Be Returned menjadi 12 Tag dalam scope (kunci `tbr12`) lewat fixture backend hingga tersimpan, muat ulang halaman (F5), lalu klik tab `To Be Returned`
14. Klik tombol "Select All (12 records)"
15. Verifikasi seluruh 12 baris terpilih
16. Verifikasi tombol berlabel "Unselect All"
17. Klik tombol "Unselect All"
18. Verifikasi Bulk Action Bar tertutup
19. Verifikasi tidak ada baris tercentang

### TC-FA-TAG-1410: perubahan Filter tidak mereset seleksi

20. Atur dataset tab To Be Returned ke Pre-setup tiga Tag RF-00071, RF-00088, dan NF-00092 (kunci `tbr3`) lewat fixture backend hingga tersimpan, muat ulang halaman (F5), lalu klik tab `To Be Returned`
21. Centang RF-00071, RF-00088, dan NF-00092
22. Buka Filter Panel
23. Pilih TAG Type NFC
24. Klik [Apply]
25. Verifikasi tabel hanya menampilkan baris NF-00092
26. Verifikasi Bulk Action Bar tetap menampilkan "3 TAGs selected"
27. Klik [Clear Field]
28. Klik [Apply]

### TC-FA-TAG-1411: perubahan sort tidak mereset seleksi

29. Klik ikon `×` di sisi kanan Bulk Action Bar
30. Centang RF-00071 dan RF-00088
31. Klik header kolom TAG Code untuk mengubah sort
32. Verifikasi baris RF-00071 dan RF-00088 tetap tercentang
33. Verifikasi Bulk Action Bar tetap menampilkan "2 TAGs selected"

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1408 s.d. 1411). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-1371 s.d. 1376 ada di spec 264; TC-FA-TAG-1412 dan 1413 ada di spec 266; TC-FA-TAG-1400 s.d. 1407 ada di spec 267 dan 268.
- Dataset diganti lewat fixture pada langkah penghubung 13 dan 20 (tiap TC memakai dataset berbeda); muat ulang halaman membuang seleksi sebelumnya.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 11 (memeriksa halaman 2); 13 (memuat dataset 12 Tag dan membuka tab); 20 (memuat dataset 3 Tag dan membuka tab); 27 (mengosongkan Filter lewat [Clear Field]); 28 (menerapkan Filter kosong lewat [Apply]); 29 (membatalkan seleksi sisa TC-FA-TAG-1410).
- Asersi tambahan di luar Expected TC: tidak ada.
- A-15: nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` karena asersi bergantung pada kode, urutan, dan jumlah persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi bisnis TAG (Replace, Pair, Report, Decline, Cancel Report, Receive, Print QR) dan hanya mengubah data lewat fixture backend (langkah 13, 20) yang menyiapkan atau memulihkan state.
- Temuan untuk QA:
  - TC-FA-TAG-1408 langkah 5 hanya menyebut "Kembali ke halaman 1" sedangkan Expected c meminta halaman 2 juga; spec menambah pindah ke halaman 2 sebagai langkah penghubung sebelum `Verifikasi` halaman 2.
  - TC-FA-TAG-1410 dan 1411 memakai precondition yang sama, tetapi 1410 meninggalkan tiga baris tercentang; spec menambah langkah penghubung pembatalan seleksi sebelum TC-FA-TAG-1411.
  - TC-FA-TAG-1408 s.d. 1411 tidak menyebut kode Tag selain tiga Tag Pre-setup; spec hanya memakai jumlahnya.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
