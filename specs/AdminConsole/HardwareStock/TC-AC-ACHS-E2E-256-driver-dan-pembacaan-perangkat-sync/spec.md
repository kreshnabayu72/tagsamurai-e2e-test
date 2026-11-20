---
id: TC-AC-ACHS-E2E-256-driver-dan-pembacaan-perangkat-sync
title: "Driver dan Pembacaan Perangkat pada Add Stock Sync"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACHS-118
  - TC-AC-ACHS-119
  - TC-AC-ACHS-120
  - TC-AC-ACHS-124
  - TC-AC-ACHS-125
  - TC-AC-ACHS-126
  - TC-AC-ACHS-127
coverage:
  web: automated
---

# Driver dan Pembacaan Perangkat pada Add Stock Sync

## Prerequisites

- Mode: FE+BE (backend nyata, seeding via API).
- Akun aktor: Total Control Principal `totalControlPrincipal_automated_qaTeam1@qwertysystem.net` (Pre-setup #1; `Spectra.env.AC_TC_PASSWORD`). Login di hook `before` spec ini; halaman Hardware > Stock (Stock List) dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Hook suite (`suite.md`): flag Guided Tooltip halaman Stock List, sesi API aktor, seeding Population Stock Pre-setup #16 s.d. #20 dan #27. Suite serial (`parallel: false`).
- Kelas harness: d (simulator reader USB, Pre-setup #25).
- Parameter Pre-setup (nilai persis dibaca dari `fixtures/hardwareStock.json` lewat kunci `Fixture.hardwareStock.<jalur>` pada kolom Fixture key; spec tidak menulis nilainya mentah, dan tiap parameter `{...}` di `## Test Steps` dibaca sebagai nilai kunci itu):

| Parameter | Pre-setup item | Peran/atribut | Fixture key |
|---|---|---|---|
| `{skuLong}` | #16 Tabel A baris 4; #17; #18 | kode SKU Handheld Reader Long Range, Total Registered 25 (18 Available, 7 In Use) dan 1 unit Waiting for Approval | `Fixture.hardwareStock.p16.a[4].sku` |

- Data Pre-setup: SKU `{skuLong}` (Handheld Reader, Long Range; Pre-setup #16); service driver mock Handheld Reader (Pre-setup #25) dan mode driver tidak terpasang (Pre-setup #25b).
- Data Dinamis: Serial Number perangkat simulasi TC-127 `SN-ZEBRA-RFD40-100021-{runId}-256` (Min Power `-20 dBm`, Max Power `30 dBm`, Current Power gagal terbaca) dan TC-120 `SN-ZEBRA-RFD40-100022-{runId}-256`; Serial Number 121 karakter TC-126 `SN-LEN121-` + 111 karakter `A`. Tidak ada unit yang disimpan (form ditutup tanpa Submit).
- Kemampuan teknis (disediakan tim FE): simulator reader USB Pre-setup #25 dengan mode: driver terpasang atau tidak terpasang, cek driver diperlambat 2 detik (nilai TC-118), tanpa perangkat terhubung, perangkat gagal baca Serial Number, Serial Number 121 karakter, dan Current Power gagal terbaca; pemantauan permintaan jaringan ke server (TC-124 butir b); jeda nyata 30 detik tanpa tindakan (nilai TC-120, jeda pendek yang diizinkan bagian 6). Mode simulator dipulihkan ke driver terpasang di hook `after` walau spec gagal di tengah.
- State global: mode simulator driver (langkah 1, 9, 14, 18, 22, 30, 40); dipulihkan di hook `after`.

## Test Steps

### TC-AC-ACHS-118: Banner driver terdeteksi dan state Checking driver

1. Atur simulator: driver terpasang dengan cek driver diperlambat 2 detik
2. Ketik Search `{skuLong}`, tekan Enter
3. Klik `(⋯)` pada baris SKU `{skuLong}`
4. Klik opsi `Add Stock`
5. Verifikasi spinner "Checking driver..." tampil saat halaman dimuat
6. Verifikasi `[Sync]` disabled saat cek driver
7. Verifikasi banner netral "Driver detected — ready to sync." tampil setelah cek selesai
8. Verifikasi `[Sync]` enabled setelah driver terdeteksi

### TC-AC-ACHS-124: Driver ada tetapi perangkat tidak terhubung

9. Atur simulator: cek driver normal dan tidak ada perangkat terhubung
10. Klik `[Sync]`
11. Verifikasi error banner inline "No device detected. Connect a Handheld Reader and try again."
12. Verifikasi tidak ada baris ditambahkan pada tabel Synced Units
13. Verifikasi tidak ada permintaan ke server selama Sync

### TC-AC-ACHS-125: Serial Number tidak terbaca dari perangkat

14. Atur simulator: perangkat terhubung tetapi gagal membaca Serial Number
15. Klik `[Sync]`
16. Verifikasi error banner inline "Could not read serial number from device. Try reconnecting."
17. Verifikasi tabel Synced Units tidak berubah

### TC-AC-ACHS-126: Serial Number hasil pembacaan lebih dari 120 karakter

18. Atur simulator: perangkat dengan Serial Number 121 karakter (`SN-LEN121-` + 111 karakter `A`)
19. Klik `[Sync]`
20. Verifikasi error banner inline "Serial number is too long to register."
21. Verifikasi baris tidak ditambahkan

### TC-AC-ACHS-127: Sebagian nilai Power gagal terbaca

22. Atur simulator: perangkat `SN-ZEBRA-RFD40-100021-{runId}-256` dengan Min Power `-20 dBm`, Max Power `30 dBm`, dan Current Power gagal terbaca
23. Klik `[Sync]`
24. Verifikasi baris masuk dengan Status `OK`
25. Verifikasi Current Power baris itu tampil `—`
26. Verifikasi tidak ada toast error dan tidak ada banner

### Menutup form pertama

27. Klik `[Cancel]`
28. Verifikasi dialog Unsaved Changes dengan pesan "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
29. Klik `[Leave]`

### TC-AC-ACHS-119: Driver tidak terdeteksi

30. Atur simulator ke mode driver tidak terpasang (Pre-setup #25b)
31. Klik `[Add Stock]` pada toolbar Tab Available SKU `{skuLong}` (form baru)
32. Verifikasi banner warning persisten (bukan dialog) dengan judul tebal "Driver isn't connected." dan isi "Install the reader driver to connect your reader. Already installed? Open it, or paste the code below into the driver."
33. Verifikasi banner memuat link `[Open it]`, baris "Driver Code:" berisi kode, tombol ikon Copy tanpa label teks dengan aria-label "Copy driver code", dan tombol outline `[Download driver]` di kanan banner yang selalu tampil
34. Klik `[Sync]`
35. Verifikasi `[Sync]` tetap bisa diklik ulang (retry manual) dan banner tetap tampil
36. Verifikasi tidak ada baris ditambahkan
37. Verifikasi tidak ada textarea atau fallback input manual

### TC-AC-ACHS-120: Retry manual setelah driver dipasang

38. Tunggu 30 detik tanpa tindakan
39. Verifikasi banner warning tidak berubah sendiri (tidak ada polling otomatis)
40. Atur simulator: driver terpasang dan perangkat `SN-ZEBRA-RFD40-100022-{runId}-256` terhubung
41. Klik `[Sync]`
42. Verifikasi baris perangkat `SN-ZEBRA-RFD40-100022-{runId}-256` masuk ke tabel Synced Units
43. Klik `[Cancel]`
44. Verifikasi dialog Unsaved Changes dengan pesan "You have unsaved changes. Are you sure you want to leave?" dan tombol `[Cancel]` dan `[Leave]`
45. Klik `[Leave]`

## Notes

- Sumber: `admin-console/hardware-stock/TestCases/tc-hardware-stock.md` (TC-AC-ACHS-118, 119, 120, 124, 125, 126, 127). Tidak ada TC hanya-BE di spec ini.
- Spec ini melewati sekitar 35 langkah (45 langkah). Alasan: seluruh blok satu kelas harness (d, simulator USB) pada satu layar Add Stock Sync SKU yang sama; tiap blok mengatur mode simulator sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna (soft assertion).
- Urutan TC di spec berbeda dari nomor TC: driver terpasang (TC-118, 124, 125, 126, 127) lebih dulu pada form pertama, lalu mode driver tidak terpasang (TC-119, 120) pada form kedua karena memuat ulang deteksi driver. Buka form 2 kali (langkah 4 dan 31) untuk 2 kejadian menutup form dirty (langkah 27 sampai 29 dan 43 sampai 45). TC-120 melanjutkan form TC-119 (precondition sama: driver belum terpasang saat halaman dibuka).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (langkah 2), pengaturan simulator (langkah 1, 9, 14, 18, 22, 30, 40), `[Add Stock]` toolbar pada langkah 31, jeda 30 detik (langkah 38, nilai TC-120), serta `[Cancel]` dan `[Leave]` (S-08).
- Nilai 2 detik (TC-118) dan 30 detik (TC-120) adalah nilai dari Data Uji TC. Kolom sumber PRD TC tidak menandai keduanya `PRD?`; keduanya diperlakukan sebagai pilihan spec.
- Temuan untuk QA:
  - TC-118 butir a menyebut "spinner `Checking driver...`" tanpa menyebut apakah teks banner driver lain tampil; spec mengasersi spinner dan `[Sync]` disabled.
  - TC-124 Expected b ("tidak ada request ke server") tidak menyebut cara mengamati permintaan; spec memakai pemantauan jaringan yang disediakan tim FE.
  - TC-119 butir c dan d (baris tidak ditambahkan dan tanpa fallback input manual) juga diuji di TC-159 (spec 255) pada konteks berbeda; keduanya tetap dipertahankan.
  - TC-118, 119, 120, 124, 125, 126, 127 tidak memuat Post Condition.
