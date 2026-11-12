---
id: TC-FA-TAG-E2E-264-seleksi-tabel-to-be-returned-select-all-selection-limit-dan-bagian-1
title: "Seleksi Tabel To Be Returned: Select All, Selection Limit, dan Reset Seleksi Setelah Receive Manually Bulk (Bagian 1)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-1371
  - TC-FA-TAG-1372
  - TC-FA-TAG-1373
  - TC-FA-TAG-1374
  - TC-FA-TAG-1375
  - TC-FA-TAG-1376
coverage:
  web: automated
---

# Seleksi Tabel To Be Returned: Select All, Selection Limit, dan Reset Seleksi Setelah Receive Manually Bulk (Bagian 1)

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD` (nama env usulan; didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite; tab `To Be Returned` dibuka pada langkah 1. Spec tidak mengganti akun; hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci `Fixture.fixedAssetTag.<kunci>` pada tabel data ditandai untuk dibuat tim FE (tahap script).
- Data Pre-setup tab To Be Returned: dataset berganti per kasus lewat fixture backend dan diatur pada langkah penghubung: TC-FA-TAG-1371 memakai 12 Tag dalam scope (kunci `Fixture.fixedAssetTag.tbr12`, dimuat hook `before`); TC-FA-TAG-1372 memakai 25 Tag (kunci `tbr25`, langkah 6); TC-FA-TAG-1373 dan 1374 memakai 8 Tag dengan Selection Limit 5 (kunci `tbr8`, langkah 13); TC-FA-TAG-1376 dan 1375 memakai tiga Tag Pre-setup: RF-00071 (RFID; Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.), RF-00088 (RFID; 'Excavator 20 Ton - 5', Disposal Center, Dedi K.), dan NF-00092 (NFC; 'Laptop Pro 14 - 8', HQ Warehouse, Rina T.) (kunci `tbr3`, langkah 23). Kode dan atribut Tag selain tiga Tag Pre-setup ditentukan seeding; TC hanya menyebut jumlahnya.
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned dalam jumlah yang dibutuhkan; pengubahan Selection Limit di Lifecycle Settings > System Limits oleh pelaku kedua lewat sesi API (nilai awal dicatat sebelum diubah); tidak ada endpoint yang dikarang di spec ini.
- Sesi API aktor: pelaku kedua (akun admin disediakan tim FE) mengubah Selection Limit dan dataset lewat login API (password) yang tidak dihitung sebagai sesi web (lihat `suite.md`), tanpa asersi di sesinya.
- State global yang diubah: Selection Limit diturunkan menjadi 5 pada langkah 13 dan dipulihkan ke nilai awal pada langkah 23; hook `after` memulihkan Selection Limit ke nilai awal dan dataset To Be Returned ke keadaan Pre-setup empat Tag lewat fixture backend, juga bila spec gagal di tengah. Suite serial mencegah spec lain membaca Selection Limit yang turun.
- TC-FA-TAG-1375 dan 1376 tidak menyebut Selection Limit; keduanya dijalankan dengan Selection Limit di nilai awal (dipulihkan pada langkah 23).
- Nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Event Log To Be Returned (Method `Manual`) (langkah 33); entri TAG Log Global `Marked Damaged/Missing` (langkah 33). Aksi lain lewat sesi API (langkah 13, 23) tidak dinyatakan PRD tag.md atau TC menimbulkan efek yang tidak terpulihkan.

## Test Steps

### TC-FA-TAG-1371: Select All dan perubahan label menjadi Unselect All

1. Klik tab `To Be Returned`
2. Klik tombol "Select All (12 records)"
3. Verifikasi seluruh 12 baris terpilih lintas halaman
4. Verifikasi Bulk Action Bar menampilkan "12 TAGs selected"
5. Verifikasi tombol berubah menjadi "Unselect All"

### TC-FA-TAG-1372: seleksi terjaga saat pindah halaman dan saat Search diubah

6. Atur dataset tab To Be Returned menjadi 25 Tag dalam scope (kunci `tbr25`) lewat fixture backend hingga tersimpan, muat ulang halaman (F5), lalu klik tab `To Be Returned`
7. Centang baris pertama halaman 1
8. Pindah ke halaman 2
9. Verifikasi Bulk Action Bar tetap menampilkan "1 TAG selected" setelah pindah halaman
10. Ketik Search `RF`, tekan Enter
11. Verifikasi Bulk Action Bar tetap menampilkan "1 TAG selected" setelah Search
12. Klik `(←)` pada kotak Search

### TC-FA-TAG-1373: seleksi manual berhenti di Selection Limit

13. Atur Selection Limit menjadi 5 di Lifecycle Settings > System Limits (pelaku kedua lewat sesi API) dan dataset tab To Be Returned menjadi 8 Tag dalam scope (kunci `tbr8`) lewat fixture backend hingga tersimpan, muat ulang halaman (F5), lalu klik tab `To Be Returned`
14. Centang baris satu per satu sampai 5 baris
15. Arahkan kursor ke checkbox baris keenam
16. Verifikasi checkbox baris keenam Disabled (tetap tampil) dengan tooltip "You've reached the maximum selection of 5 rows."
17. Verifikasi Bulk Action Bar menampilkan "5 TAGs selected"

### TC-FA-TAG-1374: Select All melebihi Selection Limit dipotong dengan toast error

18. Klik ikon `×` di sisi kanan Bulk Action Bar
19. Klik tombol "Select All (8 records)"
20. Verifikasi toast "Error, only the first 5 of 8 rows were selected. Narrow your filter to include the rest." tampil
21. Verifikasi Bulk Action Bar menampilkan "5 TAGs selected"
22. Verifikasi Bulk Action Bar tetap dapat dipakai

### TC-FA-TAG-1376: menutup dialog Receive Manually tanpa Submit tidak mereset seleksi

23. Pulihkan Selection Limit ke nilai awal (pelaku kedua lewat sesi API) dan atur dataset tab To Be Returned ke Pre-setup tiga Tag RF-00071, RF-00088, dan NF-00092 (kunci `tbr3`) lewat fixture backend hingga tersimpan, muat ulang halaman (F5), lalu klik tab `To Be Returned`
24. Centang baris RF-00071 dan RF-00088
25. Klik Bulk Action "Receive Manually"
26. Klik tombol [Cancel] pada dialog yang masih kosong
27. Verifikasi dialog menutup
28. Verifikasi Bulk Action Bar tetap menampilkan "2 TAGs selected"

### TC-FA-TAG-1375: Receive Manually Bulk sukses mereset seleksi ke 0

29. Klik ikon `×` di sisi kanan Bulk Action Bar
30. Centang baris RF-00071 dan RF-00088
31. Klik Bulk Action "Receive Manually"
32. Isi Note dengan "Tag rusak saat serah terima"
33. Klik [Submit]
34. Verifikasi Bulk Action Bar hilang
35. Verifikasi tidak ada baris tercentang pada tabel

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1371 s.d. 1376). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: TC-FA-TAG-1408 s.d. 1413 ada di spec 265 dan 266; TC-FA-TAG-1400 s.d. 1407 ada di spec 267 dan 268.
- Urutan TC di dalam spec: TC-FA-TAG-1371, 1372, 1373, 1374, 1376, lalu 1375. TC-FA-TAG-1376 (Cancel, tanpa perubahan) berada sebelum TC-FA-TAG-1375 (Submit yang mengubah status Tag) karena aksi yang mengubah data berada di akhir (S-10) dan karena RF-00071 serta RF-00088 hilang dari tab To Be Returned sesudah Submit.
- Dataset diganti lewat fixture pada langkah penghubung 6, 13, dan 23 (tiap TC memakai dataset berbeda); muat ulang halaman membuang seleksi sebelumnya.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): 1 (membuka tab); 6 (memuat dataset 25 Tag dan membuka tab); 12 (mengosongkan Search lewat `(←)`); 13 (memuat Selection Limit 5 dan dataset 8 Tag); 18, 29 (membatalkan seleksi lewat ikon `×` pada Bulk Action Bar); 23 (memulihkan Selection Limit dan memuat dataset 3 Tag).
- Asersi tambahan di luar Expected TC: tidak ada.
- A-15: nilai literal Pre-setup (kode Tag, Last Asset, Return Group, Current Holder) dipakai tanpa suffix `{runId}` karena asersi bergantung pada kode, urutan, dan jumlah persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Event Log To Be Returned (Method `Manual`) (langkah 33); entri TAG Log Global `Marked Damaged/Missing` (langkah 33). Aksi lain lewat sesi API (langkah 13, 23) tidak dinyatakan PRD tag.md atau TC menimbulkan efek yang tidak terpulihkan.
- Temuan untuk QA:
  - TC-FA-TAG-1371 s.d. 1376 memakai dataset berbeda (12, 25, 8, dan 3 Tag) tanpa menyebut kode Tag selain tiga Tag Pre-setup; spec hanya memakai jumlahnya.
  - TC-FA-TAG-1374 Expected "Bulk Action Bar tetap dapat dipakai" tidak menyebut aksi yang diverifikasi; spec mengasersi bahwa bar tampil dan aksinya tidak Disabled.
  - TC-FA-TAG-1375 tidak punya Expected toast dan tidak menyebut status akhir Tag; Post Condition tanpa langkah observasi tidak diasersi.
  - TC-FA-TAG-1373 dan 1374 tidak menyebut cara membatalkan seleksi antar kasus; spec memakai ikon `×` pada Bulk Action Bar seperti pada TC-FA-TAG-1408.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
