---
id: TC-AC-ACTS-E2E-150-absence-log-audit-tanpa-perubahan-dan-delete-tanpa-entri-event-log-tag-log
title: "Absence Log: Audit Tanpa Perubahan Tidak Menulis Log, Tanpa Baris Event Log, Tanpa Entri Audit TAG Log, dan Bulk Delete Tanpa Penghapusan Tanpa Baris Event Log"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-670
  - TC-AC-ACTS-930
  - TC-AC-ACTS-947
  - TC-AC-ACTS-970
  - TC-AC-ACTS-971
coverage:
  web: automated
---

# Absence Log: Audit Tanpa Perubahan Tidak Menulis Log, Tanpa Baris Event Log, Tanpa Entri Audit TAG Log, dan Bulk Delete Tanpa Penghapusan Tanpa Baris Event Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup: SKU `RFID-ASSET-CORE-R5` (Pre-setup #12; Device Name `RFID Asset Tag`, Brand `Core`, Model `R5`, Object TAG). Unit uji milik spec di-seed di hook `before` pada SKU itu (idempoten) dan dipulihkan fixture BE di hook `after`: 2 unit Available (A, B) dan 2 unit Damaged/Missing (C, D), seluruhnya eligible Audit. Aksi spec mengubah Last Updated SKU Pre-setup; efeknya dipulihkan fixture BE.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Sesi API aktor (login API password, token tidak dihitung sebagai sesi web) untuk pelaku kedua yang hanya memicu perubahan state, disediakan tim BE/FE (lihat `suite.md`).
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Data per blok TC (di-reset fixture BE): TC-AC-ACTS-670, 930, dan 970 memakai seluruh unit eligible berstatus Available (4 unit); TC-AC-ACTS-947 memakai unit Combined C1 dan unit Existing Record Subject pending P1; TC-AC-ACTS-971 memakai unit Available U-aktif yang diaktivasi sesi API sebelum Submit. Modal Event Log Tab Audit TAG dan Tab Add Stock memuat sedikitnya satu baris seeding sebagai pembanding (anchor).
- Kelas g (absence log): pemicu (Audit tanpa perubahan, Bulk Delete dilewati, aktivasi oleh sesi lain) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (P-5 butir a); tiap TC memakai baseline sendiri (S-12).

## Test Steps

### TC-AC-ACTS-670: Audit Submit tanpa perubahan tidak menulis log

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Buka User Detail > System Log dan Activity Log, lalu catat baseline jumlah entri System Log dan Activity Log
3. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
4. Klik `[Audit TAG]`, klik `[Start Scan]`, scan semua unit (semua sudah Available), klik `[Stop]`
5. Klik `[Submit]`
6. Verifikasi toast netral `No changes to save.` tampil
7. Buka User Detail > System Log dan Activity Log
8. Verifikasi jumlah entri System Log dan Activity Log sama dengan baseline (tidak ada entri baru)
9. Tunggu toast lama hilang

### TC-AC-ACTS-930: Audit Submit tanpa perubahan status (T-20) tidak menulis baris Event Log

10. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available, lalu klik `[Event Log]` dan buka tab `Audit TAG`
11. Catat baseline jumlah baris Tab Audit TAG, lalu tutup modal Event Log
12. Klik `[Audit TAG]`, klik `[Start Scan]`, scan semua unit, klik `[Stop]`
13. Klik `[Submit]`
14. Verifikasi toast netral `No changes to save.` tampil
15. Klik `[Event Log]` dan buka tab `Audit TAG`
16. Verifikasi Tab Audit TAG memuat baris seeding sebagai pembanding tampil
17. Verifikasi jumlah baris Tab Audit TAG sama dengan baseline (tidak ada baris baru)
18. Tutup modal Event Log
19. Tunggu toast lama hilang

### TC-AC-ACTS-947: Bulk Delete yang tidak menghapus satu unit pun tidak menulis baris Event Log

20. Klik `[Event Log]` dan buka tab `Add Stock`, catat baseline jumlah baris, lalu tutup modal Event Log
21. Centang C1 dan P1, pilih Bulk Action > `Delete`, klik `[Delete]`
22. Verifikasi toast error `Error, failed to delete units.` (T-30) tampil
23. Klik `[Event Log]` dan buka tab `Add Stock`
24. Verifikasi Tab Add Stock memuat baris seeding sebagai pembanding tampil
25. Verifikasi jumlah baris Tab Add Stock sama dengan baseline (tidak ada baris baru)
26. Tutup modal Event Log
27. Tunggu toast lama hilang

### TC-AC-ACTS-970: Audit tanpa perubahan status (T-20) tidak menulis entri `Audit` pada unit mana pun

28. Klik (⋯) pada unit A, lalu klik `TAG Log`, catat baseline jumlah entri `TAG Audited by ...`, lalu tutup Popup TAG Log
29. Klik `[Audit TAG]`, klik `[Start Scan]`, scan semua unit, klik `[Stop]`
30. Klik `[Submit]`
31. Verifikasi toast netral `No changes to save.` tampil
32. Klik (⋯) pada unit A, lalu klik `TAG Log`
33. Verifikasi Popup TAG Log memuat entri registrasi unit A tampil
34. Verifikasi jumlah entri `TAG Audited by ...` pada unit A sama dengan baseline (tidak ada entri baru)
35. Tutup Popup TAG Log
36. Tunggu toast lama hilang

### TC-AC-ACTS-971: Unit yang dilewati karena status berubah di tengah sesi Audit tidak mendapat entri `Audit`

37. Reset dataset: unit Available U-aktif lewat fixture BE
38. Klik `[Audit TAG]`, klik `[Start Scan]`, scan U-aktif, klik `[Stop]`
39. Sesi API mengaktivasi U-aktif hingga status In Use tersimpan
40. Klik `[Submit]`
41. Tunggu aksi selesai (Popup Audit TAG tertutup)
42. Buka Tab In Use, klik (⋯) pada U-aktif, lalu klik `TAG Log`
43. Verifikasi Popup TAG Log memuat entri `TAG Activated by ...` untuk U-aktif tampil
44. Verifikasi jumlah entri `TAG Audited by ...` dari sesi itu pada U-aktif adalah 0 (tidak ada entri `Audit`)

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (g, absence log; pemicu kelas lain sesuai P-5 butir a) dan satu dataset; tiap blok TC memakai baseline sendiri, berdiri sendiri, dan tidak kehilangan makna bila blok lain gagal.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), pencatatan baseline dan navigasi ke User Detail, modal Event Log, dan Popup TAG Log, "Reset dataset", dan "Tunggu toast lama hilang" (pemulihan state, S-09). Spec absence ini memuat aksi nyata untuk TC-AC-ACTS-670, 930, 947, 970, dan 971; rujukan di spec asal (spec 126, 148, 131, dan 164) dicatat di Notes mereka. Langkah "Tunggu aksi selesai" ditambahkan sebelum pindah surface atau ganti akun sesudah aksi yang hasilnya tidak diasersi langsung (bagian 8b butir 8).
- Pembagian TC lintas spec: Expected "tanpa log" pada TC-AC-ACTS-320, 767, dan 712 diasersi sebagai jumlah entri sama dengan baseline di spec 126, 131, dan 164; asersi absence murni ada di spec ini.
- Temuan untuk QA:
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - TC-AC-ACTS-670 menulis "0 entri baru di Activity Log, System Log, Activity Log" (Activity Log disebut dua kali); spec mengasersi System Log dan Activity Log.
  - TC-AC-ACTS-947 menyebut toast `T-30` tanpa teks; spec memakai teks T-30 dari TC-AC-ACTS-848 (`Error, failed to delete units.`).
  - TC-AC-ACTS-970 dan 971 tidak menyebut akses ke TAG Log (row action `TAG Log` di Tab Available atau Tab In Use); spec memakai row action `TAG Log` (TC-AC-ACTS-357 dan 364 menyebut aksi itu).
  - TC-AC-ACTS-971 butir "hanya `TAG Activated by ...`" dan 970 menyebut entri `TAG Audited by ...`; format entri TAG Log tidak didefinisikan di TC lain.
