---
id: TC-AC-ACTS-E2E-151-absence-log-delete-by-scan-tanpa-penghapusan-usage-event-dan-status-synced
title: "Absence Log: Delete by Scan Tanpa Penghapusan Tanpa Log dan Usage Event, Usage Event Tidak Tercatat tanpa Reader dan untuk Aksi Lain, serta Event Condition No-Op Tanpa Status Synced"
priority: Medium
caseType: Negative
status: draft
sourceTc:
  - TC-AC-ACTS-859
  - TC-AC-ACTS-863
  - TC-AC-ACTS-864
  - TC-AC-ACTS-865
  - TC-AC-ACTS-977
coverage:
  web: automated
---

# Absence Log: Delete by Scan Tanpa Penghapusan Tanpa Log dan Usage Event, Usage Event Tidak Tercatat tanpa Reader dan untuk Aksi Lain, serta Event Condition No-Op Tanpa Status Synced

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini sebagai Total Control; halaman dibuka hook `beforeEach` suite (TAG > Stock). Hook `after` memulihkan sesi ke akun default suite (Total Control).
- Flag Guided Tooltip `guided_tooltip_seen_ac-tag-stock` disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Dinamis (Tabel Data Uji Dinamis #5) pada SKU `RFID-ASSET-CORE-R5` (Pre-setup #12): unit uji hapus milik spec, di-seed di hook `before` (idempoten) dan dipulihkan fixture BE di hook `after`: Available U1 (`TAG-4F7K2XQ9`), U2, U3; Damaged/Missing U4; Combined C1; Existing Record Subject Register Duplicate pending P1; Waiting for Approval W1 (tidak tampil di Tab Available, Subject ada di Approvals); In Use I1; pada SKU `NFC-CARD-BETA-N2` (Pre-setup #13): Available X1. Identifier unit tetap (tidak bersuffix `{runId}`; S-12): seeding idempoten, pemulihan lewat fixture BE sebelum spec ini, suite serial.
- Data Pre-setup: Handheld Reader `HR-RFID-01` (Pre-setup #25), terdaftar dan terdeteksi di Sync Panel lewat simulator reader USB; Tab Usage dibaca sebagai baseline jumlah baris sebelum aksi (S-12). Reader USB bukan objek uji spec ini, melainkan pembentuk kondisi.
- Kemampuan teknis: Simulator Handheld Reader USB `HR-RFID-01` di Sync Panel (terdeteksi atau tidak terdaftar) dan simulator pemindai RFID disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Simulator pemindai RFID (scan satu per satu, scan beruntun, kode tidak dikenal, pemutusan koneksi) disediakan tim FE (lihat `suite.md`); mekanismenya tidak ditulis di spec.
- Kemampuan teknis: Fixture BE (seeding idempoten dan pemulihan SKU, unit, Subject, saldo Stock Ledger, dan sesi log) serta pembacaan state BE yang tidak terlihat di UI disediakan tim FE/BE tanpa endpoint karangan (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini memakai simulator reader bersama.
- Data tambahan: SKU GPS `GPS-TRACK-CORE-G3` (Pre-setup #15) dan dua IMEI baru dari Data Dinamis #2 (`356938035643809` dan `356938035643810`) untuk Import GPS (TC-AC-ACTS-864); Subject Register Duplicate pending untuk Approve (TC-AC-ACTS-864); dua TAG RFID baru dan perangkat scan yang tidak terdaftar sebagai Handheld Reader untuk TC-AC-ACTS-863; event Condition untuk unit Available (TC-AC-ACTS-977) lewat fixture BE.
- Kelas g (absence log): pemicu (Delete by Scan tertolak, Add Stock tanpa reader terdaftar, aksi non-sesi-reader, event Condition) hanya membentuk kondisi yang diasersi tidak tercatat dan bukan objek uji (P-5 butir a); tiap TC memakai baseline sendiri (S-12).

## Test Steps

### TC-AC-ACTS-859: Sesi Delete by Scan tanpa penghapusan berhasil tidak menulis entri log

1. Klik row action `Detail` pada SKU `RFID-ASSET-CORE-R5` di Stock List, lalu buka Tab Available
2. Buka Activity Log, System Log user aktor, dan modal Event Log SKU (Tab Add Stock), lalu catat baseline jumlah entri dan baris, lalu tutup modal Event Log
3. Kembali ke Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
4. Klik `[Delete by Scan]` dan scan satu kode tidak dikenal
5. Verifikasi toast error `Error, can't recognize TAG.` tampil
6. Scan unit Waiting for Approval W1
7. Verifikasi toast error `Error, this TAG is waiting for approval and can't be deleted.` tampil menggantikan toast sebelumnya (satu slot toast aktif)
8. Klik `[Stop]`
9. Tunggu aksi selesai (sesi Delete by Scan tertutup)
10. Buka Activity Log, System Log user aktor, dan modal Event Log SKU (Tab Add Stock)
11. Verifikasi jumlah entri Activity Log dan System Log sama dengan baseline (tidak ada entri `Delete Stock` maupun `Delete by Scan` baru)
12. Verifikasi jumlah baris Event Log sama dengan baseline (tidak ada baris baru)
13. Tutup modal Event Log
14. Tunggu toast lama hilang

### TC-AC-ACTS-863: Usage Event tidak tercatat bila tidak ada Handheld Reader yang terdeteksi di Sync Panel

15. Buka Hardware > Handheld Reader > Detail `HR-RFID-01` > Tab Usage, lalu catat baseline jumlah baris
16. Gunakan perangkat scan yang tidak terdaftar sebagai Handheld Reader di Sync Panel (simulator), lalu buka halaman Add Stock SKU `RFID-ASSET-CORE-R5`
17. Scan 2 TAG baru, klik `[Stop]`, klik `[Submit]`
18. Verifikasi Submit berhasil seperti biasa (toast `Success, TAG has been registered.`)
19. Buka Hardware > Handheld Reader > Detail `HR-RFID-01` > Tab Usage
20. Verifikasi Tab Usage memuat baris seeding sebagai pembanding tampil
21. Verifikasi jumlah baris Tab Usage sama dengan baseline (tidak bertambah)

### TC-AC-ACTS-864: Usage Event tidak tercatat untuk Import GPS, hapus manual, Bulk Delete, dan Approve

22. Reset dataset: unit Available U1 sampai U3 pada SKU RFID dan Subject Register Duplicate pending lewat fixture BE; hubungkan kembali `HR-RFID-01` di Sync Panel (simulator)
23. Buka Hardware > Handheld Reader > Detail `HR-RFID-01` > Tab Usage, lalu catat baseline jumlah baris
24. Import 2 IMEI baru ke halaman Add Stock SKU `GPS-TRACK-CORE-G3` dan klik `[Submit]`
25. Verifikasi Import GPS berhasil (toast sukses tampil)
26. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available, klik (⋯) pada U1, klik `Delete`, lalu klik `[Delete]`
27. Verifikasi hapus manual berhasil (toast sukses tampil)
28. Centang U2 dan U3, pilih Bulk Action > `Delete`, lalu klik `[Delete]`
29. Verifikasi Bulk Delete berhasil (toast sukses tampil)
30. Buka Approvals > TAG Stock > Tab Active, klik `Review` pada Subject Register Duplicate pending, lalu Approve
31. Verifikasi Approve berhasil (Subject berpindah dari Tab Active)
32. Buka Hardware > Handheld Reader > Detail `HR-RFID-01` > Tab Usage
33. Verifikasi Tab Usage memuat baris seeding sebagai pembanding tampil
34. Verifikasi jumlah baris Tab Usage sama dengan baseline (tidak bertambah akibat keempat aksi)

### TC-AC-ACTS-865: Sesi Delete by Scan tanpa penghapusan berhasil tidak menulis Usage Event

35. Reset dataset: unit Waiting for Approval W1 lewat fixture BE
36. Buka Hardware > Handheld Reader > Detail `HR-RFID-01` > Tab Usage, lalu catat baseline jumlah baris
37. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available, klik `[Delete by Scan]`, scan W1 dan satu kode tidak dikenal
38. Verifikasi toast error penolakan tampil (satu slot toast aktif; toast scan terakhir menggantikan toast sebelumnya)
39. Klik `[Stop]`
40. Tunggu aksi selesai (sesi Delete by Scan tertutup)
41. Buka Hardware > Handheld Reader > Detail `HR-RFID-01` > Tab Usage
42. Verifikasi jumlah baris Tab Usage sama dengan baseline (tidak bertambah)

### TC-AC-ACTS-977: Event Condition yang di-skip (no-op) tidak menulis entri `Status Synced`

43. Reset dataset: U1 sampai U4 lewat fixture BE
44. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available, klik (⋯) pada unit Available U2, klik `TAG Log`, catat baseline jumlah entri `TAG Status Synced by System`, lalu tutup Popup TAG Log
45. Kirim event Condition untuk unit U2 (Available, bukan In Use) lewat fixture BE hingga event diproses
46. Klik (⋯) pada unit U2, lalu klik `TAG Log`
47. Verifikasi Popup TAG Log memuat entri registrasi unit tampil
48. Verifikasi jumlah entri `TAG Status Synced by System` sama dengan baseline (tidak ada entri baru)

## Notes

- Alasan di atas smell ~35 langkah: seluruh blok satu kelas harness (g, absence log; pemicu kelas lain sesuai P-5 butir a) dan satu dataset; tiap blok TC memakai baseline sendiri, berdiri sendiri, dan tidak kehilangan makna bila blok lain gagal.
- Langkah penghubung (S-03): langkah 1 (membuka Detail SKU), pencatatan baseline dan navigasi ke Activity Log, System Log, Event Log, Tab Usage, dan Popup TAG Log, "Reset dataset", hubungkan kembali `HR-RFID-01`, dan "Tunggu toast lama hilang" (pemulihan state, S-09). Spec absence ini memuat aksi nyata untuk TC-AC-ACTS-859, 863, 864, 865, dan 977. Langkah "Tutup modal Event Log" menutup modal sebelum pindah surface atau ganti akun (pemulihan state, S-09).
- Langkah penghubung (S-03, 8b butir 8): "Tunggu aksi selesai (sesi Delete by Scan tertutup)" sesudah `[Stop]` menunggu sesi Delete by Scan tertutup sebelum log atau surface lain dibuka; tidak ada `Verifikasi` karena hanya pemulihan state (S-09).
- Pembagian TC lintas spec: TC-AC-ACTS-860, 861, 862, 866, dan 867 (Usage Event tercatat dan kegagalan menulis) ada di spec 152.
- Temuan untuk QA:
  - Cara simulasi reader (scan, pemutusan koneksi) tidak didefinisikan di TC, PRD, atau LLD; spec menuliskannya sebagai kemampuan yang disediakan tim FE tanpa mekanisme karangan.
  - Identifier dan hitungan tetap (Data Uji Dinamis) dipakai ulang lintas TC dan tidak dapat bersuffix per run; kebenaran hitungan hanya terjamin bila fixture BE mereset dataset sebelum spec.
  - TC-AC-ACTS-863 menyebut "perangkat scan yang dipakai tidak terdaftar" tanpa cara membentuknya; spec memakai simulator perangkat scan yang disediakan tim FE.
  - Langkah Uji TC-AC-ACTS-864 nomor 1 tidak menyebut SKU dan IMEI; spec memakai SKU GPS dan dua IMEI baru dari Data Dinamis #2. Langkah Uji nomor 4 "Approve Subject Register Duplicate" tidak menyebut jalur; spec memakai dialog Review di Approvals > TAG Stock > Tab Active.
  - TC-AC-ACTS-977 tidak menyebut cara mengirim event Condition dan format entri TAG Log; spec memakai pemicu yang disediakan tim FE/BE dan nama entri `TAG Status Synced by System` dari TC.
