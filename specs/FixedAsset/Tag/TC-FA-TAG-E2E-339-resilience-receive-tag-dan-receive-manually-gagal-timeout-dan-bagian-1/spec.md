---
id: TC-FA-TAG-E2E-339-resilience-receive-tag-dan-receive-manually-gagal-timeout-dan-bagian-1
title: "Resilience: Receive TAG Gagal (5xx, Timeout, Layanan Global Tidak Terjangkau) Mempertahankan Dialog dan Daftar Sesi (Bagian 1)"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-563
  - TC-FA-TAG-564
  - TC-FA-TAG-565
coverage:
  web: automated
---

# Resilience: Receive TAG Gagal (5xx, Timeout, Layanan Global Tidak Terjangkau) Mempertahankan Dialog dan Daftar Sesi (Bagian 1)

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di dialog Receive TAG; (2) `Spectra.intercept` parsial atas request commit Receive: respons 5xx dan tidak ada respons sampai timeout; hook `after` melepas semua intercept; (3) layanan Global (registri Tag) dibuat tidak terjangkau dan dipulihkan lewat kemampuan fixture BE; hook `after` memulihkannya; (4) seed dan pemulihan idempotent lewat fixture backend untuk Tag To Be Returned; (5) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog terbuka), dipakai untuk menutup dialog Receive TAG lewat muat ulang halaman. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Tag To Be Returned | [RFID] RF-00071 (Last Asset 'Excavator 20 Ton - 2', Reason Disposal, Return Group Disposal Center, Current Holder Dedi K.); [RFID] RF-00088 ('Excavator 20 Ton - 5', Disposal Center, Dedi K.); [NFC] NF-00092 ('Laptop Pro 14 - 8', HQ Warehouse, Rina T.) | `tbr` |

- State yang diubah dan pemulihannya: layanan Global dibuat tidak terjangkau di langkah 19 dan dipulihkan di langkah 26; semua intercept dilepas di langkah 9 dan 17. Tag `RF-00071` dan `RF-00088` tidak berubah status oleh spec ini (semua commit gagal). Hook `after` memulihkan layanan Global, melepas intercept, dan memulihkan Tag ke To Be Returned lewat fixture backend walau spec gagal di tengah.

## Test Steps

### TC-FA-TAG-563: Receive gagal 5xx

1. Buka tab To Be Returned lalu klik tombol "Receive TAG"
2. Pindai Tag RF-00071
3. Pindai Tag RF-00088
4. Pasang intercept 5xx pada request commit Receive
5. Klik tombol [Receive]
6. Verifikasi Toast "Error, failed to receive TAG." tampil
7. Verifikasi dialog "Receive TAG" tetap terbuka dengan daftar sesi utuh berisi RF-00071 dan RF-00088
8. Verifikasi penghitung "2 TAGs scanned"
9. Lepas intercept
10. Muat ulang halaman (F5)

### TC-FA-TAG-564: Receive timeout

11. Buka tab To Be Returned lalu klik tombol "Receive TAG"
12. Pindai Tag RF-00071
13. Pasang intercept: server tidak merespons sampai melewati batas timeout pada request commit Receive
14. Klik tombol [Receive]
15. Verifikasi Toast "Error, failed to receive TAG." tampil
16. Verifikasi dialog "Receive TAG" tetap terbuka dengan daftar sesi berisi RF-00071
17. Lepas intercept
18. Muat ulang halaman (F5)

### TC-FA-TAG-565: Layanan Global tidak terjangkau saat Receive

19. Jadikan layanan Global (registri Tag) tidak terjangkau lewat fixture BE hingga tersimpan
20. Buka tab To Be Returned lalu klik tombol "Receive TAG"
21. Pindai Tag RF-00071
22. Klik tombol [Receive]
23. Verifikasi Toast "Error, failed to receive TAG." tampil
24. Verifikasi dialog "Receive TAG" tetap terbuka
25. Muat ulang halaman (F5)
26. Pulihkan layanan Global lewat fixture BE hingga tersimpan

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-563 s.d. 565). Tidak ada TC hanya-BE.
- Pembagian TC lintas spec: Receive Manually gagal (TC-FA-TAG-583 s.d. 585) ada di spec 340. Receive TAG ditekan beruntun (TC-FA-TAG-566) ada di spec 342.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 9, 17 (melepas intercept), 10, 18, 25 (muat ulang halaman untuk menutup dialog Receive TAG yang berisi daftar sesi; dialog `beforeunload` ditangani sesuai Prerequisites), 1, 11, 20 (membuka tab To Be Returned sesudah muat ulang halaman), 26 (memulihkan layanan Global).
- Tag RF-00071 dan RF-00088 tetap To Be Returned sepanjang spec karena semua commit gagal, sehingga spec tidak membutuhkan pemulihan antar-TC.
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-563 ("Tag RF-00071 dan RF-00088 tetap To Be Returned; tidak ada entri Event Log baru"), TC-FA-TAG-565 ("Tag RF-00071 tetap To Be Returned di FAMS dan Global; tidak ada entri Event Log maupun TAG Log") tanpa langkah observasi di TC tidak diasersi.
  - TC-FA-TAG-565 menyebut layanan Global tidak terjangkau sebagai precondition; bila pemindaian Tag di dialog Receive TAG juga memanggil layanan Global, pemindaian di langkah 21 dapat gagal sebelum [Receive]. TC tidak menyebut urutannya; spec memasang kondisi itu sebelum pemindaian sesuai precondition.
  - Nama dan kode literal Pre-setup (Asset Name, kode Tag RF-*, NF-*) dipakai tanpa suffix `{runId}` sesuai rancangan TC karena asersi bergantung pada nama persis; Lampiran A belum memuat butir modul ini. Seeding idempotent dan pemulihan lewat fixture backend.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
