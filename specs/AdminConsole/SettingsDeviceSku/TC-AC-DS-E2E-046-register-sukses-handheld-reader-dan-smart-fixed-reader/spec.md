---
id: TC-AC-DS-E2E-046-register-sukses-handheld-reader-dan-smart-fixed-reader
title: "Register SKU Berhasil: Handheld Reader (Long Range) dan Smart Fixed Reader (Port 8080)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-DS-154
  - TC-AC-DS-155
coverage:
  web: automated
---

# Register SKU Berhasil: Handheld Reader (Long Range) dan Smart Fixed Reader (Port 8080)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal PT Arunika Prima (Data Pre-setup #1) `totalControlSku_automated_{namaCompany}@qwertysystem.net`, password dari `Spectra.env.AC_DS_TC_PASSWORD` (nama env baru, disediakan tim FE). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; tidak ada ganti akun di tengah spec. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): `before` login akun default, `beforeEach` membuka Settings > Device > Device SKU, `after` memulihkan state global; suite serial (`parallel: false`).
- Data Pre-setup (tetap di environment, nilai ditulis literal sesuai TC): pohon Category #25 (`Hardware > Handheld Reader > UHF Handheld`, `Hardware > Smart Fixed Reader > Portal Reader`); Device Name #26 (`UHF Handheld Reader`, `4-Port Fixed Reader`); Brand Principal #27 (`Arcturus`, `Veltrix`); file foto uji #37 (`foto-a.jpg`, 200 KB); SKU inti #29 dipakai sebagai precondition TC, tidak diasersi.
- General Settings entitas uji (Data Pre-setup #35): Date Format `dd/MM/yy`, Time Format 24 jam, Time Zone Asia/Jakarta; tidak diubah spec ini. Asersi Last Modified memakai waktu yang dicatat sesudah `[Submit]` dengan toleransi satu menit (kolom berketelitian menit); jam server dan jam browser sinkron (S-12).
- Data Dinamis: SKU `NEW-HHR-01-{runId}-046` (Model/Type `H-N01`, Range Type `Long Range`) dan `NEW-SFR-01-{runId}-046` (Model/Type `SF-N1`, Port `8080`), dibuat oleh TC-AC-DS-154 dan TC-AC-DS-155. Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): hapus lewat API SKU bersuffix `{runId}-046` milik Principal.
- Fixture `Fixture.settingsDeviceSku` (`fixtures/settings-device-sku.json`) belum ada dan disediakan pada tahap script; memuat email akun dan nilai Pre-setup yang dipakai. Nilai Pre-setup yang menjadi teks UI yang diasersi ditulis literal sesuai TC.

## Test Steps

### TC-AC-DS-154: Register SKU berhasil: Handheld Reader dengan Range Type Long Range

1. Klik tombol `[+ SKU]` pada toolbar
2. Klik field Category, expand `Hardware` lalu `Handheld Reader`, pilih node `UHF Handheld`, lalu klik `[Select]`
3. Klik field Device Name lalu pilih `UHF Handheld Reader`
4. Klik field Brand lalu pilih `Arcturus`
5. Ketik `H-N01` pada field Model/Type
6. Ketik `NEW-HHR-01-{runId}-046` pada field SKU
7. Pilih Range Type `Long Range`
8. Unggah `foto-a.jpg` pada field Photo
9. Klik `[Submit]`, lalu catat waktu aksi sebagai T1
10. Verifikasi toast sukses "Success, device SKU has been registered." tampil
11. Verifikasi popup Register tertutup karena Stay tidak tercentang
12. Ketik Search `NEW-HHR-01-{runId}-046`, tekan Enter
13. Verifikasi baris `NEW-HHR-01-{runId}-046` tampil dengan Category badge `UHF Handheld`, Brand badge `Arcturus`, Model/Type badge `H-N01`, dan Current Stock `0`
14. Verifikasi Last Modified baris `NEW-HHR-01-{runId}-046` menampilkan waktu pendaftaran sesuai General Settings (sama dengan T1, toleransi satu menit)
15. Klik ⋯ pada baris `NEW-HHR-01-{runId}-046` lalu pilih `Edit`
16. Verifikasi popup Edit SKU menampilkan Category `UHF Handheld` dalam keadaan read-only
17. Verifikasi popup Edit SKU menampilkan Device Name `UHF Handheld Reader`, Brand `Arcturus`, dan Model/Type `H-N01`
18. Verifikasi popup Edit SKU menampilkan Range Type `Long Range`
19. Verifikasi popup Edit SKU menampilkan satu foto sebagai default
20. Klik ikon close `[✕]` pada popup Edit SKU

### TC-AC-DS-155: Register SKU berhasil: Smart Fixed Reader dengan Port 8080

21. Klik tombol `[+ SKU]` pada toolbar
22. Klik field Category, expand `Hardware` lalu `Smart Fixed Reader`, pilih node `Portal Reader`, lalu klik `[Select]`
23. Klik field Device Name lalu pilih `4-Port Fixed Reader`
24. Klik field Brand lalu pilih `Veltrix`
25. Ketik `SF-N1` pada field Model/Type
26. Ketik `NEW-SFR-01-{runId}-046` pada field SKU
27. Ketik `8080` pada field Port
28. Unggah `foto-a.jpg` pada field Photo
29. Klik `[Submit]`, lalu catat waktu aksi sebagai T2
30. Verifikasi toast sukses "Success, device SKU has been registered." tampil
31. Verifikasi popup Register tertutup karena Stay tidak tercentang
32. Ganti isi kotak search dengan `NEW-SFR-01-{runId}-046`, tekan Enter
33. Verifikasi baris `NEW-SFR-01-{runId}-046` tampil dengan Category badge `Portal Reader`, Brand badge `Veltrix`, Model/Type badge `SF-N1`, dan Current Stock `0`
34. Verifikasi Last Modified baris `NEW-SFR-01-{runId}-046` menampilkan waktu pendaftaran sesuai General Settings (sama dengan T2, toleransi satu menit)
35. Klik ⋯ pada baris `NEW-SFR-01-{runId}-046` lalu pilih `Edit`
36. Verifikasi popup Edit SKU menampilkan Category `Portal Reader` dalam keadaan read-only
37. Verifikasi popup Edit SKU menampilkan Device Name `4-Port Fixed Reader`, Brand `Veltrix`, dan Model/Type `SF-N1`
38. Verifikasi popup Edit SKU menampilkan Port `8080`
39. Verifikasi popup Edit SKU menampilkan satu foto sebagai default
40. Klik ikon close `[✕]` pada popup Edit SKU
41. Klik `(←)` pada kotak Search

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-sku/TestCases/tc-settings-device-sku.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa Verifikasi, S-03): langkah 12, 32, dan 41 (Search untuk menemukan baris target lalu menutup Search, R-16); langkah 20 dan 40 menutup popup Edit SKU yang tidak diubah (form bersih, tanpa dialog Unsaved Changes). Pencatatan T1 dan T2 mengikuti S-12.
- Ukuran spec (di atas sekitar 35 langkah): kedua blok adalah alur Register berhasil dengan pola yang sama per tipe hardware (kelas fungsional yang sama), tiap blok membuat SKU, memeriksanya di List, dan membuka popup Edit sendiri; kegagalan satu blok tidak membuat blok lain kehilangan makna, dan langkah yang diulang per blok mengikuti langkah TC.
- Temuan untuk QA:
  - Nama env `Spectra.env.AC_DS_*` yang dipakai spec ini dan fixture `fixtures/settings-device-sku.json` belum terdaftar di `spectra.config.ts`, `.env.example`, dan `fixtures/`; disediakan tim FE.
  - S-12: Lampiran A tidak memuat butir modul ini sehingga pengecualian nama literal Pre-setup (#25, #26, #27, #29, #31) belum diputuskan; spec memakai nama Pre-setup apa adanya untuk asersi dan memberi suffix `{runId}-046` pada data Dinamis yang disimpan.
  - Walkthrough tooltip Settings > Device dimiliki modul lain; bila tampil menutupi layar, cara menyetel flag-nya belum ditentukan.
  - Post Condition TC-AC-DS-154 dan TC-AC-DS-155 (entri log Changelog, System Log, Activity Log) tidak punya langkah observasi di TC sehingga tidak diasersi di spec ini (S-01).
