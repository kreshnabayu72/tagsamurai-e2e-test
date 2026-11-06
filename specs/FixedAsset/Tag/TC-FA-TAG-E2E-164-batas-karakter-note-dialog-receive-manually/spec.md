---
id: TC-FA-TAG-E2E-164-batas-karakter-note-dialog-receive-manually
title: "Batas Karakter Note Dialog Receive Manually"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-1388
  - TC-FA-TAG-1389
  - TC-FA-TAG-1390
  - TC-FA-TAG-1391
coverage:
  web: automated
---

# Batas Karakter Note Dialog Receive Manually

## Prerequisites

- Mode: FE+BE.
- Akun aktor:

| Kode | Role (teks `Role:` TC) | Email | Env password |
|---|---|---|---|
| TC | Total Control | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Akun aktor pertama: Total Control [TC]. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > TAG > Paired). Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Password tidak ditulis di spec atau fixture; nama env didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned beserta Return Group dan Current Holder, serta pemulihan Tag yang sudah diterima kembali ke To Be Returned; tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Tag To Be Returned | RFID `RF-00071` (Last Asset Excavator 20 Ton - 2, Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); RFID `RF-00088` (Excavator 20 Ton - 5, Disposal Center, Dedi K.); NFC `NF-00092` (Laptop Pro 14 - 8, HQ Warehouse, Rina T.) | `tbrDedi` |

- State yang diubah dan pemulihannya: Tag `RF-00071` diterima sebagai Damaged/Missing oleh TC-1388 dan TC-1390; langkah 28 mengembalikannya ke To Be Returned dan hook `after` memulihkan `RF-00071` ke To Be Returned.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Event Log To Be Returned (Method `Manual`) (langkah 25, 33); entri TAG Log Global `Marked Damaged/Missing` (langkah 25, 33). Aksi tulis pada langkah 6, 15 ditolak dan tidak menambah entri.

## Test Steps

1. Klik tab "To Be Returned"

### Note 361 karakter ditolak (TC-FA-TAG-1389)

2. Buka menu aksi baris RF-00071
3. Klik "Receive Manually"
4. Isi Textarea "Note" dengan teks 361 karakter (huruf `a` diulang 361 kali)
5. Verifikasi pesan error "Max. 360 characters" tampil pada Textarea "Note" langsung setelah teks diisi
6. Klik tombol [Submit]
7. Verifikasi [Submit] diblok selama error masih tampil (tidak ada toast sukses dan error "Max. 360 characters" masih tampil)
8. Verifikasi dialog "Receive Manually" tetap terbuka
9. Klik ikon close pada header dialog "Receive Manually"
10. Verifikasi dialog "Unsaved Changes" tampil dengan Body "You have unsaved changes. Are you sure you want to leave?" dan tombol [Cancel] dan [Leave]
11. Klik [Leave]

### Note hanya berisi spasi ditolak (TC-FA-TAG-1391)

12. Buka menu aksi baris RF-00071
13. Klik "Receive Manually"
14. Isi Textarea "Note" dengan lima spasi saja (tanpa karakter lain)
15. Klik tombol [Submit]
16. Verifikasi pesan error "Note must not be empty" tampil pada Textarea "Note" karena isian dihitung kosong setelah trim
17. Verifikasi dialog "Receive Manually" tetap terbuka
18. Verifikasi tidak ada toast sukses
19. Kosongkan Textarea "Note"
20. Klik ikon close pada header dialog "Receive Manually"

### Note tepat 360 karakter diterima (TC-FA-TAG-1388)

21. Buka menu aksi baris RF-00071
22. Klik "Receive Manually"
23. Isi Textarea "Note" dengan teks 360 karakter (huruf `a` diulang 360 kali)
24. Verifikasi tidak ada pesan error "Max. 360 characters" pada Textarea "Note"
25. Klik tombol [Submit]
26. Verifikasi dialog "Receive Manually" menutup
27. Verifikasi toast "Success, TAG has been received as damaged/missing." tampil

### Note 360 karakter dengan kelebihan spasi di ujung (TC-FA-TAG-1390)

28. Atur ulang data lewat fixture backend: Tag RF-00071 kembali To Be Returned hingga tersimpan, lalu muat ulang halaman dan buka tab "To Be Returned"
29. Buka menu aksi baris RF-00071
30. Klik "Receive Manually"
31. Isi Textarea "Note" dengan teks 360 karakter (huruf `a` diulang 360 kali) diikuti 10 spasi di akhir
32. Verifikasi tidak ada pesan error "Max. 360 characters" karena panjang dihitung setelah trim
33. Klik tombol [Submit]
34. Verifikasi dialog "Receive Manually" menutup
35. Verifikasi toast "Success, TAG has been received as damaged/missing." tampil

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1388 s.d. 1391). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: dialog Receive Manually (menu, bulk, validasi Note, Cancel, dan Unsaved Changes) ada di spec 135 sampai 139.
- Urutan TC di dalam spec: TC-1389, TC-1391, TC-1388, TC-1390. Validasi yang diblokir dijalankan sebelum Submit yang berhasil; `RF-00071` diatur ulang sebelum TC-1390 karena TC-1388 sudah menerimanya (langkah 28).
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 9 sampai 11 (menutup form dirty: ikon close, `Verifikasi` dialog "Unsaved Changes", [Leave]), 19 sampai 20 (memulihkan Note yang hanya berisi spasi dengan mengosongkannya lalu menutup dialog), dan 28 (mengatur ulang state Tag lewat fixture backend).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Event Log To Be Returned (Method `Manual`) (langkah 25, 33); entri TAG Log Global `Marked Damaged/Missing` (langkah 25, 33). Aksi tulis pada langkah 6, 15 ditolak dan tidak menambah entri.
- Temuan untuk QA:
  - Panjang teks dihitung setelah trim sesuai Expected TC; nilai 360 dan 361 karakter ditulis tepat sebagai huruf `a` yang diulang tanpa suffix karena asersi bergantung pada panjang persis.
  - Pembukaan tab "To Be Returned" pada langkah 1 bukan dari langkah TC (TC menulis "Buka Fixed Asset > TAG > To Be Returned"); hook suite `beforeEach` membuka Fixed Asset > TAG tab Paired sehingga spec berpindah ke tab itu.
  - Post Condition TC-FA-TAG-1388 s.d. 1391 (status Tag RF-00071, entri TAG Log "Marked Damaged/Missing", Event Log) tanpa langkah observasi di TC tidak diasersi.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
