---
id: TC-AC-ACTS-E2E-066-add-stock-nfc-reload-back-fisik-reader-putus-dan-remove-nfc-ble
title: "Add Stock NFC: Reload, Back Fisik, Pindah Tab, Reader Tidak Terhubung atau Putus, serta Remove Manual dan Remove by Scan NFC dan BLE"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-195
  - TC-AC-ACTS-196
  - TC-AC-ACTS-197
  - TC-AC-ACTS-198
  - TC-AC-ACTS-199
  - TC-AC-ACTS-797
  - TC-AC-ACTS-877
coverage:
  web: automated
---

# Add Stock NFC: Reload, Back Fisik, Pindah Tab, Reader Tidak Terhubung atau Putus, serta Remove Manual dan Remove by Scan NFC dan BLE

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- SKU Pre-setup #13 `NFC-CARD-BETA-N2` (Device Name `NFC Access Card`, Brand `Beta`, Model `N2`, TAG Type NFC).
- SKU Pre-setup #14 `BLE-BEACON-ALPHA-B1` (Device Name `BLE Beacon Alpha`, Brand `Alpha`, Model `B1`, TAG Type BLE).
- Kemampuan teknis: simulator pemindai NFC, BLE (scan satu per satu, beruntun, kode tidak dikenal, putus koneksi, beberapa reader) disediakan tim FE; mekanismenya tidak dikarang di spec. Reader terhubung pada awal spec kecuali spec menyatakan lain.
- Kemampuan teknis tambahan: penanganan dialog `beforeunload` browser (konfirmasi bawaan muncul, lalu dibatalkan) disediakan runner; tab browser kedua hanya dipakai untuk berpindah tab (S-08).
- TAG uji NFC (identifier tetap Data Uji Dinamis #1 dan #4 untuk TAG yang disebut TC; TAG lain bernilai unik dan belum terdaftar, ditetapkan fixture):

| TAG | UID |
|---|---|
| TAG A | `Fixture.tagStock.nfcA.uid` (`A1B2C3D4E5F7`) |
| TAG B | `Fixture.tagStock.nfcB.uid` |
| TAG C | `Fixture.tagStock.nfcC.uid` |

- TAG uji BLE (blok BLE TC-AC-ACTS-877; TAG A dan TAG B pada blok itu adalah TAG BLE) (identifier tetap Data Uji Dinamis #1 dan #4 untuk TAG yang disebut TC; TAG lain bernilai unik dan belum terdaftar, ditetapkan fixture):

| TAG | MAC |
|---|---|
| TAG A | `Fixture.tagStock.bleA.mac` (`AA:BB:CC:11:22:33`) |
| TAG B | `Fixture.tagStock.bleB.mac` |

- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Catat baseline Total Registered SKU `NFC-CARD-BETA-N2` lewat kemampuan baca BE
2. Atur simulator: reader NFC tidak terhubung
3. Ketik Search `NFC-CARD-BETA-N2`, tekan Enter
4. Klik (⋯) baris SKU `NFC-CARD-BETA-N2`, klik `Add Stock`

### TC-AC-ACTS-197: Add by Scan tanpa reader NFC terhubung

5. Klik `[Add by Scan]`
6. Verifikasi toast error `Reader not connected. Check Bluetooth connection.`
7. Verifikasi sesi tidak dimulai dan halaman tetap Idle
8. Verifikasi tombol `[Reconnect]` inline tampil

### TC-AC-ACTS-199: Reader NFC putus saat Idle

9. Hubungkan reader NFC melalui simulator
10. Putuskan Bluetooth reader NFC saat belum ada sesi
11. Verifikasi `Reader disconnected.` tampil
12. Verifikasi tombol `[Reconnect]` tampil

### TC-AC-ACTS-198: Reader NFC putus di tengah sesi scan

13. Hubungkan kembali reader NFC melalui simulator
14. Klik `[Add by Scan]`
15. Scan TAG A
16. Scan TAG B
17. Putuskan Bluetooth semua perangkat yang melayani sesi
18. Verifikasi sesi berhenti otomatis seperti `[Stop]` (blur hilang)
19. Verifikasi widget scan hilang
20. Verifikasi dua baris yang sudah ter-scan tetap ada
21. Verifikasi Sync Panel terbuka otomatis
22. Verifikasi tidak ada popup `[Reconnect]` terpisah
23. Tutup Sync Panel, hubungkan kembali reader NFC melalui simulator

### TC-AC-ACTS-195: Reload dengan list berisi

24. Tekan F5
25. Verifikasi konfirmasi bawaan browser muncul (teks ditentukan browser)
26. Batalkan konfirmasi browser agar tetap di halaman

### TC-AC-ACTS-877: Remove manual dan Remove by Scan, NFC

27. Centang TAG A
28. Pilih Bulk Action > `Remove`, klik `[Remove]`
29. Verifikasi toast `Success, TAG has been removed.`
30. Klik `[Remove by Scan]`
31. Scan TAG B
32. Verifikasi toast `Success, <UID TAG B> has been removed.`
33. Klik `[Stop]`
34. Verifikasi list kosong
35. Verifikasi tombol `[Remove by Scan]` Disabled

### TC-AC-ACTS-797: Berpindah tab browser saat sesi NFC aktif

36. Klik `[Add by Scan]`
37. Pindah ke tab browser lain
38. Kembali ke tab ini
39. Verifikasi modal `NFC Scan Stopped` muncul saat tab kembali aktif
40. Klik `Continue Scan`

### TC-AC-ACTS-196: Back fisik saat sesi NFC aktif

41. Tekan Back browser
42. Verifikasi modal `NFC Scan Stopped` dengan body `The scan process was interrupted because you left this window.`, tombol `Leave Page` (kiri) dan `Continue Scan` (kanan)
43. Klik `Leave Page`
44. Verifikasi halaman Add Stock ditinggalkan
45. Verifikasi Total Registered SKU sama dengan baseline (hasil scan yang belum Submit hilang)

### TC-AC-ACTS-877: Remove manual dan Remove by Scan, BLE

46. Ketik Search `BLE-BEACON-ALPHA-B1`, tekan Enter
47. Klik (⋯) baris SKU `BLE-BEACON-ALPHA-B1`, klik `Add Stock`
48. Klik `[Add by Scan]`
49. Scan TAG A
50. Scan TAG B
51. Klik `[Stop]`
52. Centang TAG A
53. Pilih Bulk Action > `Remove`, klik `[Remove]`
54. Verifikasi toast `Success, TAG has been removed.`
55. Klik `[Remove by Scan]`
56. Scan TAG B
57. Verifikasi toast `Success, <MAC TAG B> has been removed.`
58. Klik `[Stop]`
59. Verifikasi list kosong
60. Verifikasi tombol `[Remove by Scan]` Disabled

## Notes

- Langkah penghubung (S-03): langkah 3 dan 4 (membuka halaman Add Stock), penyetelan simulator reader antar TC (menghubungkan dan memutuskan), penutupan Sync Panel, pembentukan list precondition TC-AC-ACTS-877 (scan lalu `[Stop]`), `[Add by Scan]` untuk membentuk sesi aktif, `Continue Scan` untuk melanjutkan sesi antar TC, dan Search `BLE-BEACON-ALPHA-B1` untuk menemukan baris target (R-16).
- TC-AC-ACTS-877 berisi dua bagian (NFC, lalu "ulangi untuk BLE-BEACON-ALPHA-B1"); keduanya ada di spec ini sebagai dua blok. Bagian BLE memakai scanner BLE terhubung dan MAC Address sebagai identifier.
- Urutan TC dalam spec: 197, 199, 198, 195, 877 (NFC), 797, 196, 877 (BLE) (keadaan reader tidak terhubung lebih dulu; TC yang keluar halaman 196 sebelum blok BLE, S-10).
- Alasan di atas sekitar 35 langkah (8b butir 7): semua blok satu kelas harness (simulator reader) dan satu dataset; tiap blok berdiri sendiri.
- Temuan untuk QA:
  - TC-AC-ACTS-198 dan TC-AC-ACTS-199 menyebut "putuskan Bluetooth" tanpa menjelaskan cara memutus reader di simulator; disediakan tim FE.
  - TC-AC-ACTS-877 Expected (a) menyebut dua toast berurutan yang berbeda bentuk (`Success, TAG has been removed.` untuk Remove manual, `Success, [Identifier] has been removed.` untuk Remove by Scan).
  - TC-AC-ACTS-196 Expected "hasil scan yang belum Submit hilang" tidak memberi langkah observasi; spec membandingkan Total Registered dengan baseline lewat kemampuan baca BE.
  - TC-AC-ACTS-797: keadaan saat berpindah tab tidak dapat diamati dari tab yang tidak aktif; hanya kemunculan modal saat kembali yang diasersi.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
