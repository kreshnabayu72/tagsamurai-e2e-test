---
id: TC-FA-TAG-E2E-280-pencatatan-receive-event-log-tag-log-global-dan-assigned-paired-bagian-2
title: "Pencatatan Receive: TAG Log Global untuk Receive Manually dan Receive Manually Bulk, Bagian 2"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-1108
  - TC-FA-TAG-1109
coverage:
  web: automated
---

# Pencatatan Receive: TAG Log Global untuk Receive Manually dan Receive Manually Bulk, Bagian 2

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor pertama: Manage asset & TAG dengan Update di group Disposal Center [UP_DC] `manageAssetTagDenganUpdateDiGroupDisposalCenter_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TAG_UP_DC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`).
- Login di hook `before` spec ini sebagai akun aktor pertama; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (kunci disediakan).
- Seed dan pemulihan idempotent lewat fixture backend (disediakan tim FE/BE, lihat `suite.md`): aset, Tag per status registri, stok Tag per tipe, laporan Tag, dan entri log.
- Data (Pre-setup TC, tanpa suffix) Tag To Be Returned: [RFID] `RF-00071` (Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group 'Disposal Center', Current Holder Dedi K.); [RFID] `RF-00088` ('Excavator 20 Ton - 5', 'Disposal Center', Dedi K.); [NFC] `NF-00092` ('Laptop Pro 14 - 8', 'HQ Warehouse', Rina T.).
- Nama tampil akun aktor tidak tertulis di Pre-setup TC; kolom "Received By" dan Modified By diasersi dengan nama tampil akun aktor yang dibaca fixture (format [First Name] [Last Initial], R-14).
- Baseline jumlah entri TAG Log Tag yang diamati dibaca lewat kemampuan baca (disediakan tim FE/BE) di hook `before` sebelum aksi pemicu pertama; asersi entri baru memakai selisih terhadap baseline dan kunci pencarian Name/Action/Field (S-12, S-14).
- Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan Tag To Be Returned `RF-00071`, `RF-00088`, `NF-00092`, status Tag di registri Global, aset, dan laporan ke keadaan awal lewat fixture backend.
- State global yang diubah spec ini: status Tag di registri Global dan daftar To Be Returned. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1108: Receive Manually menulis TAG Log Global "Marked Damaged/Missing"

1. Buka tab To Be Returned
2. Buka menu aksi baris RF-00071
3. Klik "Receive Manually"
4. Isi Textarea "Note" dengan "Tag rusak saat serah terima"
5. Klik tombol [Submit]
6. Buka Global Settings > TAG
7. Ketik Search `RF-00071`, tekan Enter
8. Buka Popup TAG Log Tag `RF-00071`
9. Verifikasi entri baru bertitle "TAG Marked Damaged/Missing by [PIC]" dengan PIC pelaku Receive Manually
10. Verifikasi entri memuat Previous Status "To be Returned" dan Note "Tag rusak saat serah terima"

### TC-FA-TAG-1109: Receive Manually Bulk menulis satu entri TAG Log per Tag dengan Note yang sama

11. Pulihkan Tag To Be Returned lewat fixture backend, lalu buka Fixed Asset > TAG tab To Be Returned
12. Centang baris RF-00071 dan RF-00088
13. Klik Bulk Action "Receive Manually"
14. Isi Textarea "Note" dengan "Tag rusak saat serah terima"
15. Klik tombol [Submit]
16. Buka Global Settings > TAG
17. Ketik Search `RF-00071`, tekan Enter
18. Buka Popup TAG Log Tag `RF-00071`
19. Verifikasi Tag `RF-00071` memuat tepat satu entri "Marked Damaged/Missing" dengan Note "Tag rusak saat serah terima"
20. Tutup Popup TAG Log, lalu ganti isi kotak Search dengan `RF-00088`, tekan Enter
21. Buka Popup TAG Log Tag `RF-00088`
22. Verifikasi Tag `RF-00088` memuat tepat satu entri "Marked Damaged/Missing" dengan Note "Tag rusak saat serah terima"

## Notes

- Mode: FE+BE.
- Langkah penghubung (S-03): 7, 11, 17 dan 20 (memulihkan Tag To Be Returned lewat fixture, mencari baris target di registri lewat Search, menutup popup, R-16).
- TC-FA-TAG-1111 dan TC-FA-TAG-1112 ada di spec 304.
- Temuan untuk QA:
  - TC-FA-TAG-1108 dan 1109 menulis title "TAG Marked Damaged/Missing by [PIC]" dengan placeholder [PIC]; spec mengasersi PIC sebagai nama pelaku Receive Manually.
  - TC-FA-TAG-1109 tidak menyebut baseline entri TAG Log; spec memakai jumlah entri "Marked Damaged/Missing" Tag itu dan Note (S-12).
