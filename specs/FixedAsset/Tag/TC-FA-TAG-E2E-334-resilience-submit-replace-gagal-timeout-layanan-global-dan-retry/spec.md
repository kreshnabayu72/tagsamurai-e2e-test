---
id: TC-FA-TAG-E2E-334-resilience-submit-replace-gagal-timeout-layanan-global-dan-retry
title: "Resilience: Submit Replace Gagal (5xx, Timeout, Layanan Global Tidak Terjangkau) dan Retry Berhasil"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-FA-TAG-1340
  - TC-FA-TAG-1341
  - TC-FA-TAG-1342
  - TC-FA-TAG-1343
coverage:
  web: automated
---

# Resilience: Submit Replace Gagal (5xx, Timeout, Layanan Global Tidak Terjangkau) dan Retry Berhasil

## Prerequisites

- Mode: FE+BE (intercept parsial di atas backend nyata).
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`).
- Kemampuan teknis (disediakan tim FE/BE): (1) simulator reader RFID/NFC USB (satu reader tersambung, driver terpasang, aktif, sudah disinkronkan di Global Settings > Handheld Reader) yang memindai kode Tag di ButtonScan; (2) `Spectra.intercept` parsial atas Submit Replace: respons 5xx, tidak ada respons sampai timeout, layanan Global (registri Tag) tidak terjangkau, dan 5xx hanya pada percobaan pertama lalu normal; mengganti jenis intercept tanpa menutup dialog; hook `after` melepas semua intercept; (3) seed dan pemulihan idempotent lewat fixture backend untuk aset, Tag per status registri, dan stok Global. Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset Replace | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan satu Tag RFID `RF-00330` Paired | `aset220` |
| Stok Available | Tag RFID `RF-00412`, `RF-00415`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |

- State yang diubah dan pemulihannya: langkah 25 menyimpan penggantian `RF-00330` menjadi `RF-00412` pada AST-0220; hook `after` memulihkan AST-0220 ke `RF-00330` Paired, `RF-00412` ke Available, entri Changelog dan TAG Log hasil penggantian, serta melepas semua intercept.
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 25); entri TAG Log Global (langkah 25). Aksi tulis pada langkah 5, 12, 17, 22 ditolak dan tidak menambah entri.

## Test Steps

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Klik row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
3. Klik ButtonScan `Scan RFID` pada slot `RFID TAG` lalu pindai Tag `RF-00412`

### TC-FA-TAG-1340: Submit Replace gagal 5xx

4. Pasang intercept 5xx pada Submit Replace
5. Klik [Submit]
6. Verifikasi toast "Error, failed to replace TAG."
7. Verifikasi Dialog Replace TAG tetap terbuka dengan slot `RFID TAG` tetap menampilkan `RF-00412` dan badge `Verified`
8. Verifikasi tombol [Submit] kembali dapat ditekan (loading berhenti)
9. Verifikasi user tetap di tab Paired

### TC-FA-TAG-1341: Submit Replace timeout

10. Ganti intercept: server tidak merespons Submit Replace sampai timeout
11. Tunggu toast lama hilang otomatis
12. Klik [Submit]
13. Verifikasi toast "Error, failed to replace TAG."
14. Verifikasi Dialog Replace TAG tetap terbuka

### TC-FA-TAG-1343: Layanan Global tidak terjangkau

15. Ganti intercept: layanan Global (registri Tag) tidak terjangkau saat Submit
16. Tunggu toast lama hilang otomatis
17. Klik [Submit]
18. Verifikasi toast "Error, failed to replace TAG."
19. Verifikasi Dialog Replace TAG tetap terbuka

### TC-FA-TAG-1342: Retry Submit Replace berhasil

20. Ganti intercept: Submit Replace gagal 5xx pada percobaan pertama dan normal sesudahnya
21. Tunggu toast lama hilang otomatis
22. Klik [Submit]
23. Verifikasi toast "Error, failed to replace TAG."
24. Tunggu toast lama hilang otomatis
25. Klik [Submit] lagi
26. Verifikasi toast "Success, TAG has been replaced."
27. Verifikasi dialog menutup

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-1340 s.d. 1343). Tidak ada TC hanya-BE.
- Urutan TC di dalam spec: TC-1340, TC-1341, TC-1343, lalu TC-1342, karena TC-1342 berakhir dengan Submit yang berhasil dan menutup dialog, sedangkan ketiga TC lain mensyaratkan dialog tetap terbuka dengan slot `RFID TAG` terisi `RF-00412`. TC-1341 dan TC-1343 memakai dialog yang masih terbuka dari TC sebelumnya (Tag `RF-00412` sudah terpindai di langkah 3) dan hanya mengganti jenis intercept; tidak ada pembukaan ulang dialog di antara TC.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 10, 15, dan 20 (mengganti jenis intercept), 11, 16, 21, dan 24 (menunggu toast lama hilang agar toast berikutnya adalah toast baru, R-12).
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: entri Changelog `Replace` per aset (langkah 25); entri TAG Log Global (langkah 25). Aksi tulis pada langkah 5, 12, 17, 22 ditolak dan tidak menambah entri.
- Temuan untuk QA:
  - Post Condition TC-FA-TAG-1340 s.d. 1343 (Tag `RF-00330` tetap Paired, `RF-00412` tetap Available atau Paired, entri Changelog dan TAG Log) tanpa langkah observasi di TC tidak diasersi. Judul TC-FA-TAG-1343 ("tanpa mutasi sebagian") tidak punya langkah observasi pasangannya.
  - TC-FA-TAG-1342 Post Condition ("hanya satu entri Changelog Replace") tanpa langkah observasi tidak diasersi.
  - TC-FA-TAG-1343 tidak menyebut cara membuat layanan Global tidak terjangkau; spec menuliskannya sebagai kemampuan intercept yang disediakan tim FE/BE.
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.
