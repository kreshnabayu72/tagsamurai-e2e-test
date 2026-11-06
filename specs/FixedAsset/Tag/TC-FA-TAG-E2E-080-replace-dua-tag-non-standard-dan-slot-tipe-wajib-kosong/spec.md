---
id: TC-FA-TAG-E2E-080-replace-dua-tag-non-standard-dan-slot-tipe-wajib-kosong
title: "Replace: Dua Tag Non-standard dengan Satu atau Dua Tipe Wajib Kosong, Slot Mengikuti Urutan TAG Type Asset Name"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1478
  - TC-FA-TAG-1479
coverage:
  web: automated
---

# Replace: Dua Tag Non-standard dengan Satu atau Dua Tipe Wajib Kosong, Slot Mengikuti Urutan TAG Type Asset Name

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB yang memindai kode Tag (satu reader tersambung, driver terpasang, aktif, dan sudah disinkronkan di Global Settings > Handheld Reader); seed dan pemulihan idempotent lewat fixture backend untuk aset, atribut aset, Tag per status registri, stok Tag, dan laporan Tag; pembacaan status registri Tag dan state backend lewat fixture BE (dipakai hanya untuk butir Expected TC).
- Data: aset 'Excavator 20 Ton - 72' (AST-0072, Group Plant A, TAG Type Asset Name RFID) dengan dua Tag NFC Paired `NF-00090` dan `NF-00091` (keduanya Non-standard); 'Excavator 20 Ton - 73' (AST-0073, TAG Type Asset Name RFID dan NFC) dengan dua Tag QR Paired `QR-00240` dan `QR-00241` (keduanya Non-standard); Tag RFID `RF-00420` dan `RF-00412` serta Tag NFC `NF-00500` Available (stok Global).
- Pembacaan Modal Changelog: entri Changelog Paired TAG dibaca lewat tombol `Changelog` di toolbar tab Paired; jumlah entri tidak diasersi sebagai angka absolut. Kemampuan teknis (disediakan tim FE/BE): pembacaan jumlah entri Changelog Paired TAG sebelum aksi (audit trail permanen; N tidak dapat diturunkan dari seeding, bagian 8b butir 10); baseline dicatat ulang sebelum aksi pemicu tiap TC (S-12, butir A-18).
- Fixture: `Fixture.fixedAssetTag` belum ada (disediakan tim FE); nilai data pada langkah dibaca dari TC dan dipetakan ke fixture itu oleh tahap script.
- State global: stok Tag per tipe di registri Global dan status Tag (Paired, Available, Damaged/Missing, keluar dari registri) diubah oleh aksi Replace; fixture backend memulihkannya di hook `before`, di langkah penghubung antar-TC, dan di hook `after` yang tetap jalan walau spec gagal di tengah. Suite berjalan serial (`parallel: false`).
- Nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 10, 29); entri TAG Log Global (langkah 10, 29).

## Test Steps

### TC-FA-TAG-1478: Replace dua Tag Non-standard dengan satu tipe wajib kosong: satu slot, Tag lama tanpa pasangan dilepas

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 72'
3. Centang baris `NF-00090` dan baris `NF-00091`
4. Klik ButtonScan `Scan NFC` pada baris `NF-00090`
5. Pindai Tag `NF-00090` dengan reader
6. Verifikasi bagian `Replacement TAG` hanya memuat satu slot `RFID TAG`
7. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
8. Pindai Tag `RF-00420` dengan reader
9. Catat jumlah entri Changelog Paired TAG lewat kemampuan baca sebagai N1
10. Klik [Submit]
11. Verifikasi Submit sukses: (baca lewat fixture BE) Tag `RF-00420` Paired pada 'Excavator 20 Ton - 72'
12. Verifikasi (baca lewat fixture BE) Tag `NF-00090` berstatus Available di registri Global
13. Verifikasi (baca lewat fixture BE) Tag `NF-00091` berstatus Damaged/Missing di registri Global
14. Tutup Popup Detail Assets
15. Klik tombol `Changelog` di toolbar tab Paired
16. Verifikasi jumlah entri Modal Changelog bertambah dua terhadap N1 (dibaca lewat kemampuan baca yang sama)
17. Verifikasi dua baris teratas Modal Changelog (urutan default Date terbaru) memuat baris dengan Old `[NFC] NF-00090` dan New `[RFID] RF-00420`
18. Verifikasi dua baris teratas Modal Changelog memuat baris dengan Old `[NFC] NF-00091` dan New `—`
19. Tutup Modal Changelog

### TC-FA-TAG-1479: Replace dua Tag Non-standard dengan dua tipe wajib kosong: dua slot mengikuti urutan TAG Type Asset Name

20. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
21. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 73'
22. Centang baris `QR-00240` dan baris `QR-00241`
23. Verifikasi bagian `Replacement TAG` memuat tepat dua slot berurutan: `RFID TAG` lalu `NFC TAG`
24. Klik ButtonScan `Scan RFID` pada slot `RFID TAG`
25. Pindai Tag `RF-00412` dengan reader
26. Klik ButtonScan `Scan NFC` pada slot `NFC TAG`
27. Pindai Tag `NF-00500` dengan reader
28. Catat jumlah entri Changelog Paired TAG lewat kemampuan baca sebagai N2
29. Klik [Submit]
30. Verifikasi Submit sukses: (baca lewat fixture BE) Tag `RF-00412` dan `NF-00500` Paired pada 'Excavator 20 Ton - 73'
31. Tutup Popup Detail Assets
32. Klik tombol `Changelog` di toolbar tab Paired
33. Verifikasi jumlah entri Modal Changelog bertambah dua terhadap N2 (dibaca lewat kemampuan baca yang sama)
34. Verifikasi dua baris teratas Modal Changelog memuat baris dengan Old `[QR] QR-00240` dan New `[RFID] RF-00412`
35. Verifikasi dua baris teratas Modal Changelog memuat baris dengan Old `[QR] QR-00241` dan New `[NFC] NF-00500`
36. Tutup Modal Changelog

## Notes

- Langkah penghubung (S-03): Popup Detail Assets ditutup sebelum membuka Modal Changelog dan Modal Changelog ditutup sesudah dibaca; langkah 9 dan 28 mencatat baseline jumlah entri Changelog (S-12); TC-FA-TAG-1483 (satu Tag Non-standard) ada di spec 084.
- Pembagian TC lintas spec: TC-FA-TAG-1483 ada di spec 084.
- Modal Changelog dibaca pada baris teratas urutan default Date terbaru sesudah selisih jumlah dari baseline dibuktikan; kedua entri baru jatuh pada menit yang sama, sehingga spec mengasersi himpunan dua baris teratas tanpa mengandalkan urutan di antaranya (S-14, butir A-18). Baseline dicatat ulang sebelum aksi pemicu tiap TC (langkah 9 dan 28).
- Alasan di atas sekitar 35 langkah (36 langkah): kedua TC satu topik (Replace dua Tag Non-standard) dengan dataset dan kelas yang sama; tambahan empat langkah berasal dari baseline dan selisih Changelog (S-12), dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Data literal Pre-setup (kode aset AST-*, Asset Name, kode Tag) dipakai persis seperti di TC tanpa suffix `{runId}`, karena asersi bergantung pada nama dan kode itu; seeding idempotent dan pemulihan dijamin fixture backend (suite.md).
- A-15: nilai literal Pre-setup (nama aset, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nilai persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 10, 29); entri TAG Log Global (langkah 10, 29).
- Temuan untuk QA:
  - TC tidak menyatakan apakah Popup Detail Assets tetap terbuka di bawah Dialog Replace TAG sesudah dialog ditutup; spec menganggapnya tetap terbuka dan menutupnya lewat langkah penghubung hanya saat berganti Asset Name.
  - Tag lama TC-FA-TAG-1479 'dipindai' tidak disebut: kedua Tag QR tidak dipindai di overlay (jalur row action); spec mengikuti langkah TC.
  - Tag QR lama di TC-FA-TAG-1479 'keluar dari registri' hanya disebut di Post Condition tanpa langkah observasi dan tidak diasersi.
  - Asersi urutan baris Modal Changelog tidak dinyatakan TC; spec hanya mengasersi keberadaan kedua baris (S-14).
