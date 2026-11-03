---
id: TC-AC-DS-E2E-047-register-sukses-ble-gateway-dan-tag-user
title: "Register SKU Berhasil: BLE Gateway dan TAG dengan This is User TAG"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-156
  - TC-AC-DS-157
coverage:
  web: automated
---

# Register SKU Berhasil: BLE Gateway dan TAG dengan This is User TAG

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`Hardware > BLE Gateway`, `TAG > NFC > Asset TAG`); Device Name #26 (`BLE Gateway`, `Asset TAG`); Brand Principal #27 (`Kinetia`, `Arcturus`); file foto uji #37 (`foto-a.jpg`, 200 KB); SKU inti #29 dipakai sebagai precondition TC, tidak diasersi.
- General Settings entitas uji (Data Pre-setup #35): Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta; tidak diubah spec ini. Asersi Last Modified memakai waktu yang dicatat sesudah `[Submit]` dengan toleransi satu menit (kolom berketelitian menit); jam server dan jam browser sinkron (S-12).
- Data Dinamis: SKU `NEW-BLE-01-{runId}-047` (Model/Type `GW-N1`) dan `NEW-TAG-01-{runId}-047` (Model/Type `T-N01`, This is User TAG dicentang), dibuat oleh TC-AC-DS-156 dan TC-AC-DS-157. Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API SKU bersuffix `{runId}-047` milik Principal.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

### TC-AC-DS-156: Register SKU berhasil: BLE Gateway tanpa field kondisional

1. Klik tombol `[+ SKU]` pada toolbar
2. Klik field Category, expand `Hardware`, pilih node `BLE Gateway`, lalu klik `[Select]`
3. Klik field Device Name lalu pilih `BLE Gateway`
4. Klik field Brand lalu pilih `Kinetia`
5. Ketik `GW-N1` pada field Model/Type
6. Ketik `NEW-BLE-01-{runId}-047` pada field SKU
7. Unggah `foto-a.jpg` pada field Photo
8. Klik `[Submit]`, lalu catat waktu aksi sebagai T1
9. Verifikasi toast sukses "Success, device SKU has been registered." tampil
10. Verifikasi popup Register tertutup karena Stay tidak tercentang
11. Ketik Search `NEW-BLE-01-{runId}-047`, tekan Enter
12. Verifikasi baris `NEW-BLE-01-{runId}-047` tampil dengan Category badge `BLE Gateway`, Brand badge `Kinetia`, Model/Type badge `GW-N1`, dan Current Stock `0`
13. Verifikasi Last Modified baris `NEW-BLE-01-{runId}-047` menampilkan waktu pendaftaran sesuai General Settings (sama dengan T1, toleransi satu menit)
14. Klik ⋯ pada baris `NEW-BLE-01-{runId}-047` lalu pilih `Edit`
15. Verifikasi popup Edit SKU menampilkan Category `BLE Gateway` dalam keadaan read-only
16. Verifikasi popup Edit SKU menampilkan Device Name `BLE Gateway`, Brand `Kinetia`, dan Model/Type `GW-N1`
17. Verifikasi popup Edit SKU menampilkan satu foto sebagai default
18. Verifikasi popup Edit SKU tanpa field Range Type, Port, dan This is User TAG
19. Klik ikon close `[✕]` pada popup Edit SKU

### TC-AC-DS-157: Register SKU berhasil: TAG dengan This is User TAG dicentang

20. Klik tombol `[+ SKU]` pada toolbar
21. Klik field Category, expand `TAG` lalu `NFC`, pilih node `Asset TAG`, lalu klik `[Select]`
22. Klik field Device Name lalu pilih `Asset TAG`
23. Klik field Brand lalu pilih `Arcturus`
24. Ketik `T-N01` pada field Model/Type
25. Ketik `NEW-TAG-01-{runId}-047` pada field SKU
26. Centang checkbox `This is User TAG`
27. Unggah `foto-a.jpg` pada field Photo
28. Klik `[Submit]`, lalu catat waktu aksi sebagai T2
29. Verifikasi toast sukses "Success, device SKU has been registered." tampil
30. Verifikasi popup Register tertutup karena Stay tidak tercentang
31. Ganti isi kotak search dengan `NEW-TAG-01-{runId}-047`, tekan Enter
32. Verifikasi baris `NEW-TAG-01-{runId}-047` tampil dengan Category badge `Asset TAG`, Brand badge `Arcturus`, Model/Type badge `T-N01`, dan Current Stock `0`
33. Verifikasi Last Modified baris `NEW-TAG-01-{runId}-047` menampilkan waktu pendaftaran sesuai General Settings (sama dengan T2, toleransi satu menit)
34. Klik ⋯ pada baris `NEW-TAG-01-{runId}-047` lalu pilih `Edit`
35. Verifikasi popup Edit SKU menampilkan Category `Asset TAG` dalam keadaan read-only
36. Verifikasi popup Edit SKU menampilkan Device Name `Asset TAG`, Brand `Arcturus`, dan Model/Type `T-N01`
37. Verifikasi popup Edit SKU menampilkan checkbox `This is User TAG` tercentang
38. Verifikasi popup Edit SKU menampilkan satu foto sebagai default
39. Klik ikon close `[✕]` pada popup Edit SKU
40. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 11, 31, dan 40 (Search untuk menemukan baris target lalu menutup Search, R-16); langkah 19 dan 39 menutup popup Edit SKU yang tidak diubah (form bersih, tanpa dialog Unsaved Changes). Pencatatan T1 dan T2 mengikuti S-12.
- Ukuran spec (di atas sekitar 35 langkah): kedua blok adalah alur Register berhasil dengan pola yang sama per tipe hardware (kelas fungsional yang sama), tiap blok membuat SKU, memeriksanya di List, dan membuka popup Edit sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan langkah yang diulang per blok mengikuti langkah TC.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-047` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - Post Condition TC-AC-DS-156 dan TC-AC-DS-157 (entri log Changelog, System Log, Activity Log) tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini (S-01).
