---
id: TC-FA-TAG-E2E-374-konkurensi-tag-lama-direbut-pengguna-lain-d-04-dan-perubahan-bagian-1
title: "Konkurensi: Dialog D-04 Asset TAG Has Changed Saat Tag Lama Diganti, Dilepas, atau TAG Type Berubah oleh Pelaku Lain"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1332
  - TC-FA-TAG-1333
  - TC-FA-TAG-1334
  - TC-FA-TAG-1335
coverage:
  web: automated
---

# Konkurensi: Dialog D-04 Asset TAG Has Changed Saat Tag Lama Diganti, Dilepas, atau TAG Type Berubah oleh Pelaku Lain

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup TC), password `Spectra.env.FA_TC_PASSWORD` (nama env usulan, didaftarkan tim FE di `spectra.config.ts` dan `.env.example`). Login di hook `before` spec ini; halaman Fixed Asset > TAG tab Paired dibuka hook `beforeEach` suite.
- Pelaku kedua (pengguna 'Dedi K.', proses disposal, dan admin pengubah TAG Type Asset Name; tidak ada di Pre-setup TC, disediakan tim FE) bertindak lewat sesi API aktor (lihat `suite.md`); sesi ini hanya mengubah state tanpa asersi di sesinya.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite `before`, lihat `suite.md`.
- Fixture `fixtures/fixed-asset-tag.json` belum ada; nilai literal TC pada langkah diberi kunci fixture oleh tahap script (akan disediakan).
- Kemampuan teknis (disediakan tim FE/BE): simulator reader RFID/NFC USB satu reader tersambung, driver terpasang, reader aktif, sudah disinkronkan di Global Settings > Handheld Reader (lihat `suite.md`); sesi API pelaku kedua yang mengganti Tag aset, melepas Tag lewat penyelesaian disposal, dan mengubah TAG Type Asset Name; seed dan pemulihan idempotent aset serta stok Tag lewat fixture backend.
- Data (tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis): AST-0220 'Excavator 20 Ton - 220' (Group Plant A, TAG Type Asset Name RFID) punya satu Tag RFID `RF-00130` berstatus Paired. Stok Global: Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` berstatus Available.
- Pemulihan di hook `after` (tetap jalan walau spec gagal): kembalikan AST-0220 (Tag `RF-00130` Paired), stok Tag, dan TAG Type Asset Name 'Excavator 20 Ton' ke RFID lewat fixture backend. State global: TAG Type Asset Name diubah pada langkah 24 dan dipulihkan pada langkah 30. Suite serial (`parallel: false`).

## Test Steps

### TC-FA-TAG-1332: Tag lama sudah diganti pengguna lain

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
4. Pengguna lain 'Dedi K.' mengganti Tag `RF-00130` di aset yang sama hingga penggantian tersimpan (sesi API)
5. Klik [Submit]
6. Verifikasi dialog judul "Asset TAG Has Changed", body "AST-0220 TAG was replaced by Dedi K. at [tanggal dan waktu penggantian Dedi K. dalam format General Settings].", tombol [Update Data]
7. Verifikasi tidak ada mutasi dari Submit pengguna A: Toast "Success, TAG has been replaced." tidak tampil

### TC-FA-TAG-1333: Update Data memuat ulang dialog

8. Klik [Update Data]
9. Verifikasi Dialog Replace TAG dimuat ulang dari awal untuk aset 'Excavator 20 Ton - 220' dan menampilkan Tag terbaru hasil penggantian Dedi K.
10. Verifikasi slot `Replacement TAG` kembali `Not scanned`
11. Klik `✕` pada Dialog Replace TAG
12. Pulihkan AST-0220 ke keadaan awal (Tag `RF-00130` Paired, `RF-00412` Available) lewat fixture backend

### TC-FA-TAG-1334: Tag lama dilepas oleh proses disposal

13. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
14. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
15. Tag `RF-00130` dilepas dari aset oleh proses disposal selesai hingga pelepasan tersimpan (sesi API)
16. Klik [Submit]
17. Verifikasi dialog judul "Asset TAG Has Changed", body "AST-0220 TAG has changed since this page was opened.", tombol [Update Data]
18. Verifikasi tidak ada mutasi dari Submit: Toast "Success, TAG has been replaced." tidak tampil
19. Klik [Update Data]
20. Klik `✕` pada Dialog Replace TAG
21. Pulihkan AST-0220 ke keadaan awal lewat fixture backend

### TC-FA-TAG-1335: TAG Type Asset Name berubah

22. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
23. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`
24. Admin mengubah TAG Type Asset Name 'Excavator 20 Ton' menjadi NFC di Settings > Asset Name hingga perubahan tersimpan (sesi API)
25. Klik [Submit]
26. Verifikasi dialog judul "Asset TAG Has Changed", body "AST-0220 TAG has changed since this page was opened.", tombol [Update Data]
27. Verifikasi tidak ada mutasi dari Submit: Toast "Success, TAG has been replaced." tidak tampil
28. Klik [Update Data]
29. Klik `✕` pada Dialog Replace TAG
30. Pulihkan TAG Type Asset Name 'Excavator 20 Ton' ke RFID dan AST-0220 ke keadaan awal lewat fixture backend

## Notes

- Spec konkurensi dengan pelaku kedua lewat sesi API (bukan kelas c, tidak memakai `P-2`); langkah pemicu ditulis "... hingga ... tersimpan" (R-20).
- TC-FA-TAG-1333 memakai keadaan akhir TC-FA-TAG-1332 (langkah 1 sampai 5 identik: dialog terbuka, `RF-00412` dipindai, 'Dedi K.' mengganti Tag, [Submit]); langkah itu tidak diulang. Popup Detail tetap terbuka dari langkah 1 sampai 30.
- Langkah penghubung (tanpa awalan `Verifikasi`): 1 dan 2 (membuka popup dan dialog), 11, 20, 29 (menutup dialog yang tidak dirty setelah [Update Data]), 12, 21, 30 (memulihkan state lewat fixture, S-09), 13 dan 22 (membuka kembali dialog), 19 dan 28 (menutup dialog D-04 lewat [Update Data]).
- Asersi "tidak ada mutasi" pada langkah 7, 18, 27 diamati sebagai Toast sukses penggantian tidak tampil setelah dialog D-04 tampil (dialog D-04 pada langkah 6, 17, 26 menjadi anchor positif); TC tidak memberi cara observasi lain. Langkah ini adalah tambahan observasi untuk Expected "Tidak ada mutasi" (S-03).
- Pembagian TC lintas spec: TC-FA-TAG-1336, TC-FA-TAG-1337, dan TC-FA-TAG-1338 ada di spec 375, TC-FA-TAG-1339 dan TC-FA-TAG-1351 di spec 376.
- Temuan untuk QA:
  - TC-FA-TAG-1332 sampai TC-FA-TAG-1335 berlabel Manual Only (dua sesi pengguna paralel); spec tetap ditulis dengan pelaku kedua lewat sesi API.
  - TC-FA-TAG-1332 dan TC-FA-TAG-1333 menyebut Post Condition ("Penggantian Dedi K. tidak tertimpa", "Tag `RF-00412` tetap Available", "Tidak ada mutasi dari pengguna A") tanpa langkah observasi; tidak diasersi di luar Expected.
  - TC-FA-TAG-1334 dan TC-FA-TAG-1335 menyebut pelaku kedua tanpa akun ("sesi lain", "Admin"); spec menulisnya sebagai kemampuan sesi API yang disediakan tim FE.
  - TC-FA-TAG-1332 sampai TC-FA-TAG-1335 tidak menyebut cara menutup dialog sesudah D-04; spec memakai [Update Data] lalu `✕`.
  - Nilai literal Pre-setup (Asset Name, ID aset, kode Tag) tidak bisa bersuffix `{runId}` karena asersi bergantung pada nama dan kode persis; Lampiran A belum memuat butir modul ini sehingga seeding idempotent dan pemulihan lewat fixture BE (suite serial) dicatat sebagai kebutuhan.
