---
id: TC-AC-ACTS-E2E-104-approvals-duplicate-activation-collision-dibatalkan-event-delete-tag-dan-no-op
title: "Approvals Duplicate: Activation Collision Canceled Otomatis oleh Event Delete TAG, Event Diterima Ulang No-Op, Register Duplicate Tanpa Pembatalan, dan Tanpa Timeout"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-ACTS-292
  - TC-AC-ACTS-304
  - TC-AC-ACTS-305
  - TC-AC-ACTS-306
  - TC-AC-ACTS-307
  - TC-AC-ACTS-308
coverage:
  web: automated
---

# Approvals Duplicate: Activation Collision Canceled Otomatis oleh Event Delete TAG, Event Diterima Ulang No-Op, Register Duplicate Tanpa Pembatalan, dan Tanpa Timeout

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControl_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Kelas d ringan: time-travel Subject (TC-AC-ACTS-308) lewat fixture BE yang menggeser timestamp pembuatan Subject 30 hari ke belakang (disediakan tim FE/BE); tidak ada pergeseran jam server atau jam browser.
- Data Subject disiapkan seeding fixture BE (disediakan tim FE/BE): Subject Activation Collision pending dengan tag Client yang dapat dihapus di Global Settings dan event Delete TAG yang dapat ditahan atau dikirim ulang (TC-AC-ACTS-292, TC-AC-ACTS-304, TC-AC-ACTS-305), Subject Register Duplicate pending (TC-AC-ACTS-306, TC-AC-ACTS-308), dan unit Waiting for Approval hasil Register Duplicate (TC-AC-ACTS-307). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Pelaku Client di Global Settings (hapus tag, aktivasi tag) memakai sesi API aktor, disediakan tim FE/BE; akun tidak ada di Pre-setup TC. Waktu hapus tag (TC-AC-ACTS-304) dicatat dari respons sesi API; jam server dan jam browser sinkron.
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-292: Submit Approve atau Reject saat tag Activation Collision sudah dihapus di Global Settings tetapi event belum diproses

1. Tahan pemrosesan event Delete TAG (fixture BE)
2. Client menghapus tag di Global Settings hingga tersimpan (sesi API aktor)
3. Buka Approvals > TAG Stock > Tab Active, klik `Review` pada Subject Activation Collision
4. Pilih Approve, klik `[Submit]`
5. Verifikasi server menolak dengan dialog nested `Approval cannot be made` dengan teks `This request has already been resolved.`
6. Klik `[Close]`
7. Verifikasi `[Close]` menutup kedua dialog
8. Verifikasi Subject tetap di Tab Active sampai event diproses
9. Lepas tahanan pemrosesan event Delete TAG

### TC-AC-ACTS-304: Activation Collision otomatis Canceled saat tag dihapus di Global Settings (event diproses)

10. Catat baseline jumlah entri Activity Log dan jumlah baris Event Log SKU
11. Client menghapus tag Waiting di Global Settings hingga tersimpan (sesi API aktor) dan catat waktu hapus
12. Muat ulang Tab Active setiap 5 detik sampai event Delete TAG diproses (batas tunggu 2 menit)
13. Verifikasi Subject keluar dari Tab Active
14. Buka Tab History
15. Verifikasi Subject tampil di Tab History dengan Approval `Canceled`, Approver `—`, dan TAG Code `—`
16. Verifikasi unit Waiting terkait dihapus dan unit existing target collision tidak berubah
17. Buka Activity Log
18. Verifikasi entri `Duplicate Canceled` dengan Modified By `System`
19. Verifikasi Date entri Activity Log sama dengan waktu tag dihapus (toleransi satu menit) dan sama dengan Resolved At baris Tab History
20. Buka modal Event Log SKU
21. Verifikasi Event Log memuat baris pembanding milik SKU itu
22. Verifikasi Event Log tidak memuat baris `Duplicate Canceled` (jumlah baris sama dengan baseline)
23. Tutup modal Event Log

### TC-AC-ACTS-305: Event Delete TAG diterima ulang atau setelah Subject diputuskan menjadi no-op

24. Catat baseline jumlah entri Activity Log
25. Kirim ulang event Delete TAG yang sama (fixture BE)
26. Buka Activity Log dan Approvals > Tab History
27. Verifikasi Subject Canceled tetap berstatus Canceled di Tab History (tidak ada perubahan status)
28. Verifikasi tidak ada entri log baru (jumlah entri Activity Log sama dengan baseline)

### TC-AC-ACTS-306: Register Duplicate tidak punya jalur pembatalan otomatis

29. Client menghapus tag lain di Global Settings hingga tersimpan (sesi API aktor)
30. Muat ulang Tab Active setiap 5 detik sampai event Delete TAG diproses (batas tunggu 2 menit)
31. Verifikasi Subject Register Duplicate tetap pending di Tab Active (tidak Canceled)

### TC-AC-ACTS-307: Activate TAG pada identifier unit Waiting tidak membuat Subject kedua

32. Catat baseline jumlah Subject di Tab Active
33. Client mengaktivasi tag dengan identifier sama dengan unit Waiting di Global Settings hingga tersimpan (sesi API aktor)
34. Buka Approvals > TAG Stock > Tab Active
35. Verifikasi tidak ada Subject Activation Collision baru (jumlah Subject sama dengan baseline)
36. Verifikasi Subject Register Duplicate yang pending tidak berubah

### TC-AC-ACTS-308: Subject tidak memiliki timeout atau peringatan H-24

37. Geser timestamp pembuatan Subject pending 30 hari ke belakang (fixture BE)
38. Muat ulang Tab Active
39. Buka Notification Center
40. Verifikasi Subject tetap pending di Tab Active tanpa auto-cancel
41. Verifikasi Notification Center tampil tanpa notifikasi peringatan 24 jam

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (41 langkah); alasan: semua blok satu kelas harness (kelas d ringan, event Delete TAG dan time-travel Subject) dan satu dataset Subject, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- P-1 (state berat): TC-AC-ACTS-304 memuat asersi tidak adanya baris Event Log `Duplicate Canceled` dengan baseline karena state Canceled baru dibangun langkah sebelumnya; ini asersi jumlah, bukan kelas g.
- Langkah penghubung tanpa Verifikasi (S-03): mencatat baseline (S-12), menahan dan melepas pemrosesan event, membuka layar, dan memuat ulang Tab Active tiap 5 detik memakai idiom baku "polling worker commit" (bagian 6, batas tunggu 2 menit). Pelaku Client lewat sesi API aktor ditulis "hingga tersimpan" (R-20). Langkah "Tutup modal Event Log" menutup modal sebelum pindah surface atau ganti akun (pemulihan state, S-09).
- Absence pada TC-AC-ACTS-308 didahului anchor positif (Subject tetap tampil di Tab Active; Notification Center tampil); pergeseran timestamp memakai fixture BE, bukan jam server.
- Temuan untuk QA:
  - TC-AC-ACTS-308 menyatakan "timestamp pembuatan digeser 30 hari (fixture)" tanpa mekanisme; spec menuliskannya sebagai kemampuan fixture BE.
  - TC-AC-ACTS-292 menyebut "event belum diproses" tanpa cara menahan event; disediakan tim FE/BE.
  - TC-AC-ACTS-304 dan TC-AC-ACTS-305 menyebut "Client menghapus tag" tanpa akun Client.
