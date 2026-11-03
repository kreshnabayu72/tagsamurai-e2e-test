---
id: TC-AC-ACHS-E2E-257-sync-berhasil-counter-remove-dan-power
title: "Sync Berhasil, Counter, Remove, dan Nilai Power Add Stock Sync"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACHS-121
  - TC-AC-ACHS-122
  - TC-AC-ACHS-123
  - TC-AC-ACHS-128
  - TC-AC-ACHS-129
  - TC-AC-ACHS-160
coverage:
  web: automated
---

# Sync Berhasil, Counter, Remove, dan Nilai Power Add Stock Sync

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

- Data Pre-setup: SKU `{skuLong}` (Long Range, Min `-20 dBm`, Max `30 dBm`) dan `{skuTc52}` (Short Range) dari Pre-setup #16; service driver mock Handheld Reader dengan perangkat simulasi (Pre-setup #25).
- Data Dinamis (suffix per run `{runId}-257`): perangkat simulasi `SN-ZEBRA-TC52-100001-{runId}-257` (TC-122); `SN-ZEBRA-RFD40-100001-{runId}-257` dengan Min `-20 dBm`, Max `30 dBm`, Current `27 dBm` (TC-121); `SN-ZEBRA-RFD40-100011-{runId}-257` (TC-123, TC-129); `SN-ZEBRA-RFD40-100031-{runId}-257` dan `sn-zebra-rfd40-100031-{runId}-257` huruf kecil (TC-128); `SN-ZEBRA-RFD40-100171-{runId}-257` (TC-160). Unit yang disimpan hanya `SN-ZEBRA-RFD40-100031-{runId}-257` dan `SN-ZEBRA-RFD40-100171-{runId}-257` (langkah 53), dihapus hook `after`.
- Kemampuan teknis (disediakan tim FE): simulator reader USB Pre-setup #25 dengan Serial Number dan Min/Max/Current Power yang dapat diatur serta pembacaan perangkat yang dapat ditunda sesaat (agar spinner `Syncing...` teramati; penundaan hanya pemicu state UI dan dilepas segera); pencatatan permintaan driver (TC-122 butir b dan c); pemantauan permintaan jaringan (TC-129 butir d); fixture BE yang menghapus unit bersuffix `-{runId}-257` di hook `after` (mekanismenya tidak didefinisikan di TC, PRD, atau LLD, lihat Temuan untuk QA). Mode simulator dipulihkan di hook `after`.
- Efek pada Pre-setup: Total Registered, Available, dan Last Updated baris SKU {skuLong} berubah oleh dua unit baru (SKU Pre-setup tidak dapat dimiliki spec); dua unit dihapus hook `after`.

## Test Steps

### TC-AC-ACHS-122: Short Range, nilai Power tidak diminta

1. Atur simulator: driver terpasang dan perangkat `SN-ZEBRA-TC52-100001-{runId}-257` terhubung
2. Ketik Search `{skuTc52}`, tekan Enter
3. Klik `(⋯)` pada baris SKU `{skuTc52}`
4. Klik opsi `Add Stock`
5. Klik `[Sync]`
6. Verifikasi satu baris masuk dengan Serial Number `SN-ZEBRA-TC52-100001-{runId}-257` dan Status `OK`
7. Verifikasi driver hanya diminta membaca Serial Number
8. Verifikasi Min Power, Max Power, dan Current Power tidak diminta ke driver
9. Verifikasi tabel Synced Units tidak memiliki kolom Min Power, Max Power, dan Current Power
10. Klik `[Cancel]`
11. Verifikasi dialog Unsaved Changes dengan pesan "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
12. Klik `[Leave]`

### TC-AC-ACHS-121: Sync Long Range berhasil

13. Atur simulator: perangkat `SN-ZEBRA-RFD40-100001-{runId}-257` dengan Min `-20 dBm`, Max `30 dBm`, Current `27 dBm`, pembacaan ditunda sesaat
14. Klik segmen `Stock` pada breadcrumb
15. Ketik Search `{skuLong}`, tekan Enter
16. Klik `(⋯)` pada baris SKU `{skuLong}`
17. Klik opsi `Add Stock`
18. Klik `[Sync]`
19. Verifikasi tombol `[Sync]` berubah menjadi spinner "Syncing..." dan disabled selama proses
20. Lepas penundaan pembacaan simulator
21. Verifikasi satu baris masuk dengan Serial Number `SN-ZEBRA-RFD40-100001-{runId}-257` (mono)
22. Verifikasi Status baris itu `OK` (badge success)
23. Verifikasi Min Power `-20 dBm`, Max Power `30 dBm`, dan Current Power `27 dBm` pada baris itu
24. Verifikasi counter "1 unit synced"
25. Verifikasi `[Submit]` enabled

### TC-AC-ACHS-123: Counter satu dan jamak

26. Atur simulator: perangkat `SN-ZEBRA-RFD40-100011-{runId}-257` terhubung
27. Klik `[Sync]`
28. Verifikasi counter "2 units synced"

### TC-AC-ACHS-129: Remove baris Synced Units

29. Klik `(⋯)` pada baris pertama tabel Synced Units
30. Verifikasi overlay berisi satu opsi `Remove` (ikon merah atau danger)
31. Klik `Remove`
32. Verifikasi baris pertama hilang dari tabel tanpa dialog konfirmasi
33. Verifikasi counter turun menjadi "1 unit synced"
34. Verifikasi tidak ada permintaan ke server selama Remove
35. Klik `[Cancel]`
36. Verifikasi dialog Unsaved Changes dengan pesan "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
37. Klik `[Leave]`

### TC-AC-ACHS-128: Perangkat yang sama di-Sync dua kali

38. Atur simulator: perangkat `SN-ZEBRA-RFD40-100031-{runId}-257` terhubung
39. Klik `[Add Stock]` pada toolbar Tab Available SKU `{skuLong}` (form baru)
40. Klik `[Sync]`
41. Klik `[Sync]` lagi dengan perangkat yang sama
42. Verifikasi banner warning inline "This unit is already in the list." tampil pada Sync kedua
43. Atur simulator: perangkat dengan Serial Number huruf kecil `sn-zebra-rfd40-100031-{runId}-257`
44. Klik `[Sync]`
45. Verifikasi banner warning inline "This unit is already in the list." tampil pada Sync ketiga
46. Verifikasi tabel tetap berisi satu baris dan counter "1 unit synced"

### TC-AC-ACHS-160: Nilai Power tidak bisa diubah

47. Atur simulator: perangkat `SN-ZEBRA-RFD40-100171-{runId}-257` terhubung
48. Klik `[Sync]`
49. Klik sel Current Power baris `SN-ZEBRA-RFD40-100171-{runId}-257` pada tabel Synced Units
50. Verifikasi sel Power pada tabel Synced Units tidak dapat diedit
51. Klik `(⋯)` pada baris `SN-ZEBRA-RFD40-100171-{runId}-257`
52. Verifikasi overlay tidak memuat aksi Edit atau re-sync
53. Klik `[Submit]`
54. Tunggu aksi selesai (redirect ke Stock Detail > Tab Available)
55. Ketik Search `SN-ZEBRA-RFD40-100171-{runId}-257` pada Tab Available, tekan Enter
56. Klik sel Min Power unit `SN-ZEBRA-RFD40-100171-{runId}-257`
57. Verifikasi sel Power pada Tab Available tidak dapat diedit
58. Klik `(⋯)` pada baris unit itu
59. Verifikasi overlay unit tidak memuat aksi Edit atau re-sync

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-121, 122, 123, 128, 129, 160). Tidak ada TC hanya-BE di spec ini.
- Spec ini melewati sekitar 35 langkah (59 langkah). Alasan: seluruh blok satu kelas harness (d, simulator USB) pada layar Add Stock Sync yang sama; blok TC-122 memakai SKU berbeda pada form terpisah dan blok TC-121/123/129 serta TC-128/160 masing-masing form baru; kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Urutan TC di spec berbeda dari nomor TC: TC-122 (SKU Short Range, form bersih lebih dulu); TC-121, 123, 129 pada satu form (jumlah baris berurutan 1, 2, lalu 1 setelah Remove); TC-128 dan TC-160 pada form kedua RFD40, dengan TC-160 di akhir karena menyimpan dua unit (aksi mengubah data di akhir, prinsip 5). Buka form 3 kali (langkah 4, 17, 39) untuk 3 kejadian menutup form: dua kali dirty lewat `[Cancel]` dan `[Leave]` (langkah 10 sampai 12 dan 35 sampai 37) dan satu kali Submit (langkah 53).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search (langkah 2, 15, 55), pengaturan simulator (langkah 1, 13, 20, 26, 38, 43, 47), `[Add Stock]` toolbar (langkah 39), klik segmen `Stock` pada breadcrumb (langkah 14) dan `Tunggu aksi selesai` (langkah 54). Pada TC-123, perangkat pertama adalah baris dari TC-121 (`100001`) sehingga counter "1 unit synced" sudah diverifikasi pada langkah 24 (Expected a TC-123); perangkat kedua `100011` menggantikan pasangan `100011` dan `100012` di TC-123 supaya blok tetap satu form (Expected b pada langkah 28).
- Penundaan pembacaan simulator pada langkah 13 sampai 20 adalah pemicu state UI sementara (spinner), bukan kelas b; dilepas segera setelah asersi spinner (S-09).
- Temuan untuk QA:
  - TC-123 mensyaratkan dua perangkat berbeda (`100011` lalu `100012`) dalam satu langkah; spec memakai perangkat TC-121 sebagai perangkat pertama (lihat atas).
  - TC-121 butir a menyebut spinner "Syncing..." selama proses tanpa menyebut durasinya; penundaan pembacaan oleh simulator tidak didefinisikan di TC, PRD, atau LLD dan disediakan tim FE.
  - TC-160 butir b ("tidak ada aksi Edit atau re-sync") tidak menyebut lokasi pemeriksaan; spec memeriksa overlay `(⋯)` pada tabel Synced Units dan pada Tab Available.
  - TC-122 butir b dan c (driver hanya diminta membaca Serial Number) tidak menyebut cara mengamati permintaan driver; disediakan tim FE (pencatatan permintaan simulator).
  - TC-121, 122, 123, 128, 129, dan 160 tidak memuat Post Condition yang punya langkah observasi.
