---
id: TC-FA-TAG-E2E-302-sinkron-masuk-global-delete-dan-tag-lama-hasil-replace
title: "Sinkron Masuk Global: Tag Lama Hasil Replace dan Tag To Be Returned yang Dihapus di Global"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1244
  - TC-FA-TAG-1245
  - TC-FA-TAG-1246
  - TC-FA-TAG-1247
coverage:
  web: automated
---

# Sinkron Masuk Global: Tag Lama Hasil Replace dan Tag To Be Returned yang Dihapus di Global

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Total Control [TC] `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Simulator reader RFID/NFC USB (disediakan tim FE/BE, lihat `suite.md`): satu reader tersambung, driver terpasang, reader aktif, dan sudah disinkronkan di Global Settings > Handheld Reader; langkah "Pindai" memakai simulator itu sebagai langkah rutin.
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Data (Pre-setup TC, tanpa suffix) Tag To Be Returned: [RFID] `RF-00071` (Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group 'Disposal Center', Current Holder Dedi K.); [RFID] `RF-00088` ('Excavator 20 Ton - 5', 'Disposal Center', Dedi K.); [NFC] `NF-00092` ('Laptop Pro 14 - 8', 'HQ Warehouse', Rina T.).
- Data tambahan (Pre-setup TC, tanpa suffix): aset AST-0020 ('Excavator 20 Ton - 20', Plant B) dengan Tag RFID `RF-00130` Paired; Tag RFID `RF-00500` Available.
- Baseline badge tab To Be Returned dan jumlah entri Event Log dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` (S-12).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan aset AST-0020, Tag `RF-00130`, `RF-00500`, `RF-00088` (termasuk pembuatan ulang setelah dihapus), dan daftar To Be Returned ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: registri Global (Tag `RF-00088` dihapus lalu dipulihkan), status Tag. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1244: Tag lama hasil Replace langsung Available di Global dan tidak singgah di To Be Returned

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant B untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 20'
3. Pindai Tag lama `RF-00130` pada `Scan Current TAG`
4. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00500`
5. Klik [Submit]
6. Buka Fixed Asset > TAG > To Be Returned
7. Ketik Search `RF-00130`, tekan Enter
8. Verifikasi Illustration `No results found`: pencarian "RF-00130" tidak menemukan Tag di tab To Be Returned
9. Verifikasi badge tab "To Be Returned" tidak bertambah terhadap baseline

### TC-FA-TAG-1245: Tag lama RFID yang tidak dipindai langsung Damaged/Missing dan tidak singgah di To Be Returned

10. Klik `(←)` pada kotak Search, lalu pulihkan aset, Tag, dan stok lewat fixture backend dan buka Fixed Asset > TAG tab Paired
11. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant B untuk membuka Popup Detail
12. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 20'
13. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00500`
14. Klik [Submit]
15. Buka Fixed Asset > TAG > To Be Returned
16. Ketik Search `RF-00130`, tekan Enter
17. Verifikasi Illustration `No results found`: pencarian "RF-00130" tidak menemukan Tag di tab To Be Returned

### TC-FA-TAG-1246: Tag To Be Returned yang dihapus di Global keluar dari tab tanpa jejak di FAMS

18. Klik `(←)` pada kotak Search, lalu pulihkan Tag To Be Returned lewat fixture backend
19. Buka Global Settings > TAG
20. Hapus Tag `RF-00088` (status To be Returned)
21. Buka Fixed Asset > TAG > To Be Returned
22. Ketik Search `RF-00088`, tekan Enter
23. Verifikasi Illustration `No results found`: baris RF-00088 tidak ada lagi di tab To Be Returned
24. Verifikasi badge tab "To Be Returned" berkurang satu terhadap baseline
25. Klik tombol "Event Log"
26. Verifikasi Event Log tidak memuat entri untuk RF-00088

### TC-FA-TAG-1247: penghapusan satu Tag di Global tidak memengaruhi baris Tag lain

27. Tutup Modal Event Log, klik `(←)` pada kotak Search, lalu pulihkan Tag To Be Returned lewat fixture backend
28. Buka Global Settings > TAG
29. Hapus Tag `RF-00088`
30. Buka Fixed Asset > TAG > To Be Returned
31. Verifikasi baris RF-00071 dan NF-00092 tetap tampil dengan data snapshot yang sama

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 10, 18 dan 27 (mereset Search, memulihkan data lewat fixture antar TC, S-09; menutup modal).
- Absence TC-FA-TAG-1244, 1245, dan 1246: memakai empty state `No results found` hasil Search sebagai anchor positif; TC-FA-TAG-1246 b (Event Log tidak memuat entri RF-00088) didahului asersi `Verifikasi` tab To Be Returned yang menunjukkan Search selesai (bagian 8b butir 2).
- Temuan untuk QA:
  - TC-FA-TAG-1244 dan 1245 Post Condition (Tag RF-00130 berstatus Available atau Damaged/Missing di registri Global; tidak ada entri Event Log untuk RF-00130) tidak punya langkah observasi di TC; tidak diasersi.
  - TC-FA-TAG-1246 dan 1247 langkah TC ke-1 ('hapus Tag RF-00088') tidak menyebut dialog konfirmasi hapus; spec menulis satu langkah mengikuti TC.
  - TC-FA-TAG-1244 menyebut 'Scan Current TAG' sedangkan TC lain memakai ButtonScan pada baris Tag lama; spec mengikuti teks TC.
