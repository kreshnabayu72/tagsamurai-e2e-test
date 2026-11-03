---
id: TC-AC-ACHS-E2E-255-screening-add-stock-sync-dan-tanpa-input-manual
title: "Screening Add Stock Sync dan Tanpa Input Manual"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-116
  - TC-AC-ACHS-117
  - TC-AC-ACHS-131
  - TC-AC-ACHS-159
coverage:
  web: automated
---

# Screening Add Stock Sync dan Tanpa Input Manual

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Pre-setup #1; `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip halaman Stock List, sesi API aktor, seeding Population Stock Pre-setup #16 s.d. #20 dan #27. Suite serial (`parallel: false`).
- Kelas harness: d (simulator reader USB, Pre-setup #25).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{skuTc52}` | #16 Tabel A baris 1; #19 | kode SKU Handheld Reader Short Range, Total Registered 50 (34 Available, 16 In Use) | `Fixture.hardwareStock.p16.a[1].sku` |
| `{skuLong}` | #16 Tabel A baris 4; #17; #18 | kode SKU Handheld Reader Long Range, Total Registered 25 (18 Available, 7 In Use) dan 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |
| `{deviceNameLong}` | #16 Tabel A baris 4 | Device Name SKU Handheld Reader Long Range | `Fixture.hardwareStock.p16.a[4].deviceName` |
| `{brandLong}` | #16 Tabel A baris 4 | Brand SKU Handheld Reader Long Range | `Fixture.hardwareStock.p16.a[4].brand` |
| `{modelLong}` | #16 Tabel A baris 4 | Model/Type SKU Handheld Reader Long Range | `Fixture.hardwareStock.p16.a[4].modelType` |

- Data Pre-setup: SKU `{skuLong}` (Handheld Reader, Long Range) dan `{skuTc52}` (Handheld Reader, Short Range) dari Pre-setup #16 (atribut katalog lewat parameter atribut pada tabel Parameter Pre-setup); service driver mock Handheld Reader dengan perangkat simulasi (Pre-setup #25) dan mode driver tidak terpasang (Pre-setup #25b).
- Data Dinamis: perangkat simulasi pada TC-131 memakai Serial Number `SN-SYNC-0131-{runId}-255`; tidak pernah disimpan (baris di-Remove dan form ditutup tanpa Submit).
- Kemampuan teknis (disediakan tim FE): simulator reader USB Pre-setup #25 (driver terpasang, perangkat terhubung dengan Serial Number yang dapat diatur, serta mode driver tidak terpasang); mode simulator dipulihkan ke driver terpasang di hook `after` walau spec gagal di tengah.
- State global: mode simulator driver diubah ke tidak terpasang pada langkah 27 dan dipulihkan di hook `after`.

## Test Steps

### TC-AC-ACHS-117: Short Range, kolom Power tidak dirender

1. Ketik Search `{skuTc52}`, tekan Enter
2. Klik `(⋯)` pada baris SKU `{skuTc52}`
3. Klik opsi `Add Stock`
4. Verifikasi SKU Info Card memuat badge `Handheld Reader` dan badge `Short Range`
5. Verifikasi tabel Synced Units hanya berkolom `Serial Number | Status | Actions (⋯)`
6. Verifikasi kolom Min Power, Max Power, dan Current Power tidak dirender sama sekali
7. Klik segmen `Stock` pada breadcrumb (form bersih)

### TC-AC-ACHS-116: Screening Add Stock Sync Long Range

8. Ketik Search `{skuLong}`, tekan Enter
9. Klik `(⋯)` pada baris SKU `{skuLong}`
10. Klik opsi `Add Stock`
11. Verifikasi Breadcrumb `Hardware > Stock > Add Stock`
12. Verifikasi Page Header `Add Stock — {skuLong}`
13. Verifikasi SKU Info Card memuat Foto, `{deviceNameLong}`, `{brandLong}`, `{modelLong}`, badge `Handheld Reader`, dan badge `Long Range`
14. Verifikasi Card Sync memuat banner driver, tombol `[Sync]`, dan helper `Connect the Handheld Reader via USB, then click Sync to read its serial number and power specs.`
15. Verifikasi Card Synced Units: tabel berkolom `Serial Number | Status | Min Power | Max Power | Current Power | Actions (⋯)`
16. Verifikasi empty state tabel Synced Units `No units synced yet. Connect a device and click Sync.`
17. Verifikasi tidak ada textarea Serial Numbers manual
18. Verifikasi Footer (sticky) memuat `[Cancel]` (text, contrast) dan `[Submit]` (filled, success, disabled karena 0 unit ter-Sync)

### TC-AC-ACHS-131: Submit disabled saat 0 unit ter-Sync tanpa pesan

19. Verifikasi `[Submit]` disabled dan tidak bisa diklik pada keadaan 0 baris
20. Verifikasi tidak ada pesan error
21. Klik `[Sync]` dengan perangkat simulasi Serial Number `SN-SYNC-0131-{runId}-255`
22. Klik `(⋯)` pada baris pertama tabel Synced Units
23. Klik `Remove`
24. Verifikasi `[Submit]` disabled dan tidak bisa diklik pada keadaan 0 baris sesudah Remove
25. Verifikasi tidak ada pesan error sesudah Remove
26. Klik `[Cancel]`

### TC-AC-ACHS-159: Tanpa jalur input manual saat driver gagal

27. Atur simulator ke mode driver tidak terpasang (Pre-setup #25b)
28. Klik `[Add Stock]` pada toolbar Tab Available SKU `{skuLong}` (form baru)
29. Verifikasi tombol `[Sync]` tampil
30. Verifikasi tidak ada textarea atau input Serial Number manual pada halaman
31. Klik `[Sync]` saat driver gagal
32. Verifikasi tidak ada textarea atau input Serial Number manual sesudah driver gagal
33. Verifikasi satu-satunya jalan input adalah `[Sync]`
34. Klik `[Cancel]`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-116, 117, 131, 159). Tidak ada TC hanya-BE di spec ini.
- Satu kelas harness: d (simulator reader USB). Urutan TC di spec berbeda dari nomor TC: TC-117 lebih dulu karena memakai SKU lain pada form bersih; TC-131 melanjutkan form TC-116 (keadaan 0 unit ter-Sync tetap sama sampai Sync); TC-159 terakhir karena mengubah mode simulator. Buka form 3 kali (langkah 3, 10, 28) untuk 3 kejadian menutup form (langkah 7, 26, 34); `[Cancel]` pada langkah 26 dan 34 menutup form dengan tabel Synced Units kosong sehingga tidak memunculkan dialog (TC-156).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (langkah 1, 8), langkah 21 sampai 23 dan 27 (pemicu), serta `[Add Stock]` toolbar pada langkah 28 dan `[Cancel]`.
- Expected TC-131 butir a (`[Submit]` disabled) dan butir b (tanpa pesan) diasersi dua kali: sebelum Sync (langkah 19, 20) dan sesudah Remove (langkah 24, 25) sesuai langkah TC-131 yang menyebut kedua keadaan.
- Expected TC-159 butir a dan b adalah dua klausa dari langkah "driver gagal lalu cari alternatif input"; spec memeriksa keduanya sesudah `[Sync]` pada driver gagal (langkah 32 dan 33).
- Temuan untuk QA:
  - TC-116 Expected a.i tidak menyebut isi banner driver pada Card Sync; spec mengasersi banner tampil bersama tombol dan helper.
  - TC-159 langkah 5 ("Simulasikan driver gagal") tidak menyebut apakah yang dimaksud driver tidak terpasang atau perangkat gagal baca; spec memakai mode driver tidak terpasang (Pre-setup #25b).
  - TC-117, 131, dan 159 tidak memuat Post Condition; TC-116 tidak memuat Post Condition.
