---
id: TC-AC-ACTS-E2E-163-audit-rfid-sesi-scan-aktif-back-fisik-reader-putus-pindah-tab-dan-reload
title: "Audit RFID: Sesi Scan Aktif Ditinggalkan (Back Fisik, Semua Reader Putus, Pindah Tab, dan Reload)"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-335
  - TC-AC-ACTS-336
  - TC-AC-ACTS-799
  - TC-AC-ACTS-800
coverage:
  web: automated
---

# Audit RFID: Sesi Scan Aktif Ditinggalkan (Back Fisik, Semua Reader Putus, Pindah Tab, dan Reload)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Kemampuan teknis: Penanganan dialog `beforeunload` browser (dibatalkan agar tetap di halaman) dan pemindahan fokus antar tab browser disediakan tim FE; pemutusan Bluetooth semua reader lewat simulator.

## Test Steps

### TC-AC-ACTS-335: Back fisik saat sesi aktif menampilkan modal `RFID Scan Stopped`

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Klik `[Audit TAG]` di toolbar Tab Available
3. Klik `[Start Scan]`
4. Scan 1 unit
5. Tekan Back browser
6. Verifikasi modal `RFID Scan Stopped` dengan `Leave Page` dan `Continue Scan`
7. Klik `Leave Page`
8. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
9. Klik `[Audit TAG]` di toolbar Tab Available
10. Verifikasi `Leave Page` membuang baris Verified: seluruh baris `Not Scanned`
11. Klik `✕` pada popup untuk menutup popup Idle

### TC-AC-ACTS-336: Semua reader putus di tengah sesi menghentikan sesi otomatis

12. Klik `[Audit TAG]` di toolbar Tab Available
13. Klik `[Start Scan]`
14. Scan 1 unit
15. Putuskan Bluetooth semua reader
16. Verifikasi sesi berhenti otomatis
17. Verifikasi Sync Panel terbuka
18. Verifikasi hasil Verified sejauh ini tidak hilang (unit yang discan tetap `✓ Verified`)
19. Tutup Sync Panel
20. Klik `✕` pada popup
21. Verifikasi dialog Unsaved Changes `You have unsaved changes. Are you sure you want to leave?` dengan `[Cancel]` dan `[Leave]`
22. Klik `[Leave]`

### TC-AC-ACTS-799: Berpindah tab browser saat sesi scan aktif memunculkan modal saat kembali

23. Hubungkan kembali reader RFID (simulator)
24. Klik `[Audit TAG]` di toolbar Tab Available
25. Klik `[Start Scan]`
26. Pindah ke tab browser lain
27. Kembali ke tab ini
28. Verifikasi setelah tab ini kembali aktif, modal `RFID Scan Stopped` tampil dengan body `The scan process was interrupted because you left this window.` dan tombol `[Leave Page]` serta `[Continue Scan]`
29. Klik `Leave Page`

### TC-AC-ACTS-800: Reload atau tutup tab saat sesi scan aktif memunculkan konfirmasi browser

30. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
31. Klik `[Audit TAG]` di toolbar Tab Available
32. Klik `[Start Scan]`
33. Tekan F5
34. Verifikasi konfirmasi bawaan browser muncul (teks ditentukan browser)
35. Batalkan dialog `beforeunload` agar tetap di halaman
36. Klik `[Stop]`
37. Klik `✕` pada popup untuk menutup popup Idle

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (d, simulator reader) dengan satu dataset; tiap blok TC berdiri sendiri dan tidak kehilangan makna bila blok lain gagal. Langkah penutup popup (`✕`, dialog Unsaved Changes, `[Leave]`) diulang per blok.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), pembukaan ulang Detail SKU sesudah `Leave Page`, "Hubungkan kembali reader RFID", "Tutup Sync Panel", pembatalan dialog `beforeunload`, `[Stop]`, dan penutup popup (pemulihan state, S-09).
- Temuan untuk QA:
  - Email akun Total Control memakai Pre-setup #1 (`totalControl_automated_{namaCompany}`); suite Admin Console lain mendaftarkan `AC_TC_PASSWORD` untuk `totalControlAdminConsole_automated_{namaCompany}`. Kesamaan akun perlu dikonfirmasi tim FE.
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - Langkah Uji TC-AC-ACTS-335 nomor 1-3 tidak men-scan unit sebelum Back, sedangkan Expected menyatakan `Leave Page` membuang baris Verified; spec menambah scan satu unit sebelum Back dan membuka ulang Popup Audit untuk mengasersinya.
  - TC-AC-ACTS-799 Expected menyatakan modal muncul "saat tab kembali aktif, bukan saat berpindah"; keadaan saat tab tidak aktif tidak dapat diamati dari tab latar, sehingga hanya kemunculan modal saat kembali yang diasersi.
  - TC-AC-ACTS-800 menyatakan teks konfirmasi ditentukan browser; spec mengasersi kemunculan konfirmasi saja dan membatalkannya (kemampuan penanganan `beforeunload` disediakan tim FE).
  - Pembagian TC lintas spec: TC-AC-ACTS-332, 333, dan 334 (menutup popup) ada di spec 128.
