---
id: TC-AC-ACTS-E2E-072-add-stock-ble-reload-back-fisik-pindah-tab-scanner-tidak-terhubung-dan-putus
title: "Add Stock BLE: Reload, Back Fisik, Pindah Tab, Scanner Tidak Terhubung (Toast V-04), Putus di Tengah Sesi, dan Putus saat Idle"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-224
  - TC-AC-ACTS-225
  - TC-AC-ACTS-226
  - TC-AC-ACTS-227
  - TC-AC-ACTS-228
  - TC-AC-ACTS-798
coverage:
  web: automated
---

# Add Stock BLE: Reload, Back Fisik, Pindah Tab, Scanner Tidak Terhubung (Toast V-04), Putus di Tengah Sesi, dan Putus saat Idle

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- SKU Pre-setup #14 `BLE-BEACON-ALPHA-B1` (Device Name `BLE Beacon Alpha`, Brand `Alpha`, Model `B1`, TAG Type BLE).
- Kemampuan teknis: simulator pemindai BLE (scan satu per satu, beruntun, kode tidak dikenal, putus koneksi, beberapa reader) disediakan tim FE; mekanismenya tidak dikarang di spec. Reader terhubung pada awal spec kecuali spec menyatakan lain.
- Kemampuan teknis tambahan: penanganan dialog `beforeunload` browser (konfirmasi bawaan muncul, lalu dibatalkan) disediakan runner; tab browser kedua hanya dipakai untuk berpindah tab (S-08).
- TAG uji BLE (identifier tetap Data Uji Dinamis #1 dan #4 untuk TAG yang disebut TC; TAG lain bernilai unik dan belum terdaftar, ditetapkan fixture):

| TAG | MAC |
|---|---|
| TAG A | `Fixture.tagStock.bleA.mac` (`AA:BB:CC:11:22:33`) |
| TAG B | `Fixture.tagStock.bleB.mac` |

- Kemampuan teknis: kemampuan baca BE (jumlah baris Event Log, entri Activity Log, Subject pending, Total Registered, saldo Stock Ledger) dan fixture BE (seed dan pemulihan SKU, unit, Subject, toggle) serta sesi API aktor disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Seeding di hook `before`; unit, Subject, dan log milik spec dipulihkan atau dihapus lewat fixture BE di hook `after` (S-06). Identifier tetap (Data Uji Dinamis #1, #2, #4) tidak bersuffix `{runId}` dan seeding idempotent (S-12, lihat Temuan untuk QA).
- Suite berjalan serial (`parallel: false`); simulator reader bersama. Spec ini tidak mengubah state global kecuali yang disebut di atas.

## Test Steps

1. Catat baseline Total Registered SKU `BLE-BEACON-ALPHA-B1` lewat kemampuan baca BE
2. Atur simulator: scanner BLE tidak terhubung
3. Ketik Search `BLE-BEACON-ALPHA-B1`, tekan Enter
4. Klik (⋯) baris SKU `BLE-BEACON-ALPHA-B1`, klik `Add Stock`

### TC-AC-ACTS-226: Add by Scan tanpa scanner BLE terhubung

5. Klik `[Add by Scan]`
6. Verifikasi toast error `Scanner not connected. Check Bluetooth connection.`
7. Verifikasi sesi tidak dimulai dan halaman tetap Idle
8. Verifikasi tombol `[Reconnect]` inline tampil

### TC-AC-ACTS-228: Scanner BLE putus saat Idle

9. Hubungkan scanner BLE melalui simulator
10. Putuskan Bluetooth scanner BLE saat belum ada sesi
11. Verifikasi `Scanner disconnected.` tampil
12. Verifikasi tombol `[Reconnect]` tampil

### TC-AC-ACTS-227: Scanner BLE putus di tengah sesi scan

13. Hubungkan kembali scanner BLE melalui simulator
14. Klik `[Add by Scan]`
15. Scan TAG A
16. Scan TAG B
17. Putuskan Bluetooth semua perangkat yang melayani sesi
18. Verifikasi sesi berhenti otomatis seperti `[Stop]` (blur hilang)
19. Verifikasi widget scan hilang
20. Verifikasi dua baris yang sudah ter-scan tetap ada
21. Verifikasi Sync Panel terbuka otomatis
22. Verifikasi tidak ada popup `[Reconnect]` terpisah
23. Tutup Sync Panel, hubungkan kembali scanner BLE melalui simulator

### TC-AC-ACTS-224: Reload dengan list berisi

24. Tekan F5
25. Verifikasi konfirmasi bawaan browser muncul (teks ditentukan browser)
26. Batalkan konfirmasi browser agar tetap di halaman
27. Klik `Select All (2 records)`, pilih Bulk Action > `Remove`, klik `[Remove]`
28. Verifikasi Scanned TAG List kosong
29. Tekan F5
30. Verifikasi halaman Add Stock tampil
31. Verifikasi konfirmasi bawaan browser tidak muncul
32. Hubungkan scanner BLE melalui simulator

### TC-AC-ACTS-798: Berpindah tab browser saat sesi BLE aktif

33. Klik `[Add by Scan]`
34. Pindah ke tab browser lain
35. Kembali ke tab ini
36. Verifikasi modal `BLE Scan Stopped` muncul saat tab kembali aktif
37. Klik `Continue Scan`

### TC-AC-ACTS-225: Back fisik saat sesi BLE aktif

38. Tekan Back browser
39. Verifikasi modal `BLE Scan Stopped` dengan body `The scan process was interrupted because you left this window.`, tombol `Leave Page` (kiri) dan `Continue Scan` (kanan)
40. Klik `Leave Page`
41. Verifikasi halaman Add Stock ditinggalkan
42. Verifikasi Total Registered SKU sama dengan baseline (hasil scan yang belum Submit hilang)

## Notes

- Langkah penghubung (S-03): langkah 3 dan 4 (membuka halaman Add Stock), langkah 27 (mengosongkan list untuk Expected (b) TC-AC-ACTS-224), langkah 32 (menyambungkan scanner lagi sesudah reload), penyetelan simulator scanner antar TC (menghubungkan dan memutuskan), penutupan Sync Panel, `[Add by Scan]` untuk membentuk sesi aktif, dan `Continue Scan` untuk melanjutkan sesi antar TC.
- Urutan TC dalam spec: 226, 228, 227, 224, 798, 225 (keadaan scanner tidak terhubung lebih dulu; TC yang keluar halaman 225 di akhir, S-10).
- Temuan untuk QA:
  - TC-AC-ACTS-227 dan TC-AC-ACTS-228 menyebut "putuskan Bluetooth" tanpa menjelaskan cara memutus scanner di simulator; disediakan tim FE.
  - TC-AC-ACTS-225 Expected "hasil scan yang belum Submit hilang" tidak memberi langkah observasi; spec membandingkan Total Registered dengan baseline lewat kemampuan baca BE.
  - TC-AC-ACTS-798: keadaan saat berpindah tab tidak dapat diamati dari tab yang tidak aktif; hanya kemunculan modal saat kembali yang diasersi.
- Alasan di atas sekitar 35 langkah (8b butir 7): semua blok satu kelas harness (simulator scanner BLE) dan satu dataset; tiap blok berdiri sendiri dan kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Temuan untuk QA (identifier): identifier TAG tetap (EPC, UID, MAC, IMEI Data Uji Dinamis #1, #2, #4) dipakai bersama banyak TC dan tidak dapat bersuffix `{runId}` (S-12); state awal (unit tidak ada atau ada) dijamin seeding idempotent dan fixture BE di hook `before`.
