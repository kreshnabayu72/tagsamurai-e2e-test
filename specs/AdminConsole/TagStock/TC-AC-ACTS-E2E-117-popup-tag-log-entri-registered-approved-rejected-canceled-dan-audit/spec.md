---
id: TC-AC-ACTS-E2E-117-popup-tag-log-entri-registered-approved-rejected-canceled-dan-audit
title: "Popup TAG Log Entri: Registered (Add Stock Scan, Import GPS, Bypass E2a), Waiting lalu Approved, Activated, Unit Ditolak dan Canceled Tanpa Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACTS-960
  - TC-AC-ACTS-961
  - TC-AC-ACTS-962
  - TC-AC-ACTS-963
  - TC-AC-ACTS-964
  - TC-AC-ACTS-965
  - TC-AC-ACTS-966
coverage:
  web: automated
---

# Popup TAG Log Entri: Registered (Add Stock Scan, Import GPS, Bypass E2a), Waiting lalu Approved, Activated, Unit Ditolak dan Canceled Tanpa Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlAdminConsole_automated_{namaCompany}@qwertysystem.net` (Pre-setup #1), password dari `Spectra.env.AC_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Total Control).
- Halaman awal: Detail SKU `RFID-ASSET-CORE-R5` > Tab Available (dibuka langkah 1).
- Hook suite (flag Guided Tooltip, sesi API aktor, simulator reader, fixture BE, jam server dan jam browser, pemulihan state global) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya kecuali yang tertulis di Prerequisites ini.
- Data milik spec disiapkan seeding fixture BE (disediakan tim FE/BE; keadaan dibentuk sebelum spec dan dipakai sebagai precondition TC, tidak diasersi): unit baru hasil Add Stock scan dengan Handheld Reader `HR-RFID-01` (TC-AC-ACTS-960; Data Pre-setup #25), unit GPS hasil Import pada `GPS-TRACK-CORE-G3` (TC-AC-ACTS-961), unit hasil bypass E2a (TC-AC-ACTS-962), unit hasil Approve Register Duplicate dengan Approval Note `OK, valid` (TC-AC-ACTS-963), unit In Use hasil Approve Activation Collision dari Client `PT Maju Bersama` (TC-AC-ACTS-964), Subject Register Duplicate yang sudah di-reject (TC-AC-ACTS-965), dan unit Waiting terkait Activation Collision yang tagnya dihapus Client (TC-AC-ACTS-966). Fixture `fixtures/tag-stock.json` belum ada dan dibuat di tahap script.
- Pelaku Client yang menghapus tag Waiting (TC-AC-ACTS-966) memakai sesi API aktor, disediakan tim FE/BE; akun tidak ada di Pre-setup TC. Spec ini hanya membaca data kecuali pemicu tersebut.
- Env var password akun aktor: `Spectra.env.AC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`). Spec ini menyiapkan dan memulihkan datanya sendiri dan tidak bergantung pada hasil spec lain.

## Test Steps

### TC-AC-ACTS-960: Entri Registered dari Add Stock Scan memuat Source dan Hardware

1. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available
2. Klik (⋯) > `TAG Log` pada unit hasil scan Add Stock dengan `HR-RFID-01`
3. Verifikasi entri berjudul `TAG Registered by [pelaku admin yang Submit]` dengan Description `Source: Scan` dan `Hardware: HR-RFID-01`
4. Tutup popup lewat (X)

### TC-AC-ACTS-961: Entri Registered dari Import GPS memuat Source Import tanpa Hardware

5. Buka Detail SKU `GPS-TRACK-CORE-G3` > Tab Available, klik (⋯) > `TAG Log` pada unit GPS hasil Import
6. Verifikasi entri berjudul `TAG Registered by [pelaku admin yang Submit]` dengan Description `Source: Import`
7. Verifikasi tidak ada baris `Hardware` pada Description entri itu
8. Tutup popup lewat (X)

### TC-AC-ACTS-962: Entri Registered dari bypass E2a memuat Approval Bypass dengan PIC requester

9. Buka Detail SKU `RFID-ASSET-CORE-R5` > Tab Available, klik (⋯) > `TAG Log` pada unit hasil bypass
10. Verifikasi entri berjudul `TAG Registered by [pelaku requester]` dengan Description `Approval: Bypass`
11. Verifikasi tidak ada entri `TAG Sent for Approval by ...` maupun `TAG Approved by ...`
12. Tutup popup lewat (X)

### TC-AC-ACTS-963: Register Duplicate yang di-approve menghasilkan Waiting for Approval lalu Approved dengan Approval Note

13. Klik (⋯) > `TAG Log` pada unit hasil Approve Register Duplicate
14. Verifikasi entri `TAG Sent for Approval by [pelaku admin yang Submit]` dengan Description `Source: Scan`
15. Verifikasi entri `TAG Approved by [pelaku approver]` dengan Description `Approval Note: OK, valid`
16. Verifikasi urutan tampil `TAG Approved by ...` di atas `TAG Sent for Approval by ...`
17. Tutup popup lewat (X)

### TC-AC-ACTS-964: Activation Collision yang di-approve menghasilkan Waiting for Approval, Approved, dan Activated

18. Buka Tab In Use, klik (⋯) > `TAG Log` pada unit hasil Activation Collision yang di-approve
19. Verifikasi entri `TAG Sent for Approval by [pelaku user Client pemohon]` dengan Description `Source: Activate TAG`
20. Verifikasi entri `TAG Approved by [pelaku approver]` dengan Description `Approval Note`
21. Verifikasi entri `TAG Activated by [pelaku user Client pemohon]` dengan Description `Client: PT Maju Bersama` pada waktu yang sama dengan entri Approved
22. Tutup popup lewat (X)

### TC-AC-ACTS-965: Unit yang ditolak tidak tampil di tab mana pun sehingga tidak punya TAG Log

23. Buka Tab Available dan cari unit hasil Reject
24. Verifikasi Tab Available memuat sedikitnya satu baris
25. Verifikasi unit hasil Reject tidak tampil di Tab Available
26. Buka Tab In Use dan cari unit hasil Reject
27. Verifikasi Tab In Use memuat sedikitnya satu baris
28. Verifikasi unit hasil Reject tidak tampil di Tab In Use
29. Buka Approvals > TAG Stock > Tab History
30. Verifikasi keputusan Reject terlihat di Tab History

### TC-AC-ACTS-966: Unit Activation Collision yang dibatalkan otomatis tidak punya TAG Log

31. Client menghapus tag Waiting di Global Settings hingga tersimpan (sesi API aktor)
32. Muat ulang Detail SKU `RFID-ASSET-CORE-R5` > Tab Available setiap 5 detik sampai event diproses (batas tunggu 2 menit)
33. Verifikasi Tab Available memuat sedikitnya satu baris
34. Verifikasi unit Waiting terkait tidak tampil di Tab Available
35. Buka Tab In Use
36. Verifikasi Tab In Use memuat sedikitnya satu baris
37. Verifikasi unit Waiting terkait tidak tampil di Tab In Use

## Notes

- Mode: FE+BE. Spec ini melewati sekitar 35 langkah (37 langkah); alasan: semua blok satu halaman sumber (Popup TAG Log) dan satu dataset, hanya membaca data, dan tiap blok TC berdiri sendiri sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna.
- Langkah penghubung tanpa Verifikasi (S-03): menutup popup lewat (X) sebelum TC berikutnya (S-09), membuka Detail SKU dan tab, serta memuat ulang tiap 5 detik memakai idiom baku "polling worker commit" (bagian 6, batas tunggu 2 menit). Pelaku Client ditulis "hingga tersimpan" (R-20).
- Absence entri dan unit pada TC-AC-ACTS-962, TC-AC-ACTS-965, dan TC-AC-ACTS-966 didahului anchor positif (entri Registered tampil; baris lain pada tabel yang sama; 8b butir 2).
- Temuan untuk QA:
  - TC-AC-ACTS-960 sampai TC-AC-ACTS-964 menyebut "[pelaku ...]" sebagai nilai dinamis; spec mengasersi pola judul dengan pelaku dari seeding.
  - TC-AC-ACTS-966 menyebut "TAG Log-nya ikut terhapus" yang tidak teramati dari UI selain unit tidak tampil; spec mengasersi unit tidak tampil di tab mana pun.
  - TC-AC-ACTS-965 menyebut "log aktivitas" selain Tab History; spec mengasersi Tab History saja.
