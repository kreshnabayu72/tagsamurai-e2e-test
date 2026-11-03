---
id: TC-FA-TAG-E2E-340-resilience-receive-tag-dan-receive-manually-gagal-timeout-dan-bagian-2
title: "Resilience: Receive Manually dan Bulk Receive Manually Gagal (5xx, Layanan Global Tidak Terjangkau) Mempertahankan Dialog dan Seleksi (Bagian 2)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-583
  - TC-FA-TAG-584
  - TC-FA-TAG-585
coverage:
  web: automated
---

# Resilience: Receive Manually dan Bulk Receive Manually Gagal (5xx, Layanan Global Tidak Terjangkau) Mempertahankan Dialog dan Seleksi (Bagian 2)

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) `Spectra.intercept` parsial atas request Receive Manually (satu Tag dan bulk): respons 5xx; hook `after` melepas semua intercept; (2) layanan Global (registri Tag) dibuat tidak terjangkau dan dipulihkan lewat kemampuan fixture BE; hook `after` memulihkannya; (3) seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned; (4) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog dirty terbuka), dipakai untuk menutup dialog Receive Manually lewat muat ulang halaman. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Tag To Be Returned | [RFID] RF-00071 (Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 ('Excavator 20 Ton - 5', Disposal Center, Dedi K.); [NFC] NF-00092 ('Laptop Pro 14 - 8', HQ Warehouse, Rina T.) | `tbr` |
| Note | Tag rusak saat serah terima | `noteReceiveManually` |

- State yang diubah dan pemulihannya: layanan Global dibuat tidak terjangkau di langkah 25 dan dipulihkan di langkah 31; semua intercept dilepas di langkah 8 dan 21. Tag tidak berubah status oleh spec ini (semua commit gagal). Hook `after` memulihkan layanan Global, melepas intercept, dan memulihkan Tag ke To Be Returned lewat fixture backend walau spec gagal di tengah.

## Test Steps

### TC-FA-TAG-583: Receive Manually gagal 5xx

1. Buka tab To Be Returned lalu buka menu aksi baris RF-00071
2. Klik "Receive Manually"
3. Isi Textarea "Note" dengan "Tag rusak saat serah terima"
4. Pasang intercept 5xx pada request Receive Manually
5. Klik tombol [Submit]
6. Verifikasi Toast "Error, failed to receive TAG." tampil
7. Verifikasi dialog "Receive Manually" tetap terbuka
8. Lepas intercept
9. Muat ulang halaman (F5)

### TC-FA-TAG-584: Bulk Receive Manually gagal 5xx

10. Buka tab To Be Returned lalu centang baris RF-00071 dan RF-00088
11. Klik Bulk Action "Receive Manually"
12. Isi Textarea "Note" dengan "Tag rusak saat serah terima"
13. Pasang intercept 5xx pada request Receive Manually
14. Klik tombol [Submit]
15. Verifikasi Toast "Error, failed to receive TAG." tampil
16. Verifikasi dialog tetap terbuka
17. Klik tombol [Cancel]
18. Verifikasi dialog "Unsaved Changes" tampil
19. Klik [Leave]
20. Verifikasi Bulk Action Bar tetap tampil dengan "2 TAGs selected"
21. Lepas intercept
22. Muat ulang halaman (F5)

### TC-FA-TAG-585: Layanan Global tidak terjangkau saat Receive Manually

23. Buka tab To Be Returned lalu buka menu aksi baris RF-00071
24. Klik "Receive Manually"
25. Jadikan layanan Global (registri Tag) tidak terjangkau lewat fixture BE hingga tersimpan
26. Isi Textarea "Note" dengan "Tag rusak saat serah terima"
27. Klik tombol [Submit]
28. Verifikasi Toast "Error, failed to receive TAG." tampil
29. Verifikasi dialog tetap terbuka
30. Muat ulang halaman (F5)
31. Pulihkan layanan Global lewat fixture BE hingga tersimpan

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-583 s.d. 585). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: Receive TAG gagal (TC-FA-TAG-563 s.d. 565) ada di spec 339. Submit Receive Manually ditekan beruntun (TC-FA-TAG-587) ada di spec 342.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 8, 21 (melepas intercept), 9, 22, 30 (muat ulang halaman untuk menutup dialog yang berisi isian dan membersihkan seleksi; dialog `beforeunload` ditangani sesuai Prerequisites), 10 dan 23 (membuka tab To Be Returned sesudah muat ulang halaman), 25 (kondisi layanan Global dipasang sesudah dialog dibuka agar dialog terbuka normal; precondition TC menyebutnya tanpa urutan), 31 (memulihkan layanan Global).
- Langkah 20 (Bulk Action Bar tetap tampil) diasersi sesudah dialog ditutup lewat [Cancel] dan [Leave], sesuai Expected butir b TC-FA-TAG-584.
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-583 dan TC-FA-TAG-585 ("Tag RF-00071 tetap To Be Returned ...; tidak ada entri Event Log maupun TAG Log") tanpa langkah observasi di TC tidak diasersi.
  - TC-FA-TAG-585 menyebut layanan Global tidak terjangkau sebagai precondition tanpa urutan terhadap pembukaan dialog; spec memasangnya setelah dialog terbuka (langkah 25), sedangkan TC-FA-TAG-565 di spec 339 memasangnya sebelum pemindaian. Kedua urutan mengikuti kalimat precondition masing-masing TC; QA diminta menegaskan urutan yang dimaksud.
  - Nama dan kode literal Pre-setup (kode Tag RF-*, NF-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
